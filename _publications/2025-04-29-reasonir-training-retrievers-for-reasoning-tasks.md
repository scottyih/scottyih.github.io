---
title: "ReasonIR: Training Retrievers for Reasoning Tasks"
collection: "publications"
permalink: "/publication/2025-04-29-reasonir-training-retrievers-for-reasoning-tasks"
date: 2025-04-29
author: "Rulin Shao, Rui Qiao, Varsha Kishore, Niklas Muennighoff, Xi Victoria Lin, Daniela Rus, Bryan Kian Hsiang Low, Sewon Min, Wen-tau Yih, Pang Wei Koh, Luke Zettlemoyer"
venue: "arXiv preprint"
paperurl: "https://arxiv.org/abs/2504.20595"
biburl: "/publications/2025-04-29-reasonir-training-retrievers-for-reasoning-tasks.txt"
source_urls: ["https://arxiv.org/abs/2504.20595", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:uDGL6kOW6j0C"]
code: "https://github.com/facebookresearch/ReasonIR"
model: "https://huggingface.co/reasonir/ReasonIR-8B"
dataset: "https://huggingface.co/datasets/reasonir/reasonir-data"
---

[Read the paper](https://arxiv.org/abs/2504.20595)

We present ReasonIR-8B, the first retriever specifically trained for general reasoning tasks. Existing retrievers have shown limited gains on reasoning tasks, in part because existing training datasets focus on short factual queries tied to documents that straightforwardly answer them. We develop a synthetic data generation pipeline that, for each document, our pipeline creates a challenging and relevant query, along with a plausibly related but ultimately unhelpful hard negative. By training on a mixture of our synthetic data and existing public data, ReasonIR-8B achieves a new state-of-the-art of 29.9 nDCG@10 without reranker and 36.9 nDCG@10 with reranker on BRIGHT, a widely-used reasoning-intensive information retrieval (IR) benchmark. When applied to RAG tasks, ReasonIR-8B improves MMLU and GPQA performance by 6.4% and 22.6% respectively, relative to the closed-book baseline, outperforming other retrievers and search engines. In addition, ReasonIR-8B uses test-time compute more effectively: on BRIGHT, its performance consistently increases with longer and more information-rich rewritten queries; it continues to outperform other retrievers when combined with an LLM reranker. Our training recipe is general and can be easily extended to future LLMs; to this end, we open-source our code, data, and model.
