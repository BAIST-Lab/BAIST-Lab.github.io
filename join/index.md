---
title: Join Us
body_class: page-top-level
nav:
  order: 5
  title: {zh: 加入我们, en: Join Us}
---

# {% include icon.html icon="fa-solid fa-chalkboard-user" %}加入我们
{: .lang-zh}

# {% include icon.html icon="fa-solid fa-chalkboard-user" %}Join Us
{: .lang-en}

{% include section.html %}

“时空大数据智能与计算实验室”经费充足，聚焦前沿，科研思路兼顾高水平论文发表与实际应用价值。欢迎对数据挖掘、人工智能，尤其是时空大数据分析挖掘感兴趣的同学加盟我组。
{: .lang-zh}

The Spatiotemporal Big Data Intelligence and Computing Lab has sufficient funding and focuses on frontier research, balancing high-quality publications with real-world applications. We welcome students interested in data mining, artificial intelligence, and especially spatiotemporal big data analytics to join us.
{: .lang-en}

除计算机专业外，我组也欢迎数学、通信、电子信息、GIS、交通等专业，具有深度学习和编程基础的同学申请博士。每年招收 2–4 名博士生，3–4 名硕士研究生。同时，欢迎研究方向与数据科学、大数据计算、机器学习与人工智能、计算机视觉、具身智能等方向相关的青年教师、博士后、研究助理加入团队。深圳市与我校提供具有竞争力的科研环境、启动资金与科研资源，具体意向欢迎邮件联系。
{: .lang-zh}

In addition to computer science, we welcome applicants from mathematics, communications, electronic information, GIS, and transportation with solid deep learning and programming foundations for PhD positions. We recruit 2–4 PhD students and 3–4 master's students each year. We also welcome faculty, postdocs, and research assistants working on data science, big data computing, machine learning &amp; AI, computer vision, and embodied intelligence. Shenzhen and HIT provide a competitive research environment, start-up funding, and resources. Please feel free to contact us by email.
{: .lang-en}

**招生招聘信息具体如下：**
{: .lang-zh}

**Specific openings are as follows:**
{: .lang-en}

{% for section in site.data.join.sections %}
<h2 class="lang-zh">{{ forloop.index }}. {{ section.title.zh }}</h2>
<h2 class="lang-en">{{ forloop.index }}. {{ section.title.en }}</h2>
<div class="lang-zh">{{ section.content.zh | markdownify }}</div>
<div class="lang-en">{{ section.content.en | markdownify }}</div>
{% unless forloop.last %}{% include section.html %}{% endunless %}
{% endfor %}

请发送简历及相关材料至：**zhouxun2023@hit.edu.cn**
{: .lang-zh}

Please send your CV and relevant materials to: **zhouxun2023@hit.edu.cn**
{: .lang-en}
