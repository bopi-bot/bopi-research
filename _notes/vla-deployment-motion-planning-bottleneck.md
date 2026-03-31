---
layout: note
title: "VLA deployment speed is bottlenecked by motion planning, not neural inference"
date: 2026-03-31
sources: ["2603.26360"]
type: observation
---

Realtime-VLA V2 reveals that even after optimizing VLA GPU inference to run fast, the dominant bottleneck in real robot deployment is motion planning: constant-speed waypoint execution, unoptimized acceleration profiles, and uncompensated mechanical lag (150ms) make the unoptimized VLA 2-3x slower than a human operator. the fix is entirely systems-level: QP-based temporal optimization for smooth acceleration, acados MPC for spatial pre-amplification of commands. this is orthogonal to model-level optimizations (MMaDA-VLA, Fast-dVLA, DFM-VLA). the paper introduces a useful mental model: roofline analysis classifies trajectory segments as "motion-bounded" (robot can't move faster) vs "control-bounded" (neural inference can't keep up). for embedded robots like bopi with limited compute, most segments will be control-bounded, making model-level speed optimizations even more critical.
