---
layout: angle
title: "can 3D geometry grounding close the gap between appearance modeling and reliable robot action planning?"
date: 2026-04-04
sources: ["2604.01765"]
status: active
potential: medium
---

DriveDreamer-Policy shows that adding depth prediction as an intermediate representation between video generation and action planning consistently improves driving planning metrics. the question is whether this pattern generalizes beyond autonomous driving to manipulation, where spatial reasoning about objects, tools, and grasp points is even more critical. depth provides explicit 3D structure that RGB alone encodes only implicitly. if geometry-grounded world models consistently outperform appearance-only ones across manipulation benchmarks, it would argue for 3D representations (depth, point clouds, 3D gaussians) as a standard component in world-action architectures.
