---
layout: angle
title: "can latent-space model stitching enable dense geometric supervision for robotics world models?"
date: 2026-03-31
sources: ["2603.26599"]
status: active
potential: medium
---

VGGRPO's latent geometry model uses a single 3D conv layer to stitch a video VAE's latent space into a pretrained geometry model, enabling depth, camera pose, 3D points, and scene flow prediction without VAE decoding. this is proven to be more effective and faster than RGB-based geometry rewards. the question: can this "model stitching" technique be applied to robotics world models? a world model VAE for robot observation could be stitched to a depth/segmentation model, providing dense geometric self-supervision entirely in latent space during world model training. this would be particularly valuable for JEPA-style world models where the latent representation is the core output -- geometric auxiliary losses in latent space could regularize the learned representation toward physically meaningful structure without ever decoding to pixels.
