# 将实验室网站仓库迁移到实验室共用 GitHub 账户

本文档说明如何把 `lab-site` 仓库的所有提交/操作从个人 GitHub 账户改为「实验室共用账户」，
让网站历史上和今后的提交都显示为共用账户，并保持网站与后台正常可用。

> 注意：改写 git 历史会 `force push`，会使远端所有 commit 的 hash 变化，团队成员本地已有的克隆需要重新 clone。
> 请先在副本上测试，确认无误后再对正式仓库操作。

---

## 一、目标

- 仓库历史（author / committer）全部显示为「实验室共用账户」。
- 之后在后台（Decap CMS）或直接 push 的提交，都归属于共用账户。
- 网站（GitHub Pages）、GitHub Actions 部署、后台登录仍正常。

---

## 二、准备

1. 在 GitHub 创建「实验室共用账户」（如 `lab-hitsz`），设置好密码/2FA，作为机器账户保管。
2. 安装 `git-filter-repo`（推荐，速度更快、更安全）：
   - Windows（用 Python 安装）：`pip install git-filter-repo`
   - 或下载官方脚本 `git-filter-repo` 放到 PATH。
   - 如果不想装，也可用 git 自带的 `git filter-branch`（见「方案 B」）。

---

## 三、改写历史提交作者

### 方案 A：git-filter-repo（推荐）

1. 先查看当前仓库中有哪些作者邮箱：
   ```bash
   git log --format='%an <%ae>' | sort -u
   git log --format='%cn <%ce>' | sort -u
   ```

2. 新建一个 `mailmap.txt`，把每个旧作者映射到共用账户（格式：`新名字 <新邮箱> 旧名字 <旧邮箱>`）：
   ```
   Lab Site <lab@example.com> MiSevenJoy <MiSevenJoy@users.noreply.github.com>
   Lab Site <lab@example.com> XinyueWang <46353212+MiSevenJoy@users.noreply.github.com>
   Lab Site <lab@example.com> 张三 <zhangsan@xxx.com>
   ```
   把上面列出的所有旧邮箱都加进去。

3. 克隆一份裸仓库来做改写（不要直接在现有工作目录上做）：
   ```bash
   git clone --bare https://github.com/原账户/lab-site.git
   cd lab-site.git
   git filter-repo --mailmap ../mailmap.txt --force
   ```

4. 改完后验证：
   ```bash
   git log --format='%an <%ae>' | sort -u
   ```

### 方案 B：git filter-branch（git 自带，备选）

```bash
git filter-branch -f --env-filter '
OLD_EMAIL="原邮箱1"
NEW_NAME="Lab Site"
NEW_EMAIL="lab@example.com"
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]; then
    export GIT_COMMITTER_NAME="$NEW_NAME"
    export GIT_COMMITTER_EMAIL="$NEW_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]; then
    export GIT_AUTHOR_NAME="$NEW_NAME"
    export GIT_AUTHOR_EMAIL="$NEW_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags
```
每个旧邮箱都要改一次（复制上面的 `if` 块）。

---

## 四、转移仓库 / 建立新仓库

### 方式 1：仓库转移（保留原 URL 结构，推荐）
- 用「原账户」在 GitHub 进入仓库 → `Settings` → `Danger Zone` → `Transfer ownership` → 目标选共用账户。
- 转移后仓库地址为 `https://github.com/共用账户/lab-site`，GitHub Pages 站点变为 `https://共用账户.github.io/lab-site/`。
- 转移需要在「原账户」和「共用账户」之间进行确认。

### 方式 2：共用账户 fork + 原仓库归档
- 共用账户 fork 该仓库，原账户将原仓库归档（Archive）。
- 缺点：fork 的关系、后续工作都在 fork 上；原仓库历史地址仍指向原账户。

### 改写后推送
如果是新建仓库/空仓库：
```bash
# 把改写后的裸仓库推送到共用账户下的仓库
cd lab-site.git
git remote set-url origin https://github.com/共用账户/lab-site.git
git push --force --mirror origin
```

---

## 五、更新仓库内的网站/后台配置

改写账户后，仓库里指向「原账户」的配置也要改，否则后台和站点 URL 会指向旧地址。

| 文件 | 字段 | 改成 |
|---|---|---|
| `admin/config.yml` | `backend.repo` | `共用账户/lab-site` |
| `admin/config.yml` | `site_url` / `display_url` | `https://共用账户.github.io/lab-site/` |
| `admin/config.yml` | 顶部注释里的后台地址 | 同上 |
| `_config.yaml` | `links.github` | 共用账户名（若想展示） |
| `README.md` | 标题 / 访问地址 | 共用账户地址 |

改完提交并推送（这些提交会以当前登录账户身份记录，正常）。

另外检查 GitHub 仓库设置：
- `Settings → Pages`：确认 Source 分支仍是构建产物（`gh-pages` 分支或 Actions 构建），不需要改动；若原来用默认分支构建，确认 `main` 仍是构建分支。
- `Settings → Actions`：确认 Actions 权限正常（on-push 工作流会自动构建部署）。
- GitHub Actions 里用到的 secrets / token（若有）需要重新在共用账户仓库里配置。

---

## 六、后台（Decap CMS）的登录与提交身份

后台用的是 GitHub OAuth（`admin/config.yml` 里的 `base_url: https://lab-site-oauth.onrender.com`）。

- 这个 OAuth 代理对应一个 GitHub OAuth App，**注册在原账户名下**。
- 后台登录时，每位操作者用自己的 GitHub 账号授权，**提交会以「登录的那个人」的账号显示**。

要保证后台修改都显示为「共用账户」，有两种做法：

1. **共用账户登录后台**（最简单）
   - 让 OAuth App 的 Homepage URL / 回调保持指向后台地址。
   - 用共用账户去 `https://misevenjoy.github.io/lab-site/admin/`（或迁移后的新地址）登录并授权。
   - 之后共用账户在后台做的修改，提交作者就是共用账户。
   - 若仓库已转移到共用账户，共用账户对仓库有完全权限，OAuth App 仍可代它提交。

2. **把 OAuth App 也转到共用账户名下**
   - 到原账户的 GitHub `Settings → Developer settings → OAuth Apps` 找到 `lab-site-oauth` 对应的 App。
   - GitHub 不支持直接转移 OAuth App 所有权；需在共用账户下新建一个 OAuth App，把 `Client ID / Client Secret` 更新到 Render 上的环境变量（`lab-site-oauth.onrender.com` 的 `CLIENT_ID` / `CLIENT_SECRET`），并重新部署。
   - 步骤：
     a. 共用账户创建新 OAuth App：Homepage URL = 新后台地址，Authorization callback URL = `https://lab-site-oauth.onrender.com/callback`（与现有一致）。
     b. 到 Render 控制台打开 `lab-site-oauth` 服务 → `Environment` → 更新 `CLIENT_ID`、`CLIENT_SECRET`、`OAUTH_HOST`（github.com）等。
     c. Redeploy，测试后台登录。

> 说明：自定义媒体库上传图片、删除图片也是用「当前登录用户」的 token 直接调用 GitHub API 提交，因此同样会以登录账户显示。想让其显示为共用账户，就用共用账户登录后台操作。

---

## 七、注意事项

1. **force push 会改变全部 commit hash**：改写历史后，团队成员本地仓库需删除后重新 `git clone`，不要用旧 clone 直接 pull。
2. **gh-pages 分支**：历史改写会连带 gh-pages 分支一起改，确保 `--mirror` 推送覆盖它；否则站点仍从旧构建服务。
3. **先测试**：建议先 clone 副本改写、推到一个临时测试仓库验证，再对正式仓库操作。
4. **备份**：改写前保留一个完整备份（例如 `git clone --mirror` 存到本地）。
5. **安全**：共用账户是机器账户，凭证（PAT、OAuth Secret）要妥善保管，建议开启 2FA；不要把它用于个人用途。
6. **域名**：如果将来绑定了自定义域名，需要在仓库 `Settings → Pages` 的 Custom domain 里重新配置，并更新 DNS。
