---
title: Team
nav:
  order: 3
  title: {zh: 团队成员, en: People}
  menu:
    - {title: {zh: 教师, en: Faculty}, anchor: faculty}
    - {title: {zh: 博士后, en: Postdocs}, anchor: postdocs}
    - {title: {zh: 博士生, en: Ph.D Students}, anchor: phd}
    - {title: {zh: 硕士生, en: Master Students}, anchor: master}
    - {title: {zh: 本科生, en: Undergraduate Students}, anchor: undergraduate}
    - {title: {zh: 校友, en: Alumni}, anchor: alumni}
---

# {% include icon.html icon="fa-solid fa-users" %}团队成员
{: .lang-zh #people}

# {% include icon.html icon="fa-solid fa-users" %}People
{: .lang-en #people-en}

{% include section.html %}

## 教师
{: .lang-zh #faculty}

## Faculty
{: .lang-en #faculty-en}

{% include list.html data="members" component="portrait" filter="role == 'professor' or role == 'teacher'" sort="date" %}

{% include section.html %}

## 博士后
{: .lang-zh #postdocs}

## Postdocs
{: .lang-en #postdocs-en}

{% include list.html data="members" component="portrait" filter="role == 'postdoc'" sort="date" %}

{% include section.html %}

## 博士生
{: .lang-zh #phd}

## Ph.D Students
{: .lang-en #phd-en}

{% include list.html data="members" component="portrait" filter="role == 'phd'" sort="date" %}

{% include section.html %}

## 硕士生
{: .lang-zh #master}

## Master Students
{: .lang-en #master-en}

{% include list.html data="members" component="portrait" filter="role == 'master'" sort="date" %}

{% include section.html %}

## 本科生
{: .lang-zh #undergraduate}

## Undergraduate Students
{: .lang-en #undergraduate-en}

{% include list.html data="members" component="portrait" filter="role == 'undergrad'" sort="date" %}

{% include section.html %}

## 校友
{: .lang-zh #alumni}

## Alumni
{: .lang-en #alumni-en}

{% include list.html data="members" component="portrait" filter="role == 'graduate'" sort="date" %}
