---
title: "MemoProAgent: Toward Memory-Driven Proactive Assistance"
collection: "publications"
permalink: "/publication/2026-10-15-memoproagent-toward-memory-driven-proactive-assistance"
date: 2026-10-15
author: "Shenglai Zeng, Xiao Yang, Tiffany Ma, Xinyuan Zhang, Nanshu Wang, Deren Lei, Kai Sun, Xilun Chen, Tammy Stark, Xianhui Zhu, Yuetai Li, Rulin Shao, Tianxin Wei, Rakesh Wanga, Anuj Kumar, Jiliang Tang, Wen-tau Yih, Xin Luna Dong"
venue: "arXiv preprint"
paperurl: "https://arxiv.org/abs/2610.22671"
biburl: "/publications/2026-10-15-memoproagent-toward-memory-driven-proactive-assistance.txt"
source_urls: ["https://arxiv.org/abs/2610.22671", "https://scholar.google.com/citations?view_op=view_citation&hl=en&oe=ASCII&user=8rDNIMsAAAAJ&pagesize=100&sortby=pubdate&citation_for_view=8rDNIMsAAAAJ:PYBJJbyH-FwC"]
code: "https://github.com/facebookresearch/Memo-Pro-Agent"
dataset: "https://huggingface.co/datasets/facebook/MemProBench"
---

[Read the paper](https://arxiv.org/abs/2610.22671)

As assistants move from reactive answering toward proactive intervention, memory changes role: it no longer only supplies the answer to a query, it determines whether and when to speak at all. Prior work in this setting hands the system the relevant fact in context; we study the regime that makes the problem hard, where the evidence justifying an intervention must be mined from a long-horizon personal memory. We introduce MemoProBench, a benchmark for memory-driven proactive assistance (MPA), pairing egocentric video with year-long, distractor-rich user memories (~618K tokens on average), human-verified trigger windows, and a protocol that scores content and timing jointly. Every baseline we evaluate performs poorly (at most 15%), including frontier models given summarized or retrieval-augmented memory. A controlled study explains why: with oracle evidence delivered inside the trigger window GPT-5.3-Chat reaches 96%; letting it choose the timing drops it to 38%, and replacing oracle evidence with retrieval drops it to 15%. Content and timing are separately necessary, and missing either is catastrophic. Guided by this, we build MemoProAgent with a plug-and-play harness that surfaces memory from a graph-organized store and gates it down to what is worth interrupting for, plus a lightweight RL stage that curbs early and repeated firing. Without any training, MemoProAgent lifts strict accuracy from below 10% to 37.5% on Qwen3.8-27B and 38% on GPT-5.3-Chat; RL post-training reaches 42.4%.
