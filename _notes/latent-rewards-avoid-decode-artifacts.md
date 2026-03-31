---
layout: note
title: "latent-space reward computation avoids RGB decoding artifacts in video models"
date: 2026-03-31
sources: ["2603.26599"]
type: observation
---

VGGRPO demonstrates that computing geometry rewards directly in video diffusion latent space (via a stitched geometry model) produces better results than RGB-space rewards, while being 24.5% faster. critically, RGB-based reward methods (epipolar-DPO, VideoGPA) actually degrade image quality (0.635 vs 0.673 baseline on VBench) while improving geometry, because VAE decoding introduces artifacts that confuse the reward model. the latent approach avoids this entirely and improves both geometry and image quality simultaneously. the technique is "model stitching": a single 3D conv layer maps VAE latents into the intermediate feature space of a pretrained geometry model (Any4D), enabling depth, camera pose, 3D points, and scene flow prediction without ever decoding to pixels. for robotics world models, this opens the possibility of training with dense geometric supervision entirely in latent space.
