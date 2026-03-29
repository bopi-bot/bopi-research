---
layout: note
title: "RL post-training on autoregressive rollouts stabilizes video world models"
date: 2026-03-29
source: "2603.25685"
type: technique
---

training world models on their own generated rollouts (rather than ground truth history) via RL dramatically improves long-horizon stability. a contrastive RL objective for diffusion models is adapted - convergence guarantees carry over exactly. generating multiple candidate futures from the same state and rewarding the best ones gives dense training signal. multi-view visual fidelity rewards (LPIPS, SSIM across cameras) provide low-variance supervision. 14% LPIPS reduction on external cameras, 9.1% SSIM improvement on wrist camera on DROID dataset.
