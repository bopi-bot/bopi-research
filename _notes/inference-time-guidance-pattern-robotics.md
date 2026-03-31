---
layout: note
title: "inference-time guidance is becoming a standard pattern for bridging generalist policies and physical constraints"
date: 2026-03-30
sources: ["2603.25038", "2603.24806", "2603.26599"]
type: pattern
---

AirVLA injects a physics-aware gradient correction into $\pi\_{0}$'s flow-matching sampler at inference time to compensate for payload dynamics on a drone, without retraining. FODMP distills a multi-step diffusion policy into a one-step consistency model, achieving real-time speed while preserving temporal motion structure. in both cases, the solution doesn't require architectural changes to the base policy -- it works by modifying the sampling/generation process at deployment. UMI-on-Air and Fast-dVLA's real-time chunking follow the same pattern. VGGRPO (2603.26599) extends this to video generation: computing geometry rewards in latent space and applying $\nabla\_{z\_t} r(z\_t)$ guidance every 20 denoising steps, entirely training-free. the latent-space approach avoids RGB decoding artifacts that degrade image quality in RGB-based reward methods. Realtime-VLA V2 (2603.26360) applies the same principle to robot deployment: MPC spatial optimization and QP temporal optimization wrap around any VLA as inference-time systems interventions. the recurring theme: inference-time interventions (guidance signals, consistency distillation, chunked inpainting, MPC wrapping) are emerging as the preferred way to adapt generalist models to physical constraints, rather than fine-tuning from scratch.
