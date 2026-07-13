**Run on demand** — once, when a DRAPER app export folder is dropped into a fresh clone of this template. This is the automated version of `00 intake.md`: it takes the brand's export and files everything into place. After it runs, the repo is loaded and the first board pass can happen.

# Load Brand

You've been handed a brand export folder (the DRAPER app produces these). Your job is to load it into this repo — place every file, conform it to the template's shapes, merge the commentary, verify the CDN links, and report what's missing. Do not produce anything creative here; this is placement and conforming only. **Do not create expressions** — that's the board pass, run later with the user.

## What the export looks like

A DRAPER app export folder contains (folder names may vary slightly):

```
brief.md                              a manifest — an index linking everything below. Your load map.
production-notes/
  strategy-overview-*.md              the strategy digest
knowledge/*.md                        one md per domain (facts)
media/
  [name].md                           one md per asset: Description + Assets + CDN Links
  assets/[name]                       the actual assets
  context.md                          bulk CDN index (no commentary)
references/
  [name].md                           one md per reference: Description + CDN
  assets/[name]                       the actual references (images, video)
  context.md                          per-reference USER COMMENTARY + CDN  ← the load-bearing part
explorations/
  [name].md                           one md per prior output: User Context + Prompt + CDN
  assets/[name]                       the actual outputs
  context.md                          per-exploration commentary + CDN
```

Not every export has every folder. Some also carry an identity/brand-elements set. Load what's there; note what isn't.

## The mapping

| Export | → This repo |
|---|---|
| `production-notes/strategy-overview*.md` | `input/01 brief (strategy).md` |
| `brief.md` (manifest) | your load map — not copied in |
| `knowledge/*.md` | `06 knowledge/` |
| `media/[name].md` + `media/assets/` | `03 media/` + `03 media/assets/` |
| `references/[name].md` + `assets/` + `context.md` | `04 references/` (+ merge commentary — see below) |
| `explorations/[name].md` + `assets/` | `input/explorations/` (staging for the board pass) |

## Steps

1. **Read the manifest** (`brief.md`) to see the full inventory. Read each folder's `context.md` — that's where the user's commentary lives.

2. **Strategy → `input/01 brief (strategy).md`.** Copy the strategy overview in. Strip any app-only header (e.g. `**Source type:** text_note`) and any duplicated title. Confirm it has the expected sections (Task · Who this is for · Who the brand is now · Offering · Messaging · Why · What it needs to do · Desired outcome).

3. **Fill `00 brand.md` from the strategy overview** — the brand, what's being made, the one-line. That's enough to bind the repo. The round/mode/toolchain fields have defaults (Round 1, high-volume, toolchain confirmed at first build) — leave them at their defaults; they don't block loading or the board pass. There is no "user/principal" field to fill — the human directing the session is the authority, and the loaded commentary is the authority of record. Don't invent a goal or a toolchain; leave the placeholders and note them in your report so they get confirmed when production starts.

4. **Knowledge → `06 knowledge/`.** Copy each md as-is. If filenames aren't dated, leave them; note it.

5. **Media → `03 media/`.** Copy each `[name].md` to `03 media/` and each asset to `03 media/assets/`. Each md already carries Description + CDN — leave it. Discard `media/context.md` (it's a bulk CDN index, redundant with the per-asset mds). Confirm every media md has its CDN link.

6. **References → `04 references/` — and MERGE the commentary.** Copy each `[name].md` to `04 references/` and each asset to `04 references/assets/`. Then, for each reference, pull its commentary from `references/context.md` (match by title) and write it into that reference's md under a `## User context` section, verbatim. This is the most important step — the commentary is what becomes locked controls, and it must live with each reference, not in a separate file. Follow `04 references/_reference-doc-template.md` for the shape. **Tag identity references** (an existing logo, monogram, wordmark) in their `## User context` and list them in your report — they may also seed `05 graphics/`, but leave that call to the board pass.

7. **Explorations → `input/explorations/`.** Copy each md + asset. These are prior outputs (each has the user's commentary + the prompt that made it). They are pre-board-pass — do NOT turn them into expressions. They stage here until the board pass groups them.

8. **Verify integrity.** Every media / reference / exploration md must have (a) a CDN link and (b) a local asset path that resolves. Where a per-item md is missing a CDN, pull it from that folder's `context.md`. Flag anything still broken.

9. **Report.** Write a short load report to the chat:
   - counts loaded per folder,
   - `00 brand.md` is bound (brand + strategy in place); the round/mode/toolchain defaults hold until production — no need to stop for them,
   - identity references found and flagged,
   - anything missing or broken,
   - and the next step: **a board pass** (`function/tools/board pass.md`) to form expressions from the references + explorations + commentary, since `02 expressions/` is still empty.

## What stays empty after loading

`02 expressions/`, `07 content concepts/`, `08 briefs/`, `09 output/`, and usually `01 settled/` and `05 graphics/to-make.md`. These are produced through the loop, not loaded. If the strategy or commentary states a genuinely settled decision (a locked color, a mark that won't change), you may note it in `01 settled/settled.md` as near-locked pending the user — but don't over-reach; most "settled" lands during the board pass.

## The bar

After this runs, a person should be able to open the repo, fill the three missing `00 brand.md` fields, and start a board pass — with every asset in place, every reference carrying its commentary, and every CDN link live. Placement and conforming only; no creative decisions, no expressions.
