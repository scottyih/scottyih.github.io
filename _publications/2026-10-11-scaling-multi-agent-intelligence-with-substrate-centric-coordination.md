---
title: "Scaling Multi-Agent Intelligence with Substrate-Centric Coordination"
collection: "publications"
permalink: "/publication/2026-10-11-scaling-multi-agent-intelligence-with-substrate-centric-coordination"
date: 2026-10-11
author: "Zhenting Qi, Zhuokai Zhao, Rulin Shao, Kerem Oktar, Zhiyuan Yao, Himabindu Lakkaraju, Wen-tau Yih, Ansong Ni, Bhargavi Paranjape, Yilun Du"
venue: "arXiv preprint"
paperurl: "https://arxiv.org/abs/2610.16120"
biburl: "/publications/2026-10-11-scaling-multi-agent-intelligence-with-substrate-centric-coordination.txt"
source_urls: ["https://arxiv.org/abs/2610.16120", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:wKETBy42zhYC"]
---

[Read the paper](https://arxiv.org/abs/2610.16120)

Existing large language model (LLM) based multi-agent systems have been shown to scale poorly, and we identify three problems: reading burden that grows with the group, useful information diluted by shared work of unknown quality, and fragility to failed agents. We argue that the problems are largely due to agent-centric designs: the coordination structure is wired into fixed workflows, central coordinators, or peer-to-peer messaging, and recent blackboard-style methods that move the coordination into a shared medium relieve only the last problem. To close the gaps, we build ScaleMAS, where asynchronous agents interact with a shared datastore of linked messages via three operations: publishing messages with optional references to earlier ones that they build on, searching for messages by content, and visiting messages by address. Search returns at most $k$ messages, so an agent's read stays bounded at any group size; results are ranked by relevance and by how often they are cited, which we find to be an effective proxy for quality; and messages persist after their producers leave, so the group carries on when individual agents fail. Across four agentic tasks, ScaleMAS outperforms agent-centric and blackboard-style baselines at lower inference compute, continues to scale up to 128 agents, and tolerates losing agents midway.
