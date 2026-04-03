---
layout: note
title: "WAMs dominate visual perturbation robustness but trail VLAs on camera and robot perturbations"
date: 2026-04-03
sources: ["2603.22078"]
type: observation
---

in a systematic robustness comparison across 7 perturbation dimensions (LIBERO-Plus, RoboTwin 2.0-Plus), World Action Models consistently outperform VLAs on visual perturbations: noise (Cosmos-Policy 92.7% vs $\pi\_0.5$ 89.7%), lighting (LingBot-VA 89.0% vs $\pi\_0.5$ 49.6% on RoboTwin), layout (LingBot-VA 87.9% vs $\pi\_0.5$ 56.8%), background (LingBot-VA 91.3% vs $\pi\_0.5$ 71.7%). but WAMs are weak on camera viewpoint changes (LingBot-VA 28.9% vs $\pi\_0.5$ 45.6% on RoboTwin) and robot initial state perturbations (LingBot-VA 36.2% vs X-VLA 65.2%). the spatiotemporal video priors from web-scale pre-training help with visual diversity but not with embodiment-specific perturbations.
