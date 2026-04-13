---
layout: angle
title: "can compute-from-quantized representations replace all dequantization in edge LLM inference?"
date: 2026-04-07
sources: ["2604.02638", "2506.12040"]
status: active
potential: high
---

AXELRAM shows that attention scores can be computed directly from quantized KV cache indices via table lookup, eliminating the dequantize-then-matmul bottleneck. HCCS shows softmax can be replaced with a 3-parameter integer linear approximation. together, these suggest a broader possibility: if every operation in the transformer forward pass can be reformulated to accept quantized inputs directly (via fixed codebooks, lookup tables, or integer-only approximations), then the entire inference path could run without any floating-point dequantization. this would be transformative for edge FPGAs and ASICs that lack FPUs. the open question: can matrix multiplication itself be replaced or approximated in this framework, or is dequant-unavoidable for the linear projections? ternary/binary weight nets provide one answer but at significant quality cost.
