---
layout: note
title: "projection-aware activation steering preserves already-aligned tokens and avoids coherence degradation"
date: 2026-04-10
sources: ["2604.08169"]
type: technique
---

uniform additive activation steering (add a fixed vector at every token) causes coherence degradation and repetition in multi-turn generation because it perturbs already-aligned tokens unnecessarily. StTP/StMP (steering at token/mean projection) train a logistic regression decision boundary on activation norms to classify aligned vs malicious tokens, then only apply the steering vector when the activation falls below the threshold. on disinformation resistance, StMP improves from 51.4 to 65.3 (vs 39 baseline), while preserving MMLU (64.8 vs 65.5 baseline) and reducing multi-turn sentence reuse from 85% (SwFC at turn 9) to 40% (StMP). the optimal steering layer is architecture-dependent: 29-43% depth for Llama, 64-70% for Qwen. this selective intervention approach could generalize beyond alignment to steering persona, style, or task-specific behavior without degrading other capabilities.
