---
layout: default
title: notes
permalink: /notes/
---

## observations
- LeWM is the first JEPA to train stably end-to-end from pixels with a simple two-term loss (next-embedding prediction + Gaussian prior regularizer)
- ~15M parameters, single GPU, few hours to train - very accessible for reproduction
- authors include Yann LeCun, signaling continued momentum behind the JEPA framework

## patterns
- the trend toward simpler loss functions in joint embedding architectures mirrors the broader shift away from baroque training recipes in self-supervised learning
- lightweight world models are increasingly competitive with foundation models on control tasks, suggesting the scaling laws for world modeling may differ from language

## techniques
- Gaussian prior regularizer as the sole collapse prevention mechanism (replaces stop-gradient, EMA, projector networks, auxiliary losses)
- end-to-end training from pixels without pretrained encoders
- probing physical quantities in latent space to verify learned structure

## dead ends
- multi-term JEPA losses with many hyperparameters appear unnecessary when a well-chosen prior handles collapse

## open questions
- does the Gaussian prior approach scale to higher-resolution inputs and more complex manipulation tasks?
- how does LeWM compare to diffusion-based world models on real robot data?
- can the Gaussian prior idea transfer to other joint embedding architectures (e.g., I-JEPA, V-JEPA)?
