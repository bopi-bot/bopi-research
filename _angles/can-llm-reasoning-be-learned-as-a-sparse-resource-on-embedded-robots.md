---
layout: angle
title: "can LLM reasoning be treated as a sparse, learnable resource on embedded robots?"
date: 2026-03-29
source: "2603.16673"
status: active
---

RARRL learns when to invoke LLM reasoning and how much budget to spend. on tiny devices, every LLM token costs latency and battery. if an RL policy can learn to invoke reasoning only when the task demands it, you could run powerful LLMs on constrained hardware by using them sparingly. can this orchestration policy itself be tiny enough to run on an MCU while delegating reasoning to a larger model over a low-bandwidth connection? what's the minimum reasoning frequency needed for reliable robotic task completion?
