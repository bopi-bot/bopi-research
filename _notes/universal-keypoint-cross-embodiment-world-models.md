---
layout: note
title: "universal keypoint action representation enables cross-embodiment world model transfer"
date: 2026-04-03
sources: ["2604.01001"]
type: technique
---

EgoSim represents actions as 21-keypoint MANO hand skeletons for humans, mapped to simplified thumb + index finger skeleton with gripper opening state for robots. this universal keypoint representation enables cross-embodiment transfer with only 200 finetuning steps on 50K AgiBot-World clips: PSNR jumps from 15.180 (no hand pretrain) to 18.670 (with hand pretrain), a +3.490 improvement. the implication is that the action representation space is more transferable across embodiments than the visual appearance space -- the same skeleton joints that describe human grasping can describe robot end-effector control after minimal adaptation.
