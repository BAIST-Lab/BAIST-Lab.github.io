---
title: Research Achievements
body_class: page-projects page-top-level
nav:
  order: 2
  title: {zh: 研究成果, en: Research Achievements}
---

# {% include icon.html icon="fa-solid fa-wrench" %}研究成果
{: .lang-zh}

# {% include icon.html icon="fa-solid fa-wrench" %}Research Achievements
{: .lang-en}

{% include section.html %}

{% assign featured_publications = site.featured_publications %}
{% if featured_publications.size > 0 %}
## 代表工作
{: .lang-zh}

## Selected Publications
{: .lang-en}

{% assign featured_categories = site.featured_categories | sort: "order" %}
<div class="featured-publication-categories">
{% for category in featured_categories %}
{% assign category_works = featured_publications | where: "category", category.title %}
{% if category_works.size > 0 %}
<section class="featured-publication-category">
  <h3 class="featured-publication-category-title">
    <span class="lang-zh">{{ category.name.zh }}</span><span class="lang-en">{{ category.name.en }}</span>
  </h3>
  <div class="featured-publication-grid">
    {% for publication in category_works %}
      {% include featured-publication-card.html publication=publication %}
    {% endfor %}
  </div>
</section>
{% endif %}
{% endfor %}

{% assign uncategorized_count = 0 %}
{% for publication in featured_publications %}
  {% assign matched_categories = featured_categories | where: "title", publication.category %}
  {% if matched_categories.size == 0 %}
    {% assign uncategorized_count = uncategorized_count | plus: 1 %}
  {% endif %}
{% endfor %}
{% if uncategorized_count > 0 %}
<section class="featured-publication-category">
  <h3 class="featured-publication-category-title">
    <span class="lang-zh">未分类</span><span class="lang-en">Uncategorized</span>
  </h3>
  <div class="featured-publication-grid">
    {% for publication in featured_publications %}
      {% assign matched_categories = featured_categories | where: "title", publication.category %}
      {% if matched_categories.size == 0 %}
      {% include featured-publication-card.html publication=publication %}
      {% endif %}
    {% endfor %}
  </div>
</section>
{% endif %}

</div>

{% include section.html %}
{% endif %}

{% assign results = site.projects | sort: "start_date" | reverse %}
{% if results.size > 0 %}
## 研究课题
{: .lang-zh}

## Research Topics
{: .lang-en}

<div class="research-result-list">
  {% for result in results %}
    {% include research-result-summary.html project=result %}
  {% endfor %}
</div>
{% else %}
<p class="lang-zh center">暂无研究成果。</p>
<p class="lang-en center">No research achievements are available yet.</p>
{% endif %}
