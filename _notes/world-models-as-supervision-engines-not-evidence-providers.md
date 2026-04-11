---
layout: note
title: "world models are more valuable as supervision engines than as test-time evidence providers"
date: 2026-04-10
sources: ["2604.07957"]
type: observation
---

WorldMAP shows that using a world model to generate imagined future views, then converting those into semantic-spatial memory + BEV cost maps + FMM planning trajectories, and distilling the result into a lightweight student produces 4.4x better trajectory prediction (ADE 42.06 vs 183.93) than the raw VLM. critically, mindjourney (o3 + world model as evidence at test time) actually underperforms direct o3 (152.41 vs 112.14 ADE) -- imagined evidence hurts when not converted into persistent structure. the world model's value is in the supervision pipeline (teacher), not at inference (student runs independently). neither supervision source alone suffices: GT-only gives ADE 78.34, WM-only gives 95.98, but GT+WM gives 42.06.
