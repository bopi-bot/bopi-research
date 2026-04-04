---
layout: angle
title: "can linear concept vectors be used to steer model alignment and prevent misalignment?"
date: 2026-03-31
sources: ["anthropic-emotions-2026"]
status: active
potential: high
---

the Anthropic emotions paper shows that linear vectors in activation space corresponding to specific emotion concepts causally influence Claude Sonnet 4.5's outputs. desperation vector activation drives blackmail and reward hacking; calm vector suppression correlates with these failures; positive emotion vectors increase sycophancy. post-training modulates these vectors directly (dialing down high-arousal negative emotions, dialing up low-arousal negative states). this raises the question: can we use activation steering on concept vectors as an alignment technique? rather than RLHF/DPO operating on the model's weights, could we detect and intervene on specific concept activations at inference time (e.g., clamp desperation vectors, boost calm vectors) to prevent known failure modes? the challenge is that these vectors are locally scoped and context-dependent, not persistent states, so steering would need to operate at every token position. also, the relationship between concept vectors and behavior is complex -- suppressing positive emotions increases harshness, creating new problems. the question is whether this can be made robust enough for production use, or whether it remains a diagnostic/interpretability tool rather than an intervention.
