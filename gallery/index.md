---
title: Gallery
body_class: page-top-level
nav:
  order: 4
  title: {zh: 相册, en: Gallery}
---

<h1 class="lang-zh">{% include icon.html icon="fa-regular fa-images" %}相册</h1>
<h1 class="lang-en">{% include icon.html icon="fa-regular fa-images" %}Gallery</h1>

{% include section.html %}

<p class="lang-zh">实验室科研活动与生活瞬间，点击图片可放大查看。</p>

<p class="lang-en">Moments from lab research and activities. Click an image to enlarge.</p>

{% include section.html %}

<div class="gallery-wall">
  {% for photo in site.data.gallery.photos %}
  {% assign cap_zh = photo.caption.zh | default: '' | strip %}
  {% assign cap_en = photo.caption.en | default: '' | strip %}
  <figure class="gallery-figure">
    <img class="gallery-item" src="{{ photo.image | relative_url | uri_escape }}" alt="{{ cap_zh | default: cap_en | default: 'gallery photo' | xml_escape }}" loading="lazy" onclick="openLightbox(this)">
    {% if cap_zh != '' or cap_en != '' %}
    <figcaption class="gallery-caption">
      {% if cap_zh != '' %}<span class="lang-zh">{{ cap_zh }}</span>{% endif %}
      {% if cap_en != '' %}<span class="lang-en">{{ cap_en }}</span>{% endif %}
    </figcaption>
    {% endif %}
  </figure>
  {% endfor %}
</div>

<div class="lightbox" id="lightbox" onclick="closeLightbox()">
  <img id="lightbox-img" alt="enlarged photo">
</div>
