---
layout: note
title: "energy-per-token savings from 1-bit come from faster completion, not lower power"
date: 2026-03-31
sources: ["prismml-bonsai-1bit-8b"]
type: observation
---

1-bit Bonsai 8B draws equal or higher instantaneous power during generation than FP16 (31.9W vs 23.3W on M4 Pro with MLX). the energy savings (5.6x lower mWh/token) come entirely from completing token generation much faster, not from drawing less power. inline dequantization inside matmul kernels shifts execution toward a more compute-intensive regime. this is an important nuance that many efficiency papers obscure -- lower energy per token does not imply lower power draw. the implication: for thermal-constrained devices where peak power matters (phones, embedded), 1-bit may not help with thermal throttling even though it helps with total energy consumption.
