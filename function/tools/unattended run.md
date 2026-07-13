**Run on demand** — the autonomous production mode. Run it in-chat on a bound brand and it works the production loop by itself until the queue clears the bar or the time ceiling hits. The name is "unattended run," always — never "overnight run." This is the in-repo, run-and-go version of the method; it is self-contained (you don't need any external skill to run it).

# Unattended Run

You are about to run production autonomously, with nobody watching. The failure mode of autonomous runs is two-sided: **stopping** (on an error, an ambiguity, or the instinct to wrap up and report) and **going fast-and-shallow** (coverage over quality — reskin variants, one tool for every job, build-once-and-move-on). This tool guards both. Cost is not the constraint; a considered, distinct, grounded set is.

## Pre-flight — do this in-chat, then get one "go"

Quick, before any building:

1. **Read the brand** — `input/01 brief (strategy).md`, and skim `01 settled/settled.md` for constraints and the open questions you must flag-not-decide.
2. **Confirm the queue and the ceiling.** What is this run building — which expressions/concepts, in what priority? And the time ceiling (or "until done"). If you weren't given a queue, propose one from the current state and say so.
3. **Verify the lanes are actually connected** (§ Lanes). A lane you'll need that isn't wired this session is a blocker — surface it now, not mid-run. A newly-added MCP may need a session reload.
4. **State the plan back** in a few lines (scope · lanes · ceiling · anything unresolved) and wait for an explicit **"go."** After that, do not check in until the run ends.

Requires that the brand is past intake and has expressions + at least one content concept (you build against a concept, never a blank page). If `02 expressions/` is empty, the run is a board pass + L1 first, not this.

## The principles (these govern every unit)

1. **Full scope, always.** Do everything the queue asks. Coverage is never what gets cut.
2. **Depth is the flex variable, not scope.** Build the whole scope breadth-first to a baseline, then deepen weakest-first. Half the units at 3 iterations and half at 2 is a good run; half *unbuilt* is a bad run, even if the built half is perfect.
3. **Time is a ceiling, not a target.** A big queue uses the time; a small one finishes when genuinely good, then *stops*. Never pad the clock, never rush it.
4. **Three structurally distinct directions, never reskins.** Variations must differ in layout logic, type system, or compositional idea — not a swapped image or word. **Name the three distinct directions before building.** If you can't name three, build fewer, better.
5. **Route each unit to the right lane** (below). Never force everything through one tool.
6. **Ground every design in a content concept, and follow the brand's L-steps** as the per-unit procedure. The critique loop wraps the L-steps; it doesn't replace them.
7. **Critique and revise against the written bar.** Don't build once and move on.

## Lanes — route by work type

This is the mapping of work → lane; the tool for each lane is named in its row (DRAPER's standard stack).

| Work type | Lane |
|---|---|
| **Web / UI compositions** | An HTML-rendering design tool (Claude Design / Paper / Artifacts): write real HTML/CSS, render, critique, iterate. Sync a winner into Figma only if a layered file is the deliverable. **Never coordinate-place original compositions in Figma** — that is the bad creative loop. |
| **Data / catalog treatments** | Same composition lane; keep the honesty + math discipline. |
| **Raster: illustration · texture · icons · marks** | An image-generation tool (e.g. Nano Banana Pro). **Never hand-code SVG for illustration** — it comes out geometric and cheap. |
| **Lettering / mark redraws** | Image-gen or a dedicated lettering pass — not composition tooling. |

## Per unit — the loop you actually run

For each unit in the queue:

1. **Enter via an expression** (`02 expressions/[NN name]/doc.md` — locks are constraints, open controls are the variation space).
2. **Ground it in a content concept** (`07 content concepts/`) — never a blank page. Write one (L1) if none fits.
3. **Walk the L-steps:** L2 outline → L3 visual direction (pull the relevant expression docs + media/reference CDN docs) → L4 copy → L5 compile 2–3 build prompts, CDN links inline.
4. **Name three structurally distinct directions**, then generate them **in the right lane**.
5. **Critique against the bar** (below). Redo or rewrite the weak one. Regenerate. This is where the quality is won.
6. **Capture at the moment of making** per `09 output/_contract.md` (tool · prompt · expressions in play · honest commentary · which axes each variation moved), and copy into each source expression's `explorations/`.
7. **Run the production log round** (`production log round.md`) on the set, act on the fault line, then feed the expressions (new → new folder; developed → advance the doc; dead → say so).
8. **Move on.** Later passes deepen the weakest units.

## The critique gate (the teeth)

A design is **rejected and redone** if any is true:

- the "variations" are one idea with a swapped attribute (reskin),
- it isn't grounded in a real content concept (generic),
- the type is default / AI-generic or not matched to the reference's character,
- it reads cheap: boxy, evenly-spaced, timid scale/whitespace, no compositional tension,
- it leans on decoration instead of one strong idea.

**Stop condition per unit:** it clears the bar, *or* N revise-cycles pass with no improvement, *or* the per-unit budget is hit — then record what was rejected and why, and move on. The production log round's "clean requires receipts" holds: name the comparison, cite every claim to a control/ref/knowledge, no self-grading by vibe.

## Anti-stop rules (because no one's watching)

- **Errors:** retry once, then log it and move to the next unit. Never let one failure stall the run.
- **Questions only the human can answer:** flag them in the log, take the least-committal path that keeps the unit moving, mark the output "(pending [question])." Never wait.
- **Doc ambiguity:** resolve per the fill order (refs → documented taste → settled + knowledge → your judgment, flagged). A gap is a flag, not a pause.
- **Do not check in mid-run** because a result is good, or to report progress. Capture and continue.
- **`settled/` is never re-opened; the open questions recorded in `01 settled/settled.md` are flagged, not decided.**

## Token / effort discipline

Terse self-critiques, one compact log entry per round, one generation per attempt, view each source once. Reusable tool/prompt findings go once into `01 settled/learnings.md` — check it before every compile, never re-derive.

## When the run ends

Write a run summary at the top of the run log: units completed, keepers, open flaws, flagged questions, what needs the human's eye first. Then stop.
