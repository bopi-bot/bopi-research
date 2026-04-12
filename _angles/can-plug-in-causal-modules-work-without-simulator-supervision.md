---
layout: angle
title: "can plug-in causal structure modules work on real-robot world models without simulator supervision?"
date: 2026-04-12
sources: ["2604.07712"]
status: active
potential: medium
---

CausalVAE (2604.07712) shows strong counterfactual improvements on simulated benchmarks (up to +302% CF-H@1 on Physics 3-body), but requires simulator states for alignment supervision ($\mathcal{L}\_{\mathrm{align}} = \|g(\tilde{z}\_t) - s\_t\|\_2^2$) and the identifiability theorem depends on this anchoring. without simulator states, the best you can do is enforce the DAG constraint and reconstruction/KL losses, which lose permutation/scale identification. the question is whether real-robot data provides enough structure (e.g. via self-supervised object tracking, physics-aware embeddings, or video prediction consistency) to substitute for simulator alignment. if yes, this plug-in pattern could be applied to real-robot world models to make them intervention-aware for planning under perturbations.
