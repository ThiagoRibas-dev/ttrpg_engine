# Engine Boundaries

**Status:** Locked canonical specification.  
**Spine:** 01 Core Engine, Batch 5 of 5 ([DEC-109](../../02_decisions/01_master_decision_log.md)).  
**Source:** Migrated 2026-10-18 from archived `03_core_baseline_system/01_resolution_engine.md` §9–11.  
**Voice:** [DEC-110](../../02_decisions/01_master_decision_log.md), [DEC-111](../../02_decisions/01_master_decision_log.md) — rules and meaning unchanged.

## Purpose <a id="purpose"></a>

This is the smallest specification in the Core Engine. The procedures are done; what remains is the vocabulary that content uses to attach its rules to those procedures, and the boundary declarations that say where the engine ends and the other layers begin.

For example, a spell that reads "Requirement: a visible target" is using this specification: the spell's own rule states a condition that must hold before the engine's check can happen.

## Scope <a id="scope"></a>

**Owns:**
- The definition of **Requirement** as an engine-attaching term.
- The **Access** and **Exception** terms as they attach to engine procedures (the DEC-102 replacements for the deprecated "Permission").
- The multi-success principle: additional successful faces satisfying Required Successes or triggering explicitly defined results.
- The boundary declarations: maneuver procedures belong to the Conflict Framework; the engine generates no exceptional outcomes without a specific rule.

**Does not own:**
- The player-facing entry format (the keyword fields): [Entry Format Template](../../03_workflows/content_templates/entry_format_template.md), per DEC-103.
- Maneuver and Called Shot procedures: Conflict Framework, pending migration.
- What grants Requirements, Access, or Exceptions: the specific Classes, Feats, Spells, Equipment, Traditions, Ancestries, and Conditions that carry them.
- The aggregated glossary: 08 Framework Reference, per DEC-109.

## Canonical Procedure <a id="canonical-procedure"></a>

### Requirement, Access, and Exception <a id="requirement-access-exception"></a>

A **Requirement** states what must be true before an action or effect may be used.

**Access** is eligibility for content or capability. **Exception** overrides a baseline rule within a stated scope. Together they replace the deprecated "Permission" (DEC-102); the archived source's definition ("explicitly allows an actor to do something outside the ordinary baseline procedure") is carried by Exception.

The archived examples, translated:

```text
Requirement: Veteran Death Tradition.
Requirement: A visible target.
Exception: Cast as a Reaction.
Exception: Affect an immune target.
Exception: Choose one die result after rolling.
```

For an example of Access, a Divine Domain grants Access to its associated Tradition (DEC-100): eligibility for that Tradition's content, with no check procedure involved.

Requirements, Access, and Exceptions belong to the specific Class, Feat, Spell, Equipment, Tradition, Ancestry, or Condition that grants them.

> **Terminology note (DEC-102):** the archived source labeled its second term "Permission." That term is deprecated; its examples are rendered here as Exceptions because each one overrides a stated baseline (Reaction casting overrides the casting activity, affecting an immune target overrides immunity, choosing a die result overrides keep-highest). An alternative reading could treat some as Access; flagged in [Open Definitions](#open-definitions), not decided silently.

### The Multi-Success Principle <a id="multi-success"></a>

Additional successful faces can satisfy Required Successes or trigger explicitly defined results.

Universal combat maneuvers and Called Shots use Required Successes or an explicit Bane (`-1B`) trade-off. The exact maneuver procedures and consequences belong to the Conflict Framework (pending migration).

The engine does not automatically generate counterattacks, special effects, or superior defensive maneuvers unless a specific rule grants an Exception. This restates the base-outcome rule of [opposed checks](04_opposed_checks_and_automatic_successes.md#opposed-checks) for all checks, opposed or not.

### Layer Boundaries <a id="layer-boundaries"></a>

The archived "related canonical owners" list, translated to the framework spine:

| Archived owner | Now lives in |
|---|---|
| Framework vocabulary (glossary) | 08 Framework Reference, when it migrates (DEC-109) |
| Attributes and derived statistics | 02 Actor Framework (planned) |
| Statistical relationships | [Difficulty and Target Numbers](02_difficulty_and_target_numbers.md) (absorbed); probability data in `04_research/` |
| Domains and Skills | 02 Actor Framework (planned) |
| Magic Schools and Traditions | 05 Magic Framework (planned) |
| Defenses, damage, and wounds | 04 Conflict Framework (planned) |
| Combat maneuvers | 04 Conflict Framework (planned) |
| Resources and conditions | 04 Conflict Framework (planned) |

These are `related` edges in the registry, not dependencies: the engine functions whether or not those layers exist.

## State Changes and Results <a id="state-changes"></a>

None. This specification defines attaching vocabulary and boundaries; it creates no procedures, conditions, or state. Everything a Requirement, Access, or Exception does happens inside the rule that carries it.

## Rule Interactions <a id="rule-interactions"></a>

- All engine specifications express granted capabilities through these terms (see, for example, the granted capabilities in [Core Checks and Dice Pools](01_checks_and_dice_pools.md) and the Exceptions in [Opposed Checks and Automatic Successes](04_opposed_checks_and_automatic_successes.md)).
- Player-facing content presents these terms through the DEC-103 keyword fields, laid out in the [Entry Format Template](../../03_workflows/content_templates/entry_format_template.md).
- The specific-over-general hierarchy that governs Exceptions is DEC-103's rule: the most specific applicable rule supersedes the more general within its stated scope, and exceptions are never inferred from flavor text.

Formal edges live in the [Framework Registry](../../00_architecture/framework_registry.yaml), not in this file.

## Open Definitions and Deferred Content <a id="open-definitions"></a>

1. **Translation judgment (DEC-102):** all three archived "Permission" examples were rendered as Exceptions. Whether any should instead read as Access is an open review question.
2. **Entry-format ownership:** the keyword fields are embodied in the content template now; whether their canonical definition home is the 08 Framework Reference (with the glossary) or the template itself gets settled when 08 migrates.
3. **Standing terminology questions** (from the archived terminology matrix, tracked here because they concern entry vocabulary): whether `Feature` is the universal player-facing term; whether `rule element` appears in player-facing text; the `Special` field versus prose; `Activity` versus Project/Downtime.
4. **Cross-reference debt:** Conflict-layer links (maneuvers, Called Shots, Required Successes procedure) and Actor-layer links (attributes, skills) land when those layers migrate.

## References <a id="references"></a>

- Decisions: [DEC-102](../../02_decisions/01_master_decision_log.md) (terminology), DEC-103 (hierarchy and keyword fields), DEC-104 (link policy), DEC-109 (this migration), DEC-110 and DEC-111 (voice).
- Related specifications: [Core Checks and Dice Pools](01_checks_and_dice_pools.md), [Difficulty and Target Numbers](02_difficulty_and_target_numbers.md), [Boons, Banes, and Die Steps](03_boons_banes_and_die_steps.md), [Opposed Checks and Automatic Successes](04_opposed_checks_and_automatic_successes.md).
- [Entry Format Template](../../03_workflows/content_templates/entry_format_template.md) — the player-facing fields.
- [Migration Manifest](../../00_architecture/migration_manifest.md) — migration provenance.
- Archived source: `ttrpg_idealization_pre_reorganization_archive_2026-08-07/03_core_baseline_system/01_resolution_engine.md` (§9–11).
