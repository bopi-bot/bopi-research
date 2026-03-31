---
layout: note
title: "CPU-optimized vision backbones need grouped convolutions and small kernels, not depthwise convolutions"
date: 2026-03-31
sources: ["2603.26425"]
type: technique
---

CPUBone shows that on CPUs with limited parallelism (4-8 cores), depthwise convolutions are deceptively inefficient: they have low MACs but terrible MACpS (MACs-per-second) due to poor hardware utilization. the effective metric on CPUs is MACs / MACpS = latency. two design rules emerge: (1) grouped convolutions with groups=2 halve the MACs of the expansion conv while maintaining ~95% of MACpS, and (2) 2x2 kernels reduce convolution MACs by ~56% while giving ~42% higher MACpS for depthwise convolutions on ARM. the result: CPUBone-B0 (5.4M params) achieves 78.7% top-1 at 42.3ms on raspberry pi 5 CPU, 3.7x faster than MobileNetV3-Large at higher accuracy. for robotics on MCUs where even 4 cores is a lot, these grouped conv + small kernel design rules are directly applicable to custom perception architectures. the key caveat: all benchmarks are on ARM application processors, not actual MCUs (STM32, ESP32) -- verification needed at the lower end.
