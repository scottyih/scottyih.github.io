---
title: "TruthRL: Incentivizing Truthful LLMs via Reinforcement Learning"
collection: "publications"
permalink: "/publication/2025-09-30-truthrl-incentivizing-truthful-llms-via-reinforcement-learning"
date: 2026-09-29
author: "Zhepei Wei, Xiao Yang, Kai Sun, Jiaqi Wang, Rulin Shao, Jingxiang Chen, Mohammad Kachuee, Teja Gollapudi, Yiwei Liao, Nicolas Scheffer, Rakesh Wanga, Anuj Kumar, Yu Meng, Wen-tau Yih, Xin Luna Dong"
venue: "ICML 2026"
paperurl: "https://proceedings.mlr.press/v306/wei26ab.html"
biburl: "/publications/2025-09-30-truthrl-incentivizing-truthful-llms-via-reinforcement-learning.txt"
source_urls: ["https://arxiv.org/abs/2509.25760", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:jgBuDB5drN8C", "https://proceedings.mlr.press/v306/wei26ab.html"]
preprint: "https://arxiv.org/abs/2509.25760"
code: "https://github.com/facebookresearch/TruthRL"
---

[Read the paper](https://proceedings.mlr.press/v306/wei26ab.html)

While large language models (LLMs) have demonstrated strong performance on factoid question answering, they are still prone to hallucination and untruthful responses, particularly when tasks demand information outside their parametric knowledge. Indeed, truthfulness requires more than accuracy -- models must also recognize uncertainty and abstain when unsure to avoid hallucinations. This presents a fundamental challenge for existing methods: approaches that optimize for accuracy often amplify hallucinations, while those that encourage abstention can become overly conservative, sacrificing correct answers. Both extremes ultimately compromise truthfulness. In this work, we present TruthRL, a general reinforcement learning (RL) framework that directly optimizes the truthfulness of LLMs. Specifically, we implement TruthRL using GRPO with a simple yet effective ternary reward that distinguishes correct answers, hallucinations, and abstentions. It incentivizes models to reduce hallucinations not only by providing correct responses, but also by enabling abstention when uncertain, thereby improving truthfulness. Extensive experiments across four knowledge-intensive benchmarks show that TruthRL significantly reduces hallucinations (e.g., 43.5% $\rightarrow$ 19.4%) and improves truthfulness (e.g., 5.3% $\rightarrow$ 37.2%), with consistent gains across various backbone models. Analysis shows that the improvement of TruthRL arises from enhanced capability of LLMs to recognize their knowledge boundary, hence avoiding being overly conservative as the baselines are.
