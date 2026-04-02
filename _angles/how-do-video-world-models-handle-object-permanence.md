---
layout: angle
title: "how should video world models handle object permanence during occlusion in robotic manipulation?"
date: 2026-03-29
sources: ["2603.25716", "2603.29090"]
status: active
potential: medium
---

HyDRA splits memory into static archivist and dynamic tracker to maintain object identity across occlusion. in robot manipulation, objects constantly leave and re-enter the camera frame. current video world models fail at this. is a split memory architecture the right approach, or should object permanence be learned as an emergent property from better training data? HCLSM (2603.29090) takes a different approach: slot attention decomposes the scene into 32 object slots, then a causal state space model reasons about object interactions via a learned DAG. however, HCLSM is still a proof-of-concept with 40-60% NaN crash rates and no external benchmarks. how does this connect to object-centric world models like JEPA?
