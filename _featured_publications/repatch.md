---
title: RePatch
category: time-series-analysis
name:
  zh: "RePatch: Learning Entropy-Guided Patch Structures with Quantized
    Representations for Time Series Forecasting"
  en: "RePatch: Learning Entropy-Guided Patch Structures with Quantized
    Representations for Time Series Forecasting"
venue:
  zh: KDD 2026
  en: KDD 2026
image: images/featured-works/repatch.png
summary_text:
  zh: 提出两阶段预测框架 RePatch，通过熵引导的动态分块、时间交互建模与向量量化，学习紧凑、可迁移且可复用的离散时间表示，并在 14
    个真实数据集上展现出领先的预测与跨场景泛化能力。
  en: RePatch combines entropy-guided dynamic patching, temporal interaction
    modeling, and vector quantization to learn compact, transferable, and
    reusable discrete representations for time series forecasting.
details:
  zh: >-
    多元时间序列预测受到非平稳动态、持续演化的时间结构以及跨场景泛化能力有限等因素影响，仍是一项具有挑战性的基础任务。近年来的分块方法通过将序列切分为局部单元来增强长程建模能力，但大多依赖固定或适应性较弱的分块策略和连续隐表示，因而限制了模型的灵活性与时间模式复用能力。


    论文提出两阶段框架 RePatch。在自监督预训练阶段，Dynamic Patcher 以熵目标为引导，将时间序列自适应地切分为可变长度的片段，使分块边界更准确地对应局部时间动态；Temporal Interaction Module 则同时捕捉局部与全局时间依赖，并通过向量量化将所得表示映射到结构化的离散潜空间。


    这些离散表示形成了紧凑、可迁移的时间模式抽象，也能够自然支持下游预测中的序列化 token 建模。在 14 个真实数据集上的实验中，RePatch 在多数基准上取得了领先性能，并在多种迁移场景中表现出稳定的泛化能力。
  en: >-
    Multivariate time series forecasting remains difficult because temporal
    dynamics are non-stationary, structures evolve over time, and models often
    generalize poorly across scenarios. Patch-based approaches strengthen
    long-range modeling by dividing a sequence into local units, but fixed or
    weakly adaptive patching and continuous latent representations can restrict
    flexibility and pattern reuse.


    RePatch addresses these limitations with a two-stage framework. During self-supervised pretraining, its Dynamic Patcher uses an entropy-based objective to divide each series into variable-length patches aligned with local temporal dynamics. A Temporal Interaction Module then models both local and global dependencies before vector quantization maps the representations into a structured discrete latent space.


    The resulting discrete representations provide a compact and transferable abstraction of temporal patterns and naturally support token-based sequence modeling for downstream forecasting. Experiments on 14 real-world datasets show state-of-the-art results on most benchmarks and consistent generalization across a range of transfer scenarios.
---
