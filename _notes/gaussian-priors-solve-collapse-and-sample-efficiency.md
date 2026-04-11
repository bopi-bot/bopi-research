---
layout: note
title: "gaussian prior prevents collapse in lightweight JEPAs with simpler training recipes"
date: 2026-04-10
sources: ["2603.19312", "2604.02292", "2604.01570", "2604.01570"]
type: observation
---

LeWM avoids representation collapse in JEPAs with just a Gaussian prior regularizer instead of complex multi-term losses, EMAs, pretrained encoders, or auxiliary supervision. reducing tunable loss hyperparameters from six to one directly improves reproducibility. this fits a broader trend toward simpler loss functions in joint embedding architectures, mirroring the shift away from baroque training recipes in self-supervised learning. the result is a ~15M param model, trainable on single GPU in a few hours, that plans 48x faster than foundation-model world models while staying competitive on control tasks. this is a clean, potentially generalizable approach worth testing beyond LeWM's setup.

the Feasible Action Neighborhood (FAN) prior addresses a fundamental mismatch: VLA models are trained with language-style one-hot supervision, but physical manipulation admits a neighborhood of near-equivalent actions per state. the FAN regularizer is a Gaussian KL divergence term $\mathcal{L}\_{\text{FAN}} = D\_{\text{KL}}(q \mid \mid \mathcal{N}(\mu\_{\text{ref}}, \sigma^2 I))$ that shapes the predicted action distribution from "spiky" overconfident peaks to smooth, locally unimodal predictions around the demonstrated direction. this is closely related to the gaussian prior collapse prevention technique in JEPAs (LeWM) -- in both cases, a simple Gaussian prior on the latent/action space regularizes the model away from degenerate solutions. the FAN approach yields +11.7% in-distribution and +6.2% OOD improvement on ManiSkill, plus 2.5x faster RFT convergence.
