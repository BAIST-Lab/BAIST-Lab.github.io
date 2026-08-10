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
  <img class="gallery-item" src="{{ "images/gallery/photo1.jpg" | relative_url | uri_escape }}" alt="gallery photo" loading="lazy" onclick="openLightbox(this)">
  <img class="gallery-item" src="{{ "images/gallery/photo2.jpg" | relative_url | uri_escape }}" alt="gallery photo" loading="lazy" onclick="openLightbox(this)">
  <img class="gallery-item" src="{{ "images/gallery/photo3.jpg" | relative_url | uri_escape }}" alt="gallery photo" loading="lazy" onclick="openLightbox(this)">
  <img class="gallery-item" src="{{ "images/gallery/photo4.jpg" | relative_url | uri_escape }}" alt="gallery photo" loading="lazy" onclick="openLightbox(this)">
  <img class="gallery-item" src="{{ "images/gallery/photo5.jpg" | relative_url | uri_escape }}" alt="gallery photo" loading="lazy" onclick="openLightbox(this)">
</div>

<div class="lightbox" id="lightbox" onclick="closeLightbox()">
  <img id="lightbox-img" alt="enlarged photo">
</div>
