# I — the settle

Motion fork (a): a single coyote walks in and lies down. Corner-weighted: animal one corner, script-mixed type the opposite one. Color direction 3 (Sky Blue). Assets are live cutouts.

```
Build a website preloader for Caven Ranch as a self-contained HTML page. Viewport 1440 x 900px.

THE ONE IDEA
A coyote walks into an empty cream frame from the left, crosses it, and lies down in the bottom-right corner. The brand name sits jammed into the opposite corner, top-left. It plays once, then lifts away to reveal the home page. No spinner, no percentage, no UI. The animal arriving IS the loading.

GROUND
Solid Warm White #F7F3F0 filling the viewport. No texture, no paper, no gradient, no image.

ASSETS (both are live transparent PNGs, use these exact URLs)
- Walking coyote, faces right: https://raw.githubusercontent.com/ewiktor/caven-ranch-production/main/05%20graphics/assets/paper-run-02/coyotes/v2-coyote-walking-right-cutout.png
- Resting coyote, faces right: https://raw.githubusercontent.com/ewiktor/caven-ranch-production/main/05%20graphics/assets/paper-run-02/coyotes/v1-coyote-resting-right-cutout.png
Both are contemporary painterly illustrations on transparent backgrounds, already cut out. Do not add a drop shadow, outline, halo or containing box to either. Do not recolour, filter or duotone them.

TYPE BLOCK — top-left corner, x=96, y=96
- Line 1: the word "Caven" in Yellowtail, 60px, ink #111111.
- Line 2, 16px below line 1: "1,000 acres on the Pedernales, kept by one family for more than 150 years" in Piazzolla, weight 500, 22px, line-height 1.45, tracking -0.02em, ink #111111, max-width 380px, left-aligned ragged right.
- The script word and the serif line are one block: this is the script-mixed-into-type moment. Yellowtail is used for the word "Caven" and nothing else on the page.

MOTION TIMELINE (plays once)
- 0ms: empty Warm White frame. Type block present at opacity 0. No coyote visible.
- 0 to 240ms: type block fades opacity 0 to 1. It does not move, slide or letter-stagger. It is simply there.
- 240ms: the walking coyote enters from off-canvas left. Render it 380px tall, bottom edge (its paws) sitting on an invisible baseline at y=804. Start with its left edge at x=-420.
- 240 to 2100ms: translate the walking coyote right until its right edge reaches x=1344. Easing cubic-bezier(0.33, 0, 0.25, 1) so it arrives decelerating, like an animal choosing to stop.
- Gait, since this is a single still: superimpose a subtle loop on the walk. translateY oscillating between 0 and -5px, and rotation between -0.7deg and +0.7deg, one full cycle every 360ms, linear. The oscillation damps to zero over the final 300ms of the walk. This must read as weight, not as bouncing. If it looks like a hopping toy, halve the amplitude.
- 2100 to 2380ms: cross-fade the walking coyote to the resting coyote. Walking opacity 1 to 0, resting opacity 0 to 1, both ease-in-out, overlapping across the full 280ms. The resting coyote is 300px tall and its bottom edge sits on the SAME baseline y=804, with its right edge at x=1344. The two must overlap in position so the animal settles in place rather than jumping.
- 2380 to 2900ms: hold. Nothing moves. This pause is the whole point of the piece.
- 2900ms: exit. The entire preloader plane (ground, coyote, type together as one layer) translates up 40px and fades opacity 1 to 0 over 520ms, cubic-bezier(0.65, 0, 0.35, 1), revealing the home page beneath. Remove the layer from the document on completion.
- Total: roughly 3.4 seconds.

PLAYS ONCE
Guard with sessionStorage: on first land, run the sequence; on any later navigation within the session, skip it and render the page directly. Honour prefers-reduced-motion: if set, skip every transform, show the resting coyote and the type at full opacity for 600ms, then fade the plane out. No walk, no oscillation.

COLOUR — direction 3, Sky Blue. Total colours on screen: 4 maximum.
- Ground: Warm White #F7F3F0
- Ink: Coal Black #111111
- The coyote illustration is the ONE colour moment on the page.
- Sky Blue #CBDEE6 and Khaki #C5BA8C belong to this direction but are NOT to be placed as decoration. Leave them out entirely rather than sprinkling them. One accent moment, and the animal is it.

SPACING — use only these values: 4 / 8 / 16 / 24 / 40 / 64 / 96 / 128 / 160.

DO NOT
- Do not add a progress bar, percentage counter, spinner, dots, or any loading indicator. The walk is the indicator.
- Do not put any text behind, under or over the coyote. The type stays in its opposite corner.
- Do not add technical-line framing, crop marks, registration marks, corner brackets or rules of any kind.
- Do not add corner numbers, plate numbers or fake-technical data labels.
- Do not add a small accent rule or tick above or below the type.
- Do not use uppercase anywhere, at any size.
- Do not use em dashes in any copy.
- Do not use a dark ground. The ground is Warm White and nothing else.
- Do not use green in any form.
- Do not use aged paper, scrapbook or old-paper texture.
- Do not use Fraunces, Barlow Condensed, Archivo, Archivo Black, Space Grotesk, Instrument Serif, or any mono font.
- Do not colour the type with an accent. Type is ink.
- Do not letter-stagger, typewriter, blur-in or scale the type. It fades, that is all.
- Do not loop the sequence. It plays once.
```
