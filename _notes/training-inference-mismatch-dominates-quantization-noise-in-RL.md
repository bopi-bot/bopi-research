---
layout: note
title: "training-inference mismatch dominates quantization noise as the failure mode in quantized RL rollouts"
date: 2026-04-10
sources: ["2604.07853"]
type: observation
---

QaRL shows that once the training forward pass is aligned with quantized rollouts (executing actual low-bit GEMM, not fake-quant), RL convergence becomes insensitive to the specific bit format: W4A16, W8A8, and FP8W8A8 all converge similarly under TBPO. the dominant failure mode is the mismatch between the quantized sampler and full-precision learner, which produces "error tokens" -- repetitive, garbled tokens in long responses that concentrate in negative samples and break PPO trust-region control at the token level. sequence-level rejection (TBPO's dual clipping + masking) is essential because token-level clipping cannot handle the error-token contamination that propagates through the autoregressive chain. the practical takeaway: quantized rollouts are viable for RL post-training if you align the training computation and use sequence-level objectives.
