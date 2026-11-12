---
title: "Anchored Decoding: Provably Reducing Copyright Risk for Any Language Model"
collection: "publications"
permalink: "/publication/2026-02-06-anchored-decoding-provably-reducing-copyright-risk-for-any-language-model"
date: 2026-09-29
author: "Jacqueline He, Jonathan Hayase, Wen-tau Yih, Sewoong Oh, Luke Zettlemoyer, Pang Wei Koh"
venue: "ICML 2026"
paperurl: "https://proceedings.mlr.press/v306/he26k.html"
biburl: "/publications/2026-02-06-anchored-decoding-provably-reducing-copyright-risk-for-any-language-model.txt"
source_urls: ["https://arxiv.org/abs/2602.07120", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:MpfHP-DdYjUC", "https://proceedings.mlr.press/v306/he26k.html"]
preprint: "https://arxiv.org/abs/2602.07120"
code: "https://github.com/jacqueline-he/anchored-decoding"
---

[Read the paper](https://proceedings.mlr.press/v306/he26k.html)

Language models (LMs) tend to memorize portions of their training data and emit verbatim spans. When the underlying sources are sensitive or copyright-protected, such reproduction raises issues of consent and compensation for creators and compliance risks for developers. We propose Anchored Decoding, a plug-and-play inference-time method for suppressing verbatim copying: it enables decoding from any risky LM trained on mixed-license data by keeping generation in bounded proximity to a permissively trained safe LM. Anchored Decoding adaptively allocates a user-chosen information budget over the generation trajectory and enforces per-step constraints that yield a sequence-level guarantee, enabling a tunable risk-utility trade-off. To make Anchored Decoding practically useful, we introduce a new permissively trained safe model (TinyComma 1.8B), as well as Anchored$_{\mathrm{Byte}}$ Decoding, a byte-level variant of our method that enables cross-vocabulary fusion via the ByteSampler framework (Hayase et al., 2025). Across six model pairs on long-form metrics for copying risk and utility, Anchored and Anchored$_{\mathrm{Byte}}$ Decoding define a new Pareto frontier, preserving near-original fluency and factuality while closing up to 75% of the measurable copying gap between the risky baseline and a safe reference, at a modest inference overhead.
