---
layout: note
title: "verifying candidate actions via inverse dynamics is fundamentally easier than predicting all forward outcomes"
date: 2026-04-04
sources: ["2604.01985"]
type: observation
---

the World Action Verifier (WAV) exploits a key asymmetry: for a world model to be useful in search-based planning, it needs to be reliable over a much broader distribution of suboptimal actions than any policy would ever take. but predicting accurate outcomes for arbitrary actions (including bad ones) is hard. the inverse problem -- given a state transition, recovering the action that caused it -- is sparser and easier to learn. WAV uses this by running a reverse cycle: generate candidate subgoals, use a sparse inverse dynamics model to propose actions, then verify through the forward world model. this achieves 2x sample efficiency and 18% downstream policy improvement. the implication is that inverse dynamics models may be underexploited as cheap verifiers in world-model-based planning.
