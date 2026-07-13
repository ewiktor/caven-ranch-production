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

**The placement is done by a script, not by hand** — hand-copying drops files (explorations got skipped in early testing). Run the script, then do the judgment half.

1. **Run the load script:**

   ```
   python3 "function/tools/load-brand.py" <path-to-the-brand-export-folder>
   ```

   Run it from the template repo root. It deterministically: places the strategy overview → `input/01 brief (strategy).md` (stripping the app header); knowledge → `06 knowledge/`; media docs + bundled assets → `03 media/`; reference docs + assets → `04 references/` **and merges each reference's commentary from `context.md` into its own `## User context` section**; and stages explorations (docs + assets) → `input/explorations/`. It prints a report of counts per folder. It does **not** download assets — the CDN link in each doc is the asset of record; local asset files are only those the export bundled (so `03 media/assets/` is often sparse — that's the export being CDN-only, not a failure).

2. **Check the report against the export.** Counts should match: every knowledge/media/reference/exploration doc placed, references' commentary merged, explorations staged. If a count is off, the export folder is shaped unusually — read `brief.md` (the export manifest) and place the odd ones by hand.

3. **The strategy overview is the binding.** `input/01 brief (strategy).md` (placed by the script) is what tells every agent which brand this is — there's nothing else to fill. Confirm it landed and reads right.

4. **Tag identity references.** Scan `04 references/` for existing brand marks (a logo, monogram, wordmark — the commentary usually says "the original logo"). Note them in the report; they may also seed `05 graphics/`, but leave that call to the board pass.

5. **Ask about a board, then report.** Write a short report: the script's counts, identity references found, and **ask whether there's an exploration board** (Figma / FigJam / whiteboard). The user may have one and not have included the link. If yes, hold onto it for the board pass. Then name the next step: **a board pass** (`function/tools/board pass.md`) to form expressions from the board (if any) plus the references + explorations + commentary, since `02 expressions/` is still empty.

## What stays empty after loading

`02 expressions/`, `07 content concepts/`, `08 briefs/`, `09 output/`, and usually `01 settled/` and `05 graphics/to-make.md`. These are produced through the loop, not loaded. If the strategy or commentary states a genuinely settled decision (a locked color, a mark that won't change), you may note it in `01 settled/settled.md` as near-locked pending the user — but don't over-reach; most "settled" lands during the board pass.

## The bar

After the script runs and you've done the judgment half, a person can open the repo, read the strategy overview, and start a board pass — every doc placed, every reference carrying its commentary, every CDN link intact, explorations staged. Placement and conforming only; no creative decisions, no expressions.

## Note on assets

The script never downloads. The CDN link inside each media/reference doc is the asset of record — that's what compiled build prompts use, and it resolves in the DRAPER environment even when a plain fetch 404s. Local files under `assets/` are only the ones the export bundled, so those folders are often partial. That is expected; do not treat a sparse `assets/` as a broken load. If a local copy is ever needed, download it in the environment where the CDN is authenticated.
