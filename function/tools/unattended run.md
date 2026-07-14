**Run on demand, UNDER A LOOP.** The autonomous production mode. The name is "unattended run," always — never "overnight run." **Critical: this does not run in one turn — it runs under a loop harness (`/loop`) that re-fires the agent until the completion gate is met.** A single turn always stops early; the loop is what makes it not stop. See "How this actually runs" below.

# Unattended Run

You are running production autonomously, with nobody watching. The failure mode is two-sided: **stopping early** (covering breadth, then wrapping up and reporting — the model's strongest instinct, and no prose rule reliably beats it: a real run quoted the "don't stop" rule and stopped anyway at 8 minutes of a 30-minute ceiling) and **going fast-and-shallow** (reskin variants, one tool for every job, build-once-and-move-on). The loop harness guards the first; the depth bar and critique gate guard the second. Cost is not the constraint; a considered, distinct, grounded, *deep* set is.

## Pre-flight — do this in-chat, then get one "go"

Quick, before any building:

1. **Read the brand** — `input/01 brief (strategy).md`, and read `01 settled/settled.md`. From settled, derive the **open/settled axes map**: which axes (type, palette, marks, composition, scale, detail…) are **settled** (honor exactly) vs **open** (must be explored). This map decides where your variations are allowed to diverge — write it into your plan.
2. **Confirm the queue and the ceiling.** What is this run building — which expressions/concepts, in what priority? And the time ceiling (or "until done"). If you weren't given a queue, propose one from the current state and say so.
3. **Verify the lanes are actually connected** (§ Lanes). A lane you'll need that isn't wired this session is a blocker — surface it now, not mid-run. A newly-added MCP may need a session reload.
4. **State the plan back** in a few lines (scope · lanes · ceiling · anything unresolved) and wait for an explicit **"go."** On "go," **launch the loop** (below) — don't try to do the whole run in this turn.

Requires that the brand is past intake and has expressions + at least one content concept (you build against a concept, never a blank page). If `02 expressions/` is empty, the run is a board pass + L1 first, not this.

## How this actually runs — under a loop, not one heroic turn

The #1 failure is **stopping early**: the agent covers breadth, writes a summary, and hands back, because finishing a turn is the model's strongest instinct and no in-doc "don't stop" reliably beats it. So the run is **not one long turn** — it's driven by a loop that re-fires the agent until the completion gate is met.

**Launch it under `/loop`, self-paced, with the ceiling** — e.g. `/loop` repeating "continue the unattended run per `function/tools/unattended run.md`, ceiling 30m." Each firing is **one iteration**: your job in this turn is only the next most valuable chunk, then let the loop bring you back. You are not trying to finish everything now.

**Each iteration:**
1. **Resume by reading state** — what already exists (the run log, `09 output/`, each unit's tally). Never rebuild what's done.
2. **Pick the next most valuable chunk** — the weakest/most-important unit still below its depth bar, or the next uncovered unit. One chunk, not the whole plan.
3. **Do it** (per-unit work below), update that unit's tally, log one line.
4. **Check the completion gate.** Not met → end the turn and let the loop fire again. Met → stop the loop and write the summary.

**The completion gate — the ONLY two reasons to end the whole run:**
- the **time ceiling** has been reached, **or**
- **every unit shows a full depth tally** (`dirs 3/3 · revise 2/2 · re-rolls 2/2 · craft ✓`).

**Breadth coverage is NOT a completion condition.** "All units have a baseline" is the trap that ended the 8-minute run. While the clock has time left and any unit is below its depth bar, there is *always* a next chunk — another revise cycle on a leader, another system on an open axis, a craft pass, the next uncovered unit. **If you catch yourself writing a run summary while time remains and bars are unfilled, that IS the failure: delete it and do the next chunk.**

## The principles (these govern every unit)

1. **Full scope, always.** Do everything the queue asks. Coverage is never what gets cut.
2. **Depth is the flex variable, not scope — and baseline is NOT done.** Build the whole scope breadth-first to a baseline, then **deepen weakest-first, and depth is mandatory up to the time ceiling.** Hitting baseline on everything and stopping is the #1 failure (a real run stopped at ~50 min of a 6h ceiling because it read "everything cleared the baseline" as "done"). Keep deepening until the ceiling hits or every unit clears the *depth* bar (§ the countable depth bar) — not the baseline bar.
3. **Time is a ceiling, not a target.** A big queue uses the time; a small one finishes when everything genuinely clears the depth bar, then *stops*. Never pad the clock, never rush it. But do not finish early just because breadth is covered — that's the trap in #2.
4. **Distinct on the OPEN axes — never a reskin, never a silent settle.** "Three structurally distinct directions" means distinct **on the axes that are open for this brand** (from your open/settled map). Honor settled axes exactly and get your divergence elsewhere. An **open axis is a mandate to explore** — put ≥3 genuinely different systems against each other *within the references' character* — never a blank check to invent, and never something to lock on pass 1. The enemy is not only the obvious reskin (same layout, swapped image) — it's the whole set quietly **sharing one system on an open axis** (one type system, one spacing rhythm, one detail language across every board) and calling breadth "done." That's a system-level reskin and it's fatal in an exploration round.
5. **Route each unit to the right lane** (below). Never force everything through one tool.
6. **Ground every design in a content concept, and follow the brand's L-steps** as the per-unit procedure. The critique loop wraps the L-steps; it doesn't replace them.
7. **Critique and revise against the written bar.** Don't build once and move on.

## Lanes — route by work type

This is the mapping of work → lane; the tool for each lane is named in its row (DRAPER's standard stack). **Paper is a single stateful session — run units serially, not in parallel; a parallel workflow is unsafe for one stateful plugin session.**

| Work type | Lane |
|---|---|
| **Web / UI compositions** | An HTML-rendering design tool (Claude Design / Paper / Artifacts): write real HTML/CSS, render, critique, iterate. Sync a winner into Figma only if a layered file is the deliverable. **Never coordinate-place original compositions in Figma** — that is the bad creative loop. |
| **Data / catalog treatments** | Same composition lane; keep the honesty + math discipline. |
| **Raster: illustration · texture · icons · marks** | An image-generation tool (e.g. Nano Banana Pro). **Never hand-code SVG for illustration** — it comes out geometric and cheap. |
| **Lettering / mark redraws** | Image-gen or a dedicated lettering pass — not composition tooling. |

## Per unit — the work of one unit (a chunk of an iteration)

When an iteration works a unit:

1. **Enter via an expression** (`02 expressions/[NN name]/doc.md` — locks are constraints, open controls are the variation space).
2. **Ground it in a content concept** (`07 content concepts/`) — never a blank page. Write one (L1) if none fits.
3. **Walk the L-steps:** L2 outline → L3 visual direction (pull the relevant expression docs + media/reference CDN docs) → L4 copy → L5 compile 2–3 build prompts, CDN links inline.
4. **Name three structurally distinct directions**, then generate them **in the right lane**.
5. **Critique against the bar** and **fill the countable depth bar** (both below): ≥2 critique → rewrite → rebuild cycles on the leader, ≥2 re-rolls on raster, an explicit craft pass. This is where the quality is won — a single pass is not a done unit.
6. **Capture at the moment of making** per `09 output/_contract.md` (tool · prompt · expressions in play · honest commentary · which open axes each variation moved), and copy into each source expression's `explorations/`.
7. **Run the production log round** (`production log round.md`) on the set, act on the fault line, then feed the expressions (new → new folder; developed → advance the doc; dead → say so).
8. **Move on once the depth bar is full** — then, after breadth is covered, keep deepening the weakest units until the ceiling. Baseline coverage is not the finish line; the ceiling (or every unit clearing the depth bar) is.

## The countable depth bar (baseline can't masquerade as done)

Keep a **visible per-unit tally** so you can't mistake breadth for depth. A unit isn't done until its tally is full or the ceiling hits:

`dirs 3/3 · revise 2/2 · re-rolls 2/2 · craft ✓`

- **dirs 3/3** — three directions that are genuinely distinct *on the open axes* (not a reskin, not a shared system).
- **revise 2/2** — at least two critique → rewrite → rebuild cycles on the leading direction. Single-pass is not done.
- **re-rolls 2/2** — for raster/image-gen units, at least two prompt re-rolls, not a one-shot.
- **craft ✓** — an explicit fine-craft pass: kerning, optical spacing, alignment, the small touches. Named, not assumed.

## The critique gate (the teeth)

A design is **rejected and redone** if any is true:

- the "variations" are one idea with a swapped attribute (reskin),
- **the whole set shares one system on an open axis** — one type system / one spacing rhythm / one detail language across every board when that axis was open to explore (system-level reskin),
- an **open axis got silently settled** on pass 1 instead of explored,
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

## When the run ends (gate met, not before)

Only once the completion gate is met — ceiling reached, or every unit's depth tally full — write a run summary at the top of the run log: units completed, per-unit tallies, keepers, open flaws, flagged questions, what needs the human's eye first. Then stop the loop.

If the gate is **not** met, there is no "end." The turn ends; the loop fires again and you do the next chunk. A summary is the last thing you write, never the thing that lets you stop early.
