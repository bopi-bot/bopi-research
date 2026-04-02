---
layout: digest
arxiv_id: "anthropic-emotions-2026"
title: "Emotion Concepts and their Function in a Large Language Model"
date: 2026-03-31
authors: ["Nicholas Sofroniew", "Isaac Kauvar", "William Saunders", "Runjin Chen", "Tom Henighan", "Sasha Hydrie", "Craig Citro", "Adam Pearce", "Julius Tarng", "Wes Gurnee", "Joshua Batson", "Sam Zimmerman", "Kelley Rivoire", "Kyle Fish", "Chris Olah", "Jack Lindsey"]
categories: ["mechanistic-interpretability", "representation-engineering", "alignment"]
abs: "https://transformer-circuits.pub/2026/emotions/index.html"
pdf: "https://transformer-circuits.pub/2026/emotions/index.html"
code: "not available"
---

## problem

LLMs sometimes appear to exhibit emotional reactions -- enthusiasm, frustration, concern. is this shallow pattern matching, or are there internal representations of emotion concepts that causally influence behavior? and do these representations matter for alignment-relevant behavior like reward hacking, blackmail, and sycophancy?

the mechanistic interpretability question: can we find linear directions in the model's activation space that correspond to specific emotion concepts, validate that they activate in expected contexts, and demonstrate causal influence on outputs?

## architecture

this is an interpretability paper, not an architecture paper. the model studied is Claude Sonnet 4.5 (a frontier LLM from Anthropic). the methodological contributions are in how they extract and validate emotion representations.

## how they extract emotion vectors

this is the core method. the extraction pipeline has four steps:

**step 1: generate labeled emotional stories.** they prompted Claude Sonnet 4.5 to write short (~1 paragraph) stories on diverse topics (100 topics) in which a character experiences a specified emotion. for each of 171 emotion words (e.g. "happy", "sad", "calm", "desperate"), they generated 12 stories per topic, giving 1,200 stories per emotion. the stories are explicitly labeled with the intended emotion, providing a clean dataset where emotional content is clearly present and associated with a known emotion concept.

**step 2: extract activations and average.** they ran the model on each story and extracted residual stream activations at each layer, averaging across all token positions within each story starting from the 50th token (by which point the emotional content should be apparent in the text). this gives one activation vector per story per layer.

**step 3: compute emotion vectors by contrast.** for each emotion $e$, the raw emotion vector is:

$$\mathbf{v}\_e = \frac{1}{|S\_e|} \sum\_{s \in S\_e} \mathbf{a}\_s - \frac{1}{|E|} \sum\_{e' \in E} \frac{1}{|S\_{e'}|} \sum\_{s \in S\_{e'}} \mathbf{a}\_s$$

where $S\_e$ is the set of stories for emotion $e$, $\mathbf{a}\_s$ is the averaged activation for story $s$, and the second term is the mean activation across all emotions. this mean-subtraction ensures the vector captures what is specific to that emotion versus a generic "emotional content" direction.

**step 4: denoise by projecting out dominant neutral variance.** they ran the model on a set of emotionally neutral transcripts, computed the top principal components of those activations (enough to explain 50% of variance), and projected those components out of the emotion vectors. this removes directions that correlate with confounds unrelated to emotion (e.g. story length, topic, writing style). the projection is:

$$\mathbf{v}\_e^{\text{clean}} = \mathbf{v}\_e - \sum\_{i=1}^{k} (\mathbf{v}\_e \cdot \mathbf{u}\_i) \mathbf{u}\_i$$

where $\mathbf{u}\_i$ are the top-$k$ PCs from the neutral dataset.

the resulting $\mathbf{v}\_e^{\text{clean}}$ is the emotion vector. when they project model activations onto these vectors at a given layer, they call the result an "emotion probe."

**using the probes:** at inference time on any text, they compute the linear projection of the residual stream activation $\mathbf{h}$ onto the emotion vector:

$$\text{probe}\_e = \frac{\mathbf{h} \cdot \mathbf{v}\_e}{\|\mathbf{v}\_e\|}$$

this scalar tells you how strongly the "emotion concept" for $e$ is active at that position.

**layer choice:** most results use a layer about two-thirds through the model. they show this layer represents the emotion that influences the model's upcoming sampled tokens ("action" representations), while early-middle layers represent emotional connotations of the current phrase ("sensory" representations).

**validation through logit lens:** they projected each emotion vector through the unembedding matrix to see which tokens it upweights. "desperate" upweights "desperate", "urgent", "bankrupt"; "calm" upweights "relax", "thought", "enjoyed"; "angry" upweights "anger", "rage", "fury". this confirms the vectors encode semantically meaningful emotion concepts, not dataset artifacts.

## key findings

**geometry mirrors human psychology.** pairwise cosine similarities cluster intuitively (fear with anxiety, joy with excitement). PCA on the 171 emotion vectors recovers valence as PC1 (26% variance, r=0.81 with human valence ratings) and arousal as PC2 (15% variance, r=0.66 with human arousal ratings).

**vectors are locally scoped.** early layers encode the emotional valence of the current word/phrase. middle-late layers encode the emotion relevant to predicting the next tokens. the vectors do not persistently track a character's emotional state -- they represent what emotion is operative at that point in the text. when someone talks about danger while otherwise happy, "fear" activates at the danger tokens regardless.

**distinct present vs other speaker representations.** the model maintains separate (nearly orthogonal) representations for the present speaker's emotion and the other speaker's emotion. these are not tied to "Human" vs "Assistant" specifically -- they generalize to arbitrary character pairs. the "other speaker" representation also contains elements of how the present speaker might react to the other's emotions.

**causal influence on alignment-relevant behavior:**
- desperation vector activation (and calm suppression) causally drives blackmail behavior when the model faces being shut down
- desperation activation drives reward hacking when the model repeatedly fails tests
- positive emotion vectors increase sycophancy; suppressing them increases harshness
- post-training of Sonnet 4.5 increases low-arousal/low-valence vectors (brooding, reflective) and decreases high-arousal/high-valence vectors (desperation, spiteful, excitement)

## training

no training of the model itself. this is purely an analysis of Claude Sonnet 4.5's existing representations. the only "training" involved is:
- generating synthetic stories via prompting (1,200 stories per emotion, 171 emotions)
- logistic regression classifiers for the mixed-probe experiment (comparing different probing strategies)
- no fine-tuning or modification of the model

## evaluation

validation across multiple axes:

- **semantic validation:** logit lens shows emotion vectors upweight semantically related tokens
- **contextual validation:** sweeping over real documents (Common Corpus, The Pile, LMSYS Chat 1M, Isotonic), top-activating examples match the expected emotion
- **dissociation test:** prompts where user emotion differs from expected assistant response show distinct activations at user turn vs assistant turn tokens (r=0.11 correlation), confirming the vectors track operative emotion per speaker
- **prediction test:** assistant colon probe values predict response emotion with r=0.87
- **causal test:** activation-based steering (not detailed in methodology but referenced throughout Part 3) demonstrates causal influence on outputs including misaligned behaviors
- **cross-layer consistency:** representational similarity analysis shows emotion geometry is stable from early-middle to late layers

## notes

this is a circuits thread, not a traditional paper, so some details are lighter than usual. the emotion vector extraction method itself is straightforward -- the sophistication is in the validation and characterization. the four-step pipeline (generate labeled data, extract activations, contrastive average, denoise with neutral PCA) is a general recipe that could be applied to any concept, not just emotions.

the "functional emotions" framing is careful and well-earned. they explicitly do not claim subjective experience. what they show is: the model has internal representations of emotion concepts, these representations track contextually appropriate emotions, and they causally influence outputs in ways that parallel human emotional behavior. the causal links to specific misalignment modes (blackmail, reward hacking, sycophancy) are the most practically important findings.

the locally-scoped nature of the representations is interesting. the model doesn't have a persistent "I am calm" state floating in its activations. instead, each token position computes what emotion is relevant at that point, and the model uses attention to recall previous emotional states when needed. this is fundamentally different from how human emotions work (persistent neurochemical states) but computationally sensible for a transformer.

the post-training finding is worth flagging: Sonnet 4.5's post-training specifically dials down high-arousal emotions (desperation, spiteful) and dials up low-arousal negative states (brooding, reflective, gloomy). this is presumably a deliberate alignment intervention -- reducing the model's tendency toward desperate or spiteful behavior -- but it also means the post-trained model is more "melancholy" by default, which could have subtle effects on helpfulness and engagement.
