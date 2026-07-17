# I — the illustration cuts the seam

Home page. Structural axis: a hard vertical split, and a single illustration breaking across it so the seam stops reading as a divider. Color direction 2 (Rust).

```
Build a desktop home page for Caven Ranch. Frame: 1440 x 1800px.

THE ONE IDEA
A hard vertical split down the page, and a single large illustration straddling it — the illustration is drawn across the seam so the two halves read as one space with something standing in front of them. The seam must be visibly interrupted. If the illustration sits neatly inside either half, the design has failed.

STRUCTURE
- Vertical split at 58% / 42%. Left panel: ground Off White #ECE7E3. Right panel: a full-bleed photograph, edge to edge, running the full height of the panel.
- Right panel photograph: https://media.withdraper.com/1bc4729a-07cd-4572-98aa-8402c8bb5ea8/3347d2354c58a082fd1f6dc8581d9db4a0c78f41ba4bf4e64449be771cea3a0f (eroded limestone shelves descending into pale teal and cerulean water). Fill the panel, crop as needed, no outline, no caption.
- The illustration (spec below) is placed so its horizontal centre sits ON the 58% seam: roughly 62% of its body over the left cream panel, 38% over the photograph. It overlaps the photo directly, no white gap, no halo, no drop shadow. Bottom of the illustration sits at y=1500. It is large: 620px tall.
- Headline sits on the left panel, top-left area, starting x=96, baseline y=420. The illustration overlaps the last line of the headline by roughly 40px vertically — the type goes BEHIND the illustration. Do not move the type to avoid the collision; the collision is the design.
- Body paragraph on the left panel, x=96, top y=1580, max-width 440px.
- Small wordmark "caven ranch" top-left, x=96, y=64, Geist 400, 13px.
- Nothing else. No nav links, no button, no scroll indicator.

ILLUSTRATION — ASSET TO CREATE (no CDN link exists yet; generate it)
A single coyote, standing in profile, facing left, contemporary editorial illustration. Painterly colour-field technique: forms built from confident directional brushstrokes and flat contrasting colour fields rather than outlines. Muted warm palette drawn from Rust #813517 and Walnut #432F2E against a warm neutral body. No hard vector edges. No black keyline. Transparent background, cleanly cut out. It is an actual coyote: no clothing, no hat, no bandana, no human accessories, no anthropomorphising. Deadpan and still, not cute, not snarling. Contemporary illustration — NOT pen-and-ink, NOT charcoal, NOT engraving, NOT woodblock, NOT linocut, NOT risograph, NOT scratchy hand-drawn linework.
(There are existing coyote PNGs at 05 graphics/assets/paper-run-02/coyotes/ — v1-coyote-resting.png and v2-coyote-walking.png — but they are local files with no CDN link, so they cannot be referenced by URL. Either upload one to the CDN and use it, or generate fresh to the spec above.)

TYPE
- Display: Piazzolla, weight 500, tracking -0.02em, line-height 1.05.
- Utility/body: Geist, weight 400.
- Headline: Piazzolla 72px, three lines, left-aligned ragged right.
- Body: Geist 18px, line-height 1.55.
- Wordmark: Geist 13px.
- Type is near-black ink #000A0A only. Body text may be #432F2E. Never colour type with an accent. Never green.

COPY (use exactly, no changes)
Headline: "Most of this land will never be built on, and that is the point."
Body: "Caven Ranch is 1,000 acres on the Pedernales River, outside Johnson City, held by the same family for more than 150 years and largely kept in conservation. A small number of cabins are being drawn into one corner of it now, set far enough apart that you will rarely see another one."
Wordmark: "caven ranch"

COLOUR — direction 2, Rust. Total colours on screen: 5 maximum.
- Ground: Off White #ECE7E3
- Ink: Deep Black #000A0A
- Accents (in the illustration only): Rust #813517, Walnut #432F2E
- The photograph is the one image moment; the illustration is the one accent moment.

SPACING — use only these values: 4 / 8 / 16 / 24 / 40 / 64 / 96 / 128 / 160.
Within-group gaps must be at most one third of between-group gaps. Make the ratio sharp: 8 inside a group, 64 between groups.

DO NOT
- Do not leave a white gap, halo, outline or shadow between the illustration and the photograph. They touch.
- Do not use uppercase anywhere, in any element, at any size.
- Do not use em dashes in any copy.
- Do not put a caption or explainer line under the image.
- Do not add decorative chrome: no corner numbers, no plate numbers, no fake-technical data labels, no bracket framing, no small accent rules or ticks above labels.
- Do not use green in any form.
- Do not use aged paper, scrapbook or old-paper texture as the ground.
- Do not state or imply that the retreat is open, bookable, or operating. It is in development. No prices, no booking button, no "reserve".
- Do not use Fraunces, Space Grotesk, Archivo Black, Instrument Serif, Geist as a display face, or any mono font.
- Do not centre the layout.
```
