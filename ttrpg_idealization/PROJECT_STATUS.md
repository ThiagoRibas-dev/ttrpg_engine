# Project Status — Framework Rewrite

**Current phase:** Phase 4 — case-by-case framework migration (reorg model §13).  
**Current operation:** Core Engine migration — Batches 1–2 of 5 complete; Batch 3 (boons, banes, die steps) next.

## Active state

Two canonical rule specifications are live under `01_framework/01_core_engine/`: `01_checks_and_dice_pools.md` (Batch 1) and `02_difficulty_and_target_numbers.md` (Batch 2), plus the first research artifact, `04_research/probability_and_calibration/tier_difficulty_vector_reference.md` (calibration data, DEC-109). Archived mechanics remain non-canonical until individually migrated.

## Remote repository

Since 2026-09-19 the project lives in a public git repository: `https://github.com/ThiagoRibas-dev/ttrpg_engine`. Both trees (active root and pre-reorganization archive) were moved into it as siblings, preserving every relative archive link. Publishing procedure, credential handling, and the clone-without-archive command: [AGENTS.md — Git publishing](AGENTS.md).

## Completed reorganization phases

### Phase 1 — Archive snapshot (2026-08-07)

The complete prior root was renamed and preserved at:

```text
/home/user/ttrpg_idealization_pre_reorganization_archive_2026-08-07/
```

Location note (2026-09-19): the archive has since moved into the git repository as a sibling of the active root — see [Remote repository](#remote-repository).

### Phase 2 — Fresh architecture scaffold (2026-08-07)

Framework Spine directories, YAML registry skeleton, architecture-map skeleton, migration manifest, generated-view policy, continuing master decision log, and directory boundaries.

### Phase 4 (first target) — Architecture map and vocabulary (2026-08-29)

- **DEC-106:** nine-term registry relationship vocabulary approved; software terms rejected.
- **DEC-107:** architecture map populated from archived canon; registry seeded.

### Phase 4 (continued) — stable-anchor validation (2026-09-18)

**DEC-108:** DEC-104 anchor syntax validated in VS Code's built-in Markdown preview. `<a id>` heading anchors, auto-slugs, `{#id}` attributes, cross-file `path#anchor` links, and bare anchors all pass; legacy `<a name>` fails and is rejected. Test retained as regression check.

### Phase 4 (continued) — Core Engine Batches 1–2 (2026-09-18/19)

**DEC-109:** five-batch Core Engine plan approved (checks/pools → difficulty → boons/banes/steps → opposed/automatic → boundaries); difficulty tables split to `04_research/`; specs own their definitions inline.

- **Batch 1:** `01_checks_and_dice_pools.md` — locked spec, registry node `core.checks-and-pools`, DEC-102 terminology applied with in-spec note, open definitions listed. Re-voiced per DEC-110/111.
- **Batch 2:** `02_difficulty_and_target_numbers.md` — locked spec (DC scale, vectors, check modes from archived §4 + 08); `13_tier_difficulty_vector_reference.md` relocated to `04_research/` with its dual canonical/research status reduced to research calibration (flagged in manifest); registry nodes `core.difficulty-and-target-numbers` and `research.tier-difficulty-vectors`, with the first `uses` and `tests` edges.

### Phase 4 (continued) — prose voice (2026-09-19)

**DEC-110:** house prose voice adopted for all framework prose and project communication — warm plain English modeled on the D&D 3.5e PHB introduction, with an explicit AI-ism ban list. Standard: `03_workflows/content_templates/voice_and_style_guide.md`.

**DEC-111:** voice refined — each claim is stated once and shown once with a concrete example; no restatement, no nested parenthetical re-statements.

## Next operation

**Core Engine Batch 3 — boons, banes, and die steps:** extract archived `01_resolution_engine.md` §5–6 into `01_framework/01_core_engine/03_boons_banes_and_die_steps.md`; register nodes/edges; add manifest row; link decisions; list open definitions; user review before Batch 4.

## Open decisions still needed

See reorg model §15 items 2 (partial), 3, 6.
