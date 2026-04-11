---
layout: note
title: "cross-modal priors (proprioceptive foresight, event cameras) improve VLA robustness at near-zero cost"
date: 2026-04-05
sources: ["2604.04834", "2603.29409"]
type: technique
---

CLaD uses asymmetric cross-attention where proprioceptive state queries attend to semantic visual features to produce grounded latent foresights of future states. the asymmetry matters: proprio $\to$ semantic achieves 94.7% on LIBERO-LONG, while semantic $\to$ proprio gets 93.8% and symmetric gets 86.7%. proprioceptive-only foresight catastrophically degrades to 50.4%. the insight is that the robot's own state (joint positions, gripper) is the right query space for retrieving what matters from visual observations. the foresights are then injected into a diffusion policy via FiLM modulation, achieving 25 Hz inference on 4 GB memory with only 0.66B parameters. this is a concrete, deployable architecture pattern: lightweight latent predictions conditioned on proprioception, not full video generation.

E-VLA shows that simply adding a binned event count map as an extra channel to the VLA vision encoder (concatenating to RGB) costs zero additional parameters but recovers manipulation ability where frame-based perception fails completely. on a SmolVLA backbone with DAVIS346 event camera on a SO100 arm, image-only VLA achieves 0% success at 20 lux pick-and-place, while the zero-parameter overlay fusion achieves 60%. the full hierarchical event adapter (13.31M params) pushes this to 90%. the practical insight: event cameras capture motion and structural cues that survive extreme lighting conditions, and these cues are naturally compatible with convolutional vision encoders that already process spatial feature maps. no event-to-image reconstruction is needed -- the raw binned events carry sufficient semantic information for the downstream policy.
