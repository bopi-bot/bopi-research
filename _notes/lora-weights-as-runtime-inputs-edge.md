---
layout: note
title: treating LoRA weights as runtime inputs to a single compiled graph eliminates edge NPU graph swap overhead
date: 2026-04-02
sources: ["2603.29535"]
- "2604.02051"
type: technique
---

QUAD from Samsung Research treats LoRA weights as runtime inputs to a single frozen compiled graph rather than baking them into separate binaries. on mobile NPUs (Qualcomm, Exynos, MediaTek), swapping between 10+ LoRA-adapted vision models costs 1.5s per switch due to graph recompilation. QUAD's approach eliminates this entirely: the base model graph is compiled once, and LoRA weights are injected at runtime. a quantization sensitivity score (QSS) determines the anchor LoRA whose quantization profile is shared across all adapters, with knowledge distillation fine-tuning the rest. W8A16 is optimal (W8A8 causes catastrophic FID collapse to ~600). tested on Galaxy S25 and Tab S11 with real on-device latency numbers (~1.0-1.9s per task). the key insight for embedded deployment: compile-time specialization vs runtime flexibility is a real engineering bottleneck on NPUs, not just a theoretical concern.
