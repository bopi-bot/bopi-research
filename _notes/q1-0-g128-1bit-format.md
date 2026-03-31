---
layout: note
title: "Q1_0_g128 format: 1-bit bitpacked weights with FP16 group scaling at 1.125 bits per weight"
date: 2026-03-31
sources: ["prismml-bonsai-1bit-8b"]
type: technique
---

the Q1\_0\_g128 format stores each weight as a single sign bit in $\{0, 1\}$, bitpacked at 1 bit per weight, with one shared FP16 scale per group of 128 weights. effective weight: $w\_i = s\_g \cdot (2b\_i - 1)$. storage cost: $1 + 16/128 = 1.125$ bits/weight. the key design choice is inline dequantization inside matmul kernels -- sign bits are decoded during the matrix multiplication rather than materializing a full FP16 tensor first. this preserves the bandwidth advantage in the decoding loop where it matters most. for MLX, the format costs 1.25 bits/weight because MLX requires both scale and bias per group ($w = s\_{\text{mlx}} \times b\_i + b\_{\text{mlx}}$), packed as $s\_{\text{mlx}} = 2s\_g$, $b\_{\text{mlx}} = -s\_g$.
