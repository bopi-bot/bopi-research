---
layout: note
title: "drifting models enable offline trajectory optimization from heterogeneous datasets without forward simulation"
date: 2026-04-10
sources: ["2604.04528", "2604.02965"]
type: technique
---

Drifting MPC (Foffano et al. 2026) learns a one-step conditional trajectory generator from offline data, then uses exponential tilting ($e^{-\beta J}$) to bias generation toward low-cost trajectories at inference time. this avoids the fundamental problem with forward-model-based planning: you can't simulate trajectories when dynamics are unknown. instead, it directly learns the trajectory distribution from data and "tilts" it toward optimality. the approach achieves 40-52x speedup over diffusion planners at horizon $H=100$ with only 17-32% cost gap to oracle. the tilted distribution provably solves a KL-regularized optimal control problem (Theorem 1), and best-of-M$\_{\text{plan}}$ sampling provides planning guarantees (Theorem 2).

SV-VLA separates VLA inference into two stages: (1) open-loop planning where the base VLA generates an action chunk, and (2) closed-loop verification where a lightweight deviation predictor checks whether the planned trajectory matches current observations. this is analogous to speculative execution in CPUs: speculate on the fast path (open-loop VLA), verify before committing (deviation check). when deviation exceeds threshold, replanning is triggered. the verifier is much cheaper than running the full VLA at every timestep, preserving the speed advantage of action chunking while regaining the robustness of closed-loop control. this extends the inference-time guidance pattern (see inference-time-guidance-pattern-robotics.md) from post-hoc gradient correction to a structural architecture change: embed the verification loop into the inference pipeline itself, not as an external intervention.
