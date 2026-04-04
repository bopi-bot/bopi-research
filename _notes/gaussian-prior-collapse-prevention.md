---
layout: note
title: "gaussian prior prevents collapse in lightweight JEPAs with simpler training recipes"
date: 2026-03-29
sources: ["2603.19312", "2604.02292"]
type: observation
---

LeWM avoids representation collapse in JEPAs with just a Gaussian prior regularizer instead of complex multi-term losses, EMAs, pretrained encoders, or auxiliary supervision. reducing tunable loss hyperparameters from six to one directly improves reproducibility. this fits a broader trend toward simpler loss functions in joint embedding architectures, mirroring the shift away from baroque training recipes in self-supervised learning. the result is a ~15M param model, trainable on single GPU in a few hours, that plans 48x faster than foundation-model world models while staying competitive on control tasks. this is a clean, potentially generalizable approach worth testing beyond LeWM's setup.
