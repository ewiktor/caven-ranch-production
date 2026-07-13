# Strategy Overview Writer

**Run this OUTSIDE the repo.** Copy this whole prompt into a separate chat, paste the brand's strategy materials under it, and it writes the strategy overview. Take the output and save it into the brand repo at `input/01 brief (strategy).md`. The repo never compiles this itself — it arrives already written.

This is self-contained on purpose: it carries its own output shape so it works in a chat that can't see the repo.

---

You are writing the **strategy overview** for a brand — a single, tight digest that everything downstream reads instead of the full strategy set. I will give you the brand's strategy materials (some mix of customer research, competitive set, product offering, brand strategy, communications, content strategy, and creative — whatever exists). Distill them into the overview below.

## What this is

The one working digest of the brand's strategy. Downstream production reads this, not the full source docs. It must stand on its own: someone who never sees the source material should understand who the brand is, who it's for, what it's saying, and why.

## Rules

- **Narrative only.** No asset lists, no media/reference manifests, no file links. Those live elsewhere and change constantly. This is the thinking, not the inventory.
- **Distill, don't copy.** Pull the load-bearing points from across the source docs. Drop the rest. If the source is thin somewhere, say so plainly rather than padding.
- **Current vs. planned, kept separate.** State what the brand is now and what's planned as distinctly different things. Nothing planned may be written as if it already exists.
- **Facts only.** Don't invent numbers, claims, or positioning the source doesn't support.
- **Plain and grounded.** Write like a competent professional briefing a colleague. No hype, no marketing rhetoric, no clever phrasing. Say the point directly. No em dashes.

## Output — fill every section, in this order

```
# Strategy overview — [brand name]

**Compiled:** [date]

## Task
[What is being made and why, the hard constraints, the timeline. The frame everything serves.]

## Who this is for
[The audience segments read as people: what they want, what they're deciding between, what they need. From customer research.]

## Who the brand is (right now)
[The honest current state — what the brand is and isn't yet. From brand strategy + product offering.]

## What it's offering (at this stage)
[What this specific work is actually selling or delivering, in priority order. From product offering + content strategy.]

## What it's messaging
[The primary message in one line, then the supporting messages. From communications.]

## Why this approach
[The core constraint or tension and how the strategy resolves it; the operating principle. From brand strategy + communications.]

## What it needs to do
[The concrete jobs this work has to accomplish, ordered. From content strategy.]

## Desired outcome
[What a person understands, feels, or does after encountering it. The success condition.]
```

If a section has no support in the material provided, write "Not covered in the source material" under it rather than inventing content — that tells the brand team where the strategy has a gap.
