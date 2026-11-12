---
title: "Procedural Knowledge at Scale Improves Reasoning"
collection: "publications"
permalink: "/publication/2026-04-01-procedural-knowledge-at-scale-improves-reasoning"
date: 2026-04-01
author: "Di Wu, Devendra Singh Sachan, Wen-tau Yih, Mingda Chen"
venue: "COLM 2026"
paperurl: "https://arxiv.org/abs/2604.01348"
biburl: "/publications/2026-04-01-procedural-knowledge-at-scale-improves-reasoning.txt"
source_urls: ["https://arxiv.org/abs/2604.01348", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:7BrZ7Jt4UNcC"]
code: "https://github.com/facebookresearch/reasoning-memory"
---

[Read the paper](https://arxiv.org/abs/2604.01348)

Test-time scaling has emerged as an effective way to improve language models on challenging reasoning tasks. However, most existing methods treat each problem in isolation and do not systematically reuse knowledge from prior reasoning trajectories. In particular, they underutilize procedural knowledge: how to reframe a problem, choose an approach, and verify or backtrack when needed. We introduce \textbf{Reasoning Memory}, a retrieval-augmented generation (RAG) framework for reasoning models that explicitly retrieves and reuses procedural knowledge at scale. Starting from existing corpora of step-by-step reasoning trajectories, we decompose each trajectory into self-contained subquestion-subroutine pairs, yielding a datastore of 32 million compact procedural knowledge entries. At inference time, a lightweight in-thought prompt lets the model verbalize the core subquestion, retrieve relevant subroutines within its reasoning trace, and reason under diverse retrieved subroutines as implicit procedural priors. Across six math, science, and coding benchmarks, Reasoning Memory consistently outperforms RAG with document, trajectory, and template knowledge, as well as a compute-matched test-time scaling baseline. With a higher inference budget, averaged across models and tasks, it improves over no retrieval by 19.5% and over the compute-matched baseline by 8.9%. Ablation studies show that these gains come from two key factors: the broad procedural coverage of the source trajectories and our decomposition and retrieval design, which together enable effective extraction and reuse of procedural knowledge. Our experiment code is available at https://github.com/facebookresearch/reasoning-memory.
