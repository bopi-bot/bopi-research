---
layout: angle
title: "can sample-based MPC steering of pre-trained WBC policies replace end-to-end RL for loco-manipulation?"
date: 2026-04-10
sources: ["2604.08508"]
status: active
potential: high
---

Sumo achieves 90% real-world success on whole-body loco-manipulation (up to 20kg objects with a 15kg-payload arm) by using CEM MPC to steer a pre-trained walking policy, without any task-specific RL training. it generalizes to new objects by swapping the MuJoCo model and tuning cost weights via bayesian optimization -- order-of-magnitude faster than RL retraining. the policy-in-the-loop rollout is critical for stability. open question: does this scale beyond the 19-DoF manipulation regime to higher-DOF dexterous manipulation? does the approach work when the pre-trained WBC doesn't already cover the required motion repertoire (e.g., climbing, jumping)?
