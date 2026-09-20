# Stable-Anchor Syntax Validation Test

**Status:** Completed 2026-09-18 — DEC-104 confirmed (DEC-108). Retained as a regression test for future renderers; a validation tool, not canonical content, not a registry node or migration row.  
**Purpose:** Empirically confirm which anchor syntax survives the Markdown renderer(s) this project will actually be read in, before broad migration (DEC-104; reorg model §15.5).  
**Created:** 2026-09-18.

## How to run

1. Open this file in the viewer/editor you will actually use to read the framework. If you use several, repeat per viewer.
2. Click each "Try it" link.
3. Report results: viewer name + which tests passed (table at the bottom).

**Pass** = clicking the link jumps to the target section.  
**Fail** = nothing happens, jumps to the wrong place, or a heading/anchor visibly shows literal code such as `<a id="...">` or `{#test-d}`.

Note: the in-chat workspace preview is a valid extra data point, but it is sandboxed — it is not authoritative for your real workflow.

## Anchor ID convention under test

DEC-104 anchor IDs are lowercase with hyphens, e.g. `resource-stamina`, `map-pillars`.

---

## Test A — DEC-104 primary: HTML `id` anchor inside a heading

Try it: [Jump to Target A](#test-a)

## Target A <a id="test-a"></a>

Destination for Test A. If the link above brought you here, inline HTML `<a id>` anchors work in this renderer.

## Test B — HTML `name` attribute variant

Try it: [Jump to Target B](#test-b)

## Target B <a name="test-b"></a>

Destination for Test B. The `name` attribute is an older HTML variant that some sanitizers accept when they strip `id`.

## Test C — Auto-generated heading slug (no manual anchor)

Try it: [Jump to Target C](#target-c-auto-slug)

## Target C Auto Slug

Destination for Test C. No manual anchor here — the link targets the renderer's automatic slug for this heading. If this passes while A and B fail, we fall back to auto-slugs, at the cost that renaming a heading silently breaks every link to it.

## Test D — Heading attribute syntax `{#id}` (Pandoc / kramdown extension)

Try it: [Jump to Target D](#test-d)

## Target D {#test-d}

Destination for Test D. Renderers without this extension will show the literal text `{#test-d}` in the heading above — that visible text is itself a fail signal.

## Test E — Cross-file link to a real DEC-104 anchor

Try it: [Design Pillars section of the Framework Architecture Map](../../00_architecture/framework_architecture_map.md#map-pillars)

This is the live pattern DEC-104 mandates for all future framework documents: a precise relative Markdown link ending in a stable anchor ID, pointing into an actual architecture document.

## Test F — Bare anchor before a paragraph (outside any heading)

Try it: [Jump to Target F](#test-f)

<a id="test-f"></a>
This paragraph is the destination for Test F. This tests whether anchors may live outside headings — which matters for anchoring tables, list items, or paragraphs that have no heading of their own.

---

## Results — 2026-09-18

**Viewer tested:** VS Code (built-in Markdown preview)

| Test | Method | Pass/Fail | Notes |
|---|---|---|---|
| A | `<a id>` in heading (DEC-104 primary) | **Pass** | Primary syntax confirmed. |
| B | `<a name>` in heading | **Fail** | Legacy attribute not a link target here; variant rejected. |
| C | auto heading slug | **Pass** | Emergency fallback available. |
| D | `{#id}` heading attribute | **Pass** | Works, but non-standard; not adopted — A is primary. |
| E | cross-file `path#anchor` | **Pass** | Live link into `framework_architecture_map.md#map-pillars` — the mandated pattern. |
| F | bare anchor before paragraph | **Pass** | Tables and paragraphs can be anchored. |

## Decision rule

- **A passes** in every target viewer → DEC-104 confirmed unchanged.
- A fails, **B passes** → amend DEC-104 to `<a name="...">`.
- A and B fail, **C passes** → fall back to auto-slugs plus a "heading text is frozen" rule (weakest option; renames break links).
- **D passes** everywhere and A fails → adopt `{#id}` only if the toolchain is strictly Pandoc/kramdown (non-standard elsewhere).
- **E failure** with A passing → cross-file anchor links are unreliable; anchors get scoped to same-file use only, and cross-file links point to the file (section references by name).

Whatever the outcome, it gets recorded as a decision (confirmation or amendment of DEC-104) before the 01 Core Engine migration begins.

**Outcome (2026-09-18):** Test A passes in VS Code's built-in Markdown preview → **DEC-104 confirmed unchanged**; recorded as DEC-108. This document is retained as a regression check for any future renderer.
