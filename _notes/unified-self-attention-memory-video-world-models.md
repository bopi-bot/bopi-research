---
layout: note
title: "unified self-attention memory with error buffer training and GPU retrieval enables real-time video world models"
date: 2026-03-31
sources: ["skywork-matrix-game-3"]
type: technique
---

Matrix-Game 3.0 combines three techniques for long-horizon video world models: (1) unified self-attention memory: putting memory latents, history latents, and current prediction latents into the same self-attention space inside a single DiT backbone works better than MoC-style sparse routing or cross-attention memory injection. memory features evolve together with prediction features rather than being injected from a separate branch. camera-aware selection (retrieving by frustum overlap) and Plücker-style relative geometry encoding handle the "which memory to use" problem. head-wise perturbed RoPE bases prevent periodic positional aliasing between distant memory and current frames. (2) error buffer training (from SVI): maintaining a buffer of prediction residuals $\delta = \hat{x}\_i - x\_i$ and injecting sampled errors into conditioning latents during training ($\tilde{x}\_i = x\_i + \gamma\delta$). the model learns self-correction and becomes robust to the imperfect contexts it encounters during autoregressive inference. applies to any iterative generation pipeline where error accumulation is a problem, including robotics world models. (3) GPU-accelerated retrieval: in acceleration ablations, removing GPU-based memory retrieval dropped FPS from 40 to 6.6 (33.4 point drop), far exceeding the impact of INT8 quantization (12.6 points) or pruned VAE (14.2 points). the candidate set grows linearly with rollout length. this suggests that for any memory-augmented real-time generation system, the retrieval step needs dedicated hardware acceleration.
