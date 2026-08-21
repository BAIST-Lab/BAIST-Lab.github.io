---
title: Publications
body_class: page-research
nav:
  order: 1
  title: {zh: 发表论著, en: Publications}
---

# {% include icon.html icon="fa-solid fa-microscope" %}发表论著
{: .lang-zh}

# {% include icon.html icon="fa-solid fa-microscope" %}Publications
{: .lang-en}

{% include section.html %}

{% assign featured_publications = site.featured_publications %}
{% if featured_publications.size > 0 %}
## 代表成果
{: .lang-zh}

## Representative Work
{: .lang-en}

<div class="featured-publication-grid">
  {% for publication in featured_publications %}
    {% include featured-publication-card.html publication=publication %}
  {% endfor %}
</div>

{% include section.html %}
{% endif %}

{% include search-box.html %}

{% include search-info.html %}

{% include list.html data="citations" component="citation" style="list" %}
