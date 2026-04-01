---
layout: note
title: "scene distribution breadth matters more than RL algorithm for sim-to-real VLA generalization"
date: 2026-04-01
sources: ["2603.18532"]
type: observation
---

PPOFlow on $\pi\_0$ with 100 generated scenes achieves 79.8% sim success, while the same algorithm with 3 manually designed scenes gets 36.0% on the same generated test set (60.7pp gap from overfitting). scaling from $N=1$ to $N=50$ gives +24.7pp OOD improvement (53.2% to 77.9%). the manually designed scenes actually achieve 96.7% on themselves but only 36.0% on generated scenes -- they produce overfitted policies despite identical RL hyperparameters. this strongly suggests that for sim-to-real RL, the diversity of the training distribution dominates over algorithmic sophistication. 5 days on 8x RTX 6000 Ada is sufficient for the RL itself; the bottleneck is generating enough diverse scenes.
