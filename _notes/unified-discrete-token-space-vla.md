---
layout: note
title: "embedding language, images, and robot controls into one discrete token space enables joint generation"
date: 2026-03-29
sources: ["2603.25406", "2603.25661", "2603.26320", "2604.03191"]
type: technique
---

MMaDA-VLA maps language, images, and continuous robot controls into a single discrete token space, then trains one backbone with masked token denoising. the model jointly generates a future goal observation and an action chunk in parallel via iterative denoising. this eliminates the need for separate world models in VLA pipelines - the model predicts what it should see alongside what it should do. iterative refinement allows order-free correction of both vision and action tokens. achieves 98% on LIBERO. Fast-dVLA extends this by making discrete-diffusion VLAs run at real-time speed (30 Hz) through block-wise causal attention and diffusion forcing, proving the discrete token approach is not just accurate but also practical for physical robot control. DFM-VLA (2603.26320) pushes this further by replacing discrete diffusion with discrete flow matching, which enables full-sequence token revision at every step -- solving the "irreversible commitment" problem that limits both autoregressive and discrete diffusion decoding. achieves 95.7% on LIBERO average with 70.8% on real bimanual tasks.
