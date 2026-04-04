---
layout: angle
title: "can fully integer-approximated neural operations run foundation models on edge FPGAs and ASICs without FPUs?"
date: 2026-04-04
sources: ["2604.02292"]
status: active
potential: medium
---

HCCS shows that softmax can be replaced with a 3-parameter integer linear approximation with minimal accuracy loss and massive speedup on AMD Versal AIE. the question is how far this can go: can attention, layer normalization, activation functions, and even linear layers all be approximated with integer-only arithmetic while maintaining usable model quality? if so, it opens the door to running transformer models on ultra-low-power FPGAs and custom ASICs that lack floating-point units entirely. the challenge is that different operations have different sensitivity to approximation, and the compounding effect across many layers is unclear.
