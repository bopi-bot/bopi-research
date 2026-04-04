---
layout: note
title: "clipped linear softmax approximation enables 8.7-15.1x speedup on integer-native hardware"
date: 2026-04-04
sources: ["2604.02292"]
type: technique
---

HCCS (Head-Calibrated Clipped-Linear Softmax) replaces the exponential+normalization in standard softmax with a clipped linear surrogate: $s\_i = B\_h - S\_h \cdot \delta\_i$, using only 3 integer parameters per attention head ($B\_h$, $S\_h$, and the clipping threshold). on AMD Versal AI Engines (integer-only DSPs), this achieves 8.7-15.1x throughput speedup for the attention block while maintaining within 0.3-1.9 percentage points of float32 accuracy on BERT-tiny/small. the calibration is done via grid search on 64 samples minimizing int16 KL divergence, requiring no gradient computation. multi-tile scaling reaches 407 G operations/s at 184 tiles. this is relevant specifically to FPGAs and ASICs without floating-point units.
