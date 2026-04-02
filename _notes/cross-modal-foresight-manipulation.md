---
layout: note
title: proprioceptive-semantic cross-modal foresight dramatically improves manipulation planning
date: 2026-04-02
sources: ["2603.29409"]
type: technique
---

CLaD uses asymmetric cross-attention where proprioceptive state queries attend to semantic visual features to produce grounded latent foresights of future states. the asymmetry matters: proprio $\to$ semantic achieves 94.7% on LIBERO-LONG, while semantic $\to$ proprio gets 93.8% and symmetric gets 86.7%. proprioceptive-only foresight catastrophically degrades to 50.4%. the insight is that the robot's own state (joint positions, gripper) is the right query space for retrieving what matters from visual observations. the foresights are then injected into a diffusion policy via FiLM modulation, achieving 25 Hz inference on 4 GB memory with only 0.66B parameters. this is a concrete, deployable architecture pattern: lightweight latent predictions conditioned on proprioception, not full video generation.
