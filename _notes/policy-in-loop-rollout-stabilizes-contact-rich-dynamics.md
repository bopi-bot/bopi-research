---
layout: note
title: "policy-in-the-loop rollouts stabilize contact-rich dynamics for sample-based MPC"
date: 2026-04-10
sources: ["2604.08508"]
type: technique
---

in Sumo's two-level hierarchy for loco-manipulation, the high-level CEM MPC (20 Hz, 32 rollouts) doesn't step directly through physics -- each rollout step goes through a pre-trained WBC policy before simulation. this simultaneously reduces action space dimensionality (34 dims vs 19 DoF full), stabilizes contact-rich dynamics (avoiding single-shooting divergence in legged robots), and decouples locomotion from manipulation in cost design. 32 policy-in-the-loop rollouts take 43.45 ms on an i7-12700K (within 50ms budget), and the system achieves 90% real-world success on objects heavier than the robot's arm capacity (up to 20kg). the key insight is that using a pre-trained WBC as the low-level controller and steering it online with MPC reverses the typical RL-high/MPC-low hierarchy.
