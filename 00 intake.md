# Intake — dropping a new brand into this template

Duplicate the template repo, then work down this list. The system (CLAUDE.md, `00 index.md`, everything in `01 logic/` and `02 function/`, and the `_` templates) does not change per brand. Everything below is what does.

A brand will arrive with varying degrees of material. Nothing on this list except the first two items blocks starting — the step docs all state what they do when a module is missing. Fill what exists, flag what doesn't.

## 1. Bind the brand — required

- [ ] Fill `00 brand.md` completely: brand, principal, round + mode, toolchain, state line, open questions. An agent landing in a repo with an unfilled brand.md is instructed to stop.
- [ ] Drop the strategy brief into `input/` (`01 brief (strategy).md`). If a communications/content strategy exists, it goes next to it. If no brief exists yet, writing one is the first job of the engagement, not a template task.

## 2. Knowledge — `07 knowledge/`

- [ ] One md per domain (the building, the region, the operation, the catalog — whatever the brand's domains are), per `07 knowledge/_knowledge-doc-template.md`. Date-stamp the filenames.
- [ ] Facts only, sourced. This folder is the hard-truth base: if it isn't in here, production can't state it.

## 3. Media — `05 media/`

- [ ] Assets into `05 media/assets/`.
- [ ] One md per asset in `05 media/Media Markdown Docs/`, per `_media-doc-template.md`: description (what it shows, what it carries), local path, and the CDN link. **The CDN link is what compiled prompts use — a media doc without one is not done.**
- [ ] Subfolders for processed families (e.g. improved/doctored versions of current photography) are fine; each still gets its md.

## 4. References — `input/new-references/` → `04 expressions/`

- [ ] Raw references the brand or principal supplies land in `input/new-references/` as an inbox.
- [ ] References only become production material once they are attached to an expression: a folder in `04 expressions/` with the reference in `refs/`, the principal's commentary in `feedback.md`, and a `doc.md` written per the expression doc writer tool. If the brand arrives pre-explored (a prior round happened), port each surviving idea as one expression folder.
- [ ] If the brand arrives cold (no exploration yet), `04 expressions/` stays empty until the first round's board pass — that is correct, not a gap.

## 5. Graphics — `06 graphics/`

- [ ] Existing brand marks/graphics: asset + one md each (use the mark analyzer tool for wordmarks and lettering).
- [ ] Assets that need making go on `06 graphics/to-make.md`, ordered, with blockers named (an asset that blocks judging an expression goes first).

## 6. Settled — `03 settled/`

- [ ] Anything already decided and off the table (colors locked by an existing identity, a mark that is not changing) goes into `settled.md` with its provenance. Only real decisions — near-locked items are recorded as near-locked, pending the principal's confirm.
- [ ] `learnings.md` starts empty except for any toolchain findings ported from previous brand repos that used the same tools (tool findings transfer; brand findings never do).

## 7. Concepts and briefs — usually empty at intake

- [ ] `08 content concepts/`, `09 briefs/`, `10 output/` start empty (templates and contract in place). They fill through the L-steps. Port them only if a prior round genuinely produced them.

## 8. Verify

- [ ] Grep the repo for the previous brand's name, people, and URLs — a duplicated repo must carry zero of the source brand. (`02 function/steps/L5a` is the one sanctioned exception: it is a worked example and says so in its header.)
- [ ] Read `CLAUDE.md` top to bottom once as if you were the landing agent: every pointer it makes must resolve to something real in this repo.
- [ ] Update the state line in `00 brand.md` and commit.
