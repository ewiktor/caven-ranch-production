# Learnings — reusable tool and prompt findings

One line per finding. Check before every compile; add only NEW findings — never re-derive what's already logged. This file exists so per-round logs stay short.

Scope: toolchain and prompt-craft findings that will recur (a phrasing that reliably works, a tool behavior that bites, a parameter that gets ignored). Brand decisions do not go here — those are `settled.md`. Per-round observations stay in the round entries.

Toolchain findings transfer between brand repos that use the same tools: when starting a new brand on a known toolchain, port the relevant sections from the previous repo's learnings at intake. Brand findings never transfer.

Group by tool, works vs. fails:

## [Tool / model name]

### Works (reuse)
- [finding]

### Fails (avoid)
- [finding]

### Proven skeletons
[Prompt skeletons that have earned reuse, if any.]

## Figma MCP (get_screenshot / get_metadata)

### Works (reuse)
- Band/section title strips on huge canvases: screenshot the header frame node directly, then crop the left portion and upscale 3x locally (PIL) — titles read cleanly even from 30,000px-wide strips.
- get_metadata on a whole canvas overflows; save to file and cluster top-level nodes by x/y buckets in python to map a big working page cheaply.

### Fails (avoid)
- get_screenshot errors ("unexpected error") on page-level nodes and very large frames (~38,000px wide Frame 21 failed twice). Screenshot child frames/regions instead.

## Notion MCP (notion-fetch)

### Works (reuse)
- Pages >25k tokens get saved to a file by the harness; hand the file to a general-purpose subagent for a full-coverage digest (structure + complete entry list + verbatim quotes for load-bearing parts) instead of slicing it in the main context.

## DRAPER exports (load-brand.py)

### Fails (avoid)
- context.md commentary in the numbered `N. **Title**` format isn't parsed by load-brand.py (expects `### Title`) — reports "0 got commentary merged". Merge by hand/one-off script; a parser fix is flagged as a background task.
- Media exports can carry real per-item commentary in media/context.md (spec says bulk CDN index only) — check and merge it like references.

## Paper MCP — parallel multi-agent runs

### Works (reuse)
- Fan out one agent per expression into ONE Paper file: pass fileId explicitly on EVERY Paper call, and never call open_file inside an agent (it hijacks the sticky-file target for other agents). ~12 concurrent cap on a 14-core box; excess queues.
- paper-asset:// + absolute local path places generated PNGs; brand CDN https URLs place directly in <img src>. Both verified in-canvas.
- A "1 child" artboard is often fine — one big flex container holds the whole comp; judge by screenshot, not childCount.
- A `Workflow` pipeline (build stage -> fresh-agent polish stage, one lane per expression, `agentType: 'general-purpose'`) ran 42 agents into ONE Paper file with 0 errors / 0 orphans. Same discipline holds as Agent-tool fan-out: fileId on every call, no open_file. This supersedes the "run serially, parallel workflow is unsafe" line in `unattended run.md`.
- **Assign each lane explicit non-overlapping coordinates** (V-columns at left 0/1560/3120, row pitch ~3200 by expression index) and have each agent `create_artboard` then `update_styles` to pin its `left`/`top`. create_artboard auto-places to "best empty spot", which races under concurrency; pinning after creation removes all overlap. Verified: 63 artboards landed pixel-perfect in lanes.
- `write_html` in `replace` mode on an image slot keeps the slot's flex position even though `createdNodes` reports a pre-layout worldX (looked like it jumped to x:0 but rendered in the right slot). Trust the screenshot, not the returned coord.
- Placing a generated PNG: reference the **no-spaces scratchpad path** (`paper-asset:///private/tmp/.../scratchpad/...`) rather than the repo path (which has spaces like `05 graphics/`). Paper then persists the image to its own CDN, so the frame survives even after scratchpad is cleaned.

## Prompt workflow (2026-07-17, user-set)

### Works (reuse)
- **Two-stage prompt loop:** stage 1 = three directions written as SINGLE-IMAGE image-gen prompts (fully standalone prose, whole frame described, copy in quotes, hex in parentheses, NO links/assets/build specs) that the user runs in an image tool to see the direction in seconds; stage 2 = only the picked winner gets a full Paper build. Full build prompts with CDN links break in Claude Design ("Drop image / Browse file"), and paper-asset:// paths only resolve in the authoring session — never hand those to the user for external tools.

## Nano Banana Pro (image-gen in subagents)

### Works (reuse)
- Subagents CAN generate contemporary images and place them in Paper — this run produced strong on-brand coyotes (resting, pack, walking, a photorealistic dusk two-coyote sighting), painterly/subtraction illustrations, flood scenes, and nature specimens.

### Fails (avoid)
- **Image-gen availability is INCONSISTENT across parallel subagents:** some agents had the key, others hit `GEMINI_API_KEY/GOOGLE_API_KEY unset` and silently fell back to photography (E01 partly, E16 footer, E19 texture) — even though a perfect asset (e.g. `v1-coyote-resting.png`) had already been generated by another agent. Before a run, confirm the key is set for the subagent environment; after a run, sweep the scratchpad for assets other agents made and reuse them.
- **Generated PNGs live only in the per-run scratchpad and vanish at session end.** Copy them into the repo (`05 graphics/assets/paper-run-NN/`) + write a manifest as a post-run step, or the work is lost.

### Fails (avoid)
- Workflow args passed as a JSON string can break on embedded quotes/apostrophes; embed the units array INLINE in the script instead of routing through args for large payloads.
- A monthly spend-limit mid-run leaves interrupted agents' partial artboards orphaned; resume rebuilds them fresh (new higher IDs), so dedupe afterward by keeping the completed set and deleting the older partial trio.
