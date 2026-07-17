# III — the land parts

The user's second idea: two images together covering the frame, sliding apart to reveal the page. No character. Pure motion transition. Color direction 4b (Ice). Real Caven photography.

```
Build a website preloader for Caven Ranch as a self-contained HTML page. Viewport 1440 x 900px.

THE ONE IDEA
Two photographs of the ranch sit locked together, covering the whole screen, with the brand name across the seam. They part like a gate and slide off opposite edges, revealing the home page underneath. No character, no counter, no spinner. The land opens and you are let in.

STRUCTURE
- Two panels, each 720 x 900px, side by side with no gap, together covering the full 1440 x 900 viewport.
- LEFT panel: https://media.withdraper.com/1bc4729a-07cd-4572-98aa-8402c8bb5ea8/3347d2354c58a082fd1f6dc8581d9db4a0c78f41ba4bf4e64449be771cea3a0f (eroded limestone shelves descending into pale teal and cerulean water). object-fit: cover, filling the panel completely. No outline, no caption.
- RIGHT panel: https://media.withdraper.com/1bc4729a-07cd-4572-98aa-8402c8bb5ea8/26130ecc1ef9d187ae9857adf2f6a38d7924037d2c920a1093cf416a3714360a (a wooden structure under canopy-filtered dappled light). object-fit: cover, filling the panel completely. No outline, no caption.
- The seam between them is a hard edge. No divider line, no rule, no gap, no shadow.
- Beneath both panels: solid Bone #F6F6F2, which is what shows in the instant before the home page renders.

THE NAME — centred across the seam
- The word "Caven" in Yellowtail, 84px, near-white #F6F6F2, centred horizontally at x=720 and vertically at y=450, sitting ON the seam so that half the word lies over each photograph.
- This is the whole point of the centring: when the panels part, the word is cut in half and each half leaves with its own panel.
- Near-white over photography is scrim contrast, not coloured type. Add a very soft radial darkening behind the word, centred on it, 400px radius, Smoke Black #2F2E31 at 18 percent maximum opacity falling to 0, so the word stays legible without a box. No hard scrim rectangle, no band, no plate.
- Yellowtail is used for the word "Caven" and nothing else on the page.

MOTION TIMELINE (plays once)
- 0 to 200ms: both panels present and still, the word at opacity 0 ramping to 1. Nothing moves.
- 200 to 1100ms: hold. Both panels locked together, the word whole across the seam. This stillness is what makes the part land.
- 1100ms: THE PART. Each panel takes its half of the word with it (clip the word to each panel so it splits exactly at x=720).
  - Left panel translates to x=-720 (fully off the left edge).
  - Right panel translates to x=+720 (fully off the right edge).
  - Duration 900ms, easing cubic-bezier(0.76, 0, 0.24, 1) so they hesitate, then commit, then ease out. It must feel like weight being moved, not a UI slide.
  - The word does NOT fade during the part. It leaves with the panels, cut in half. Letting it fade is the boring version.
- 2000ms: the panels are gone and the home page is fully revealed beneath. Remove the preloader layer from the document.
- Total: roughly 2 seconds.

PLAYS ONCE
Guard with sessionStorage: on first land, run the sequence; on any later navigation within the session, skip it and render the page directly. Honour prefers-reduced-motion: if set, skip the slide entirely, hold both panels and the word for 500ms, then cross-fade the whole plane to opacity 0 over 400ms.

COLOUR — direction 4b, Ice. Total colours on screen: 4 maximum.
- Ground beneath the panels: Bone #F6F6F2
- Ink: Smoke Black #2F2E31 (the soft radial behind the word only)
- The word over the photographs: near-white #F6F6F2
- The two photographs are the colour. Ice Blue #DFE8F3 and Matt Sage #C7C4B0 belong to this direction but are NOT to be placed as decoration. Leave them out rather than sprinkling them.

SPACING — use only these values: 4 / 8 / 16 / 24 / 40 / 64 / 96 / 128 / 160.

DO NOT
- Do not add a progress bar, percentage counter, spinner or dots.
- Do not put a caption, credit or explainer line on either photograph.
- Do not add a divider line, rule or visible seam between the panels. They simply touch.
- Do not add technical-line framing, crop marks, registration marks or corner brackets.
- Do not add corner numbers, plate numbers or fake-technical data labels.
- Do not add a small accent rule or tick above or below the word.
- Do not use uppercase anywhere, at any size.
- Do not use em dashes in any copy.
- Do not use a dark ground, and do not darken the photographs overall. Only the soft radial behind the word.
- Do not use green in any form.
- Do not use aged paper, scrapbook or old-paper texture.
- Do not use Fraunces, Barlow Condensed, Archivo, Archivo Black, Space Grotesk, Instrument Serif, or any mono font.
- Do not fade the word out during the part. It splits and travels with the panels.
- Do not slide the panels vertically, diagonally, or with a rotation. Horizontal only.
- Do not loop the sequence. It plays once.
```
