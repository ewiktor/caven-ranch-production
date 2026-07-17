**Run on demand** — when the user says "explore expression N" (or points at an expression and wants to see it). This is the **light path**: expression → 3 build prompts, in chat, done. It is NOT the full content-concept production pipeline. Use this by default for exploration; use the L2–L5 pipeline only when the user is producing a specific named content concept.

# Explore Expression

The user wants to *see* an expression in the brand's light. Your deliverable is **3 structurally-distinct compiled build prompts, written in the chat.** That's it. This is the simple, fast move — the one that actually works.

## Do NOT

- Do **not** route through content concepts, L2/L3/L4, or a brief. Exploration doesn't need a formal content concept — pick an obvious surface for the expression (a hero, a representative section) and explore the treatment on it.
- Do **not** ask "want me to go?" or "should I compile?" — just write the prompts. Producing them *is* the task.
- Do **not** build the design (no HTML, no rendering, no tool-driving).
- Do **not** detour into revising the expression doc. If you spot a doc problem, add it as **one flagged line after** the prompts — never instead of them.
- Do **not** write an essay of analysis first. A couple of sentences of grounding, then the prompts.

## Do

1. **Read the expression, fast:** `02 expressions/[NN name]/doc.md` (locked controls = hard constraints; focus/open controls = where you explore), `feedback.md` for the raw read, and its tagged references in `04 references/` (each carries the user's commentary — that's the taste you're exploring). Glance at kept explorations if any.
2. **Name 3 structurally-distinct directions** on the expression's open/focus axes (distinct on what's *open*; honor what's locked). One line each on what axis each direction moves. If you can't name three genuinely distinct ones, do two, better.
3. **Make the missing assets FIRST, then write the prompts.** List what the three directions need; check each has a working URL. Anything missing gets generated and hosted **before** the prompt is written; anything local-only gets published, then linked. **Never write "ASSET TO CREATE — generate this" into a prompt** — that hands the user back the work. If an asset genuinely cannot be made, cut the direction or redesign it around what exists; do not ship a prompt with a hole in it.
4. **Write each as a compiled build prompt** — full spec, self-contained: the locked controls as hard constraints, live asset links inline (from `03 media/`, `04 references/`, `05 graphics/`), exact values where settled, do-nots. Same completeness as `function/steps/L5a`.

   **Every prompt is standalone — this is not optional.** The user sends prompts to the build tool **one at a time**, so a prompt that references another is broken. Inside each code block: never write "Hero I", "the baseline", "same as above", "same content/copy/type/color as [other]", or any cross-reference. **Repeat every shared element in full** in each prompt — content, copy, palette, type system, the off-kilter degree, the spine rule, CDN links. Yes, the three will be highly repetitive; that's correct, because they travel separately. The *only* place variations get compared is the chat prose and the `I/II/III` labels around the code blocks (for you reading the set) — never inside the prompt text.
5. **Present in the chat, in this shape:**
   - **Grounding** — 1–2 sentences: what this expression is, what's locked, what varies across the three, any scenario dependency.
   - **I — [axis it moves]** · then the prompt in a code block, copy-ready.
   - **II — …** · code block.
   - **III — …** · code block.
   Save copies into `08 briefs/[expression]/prompts/` too, but the chat is the handoff.
6. **Stop.** The prompts are the deliverable. The user runs them (or an unattended run does). If a doc fix is worth making, flag it in one line — don't do it unless asked.

## The bar

Fast and direct. The user should be able to copy a prompt straight into their build tool. If you've written more prose than prompt, you've done it wrong.
