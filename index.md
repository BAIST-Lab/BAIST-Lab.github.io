---
body_class: page-top-level
---

<h1 class="home-lab-heading">
  <span class="lang-zh">时空大数据智能与计算实验室</span>
  <span class="lang-en"><a href="https://baist-lab.github.io/">Big Data AI &amp; Spatial-Temporal Computing Lab</a> (BAIST)</span>
</h1>
<p class="home-lab-english-name lang-zh"><a href="https://baist-lab.github.io/">Big Data AI &amp; Spatial-Temporal Computing Lab</a> (BAIST)</p>

{% include section.html %}

<p class="lang-zh">实验室以数据驱动的智能与计算为核心，面向复杂、异构、多模态大数据，围绕人工智能、机器学习、数据分析与挖掘、数据管理等技术及其在垂直领域中的应用开展研究。当前重点方向包括：通用与领域大数据智能体系统、AI4S与科学智能体、时空数据挖掘与时间序列分析、可解释机器学习与推理、强化学习与模仿学习、多模态时空智能与具身智能、AI计算基座（AI Infra）等。研究成果广泛应用于智慧城市与智慧交通、低空经济、共享经济与城市物流、公共安全、环境保护、智慧能源与电力系统智能等领域。</p>

<p class="lang-en">The lab centers on data-driven intelligence and computing, conducting research on artificial intelligence, machine learning, data analytics and mining, data management, and their applications in vertical domains for complex, heterogeneous, and multimodal big data. Current focus areas include general-purpose and domain-specific big-data agent systems, AI for Science (AI4S) and scientific agents, spatiotemporal data mining and time-series analysis, explainable machine learning and reasoning, reinforcement learning and imitation learning, multimodal spatiotemporal intelligence and embodied AI, and AI infrastructure (AI Infra). Its research outcomes are widely applied to smart cities and intelligent transportation, the low-altitude economy, the sharing economy and urban logistics, public safety, environmental protection, smart energy, and intelligent power systems.</p>

{% include section.html %}

<h2 class="lang-zh center">最新进展</h2>
<h2 class="lang-en center">Highlights</h2>

{% for post in site.posts %}
{% include news.html url=post.url title=post.title title_en=post.title_en image=post.image date=post.date news_type=post.news_type summary=post.summary_text %}
{% endfor %}
