---
layout: note
title: "compute-from-quantized-without-dequant: hardware co-design eliminates the KV cache dequant bottleneck"
date: 2026-04-07
sources: ["2604.02638"]
type: technique
---

AXELRAM computes attention scores directly from quantized KV cache indices without ever dequantizing. the key insight: orthogonal-transform-based quantization concentrates each coordinate's distribution to $\mathcal{N}(0, 1/d)$, making the optimal quantizer dependent only on dimension $d$ and bit-width $b$, not on input data. this means a fixed codebook (30 bytes for $b=3$, $d=128$) can be used at design time, and attention scores become table-lookup operations at inference time. the asymmetric path design is critical: transform-on-write (orthogonal rotation when writing to KV cache) + table-lookup-on-read (no inverse transform). this reduces per-query multiplications from 524,288 to 5,120 (a 102.4x reduction) and KV cache memory from 512 MB to 100 MB (5.1x compression) for an 8B model at $T=4096$. the pattern generalizes beyond attention: any operation that currently requires dequant can potentially be replaced with precomputed table lookups if the quantized representation has a known distributional form.
