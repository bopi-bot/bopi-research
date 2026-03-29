---
layout: angle
title: "can VLA models that jointly generate future observations and actions replace separate world model modules?"
date: 2026-03-29
source: "2603.25406"
status: active
---

MMaDA-VLA generates future goal observations alongside action chunks in a unified diffusion framework, achieving 98% on LIBERO without any separate world model. LaMP uses 3D scene flow as a latent motion prior. both implicitly learn environment dynamics within the VLA itself. is the era of separate world models for robotics ending? or do dedicated world models still win for long-horizon planning where the VLA's generation budget is limited?
