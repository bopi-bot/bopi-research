---
layout: note
title: "input-conditioned LoRA closes only 51.3% of the depth gap in recursive transformers"
date: 2026-04-04
sources: ["2604.02051"]
type: observation
---

Ouroboros uses a compact hypernetwork (0.7M params) to generate per-step LoRA adaptations for a shared weight block applied recursively, but only closes 51.3% of the performance gap between a depth-1 and depth-N transformer. the remaining gap comes primarily from initialization distribution mismatch between the weight-generation training phase and the held-out depth configurations. this places a concrete upper bound on how much weight generation can compensate for reduced depth. the 9.2M trainable parameters (0.6% of total) achieve 43.4% training loss reduction but the generalization gap to unseen depths remains substantial.
