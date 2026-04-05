---
layout: note
title: "formulating RL policy improvement as posterior inference prevents catastrophic collapse in generative VLA fine-tuning"
date: 2026-04-05
sources: ["2604.01860"]
type: technique
---

POCO reformulates policy improvement in generative policies as a posterior inference problem. instead of directly optimizing policy parameters with RL gradients (which causes catastrophic forgetting in pretrained VLA models), POCO runs an EM procedure: the E-step creates a reward-weighted implicit posterior over action trajectories, and the M-step distills this posterior into the policy using a clipped surrogate objective (borrowing the clipping idea from PPO). this offline-to-online approach anchors exploration to the pretrained prior while allowing targeted improvement, achieving 96.7% real-world success across 4 contact-rich tasks. the key design choice is operating at the chunk level (action sequences, not single steps) which aligns naturally with flow-matching VLA architectures like $\pi\_0.5$.
