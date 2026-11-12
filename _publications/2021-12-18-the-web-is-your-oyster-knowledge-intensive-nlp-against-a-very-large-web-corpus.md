---
title: "The Web Is Your Oyster - Knowledge-Intensive NLP against a Very Large Web Corpus"
collection: "publications"
permalink: "/publication/2021-12-18-the-web-is-your-oyster-knowledge-intensive-nlp-against-a-very-large-web-corpus"
date: 2021-12-18
author: "Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Dmytro Okhonko, Samuel Broscheit, Gautier Izacard, Patrick Lewis, Barlas Oğuz, Edouard Grave, Wen-tau Yih, Sebastian Riedel"
venue: "arXiv preprint"
paperurl: "https://arxiv.org/abs/2112.09924"
biburl: "/publications/2021-12-18-the-web-is-your-oyster-knowledge-intensive-nlp-against-a-very-large-web-corpus.txt"
source_urls: ["https://arxiv.org/abs/2112.09924", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:BUYA1_V_uYcC"]
code: "https://github.com/facebookresearch/Sphere"
model: "https://github.com/facebookresearch/Sphere#download-assets"
dataset: "https://github.com/facebookresearch/Sphere#index-download"
---

[Read the paper](https://arxiv.org/abs/2112.09924)

In order to address increasing demands of real-world applications, the research for knowledge-intensive NLP (KI-NLP) should advance by capturing the challenges of a truly open-domain environment: web-scale knowledge, lack of structure, inconsistent quality and noise. To this end, we propose a new setup for evaluating existing knowledge intensive tasks in which we generalize the background corpus to a universal web snapshot. We investigate a slate of NLP tasks which rely on knowledge - either factual or common sense, and ask systems to use a subset of CCNet - the Sphere corpus - as a knowledge source. In contrast to Wikipedia, otherwise a common background corpus in KI-NLP, Sphere is orders of magnitude larger and better reflects the full diversity of knowledge on the web. Despite potential gaps in coverage, challenges of scale, lack of structure and lower quality, we find that retrieval from Sphere enables a state of the art system to match and even outperform Wikipedia-based models on several tasks. We also observe that while a dense index can outperform a sparse BM25 baseline on Wikipedia, on Sphere this is not yet possible. To facilitate further research and minimise the community's reliance on proprietary, black-box search engines, we share our indices, evaluation metrics and infrastructure.
