---
title: "Improving Faithfulness of Abstractive Summarization by Controlling Confounding Effect of Irrelevant Sentences"
collection: "publications"
permalink: "/publication/2022-12-19-improving-faithfulness-of-abstractive-summarization-by-controlling-confounding-effect-of-irrelevant-sentences"
date: 2022-12-19
author: "Asish Ghoshal, Arash Einolghozati, Ankit Arun, Haoran Li, Lili Yu, Vera Gor, Yashar Mehdad, Wen-tau Yih, Asli Celikyilmaz"
venue: "arXiv preprint"
paperurl: "https://arxiv.org/abs/2212.09726"
biburl: "/publications/2022-12-19-improving-faithfulness-of-abstractive-summarization-by-controlling-confounding-effect-of-irrelevant-sentences.txt"
source_urls: ["https://arxiv.org/abs/2212.09726", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:ClCfbGk0d_YC"]
---

[Read the paper](https://arxiv.org/abs/2212.09726)

Lack of factual correctness is an issue that still plagues state-of-the-art summarization systems despite their impressive progress on generating seemingly fluent summaries. In this paper, we show that factual inconsistency can be caused by irrelevant parts of the input text, which act as confounders. To that end, we leverage information-theoretic measures of causal effects to quantify the amount of confounding and precisely quantify how they affect the summarization performance. Based on insights derived from our theoretical results, we design a simple multi-task model to control such confounding by leveraging human-annotated relevant sentences when available. Crucially, we give a principled characterization of data distributions where such confounding can be large thereby necessitating the use of human annotated relevant sentences to generate factual summaries. Our approach improves faithfulness scores by 20\% over strong baselines on AnswerSumm \citep{fabbri2021answersumm}, a conversation summarization dataset where lack of faithfulness is a significant issue due to the subjective nature of the task. Our best method achieves the highest faithfulness score while also achieving state-of-the-art results on standard metrics like ROUGE and METEOR. We corroborate these improvements through human evaluation.
