---
layout: angle
title: "can fast-slow inference patterns make foundation 3D models practical for real-time robot control?"
date: 2026-04-01
sources: ["2603.14498", "2604.01681", "2604.01577", "2604.05672"]
status: active
potential: high
---

R3DP demonstrates that running VGGT every $\tau=8$ frames and propagating features via a lightweight TFPNet reduces 3D inference cost by 44.8% (40.3ms vs 73.1ms) with minimal accuracy loss. but the pattern now extends well beyond 3D inference. AFSP applies it to planning: slow LLM reasoning for scene understanding (4.13s) paired with fast MPC for trajectory tracking (10Hz), cutting lateral deviation by 45%. FSRM uses fast-slow recurrence in world model latent dynamics: fast recurrent updates between slow observation steps, achieving 60% OOD accuracy on maze tasks vs 20-30% for uniform baselines. AnchorVLA's residual correction module at 50Hz paired with slow diffusion head firing every H steps is another instance. the pattern is now confirmed across 4 domains (3D perception, planning, world modeling, VLA policy). the open question is whether a universal fast-slow decomposition can be learned automatically rather than designed by hand.
