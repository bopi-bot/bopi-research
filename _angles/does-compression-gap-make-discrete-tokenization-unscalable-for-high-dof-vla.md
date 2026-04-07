---
layout: angle
title: "does the compression gap make discrete tokenization fundamentally unscalable for high-DOF VLA?"
date: 2026-04-07
sources: ["2604.03191"]
status: active
potential: medium
---

the Compression Gap paper shows that discrete action tokenization creates a hard information bottleneck that prevents VLA scaling. as robot manipulation tasks require higher DOF and finer granularity (e.g., dexterous manipulation with 20+ DOF), the codebook capacity needed grows exponentially while the codebook size is bounded by the tokenizer design. continuous action representations (diffusion, flow matching) don't have this bottleneck. but discrete tokens offer advantages: simpler training (cross-entropy loss), easier autoregressive generation, and compatibility with language model architectures. the question: is there a way to get the best of both worlds? variable-rate tokenization? hierarchical discrete codes? or should the field fully commit to continuous action representations for VLA scaling?
