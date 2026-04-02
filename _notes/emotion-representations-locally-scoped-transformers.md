---
layout: note
title: "emotion representations in transformers are locally scoped, not persistent states"
date: 2026-03-31
sources: ["anthropic-emotions-2026"]
type: observation
---

in Claude Sonnet 4.5, emotion concept representations do not persistently track a character's emotional state. instead, each token position computes what emotion is operative at that point. early layers encode emotional connotations of the current word/phrase ("sensory"). middle-late layers encode the emotion relevant to predicting upcoming tokens ("action"). these are often correlated but not always -- when someone talks about danger while otherwise happy, fear activates at the danger tokens. the model tracks emotional states across time not through persistent activity, but through attention recalling previously computed emotion representations. this is fundamentally different from human emotions (persistent neurochemical states) but makes sense for a transformer's architecture where each forward pass independently computes representations for the current position.
