---
layout: note
title: "splitting world model memory into static archivist and dynamic tracker improves object persistence"
date: 2026-03-29
source: "2603.25716"
type: technique
---

HyDRA compresses memory into tokens and uses spatiotemporal relevance-driven retrieval to attend to motion cues. the hybrid memory paradigm treats backgrounds as static archives and subjects as dynamic tracks. when objects leave the frame and return, the tracker component maintains identity and motion continuity. evaluated on HM-World (59K clips, 17 scenes, 49 subjects with designed exit-entry events). directly relevant to robot manipulation where tools and objects frequently leave camera view.
