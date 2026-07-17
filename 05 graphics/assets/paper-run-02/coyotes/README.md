# Coyote assets — cutouts

The `-cutout.png` files are transparent PNGs derived from the run-02 painted
coyotes, made 2026-07-17 for the preloader (expression 08).

The originals were painted onto baked cream grounds, so they could not sit on a
coloured field. Keyed out on saturation (S < 24) with border-connectivity: a
plain flood fill could not reach the contact shadow, and a global colour key ate
the pale chest fur. The resting coyote keeps a faint contact shadow — it reads as
a shadow on the off-white grounds all five colour directions use.

| file | faces | use |
|---|---|---|
| `v2-coyote-walking-cutout.png` | left | walks right-to-left |
| `v1-coyote-resting-flip-cutout.png` | left | settled, matches the left walk |
| `v2-coyote-walking-right-cutout.png` | right | walks left-to-right |
| `v1-coyote-resting-right-cutout.png` | right | settled, matches the right walk |

Walk and settle in the same pair share a facing, so a walk-in and settle reads as
one continuous move. Raw URL pattern (spaces are `%20`):

https://raw.githubusercontent.com/ewiktor/caven-ranch-production/main/05%20graphics/assets/paper-run-02/coyotes/<file>

No cutout exists for `v3-coyote-pack.png`: the gaps between the legs are enclosed
background that border-connectivity cannot reach, so it needs manual masking or a
regenerated transparent original.
