- "2604.02051"
---
layout: angle
title: "can generative weight synthesis replace weight storage on kilobyte-constrained MCUs?"
date: 2026-03-29
sources: ["2603.24916", "2603.25284", "2603.25385"]
status: archived
potential: low
---

HYPER-TINYPW achieves 6.31x compression by generating pointwise mixer weights at load time from tiny codes. SliderQuant pushes PTQ to viable 2-bit quantization (9.59 ppl on Llama2-7B) by adapting sliding windows to layer sensitivity. GlowQ reduces edge inference latency by 37.4% through group-shared computation. the convergence is striking: multiple independent approaches (generative synthesis, layer-adaptive PTQ, shared computation) are all chipping away at the memory and compute requirements for running LLMs on constrained hardware. could these be combined -- generate weights, quantize with layer-aware windows, and share computation across modules?


update: Ouroboros (2604.02051) provides counter-evidence. input-conditioned LoRA generation closes only 51.3% of the depth gap in recursive transformers, with the remaining gap coming from initialization distribution mismatch. this suggests dynamic weight generation may have fundamental limits that prevent it from fully replacing stored weights.