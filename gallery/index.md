---
title: Gallery
nav:
  order: 4
  title: {zh: 相册, en: Gallery}
---

# {% include icon.html icon="fa-regular fa-images" %}相册
{: .lang-zh}

# {% include icon.html icon="fa-regular fa-images" %}Gallery
{: .lang-en}

实验室科研活动与生活瞬间，点击图片可放大查看。
{: .lang-zh}

Moments from lab research and activities. Click an image to enlarge.
{: .lang-en}

{% include section.html %}

<div class="gallery-wall">
  {% for photo in site.data.gallery.photos %}
  <figure class="gallery-figure">
    <img class="gallery-item" src="{{ photo.image | relative_url | uri_escape }}" alt="{{ photo.caption.zh | default: photo.caption.en | default: 'gallery photo' | xml_escape }}" loading="lazy" onclick="openLightbox(this)">
    {% if photo.caption.zh or photo.caption.en %}
    <figcaption class="gallery-caption">
      <span class="lang-zh">{{ photo.caption.zh }}</span><span class="lang-en">{{ photo.caption.en }}</span>
    </figcaption>
    {% endif %}
  </figure>
  {% endfor %}
</div>

<div class="lightbox" id="lightbox" onclick="closeLightbox()">
  <img id="lightbox-img" alt="enlarged photo">
</div>
