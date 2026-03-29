---
layout: note
title: "generating pointwise mixer weights at load time enables 6x compression on microcontrollers"
date: 2026-03-29
source: "2603.24916"
type: technique
---

HYPER-TINYPW replaces stored PW mixer weights with generated ones. a shared micro-MLP synthesizes kernels from tiny per-layer codes at load time. steady-state latency matches INT8 baselines since generation is one-off. at 225 kB matches 1.4 MB CNN (6.31x smaller, 84% fewer bytes). retains 95% of large-model accuracy. works across ECG, speech commands, and other embedded sensing tasks. the shared latent basis across layers explicitly removes cross-layer redundancy.
