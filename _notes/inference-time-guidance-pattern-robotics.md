---
layout: note
title: "inference-time guidance is becoming a standard pattern for bridging generalist policies and physical constraints"
date: 2026-03-30
sources: ["2603.25038", "2603.24806"]
type: pattern
---

AirVLA injects a physics-aware gradient correction into $\pi\_0$'s flow-matching sampler at inference time to compensate for payload dynamics on a drone, without retraining. FODMP distills a multi-step diffusion policy into a one-step consistency model, achieving real-time speed while preserving temporal motion structure. in both cases, the solution doesn't require architectural changes to the base policy -- it works by modifying the sampling/generation process at deployment. UMI-on-Air and Fast-dVLA's real-time chunking follow the same pattern. the recurring theme: inference-time interventions (guidance signals, consistency distillation, chunked inpainting) are emerging as the preferred way to adapt generalist robot policies to new embodiments and constraints, rather than fine-tuning from scratch.
