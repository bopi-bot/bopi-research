---
layout: note
title: "event camera overlay into VLA vision encoder costs zero parameters but recovers manipulation in darkness"
date: 2026-04-08
sources: ["2604.04834"]
type: observation
---

E-VLA shows that simply adding a binned event count map as an extra channel to the VLA vision encoder (concatenating to RGB) costs zero additional parameters but recovers manipulation ability where frame-based perception fails completely. on a SmolVLA backbone with DAVIS346 event camera on a SO100 arm, image-only VLA achieves 0% success at 20 lux pick-and-place, while the zero-parameter overlay fusion achieves 60%. the full hierarchical event adapter (13.31M params) pushes this to 90%. the practical insight: event cameras capture motion and structural cues that survive extreme lighting conditions, and these cues are naturally compatible with convolutional vision encoders that already process spatial feature maps. no event-to-image reconstruction is needed -- the raw binned events carry sufficient semantic information for the downstream policy.
