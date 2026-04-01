---
layout: note
title: "lagged cross-episode context separates static domain info from time-varying dynamics without labels"
date: 2026-04-01
sources: ["2602.04037"]
type: technique
---

DADP's lagged context dynamical prediction uses temporal offset $\Delta t$ to disentangle static domain properties (friction, gravity, mass) from time-varying dynamical properties (higher-order temporal derivatives). by selecting context from a different episode in the same domain (cross-episode prediction with $\Delta t \to \infty$), time-varying information is information-theoretically eliminated while static domain info is preserved. a simple transformer context encoder (dim 256, 4 layers, 8 heads) trained with forward + inverse dynamics prediction reaches 99.3% linear probe accuracy on Walker2d -- comparable to supervised oracle (99.8%). this is an unsupervised representation learning technique that requires no domain labels, only the implicit signal that episodes from the same domain share static properties.
