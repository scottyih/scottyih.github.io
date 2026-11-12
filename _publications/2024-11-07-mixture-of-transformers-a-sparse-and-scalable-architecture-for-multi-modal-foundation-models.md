---
title: "Mixture-of-Transformers: A Sparse and Scalable Architecture for Multi-Modal Foundation Models"
collection: "publications"
permalink: "/publication/2024-11-07-mixture-of-transformers-a-sparse-and-scalable-architecture-for-multi-modal-foundation-models"
date: 2025-01-01
author: "Weixin Liang, Lili Yu, Liang Luo, Srinivasan Iyer, Ning Dong, Chunting Zhou, Gargi Ghosh, Mike Lewis, Wen-tau Yih, Luke Zettlemoyer, Xi Victoria Lin"
venue: "TMLR 2025"
paperurl: "https://arxiv.org/abs/2411.04996"
biburl: "/publications/2024-11-07-mixture-of-transformers-a-sparse-and-scalable-architecture-for-multi-modal-foundation-models.txt"
source_urls: ["https://arxiv.org/abs/2411.04996", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:Ak0FvsSvgGUC"]
code: "https://github.com/facebookresearch/Mixture-of-Transformers"
---

[Read the paper](https://arxiv.org/abs/2411.04996)

The development of large language models (LLMs) has expanded to multi-modal systems capable of processing text, images, and speech within a unified framework. Training these models demands significantly larger datasets and computational resources compared to text-only LLMs. To address the scaling challenges, we introduce Mixture-of-Transformers (MoT), a sparse multi-modal transformer architecture that significantly reduces pretraining computational costs. MoT decouples non-embedding parameters of the model by modality -- including feed-forward networks, attention matrices, and layer normalization -- enabling modality-specific processing with global self-attention over the full input sequence. We evaluate MoT across multiple settings and model scales. In the Chameleon 7B setting (autoregressive text-and-image generation), MoT matches the dense baseline's performance using only 55.8\% of the FLOPs. When extended to include speech, MoT reaches speech performance comparable to the dense baseline with only 37.2\% of the FLOPs. In the Transfusion setting, where text and image are trained with different objectives, a 7B MoT model matches the image modality performance of the dense baseline with one third of the FLOPs, and a 760M MoT model outperforms a 1.4B dense baseline across key image generation metrics. System profiling further highlights MoT's practical benefits, achieving dense baseline image quality in 47.2\% of the wall-clock time and text quality in 75.6\% of the wall-clock time (measured on AWS p4de.24xlarge instances with NVIDIA A100 GPUs).
