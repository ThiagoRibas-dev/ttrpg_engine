# Framework Architecture Map

**Status:** Active — overview populated 2026-08-29 (DEC-107). Mechanics migrate case-by-case; this map points, it never duplicates rule text (DEC-104).  
**Purpose:** The top-level map of the active framework's goals, constraints, scope, building blocks, cross-cutting concepts, vocabularies, decisions, quality requirements, risks, and migration state.

## 1. System Overview <a id="map-overview"></a>

A **game-design framework** for a mathless, grounded-simulationist, exception-based fantasy TTRPG — not yet a finished player/GM rulebook. The framework defines canonical procedures and controlled vocabularies; player-facing publications are built from it later (reorg model §13 Phase 6).

Everything under `01_framework/` is currently empty scaffold. Until a rule is explicitly migrated, the only surviving copies live in the [sibling archive](../../ttrpg_idealization_pre_reorganization_archive_2026-08-07/README.md) and are **not** active canon (Migration Manifest rule).

## 2. Design Pillars <a id="map-pillars"></a>

Source of truth (archived, pending canonical migration): [Core Design Pillars](../../ttrpg_idealization_pre_reorganization_archive_2026-08-07/01_design_philosophy_and_pillars/01_core_design_pillars.md).

| # | Pillar | One-line thesis |
|---|---|---|
| 1 | Mathless Resolution Engine | Raw die faces vs. Target Number; step dice (d4→d12) for ceiling, pool volume for reliability, Boons/Banes instead of modifiers. |
| 2 | Grounded Simulationism | Multi-layer defenses (Evasion → Parry/Deflect → Soak → Resilience) over abstract AC; Skills as concrete capabilities with thresholds and maneuver unlocks. |
| 3 | No Meta-Currencies | Every spendable resource exists in-world (Stamina/Poise, Focus, equipment durability); no out-of-fiction reroll/editor tokens. |
| 4 | Content Wealth, High Option-Density | Options built from discrete mechanical vectors (step upgrades, pool expansion, face manipulation, action economy, defense-layer changes) + low-memory feature design (DEC-101). |

## 3. Constraints <a id="map-constraints"></a>

```text
C1  No arithmetic during active play (Pillar 1).
C2  No out-of-world spendable resources (Pillar 3, DEC-101).
C3  Exception-based rule hierarchy: the most specific applicable rule
    supersedes more general ones within its stated scope only (DEC-103).
C4  Controlled terminology: Access, Requirement, Effect, Exception,
    Restriction, Disruption (DEC-102); player-facing entries use the
    controlled keyword fields (DEC-103). Legacy wording is rewrite-target,
    not canon.
C5  One-way procedural ownership across the spine (DEC-105 §8.4):
    later layers may use/modifies earlier procedures; earlier layers
    never require later layers; requires-cycles are validation warnings.
C6  No rule-text duplication: precise links to the single owner (DEC-104).
```

## 4. Building Blocks — the Framework Spine <a id="map-spine"></a>

Dependency/authority layering (arrows = "is available to"):

```text
01 Core Engine
    → 02 Actor Framework
        → 03 Adventure Framework  ∥  04 Conflict Framework   (parallel middle)
            → 05 Magic Framework  ∥  06 Equipment Framework  (parallel)
                → 07 World and GM Framework
                    → 08 Framework Reference (aggregates; owns no procedures)
```

| Layer | Owns (future) | Status |
|---|---|---|
| 01 Core Engine | Check resolution, opposed checks, step dice, pools, Boons/Banes | In progress — Batches 1–4/5 migrated ([checks & pools](../01_framework/01_core_engine/01_checks_and_dice_pools.md), [difficulty](../01_framework/01_core_engine/02_difficulty_and_target_numbers.md), [boons & steps](../01_framework/01_core_engine/03_boons_banes_and_die_steps.md), [opposed & automatic](../01_framework/01_core_engine/04_opposed_checks_and_automatic_successes.md); DEC-109) |
| 02 Actor Framework | Attributes, derived statistics, resources, skills, leveling | Planned |
| 03 Adventure Framework | Exploration, downtime, activities, crafting | Planned |
| 04 Conflict Framework | Combat exchange, defenses, maneuvers, conditions | Planned |
| 05 Magic Framework | Traditions, spellcasting, domains | Planned |
| 06 Equipment Framework | Weapons, armor, durability, gear | Planned |
| 07 World and GM Framework | GM procedures, world scaling, simplified actors | Planned |
| 08 Framework Reference | Aggregated reference; no owned procedures | Planned |

Note: migration order (reorg model §13 Phase 4) is **not** the layering order — Conflict (04) migrates before Adventure (03) because it is more settled.

## 5. Cross-Cutting Concepts <a id="map-concepts"></a>

Pointers only — canonical text lands in `01_framework/` on migration.

- **Resolution primitives** — step dice d4–d12, pools keep-highest, Boon/Bane dice (Pillar 1; archived resolution engine).
- **Defense layers** — Evasion, Parry/Deflection, Soak, Resilience (Pillar 2.1; archived simulationist subsystems).
- **In-world resources** — Vitality, Stamina/Poise, Focus, Essence (Pillar 3.2; archived attributes doc).
- **Skills** — 73 fixed Skills (Combat 9, Athletics/Movement/Survival 7, Subterfuge/Perception 6, Knowledge 9, Social 6, Craft 8, Magic Traditions 28) + open-ended Lore; Manual Skill Investments (DEC-095); 28 canon Traditions (DEC-098); caster benchmark 1 Magic Investment per Spell Slot Advancement + Domain Tradition Grant (DEC-100).
- **Content conversion vectors** — DEC-101 low-memory preference order; source feature names retained until replacement approved.

## 6. Controlled Vocabularies <a id="map-vocabulary"></a>

| Vocabulary | Scope | Authority |
|---|---|---|
| Registry relationships (`requires`, `uses`, `grants`, `modifies`, `limits`, `tests`, `replaces`, `contains`, `related`) | Registry edges only | [relationship_vocabulary.md](relationship_vocabulary.md) — DEC-106 |
| Player-facing entry keywords (Traits, Prerequisite, Requirement, Trigger, Frequency, Cost, Effect, Restriction, Exception, Special) | Published rules text | DEC-103 |
| Core rule nouns (Access, Requirement, Effect, Exception, Restriction, Disruption) | All active prose | DEC-102 + glossary (archived, pending migration) |

## 7. Decisions <a id="map-decisions"></a>

Continuous log (DEC-001 → present): [Master Decision Log](../02_decisions/01_master_decision_log.md). Load-bearing recent decisions:

| DEC | Subject |
|---|---|
| DEC-095 / 098 / 100 | Skill investments, 28 Traditions, caster benchmark |
| DEC-101 | Low-memory feature conversion |
| DEC-102 / 103 | Terminology deprecations; exception-based hierarchy |
| DEC-104 / 105 | Link + anchor policy; reorganization baseline |
| DEC-106 / 107 | Registry vocabulary locked; first migration target |

## 8. Quality Requirements <a id="map-quality"></a>

- Registry completeness: no dangling edges, missing paths, duplicate owners (reorg model §9 completeness report; validation rules §11).
- Every migrated rule gets: canonical path + registry node + manifest row + precise links + explicit open definitions (Migration Manifest rule).
- Generated views on demand only (DEC-105); never hand-edited.

## 9. Risks and Open Items <a id="map-risks"></a>

- `01_framework/` still empty — all mechanics remain archive-only until migrated.
- Open terminology questions: `Feature` as universal player term; `rule element` player-facing visibility; `Special` field vs. prose; `Activity` vs. Project/Downtime (terminology matrix §9, archived).
- Outstanding-definitions index still lives only in the archive (Phase 5 reclassification pending).
- Long-standing open design items: weapon Damage Boxes, shields, Disarm, Shove forced movement, Rally/Intimidate/Taunt/Assess, companions, spell preparation/acquisition, simplified actors.

## 10. Migration State <a id="map-migration"></a>

Current: reorg model Phase 4 started — architecture map + registry seed (DEC-106/107), anchor syntax validated (DEC-108), Core Engine Batches 1–4 of 5 migrated (DEC-109: checks & pools, difficulty & target numbers, boons/banes & die steps, opposed checks & automatic successes), and the first research artifact registered (Tier Difficulty Vector calibration). Next: Core Engine **Batch 5 — engine boundaries**, the final Core Engine batch. Progress table: [Migration Manifest](migration_manifest.md).

## Navigation

- Formal relationship data: [Framework Registry](framework_registry.yaml)
- Migration status: [Migration Manifest](migration_manifest.md)
- Reorganization model: [Framework Reorganization Model](../FRAMEWORK_REORGANIZATION_MODEL_DRAFT.md)
- Continuing decisions: [Master Decision Log](../02_decisions/01_master_decision_log.md)
