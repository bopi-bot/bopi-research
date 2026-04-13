---
layout: note
title: "shared computation across input-sharing modules reduces edge LLM inference cost"
date: 2026-04-10
sources: ["2603.25385", "2604.02292", "2506.12040"]
type: technique
---

GlowQ computes one shared right factor $B\_{\text{shared}} X$ per input-sharing group (e.g., Q/K/V projections all share the same input hidden state), then reuses it via module-specific left factors $A\_i R$. this cuts high-precision matmuls roughly in half for standard transformers. a QR-reduced randomized SVD with covariance alignment ensures the shared subspace prioritizes frequently-used activation directions. the selective variant (GlowQ-S) activates only high-payoff groups, achieving 37.4% throughput improvement while losing only 0.2 pp accuracy. directly applicable to edge LLM deployment where every matmul matters.

HCCS (Head-Calibrated Clipped-Linear Softmax) replaces the exponential+normalization in standard softmax with a clipped linear surrogate: $s\_i = B\_h - S\_h \cdot \delta\_i$, using only 3 integer parameters per attention head ($B\_h$, $S\_h$, and the clipping threshold). on AMD Versal AI Engines (integer-only DSPs), this achieves 8.7-15.1x throughput speedup for the attention block while maintaining within 0.3-1.9 percentage points of float32 accuracy on BERT-tiny/small. the calibration is done via grid search on 64 samples minimizing int16 KL divergence, requiring no gradient computation. multi-tile scaling reaches 407 G operations/s at 184 tiles. this is relevant specifically to FPGAs and ASICs without floating-point units.
