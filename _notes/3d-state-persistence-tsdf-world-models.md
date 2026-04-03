---
layout: note
title: "3D state persistence via TSDF fusion enables multi-clip world model simulation"
date: 2026-04-03
sources: ["2604.01001"]
type: technique
---

EgoSim maintains a persistent 3D scene state across simulation clips using TSDF (Truncated Signed Distance Function) fusion with Sim3 Umeyama alignment. after generating each clip, it reconstructs the 3D state from the generated video using off-the-shelf depth estimation (DepthAnything3), SLAM (DROID-SLAM), and segmentation (SAM3 + Grounding-DINO). the state updating module is entirely training-free -- it's a pipeline of existing perception modules. this enables closed-loop simulation where objects that move in clip $k$ stay moved in clip $k+1$. the TSDF voxel size is 0.003m with 3.0m max depth truncation. statistical outlier removal uses 20 neighbors with std dev ratio 2.0. key limitation: relies on monocular depth estimation which accumulates error across clips, causing PSNR degradation from 25.056 (single clip) to 19.165 (continuous).
