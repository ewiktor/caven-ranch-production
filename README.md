# DRAPER Production Template

The universal repo shape for DRAPER autonomous brand production. Duplicate it, run `00 intake.md` to load a brand in, and the system prompt, logic, and templates apply as-is — they contain no brand facts.

This repo form is a pre-implementation of the DRAPER system in plain folders and markdown, ahead of the actual tooling. The conventions here are the conventions the tooling will adopt.

## Land here first

- **Agents:** `CLAUDE.md` (the system prompt — loads automatically in Claude Code) then `00 brand.md` then `00 index.md`.
- **Humans:** `00 - START HERE.md` — the loop, the bar, the rules that don't bend.
- **Loading a new brand:** `00 intake.md`.

## What's universal vs. what's brand

**Universal (never edited per brand):** `CLAUDE.md`, `00 index.md`, `00 - START HERE.md`, this README, everything in `02 logic/` (steps, blocks, tools), and every `_`-prefixed template and contract file.

**Brand (filled at intake, grows through rounds):** `00 brand.md`, `input/`, and the contents of `01` and `03`–`09`. The folders themselves and their templates are the system; what fills them is the brand.

One deliberate exception: `02 logic/L5a applied direction - prmpt example.md` is a worked example from an unrelated brand ("prmpt"), kept because a concrete compiled prompt teaches the format better than a schema. Its header says so; its CDN links are stale and nothing in it applies to your brand.

## How this maps to the DRAPER system breakdown

DRAPER-wide, the documentation splits into four layers. This repo is the production-side instance of each:

- **Logic** — the concept-level material: what controls are, the control lists per production type, the AD-logic option vocabulary, how commentary becomes locked keywords. Here: `02 logic/blocks/`.
- **Function** — the runnable units: steps, tools, checks, prompts, rule blocks. Here: the L-step docs and `02 logic/tools/`.
- **Structure** — where things live and how they're served: the folder map, the doc shapes, the CDN convention, eventually the database and front end. Here: the numbered folders, the `_` templates, and the conventions in `00 index.md`.
- **Process** — the stages of a brand build and of production, and the loop that runs inside them. Here: `00 - START HERE.md` and the round/mode framing in `00 brand.md`.

## The core mechanic, in one paragraph

References plus the principal's commentary become expressions. An expression doc locks only the controls the commentary actually covered, written as keywords, terms, and phrases; everything else stays open, and cycling the open controls plus the variant directions inside the focus controls is what makes variations. Briefs package a content concept with knowledge, media CDNs, and expression directives; compiled prompts hand the build tools everything so they do nothing but build. Every output is captured at the moment of making, every variation set gets a production log round, and every failure is classified to the surface it lives on: fix the doc, fix the prompt, fix the build, or record the axis finding. The control set is the source of truth; prompts are disposable compilations.
