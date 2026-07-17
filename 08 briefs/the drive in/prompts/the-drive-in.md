# The drive in — field-sketch route across a cream split

V2 · 2026-07-17 · Concept [the drive in](../../../07%20content%20concepts/the%20drive%20in.md), expression [07 property cartography](../../../02%20expressions/07%20property%20cartography/doc.md). Anatomy from the Lausanne "Rapport de stage" reference: a two-tint cream split with no divider line, and a hand-drawn route map that bleeds across the seam so the spread reads as one journey. Fixes over V1: the map is a real hosted image, not SVG; all type is ink (no accent-coloured words); no paper texture; no killed faces. Map is monochrome ink so the photograph carries all colour. Type is Public Sans as a neutral placeholder (the display face is still unsettled), with Special Elite on the small map labels only, a confirmed keeper for the field-sketch map.

```
Design a desktop web section, 1440 x 820. A single static layout.

THE ONE IDEA
The drive is the arrival. A hand-drawn route wanders from Austin down to the cabin, and the map crosses the seam between the two cream halves so the page reads as one journey rather than two panels. The whole map is ink, so the only colour on the page is the one photograph.

THE SPLIT — two tints of cream, no line between them
Left half, x=0 to x=720: warm sand (#E7DECF).
Right half, x=720 to x=1440: off white (#ECE7E3).
They meet on a clean vertical butt edge at x=720. The change in value is the only divider. Draw no rule.

THE MAP — one hand-drawn ink image, placed large and crossing the seam
Place this image at x=20, y=30, width=1400, keeping its aspect ratio, so its winding route runs from the upper-left, down through the centre, to the map pin low on the right, and the river squiggles across the lower third. It is a transparent PNG of black ink, so the cream shows through it and it visibly crosses the x=720 seam as one continuous drawing. Its upper-right area is open, and the content sits in that opening.
https://raw.githubusercontent.com/ewiktor/caven-ranch-production/main/05%20graphics/assets/drive-maps/route-sketch.png

THE WAYPOINT LABELS — small text set beside the markers along the route, from start to pin
Each in Special Elite at 13px, mixed case, deep black (#000A0A). Place each one just beside its triangle or dot marker along the drawn route, following it from the upper-left start down to the pin:
- beside the first marker, upper-left: "Austin"
- next marker down: "290, going west"
- next: "Johnson City"
- around the middle bend: "the two-lane"
- near the pin: "the last gate"
- at the pin itself, lower right: "your cabin"
One playful aside, dropped by the route near a bend in the centre with no leader, Special Elite at 12px deep black: "turkeys, usually."

THE WORDMARK — top left corner
"Caven Ranch" at x=40, baseline y=52, Public Sans at 19px, weight 600, mixed case, deep black (#000A0A).

THE CONTENT — upper right, over the open part of the map, one hard left lane at x=820
Headline, first baseline y=180, Public Sans at 44px, weight 600, line-height 50px, deep black (#000A0A), mixed case, two lines with tight leading:
  The road does the
  unwinding for you.
Directly under it, at x=820, baseline y=224, a small onward mark ">" in Public Sans at 26px, deep black (#000A0A).

THE PHOTO INSET — on the content side, x=820, top edge y=270
A plain square, 300 x 300px, object-fit cover, sitting directly on the cream. No border, no shadow, no rounding.
https://raw.githubusercontent.com/ewiktor/caven-ranch-production/main/05%20graphics/assets/paper-run-01/12-drive-tunnel-v1.png
(a pale gravel lane running into a dark tunnel of Ashe juniper, the view ahead hidden by the trees). Its left edge sits on the x=820 lane.

THE BODY — x=820, width 360px, first baseline y=620
Four to five lines in Public Sans at 13px, weight 400, line-height 20px, deep black (#000A0A), mixed case:
"The four-lane gives out to a two-lane, and the two-lane gives out to gravel under a low run of juniper. You lose the view in the trees and you do not get it back until you are standing on the cabin ramp. By then you have already slowed all the way down."

THE FOOT — bottom right of the content side, x=820, baseline y=780
"Caven Ranch · the drive in" in Public Sans at 12px, weight 400, mixed case, deep black (#000A0A) at 70 percent.

TYPE
Public Sans for the wordmark, headline, body, and foot. Special Elite for the small map labels and the aside only, never large. Mixed case everywhere, no uppercase.

COLOUR
Warm sand (#E7DECF) left, off white (#ECE7E3) right. All map ink and all type deep black (#000A0A). There is no accent colour anywhere. The single photograph carries all the colour on the page.

SPACING
The map field is mostly empty, and the emptiness is the distance of the drive. The content sits in one lane at x=820, in the open upper-right of the map. Use 8 / 16 / 24 / 40 / 64 / 96 / 140.
```
