---
layout: note
title: "outlier patterns vary across tensors: fixed Hadamard rotation is suboptimal for 6 of 9 matmul types"
date: 2026-04-07
sources: ["2604.02525"]
type: observation
---

AdaHOP provides the first systematic study of outlier patterns across weights, activations, and gradients in LLMs. they identify three patterns: CR (coherent row outliers), CC (coherent column outliers), and None (no structure). inverse Hadamard transform (IHT) is the best rotation for CR pairs but actively harmful for 6 of 9 matmul type pairs. the effectiveness of Hadamard-based suppression depends on alignment between the outlier structure and the rotation axis. a calibration-based detection (30 BF16 steps, threshold $\tau=2.0$) classifies each matmul's outlier pattern and selects the optimal strategy. this nuance refines the earlier observation that "Hadamard rotation accounts for 98% of quantization improvement at 5-bit" (PolarQuant): that finding holds on average across layers, but per-tensor the picture is more varied. the implication for edge deployment: a per-tensor strategy selector adds negligible overhead (calibration is <0.01% of total training compute) but can recover significant accuracy at low precision.
