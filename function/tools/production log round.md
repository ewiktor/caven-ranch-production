**Run on demand** — per expression, the moment its variation set completes (a substantive stopping point: the batch of derivations for one expression exists and is captured). Vocabulary authority is this repo's own blocks (`controls - composition.md` / `ad logic - composition.md`) — never an external prompt table, which may lag them.

# Production Log Round

Review one expression's just-finished variation set and act on what the review finds. The per-derivation capture (`09 output/_contract.md`) records what was made; the round is the QA — the system checks itself, nothing waits on a human. A round that only logs has failed.

## The loop

This tool is one station in a cycle that repeats *within* the expression until it converges:

**compile/state the build decisions in the open — chat or brief, no invisible steps → build → self-review against doc + refs → round (this doc) → implement the fix at the level the fault line names → if doc-level, revise the control set (doc.md) → build again → round again.**

**One round per variation set by default** — re-enter the build-again loop only when the round finds a doc or prompt fault worth rebuilding for; otherwise record, deliver, and move to the next expression. Later passes return to an expression with the prior round's preserve/avoid in hand. Never declare an axis "exhausted" by feel; axes are combinatorial and a full sweep is not the job. A run that perfects one expression and never reaches the rest has failed the round it's in.

**This tool is lane-agnostic** — it runs the same whichever tool produced the set. The control set (the expression docs) is shared across all lanes, so a doc fix written back from any lane corrects every lane's next run. The one lane difference is the fault-line taxonomy:

- **Generation lane** (a compiled prompt from `08 briefs/` runs in a tool): doc / prompt / execution / axis-finding.
- **Direct-build lane** (the agent reads the docs and builds in-tool, live): doc / execution / axis-finding. **No prompt bucket exists — don't invent one.** "The instructions were unclear" is not a category: if the doc misled you, that's a doc problem, edit it; if you missed what it said, that's an execution problem, fix the build. A phantom prompt bucket is a blame sink that lets both off the hook.

"Build again" means whatever rebuilding is in your lane — recompile and rerun the prompt, or rebuild the variation directly.

**Reads:** the set's capture.md files · the expression's `doc.md` (the control set being tested) and `feedback.md` · the references this expression draws on (in `04 references/`) for the judging standard · `logic/controls - composition.md` / `controls - graphic.md` and the matching AD logic block, when classifying a finding against controls · prior rounds in the expression's `explorations/`
**Writes:** the round entry is **one markdown file in the expression's `explorations/` folder, named `round-[tool]-[date].md`** (second round same tool same day: `-2`). That is the primary home in every lane, always — no deciding, no stalling. If the set ran under a concept, copy the round file into `09 output/[concept]/` alongside the run record (same copy-back symmetry as the contract); if there is no concept run (expression studies, asset efforts), `explorations/` is the whole record and `09 output/` gets nothing. Also writes `doc.md` revisions when the fault line lands there — version-bumped, marked "(agent call, review)".

## The entry

1. **Tried / worked / failed** — across the set as a whole, not board by board. Name which open axes were cycled and what each cycle showed.
2. **Preserve** — what carries forward, specific enough the next build reuses it verbatim: values, faces, sizes, placements, recipes. Not "the type felt right."
3. **Avoid** — as positive future direction where possible ("crop at the ascenders only"), not only negatives. Negatives-as-kills stay the user's alone.
4. **Fault line** — every failure classified to the surface it lives on:
   - **Doc problem** — a *locked* control is wrong, missing, or misleading → revise `doc.md` now, version-bumped, "(agent call, review)". The standing rule holds: fix the control set, never the prompt.
   - **Prompt problem** — the doc was right but the translation layer mistranslated it → fix the translation for the next run; the doc stays untouched. *Lane note:* in a compiled-prompt lane the translation layer is the compiled prompt; in a direct build it's the stated build decisions; where no translation layer exists separately from the build, this category collapses away — fault-line on doc / execution / axis-finding only.
   - **Execution problem** — prompt was right, the build or tool missed it → fix it in the build. Code is steerable mid-flight: edit and re-verify, don't re-roll.
   - **Axis finding** — the failure sits on an *open* control and the variation did its job by ruling a direction out. That's evidence, not a fault: record it in the round, flag it as a negative *candidate* — it becomes a real negative only when the user kills it. Findings that land on not-yet-vetted controls feed that open vet as evidence; they classify nothing and lock nothing.
5. **Next move** — named and then *done*: another variation, a doc revision, a reference/media swap (pull different media from `03 media/` or different references from `04 references/`), an asset that must be made first, or — only when the doc genuinely cannot answer — a flagged question for the user that the run routes around, never waits on.

## What counts as clean

"Clean" is not self-graded — the same agent builds, reviews, and judges, so a vibe check inflates. A round may declare itself clean only with receipts:

1. **The comparison is named** — which kept exploration or ref image each board was judged side-by-side against, looking at composition, scale relationships, and how the type fills the frame — not "does it fit."
2. **Every line cites its source** — each preserve, avoid, and fault traces to a specific control in the doc, a ref, settled, or knowledge. A claim with no source is an opinion; it gets flagged as agent judgment or cut.
3. **Zero doc or prompt faults found** — execution fixes already made, axis findings recorded.

Missing receipts = not clean = the round says so plainly.

## Locked vs open, at the fault line

A fully-specified control set (photography-style production) makes every failure a doc/prompt/execution problem. An expression doc deliberately doesn't specify everything — locks are constraints, open controls are the variation space. So the fault line splits by lock status: failures against **locked** controls are doc/prompt/execution problems; outcomes on **open** controls are usually axis findings. Don't let a round harden an open control into a lock — that's the lock-hardening ban.

## The bar

Separate what the control set got wrong from what the translation or the tool got wrong, and put each fix where it lives. A next agent reading only the rounds should know what to reuse, what to skip, and why — without this conversation.
