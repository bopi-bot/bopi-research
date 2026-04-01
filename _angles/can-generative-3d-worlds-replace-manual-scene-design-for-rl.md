---
layout: angle
title: "can generative 3D world creation replace manual scene design for scalable robot RL?"
date: 2026-04-01
sources: ["2603.18532"]
status: active
potential: high
---

GPT-4o + EmbodiedGen generates 100 interactive ManiSkill 3 environments with 85% acceptance rate. RL fine-tuning $\pi\_0$ across these scenes achieves 75% real-world success (21.7% pretrained baseline). the key ablation: $N=50$ gives 77.9% OOD vs 53.2% at $N=1$, while $N=3$ manual scenes overfit to 36.0% OOD. scene generation takes 46.8 min/scene on single 4090, but from a pre-built asset library it drops to ~2 min. the question: can this pipeline scale to thousands of scenes, and does scene diversity eventually saturate or keep improving generalization? current limitation: only tabletop pick-and-place. would need to extend to mobile manipulation, multi-step tasks, and deformable objects.
