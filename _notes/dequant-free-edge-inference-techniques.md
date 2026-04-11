---
layout: note
title: "dequant-free edge inference: LoRA as runtime inputs, LUT lookup, and compute-from-quantized"
date: 2026-04-10
sources: ["2603.29535", "2604.02051", "2604.02215", "2604.02638", "2604.08118"]
type: technique
---

QUAD from Samsung Research treats LoRA weights as runtime inputs to a single frozen compiled graph rather than baking them into separate binaries. on mobile NPUs (Qualcomm, Exynos, MediaTek), swapping between 10+ LoRA-adapted vision models costs 1.5s per switch due to graph recompilation. QUAD's approach eliminates this entirely: the base model graph is compiled once, and LoRA weights are injected at runtime. a quantization sensitivity score (QSS) determines the anchor LoRA whose quantization profile is shared across all adapters, with knowledge distillation fine-tuning the rest. W8A16 is optimal (W8A8 causes catastrophic FID collapse to ~600). tested on Galaxy S25 and Tab S11 with real on-device latency numbers (~1.0-1.9s per task). the key insight for embedded deployment: compile-time specialization vs runtime flexibility is a real engineering bottleneck on NPUs, not just a theoretical concern.

AXELRAM computes attention scores directly from quantized KV cache indices without ever dequantizing. the key insight: orthogonal-transform-based quantization concentrates each coordinate's distribution to $\mathcal{N}(0, 1/d)$, making the optimal quantizer dependent only on dimension $d$ and bit-width $b$, not on input data. this means a fixed codebook (30 bytes for $b=3$, $d=128$) can be used at design time, and attention scores become table-lookup operations at inference time. the asymmetric path design is critical: transform-on-write (orthogonal rotation when writing to KV cache) + table-lookup-on-read (no inverse transform). this reduces per-query multiplications from 524,288 to 5,120 (a 102.4x reduction) and KV cache memory from 512 MB to 100 MB (5.1x compression) for an 8B model at $T=4096$. the pattern generalizes beyond attention: any operation that currently requires dequant can potentially be replaced with precomputed table lookups if the quantized representation has a known distributional form.
