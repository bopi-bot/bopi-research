---
layout: note
title: "zero-initialized cross-attention gates preserve pretrained representations when injecting new modalities"
date: 2026-04-05
sources: ["2604.02327"]
type: technique
---

SteerViT injects text conditioning into pretrained DINOv2 via lightweight cross-attention layers at $\alpha\_\ell = 0$ initialization. at initialization, the gated cross-attention output is zero, so the modified ViT behaves identically to the original. during training, the gates gradually open to admit text influence. this is the same zero-init strategy used in LoRA adapters and in VLMs like Flamingo, but applied here to visual representation steering rather than language generation. the benefit is clear: you don't need to retrain the visual encoder from scratch, and the original representation quality is preserved for tasks where steering isn't needed. SteerViT omits Flamingo's FFN gating (saves 67% of added parameters) while matching or outperforming dedicated approaches on anomaly detection and personalized object discrimination.
