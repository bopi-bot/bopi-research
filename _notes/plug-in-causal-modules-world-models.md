---
layout: note
title: "plug-in causal modules can retrofit world models with intervention-aware latent spaces"
date: 2026-04-12
sources: ["2604.07712"]
type: technique
---

CausalVAE (2604.07712) demonstrates a modular approach to adding causal structure to world models: a plug-in CausalVAE branch sits between encoder and transition, learning a DAG-constrained structural transformation of encoder latents without changing the backbone. three-stage training decouples factual prediction (stage 1), causal structure learning (stage 2), and counterfactual transition refinement (stage 3). an alpha-gated fusion mechanism ($\alpha\_t = \alpha\_0 \exp(-k\_\alpha t)$) interpolates between raw and causal-refined latents during rollouts. on Physics 3-body, counterfactual retrieval (CF-H@1) improves from 10.5% to 41% (+302%) over the AE_NLL baseline. the identifiability theorem shows that with alignment supervision (mapping latents to simulator states), the learned DAG is unique up to the anchored coordinate frame. limitations: first-order approximation only, requires simulator states for alignment, gains vary across backbone types (AE/GNN_NLL benefit most, VAE_Contrastive often doesn't).
