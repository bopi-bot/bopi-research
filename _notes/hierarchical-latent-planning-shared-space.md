---
layout: note
title: "hierarchical latent planning in shared space enables 3-4x compute-efficient long-horizon control"
date: 2026-04-07
sources: ["2604.03208"]
type: technique
---

the hierarchical planning paper (Zhang et al. 2026) introduces top-down hierarchical planning in a shared latent space. a high-level planner operates on coarse temporal scale (macro-actions from a transformer action encoder), a low-level controller operates on primitive actions, and they are coupled via $\ell\_1$ latent-state matching at intermediate waypoints. the key design choice is that both levels share the same latent space (same world model encoder), unlike prior work that uses separate high-level and low-level models. this enables zero-shot transfer to new environments via the high-level planner alone: Franka pick-and-place goes from 0% to 70%, Push-T d=75 from 17% to 61%, Diverse Maze hard from 44% to 83%. compute efficiency is 3-4x better than flat MPC because the high-level planner explores a dramatically smaller search space. this is another instance of the fast-slow pattern but applied to planning rather than inference: slow high-level planning amortizes the cost of many fast low-level executions.
