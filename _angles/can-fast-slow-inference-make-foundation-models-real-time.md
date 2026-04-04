- "2604.02292"
---
layout: angle
title: "can fast-slow inference patterns make foundation 3D models practical for real-time robot control?"
date: 2026-04-01
sources: ["2603.14498"]
status: active
potential: medium
---

R3DP demonstrates that running VGGT every $\tau=8$ frames and propagating features via a lightweight TFPNet reduces 3D inference cost by 44.8% (40.3ms vs 73.1ms) with minimal accuracy loss (65.7% vs 69.0%). the pattern is analogous to keyframe-based video compression: expensive computation at sparse keyframes, cheap interpolation in between. could this extend to other expensive foundation models? e.g., running a full VLA every N frames with a lightweight action predictor in between. current limitation: TFPNet is task-specific (trained per task) and doesn't generalize across tasks. a universal feature propagator would make this pattern more practical.
