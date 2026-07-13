# START HERE — running a DRAPER production round

This is the human guide. Agents orient with `CLAUDE.md` and `00 index.md` instead; the step docs in `02 function/steps/` each carry their own Reads/Writes header.

## What this repo is

One brand's production repo, duplicated from the DRAPER production template. The system — the loop, the logic steps, the blocks and tools, the templates — is universal and identical across brand repos. The brand — its brief, knowledge, media, references, expressions, and everything produced — lives in the numbered folders. `00 brand.md` says which brand this is and where the work stands; `00 intake.md` is how a new brand gets loaded in.

## The loop you're running

0. **If `04 expressions/` is still empty and the brand arrived cold, that's correct.** The first exploration round plus a board pass (`02 function/tools/board pass.md`, run with the principal) is what fills it. Don't skip to briefs.

1. **Open an expression before you make anything.** Each folder in `04 expressions/` is one idea that survived exploration. Its `doc.md` tells you what it is, what the principal likes about it, which controls are locked (written as keywords, terms, and phrases — follow these exactly), and what's deliberately open. The open controls are your variation space: cycle them to make versions, don't touch the locked ones. `feedback.md` is the principal's raw commentary if you want the unfiltered read. `refs/` and `explorations/` show where it came from and where it's been.

2. **Work from a content concept, not a blank page.** `08 content concepts/` holds the decided pieces — each one says what the piece is for, who it moves, the one message, and the angle. If a concept doesn't exist yet for what you want to make, it gets written first (step L1 in `02 function/steps/`).

3. **Build the brief.** Per concept, walk the steps in `02 function/steps/`: L2 outline (what it covers, in what order, the single point), L3 visual direction (which expressions are in play, which media lands where — this is where you pull the expression docs and the media CDN docs), L4 copy (good enough for the round's mode — see the bar below). Each step doc says exactly what to read and where to write. The result accumulates in `09 briefs/[concept]/` in the template's shape.

4. **Compile, then produce.** L5 turns the finished brief into 2–3 build prompts (full spec, CDN links inline, so the tool does nothing but build). Run those in the tools named in `00 brand.md`.

5. **Capture at the moment of making.** Before moving to the next thing: screenshot/export the result and write the small markdown per `10 output/_contract.md` — which tool, which prompt, which expressions were in play, and your honest commentary. Then copy that capture into each source expression's `explorations/`. Feedback captured in the moment is what the next round runs on; feedback left in your head is gone.

6. **Round, then feed.** When an expression's variation set completes, run `02 function/tools/production log round.md` — the self-QA that classifies every failure to the surface it lives on and acts on it. Then feed the expressions: new idea surfaced → new expression folder. Existing idea developed → its doc.md advances (V2, V3). Idea died → say so in the doc and stop carrying it.

## The bar

Set per round in `00 brand.md`. In a high-volume round, copy doesn't need to be perfect and media picks don't need to be final — the output needs to be good enough to really see a specific expression in the light of this brand. What a volume round produces is (a) outputs, yes, but mainly (b) developed expressions docs and captured judgment that the slower rounds build on. In slow production, the full checks gate.

## Rules that don't bend

- Locked controls in an expression doc are locked. Variation comes from the open ones.
- `03 settled/` items are constraints, never considerations.
- Open questions listed in `00 brand.md` belong to the principal — flag them when your work touches them, don't decide them.
- Facts come from `07 knowledge/` only: no invented facts, nothing planned framed as already real.
- Check tiering per `00 index.md`, mode per `00 brand.md`.
