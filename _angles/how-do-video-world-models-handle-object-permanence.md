---
layout: angle
title: "how should video world models handle object permanence during occlusion in robotic manipulation?"
date: 2026-03-29
sources: ["2603.25716", "2603.29090", "2604.01001"]
status: active
potential: high
---

HyDRA splits memory into static archivist and dynamic tracker to maintain object identity across occlusion. in robot manipulation, objects constantly leave and re-enter the camera frame. current video world models fail at this. is a split memory architecture the right approach, or should object permanence be learned as an emergent property from better training data? HCLSM (2603.29090) takes a different approach: slot attention decomposes the scene into 32 object slots, then a causal state space model reasons about object interactions via a learned DAG. however, HCLSM is still a proof-of-concept with 40-60% NaN crash rates and no external benchmarks. EgoSim (2604.01001) offers a third path: rather than learning object permanence end-to-end, it maintains explicit 3D point cloud state via TSDF fusion and updates it after each interaction using off-the-shelf SLAM (DROID-SLAM) and segmentation (SAM3 + Grounding-DINO). the 3D state persists across clips, so objects that move stay moved. the approach is training-free for the state updating module and achieves 5x better Depth ERR than video-only baselines, but it relies on monocular depth estimation which accumulates error. the question becomes: can an explicit 3D state representation (point clouds, TSDF) replace learned object permanence, or is the monocular depth bottleneck fatal for long-horizon manipulation?
