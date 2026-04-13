---
layout: note
title: "codebook initialisation determines the quantization basin more than search effort at extreme bit rates"
date: 2026-04-10
sources: ["2604.08118", "2506.12040"]
type: observation
---

the representational ratio $\rho = N / K^M$ (weight groups per layer divided by codebook capacity) determines the quantization regime. at 3 bpp AQLM is overcomplete ($\rho \approx 0.07$) and initialisation errors get absorbed. at 2 bpp the 256x capacity reduction makes weight groups compete for limited codebook entries and initial placement becomes the binding constraint. OA-EM (output-aware EM) at beam=4 (6.1h) beats greedy k-means at beam=16 (16.9h) by 2.8x on perplexity -- better initialisation with less search. PV-tuning compresses the gap between initialisation methods but never closes it entirely, confirming that optimisation stays within the basin defined by the initial codebook centroids. this suggests that for sub-3-bit quantization, research effort should shift from search algorithms to smarter initialisation strategies.
