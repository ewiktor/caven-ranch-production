# START HERE — running a DRAPER production round

This is the human guide. Agents orient with `CLAUDE.md` and `00 index.md` instead; the step docs in `function/steps/` each carry their own Reads/Writes header.

## What this repo is

One brand's production repo, duplicated from the DRAPER production template. The system — the loop, the logic steps, the blocks and tools, the templates — is universal and identical across brand repos. The brand — its strategy, knowledge, media, references, expressions, and everything produced — lives in the numbered folders. `input/01 brief (strategy).md` is the brand's strategy overview; `00 intake.md` is how a new brand gets loaded in.

## The loop you're running

0. **Round-1 startup, from a freshly loaded brand.** If `02 expressions/` is empty, that's correct — you haven't done the board pass yet. The bootstrap order is: **board pass** (`function/tools/board pass.md`, with the user) forms the expressions from the references + explorations → **L1** writes the first content concepts from the strategy (`07 content concepts/` is empty and you can't build a brief without one) → *then* the production loop below. Don't jump from the board pass straight to producing — you need at least one content concept first.

1. **Open an expression before you make anything.** Each folder in `02 expressions/` is one idea that survived exploration. Its `doc.md` tells you what it is, what the user likes about it, which controls are locked (written as keywords, terms, and phrases — follow these exactly), and what's deliberately open. The open controls are your variation space: cycle them to make versions, don't touch the locked ones. `feedback.md` is the user's raw commentary if you want the unfiltered read. The references it came from are tagged in `04 references/`; `explorations/` shows where it's been.

2. **Work from a content concept, not a blank page.** `07 content concepts/` holds the decided pieces — each one says what the piece is for, who it moves, the one message, and the angle. If a concept doesn't exist yet for what you want to make, it gets written first (step L1 in `function/steps/`).

3. **Build the brief.** Per concept, walk the steps in `function/steps/`: L2 outline (what it covers, in what order, the single point), L3 visual direction (which expressions are in play, which media lands where — this is where you pull the expression docs and the media CDN docs), L4 copy. Each step doc says exactly what to read and where to write. The result accumulates in `08 briefs/[concept]/`.

4. **Compile — that's the deliverable.** L5 turns the finished brief into 2–3 build prompts (full spec, CDN links inline). The loop stops here: the compiled prompts are what this repo produces. Building the design from them — running a prompt in Paper / image tools, the recursive build-and-critique — is a separate step that lives in `function/tools/unattended run.md`, or the user runs the prompts themselves. You do not build the design in this loop.

**When built outputs come back:**

5. **Capture at the moment of making** per `09 output/_contract.md` — which tool, which prompt, which expressions were in play, and the honest commentary — and copy it into each source expression's `explorations/`. Feedback left in your head is gone.

6. **Round, then feed.** When a variation set completes, run `function/tools/production log round.md` — the self-QA that classifies every failure to the surface it lives on. Then feed the expressions: new idea → new folder; developed → advance the doc version; dead → say so and stop carrying it.

## The bar

Output needs to be good enough to really *see* a specific expression in the light of this brand — copy doesn't have to be final, media picks don't have to be final. What a round mainly produces is (a) outputs, and (b) developed expression docs and captured judgment the next round builds on.

## Rules that don't bend

- Locked controls in an expression doc are locked. Variation comes from the open ones.
- `01 settled/` items are constraints, never considerations.
- Facts come from `06 knowledge/` only: no invented facts, nothing planned framed as already real.
