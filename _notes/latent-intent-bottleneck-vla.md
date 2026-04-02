---
layout: note
title: latent intent bottleneck decouples planning from execution in VLA
date: 2026-04-02
sources: ["2603.29844"]
type: observation
---

DIAL introduces a dual-system VLA where System-2 (Qwen2.5-VL-3B) performs latent world modeling -- predicting future ViT feature representations at the intent horizon -- while System-1 (self-attention + DiT with flow matching) acts as a fast inverse dynamics model that converts intents to action chunks. the differentiable intent bottleneck $z\_{\text{intent}}$ is the key: it forces the VLM to compress its reasoning about future states into a compact latent that the fast policy decoder can execute from. this is architecturally different from approaches that generate full future frames (MMaDA-VLA) or reason in language space. the two-stage training (decoupled warmup then end-to-end) is critical -- removing warmup causes a 20-point OOD drop, suggesting the latent intent space needs to stabilize before the policy decoder can learn from it.
