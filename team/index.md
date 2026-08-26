---
title: Team
body_class: page-top-level page-team
nav:
  order: 3
  title: {zh: 团队成员, en: People}
  menu:
    - {title: {zh: 教师, en: Faculty}, anchor: faculty}
    - {title: {zh: 博士后, en: Postdocs}, anchor: postdocs}
    - {title: {zh: 博士生, en: Ph.D Students}, anchor: phd}
    - {title: {zh: 硕士生, en: Master Students}, anchor: master}
    - {title: {zh: 本科生, en: Undergraduate Students}, anchor: undergraduate}
    - {title: {zh: 已毕业成员, en: Alumni}, anchor: alumni}
---

<h1 class="lang-zh" id="people">{% include icon.html icon="fa-solid fa-users" %}团队成员</h1>
<h1 class="lang-en" id="people-en">{% include icon.html icon="fa-solid fa-users" %}People</h1>

{% include section.html %}

<h2 class="lang-zh" id="faculty">教师</h2>
<h2 class="lang-en" id="faculty-en">Faculty</h2>

{% include list.html data="members" component="portrait" filter="role == 'professor' or role == 'teacher'" sort="date" %}

{% include section.html %}

<h2 class="lang-zh" id="postdocs">博士后</h2>
<h2 class="lang-en" id="postdocs-en">Postdocs</h2>

{% include list.html data="members" component="portrait" filter="role == 'postdoc'" sort="date" %}

{% include section.html %}

<h2 class="lang-zh" id="phd">博士生</h2>
<h2 class="lang-en" id="phd-en">Ph.D Students</h2>

{% include list.html data="members" component="portrait" filter="role == 'phd'" sort="date" %}

{% include section.html %}

<h2 class="lang-zh" id="master">硕士生</h2>
<h2 class="lang-en" id="master-en">Master Students</h2>

{% include list.html data="members" component="portrait" filter="role == 'master'" sort="date" %}

{% include section.html %}

<h2 class="lang-zh" id="undergraduate">本科生</h2>
<h2 class="lang-en" id="undergraduate-en">Undergraduate Students</h2>

{% include list.html data="members" component="portrait" filter="role == 'undergrad'" sort="date" %}

{% include section.html %}

<h2 class="lang-zh" id="alumni">已毕业成员</h2>
<h2 class="lang-en" id="alumni-en">Alumni</h2>

{% include list.html data="members" component="portrait" filter="role == 'graduate'" sort="date" %}
