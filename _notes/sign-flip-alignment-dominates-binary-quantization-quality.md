---
layout: note
title: "learned channel-wise sign flips recover as much quantization quality as full affine transformations in binary quantization"
date: 2026-04-13
sources: ["2506.12040"]
type: observation
---

in BTC-LLM's ablation on LLaMA-2-7B at 1.11 bits, a diagonal sign-flip matrix $D\_{\pm}$ alone (zero learned parameters beyond binary signs) drops WikiText2 PPL from 9.23 (no transform) to 7.33, while a full learnable affine transformation $P$ drops it to 6.95. combining both ($D\_{\pm} + P$) reaches 6.06 -- but the marginal gain from adding $P$ on top of $D\_{\pm}$ (7.33 to 6.06) is similar to $P$ alone (6.95 to 6.06).

this means simple channel-wise sign alignment captures the majority of what expensive transformations provide. the sign-flip matrix is a cheaper, more interpretable alternative to hadamard rotation for binary quantization -- it's learned per-model, targets the specific sign misalignment problem, and costs almost nothing to apply at inference (absorbed into weights). this reinforces the finding that rotation quality matters more than rotation complexity for quantization.
