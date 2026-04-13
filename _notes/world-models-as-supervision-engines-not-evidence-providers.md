---
layout: note
title: "world models are more valuable as supervision engines than as test-time evidence providers"
date: 2026-04-10
sources: ["2604.07957", "2604.08168", "2604.07712", "2604.08544"]
type: observation
---

WorldMAP shows that using a world model to generate imagined future views, then converting those into semantic-spatial memory + BEV cost maps + FMM planning trajectories, and distilling the result into a lightweight student produces 4.4x better trajectory prediction (ADE 42.06 vs 183.93) than the raw VLM. critically, mindjourney (o3 + world model as evidence at test time) actually underperforms direct o3 (152.41 vs 112.14 ADE) -- imagined evidence hurts when not converted into persistent structure. the world model's value is in the supervision pipeline (teacher), not at inference (student runs independently). neither supervision source alone suffices: GT-only gives ADE 78.34, WM-only gives 95.98, but GT+WM gives 42.06.

ViVa (2604.08168) extends this pattern to robot RL: repurposing a pretrained video generator (Wan2.2) as a value function rather than using it for prediction. the video generator's spatiotemporal priors about how scenes evolve provide better value signals than static VLM-based value functions (73% vs 58% success on box assembly). the generative model's value comes from its internal dynamics model, not from generating explicit future frames at test time -- ViVa uses only 1 DDIM step at inference.

CausalVAE (2604.07712) adds another dimension: a plug-in causal structural module that makes world model latents interpretable and intervention-aware without changing the backbone. the learned DAG recovers first-order physical interaction trends, and counterfactual retrieval improves by up to +302% on Physics 3-body. this suggests world models can also serve as supervision engines for causal discovery, not just for policy training.
