---
title: "Self-Pruned Key-Value Attention: Learning When to Write by Predicting Future Utility"
collection: "publications"
permalink: "/publication/2026-05-13-self-pruned-key-value-attention-learning-when-to-write-by-predicting-future-utility"
date: 2026-05-13
author: "Gergely Szilvasy, Manuel Faysse, Maria Lomeli, Matthijs Douze, Pierre-Emmanuel Mazaré, Loïc Cabannes, Wen-tau Yih, Hervé Jégou"
venue: "arXiv preprint"
paperurl: "https://arxiv.org/abs/2605.14037"
biburl: "/publications/2026-05-13-self-pruned-key-value-attention-learning-when-to-write-by-predicting-future-utility.txt"
source_urls: ["https://arxiv.org/abs/2605.14037", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:j7_hQOaDUrUC"]
---

[Read the paper](https://arxiv.org/abs/2605.14037)

Under modern test-time compute and agentic paradigms, language models process ever-longer sequences. Efficient text generation with transformer architectures is increasingly constrained by the Key-Value cache memory footprint and bandwidth. To address this limitation, we introduce Self-Pruned Key-Value Attention (SP-KV), a mechanism designed to predict future KV utility in order to reduce the size of the long-term KV cache. This strategy operates at a fine granularity: a lightweight utility predictor scores each key-value pair, and while recent KVs are always available via a local window, older pairs are written in the cache and used in global attention only if their predicted utility surpasses a given threshold. The LLM and the utility predictor are trained jointly end-to-end exclusively through next-token prediction loss, and are adapted from pretrained LLM checkpoints.
  Rather than enforcing a fixed compression ratio, SP-KV performs dynamic sparsification: the mechanism adapts to the input and typically reduces the KV cache size by a factor of $3$ to $10\times$, longer sequences often being more compressible. This leads to vast improvements in memory usage and decoding speed, with little to no degradation of validation loss nor performance on a broad set of downstream tasks. Beyond serving as an effective KV-cache reduction mechanism, our method reveals structured layer- and head-specific sparsity patterns that we can use to guide the design of hybrid local-global attention architectures.
