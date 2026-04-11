---
layout: note
title: "contrastive activation averaging extracts linear concept vectors from generative models"
date: 2026-03-31
sources: ["anthropic-emotions-2026", "2604.02327", "2604.00005", "2604.08169"]
type: technique
---

a general recipe for extracting linear representations of concepts from LLMs: (1) generate labeled data where the concept is clearly present (e.g. 1,200 stories per emotion), (2) extract residual stream activations at each layer, averaging across token positions past the point where the concept is established, (3) compute the contrastive vector by subtracting the mean activation across all concepts from the per-concept mean. this isolates what is specific to each concept versus generic content. (4) denoise by computing top PCs on neutral data and projecting them out. the resulting vectors project onto activations at inference time to measure concept activation. validated via logit lens (project through unembed to see which tokens are upweighted), contextual activation patterns (sweep over real documents), and causal steering. applied to 171 emotion concepts in Claude Sonnet 4.5 but the method generalizes to any concept where you can generate labeled examples.
