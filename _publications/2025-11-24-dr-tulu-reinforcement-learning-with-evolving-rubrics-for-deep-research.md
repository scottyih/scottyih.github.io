---
title: "DR Tulu: Reinforcement Learning with Evolving Rubrics for Deep Research"
collection: "publications"
permalink: "/publication/2025-11-24-dr-tulu-reinforcement-learning-with-evolving-rubrics-for-deep-research"
date: 2026-09-29
author: "Rulin Shao, Akari Asai, Shannon Zejiang Shen, Hamish Ivison, Varsha Kishore, Jingming Zhuo, Xinran Zhao, Molly Park, Samuel G. Finlayson, David Sontag, Tyler Murray, Sewon Min, Pradeep Dasigi, Luca Soldaini, Faeze Brahman, Wen-tau Yih, Tongshuang Wu, Luke Zettlemoyer, Yoon Kim, Hannaneh Hajishirzi, Pang Wei Koh"
venue: "ICML 2026"
paperurl: "https://proceedings.mlr.press/v306/shao26a.html"
biburl: "/publications/2025-11-24-dr-tulu-reinforcement-learning-with-evolving-rubrics-for-deep-research.txt"
source_urls: ["https://arxiv.org/abs/2511.19399", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:cK4Rrx0J3m0C", "https://proceedings.mlr.press/v306/shao26a.html"]
preprint: "https://arxiv.org/abs/2511.19399"
code: "https://github.com/rlresearch/dr-tulu"
project: "https://huggingface.co/collections/rl-research/dr-tulu"
model:
  - "https://huggingface.co/rl-research/DR-Tulu-8B"
  - "https://huggingface.co/rl-research/DR-Tulu-SFT-8B"
dataset:
  - "https://huggingface.co/datasets/rl-research/dr-tulu-sft-data"
  - "https://huggingface.co/datasets/rl-research/dr-tulu-rl-data"
---

[Read the paper](https://proceedings.mlr.press/v306/shao26a.html)

Deep research agents perform multi-step research to produce long-form, well-attributed answers. However, most open deep research agents are trained on easily verifiable short-form QA tasks via reinforcement learning with verifiable rewards, which does not extend to realistic long-form tasks. We address this with Reinforcement Learning with Evolving Rubrics (RLER), where rubrics are constructed and maintained to co-evolve with the policy model during training. This allows the rubrics to incorporate newly explored information from search and contrasting model responses, enabling better fact checking and more discriminative on-policy feedback. Using RLER, we develop Deep Research Tulu (DR Tulu-8B), the first fully open model that is directly trained for open-ended, long-form deep research. Across four long-form deep research benchmarks in science, healthcare, and general domains, DR Tulu substantially outperforms existing open deep research agents (by 15.6% over Tongyi DR on average) and matches or exceeds proprietary deep research agents (by 0.7% over OpenAI DR on average), while being significantly smaller and cheaper per query (1000x cheaper than OpenAI DR per query).
