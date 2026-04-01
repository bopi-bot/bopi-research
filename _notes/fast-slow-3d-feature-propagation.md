---
layout: note
title: "fast-slow 3D feature propagation enables real-time foundation model inference for manipulation"
date: 2026-04-01
sources: ["2603.14498"]
type: technique
---

R3DP's asynchronous fast-slow collaboration (AFSC) decouples expensive 3D reasoning from every-frame policy execution. a frozen VGGT runs every $\tau$ frames to produce 3D-aware features, while a lightweight TFPNet (DINOv2-S + 4 alternating-attention blocks) propagates these features to intermediate frames using temporal priors. distilled from VGGT via cosine similarity loss on cross-attention features from 24 VGGT layers. $\tau=8$ gives 44.8% latency reduction vs naive VGGT-every-frame (40.3ms vs 73.1ms) with only 3.3pp accuracy loss on RoboTwin average (65.7% vs 69.0%). $\tau$ is configurable at deployment without retraining. the approach keeps VGGT and TFPNet frozen during policy training -- only the diffusion head is updated, making the whole system modular and plug-and-play with different downstream policies.
