---
layout: angle
title: "can posterior inference replace gradient-based RL for stable VLA policy fine-tuning?"
date: 2026-04-05
sources: ["2604.01860"]
status: active
potential: medium
---

POCO formulates policy improvement as posterior inference (EM) rather than direct gradient optimization. the E-step creates a reward-weighted posterior over action trajectories, and the M-step distills this posterior into the policy with a clipped surrogate objective. this avoids catastrophic forgetting that plagues direct RL fine-tuning of pretrained generative policies. the question is whether this posterior-inference framing generalizes beyond the specific flow-matching VLA architectures tested. can it work for diffusion-based VLAs like AnchorVLA? for autoregressive VLAs? the chunk-level formulation (operating on action sequences, not single steps) seems well-suited to any policy that generates structured action outputs. the offline-to-online paradigm (anchor exploration to pretrained prior) is particularly interesting for robotics where pretrained VLAs are becoming the default starting point.
