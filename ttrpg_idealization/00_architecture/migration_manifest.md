# Migration Manifest

**Status:** Phase 4 in progress — Core Engine, Batch 2 of 5 complete (DEC-109).  
**Initial archive:** `/home/user/ttrpg_idealization_pre_reorganization_archive_2026-08-07`

## Migration rule

No archived document becomes active canon by default. Every migrated rule must receive:

1. A new canonical specification path under `01_framework/`.
2. A registry node in `framework_registry.yaml`.
3. A migration row showing old source, new owner, status, and action.
4. Precise Markdown links to relevant active decisions and research.

Architecture documents under `00_architecture/` follow the same row-tracking even when they are not rule specifications. Research relocations under `04_research/` are tracked here as well.

## Migration table

| Old archive source | New destination | Type | Status | Action |
|---|---|---|---|---|
| `06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md` | `02_decisions/01_master_decision_log.md` | Decision log | Migrated (Phase 2) | Copied unchanged; log continues in place (DEC-105). |
| `01_design_philosophy_and_pillars/01_core_design_pillars.md` | `00_architecture/framework_architecture_map.md` §2 | Pillar summary | Summarized (2026-08-29, DEC-107) | One-line pointers only; full canonical pillar spec still pending future migration. |
| *(new decision — no archive source)* | `00_architecture/relationship_vocabulary.md` | Vocabulary | Approved (DEC-106) | Nine-term registry vocabulary locked; software terms rejected. |
| *(new — registry seed)* | `00_architecture/framework_registry.yaml` | Registry seed | Seeded (2026-08-29, DEC-107) | Root + 8 spine areas (`contains`) + 2 architecture documents. |
| `03_core_baseline_system/01_resolution_engine.md` §1–2 | `01_framework/01_core_engine/01_checks_and_dice_pools.md` | Canonical specification | Migrated 2026-09-18 (Batch 1, DEC-109) | Rewritten per spec template; DEC-102 terminology applied (step 10 "Permission" → granted capability, note in spec); cross-reference debt and open definitions listed in-spec; registry node `core.checks-and-pools`. Re-voiced 2026-09-19 per DEC-110/111; rules and meaning unchanged. |
| `03_core_baseline_system/01_resolution_engine.md` §4 + `08_statistical_framework_and_check_modes.md` | `01_framework/01_core_engine/02_difficulty_and_target_numbers.md` | Canonical specification | **Migrated 2026-09-19 (Batch 2, DEC-109)** | §4 (DC scale, working descriptions, vector notation, positional comparison) plus 08's check-mode and statistical relationships consolidated; 08's probability-research pointers remain archived (Phase 5 reclassification); unnamed intermediate DCs (4/6/8/10) and calibration status recorded as open definitions; registry node `core.difficulty-and-target-numbers` + `uses` edge from `core.checks-and-pools`. |
| `13_tier_difficulty_vector_reference.md` | `04_research/probability_and_calibration/tier_difficulty_vector_reference.md` | Research calibration reference | **Relocated 2026-09-19 (Batch 2, DEC-109)** | Copied with provenance header; **status change flagged:** archived dual status "Canonical Tier Difficulty Vector Reference and research calibration artifact" reduced to research calibration reference per DEC-109 (procedure owned by the Batch 2 spec); internal archive paths fixed; registry node `research.tier-difficulty-vectors` + `tests` edge. |
| `03_core_baseline_system/01_resolution_engine.md` §5–6 | `01_framework/01_core_engine/03_boons_banes_and_die_steps.md` | Canonical specification | Planned — **Batch 3, next** | Boons/Banes, cancellation, typed stacking, Die Step-Up/Down. |
| `03_core_baseline_system/01_resolution_engine.md` §7–8 | `01_framework/01_core_engine/04_opposed_checks_and_automatic_successes.md` | Canonical specification | Planned — Batch 4 | Opposed contests, defender tie-wins, Automatic Successes. |
| `03_core_baseline_system/01_resolution_engine.md` §9–11 | `01_framework/01_core_engine/05_engine_boundaries.md` | Boundary specification | Planned — Batch 5 | Entry-field vocabulary home (DEC-102/103 rewrite), complex-check boundary → Conflict layer, related owners → registry edges. |

## Pending classification (Phase 3 inventory)

Remaining archived documents are classified as they migrate. None is active canon.
