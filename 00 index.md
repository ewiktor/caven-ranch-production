# Index — glossary and map

Orientation for an agent landing cold. Read `00 brand.md` first (the brand binding), then this once, then follow the Reads/Writes header at the top of whichever step doc you are running — the headers are the routing, not this file. Humans start at `00 - START HERE.md`.

## Glossary

Names marked (unsettled) are working names — use them, don't harden them, don't rename them mid-run.

- **Expression** (unsettled name) — a specific brand thing that coalesced out of exploration and gets developed in its own right. At least three types: brand expressions (logo, color, type, photography, layout, graphics), content-concept expressions (recurring subject matter), and conceptual expressions. One expression = one folder in `02 expressions/`.
- **Expressions doc** — the markdown that holds one expression: short human write-up, the locked controls as keywords/terms/phrases, what stays open, negative directives, its references tagged from `04 references/`, and `explorations/` attached. Shape: `02 expressions/_expression-template/doc.md`.
- **Controls** (unsettled) — the word-lever idea: keywords, terms, and phrases are what make the output. The controls for a production type are listed in `logic/controls - *.md`.
- **Control set** — the written artifact, distinct from Controls-the-idea: human-language direction per control, filled with keywords/terms/phrases, varying by production type. The tie: translation logic → AD logic → keywords/terms/phrases → the written control set.
- **AD logic** — per control, the options and what each one does, produces, and feels like. `logic/ad logic - *.md`.
- **Locked / filled / cycled controls** (DRAPER fill-states, per the schema board) — the governing mechanic. A production type has a full control list; each control ends up in one of three states: **locked** — the principal's commentary spoke to it, so it's fixed as keywords/terms/phrases (typically only a few of the full set); **filled** — a subject-matter control, determined by the actual `06 knowledge/` and `03 media/`, not free to invent; **cycled** — genuinely open, and cycling these is what makes the variations. Two hard rules: a lock is never absolute or one-directional unless the principal's words were — hedges stay hedged, and negatives record only things the principal killed. And filling/cycling a non-locked control follows this order: the references this expression tags (in `04 references/`) → the principal's documented taste across the other expression docs (docs cite each other as evidence freely) → 01 settled + 06 knowledge → the principal's live direction in session, which supersedes stale doc text and must be written back the same session, version-bumped → the agent's own judgment last, flagged as such.
- **Focus controls** — the controls an expression study is actually testing. They usually admit multiple variant directions (a hedge is a fork, not a lock); building those directions as distinct variations is half of where variation comes from.
- **Scenario** (unsettled name) — where one expression's meaning depends on the state of another, variations get built as explicit scenario-worlds — same mockup, different world — and judged as worlds against each other, not as isolated specimens. A doc that carries scenarios names them in their own section, with any build dependencies. Otherwise, variations are judged against their own expression doc only; cross-expression mentions are context and evidence, never constraints.
- **Message flow** (name unsettled) — building one piece, in order: **editorial outline** (the message and info in rough order, no application) → **visual direction** (what media, how and where, soft implementation ideas, not directives) → **copywriting** (the copy) → **applied direction** (the dialed final pass, copy and message matched to direction piece by piece). Steps L2–L5 in `function/steps/`.
- **Content concept** — a decided piece of content to make: one small goal under the big goal, one move for one person, one message, an angle, an execution. One md per concept in `07 content concepts/`.
- **Brief** (expression brief, unsettled) — the packaged handoff per content concept: outline, whittled media CDNs, knowledge chunks, and expression directives, handed to the build tools. Shape: `08 briefs/_brief-template.md`.
- **Reference** — an external image/video the principal gathered as inspiration, with their commentary. Lives in the reference library `04 references/` (one md per reference: description + the principal's commentary + CDN link). The commentary is what becomes locked controls; the asset is what the agent studies. Distinct from media (the brand's own assets, `03 media/`). Brand identity that arrives as a reference (an existing logo) is tagged as such and may also seed `05 graphics/`.
- **Derivation / exploration** — one output made from a brief (or directly from a reference). Captured per `09 output/_contract.md`.
- **Block** — pull-in logic: a doc an agent folds into a prompt (`logic/`). **Tool** — an action prompt run on demand (`function/tools/`). **Step** — an L-numbered action doc in `function/steps/` with a Reads/Writes header.
- **Settled** — decisions off the consideration table (`01 settled/settled.md`). Constraints in prompts, never considerations.
- **Learnings** — reusable tool and prompt findings (`01 settled/learnings.md`). Checked before every compile; toolchain findings transfer between brand repos, brand findings never do.
- **The principal** — the human creative lead named in `00 brand.md` whose judgment governs: source of locks, kills, and settled decisions.

## Map

```
input/               strategy brief + raw brand material + new-references/ inbox
logic/            control sets · controls · ad logic (the pull-in "blocks")   [SYSTEM]
function/         steps/ (L1–L8 message flow) · tools/ (run on demand)         [SYSTEM]
01 settled/          settled.md (decisions off the table) · learnings.md (tool findings)
02 expressions/      one folder per expression: doc.md, feedback.md, explorations/ (references tagged from 04 references/)
03 media/            one md per asset (description + CDN link) + assets/
04 references/       reference library — one md per reference (description + principal's commentary + CDN) + assets/
05 graphics/         existing/made brand marks + one md per asset + to-make.md
06 knowledge/        the brand's fact base (raw input to briefs; production agents don't read this directly)
07 content concepts/ one md per concept (_template.md)
08 briefs/           one folder per concept: the brief + compiled prompts (_brief-template.md)
09 output/           what tools produce, captured per _contract.md
```

## Conventions

- Root numbers (01–09) are all brand — the material that flows through a round; the system (`logic/`, `function/`) and `input/` sit outside the numbers. L-numbers are the message-flow steps. Never refer to a step by bare number.
- Files starting with `_` are templates or contracts, not content.
- Every step doc opens with **Reads:** and **Writes:** — that header is authoritative for what to pull in and where results go.

## Check tiering

The current round's mode is in `00 brand.md`.

- Always on, every output: the hard-truth rules — no invented facts, nothing planned framed as already real, facts sourced from `06 knowledge/`.
- High-volume rounds: L7 and L8 are a fast gut-pass for the hard rules above, not a full stylistic audit. Phrasing and polish enforcement is a slow-production pass, not a volume-round gate.
- L6 (AD check) fires only when a compiled control set or build prompt is about to run — not on every rough derivation.
