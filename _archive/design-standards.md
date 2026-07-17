# Design standards — the craft gates (2026-07-16)

> **Caution (2026-07-17):** the "whitespace-first / restraint / one-idea-per-frame" framing below over-corrected in Round 2 — it produced flat text-on-white and lost boldness and format variety. Do NOT read this doc as "strip everything to white." The target is bold, layered, format-true, ranch-feeling work; these gates are craft floors, not a mandate for emptiness. This doc is pending a rework.

Written after the user called out the same basics failing round after round. These are hard gates, not guidelines. Every frame — agent or main — passes ALL of them before it is called done. Judge the SCREENSHOT at 2x, not the plan.

## Type system (chosen by letterform, not by name)

- **Display, structural: Familjen Grotesk** — 500–600, tracking −0.02em. Cool, contemporary, a little character. Do not default to 700+; heavy-and-huge is a failure mode here.
- **Display, editorial/warm: Piazzolla** — 400–600, tracking −0.02em. The user's one survivor. Warm serif for editorial moments, italics for a wry line.
- **Utility (nav, labels, metadata, body): Geist** — 400–600. Clean, invisible, contemporary. Never a hero.
- **Script accent — the word "Caven" only: Yellowtail.**
- **Tiny history detail only (≤14px): Special Elite.**
- **Hard rules:** type is near-black **ink only** — NEVER colored with a palette accent, NEVER the green. No uppercase anywhere. Curly quotes, **never em dashes**. Max 3 families per frame. Text over a photo may be near-white (that is a scrim contrast, not "coloring type").

## Type scale (px) — max 4 sizes per frame, all from here

`Display 88 / 72 / 56 / 44` · `Sub 32 / 24` · `Body 18 / 16` · `Label 13 / 11`

- **Whitespace is the priority, not scale.** The headline is confident but never oversized or shouty — a giant, bold hero filling the frame is a failure mode. Let the open space do the work; size down before you size up.
- There should be clear contrast between the display and the small text, but it comes from **restraint and air around the type**, not from cranking the hero as large and heavy as possible.
- Leading: display 1.0–1.1, body 1.5–1.6, unitless intent. Tracking: display −0.02em, body 0, tiny labels +0.01em (they are sentence case, not uppercase).
- Hierarchy from **space and position first**, then size, then weight last. Prefer medium weights over bold.

## Spacing scale (px) — use ONLY these

`4 / 8 / 16 / 24 / 40 / 64 / 96 / 128 / 160`

- **Within-group gap ≤ ⅓ of the between-group gap.** Make the ratio sharp (8 inside vs 64 between), never mushy (24 vs 40).
- The big void is **placed as composition**, first — never left over by a flex spacer.
- Margins generous and equal-feeling; content sits in from the edges on a grid.

## Color — roles, not sprinkles

Per frame: **1 ground + 1 ink (near-black) + 1 accent moment + max 2 derived neutrals** (tints of the ink or ground ONLY — never a new invented hue). **Total ≤ 5 colors on screen; count them in the screenshot.**

- **Accent budget: one moment per frame** (an image, or one colored element). Five weak accents = no accent.
- Type is never the accent.
- Palettes: `02 expressions/05 palette/color-directions.md`. Rotate directions across frames.

## Composition

- **Whitespace first.** Open, quiet, lots of air. The design should feel like it has room to breathe — closer to Ett Hem than to a dense Swiss poster. When in doubt, remove and open up, do not fill.
- **One idea per frame.** Write it before building: *"The idea is X. The eye goes A → B → C. The void lives at Z."* No line, no build.
- Left-aligned, ragged right, asymmetric, grid-disciplined. One clear focal point.
- Images: **contained with a 1px low-opacity outline OR full-bleed.** No drop shadows. No captions on images. Real Caven photos (`03 media/`), never placeholder.
- **No decorative chrome:** no plate/index/corner numbering, no fake-technical data labels, no bracket framing. (All killed repeatedly.)
- **No little anchor rules/ticks above text** — the short 2px accent line sitting over a label or caption is KILLED (user, 2026-07-17: "stop with these lines to anchor text, you try to make it cool but that sucks"). If an accent is needed, it must be a real compositional element, not a tick.

## The critique gate — a frame is NOT done until every item passes

1. Whitespace-led and calm — not dense, not shouty; the hero is confident, not oversized or over-bold.
2. ≤ 4 type sizes, every one from the scale; medium weight preferred over bold.
3. ≤ 5 colours counted in the screenshot; type is ink; exactly one accent moment.
4. Every gap is from the 8-scale; within:between ratio ≤ ⅓.
5. One idea; a focal point you can point to; a legible eye path.
6. No uppercase, no coloured type, no em dashes, no decorative numbering, no captions on images.
7. 2x optical pass: kerning, baseline alignment, no ascender/descender collisions, no orphan words.
