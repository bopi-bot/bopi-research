---
layout: note
title: "predicting in VFM feature space reduces world model parameters by 35x while matching or exceeding pixel-level models"
date: 2026-04-08
sources: ["2604.04913"]
type: observation
---

DeltaTok shows that predicting future frames in the feature space of a vision foundation model (DINOv2-g at 768-dim) instead of a pixel-reconstruction latent space requires dramatically fewer world model parameters. DeltaWorld (~0.3B) matches or exceeds Cosmos-12B on dense forecasting benchmarks (segmentation mIoU 54.6 vs 52.8, depth $\delta\_1$ 0.947 vs 0.944) with 35x fewer parameters and 2,000x fewer FLOPs. the key compression comes from encoding each frame difference as a single 768-dim continuous token (1,024x reduction from 512x512 feature maps), making the world model's job fundamentally easier -- it only needs to predict how the VFM embedding changes between frames, not reconstruct pixels.
