---
layout: note
title: "steering vectors operate primarily through the OV circuit, not QK attention"
date: 2026-04-13
sources: ["2604.08524"]
type: observation
---

activation patching on steering vectors for refusal across gemma 2 2B and llama 3.2 3B shows that steering vectors interact almost exclusively with the attention mechanism's OV (output-value) circuit. freezing all attention scores (zeroing out the QK contribution) drops steering performance by only 8.75% across both model families. a mathematical decomposition of the steered OV circuit ($	ext{svv}^h = (s \odot \gamma) W\_{OV}^h$) reveals that the steering vector value (SVV) accounts for 74.9% of the total OV effect. the residual 25.1% comes from the steering-induced scaling of attention weights, which is a secondary effect.

this means steering vectors rewrite what information flows out of attention heads, not what information heads attend to. the QK circuit is largely bypassed. this has practical implications: sparsifying steering vectors to 1-10% of their dimensions retains most performance, and different steering methodologies (DIM, contrastive activation patching, RLHF-based) agree on overlapping important dimensions (IoU > 0.5 with $p \lesssim 10^{-10}$).

the finding also means that SAE decomposition of the OV circuit should be the primary target for understanding and improving steering, not attention pattern analysis.
