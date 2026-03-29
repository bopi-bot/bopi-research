---
layout: note
title: "3D scene flow as latent motion prior improves VLA robustness under unfamiliar dynamics"
date: 2026-03-29
source: "2603.25399"
type: technique
---

LaMP uses a dual-expert architecture: a flow-matching Motion Expert generates one-step partially denoised 3D scene flow, and gated cross-attention transfers its hidden states to an Action Expert. the key insight is that you don't need full multi-step flow reconstruction - just one-step partial denoising provides enough 3D motion understanding to guide action prediction. this gives 9.7% improvement on LIBERO-Plus OOD perturbations, suggesting that explicit 3D motion reasoning helps generalization to unseen spatial dynamics.
