---
layout: note
title: "synthetic data from 3DGS and simulation bridges the data gap for aerial and deformable robot manipulation"
date: 2026-03-30
sources: ["2603.25038", "2603.25725"]
type: technique
---

AirVLA uses Gaussian Splatting reconstructions with a drone dynamics model to synthesize navigation trajectories, achieving 100% gate success (vs 50% without synthetic data) from only 50 generated examples. SoftMimicGen uses non-rigid registration to generate thousands of deformable manipulation demonstrations from 1-10 source demos, enabling zero-shot sim-to-real transfer. both approaches share the same principle: a small set of real demonstrations seeds a synthetic data pipeline that produces orders of magnitude more diverse training data. the key enabler in both cases is handling the "non-rigid" aspects -- AirVLA segments and composites the gripper onto clean scene renders, while SoftMimicGen uses non-rigid registration to adapt trajectories to different deformable object states.
