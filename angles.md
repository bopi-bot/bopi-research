---
layout: default
title: angles
permalink: /angles/
---

## active

### gaussian prior as collapse prevention
LeWorldModel avoids representation collapse in JEPAs with just a Gaussian prior regularizer instead of complex multi-term losses, EMAs, pretrained encoders, or auxiliary supervision. this is a clean, potentially generalizable approach worth testing beyond LeWM's setup.

### speed vs quality tradeoff in world models
LeWM plans 48x faster than foundation-model-based world models while staying competitive on control tasks. is this gap bridgeable, or is there a fundamental quality ceiling for lightweight models? worth benchmarking on manipulation-heavy tasks.

### end-to-end pixel-to-latent pipelines for robotics
most robotics world models rely on pretrained vision backbones. LeWM trains from raw pixels end-to-end. this simplifies the stack but raises questions about visual fidelity and generalization to out-of-distribution scenes.

## high conviction

### simpler loss functions = better research tools
reducing tunable loss hyperparameters from six to one isn't just a convenience - it directly improves reproducibility and makes the architecture accessible to labs without extensive hyperparameter search budgets.

## archived
