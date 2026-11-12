---
title: "Memory Layers at Scale"
collection: "publications"
permalink: "/publication/2024-12-12-memory-layers-at-scale"
date: 2025-10-06
author: "Vincent-Pierre Berges, Barlas Oğuz, Daniel Haziza, Wen-tau Yih, Luke Zettlemoyer, Gargi Ghosh"
venue: "ICML 2025"
paperurl: "https://proceedings.mlr.press/v267/berges25a.html"
biburl: "/publications/2024-12-12-memory-layers-at-scale.txt"
source_urls: ["https://arxiv.org/abs/2412.09764", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:F1b5ZUV5XREC", "https://proceedings.mlr.press/v267/berges25a.html"]
highlight: "Sparse key-value memory adds capacity to language models for storing and retrieving information efficiently."
preprint: "https://arxiv.org/abs/2412.09764"
code: "https://github.com/facebookresearch/memory"
---

[Read the paper](https://proceedings.mlr.press/v267/berges25a.html)

Memory layers use a trainable key-value lookup mechanism to add extra parameters to a model without increasing FLOPs. Conceptually, sparsely activated memory layers complement compute-heavy dense feed-forward layers, providing dedicated capacity to store and retrieve information cheaply. This work takes memory layers beyond proof-of-concept, proving their utility at contemporary scale. On downstream tasks, language models augmented with our improved memory layer outperform dense models with more than twice the computation budget, as well as mixture-of-expert models when matched for both compute and parameters. We find gains are especially pronounced for factual tasks. We provide a fully parallelizable memory layer implementation, demonstrating scaling laws with up to 128B memory parameters, pretrained to 1 trillion tokens, comparing to base models with up to 8B parameters.
