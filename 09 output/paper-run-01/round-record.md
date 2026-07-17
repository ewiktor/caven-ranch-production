# Paper run 01 — round record (2026-07-16)

**What this was:** the first exploration build. Every one of the 21 expressions taken into Paper as **3 structurally-distinct, content-concept-grounded variations** — 63 artboards. Fanned out one agent per expression (Workflow, general-purpose), each running the method's critique→revise gate on its own frames. Imagery generated with Nano Banana Pro (98 assets), anti-AI-look prompting (physical-medium description) throughout.

**File:** Paper — "caven ranch" / page "fable make me proud here" (`01KXN489CQ7SD69SBKZAWWHMQ5`). Generated assets mirrored to `05 graphics/assets/paper-run-01/` (index: `05 graphics/generated-assets-run-01.md`) and live in `09 output/paper-run-01/img/`.

## Coverage — 21 × 3

All built. Formats routed to concept, not defaulted to web: web 1440 heroes/sections, social 4:5 posts, 2:3 posters, wide horizontal-scroll strips (3200/2800px), and multi-frame carousel systems (4600px+). Each expression's three variations move on **different open axes** — type system, compositional logic, palette world, image-vs-cutout, scale — not swapped attributes.

- **Type is treated as open** (the unresolved serif-vs-utilitarian tension): across the set, high-contrast editorial serif (Fraunces / Playfair / Libre Caslon / EB Garamond), blocky utilitarian sans (Archivo Black / Oswald / Anton / Space Grotesk), and typewriter/mono (Special Elite / Courier Prime / IBM Plex Mono) all carry different variations. `21 typography` builds the tension explicitly as three worlds on one content.
- **Palette is treated as the A/B scenario** — earth (terracotta #8B391D / sage / limestone) and river (teal / slate / limestone) both run; `05 palette` builds them as deliberately-parallel worlds so they read side by side.

## Craft / honesty audit (spot-checked 10 artboards across the range)

- **Anti-AI-look held.** Generated illustration reads as brushed ink / linocut / riso / clay-and-stone model, not AI render. Verified on 02-I riverbed ink hero, 07-III clay diorama, 06-I script wordmark, 13-I desk archive, 20-III white-ink coyote.
- **Facts trace to `06 knowledge/`.** Verified e.g. 18-III "Alonzo Robinson 1852–1936, Texas state surveyor, bought the land for very little" — exact match to family-history.md. 1,000 acres / Pedernales / 150 years / 50 min from Austin / Guadalupe bass (Micropterus treculii) / Miller Creek confluence all check.
- **No booking claims.** "Becoming a small, design-led retreat," "a retreat, in development," "PROPERTY MAP — CONCEPT IN DEVELOPMENT," "SAFARI TENT — PLANNED" — planned things are labeled planned.
- **The animal is never labeled or announced.** 20-III (character sightings) and 14-I (animal lurking on the far bank) carry it with zero explanation. Species split per the open scenario: coyote in most, GSP in a few.
- **Kills honored:** no mint green, no bright poppy red, #8B391D as the terracotta, no Western kitsch (no hats/bandanas/rope type/wagon wheels).

## What was rejected / re-rolled

- 01-I trail-cam v1 rejected (baked-in timestamp + camera visible in frame) → v2 clean.
- 02 riverbed & riso: multiply-blend seams replaced with true alpha-feathered edges; riso title rebuilt as offset two-layer print (8 revise cycles).
- Numerous prompt re-rolls where the first generation was too detailed or too thin/generic (the user's two named failure poles).

## Fault lines / flags for the principal

1. **Type direction is genuinely unresolved and now visible** — `21 typography` I/II/III and the type spread across every expression give you a real serif-vs-sans-vs-mono decision to make. This is the biggest open call.
2. **Species (coyote vs. GSP)** — both are on the board unlabeled; pick one or keep both as contexts.
3. **Fact discrepancy still standing:** the Lost Hunter (Mexico horse story) — `06 knowledge/` says **Ralph, ~1902**; the older Notion doc said Alonzo/1887. 02-II and 19-I built it as Ralph 1902 per knowledge. Confirm or correct.
4. **`05 palette` A/B** — the two worlds are built to be compared; the A-vs-B call is yours.
5. **Centered vs. asymmetric** — a few frames (01-III encyclopedia plate) use centered composition; still an open question in settled.md.

## Run mechanics (learnings — see `01 settled/learnings.md`)

- Workflow spawns 21 agents into one Paper file in parallel safely by passing `fileId` explicitly on every call and never calling `open_file` (which would hijack other agents' target). Concurrency capped at ~12; the rest queued.
- A monthly spend limit interrupted the first pass at 16/21; resume replayed the 16 from cache and rebuilt 5 live. Interrupted agents left orphaned partial artboards → cleaned up 12 duplicates by keeping the completed (higher-ID) set after visual verification.
- `paper-asset://` + absolute local path places generated PNGs; brand CDN images place by https URL directly. Both verified.
