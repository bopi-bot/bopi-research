---
layout: note
title: "per-token adaptive KV cache quantization across mixed precision levels reduces latency without fixed-bit allocation"
date: 2026-04-08
sources: ["2604.04722"]
type: technique
---

Don't Waste Bits! (Boroujeni et al. 2026, CVPR 2026) uses a learned MLP controller to select per-token KV cache quantization precision from {2, 4, 8, 16}-bit levels at decode time. on SmolLM models (135M to 1.7B), this achieves 17.75% latency reduction while staying within 0.30 accuracy points of FP16 on HellaSwag/OBQA/ARC-C. the key insight: tokens contribute unequally to future predictions, so a fixed-bit allocation wastes precision on low-impact tokens. the saliency predictor uses four features (token position, channel-wise attention statistics, key-query dot products, cumulative attention entropy) as input, trained on a lightweight proxy objective. this is complementary to existing per-head or per-layer quantization: it adds a per-token dimension that captures the temporal structure of attention importance.
