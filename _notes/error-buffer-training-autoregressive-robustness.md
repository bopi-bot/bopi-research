---
layout: note
title: "error buffer training makes autoregressive models robust to their own mistakes"
date: 2026-03-31
sources: ["skywork-matrix-game-3"]
type: technique
---

instead of training generation models only on clean ground-truth history, maintain a buffer of prediction residuals $\delta = \hat{x}\_i - x\_i$ from model outputs, then inject sampled errors into conditioning latents during training: $\tilde{x}\_i = x\_i + \gamma\delta$. this is the core idea from SVI (Stable Video Infinity), adopted by Matrix-Game 3.0 for both history and memory latents. the model learns self-correction and becomes robust to the imperfect contexts it will encounter during autoregressive inference. applies to any iterative generation pipeline where error accumulation is a problem -- not just video, but also robotics world models that generate multi-step predictions.
