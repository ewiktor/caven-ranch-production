# III — the map behind, the stack in front

Home page. Structural axis: three layers of depth on one plane — a faded topo map filling the whole page, an image stack overlapping itself in front of it, and an illustration sitting on top of the headline. Color direction 1 (Soft Blue).

```
Build a desktop home page for Caven Ranch. Frame: 1440 x 1800px.

THE ONE IDEA
Three depths on a single plane. Back: the property's own topographic map, faded almost to nothing, filling the entire page as a field rather than a picture. Middle: two photographs overlapping each other at the corners, not aligned to a grid. Front: an illustration sitting directly on top of the headline, partially covering the words. Depth comes from things overlapping, not from spacing them apart.

STRUCTURE
- LAYER 1, the field: the topographic map, scaled to cover the full 1440 x 1800 frame, faded to 12 percent opacity over the Off White #ECE7E3 ground. Desaturate it fully first, then tint the remaining linework toward Sage Gray #919D9D. It should read as a texture you half-notice, never as a map you are meant to read. Bleed it off all four edges. Use: https://media.withdraper.com/1bc4729a-07cd-4572-98aa-8402c8bb5ea8/8255ba92b312e5d921b0b16d08092e169b96e66c8bfbb429671e7ce848b5f0ca
- LAYER 2, the stack: two photographs, overlapping at a corner by roughly 90px, neither aligned to the other's edges.
  - Photo A, the larger, 620 x 780px, at x=700, y=640: https://media.withdraper.com/1bc4729a-07cd-4572-98aa-8402c8bb5ea8/1284ded75e308a8aa2cab3ab90dc5e431a1f8d90e1d96b0c6b1332c40c0b1115 (vertical wide shot, small human figures mid-ground on an S-curving river, limestone shelves).
  - Photo B, the smaller, 380 x 300px, at x=1010, y=1330, so its top-left corner lands over Photo A's bottom-right corner: https://media.withdraper.com/1bc4729a-07cd-4572-98aa-8402c8bb5ea8/26130ecc1ef9d187ae9857adf2f6a38d7924037d2c920a1093cf416a3714360a (a wooden structure under canopy-filtered dappled light).
  - Photo B sits IN FRONT of Photo A. Both are contained with a 1px #919D9D outline at 30 percent opacity. No drop shadows. No captions.
- LAYER 3, the front: the headline, left-aligned, x=96, first baseline y=560, max-width 520px, three lines. The illustration (spec below) is placed at x=380, y=380, 300px tall, sitting ON TOP of the headline and covering roughly the last 60px of the second line. The words behind it stay unmoved and partially hidden. Do not reflow the headline to make room. The covering is the design.
- Body paragraph, x=96, y=980, max-width 420px, Geist 18px.
- Small wordmark "caven ranch" top-left, x=96, y=64, Geist 400, 13px.
- The bottom-left quadrant below the body stays completely empty. That void is placed on purpose, not left over.

ILLUSTRATION — ASSET TO CREATE (no CDN link exists yet; generate it)
A live oak branch with leaves, or a stand of little bluestem grass, rendered as a contemporary editorial illustration. Painterly colour-field technique: forms built from confident directional brushstrokes and flat contrasting colour fields rather than outlines. Muted palette of Sage Gray #919D9D and Soft Blue #D6E0E2 against warm neutral. No hard vector edges, no black keyline. Transparent background, cleanly cut out, soft irregular edges rather than a hard rectangle. Contemporary illustration — NOT pen-and-ink, NOT charcoal, NOT engraving, NOT woodblock, NOT linocut, NOT risograph, NOT scratchy hand-drawn linework, NOT watercolour wash, NOT a botanical specimen plate or pressed-flower scan.
(A generated little bluestem PNG exists at 05 graphics/assets/paper-run-02/little-bluestem.png, but it is a local file with no CDN link and cannot be referenced by URL. Either upload it to the CDN and use it, or generate fresh to the spec above.)

TYPE
- Display: Piazzolla, weight 500, tracking -0.02em, line-height 1.05.
- Utility/body: Geist, weight 400.
- Headline: Piazzolla 72px, three lines, left-aligned ragged right.
- Body: Geist 18px, line-height 1.55.
- Wordmark: Geist 13px.
- Type is near-black ink #000A0A only. Never colour type with an accent. Never green.

COPY (use exactly, no changes)
Headline: "The gate is a long way from the highway, and the quiet starts well before you reach it."
Body: "Caven Ranch is 1,000 acres of Texas Hill Country on the Pedernales River, held by the same family for more than 150 years and largely kept in conservation. What is being built here is small on purpose: a handful of cabins, set far enough apart that the land stays the reason you came."
Wordmark: "caven ranch"

COLOUR — direction 1, Soft Blue. Total colours on screen: 5 maximum.
- Ground: Off White #ECE7E3
- Ink: Deep Black #000A0A
- Accents: Soft Blue #D6E0E2, Sage Gray #919D9D
- The faded map is a near-neutral field and does not count as the accent moment. The illustration is the one accent moment.

SPACING — use only these values: 4 / 8 / 16 / 24 / 40 / 64 / 96 / 128 / 160.
Within-group gaps must be at most one third of between-group gaps. Make the ratio sharp: 8 inside a group, 64 between groups.

DO NOT
- Do not align the two photographs to each other or to a shared grid. They overlap off-axis on purpose.
- Do not move, reflow or shrink the headline to avoid the illustration covering it.
- Do not let the faded map read as a legible map. No contour labels, no map pins, no location tags, no region tags, no legend.
- Do not use uppercase anywhere, in any element, at any size.
- Do not use em dashes in any copy.
- Do not put a caption or explainer line under either image.
- Do not add decorative chrome: no corner numbers, no plate numbers, no fake-technical data labels, no bracket framing, no small accent rules or ticks above labels.
- Do not use green in any form.
- Do not use aged paper, scrapbook or old-paper texture as the ground.
- Do not scatter the photographs into a moodboard or a naturalist's-desk collage. Two photographs, one overlap, nothing more.
- Do not state or imply that the retreat is open, bookable, or operating. It is in development. No prices, no booking button, no "reserve".
- Do not use Fraunces, Space Grotesk, Archivo Black, Instrument Serif, Geist as a display face, or any mono font.
```
