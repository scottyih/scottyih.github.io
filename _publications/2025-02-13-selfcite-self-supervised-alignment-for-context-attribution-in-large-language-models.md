---
title: "SelfCite: Self-Supervised Alignment for Context Attribution in Large Language Models"
collection: "publications"
permalink: "/publication/2025-02-13-selfcite-self-supervised-alignment-for-context-attribution-in-large-language-models"
date: 2025-10-06
author: "Yung-Sung Chuang, Benjamin Cohen-Wang, Shannon Zejiang Shen, Zhaofeng Wu, Hu Xu, Xi Victoria Lin, James Glass, Shang-Wen Li, Wen-tau Yih"
venue: "ICML 2025"
paperurl: "https://proceedings.mlr.press/v267/chuang25a.html"
biburl: "/publications/2025-02-13-selfcite-self-supervised-alignment-for-context-attribution-in-large-language-models.txt"
source_urls: ["https://arxiv.org/abs/2502.09604", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:0CzhzZyukY4C", "https://proceedings.mlr.press/v267/chuang25a.html"]
preprint: "https://arxiv.org/abs/2502.09604"
code: "https://github.com/facebookresearch/SelfCite"
model:
  - "https://huggingface.co/voidism/SelfCite-8B"
  - "https://huggingface.co/voidism/SelfCite-8B-from-CC"
---

[Read the paper](https://proceedings.mlr.press/v267/chuang25a.html)

We introduce SelfCite, a novel self-supervised approach that aligns LLMs to generate high-quality, fine-grained, sentence-level citations for the statements in their generated responses. Instead of only relying on costly and labor-intensive annotations, SelfCite leverages a reward signal provided by the LLM itself through context ablation: If a citation is necessary, removing the cited text from the context should prevent the same response; if sufficient, retaining the cited text alone should preserve the same response. This reward can guide the inference-time best-of-N sampling strategy to improve citation quality significantly, as well as be used in preference optimization to directly fine-tune the models for generating better citations. The effectiveness of SelfCite is demonstrated by increasing citation F1 up to 5.3 points on the LongBench-Cite benchmark across five long-form question answering tasks. The source code is available at https://github.com/facebookresearch/SelfCite
