---
layout: note
title: "video generators contain transferable value function priors for robot RL"
date: 2026-04-12
sources: ["2604.08168"]
type: observation
---

ViVa (2604.08168) repurposes Wan2.2 (a 14B video diffusion model pretrained on internet video) as a value function for robot RL without any robot-specific finetuning of the video model. the approach: denoise a noise-initialised video conditioning on current observation and candidate action at 1 DDIM step, measure noise residual norm as value. this works because video generators trained on diverse internet video learn general physics priors about object permanence, tool use, and physical plausibility that transfer to robotic manipulation. on box assembly, ViVa achieves 73% success vs 58% for static VLM baselines, using 8x8 DPM-Solver to collect 2500 trajectories. the value signal is extracted from the model's latent dynamics understanding, not from generated frames -- only 1 denoising step needed at inference. this is a qualitatively different use of generative models than explicit future prediction (WAM-style): the generator serves as a physics plausibility scorer rather than a scene forecaster.
