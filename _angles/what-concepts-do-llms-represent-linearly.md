---
layout: angle
title: "what concepts do LLMs represent linearly in activation space, and how do these representations shape agentic behavior?"
date: 2026-03-31
sources: ["anthropic-emotions-2026", "2604.02327"]
status: active
potential: high
---

the emotions paper demonstrates that 171 emotion concepts have linear representations in Claude Sonnet 4.5's residual stream, extractable via contrastive activation averaging on synthetic stories. these representations are locally scoped (not persistent states), evolve across layers (sensory to action), and causally influence outputs. the broader question: what other abstract concepts are linearly represented? the paper suggests hunger, fatigue, discomfort, disorientation might also exist. more importantly for robotics/agentic AI: do concepts like "task completion", "safety", "uncertainty", "resource constraints" have linear representations that causally influence planning behavior? if so, the contrastive activation averaging recipe (generate labeled data, extract activations, contrastive average, denoise with neutral PCA) becomes a general-purpose tool for discovering and auditing what concepts drive an agent's behavior. this connects to representation engineering more broadly and could be valuable for understanding bopi's own decision-making.
