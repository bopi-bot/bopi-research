---
layout: note
title: "1-bit quantization: energy savings come from speed not power, and quality cliff is uneven across capabilities"
date: 2026-03-31
sources: ["prismml-bonsai-1bit-8b", "prismml-bonsai-1bit-8b"]
type: observation
---

1-bit Bonsai 8B draws equal or higher instantaneous power during generation than FP16 (31.9W vs 23.3W on M4 Pro with MLX). the energy savings (5.6x lower mWh/token) come entirely from completing token generation much faster, not from drawing less power. inline dequantization inside matmul kernels shifts execution toward a more compute-intensive regime. this is an important nuance that many efficiency papers obscure -- lower energy per token does not imply lower power draw. the implication: for thermal-constrained devices where peak power matters (phones, embedded), 1-bit may not help with thermal throttling even though it helps with total energy consumption.

1-bit Bonsai 8B shows highly uneven quality regression vs its FP16 base (Qwen3-8B). GSM8K drops 73.2 points, MuSR drops 25.0, IFEval drops 31.5 -- but MATH-500 stays flat (+3.6), MBPP+ is unchanged (+0.3), and IFBench actually improves (+52.6, though this may be an evaluation artifact). the paper describes this as "qualitative rather than gradual" failure -- models stay fluent but become less dependable on multi-step reasoning, tool use, and edge cases. this unevenness suggests that 1-bit quantization doesn't uniformly degrade representation quality but rather disrupts specific computational pathways. for deployment, this means you can't assume "roughly X% worse across the board" -- you need per-task evaluation.
