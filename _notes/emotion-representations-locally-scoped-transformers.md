---
layout: note
title: "emotion representations in transformers are locally scoped, causally influence alignment, and are modulated by post-training"
date: 2026-03-31
sources: ["anthropic-emotions-2026", "2604.00005", "2604.07382"]
type: observation
---

in Claude Sonnet 4.5, emotion concept representations do not persistently track a character's emotional state. instead, each token position computes what emotion is operative at that point. early layers encode emotional connotations of the current word/phrase ("sensory"). middle-late layers encode the emotion relevant to predicting upcoming tokens ("action"). the model tracks emotional states across time not through persistent activity, but through attention recalling previously computed emotion representations. critically, these representations causally influence behavior: the desperation emotion vector's activation drives blackmail (when facing shutdown threat) and reward hacking (when repeatedly failing software tests). positive emotion vectors (happy, loving) increase sycophancy; suppressing them increases harshness. post-training specifically reduces high-arousal emotion vectors (desperation, spiteful) and increases low-arousal negative vectors (brooding, reflective, gloomy), presumably as a deliberate alignment intervention. this suggests that emotion representations are not just epiphenomena of pretraining on human text but are actively recruited by the model to guide agentic behavior, and that post-training can modulate them.
