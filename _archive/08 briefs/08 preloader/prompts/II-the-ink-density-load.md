# II — the ink-density load

Round 2's "great idea": the animal darkens as the page loads. The load is a state change in the illustration itself, not a bar. Full-screen. Color direction 2 (Rust/Walnut). Assets are live cutouts.

```
Build a website preloader for Caven Ranch as a self-contained HTML page. Viewport 1440 x 900px.

THE ONE IDEA
The coyote loads like ink soaking into paper. It starts as a barely-there walnut ghost, walks slowly in from the right, and darkens as the page loads until, at 100 percent, the ink resolves into the full painted animal and it lies down. The loading progress IS the density of the illustration. There is no bar, only a small number in the corner.

GROUND
Solid Off White #ECE7E3 filling the viewport. No texture, no paper, no gradient, no image.

ASSETS (both are live transparent PNGs, use these exact URLs)
- Walking coyote, faces left: https://raw.githubusercontent.com/ewiktor/caven-ranch-production/main/05%20graphics/assets/paper-run-02/coyotes/v2-coyote-walking-cutout.png
- Resting coyote, faces left: https://raw.githubusercontent.com/ewiktor/caven-ranch-production/main/05%20graphics/assets/paper-run-02/coyotes/v1-coyote-resting-flip-cutout.png
Both are contemporary painterly illustrations on transparent backgrounds, already cut out. Do not add a drop shadow, outline, halo or containing box.

THE INK-DENSITY MECHANIC — build it in two stacked layers, pixel-aligned
- Layer A, the ink: a div filled with solid Walnut #432F2E, masked by the walking coyote PNG. Use mask-image (and -webkit-mask-image) with the walking coyote URL, mask-size: contain, mask-repeat: no-repeat, mask-position: center. This gives a flat walnut silhouette of the animal.
- Layer B, the painting: an img of the same walking coyote PNG, occupying the exact same box as layer A, same size, same position.
- Load 0 percent: layer A opacity 0.10, layer B opacity 0. A faint ghost.
- Load 0 to 70 percent: layer A opacity ramps 0.10 to 0.85, linear against actual load progress. The animal steadily gains ink. Layer B stays at 0.
- Load 70 to 100 percent: layer A fades 0.85 to 0 while layer B fades 0 to 1, cross-faded across the same window. The flat ink resolves into the painted illustration.
- Drive this off real load progress if available; otherwise simulate a 2600ms ramp with slight irregularity (it should not feel perfectly linear, real loading never is).

MOTION TIMELINE (plays once)
- The coyote is rendered 400px tall, bottom edge (its paws) on an invisible baseline at y=790.
- 0ms: coyote begins with its right edge at x=1740 (off-canvas right), walking left.
- 0 to 2600ms, tracking load 0 to 100 percent: translate left until its left edge reaches x=440, so the animal ends slightly left of centre, not dead centre. Easing cubic-bezier(0.4, 0, 0.3, 1).
- Gait, since this is a single still: translateY oscillating 0 to -5px and rotation -0.7deg to +0.7deg, one cycle per 380ms, linear, damping to zero across the final 400ms. Weight, not bounce.
- At 100 percent (roughly 2600ms): cross-fade the walking coyote to the resting coyote over 280ms, ease-in-out. The resting coyote is 320px tall, bottom edge on the SAME baseline y=790, left edge at x=440. It settles in place and does not jump.
- 2880 to 3400ms: hold, fully resolved and still.
- 3400ms: exit. The entire preloader plane translates up 40px and fades opacity 1 to 0 over 520ms, cubic-bezier(0.65, 0, 0.35, 1), revealing the home page beneath. Remove the layer on completion.

THE COUNTER — bottom-right corner, x anchored 96 from the right edge, y anchored 96 from the bottom
- The number counts 0 to 100 in Geist, weight 400, 13px, ink #000A0A, no percent sign, no label, no leading zeros.
- It is the only UI element on the page. It sits in the corner and does nothing else: no box, no bar, no rule, no tick, no bracket.
- It fades out over the first 200ms of the exit.

COLOUR — direction 2, Rust. Total colours on screen: 4 maximum.
- Ground: Off White #ECE7E3
- Ink: Deep Black #000A0A (the counter only)
- The ink-density layer: Walnut #432F2E
- The resolved coyote illustration is the one colour moment.
- Rust #813517 belongs to this direction but is NOT to be placed as decoration. Leave it out rather than sprinkling it.

SPACING — use only these values: 4 / 8 / 16 / 24 / 40 / 64 / 96 / 128 / 160.

PLAYS ONCE
Guard with sessionStorage: on first land, run the sequence; on any later navigation within the session, skip it. Honour prefers-reduced-motion: if set, skip the walk and the oscillation, show the resting coyote fully resolved with the counter at 100 for 600ms, then fade the plane out.

DO NOT
- Do not add a progress bar, track, ring, spinner or dots. The counter and the ink density carry it.
- Do not put any text behind, under or over the coyote. The counter stays in its corner.
- Do not add technical-line framing, crop marks, registration marks, corner brackets or rules of any kind.
- Do not add corner numbers, plate numbers or fake-technical data labels. The load counter is not a plate number and must not be styled as one.
- Do not add a small accent rule or tick above or below the counter.
- Do not use uppercase anywhere, at any size.
- Do not use em dashes in any copy.
- Do not use a dark ground. The ground is Off White and nothing else.
- Do not use green in any form.
- Do not use aged paper, scrapbook or old-paper texture, and do not add a halftone or dither overlay to the illustration.
- Do not use Fraunces, Barlow Condensed, Archivo, Archivo Black, Space Grotesk, Instrument Serif, or any mono font. The counter is Geist.
- Do not colour the counter with an accent. It is ink.
- Do not loop the sequence. It plays once.
```
