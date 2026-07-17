# I — the survey route (technical · sign-sans · cool accent)

V1 · 2026-07-17 · Concept [the drive in](../../../07%20content%20concepts/the%20drive%20in.md), expression [07 property cartography](../../../02%20expressions/07%20property%20cartography/doc.md). Anatomy from the Lausanne reference: two-value cream split, route map bleeding across the gutter, destination on the content side. Axis moved: technical map treatment + the untested utilitarian sign-sans display pole (Overpass, highway-signage lineage). Palette accent from Direction 4a (Slate). Keepers honoured: N↑ mini-compass, hairline leaders, labels tied to real drive beats, no mono, no green, no boilerplate.

```
Design a desktop web section, 1440 x 820. A single static layout.

THE ONE IDEA
The drive is the arrival. A route runs from Austin across the whole frame and only reaches the cabin at the far right, and the map physically crosses the seam between the two halves so the page reads as one journey, not two panels.

THE SPLIT — two tints of cream, no line between them
Left half, x=0 to x=720: sand cream (#E6E0D6).
Right half, x=720 to x=1440: warm white (#F7F3F0).
They meet on a clean vertical butt edge at x=720 with nothing drawn on it. The value change is the only divider.

THE ROUTE — one continuous drawn line, thin coal (#111111), crossing the whole frame including the seam
A precise survey-style polyline, about 1.5px, starting at the far left around x=120 y=250 and travelling down and right through a few deliberate bends to a destination at about x=1040 y=560 on the warm-white side. Where it crosses x=720 it simply continues, unbroken. The line is drawn, not a photograph.

Waypoints along it, each a small solid coal triangle (about 9px) sitting on the line, with a label set just beside it in Overpass at 12px, mixed case, coal (#111111), and a 14px hairline leader (0.75px coal) from the triangle to the label:
- at x=120 y=250 — "Austin"
- at x=360 y=360 — "Hwy 290 west"
- at x=560 y=470 — "Johnson City, 9 min out"
- at x=730 y=520 — "the two-lane" (this one sits right on the seam, so its leader crosses onto the warm-white side)
- at x=900 y=545 — "the last gate"
The destination at x=1040 y=560 is a map pin (not a triangle), filled slate blue (#99A2AD), about 22px tall, with "your cabin" beside it in Overpass at 13px coal. This pin is the only colour on the drawn map.

THE COMPASS — top left of the map field, at about x=130 y=110
A minimal "N" in Overpass at 13px coal with a short up-arrow above it, 0.75px coal. Nothing else, no compass ring.

THE CONTENT — upper right, on the warm-white side, one hard left lane at x=800
Headline, first baseline y=210, Overpass at 46px, weight 700, line-height 50px, coal (#111111), mixed case, two lines with the leading tight:
  The last fifty minutes
  are the amenity.
Directly under the headline, at x=800 y=250, a small onward mark ">" in Overpass at 30px, slate blue (#99A2AD). It points down the page toward the route's end.

THE PHOTO INSET — on the warm-white side, x=800, top edge y=300
A plain square, 320 x 320px, object-fit cover, sitting directly on the warm white. No border, no shadow, no rounding.
https://raw.githubusercontent.com/ewiktor/caven-ranch-production/main/05%20graphics/assets/paper-run-01/12-drive-twolane-v1.png
(a two-lane blacktop winding through live oak and dry gold grass toward low hills, warm late light). Its left edge sits on the x=800 lane.

THE BODY — x=800, width 360px, first baseline y=680
Four to five lines in DM Sans at 13px, line-height 20px, coal (#111111), mixed case:
"Fifty minutes west of Austin the four-lane gives out to a two-lane that winds and narrows. The trees close in, the country drops away behind them, and the view stays hidden until you walk down the ramp at your cabin. Getting here is the first thing the place does for you."

THE FOOT — x=800, baseline y=780
"Caven Ranch · the drive in" in DM Sans at 12px, mixed case, slate blue-grey (#7C8896).

TYPE
Overpass for the wordmark voice: headline, waypoint labels, compass. DM Sans for body and foot. Mixed case everywhere.

COLOUR
Sand cream (#E6E0D6) left, warm white (#F7F3F0) right. All drawn line-work and type coal (#111111). Slate blue (#99A2AD) appears exactly twice: the destination pin and the onward ">". The photograph carries every other colour.

SPACING
The left map field is mostly empty on purpose, the emptiness is the distance of the drive. Content sits in one lane at x=800. Use 8 / 16 / 24 / 40 / 64 / 96 / 140.
```
