- "2604.01765"
---
layout: angle
title: "can discrete flow matching replace both autoregressive and diffusion decoding as the universal VLA action decoder?"
date: 2026-03-31
sources: ["2603.26320", "2603.25406", "2603.25661", "2604.03191"]
status: active
potential: medium
---

DFM-VLA shows that discrete flow matching enables full-sequence iterative action refinement that neither autoregressive decoding (irreversible left-to-right commitment) nor discrete diffusion (mask-restricted updates) can achieve. the embedding-guided velocity formulation preserves semantic neighborhood structure during refinement. at the same time, Fast-dVLA proves discrete diffusion can run at 30 Hz real-time. and MMaDA-VLA extends discrete generation to joint vision-action prediction. the question: can DFM subsume both AR and DD as the single best decoding paradigm for discrete-token VLAs? the evidence so far is strong (95.7% LIBERO average, 70.8% real-world, best low-data performance) but limited to one backbone (UniVLA/Emu3). needs testing on OpenVLA, pi-0, and smaller models suitable for edge deployment.
