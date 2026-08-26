---
title: Map as a Prompt
category: spatiotemporal-foundation-models
name:
  zh: "Map as a Prompt: Learning Multi-Modal Spatial-Signal Foundation Models for
    Cross-scenario Wireless Localization"
  en: "Map as a Prompt: Learning Multi-Modal Spatial-Signal Foundation Models for
    Cross-scenario Wireless Localization"
venue:
  zh: ICLR 2026
  en: ICLR 2026
image: images/featured-works/map-as-prompt.webp
summary_text:
  zh: 提出多模态无线定位基础模型 SigMap，以周期自适应掩码学习稳健的信号表示，并将三维地图作为轻量提示，实现面向未知环境的跨场景定位。
  en: SigMap combines cycle-adaptive masked signal modeling with lightweight 3D
    map prompts to support accurate cross-scenario wireless localization in
    unseen environments.
details:
  zh: >-
    精准、稳健的无线定位是自动驾驶、扩展现实和智能制造等 5G/6G
    应用的重要基础，但无线信号复杂且易受环境变化影响。已有数据驱动方法往往依赖大量标注数据，在跨环境迁移时也面临泛化能力不足的问题。


    为解决这些问题，论文提出多模态无线定位基础模型 SigMap。该模型根据无线信道的周期特征动态调整掩码模式，以学习稳健的信号表示；同时提出“地图即提示”机制，通过轻量级软提示融入三维地理信息，从而高效适应不同定位场景。


    多项定位任务的实验表明，SigMap 在监督和自监督基线之上取得了更好的定位性能，并在未见环境中展现出较强的零样本泛化能力。
  en: >-
    Accurate and robust wireless localization is an important enabler for
    emerging 5G/6G applications, yet the complexity of wireless signals and
    their sensitivity to environmental changes make cross-scenario localization
    difficult. Existing data-driven methods often require extensive labeled data
    and generalize poorly to new environments.


    The paper proposes SigMap, a multimodal foundation model for wireless localization. Its cycle-adaptive masking strategy changes the masking pattern according to channel periodicity to learn robust signal representations. A map-as-prompt mechanism then incorporates 3D geographic information through lightweight soft prompts for efficient adaptation across scenarios.


    Experiments across multiple localization tasks show state-of-the-art performance and strong zero-shot generalization in unseen environments compared with supervised and self-supervised baselines.
---
