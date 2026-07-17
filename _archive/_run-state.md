# Unattended run — state (source of truth)

## Run: Round 2 full pass — 21 expressions × 3 fully-distinct directions, each built then polished by a fresh agent
- **Start:** 2026-07-16 23:41 CEST (real clock, `date`)
- **Mode:** Workflow pipeline (build -> polish, per expression), backgrounded. Fresh agent for the polish pass, per the user's two-pass ask ("checked twice").
- **Paper file:** caven ranch - page `4-0` "round 2" (empty at start, 0 artboards)
- **Target:** 63 frames (21 x 3). Each frame touched twice: pass 1 = build + honest self-critique; pass 2 = fresh-agent craft polish across the 8 dimensions.
- **Tally:** 0 / 63 built - 0 / 63 polished

## Layout on page 4-0
- One expression per row. Three variations across: V1 left `0`, V2 left `1560`, V3 left `3120`. Row pitch `3200`; expression i top = i x 3200.
- Artboard names: `E{NN} V{n} {slug} — {direction}`
- Discipline (from learnings.md): every Paper call passes `fileId` explicitly; no agent calls `open_file` (hijacks the sticky target); create artboard then pin left/top; `finish_working_on_nodes` at end.

## Design spine (constant across all 63) vs. what diverges
- **Constant:** the 6 color directions (rotated), real Caven photography, contemporary-never-archival, Ett Hem restraint / whitespace-first, coyote as unannounced brand animal, warm-neighbor copy (no em dashes, spell out one-ten), type is ink never green never uppercase.
- **Diverges per direction (open axes):** type system (chosen by letterform), spacing rhythm, composition, detail language, and the assigned color direction.

## Completion
- Workflow completes when all 21 pipelines finish. Then: screenshot review of page 4-0, dedupe any orphaned partials, write the round log, feed the expressions (new -> folder, developed -> bump doc, dead -> record why).

## Early structural check — 2026-07-17 ~00:00 CEST (~7 min in)
- Mechanism VERIFIED: 31 artboards placed, lanes pixel-perfect (worldX in {0,1560,3120}, worldY = row x 3200), correct names/sizes/page. Pinning holds under ~12 concurrent agents. No collisions.
- Craft VERIFIED on 3 most-built frames: genuinely distinct, whitespace-led, mixed-case ink type, real photography, on-brand. E01 coyote V1 nails Round-2 feedback (kept trail-cam + timestamp chrome, light neutral ground, no colored background). Not templates.

### WATCH-ITEMS for the review sweep (do NOT skip)
1. FABRICATED FACT: E04 negative-space V1 says "kept by one family for six generations"; E02 says "150 years." "Six generations" and "Outside Johnson City" are UNVERIFIED. Fact-check ALL copy against 06 knowledge/ and correct. The 150-years/one-family line is the safe public fact.
2. ILLUSTRATION REGISTER: E02 illustration V1 ("Slate riverbed ink") is a loose ink line drawing — sits close to the KILLED pen-and-ink/hand-drawn register. Review E02 V2/V3 (and E01 if illustrated) to ensure the set isn't leaning archival. Contemporary editorial illustration only.
3. General: confirm no agent used a kill-list face, uppercase, colored/green type, em dashes, or old-paper texture; confirm each expression's 3 variations are distinct on the open axes (not a reskin).

## FINAL — run complete (2026-07-17 ~01:00 CEST)
- **63/63 frames built + 63/63 polished. 42 agents, 0 errors, 0 skipped, 0 orphans.** ~70 min, 7.3M subagent tokens.
- Board: page `4-0`, 21 rows x 3, lanes clean.
- **Independent review (main agent):** spot-checked 13 frames across every expression type + swept all copy for prices/booking claims. Verdict: **genuinely strong, on-brand, contemporary work with ZERO hard violations found.**
- **All three of my fact-suspicions were FALSE ALARMS — the knowledge base sanctions them:** "six generations" (Andrew = gt-gt-gt grandson of settler John Robinson, 6 gens), "Johnson City" (property-details verbatim), "$400-500/night" (guest-experience + the worth-the-price concept, using the range, no booking CTA — `book` search returned 0). The agents read `06 knowledge/` correctly.
- **Enhancement made during review:** dropped the generated resting coyote into E16 V1 footer (fulfils the Round-2 "coyote lying down in the footer" ask; the agent had fallen back to a photo because image-gen was blocked for it).
- **Assets preserved:** 22 generated PNGs -> `05 graphics/assets/paper-run-02/` + `generated-assets-run-02.md` (would have been lost at session end).

## Round log — per expression (keeper · weakness · next)
- **E01 coyote** — STRONG. V1 trail-cam+timestamp (kept), V3 dither macro (kept). V2 shares V3's dither plate -> wants a fresh coyote.
- **E02 illustration** — V2 painterly + V3 forest-subtraction excellent. **V1 "riverbed ink" borderline archival — reconsider/swap.**
- **E03 heritage** — STRONG; facts fact-checked & corrected by the agent. V3 campaign card aged-but-contemporarily-framed (user gut-check). Instrument Serif unproven.
- **E04 negative-space** — STRONG whitespace-led. V1/V3 share the image-UR/headline-BL skeleton (closest pair).
- **E05 palette** — clean comparable trio (color is the only variable). Heading reads louder than the color moment (by design).
- **E06 lettering/marks** — three type+photo mastheads (script/serif/grotesk). Bespoke drawn mark deferred (logo comes last).
- **E07 cartography** — real aerials/topo. Map pins are directional guesses, not surveyed.
- **E08 preloader** — three held-moment states; grounds close in value; V2 quietest.
- **E09 site-motion** — motion-as-static-moment. Type spread only partly 3 categories (V1/V3 both sans).
- **E10 split-screen** — asymmetric splits. V3 Instrument Serif AI-adjacent; V3 images similar subjects.
- **E11 offset-stack** — **content-to-form STRETCH: no real venue photos exist, so landscape stands in for named towns/venues. Needs day-trip/venue photography.**
- **E12 horizontal-scroll** — 1955 flood retold accurately; strong. V2 quietest; two serif frames only subtly distinct.
- **E13 infinite-canvas** — Marsha's List as contemporary scattered photos (nailed the Round-2 correction). Wants a Marsha's List identifier (deferred to E06).
- **E14 full-frame-portal** — strong hero. Pale-direction accents intentionally quiet; no real video (stills stand in).
- **E15 nav/header** — restrained; coyote line-mark unannounced (reused identically). "The gate's usually open" line is a user call given in-development.
- **E16 footer** — STRONG; resting coyote placed (Round-2 ask fulfilled). V2 "Join" button slightly loud.
- **E17 gallery/carousel** — three carousel systems. V1/V3 both grotesks.
- **E18 image-framing** — three framing languages (mat / inset crop / full-bleed).
- **E19 texture** — **WEAKEST fit: contemporary texture could not be delivered (CSS can't do crisp halftone; image-gen blocked for this agent). V2 rust duotone carries it. Needs a generated texture PNG.**
- **E20 social** — STRONG. V1 sighting uses a generated photorealistic coyote (excellent). Source PNGs preserved.
- **E21 typography** — three candidate systems shown well; **display voice STILL genuinely unfound (open axis — user's letterform verdict needed).** V1/V3 share Piazzolla DNA.

## Top things for the user's eye first
1. **Display type voice** — still unfound; E21 (+ the board) puts candidates head-to-head: Familjen Grotesk, Piazzolla, Geist, and two unproven newcomers used this run (Instrument Serif, Spectral). Needs your verdict.
2. **E02 V1 riverbed-ink** — the one frame flirting with the killed hand-drawn register.
3. **Image-gen gaps** (need a reliable key): E19 contemporary texture PNG, E01 V2 fresh coyote, E06 drawn mark.
4. **E11 day-trips** — needs real venue/town photography; landscape is standing in.
5. **Doc versions NOT advanced** — deliberately. Advancing 21 expression docs would bake in decisions you haven't seen. Review the board, then I advance docs / record kills per your calls.
