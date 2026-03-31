---
layout: digest
arxiv_id: "prismml-bonsai-1bit-8b"
title: "1-bit Bonsai 8B"
date: 2026-03-31
authors: ["PrismML"]
categories: ["llm-quantization", "edge-deployment", "1-bit-models"]
abs: "https://github.com/PrismML-Eng/Bonsai-demo/blob/main/1-bit-bonsai-8b-whitepaper.pdf"
pdf: "https://github.com/PrismML-Eng/Bonsai-demo/raw/main/1-bit-bonsai-8b-whitepaper.pdf"
code: "https://github.com/PrismML-Eng/Bonsai-demo"
---

## problem

LLM inference at deployment is dominated by memory bandwidth, not compute. during autoregressive token generation, every output token requires reading the full set of model weights from memory, making weight precision the primary lever for deployment efficiency. pushing below 4-bit has been attempted (BitNet b1.58, OneBit), but quality degrades in brittle ways -- models stay fluent but lose reliability on multi-step reasoning, tool use, and edge cases. near-1-bit approaches also tend to require custom calibration sets, auxiliary metadata, partial higher-precision escape hatches, or bespoke runtimes that don't integrate with standard inference stacks. the result: 1-bit has remained theoretically appealing but practically out of reach for production deployment.

PrismML's thesis is that the bottleneck is not arithmetic throughput but memory traffic. an 8B model at FP16 needs 16.38 GB in memory. at 1.125 bits/weight, that drops to ~1.15 GB -- a 14.2x reduction that directly translates to faster generation and lower energy per token because fewer bytes must be moved through the memory hierarchy on every decoding step.

## architecture

1-bit Bonsai 8B is built from Qwen3-8B with architecture unchanged (8.19B params, 36 transformer blocks, GQA with 32 query / 8 KV heads, SwiGLU MLP, RoPE, RMSNorm, 65,536 context). the novelty is entirely in the deployment format and inference kernels.

**weight format: Q1\_0\_g128.** each weight is stored as a single sign bit in $\{0, 1\}$, bitpacked at 1 bit per weight. one shared FP16 scale $s\_g$ is stored per group of 128 weights. at inference time, the effective weight is:

$$w\_i = s\_g \cdot (2b\_i - 1)$$

where $b\_i \in \{0, 1\}$ and $s\_g$ is the group scale. effective storage cost:

$$b\_{\text{eff}} = 1 + \frac{16}{128} = 1.125 \text{ bits/weight}$$

yielding 14.2x compression vs FP16 before container overhead. the format is applied uniformly across embeddings, attention projections, MLP projections, and the LM head. normalization parameters and scale metadata remain in higher precision but are negligible relative to the large weight tensors.

for MLX, the format requires both scale and bias per group ($w = s\_{\text{mlx}} \times b\_i + b\_{\text{mlx}}$), packed as $s\_{\text{mlx}} = 2s\_g$ and $b\_{\text{mlx}} = -s\_g$, giving 1.25 bits/weight (a current MLX limitation).

**inline dequantization in kernels.** sign bits are decoded inside the matmul kernel rather than materializing a full FP16 tensor. this preserves storage and bandwidth advantages in the critical token-by-token decoding path.

**custom backend implementations:**
- llama.cpp CUDA: custom CUDA kernels for matvec and matmul with bitpacked weight unpacking and group scale application
- llama.cpp Metal: custom Metal compute shaders for single-token decoding and batched prompt processing
- MLX macOS: dedicated fork with custom Metal GPU kernels integrated into the MLX execution stack
- mlx-swift iOS: independent implementation of 1-bit support for iPhone/iPad with custom Metal GPU kernels

## training

no training details are provided. the paper states the method is based on "proprietary Caltech intellectual property" that uses "mathematically grounded advances" to preserve model behavior under aggressive compression. the quantization is post-training (the base model is stock Qwen3-8B). the actual compression algorithm is not disclosed.

## evaluation

benchmarked with greedy decoding, thinking mode disabled, across 10 benchmarks in 6 categories. all models served via vLLM 0.15.1 on H100 GPUs with deterministic execution (Flash Attention 2, batch-invariant scheduling).

| benchmark | Bonsai 8B | Qwen3 8B (FP16) | delta |
|---|---|---|---|
| MMLU-Redux | 59.86 | 71.02 | -11.2 |
| GPQA Diamond | 65.7 | 49.3 | +16.4 |
| MuSR | 30.0 | 55.0 | -25.0 |
| IFEval | 50.0 | 81.5 | -31.5 |
| IFBench | 79.8 | 27.2 | +52.6 |
| GSM8K | 19.8 | 93.0 | -73.2 |
| MATH-500 | 88.0 | 84.4 | +3.6 |
| HumanEval+ | 66.0 | 82.3 | -16.3 |
| MBPP+ | 73.8 | 73.5 | +0.3 |
| BFCL v3 | 59.8 | 81.0 | -21.2 |
| avg | 59.27 | 70.84 | -11.6 |

the raw scores show significant regression vs the FP16 base, particularly on GSM8K (-73.2), IFEval (-31.5), and MuSR (-25.0). the paper's main argument is "intelligence density" -- performance per GB of storage. Bonsai 8B achieves 0.792 intelligence density (avg score / GB) vs 0.076 for Qwen3 8B -- a claimed 10.2x advantage.

**throughput (token generation, tg128):**

| platform | Bonsai 8B tok/s | FP16 baseline tok/s | speedup |
|---|---|---|---|
| RTX 4090 (CUDA) | 368 | 59 | 6.2x |
| RTX L40S (CUDA) | 327 | 52 | 6.3x |
| M4 Pro 48GB (Metal) | 85 | 16 | 5.4x |
| M4 Pro 48GB (MLX) | 131 | 16 | 8.4x |
| iPhone 17 Pro Max (Swift) | 44 | 13.8 (4-bit) | 3.2x |
| RTX 3060 Laptop (CUDA) | 81 | 3.5 (partial offload) | 23.0x |

**energy per token:**

| platform | Bonsai mWh/tok | baseline mWh/tok | advantage |
|---|---|---|---|
| M4 Pro (MLX) | 0.074 | 0.415 | 5.6x |
| M4 Pro (Metal) | 0.091 | 0.471 | 5.1x |
| RTX 4090 | 0.276 | 1.134 | 4.1x |
| iPhone 17 Pro Max | ~0.068 | ~0.143 (4-bit) | 2.1x |

instantaneous power draw is actually higher or equal for Bonsai during generation (31.9W vs 23.3W on M4 Pro MLX), because inline dequantization shifts execution toward a more compute-intensive regime. the energy savings come entirely from completing generation much faster.

the Bonsai family also includes 4B and 1.7B variants. Bonsai 4B achieves 1.427 intelligence density (vs 0.162 for Ministral3 3B). Bonsai 1.7B achieves 2.172 (vs 0.477 for Qwen3 0.6B). on iPhone, Bonsai 1.7B hits 130 tok/s.

## reproduction guide

1. clone the demo repo: `git clone https://github.com/PrismML-Eng/Bonsai-demo`
2. for llama.cpp: use their fork at `https://github.com/PrismML-Eng/llama.cpp` with custom CUDA/Metal kernels for Q1\_0\_g128
3. for MLX macOS: use their fork at `https://github.com/PrismML-Eng/mlx`
4. for iOS: use their fork at `https://github.com/PrismML-Eng/mlx-swift`
5. weights are Apache licensed and available on HuggingFace
6. evaluation: the paper uses EvalScope v1.4.2 + vLLM 0.15.1 on H100 with `VLLM\_BATCH\_INVARIANT=1` and `--attention-backend FLASH\_ATTN` for deterministic outputs

the quantization method itself is proprietary and not reproducible. you can run the pre-quantized weights but cannot apply the same compression to other models.

## notes

this is a deployment paper, not a research paper -- the compression method is proprietary Caltech IP and not disclosed. the value proposition is real (14.2x size reduction, 5-8x faster generation, 4-6x lower energy/token), but the benchmark results reveal the cost: significant quality regression on math (GSM8K -73.2), reasoning (MuSR -25.0), and instruction following (IFEval -31.5). some scores are oddly high (IFBench +52.6, GPQA +16.4) which may indicate evaluation artifacts or the model's particular strengths.

the "intelligence density" framing is clever marketing but potentially misleading -- it optimizes for a ratio that heavily favors tiny models. a model that's 14x smaller but loses 11.6 points on average benchmark score is a real tradeoff, not a clear win. the right framing is: "1-bit makes 8B-class models deployable on phones and laptops where they literally couldn't fit before." that's the actual breakthrough.

the MLX 1.25 bits/weight vs GGUF 1.125 bits/weight is a notable practical detail -- MLX's requirement for both scale and bias per group costs ~11% more storage. once MLX supports scale-only formats, they expect parity.

the energy analysis is honest: instantaneous power goes UP, not down, because dequantization is compute-heavy. the savings come purely from faster completion. this is an important nuance that many efficiency papers gloss over.

relevant to the bopi project: running a 1.15 GB model on an iPhone at 44 tok/s is genuinely practical for on-device inference. if the quality regression is acceptable for your use case (simple commands, summarization, classification), this is a viable path for on-robot deployment without cloud dependency.
