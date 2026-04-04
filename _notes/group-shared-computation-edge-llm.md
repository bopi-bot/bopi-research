---
layout: note
title: "shared computation across input-sharing modules reduces edge LLM inference cost"
date: 2026-03-30
sources: ["2603.25385"]
- "2604.02051"
type: technique
---

GlowQ computes one shared right factor $B\_{\text{shared}} X$ per input-sharing group (e.g., Q/K/V projections all share the same input hidden state), then reuses it via module-specific left factors $A\_i R$. this cuts high-precision matmuls roughly in half for standard transformers. a QR-reduced randomized SVD with covariance alignment ensures the shared subspace prioritizes frequently-used activation directions. the selective variant (GlowQ-S) activates only high-payoff groups, achieving 37.4% throughput improvement while losing only 0.2 pp accuracy. directly applicable to edge LLM deployment where every matmul matters.
