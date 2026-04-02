---
layout: note
title: hadamard rotation accounts for 98% of quantization quality improvement at 5-bit
date: 2026-04-02
sources: ["2603.29078", "2603.27914"]
type: observation
---

PolarQuant shows that normalizing weight blocks to the unit hypersphere and applying Walsh-Hadamard rotation (block size 128) accounts for 98% of the quality improvement at Q5 (PPL 6.90 to 6.40 on Qwen3.5-9B). the Lloyd-Max optimal centroids for $\mathcal{N}(0,1)$ contribute only 2%. ITQ3\_S independently confirms this at 3-bit: pre-rotating weights with a 256-point FWHT before ternary quantization reduces the perplexity gap by 57% vs plain ternary (IQ3\_S). the Hadamard matrix is self-inverse ($H^{-1} = H$), so dequantization is trivial and requires no additional storage. two independent papers, different bit widths, same conclusion: rotation is the dominant factor, not the quantization centroids. this means practical systems should prioritize rotation preprocessing over complex codebook design.
