---
title: "Learning to Reason for Factuality"
collection: "publications"
permalink: "/publication/2025-08-07-learning-to-reason-for-factuality"
date: 2026-09-29
author: "Xilun Chen, Ilia Kulikov, Vincent-Pierre Berges, Barlas Oğuz, Rulin Shao, Gargi Ghosh, Jason Weston, Wen-tau Yih"
venue: "ICML 2026"
paperurl: "https://proceedings.mlr.press/v306/chen26bh.html"
biburl: "/publications/2025-08-07-learning-to-reason-for-factuality.txt"
source_urls: ["https://arxiv.org/abs/2508.05618", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:ALROH1vI_8AC", "https://proceedings.mlr.press/v306/chen26bh.html"]
preprint: "https://arxiv.org/abs/2508.05618"
code:
  - "https://github.com/facebookresearch/factual_reasoning"
  - "https://github.com/facebookresearch/ScalableVeriScore"
dataset: "https://huggingface.co/datasets/facebook/factual_reasoning"
---

[Read the paper](https://proceedings.mlr.press/v306/chen26bh.html)

Reasoning Large Language Models (R-LLMs) have significantly advanced complex reasoning tasks but often struggle with factuality, generating substantially more hallucinations than their non-reasoning counterparts on long-form factuality benchmarks. However, extending online Reinforcement Learning (RL), a key component in recent R-LLM advancements, to the long-form factuality setting poses several unique challenges due to the lack of reliable verification methods. Previous work has utilized automatic factuality evaluation frameworks such as FActScore to curate preference data in the offline RL setting, yet we find that directly leveraging such methods as the reward in online RL leads to reward hacking in multiple ways, such as producing less detailed or relevant responses. We propose a novel reward function that simultaneously considers the factual precision, response detail level, and answer relevance, and applies online RL to learn high quality factual reasoning. Evaluated on six long-form factuality benchmarks, our factual reasoning model achieves an average reduction of 23.1 percentage points in hallucination rate, a 23% increase in answer detail level, and no degradation in the overall response helpfulness.
