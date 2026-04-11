---
layout: note
title: "fast-slow decomposition pattern emerges across inference, planning, and world modeling"
date: 2026-04-05
sources: ["2603.14498", "2604.01681", "2604.01577", "2604.03208", "2604.04502", "2604.05672", "2604.07957"]
type: pattern
---

three very different systems converge on the same architectural insight. R3DP uses asynchronous fast-slow collaboration (AFSC) for 3D manipulation inference: a frozen VGGT runs every $\tau=8$ frames to produce 3D-aware features, while a lightweight TFPNet (DINOv2-S + 4 alternating-attention blocks) propagates to intermediate frames. this gives 44.8% latency reduction (40.3ms vs 73.1ms) with only 3.3pp accuracy loss. agentic fast-slow planning (AFSP) decomposes autonomous driving into slow LLM reasoning (4.13s) for scene understanding and fast MPC (10Hz) for trajectory tracking, reducing lateral deviation by 45%. FSRM (thinking while listening) interleaves fast recurrent latent updates with slow observation updates for long-horizon sequential modeling, achieving ~60% OOD accuracy on maze tasks vs 20-30% for baselines. the common thread: systems operating over multiple timescales benefit from explicit separation of fast reactive and slow deliberative paths. none use uniform processing -- they all route through differently-sized modules.
