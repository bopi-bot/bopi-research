---
layout: angle
title: "can 99%-sparsified steering vectors enable practical real-time concept editing on edge devices?"
date: 2026-04-13
sources: ["2604.08524"]
status: active
potential: medium
---

2604.08524 shows that steering vectors can be sparsified to 1-10% of their dimensions while retaining most of their steering effect. at 1% sparsity on gemma 2 2B, refusal steering still works. this raises the question: if steering vectors are this compressible, can we build lightweight concept-editing systems that run on edge devices (phones, robots) with minimal memory and compute overhead?

a 1% sparse steering vector for a 2048-dim model is only ~20 nonzero values -- easily storable and appliable in a few microseconds. the OV circuit finding means the computational cost of applying the steering is just scaling a subset of output projections, not modifying attention patterns. combined with tiny model inference (as shown by the 1.3M param DOOM agent), this could enable on-device alignment steering without any cloud dependency.

open questions: does the sparsification property hold for non-refusal steering (emotion, persona, task vectors)? does it transfer across model sizes? what's the minimum sparsity that preserves safety-critical steering?
