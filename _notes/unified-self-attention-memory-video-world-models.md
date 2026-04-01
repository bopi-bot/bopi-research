---
layout: note
title: "unified self-attention for memory outperforms separate memory branches in video world models"
date: 2026-03-31
sources: ["skywork-matrix-game-3"]
type: observation
---

Matrix-Game 3.0 tested two approaches for long-horizon memory: (1) MoC-style sparse long-context routing (unreliable similarity at high noise, expensive), and (2) cross-attention memory injection with geometry cues (slow convergence, misaligned features). they found that putting memory latents, history latents, and current prediction latents into the same self-attention space inside a single DiT backbone works best. memory features evolve together with prediction features rather than being injected from a separate branch. camera-aware selection (retrieving by frustum overlap) and Plücker-style relative geometry encoding handle the "which memory to use" problem. head-wise perturbed RoPE bases ($\hat{\theta}\_h = \theta\_{\text{base}}(1 + \sigma\_\theta \epsilon\_h)$) prevent periodic positional aliasing between distant memory and current frames.
