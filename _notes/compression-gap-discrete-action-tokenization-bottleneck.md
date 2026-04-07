---
layout: note
title: "the compression gap: discrete action tokenization creates a hard information bottleneck in VLA scaling"
date: 2026-04-07
sources: ["2604.03191"]
type: observation
---

the Compression Gap principle (Shiba 2026): in any visuomotor pipeline, scaling behavior is governed by the location of the tightest information bottleneck. when actions are represented as discrete tokens (VQ-VAE, FSQ), the action codebook capacity becomes the tightest bottleneck, and upgrading the vision encoder produces diminishing returns. diffusion policy (continuous actions) gains +21.2 to +26.0 percentage points from encoder upgrades (ResNet-18 to SigLIP), while OAT (discrete tokens with FSQ, $\mid\mathcal{V}\mid = 1000$) gains only +3.6 to +10.4 pp. at weak encoder, OAT beats diffusion policy by 17.4 pp; at strong encoder, diffusion policy wins by 12.8 pp. this ~30 pp reversal is caused by the codebook capacity ceiling, not the encoder. causal experiment: increasing codebook size from 256 to 1920 tokens recovers scaling for OAT (+15.2 pp from encoder upgrade vs +3.6 pp with small codebook). the bound is information-theoretic: FSQ with $H\_l = 8$ bits limits to ~80 bits per action chunk, insufficient for high-DOF manipulation at fine granularity.
