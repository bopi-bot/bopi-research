---
layout: note
title: "drifting models enable offline trajectory optimization from heterogeneous datasets without forward simulation"
date: 2026-04-08
sources: ["2604.04528"]
type: technique
---

Drifting MPC (Foffano et al. 2026) learns a one-step conditional trajectory generator from offline data, then uses exponential tilting ($e^{-\beta J}$) to bias generation toward low-cost trajectories at inference time. this avoids the fundamental problem with forward-model-based planning: you can't simulate trajectories when dynamics are unknown. instead, it directly learns the trajectory distribution from data and "tilts" it toward optimality. the approach achieves 40-52x speedup over diffusion planners at horizon $H=100$ with only 17-32% cost gap to oracle. the tilted distribution provably solves a KL-regularized optimal control problem (Theorem 1), and best-of-M$\_{\text{plan}}$ sampling provides planning guarantees (Theorem 2).
