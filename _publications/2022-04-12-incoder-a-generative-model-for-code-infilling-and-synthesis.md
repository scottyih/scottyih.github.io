---
title: "InCoder: A Generative Model for Code Infilling and Synthesis"
collection: "publications"
permalink: "/publication/2022-04-12-incoder-a-generative-model-for-code-infilling-and-synthesis"
date: 2023-01-01
author: "Daniel Fried, Armen Aghajanyan, Jessy Lin, Sida Wang, Eric Wallace, Freda Shi, Ruiqi Zhong, Wen-tau Yih, Luke Zettlemoyer, Mike Lewis"
venue: "ICLR 2023"
paperurl: "https://arxiv.org/abs/2204.05999"
biburl: "/publications/2022-04-12-incoder-a-generative-model-for-code-infilling-and-synthesis.txt"
source_urls: ["https://arxiv.org/abs/2204.05999", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:vbGhcppDl1QC"]
project: "https://sites.google.com/view/incoder-code-models/"
code: "https://github.com/dpfried/incoder"
model:
  - "https://huggingface.co/facebook/incoder-1B"
  - "https://huggingface.co/facebook/incoder-6B"
---

[Read the paper](https://arxiv.org/abs/2204.05999)

Code is seldom written in a single left-to-right pass and is instead repeatedly edited and refined. We introduce InCoder, a unified generative model that can perform program synthesis (via left-to-right generation) as well as editing (via infilling). InCoder is trained to generate code files from a large corpus of permissively licensed code, where regions of code have been randomly masked and moved to the end of each file, allowing code infilling with bidirectional context. Our model is the first generative model that is able to directly perform zero-shot code infilling, which we evaluate on challenging tasks such as type inference, comment generation, and variable re-naming. We find that the ability to condition on bidirectional context substantially improves performance on these tasks, while still performing comparably on standard program synthesis benchmarks in comparison to left-to-right only models pretrained at similar scale. The InCoder models and code are publicly released. https://sites.google.com/view/incoder-code-models
