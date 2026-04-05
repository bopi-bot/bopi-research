---
layout: note
title: "Gaussian action neighborhood prior shapes VLA output distribution for 2.5x faster convergence"
date: 2026-04-05
sources: ["2604.01570"]
type: technique
---

the Feasible Action Neighborhood (FAN) prior addresses a fundamental mismatch: VLA models are trained with language-style one-hot supervision, but physical manipulation admits a neighborhood of near-equivalent actions per state. the FAN regularizer is a Gaussian KL divergence term $\mathcal{L}\_{\text{FAN}} = D\_{\text{KL}}(q \mid \mid \mathcal{N}(\mu\_{\text{ref}}, \sigma^2 I))$ that shapes the predicted action distribution from "spiky" overconfident peaks to smooth, locally unimodal predictions around the demonstrated direction. this is closely related to the gaussian prior collapse prevention technique in JEPAs (LeWM) -- in both cases, a simple Gaussian prior on the latent/action space regularizes the model away from degenerate solutions. the FAN approach yields +11.7% in-distribution and +6.2% OOD improvement on ManiSkill, plus 2.5x faster RFT convergence.
