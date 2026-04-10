---
layout: angle
title: "can inverse dynamics models serve as cheap verifiers to make search-based planning with world models practical?"
date: 2026-04-04
sources: ["2604.01985", "2604.02965", "2604.04502"]
status: active
potential: high
---

WAV demonstrates that verifying candidate actions via sparse inverse dynamics is easier than predicting forward outcomes across the full action distribution. if this asymmetry holds broadly, it could unlock scalable search-based planning for robotics: the world model proposes outcomes, the inverse model filters candidates, and only verified trajectories are explored. the key open question is whether the sparse inverse dynamics model itself generalizes to long-horizon, multi-step plans and novel objects. current results show 2x sample efficiency improvement, but real-world manipulation introduces contact dynamics and visual occlusion that make inverse dynamics harder.
