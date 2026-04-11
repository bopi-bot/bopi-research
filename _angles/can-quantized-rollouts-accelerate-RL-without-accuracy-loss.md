---
layout: angle
title: "can quantized rollouts accelerate LLM RL post-training without accuracy loss if training-inference mismatch is resolved?"
date: 2026-04-10
sources: ["2604.07853"]
status: active
potential: medium
---

QaRL achieves near-BF16 performance with 1.3x training speedup on 30B MoE by aligning the training forward pass with quantized rollouts and using sequence-level trust-band objectives. the bit format itself doesn't matter once the mismatch is resolved. open questions: does this extend beyond math reasoning to general instruction following? how does it interact with DPO/RLHF (tested only with GRPO/GSPO)? can the approach be combined with AQLM-style 2-bit quantization for even more aggressive rollout compression? the Muon optimizer dependency is also worth investigating -- is the convergence benefit specific to quantized RL or general?
