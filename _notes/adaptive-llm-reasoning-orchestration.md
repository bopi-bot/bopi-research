---
layout: note
title: "RL-learned orchestration policy decides when and how much to invoke LLM reasoning on robots"
date: 2026-03-29
source: "2603.16673"
type: technique
---

RARRL learns a high-level policy (via RL) that decides whether to invoke LLM reasoning, which reasoning role to use, and how much compute budget to allocate. trained on ALFRED with empirical latency profiles. improves task success rates while reducing execution latency. the orchestration policy is lightweight compared to the full LLM it controls. directly applicable to resource-constrained embedded robotics where LLM inference costs battery and adds latency.
