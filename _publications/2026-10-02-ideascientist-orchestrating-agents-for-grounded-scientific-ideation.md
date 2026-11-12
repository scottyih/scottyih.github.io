---
title: "IdeaScientist: Orchestrating Agents for Grounded Scientific Ideation"
collection: "publications"
permalink: "/publication/2026-10-02-ideascientist-orchestrating-agents-for-grounded-scientific-ideation"
date: 2026-10-02
author: "Jiarui Liu, Renjie Tao, Yiwei Liao, Chuanyang Jin, Kai Sun, Xiao Yang, Xinyuan Zhang, Xilun Chen, Zhuangqun Huang, Lechen Zhang, Yongjin Yang, Yinghui He, Weihao Xuan, Rakesh Wanga, Anuj Kumar, Mona T. Diab, Wen-tau Yih, Xin Luna Dong"
venue: "arXiv preprint"
paperurl: "https://arxiv.org/abs/2610.04074"
biburl: "/publications/2026-10-02-ideascientist-orchestrating-agents-for-grounded-scientific-ideation.txt"
source_urls: ["https://arxiv.org/abs/2610.04074", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:WC23djZS0W4C"]
highlight: "Specialized agents find research gaps, develop ideas from analogous problems, and turn those ideas into grounded proposals."
code: "https://github.com/jiarui-liu/IdeaScientist"
dataset: "https://huggingface.co/datasets/Jerry999/SvalbardIdeaVault"
---

[Read the paper](https://arxiv.org/abs/2610.04074)

Despite rapid progress in automating scientific research, generating promising and well grounded research solutions remains a central challenge. We isolate research ideation as a standalone task and build our solution on the intuition that a challenge in one field can often be addressed by a mechanism that solved an analogous challenge in another. Accordingly, we introduce IdeaScientist, which decomposes ideation into gap finding, innovation, and report writing, and trains each role with reinforcement learning. These roles identify limitations in related work, draw solution intuitions from analogous problem settings, and develop those intuitions into complete research proposals. To facilitate discovery of insights across domains, we construct the Svalbard Idea Vault, a corpus of 2.77M decomposed research ideas for retrieval, training, and temporally controlled evaluation. Our evaluation restricts access to literature available before a cutoff date and assesses how closely proposed directions align with those later explored in 15K papers authored by human researchers. On Qwen3.6-27B, IdeaScientist outperforms the strongest open-source autoresearch baseline by 14.0%, driven mainly by gains in novelty. On this 27B open backbone, IdeaScientist even outperforms Claude Code SDK with Claude-4.8-Opus and Codex SDK with GPT-5.4, by up to 5.9%.
