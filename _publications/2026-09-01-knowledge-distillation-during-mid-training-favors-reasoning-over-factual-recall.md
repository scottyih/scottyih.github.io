---
title: "Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall"
collection: "publications"
permalink: "/publication/2026-09-01-knowledge-distillation-during-mid-training-favors-reasoning-over-factual-recall"
date: 2026-09-01
author: "Jacqueline He, Howard Yen, Shuyue Stella Li, Margaret Li, Hanqing Zeng, Yinglong Xia, Benyu Zhang, Zhuokai Zhao, Qiang Zhang, Pang Wei Koh, Luke Zettlemoyer, Wen-tau Yih"
venue: "arXiv preprint"
paperurl: "https://arxiv.org/abs/2609.01532"
biburl: "/publications/2026-09-01-knowledge-distillation-during-mid-training-favors-reasoning-over-factual-recall.txt"
source_urls: ["https://arxiv.org/abs/2609.01532", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:MhiOAD_qIWkC"]
code: "https://github.com/facebookresearch/midtraining-distillation"
---

[Read the paper](https://arxiv.org/abs/2609.01532)

Logit-based knowledge distillation (KD) is used to train smaller language models (LMs) via supervision from stronger teachers, but whether its benefits are consistent across training stages remains unclear. Through controlled experiments, we find that forward Kullback-Leibler (KL) distillation--the standard KD formulation--with post-trained teachers behaves fundamentally differently during mid-training, an intermediate phase of self-supervised learning on curated corpora. Surprisingly, while forward KD simultaneously improves reasoning and factual recall during pre-training relative to standard next-token prediction (NTP), it instead slows factual recall acquisition during mid-training despite continued reasoning gains. We trace this stage dependence to an asymmetry in teacher confidence across data domains and the student's evolving knowledge state: teachers are more confident on procedural than knowledge-intensive data, while students acquire low-entropy factual knowledge earlier in training. To mitigate this imbalance, we propose Switch Distillation, a simple mid-training objective that distills on tokens where the teacher is confident, using teacher predictive entropy as a lightweight routing signal, and otherwise falls back to cross-entropy. Switch Distillation consistently outperforms existing distillation objectives across teacher sizes. Relative to standard NTP, it achieves 1.61-1.71x the reasoning performance and 1.13-1.19x the knowledge and commonsense performance while preserving 96.7-96.8% of factual recall. Crucially, these benefits persist after post-training: Switch Distillation closes the factual recall gap while maintaining 1.25-1.32x and 1.13-1.20x gains in reasoning and knowledge and commonsense, respectively.
