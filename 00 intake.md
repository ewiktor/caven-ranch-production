# Intake — dropping a new brand into this template

Duplicate the template repo, then work down this list. The system (CLAUDE.md, `00 index.md`, everything in `logic/` and `function/`, and the `_` templates) does not change per brand. Everything below is what does.

A brand will arrive with varying degrees of material. Nothing on this list except the first two items blocks starting — the step docs all state what they do when a module is missing. Fill what exists, flag what doesn't.

## The fast path — a DRAPER app export

If the brand arrives as a **DRAPER app export folder** (a folder with `brief.md` + `production-notes/` + `knowledge/` + `media/` + `references/` + `explorations/`), don't work this list by hand. Follow **`function/tools/load brand.md`** — its first step runs a deterministic script (`function/tools/load-brand.py <export-folder>`) that places every file, merges each reference's commentary, and stages the explorations, then you do the judgment half (confirm the strategy overview, ask about a board) and run a board pass.

The checklist below is the **manual/fallback path and the spec** for what each folder expects when a brand doesn't arrive as a clean export.

## 1. Bind the brand — required

- [ ] The **strategy overview** at `input/01 brief (strategy).md` is the brand binding — the load script places it from the export. Confirm it's there and reads right. There's no separate brand file to fill. An agent landing in a repo where that file is absent treats it as unloaded and asks for the brand export.
- [ ] **Paste in the strategy overview.** The overview is written OUTSIDE the repo — the repo never compiles it. Copy `function/tools/strategy overview writer.md` into a separate chat, give it the brand's strategy materials, and paste its output into `input/01 brief (strategy).md`. That digest is what the L-steps read. If no strategy exists yet, producing it is the first job of the engagement, not a template task.

## 2. Knowledge — `06 knowledge/`

- [ ] One md per domain (the building, the region, the operation, the catalog — whatever the brand's domains are), per `06 knowledge/_knowledge-doc-template.md`. Date-stamp the filenames.
- [ ] Facts only, sourced. This folder is the hard-truth base: if it isn't in here, production can't state it.

## 3. Media — `03 media/`

- [ ] Assets into `03 media/assets/`.
- [ ] One md per asset in `03 media/`, per `_media-doc-template.md`: description (what it shows, what it carries), local path, and the CDN link. **The CDN link is what compiled prompts use — a media doc without one is not done.**
- [ ] Subfolders for processed families (e.g. improved/doctored versions of current photography) are fine; each still gets its md.

## 4. References — `04 references/` (the reference library)

- [ ] One md per reference in `04 references/`, asset in `04 references/assets/`, per `_reference-doc-template.md`: **Description** (what it is) + **User context** (the user's commentary, verbatim — this is what becomes locked controls) + the **CDN link**. A reference without its commentary is half-loaded.
- [ ] Identity references (an existing logo, monogram, wordmark) get tagged as such in their User context, and flagged — they may also seed `05 graphics/`.
- [ ] The reference library is central: expressions point into it, references aren't copied per expression.

## 4b. Explorations — `input/explorations/` (if the brand arrives pre-explored)

- [ ] Prior outputs (each with the user's commentary + the prompt that made it) stage in `input/explorations/`. They are NOT expressions yet.
- [ ] The first **board pass** (`function/tools/board pass.md`) forms expressions from the references + explorations + commentary, and files each exploration into its expression. If the brand arrives cold (no explorations), `02 expressions/` and `input/explorations/` stay empty until that first board pass — correct, not a gap.

## 5. Graphics — `05 graphics/`

- [ ] Existing brand marks/graphics: asset + one md each (use the mark analyzer tool for wordmarks and lettering).
- [ ] Assets that need making go on `05 graphics/to-make.md`, ordered, with blockers named (an asset that blocks judging an expression goes first).

## 6. Settled — `01 settled/`

- [ ] Anything already decided and off the table (colors locked by an existing identity, a mark that is not changing) goes into `settled.md` with its provenance. Only real decisions — near-locked items are recorded as near-locked, pending the user's confirm.
- [ ] `learnings.md` starts empty except for any toolchain findings ported from previous brand repos that used the same tools (tool findings transfer; brand findings never do).

## 7. Concepts and briefs — usually empty at intake

- [ ] `07 content concepts/`, `08 briefs/`, `09 output/` start empty (templates and contract in place). They fill through the L-steps. Port them only if a prior round genuinely produced them.

## 8. Verify

- [ ] Grep the repo for the previous brand's name, people, and URLs — a duplicated repo must carry zero of the source brand. (`function/steps/L5a` is the one sanctioned exception: it is a worked example and says so in its header.)
- [ ] Read `CLAUDE.md` top to bottom once as if you were the landing agent: every pointer it makes must resolve to something real in this repo.
- [ ] Commit.
