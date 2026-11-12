---
title: "Reliable, Adaptable, and Attributable Language Models with Retrieval"
collection: "publications"
permalink: "/publication/2024-03-05-reliable-adaptable-and-attributable-language-models-with-retrieval"
date: 2024-03-05
author: "Akari Asai, Zexuan Zhong, Danqi Chen, Pang Wei Koh, Luke Zettlemoyer, Hannaneh Hajishirzi, Wen-tau Yih"
venue: "arXiv preprint"
paperurl: "https://arxiv.org/abs/2403.03187"
biburl: "/publications/2024-03-05-reliable-adaptable-and-attributable-language-models-with-retrieval.txt"
source_urls: ["https://arxiv.org/abs/2403.03187", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:6ZxmRoH8BuwC"]
---

[Read the paper](https://arxiv.org/abs/2403.03187)

Parametric language models (LMs), which are trained on vast amounts of web data, exhibit remarkable flexibility and capability. However, they still face practical challenges such as hallucinations, difficulty in adapting to new data distributions, and a lack of verifiability. In this position paper, we advocate for retrieval-augmented LMs to replace parametric LMs as the next generation of LMs. By incorporating large-scale datastores during inference, retrieval-augmented LMs can be more reliable, adaptable, and attributable. Despite their potential, retrieval-augmented LMs have yet to be widely adopted due to several obstacles: specifically, current retrieval-augmented LMs struggle to leverage helpful text beyond knowledge-intensive tasks such as question answering, have limited interaction between retrieval and LM components, and lack the infrastructure for scaling. To address these, we propose a roadmap for developing general-purpose retrieval-augmented LMs. This involves a reconsideration of datastores and retrievers, the exploration of pipelines with improved retriever-LM interaction, and significant investment in infrastructure for efficient training and inference.
