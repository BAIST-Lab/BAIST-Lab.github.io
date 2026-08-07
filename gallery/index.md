---
title: Gallery
nav:
  order: 4
  tooltip: Photos
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

{% assign gallery_imgs = site.static_files
  | where_exp: "f", "f.path contains '/images/gallery/'"
  | sort: "name"
%}

<div class="gallery-wall">
  {% for img in gallery_imgs %}
    <img
      class="gallery-item"
      src="{{ img.path | relative_url | uri_escape }}"
      alt="gallery photo"
      loading="lazy"
      onclick="openLightbox(this)"
    >
  {% endfor %}
</div>

<div class="lightbox" id="lightbox" onclick="closeLightbox()">
  <img id="lightbox-img" alt="enlarged photo">
</div>
