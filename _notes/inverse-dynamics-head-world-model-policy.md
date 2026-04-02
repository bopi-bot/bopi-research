---
layout: note
title: inverse dynamics head improves world model representations for downstream policy without changing the model
date: 2026-04-02
sources: ["2603.28955"]
type: technique
---

WAM augments DreamerV2 with a 3-layer MLP inverse dynamics head that predicts actions from consecutive encoder embeddings ($[e\_t; e\_{t+1}]$). this cascading effect propagates action-aware structure from the encoder through the posterior, prior, and into imagined rollouts, even though the world model itself is unchanged. the result: BC success improves from 45.8% to 61.7% and PPO fine-tuning from 79.8% to 92.8% across 8 CALVIN tasks, with 8.7x fewer world model training steps (230K vs 2M). the inverse dynamics head is discarded at inference -- it only affects training. this is a minimal intervention (3 MLP layers, no architecture changes) that improves both representation quality and data efficiency. connects to the broader pattern of auxiliary training objectives shaping world model representations without changing the core model.
