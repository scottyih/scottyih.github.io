---
title: "ConfRAG: Confidence-Guided Retrieval-Augmenting Generation"
collection: "publications"
permalink: "/publication/2025-06-08-confrag-confidence-guided-retrieval-augmenting-generation"
date: 2025-06-08
author: "Yin Huang, Yifan Ethan Xu, Kai Sun, Vera Yan, Alicia Sun, Haidar Khan, Jimmy Nguyen, Jingxiang Chen, Mohammad Kachuee, Zhaojiang Lin, Yue Liu, Aaron Colak, Anuj Kumar, Wen-tau Yih, Xin Luna Dong"
venue: "arXiv preprint"
paperurl: "https://arxiv.org/abs/2506.07309"
biburl: "/publications/2025-06-08-confrag-confidence-guided-retrieval-augmenting-generation.txt"
source_urls: ["https://arxiv.org/abs/2506.07309", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:7Hz3ACDFbsoC"]
---

[Read the paper](https://arxiv.org/abs/2506.07309)

Can Large Language Models (LLMs) be trained to avoid hallucinating factual statements, and can Retrieval-Augmented Generation (RAG) be triggered only when necessary to reduce retrieval and computation costs? In this work, we address both challenges simultaneously. We introduce ConfQA, a fine-tuning strategy that reduces hallucination rates from 20-40% to below 5% across multiple factuality benchmarks. The approach is simple: when the model answers correctly, it is trained to output the answer; otherwise, it is trained to respond with "I am unsure". Two design choices make this training effective: (1) a dampening prompt ("answer only if you are confident") that explicitly discourages overconfident hallucinations, and (2) training data drawn from atomic factual statements (e.g., knowledge graph attribute values), which calibrates model confidence and yields robust generalization across domains and question types. Building on ConfQA, we propose ConfRAG, a triggering strategy that invokes RAG only when the model responses with unsure. This framework achieves accuracy above 95% in ideal case while reducing unnecessary external retrievals by over 30%.
