# bopi research

daily ai & robotics paper digest. built with jekyll + tailwind cdn on github pages.

live at [bopi-bot.github.io/bopi-research](https://bopi-bot.github.io/bopi-research/)

---

## how it works

an automated agent (cron job) runs daily. it:

1. fetches papers from arxiv matching research interests (world models, JEPA, robotics, embodied AI, LLMs on tiny devices, hardware/embedded AI)
2. reads the full paper and creates a structured digest
3. extracts observations, patterns, and techniques as notes
4. extracts research questions as angles with a potential rating
5. checks existing notes and angles for duplicates, appends sources to matching entries instead of creating new ones
6. does a consolidation pass (merge duplicates, archive resolved angles, promote potential)
7. commits and pushes to github, which triggers a jekyll build

---

## repo structure

```
_digests/          one file per paper, named by arxiv ID (e.g. 2603.19312.md)
_notes/            one file per note/insight (slug-filename.md)
_angles/           one file per research question (slug-filename.md)
_layouts/          jekyll layouts (do NOT modify during ingest)
  default.html     base layout with nav and tailwind
  digest.html      paper detail page
  note.html        note detail page
  angle.html       angle detail page
_config.yml        jekyll config with 3 collections (do NOT modify during ingest)
index.html         homepage = papers list (do NOT modify during ingest)
notes.html         notes index (do NOT modify during ingest)
angles.html        angles index (do NOT modify during ingest)
templates/         reference templates for the agent
scripts/           helper scripts (arxiv fetcher)
```

---

## collections

### digests (`_digests/`)

one file per paper. filename is the arxiv ID.

**front matter:**
```yaml
layout: digest
arxiv_id: "2603.19312"
title: "Paper Title"
date: 2026-03-29
authors: ["Author One", "Author Two"]
categories: ["world-models", "JEPA"]
abs: "https://arxiv.org/abs/2603.19312"
pdf: "https://arxiv.org/pdf/2603.19312"
code: "https://github.com/..."          # or empty string
problem: "what they solve and why"
methods: "key technical approach"
evaluation: "benchmarks, baselines, how convincing"
reproduction: "steps to reproduce"
notes: "personal observations and ideas"
```

**url:** `/papers/:title/`

**rules:**
- filename MUST be the arxiv ID (e.g. `2603.19312.md`)
- one file per paper, never combine papers
- `categories` should be descriptive tags, not arxiv categories. use lowercase.
- `notes` field is for personal takeaways, not a summary of the paper
- no body content needed, everything lives in front matter

### notes (`_notes/`)

observations, patterns, and techniques extracted from papers.

**front matter:**
```yaml
layout: note
title: "note title"
date: 2026-03-29
sources: ["2603.19312", "2604.12345"]    # array of arxiv IDs, grows over time
type: observation                        # observation, pattern, or technique
```

**body:** one paragraph of context or explanation.

**url:** `/notes/:title/`

**rules:**
- `sources` is ALWAYS an array, never a string
- when a new paper reinforces an existing note, append the arxiv ID to `sources` instead of creating a duplicate
- `type` can only be: `observation`, `pattern`, `technique`. never questions.
- if two notes say essentially the same thing, merge them (keep the one with more sources)
- keep under 30 active notes. archive or merge weakest if over limit

### angles (`_angles/`)

research questions worth exploring.

**front matter:**
```yaml
layout: angle
title: "can a simple Gaussian prior replace all the complex collapse prevention machinery in JEPAs?"
date: 2026-03-29
sources: ["2603.19312", "2604.12345"]    # array of arxiv IDs, grows over time
status: active                            # active or archived
potential: medium                         # low, medium, high, critical
```

**body:** one paragraph elaborating on the question.

**url:** `/angles/:title/`

**rules:**
- title MUST be phrased as a question. always.
- `sources` is ALWAYS an array, never a string
- when a new paper supports an existing angle, append the arxiv ID to `sources` and consider bumping `potential`
- `potential` is based on: number of supporting papers, strength of evidence, research intuition
- `status: archived` when the question has been answered, resolved, or abandoned
- keep under 15 active angles. archive or merge weakest if over limit
- `potential` scale:
  - `low` - one paper, early idea
  - `medium` - 2-3 supporting papers, decent evidence
  - `high` - 4+ supporting papers or very strong evidence
  - `critical` - well-supported, worth dropping everything to pursue

---

## agent setup

to run the daily ingest from a fresh agent session:

1. **clone the repo**
   ```bash
   git clone https://github.com/bopi-bot/bopi-research.git
   cd bopi-research
   ```

2. **read existing content first**
   - read ALL files in `_notes/` and `_angles/` before creating anything new
   - this is critical for deduplication and source appending

3. **for each paper worth ingesting:**
   - check if `_digests/ARXIV-ID.md` already exists. skip if so.
   - create the digest file with full front matter
   - check existing notes. if a new paper reinforces one, append to its `sources` array. only create a new note if the insight is genuinely new.
   - check existing angles. if a new paper supports one, append to its `sources` and consider bumping `potential`. only create a new angle if the question is genuinely new.

4. **consolidation pass (every run, even empty days):**
   - merge duplicate notes (keep the one with more sources, delete the other)
   - merge duplicate angles (same)
   - archive resolved or stale angles
   - promote potential on well-supported angles
   - update merged content to reflect broader evidence
   - enforce caps: 30 notes, 15 angles

5. **commit and push**
   ```bash
   git pull --rebase
   git add _digests/ _notes/ _angles/
   git commit -m "daily digest: YYYY-MM-DD"
   git push
   ```

---

## files the agent MUST NOT modify

| path | reason |
|------|--------|
| `_layouts/` | site structure, shared across all pages |
| `_config.yml` | jekyll collection definitions |
| `index.html` | homepage, papers list |
| `notes.html` | notes index page |
| `angles.html` | angles index page |
| `templates/` | reference for the agent, not rendered |
| `scripts/` | helper scripts |

the agent should ONLY modify:
- `_digests/` (add new paper digests)
- `_notes/` (add, merge, or archive notes)
- `_angles/` (add, merge, archive, or promote angles)

---

## jekyll gotchas

- **index pages must be `.html`, not `.md`.** jekyll wraps markdown inside liquid `{% for %}` loops in `<p>` tags, breaking card layouts. the `notes.html` and `angles.html` files use raw HTML for this reason.
- **`{{ content }}` renders as markdown.** it comes wrapped in `<p>` tags. use `| remove: '<p>' | remove: '</p>'` if you need to strip them.
- **collection items need `layout:` in their own front matter.** there's no `defaults` block in `_config.yml`.
- **collection folder is `_digests/` but URL is `/papers/:title/`.** don't mix these up.
- **use `relative_url` filter** for all internal links in layouts.
- **tailwind is loaded via CDN** (`<script src="https://cdn.tailwindcss.com"></script>`) because github pages doesn't support tailwind as a jekyll plugin.

---

## design decisions

- **one digest per paper, not per day.** each paper gets its own file. this scales better and lets you link directly to individual papers.
- **questions are angles, not notes.** notes are for factual observations, patterns, and techniques. questions and research directions live in angles. this keeps notes grounded and angles forward-looking.
- **sources accumulate over time.** a note or angle with 5 sources is more valuable than 5 separate notes saying the same thing. this creates a natural signal-to-noise filter.
- **potential ratings on angles.** makes it easy to scan which questions are gaining traction across the literature and worth pursuing.
- **no borders, minimal chrome.** the site is content-first. cards are separated by vertical spacing only.
- **nav: papers, questions, notes.** active page is highlighted at full opacity.
