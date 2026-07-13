**Run on demand** — per expression, after the board pass has named it and its folder holds the raw material. This is the bridge from reference-plus-commentary to a documented expression.

# Expression Doc Writer

Write one expression's `doc.md` — the shape in `02 expressions/_expression-template/doc.md` — from the raw material in its folder.

**Reads:** `02 expressions/[name]/feedback.md` (the user's raw commentary — the primary source) · the references tagged to this expression in `04 references/` (each carries its description + the user's commentary) · `explorations/` and any capture.md files in it · `logic/controls - composition.md` or `controls - graphic.md` (which controls exist for this type) · `logic/ad logic - composition.md` or `ad logic - graphics.md` (the option vocabulary)
**Writes:** `02 expressions/[name]/doc.md`. The user QAs every doc before it's treated as real.

## How

1. **Type it.** Composition or graphic, and the subtype (web section, texture, lettering, etc.) — the controls doc for that type is your control list.
2. **Distill "what it is" and "what the user likes"** from the feedback, in their terms. Keep the tensions they name ("they clash, but that's good tension") — those carry more direction than the likes.
3. **Lock only what the commentary covers.** Go control by control through the type's control list. Where the user's commentary (or the reference's own markdown) actually speaks to a control, write it up as keywords, terms, and phrases — off the reference visual plus their words, in the AD-logic vocabulary where it fits. Expect a handful locked out of the full set, not all of them. **A lock is never absolute or one-directional unless the user's words were** — the keyword format strips hedges silently, so "push it further" must not become "never closer" (that exact hardening shipped in the test round and had to be torn out). Never lock this expression to another expression's state or to brand-wide consistency; real dependence is a Scenario (template section), not a lock.
4. **Everything else is leave-open.** Do not fill uncovered controls from taste, from the reference's look, or from what would make the doc feel complete — an uncovered control is variation space, and cycling it is where variations come from. Name specific directions worth cycling only if the commentary hinted at them.
5. **Negatives and open questions.** What the user ruled out, what died nearby, and what the expression is waiting on — flagged, not decided. Negatives are the user's kills only — never inferred prohibitions, never a counter-negative patching a wrong positive (delete the positive).
6. **Write-back.** When the user corrects direction live in any session, the correction supersedes the doc the moment they say it — and the doc gets amended the same session, version line bumped with what changed. Corrections that die in chat threads get re-made wrong by the next agent.

## The bar

A total stranger — a great creative or an AI — could pick up this folder and continue the expression without this conversation. If the feedback is too thin to lock a control honestly, say so in the doc and leave it open rather than padding. Flag ambiguity to the user instead of resolving it.
