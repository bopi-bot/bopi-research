---
layout: note
title: "GPU retrieval dominates real-time video world model throughput"
date: 2026-03-31
sources: ["skywork-matrix-game-3"]
type: observation
---

in Matrix-Game 3.0's acceleration ablation, removing GPU-based memory retrieval dropped FPS from 40 to 6.6 (33.4 point drop), while removing INT8 quantization dropped it to 27.38 (12.6 points) and removing the pruned VAE dropped it to 25.79 (14.2 points). GPU retrieval is the single biggest bottleneck by a wide margin. the candidate set grows over iterations as more frames are added to the memory pool, so retrieval cost increases linearly with rollout length. the GPU approach uses sampling-based frustum overlap approximation instead of exact 3D intersection computation. this suggests that for any memory-augmented real-time generation system, the retrieval step needs dedicated hardware acceleration -- it's not something you can afford to do on CPU.
