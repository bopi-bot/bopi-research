---
layout: note
title: "WAM inference latency is 4.8-83x slower than VLA inference"
date: 2026-04-03
sources: ["2603.22078"]
type: observation
---

on the same hardware, $\pi\_0.5$ generates a 50-step action chunk in 63ms. the fastest WAM (GE-Act, 36-step chunk) takes 300ms (4.8$\times$). LingBot-VA on RoboTwin takes 5230ms per 32-step chunk (83$\times$). the bottleneck is visual state denoising steps. Cosmos-Policy reduces chunk size to 16 to partially compensate (390ms, 6.2$\times$) but sacrifices action horizon. MOTUS with its optical-flow latent actions needs 1175ms for 16 steps (18.6$\times$). this latency gap is a deployment blocker for real-time robot control at 10-50Hz.
