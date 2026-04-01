---
layout: angle
title: "can VLA models that jointly generate future observations and actions replace separate world model modules?"
date: 2026-03-29
sources: ["2603.25406", "2603.25038", "2603.24806", "2603.26320", "2603.18532", "2603.14498"]
status: active
potential: critical
---

MMaDA-VLA generates future goal observations alongside action chunks in a unified diffusion framework, achieving 98% on LIBERO without any separate world model. LaMP uses 3D scene flow as a latent motion prior. AirVLA transfers $\pi\_{0}$ to aerial manipulation via inference-time guidance, showing the base VLA captures enough dynamics to work across embodiments with targeted interventions. FODMP replaces multi-step diffusion with one-step consistency distillation while preserving temporal motion structure, making VLAs fast enough for dynamic tasks like ball catching. DFM-VLA (2603.26320) achieves 95.7% on LIBERO and 70.8% on real bimanual tasks using discrete flow matching for iterative action refinement -- no world model, no vision generation, just better action decoding. generative sim-to-real RL (2603.18532) shows RL fine-tuning VLAs directly in diverse simulated 3D worlds transfers to real robots at 75% success, without any explicit world model component. R3DP (2603.14498) demonstrates that injecting 3D foundation model priors via fast-slow feature propagation into a diffusion policy achieves 69% on RoboTwin vs 59.9% for $\pi\_0$, purely through better perception architecture. the trajectory is clear: VLAs are becoming more capable, faster, and more transferable without explicit world models. the remaining question is whether this trajectory extends to long-horizon manipulation in cluttered real-world environments where predicting future states might still be necessary.
