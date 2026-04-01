---
layout: angle
title: "can RL post-training replace architectural complexity in stabilizing world model rollouts?"
date: 2026-03-29
source: "2603.25685"
status: active
---

the persistent robot world models paper shows that post-training a diffusion world model on its own autoregressive rollouts via RL dramatically stabilizes long-horizon predictions. this is a training-time intervention rather than an architectural one. LeWorldModel (2603.19312) takes the opposite approach: simplify the architecture to make training inherently stable. Matrix-Game 3.0 (skywork-matrix-game-3) uses a third approach entirely: error buffer training (from SVI) that injects prediction residuals into conditioning latents so the base model learns self-correction, plus camera-aware memory retrieval in unified self-attention. which path scales better? can RL post-training fix any world model, or does architectural simplicity (like LeWM's Gaussian prior) still win for training from scratch? and does error-aware training make RL post-training unnecessary?
