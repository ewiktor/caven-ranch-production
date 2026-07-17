**Reads:** the assembled brief in 08 briefs/[concept]/ · 03 media/ and 05 graphics/ for CDN links · logic/ad logic - composition.md (execution vocabulary) · L5a for the format
**Writes:** 2–3 compiled build prompts into 08 briefs/[concept]/prompts/. **This step's output is the prompt. It does not build.** The compiled prompts are the loop's deliverable — building the design from them happens separately (see `function/tools/unattended run.md`, or the user runs them).

# Applied Direction

The pull-it-together step. After the editorial outline, visual direction, and copy exist and have been checked, this step compiles everything into a build prompt that a production tool executes with as little left on its plate as possible — the goal is that whatever builds it is focused on nothing but building. **This step produces the prompt and stops; it is not where the design gets built.**

What goes into the compiled prompt:

- The structure and phases of the piece (from the outline and direction)
- The specific media and graphics as CDN links, already selected
- The copy, already written and checked
- The expression directives: the controls, keywords, terms, and phrases being controlled for — including motion and interaction behavior, spelled out in the execution vocabulary (see logic/ad logic - composition.md)
- Exact styling where it is settled (type, color, spacing)

See `L5a applied direction - prmpt example.md` for the reference format — a worked example that specifies everything down to pixel values, easing, and breakpoints.

The brief stayed wide on purpose; the compile is where narrowing happens. Each of the 2–3 compiled prompts is a different deliberate narrowing of the same brief — a different combination of media picks, expression directions, and open-control values — so the variation set can be judged as a set.

Open question, standing: how detailed the directive should be. The prmpt example makes every decision in advance and leaves the tool nothing but transcription. Staying looser and leaving some things in the tools' hands may serve some rounds better — the right level of detail gets figured out per brand through test cases, and findings go to `01 settled/learnings.md`.

## Presenting the prompts — write them in the chat, not just to files

The handoff is the chat. Save the prompts to `08 briefs/[concept]/prompts/` AND lay them out in the chat, in this shape, so the user can read and copy them directly:

1. **Grounding** (one short paragraph, first) — what expression this is exploring and through which content concept, what's locked, what varies across the set, and any scenario dependency (e.g. "III needs the redrawn mark from expression 25"). This comes straight from the expression doc; it's why the set hangs together.
2. **Each variation, labeled** — `I — [short title naming the one axis it moves]`, `II — …`, `III — …`. One line on what makes this one distinct.
3. **The prompt itself in a code block**, copy-ready and self-contained: color hex, exact copy, media CDN links inline, do-nots. Nothing the user has to go look up.

Keep the prose around each prompt minimal — the grounding line and the axis label. The prompt is the deliverable; don't bury it in explanation. Then stop: these prompts are what the user runs (or the unattended run runs). Do not build them yourself.

**Assets before prompts — never hand the user homework.** Before writing a single prompt, list what assets it needs and check each one has a working URL. Anything missing gets **made first**: generate the illustration/texture/mark, host it, and put the live link in the prompt. Anything that exists only as a local file gets **published first**, then linked. Writing "ASSET TO CREATE — generate this to the spec below" into a prompt is a failure, not a caveat — it hands the user back the work the compile was supposed to absorb. The compiled prompt is the handoff; a slot holding a description instead of a link means the compile is not done.

**Every prompt is standalone — this is not optional.** The user sends prompts to the build tool **one at a time**, so a prompt that references another is broken when it arrives alone. Inside each code block: never write "variation I", "the baseline", "same as above", "same content/copy/type/color as [other]", or any cross-reference. **Repeat every shared element in full** in each prompt — content, copy, palette, type system, the off-kilter degree, structural rules, CDN links. The three will be highly repetitive; that's correct, because they travel separately. Comparison between variations lives *only* in the chat prose and the `I/II/III` labels around the code blocks — never inside the prompt text.
