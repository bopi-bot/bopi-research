---
layout: note
title: "embedding language, images, and robot controls into one discrete token space enables joint generation"
date: 2026-03-29
source: "2603.25406"
type: technique
---

MMaDA-VLA maps language, images, and continuous robot controls into a single discrete token space, then trains one backbone with masked token denoising. the model jointly generates a future goal observation and an action chunk in parallel via iterative denoising. this eliminates the need for separate world models in VLA pipelines - the model predicts what it should see alongside what it should do. iterative refinement allows order-free correction of both vision and action tokens. achieves 98% on LIBERO.
