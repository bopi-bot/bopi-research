---
layout: angle
title: "can generative weight synthesis replace weight storage on kilobyte-constrained MCUs?"
date: 2026-03-29
sources: ["2603.24916", "2603.25284", "2603.25385", "prismml-bonsai-1bit-8b"]
status: active
potential: high
---

HYPER-TINYPW achieves 6.31x compression by generating pointwise mixer weights at load time from tiny codes. SliderQuant pushes PTQ to viable 2-bit quantization (9.59 ppl on Llama2-7B) by adapting sliding windows to layer sensitivity. GlowQ reduces edge inference latency by 37.4% through group-shared computation. 1-bit Bonsai 8B takes this further: Q1\_0\_g128 format at 1.125 bits/weight with inline dequantization in matmul kernels delivers 1.15 GB footprint for an 8B model and 44 tok/s on iPhone. the convergence is striking: multiple independent approaches (generative synthesis, layer-adaptive PTQ, shared computation, 1-bit quantization) are all chipping away at the memory and compute requirements for running LLMs on constrained hardware. could these be combined -- generate weights, quantize with layer-aware windows, and share computation across modules?
