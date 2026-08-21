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

{% assign results = site.projects | sort: "start_date" | reverse %}
{% assign card_count = 0 %}
{% for result in results %}
  {% assign details_zh = result.details.zh | default: "" | strip %}
  {% assign details_en = result.details.en | default: "" | strip %}
  {% if details_zh != "" or details_en != "" %}
    {% assign card_count = card_count | plus: 1 %}
  {% endif %}
{% endfor %}

{% if results.size > 0 %}
{% if card_count > 0 %}
<div class="research-result-grid">
  {% for result in results %}
    {% assign details_zh = result.details.zh | default: "" | strip %}
    {% assign details_en = result.details.en | default: "" | strip %}
    {% if details_zh != "" or details_en != "" %}
    {% include research-result-card.html project=result %}
    {% endif %}
  {% endfor %}
</div>

{% include section.html %}
{% endif %}

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
