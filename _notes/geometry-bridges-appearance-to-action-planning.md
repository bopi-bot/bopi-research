---
layout: note
title: "3D geometry grounding via causal flow-matching bridges appearance modeling to reliable action planning"
date: 2026-04-04
sources: ["2604.01765"]
type: technique
---

DriveDreamer-Policy chains three flow-matching diffusion experts (depth, video, action) on a shared Qwen3-VL-2B backbone via a causal query interface: 64 depth tokens condition 64 video tokens, which condition 8 action tokens. each expert can be independently initialized from pretrained models (depth from PPD, video from Wan-2.1-T2V) while sharing the vision-language backbone. the causal ordering matters: depth is predicted first because it provides geometric grounding, then video for temporal dynamics, then action for control. this is different from discrete token unification (like the unified token space VLAs tracked in another note) because it uses continuous flow-matching for each modality while sharing representations through cross-attention. the key finding: adding 3D depth prediction as an intermediate representation between video generation and action planning consistently improves planning metrics. depth provides geometric structure that 2D appearance alone cannot: spatial relationships between objects, ego-vehicle distance, and obstacle geometry are all more naturally encoded in depth than in RGB. removing the depth expert degrades planning scores significantly. this suggests that purely appearance-based world models may hit a ceiling for manipulation tasks where spatial reasoning matters more than visual fidelity.
