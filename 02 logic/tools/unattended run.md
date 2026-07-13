**Run on demand** — the standing order for autonomous production while the principal is away. The name is "unattended run," always — never "overnight run." Invoked with a queue (which expressions or shots, in what priority) and a return condition (a time, or "until the principal returns").

# Unattended Run

You are to run the production loop and NOT STOP until the queue is fully covered or the return condition hits. No check-ins, no waiting for approval mid-run. This doc exists because the common failure of autonomous runs is stopping — on an error, on an ambiguity, on a question only the principal can answer, or on the model's own instinct to wrap up and report. Every rule below is a route around a stop.

## Before starting

1. Read `00 brand.md` (mode, toolchain, variation budget, open questions), the queue you were given, and `01 settled/learnings.md`.
2. Confirm the queue is concrete: an ordered list of expressions (or shots, or concepts) with a per-item budget. If you were started without one, write one first from the current state and say so in the run summary — do not wander.

## The cycle, per queue item

One item at a time: build → self-review against the doc and refs (name the comparison) → capture per `09 output/_contract.md` → fix at the level the fault line names → rebuild if the round warrants it. Budget per item comes from `00 brand.md`; when it's spent, log and rotate to the next item. Second visits happen only after full coverage of the queue.

## Anti-stop rules

- **Errors:** retry once, then log it and move to the next queue item. Never let one failure stall the run.
- **Questions:** anything only the principal can answer gets flagged in the log and routed around — pick the least-committal path that keeps the item moving, mark the output "(pending [question])". Never wait.
- **Ambiguity in a doc:** resolve per the open-control fill order (refs → the principal's documented taste → settled + knowledge → your judgment, flagged). A doc gap is a flag for the log, not a reason to pause.
- **Missing asset or material:** note it on `05 graphics/to-make.md` or the log, produce the best version without it, move on.
- **Do not stop to summarize progress mid-run.** The summary happens once, at the end.
- **Do not "check in" because a result is good.** Capture it and continue.

## Token and effort discipline

- Terse self-critiques (a handful of bullets), one compact log entry per round, one generation per attempt, view each source once per item.
- Reusable findings (phrasings that work or fail, tool behaviors) go ONCE into `01 settled/learnings.md` — check it before every compile, never re-derive what's already logged.

## When the run ends

Write a short run summary at the top of the run's log: queue items completed, keepers, open flaws, flagged questions, and what needs the principal's eye first. Update the state line in `00 brand.md`. Then stop.
