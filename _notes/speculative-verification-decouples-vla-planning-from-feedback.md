---
layout: note
title: "speculative verification decouples VLA planning from closed-loop feedback at inference time"
date: 2026-04-07
sources: ["2604.02965"]
type: technique
---

SV-VLA separates VLA inference into two stages: (1) open-loop planning where the base VLA generates an action chunk, and (2) closed-loop verification where a lightweight deviation predictor checks whether the planned trajectory matches current observations. this is analogous to speculative execution in CPUs: speculate on the fast path (open-loop VLA), verify before committing (deviation check). when deviation exceeds threshold, replanning is triggered. the verifier is much cheaper than running the full VLA at every timestep, preserving the speed advantage of action chunking while regaining the robustness of closed-loop control. this extends the inference-time guidance pattern (see inference-time-guidance-pattern-robotics.md) from post-hoc gradient correction to a structural architecture change: embed the verification loop into the inference pipeline itself, not as an external intervention.
