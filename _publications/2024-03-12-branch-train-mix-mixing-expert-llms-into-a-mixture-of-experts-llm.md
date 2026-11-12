---
title: "Branch-Train-MiX: Mixing Expert LLMs into a Mixture-of-Experts LLM"
collection: "publications"
permalink: "/publication/2024-03-12-branch-train-mix-mixing-expert-llms-into-a-mixture-of-experts-llm"
date: 2024-03-12
author: "Sainbayar Sukhbaatar, Olga Golovneva, Vasu Sharma, Hu Xu, Xi Victoria Lin, Baptiste Rozière, Jacob Kahn, Daniel Li, Wen-tau Yih, Jason Weston, Xian Li"
venue: "arXiv preprint"
paperurl: "https://arxiv.org/abs/2403.07816"
biburl: "/publications/2024-03-12-branch-train-mix-mixing-expert-llms-into-a-mixture-of-experts-llm.txt"
source_urls: ["https://arxiv.org/abs/2403.07816", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:_5tno0g5mFcC"]
---

[Read the paper](https://arxiv.org/abs/2403.07816)

We investigate efficient methods for training Large Language Models (LLMs) to possess capabilities in multiple specialized domains, such as coding, math reasoning and world knowledge. Our method, named Branch-Train-MiX (BTX), starts from a seed model, which is branched to train experts in embarrassingly parallel fashion with high throughput and reduced communication cost. After individual experts are asynchronously trained, BTX brings together their feedforward parameters as experts in Mixture-of-Expert (MoE) layers and averages the remaining parameters, followed by an MoE-finetuning stage to learn token-level routing. BTX generalizes two special cases, the Branch-Train-Merge method, which does not have the MoE finetuning stage to learn routing, and sparse upcycling, which omits the stage of training experts asynchronously. Compared to alternative approaches, BTX achieves the best accuracy-efficiency tradeoff.
