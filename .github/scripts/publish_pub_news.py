#!/usr/bin/env python3
"""Generate a bilingual Jekyll news post from a Pub News Issue Form event."""

from __future__ import annotations

import argparse
import html
import io
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, NoReturn

import yaml
from PIL import Image, ImageOps


FIELD_LABELS = {
    "会议 / 期刊": "venue",
    "年份": "year",
    "论文条目": "papers",
    "新闻封面": "cover",
}

ALLOWED_IMAGE_HOSTS = {
    "github.com",
    "user-images.githubusercontent.com",
    "objects.githubusercontent.com",
    "raw.githubusercontent.com",
    "github-production-user-asset-6210df.s3.amazonaws.com",
}

MAX_DOWNLOAD_BYTES = 30 * 1024 * 1024
NEWS_COVER_RATIO = 8 / 5
NEWS_COVER_MAX_WIDTH = 1200
CHINA_STANDARD_TIME = timezone(timedelta(hours=8))


@dataclass(frozen=True)
class Paper:
    title: str
    link: str
    summary_zh: str
    summary_en: str


def fail(message: str) -> NoReturn:
    raise ValueError(message)


def clean_inline(value: Any, field: str) -> str:
    if value is None:
        fail(f"缺少字段：{field}")
    text = " ".join(str(value).replace("\r", "\n").split())
    if not text:
        fail(f"字段不能为空：{field}")
    return text


def parse_issue_sections(body: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    matches = list(re.finditer(r"(?m)^###\s+(.+?)\s*$", body or ""))
    for index, match in enumerate(matches):
        label = match.group(1).strip()
        key = FIELD_LABELS.get(label)
        if not key:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        value = body[match.end() : end].strip()
        if value == "_No response_":
            value = ""
        sections[key] = value

    missing = [label for label, key in FIELD_LABELS.items() if not sections.get(key)]
    if missing:
        fail("Issue Form 缺少必填项：" + "、".join(missing))
    return sections


def strip_code_fence(value: str) -> str:
    match = re.fullmatch(r"```(?:yaml|yml)?\s*\n([\s\S]*?)\n```", value.strip())
    return match.group(1) if match else value.strip()


def validate_link(value: Any, field: str) -> str:
    link = clean_inline(value, field)
    parsed = urllib.parse.urlparse(link)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        fail(f"{field} 必须是完整的 http/https 地址：{link}")
    return link


def parse_papers(value: str) -> list[Paper]:
    try:
        data = yaml.safe_load(strip_code_fence(value))
    except yaml.YAMLError as error:
        fail(f"论文条目不是有效的 YAML：{error}")

    if isinstance(data, dict) and "papers" in data:
        data = data["papers"]
    if not isinstance(data, list) or not data:
        fail("论文条目必须是至少包含一项的 YAML 列表")

    papers: list[Paper] = []
    for index, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            fail(f"第 {index} 个论文条目必须是对象")
        papers.append(
            Paper(
                title=clean_inline(item.get("title"), f"第 {index} 篇题目"),
                link=validate_link(item.get("link"), f"第 {index} 篇链接"),
                summary_zh=clean_inline(
                    item.get("summary_zh"), f"第 {index} 篇中文工作概括"
                ),
                summary_en=clean_inline(
                    item.get("summary_en"), f"第 {index} 篇英文工作概括"
                ),
            )
        )
    return papers


def extract_cover_reference(value: str) -> str:
    text = value.strip()
    html_image_match = re.search(
        r"<img\b[^>]*\bsrc=[\"'](https?://[^\"']+)[\"']", text, re.IGNORECASE
    )
    if html_image_match:
        return html.unescape(html_image_match.group(1))
    image_match = re.search(r"!\[[^\]]*\]\((https?://[^\s)]+)", text)
    if image_match:
        return image_match.group(1)
    link_match = re.search(r"\[[^\]]+\]\((https?://[^\s)]+)", text)
    if link_match:
        return link_match.group(1)
    url_match = re.search(r"https?://\S+", text)
    if url_match:
        return url_match.group(0).rstrip(">).,，。")
    path = text.strip().strip("`").strip()
    if not path:
        fail("字段不能为空：新闻封面")
    return path


def safe_repo_image(repo_root: Path, value: str) -> Path:
    relative = value.replace("\\", "/").lstrip("/")
    if not relative.startswith("images/"):
        fail("仓库图片路径必须位于 images/ 目录下")
    candidate = (repo_root / relative).resolve()
    images_root = (repo_root / "images").resolve()
    if not candidate.is_relative_to(images_root) or not candidate.is_file():
        fail(f"找不到仓库图片：{relative}")
    return candidate


def download_image(url: str, token: str) -> bytes:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_IMAGE_HOSTS:
        allowed = "、".join(sorted(ALLOWED_IMAGE_HOSTS))
        fail(f"封面链接仅允许 GitHub 图片附件域名（{allowed}），也可以填写仓库图片路径")

    headers = {"User-Agent": "BAIST-Lab-Pub-News-Workflow"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        data = response.read(MAX_DOWNLOAD_BYTES + 1)
    if len(data) > MAX_DOWNLOAD_BYTES:
        fail("新闻封面超过 30 MB，请压缩后重新上传")
    return data


def encode_cover(source: bytes | Path, destination: Path) -> bytes:
    file_or_buffer: Any = io.BytesIO(source) if isinstance(source, bytes) else source
    try:
        with Image.open(file_or_buffer) as opened:
            image = ImageOps.exif_transpose(opened)
            has_alpha = "A" in image.getbands()
            image = image.convert("RGBA" if has_alpha else "RGB")

            width, height = image.size
            current_ratio = width / height
            if current_ratio > NEWS_COVER_RATIO:
                crop_width = round(height * NEWS_COVER_RATIO)
                left = (width - crop_width) // 2
                box = (left, 0, left + crop_width, height)
            else:
                crop_height = round(width / NEWS_COVER_RATIO)
                top = (height - crop_height) // 2
                box = (0, top, width, top + crop_height)
            image = image.crop(box)

            output_width = min(NEWS_COVER_MAX_WIDTH, image.width)
            output_height = round(output_width / NEWS_COVER_RATIO)
            if image.size != (output_width, output_height):
                image = image.resize(
                    (output_width, output_height), Image.Resampling.LANCZOS
                )

            destination.parent.mkdir(parents=True, exist_ok=True)
            buffer = io.BytesIO()
            image.save(buffer, "WEBP", quality=85, method=6)
            return buffer.getvalue()
    except (OSError, ValueError) as error:
        fail(f"无法处理新闻封面：{error}")


def write_if_changed(path: Path, content: bytes) -> bool:
    if path.is_file() and path.read_bytes() == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return True


def prepare_cover(
    cover_value: str, repo_root: Path, issue_number: int, post_date: str, token: str
) -> tuple[str, str, bool]:
    reference = extract_cover_reference(cover_value)
    parsed = urllib.parse.urlparse(reference)

    if parsed.scheme in {"http", "https"}:
        source: bytes | Path = download_image(reference, token)
    else:
        source_path = safe_repo_image(repo_root, reference)
        relative_source = source_path.relative_to(repo_root).as_posix()
        if source_path.suffix.lower() == ".webp":
            return relative_source, "", False
        source = source_path

    relative_destination = f"images/news/{post_date}-pub-news-{issue_number}.webp"
    destination = repo_root / relative_destination
    encoded = encode_cover(source, destination)
    changed = write_if_changed(destination, encoded)
    return relative_destination, relative_destination, changed


def quote_zh_titles(papers: list[Paper]) -> str:
    return "、".join(f"“{paper.title}”" for paper in papers)


def quote_en_titles(papers: list[Paper]) -> str:
    quoted = [f"“{paper.title}”" for paper in papers]
    if len(quoted) == 1:
        return quoted[0]
    if len(quoted) == 2:
        return f"{quoted[0]} and {quoted[1]}"
    return ", ".join(quoted[:-1]) + f", and {quoted[-1]}"


def markdown_link(title: str, link: str) -> str:
    safe_title = title.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")
    safe_link = link.replace(")", "%29")
    return f"[{safe_title}]({safe_link})"


def markdown_bold(value: str) -> str:
    safe_value = value.replace("\\", "\\\\").replace("*", "\\*")
    return f"**{safe_value}**"


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def block(name: str, paragraphs: list[str]) -> list[str]:
    lines = [f"  {name}: >-"]
    for paragraph_index, paragraph in enumerate(paragraphs):
        if paragraph_index:
            lines.append("")
        for line in paragraph.splitlines() or [""]:
            lines.append(f"    {line}")
    return lines


def render_post(
    venue: str, year: str, papers: list[Paper], image_path: str, post_date: str
) -> str:
    venue_year = f"{venue} {year}"
    count = len(papers)
    if count == 1:
        title_zh = f"实验室研究成果被 {venue_year} 接收"
        title_en = f"Lab Paper Accepted by {venue_year}"
    else:
        title_zh = f"实验室 {count} 项研究成果被 {venue_year} 接收"
        title_en = f"{count} Lab Papers Accepted by {venue_year}"

    if count == 1:
        announcement_zh = (
            f"近日，实验室研究成果 {quote_zh_titles(papers)} 被 {venue_year} 接收。"
        )
        announcement_en = (
            f"Recently, our research paper {quote_en_titles(papers)} was accepted "
            f"by {venue_year}."
        )
    else:
        announcement_zh = (
            f"近日，实验室 {count} 项研究成果 {quote_zh_titles(papers)} 被 "
            f"{venue_year} 接收。"
        )
        announcement_en = (
            f"Recently, {count} research papers from our lab—"
            f"{quote_en_titles(papers)}—were accepted by {venue_year}."
        )

    detail_zh = [announcement_zh]
    detail_en = [announcement_en]
    for paper in papers:
        bold_title = markdown_bold(paper.title)
        detail_zh.extend([bold_title, paper.summary_zh])
        detail_en.extend([bold_title, paper.summary_en])

    links_zh = "；".join(markdown_link(paper.title, paper.link) for paper in papers)
    links_en = "; ".join(markdown_link(paper.title, paper.link) for paper in papers)
    detail_zh.append(f"链接：{links_zh}")
    detail_en.append(f"{'Link' if count == 1 else 'Links'}: {links_en}")

    lines = [
        "---",
        f"title: {yaml_string(title_zh)}",
        f"title_en: {yaml_string(title_en)}",
        f"image: {image_path}",
        f"date: {post_date}",
        "news_type:",
        "  preset: paper",
        "summary_text:",
        f"  zh: {yaml_string(announcement_zh)}",
        f"  en: {yaml_string(announcement_en)}",
        "details:",
        *block("zh", detail_zh),
        *block("en", detail_en),
        "---",
        "",
    ]
    return "\n".join(lines)


def write_output(name: str, value: str) -> None:
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as stream:
            stream.write(f"{name}={value}\n")
    else:
        print(f"{name}={value}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", required=True, type=Path)
    parser.add_argument("--repo-root", default=Path.cwd(), type=Path)
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    event = json.loads(args.event.read_text(encoding="utf-8"))
    issue = event.get("issue") or {}
    issue_number = int(issue.get("number") or 0)
    if issue_number <= 0:
        fail("事件中缺少有效的 Issue 编号")

    sections = parse_issue_sections(str(issue.get("body") or ""))
    venue = clean_inline(sections["venue"], "会议 / 期刊")
    year = clean_inline(sections["year"], "年份")
    if not re.fullmatch(r"20\d{2}", year):
        fail("年份必须是四位数字，例如 2027")
    papers = parse_papers(sections["papers"])

    created_at = str(issue.get("created_at") or "")
    try:
        created = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        post_date = created.astimezone(CHINA_STANDARD_TIME).date().isoformat()
    except ValueError:
        fail("事件中缺少有效的 Issue 创建时间")

    image_path, created_cover_path, cover_changed = prepare_cover(
        sections["cover"],
        repo_root,
        issue_number,
        post_date,
        os.environ.get("GITHUB_TOKEN", ""),
    )

    post_relative = f"_posts/{post_date}-pub-news-{issue_number}.md"
    post_path = repo_root / post_relative
    post_content = render_post(venue, year, papers, image_path, post_date).encode(
        "utf-8"
    )
    post_changed = write_if_changed(post_path, post_content)
    changed = post_changed or cover_changed

    write_output("changed", "true" if changed else "false")
    write_output("post_path", post_relative)
    write_output("cover_path", created_cover_path)
    print(f"Generated {post_relative} for {len(papers)} paper(s)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, urllib.error.URLError) as error:
        print(f"::error::{error}", file=sys.stderr)
        raise SystemExit(1)
