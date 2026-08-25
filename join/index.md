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

本实验室经费充足，聚焦前沿，科研思路兼顾高水平论文发表与实际应用价值。欢迎对人工智能、机器学习、数据挖掘、大数据分析计算等领域感兴趣的同学加盟。同时，欢迎研究方向与数据科学、大数据计算、机器学习与人工智能、AI4Science等方向相关的青年教师、博士后、研究助理加入团队。深圳市与我校提供具有竞争力的科研环境、启动资金与科研资源，具体意向欢迎邮件联系。
{: .lang-zh}

The lab is well funded and focuses on frontier research, with a research agenda that balances high-quality publications and practical value. We welcome students interested in artificial intelligence, machine learning, data mining, big data analytics and computing, and related fields. We also welcome early-career faculty, postdoctoral researchers, and research assistants whose interests align with data science, big data computing, machine learning and artificial intelligence, AI4Science, and related areas. Shenzhen and HIT provide a competitive research environment, start-up funding, and research resources. Please contact us by email to discuss specific opportunities.
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

<div class="join-contact">
  <p class="lang-zh">
    有兴趣加入团队的申请人，请发送简历及相关材料给团队老师：<br>
    <a href="mailto:zhouxun2023@hit.edu.cn">zhouxun2023@hit.edu.cn</a><br>
    <a href="mailto:zhangfangyuan@hit.edu.cn">zhangfangyuan@hit.edu.cn</a>
  </p>
  <p class="lang-en">
    Applicants interested in joining the team are welcome to send their CV and relevant materials to the faculty members:<br>
    <a href="mailto:zhouxun2023@hit.edu.cn">zhouxun2023@hit.edu.cn</a><br>
    <a href="mailto:zhangfangyuan@hit.edu.cn">zhangfangyuan@hit.edu.cn</a>
  </p>
</div>
