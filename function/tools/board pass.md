**Run on demand** — once, with the user, after an exploration round and before production runs on its results. `02 expressions/` stays empty until this happens. Run it again after a round returns if the groupings need reworking.

# Board Pass

Organize an exploration round's board with the user: name the groupings, confirm the merges, and sort what's settled from what's open. This is a conversation, not an autonomous pass — the user judges the visuals, the AI works their words into structure.

## The board

The exploration round's outputs, grouped and marked up — wherever they live (Figma board, wall, folder of exports). The working grammar from the test round, reusable: implementation and application concepts on one side, specific graphic assets to make split off past a hard line; distinct concepts one per horizontal band, sub-directions branching inside a band; within a band, the references that kicked it off on the left, the explorations that came out on the right. If this brand's board is organized differently, say how before starting — the pass works on any grouping the user can walk band by band.

## Access

**First, check for a board.** Ask the user directly: "Is there a Figma / FigJam / whiteboard exploration board for this brand?" Don't assume there isn't one just because the export didn't include a link — a board is common and easy to forget to send.

- **If there's a board:** get the link and read it directly (Figma MCP) — frames plus the user's comments. This is the richest input.
- **If there's no board:** the "board" is the loaded export — the references carry the user's commentary (their per-item talk-through) and the explorations carry theirs. Work from those.

Either way the judgment is the user's; the AI works their words into structure. Reliable fallback in all cases: the user flips through and talks per band (transcribed); the AI never needs to see the images — the commentary is what gets worked.

## The pass, band by band

1. **Name and number it.** Short and referable ("preloader script", not a description), with a **zero-padded number prefix**: `01 color`, `02 editorial-layout`, `03 lettering` … Number them in board order (or priority) as you confirm them — the number is the stable handle everything else cites ("expression 03"); the name can be refined later without breaking the number. Naming vocabulary comes from `logic/` where it fits — don't mint new schema terms mid-pass; flag naming tensions instead.
2. **Say what it's keying on.** One or two sentences from the user: what this band is actually about, what they like, what it must not lose. This feeds the expression doc later — capture it raw.
3. **Confirm the grouping.** Is this band one expression or two? Should it merge with another? Are the sub-groupings right?
4. **Check the columns.** Expect a middle column between full composition concepts and graphic assets: very specific little things (a formatting move, a micro-copy treatment) that aren't full compositions. Confirm per band which of the three it is.

## Outputs — where things land

- One folder per confirmed expression in `02 expressions/NN name/` (zero-padded number + short name, e.g. `01 color`) — copy `_expression-template/` in and rename it, then drop the band's keying-on commentary into `feedback.md` verbatim. Tag which references from `04 references/` belong to this expression (name them in its `doc.md` — references stay in the central library, not copied). Move any staged explorations from `input/explorations/` into the expression's `explorations/`.
- Settled decisions into `01 settled/settled.md`, at their honest strength — near-locked stays near-locked. Questions the user explicitly keeps open go into `01 settled/settled.md` under an "Open questions" section (flag, don't decide), not mixed in with the settled decisions.
- Assets to make into `05 graphics/to-make.md`, with blockers named.
- Anything that dies on the board: note it died and why, so it doesn't resurface next round.
- Record the board link (if any) and what got decided in the board-pass record (`02 expressions/_board-pass-record.md`).

## After the pass — the next step is content concepts, not production

Expressions now exist, but `07 content concepts/` is still empty — and you build briefs from a content concept, never from a blank page. So the next move is **L1 (`function/steps/L1 content creation.md`)**: write the first content concepts from the strategy overview + knowledge + media. Only once at least one content concept exists do you enter the production loop (pick an expression + a concept → L2–L5 brief → compile → produce). Don't jump straight from the board pass to "pick an expression and run variations" — there's nothing to build against yet.
