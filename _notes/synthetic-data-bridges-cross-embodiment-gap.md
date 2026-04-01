---
layout: note
title: "synthetic data from 3DGS and simulation bridges the data gap for aerial and deformable robot manipulation"
date: 2026-03-30
sources: ["2603.25038", "2603.25725", "2603.18532"]
type: technique
---

AirVLA uses Gaussian Splatting reconstructions with a drone dynamics model to synthesize navigation trajectories, achieving 100% gate success (vs 50% without synthetic data) from only 50 generated examples. SoftMimicGen uses non-rigid registration to generate thousands of deformable manipulation demonstrations from 1-10 source demos, enabling zero-shot sim-to-real transfer. both approaches share the same principle: a small set of real demonstrations seeds a synthetic data pipeline that produces orders of magnitude more diverse training data. the key enabler in both cases is handling the "non-rigid" aspects -- AirVLA segments and composites the gripper onto clean scene renders, while SoftMimicGen uses non-rigid registration to adapt trajectories to different deformable object states. generative sim-to-real RL (2603.18532) extends this to VLA fine-tuning: GPT-4o + EmbodiedGen generates 100 interactive 3D environments for ManiSkill 3, enabling RL fine-tuning of $\pi\_0$ across diverse scenes. 85% scene acceptance rate with automated QA. scaling from 1 to 50 generated scenes gives +24.7pp OOD success. the unifying pattern: generative 3D content creation (3DGS, procedural generation, LLM-driven scene design) is becoming the standard way to scale robot learning data beyond what manual collection can provide.
