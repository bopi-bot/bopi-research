---
layout: note
title: "anchored diffusion with truncated schedule reduces VLA inference cost by 4-8x via residual drift correction"
date: 2026-04-05
sources: ["2604.01567"]
type: technique
---

AnchorVLA shows diffusion policy heads for VLA models don't need full iterative denoising. by anchoring to $K$-means cluster centers (anchor trajectories) and using only $S\_{\text{tr}} = 10$ steps instead of 50-100, they cut compute by 4-8x while matching or exceeding full-step diffusion on mobile manipulation (64.0% avg success, +8.4% over AC-DiT on ManiSkill-HAB). the key insight: when the noisy sample starts near the action manifold, fewer steps recover a valid action.

a residual correction module (57K params) decouples drift correction from anchor selection. it predicts per-step adjustments $\Delta a\_t$ conditioned on $a\_{t-1}$, $o\_t$, and $a\_{\text{anchor}}$, running at full control frequency (50Hz) while the diffusion head fires every $H$ steps. this mirrors the fast-slow pattern in R3DP and FSRM: slow deliberation (anchor generation) paired with fast reactive correction (residual adjustments). total system: 726.25M params, 128.3 TFLOP/episode at $H=5$ vs 641.4 for full-step diffusion.
