# Core Checks and Dice Pools

**Status:** Locked canonical specification.  
**Spine:** 01 Core Engine, Batch 1 of 5 ([DEC-109](../../02_decisions/01_master_decision_log.md)).  
**Source:** Migrated 2026-09-18 from archived `03_core_baseline_system/01_resolution_engine.md` §1–2.  
**Voice:** [DEC-110](../../02_decisions/01_master_decision_log.md), [DEC-111](../../02_decisions/01_master_decision_log.md) — rules and meaning unchanged.

## Purpose <a id="purpose"></a>

This is the engine that runs the whole game. When your character tries something that might fail — picking a lock, or calming an angry innkeeper — you roll dice to find out what happens.

There is no arithmetic at the table. When you roll the dice, you don't add a Strength bonus or subtract a cover penalty.

Your character's limits and capabilities are defined by the size of dice, while the amount represents reliability. For example, a character that rolls 4d4 can reliably roll at least one 3, but can never roll a 6.

This is Pillar 1 of the [Core Design Pillars](../../../ttrpg_idealization_pre_reorganization_archive_2026-08-07/01_design_philosophy_and_pillars/01_core_design_pillars.md).

## Scope <a id="scope"></a>

**Owns:**
- The ten-step core check procedure.
- The Attribute die ladder and the ordinary `d12` ceiling (the Exert `d20` exception is referenced, not owned).
- The base check: `2dX keep highest`.
- The definitions of Natural Dice Pool and Enhanced Dice Pool.
- The ordinary pool-range guideline.

**Does not own:**
- Difficulty Classes and difficulty vectors: [Batch 2 specification](02_difficulty_and_target_numbers.md).
- Boons, Banes, and Die Step-Up / Step-Down mechanics: [Batch 3 specification](03_boons_banes_and_die_steps.md).
- Opposed contests and Automatic Successes: [Batch 4 specification](04_opposed_checks_and_automatic_successes.md).
- Attribute assignment and Competency Rank definitions: Actor Framework.
- Resource costs and the Exert maneuver procedure: owning layer to be determined.
- Maneuver consequences: Conflict Framework.

## Canonical Procedure <a id="core-check-procedure"></a>

### The Core Check

When an actor attempts an uncertain action:

1. Identify the relevant Skill, Tradition, defense, or other capability.
2. Determine the relevant Attribute Die Size.
3. Build the Natural Dice Pool from Attribute and Competency.
4. Apply permanent or ordinary class, feat, equipment, and situational effects.
5. Apply Die Step-Ups and Die Step-Downs.
6. Apply final Boons and Banes, including cancellation and typed stacking.
7. Resolve the final Difficulty Vector or opposed contest.
8. Roll the final dice pool.
9. Compare successful faces against the DC, Required Successes, or opposing pool.
10. Apply the resulting success, failure, maneuver, condition, or granted capability.

Ordinary resolution uses no linear numerical modifiers.

**Important:** You don't need to memorize this list. Once you understand the basics (build the pool, roll it, keep your highest die, compare it to the target), the rest is detail you'll pick up in play.

> **Terminology note (DEC-102):** Step 10 formerly read "…or Permission." "Permission" is deprecated. Its meanings now split into **Access** (eligibility for content or capability) and **Exception** (override of a baseline rule within a stated scope). Active documents express granted capabilities through those terms.

### The Attribute Die Ladder <a id="die-ladder"></a>

```text
d4 → d6 → d8 → d10 → d12
```

The ordinary ceiling is `d12`, and the former permanent over-cap notation is deprecated. One exception exists: Exert can step an affected `d12` up to `d20` for one roll, under its own maneuver procedure. That procedure's home is still undecided; see [Open Definitions](#open-definitions).

### Base Check <a id="base-check"></a>

```text
2dX keep highest
```

`X` is the relevant Attribute Die Size: roll two dice, keep the higher. Competency Rank, class features, Boons, Banes, equipment, and other explicit effects change the final pool or what it can do (Access and Exceptions, DEC-102).

### Natural Dice Pool <a id="natural-dice-pool"></a>

The pool produced by ordinary, standing factors (Attribute, Competency, Class, and other persistent traits), before temporary or special enhancements are applied.

### Enhanced Dice Pool <a id="enhanced-dice-pool"></a>

The final or temporarily modified pool, after applicable feats, spells, equipment, circumstances, and other explicit effects.

### Pool Range Guideline <a id="pool-range"></a>

An unbuffed pool normally runs from `1dX` to `6dX`, and `6dX` is reserved for Legend Competency and equivalent content. Content may exceed the guideline through explicit Legend or Mythic effects, but the expansion must remain controlled by the content granting it.

## State Changes and Results <a id="state-changes"></a>

A check resolves to an outcome: success, failure, or a counted-successes result per the difficulty vector or contest. The procedure itself creates no persistent state. Any Condition, Tag, resource expenditure, or ongoing Effect comes from the specific rule that called for the check, expressed through the DEC-102 vocabulary and the DEC-103 player-facing keyword fields.

## Rule Interactions <a id="rule-interactions"></a>

- Skills, Traditions, and defenses **use** this procedure to resolve attempts (their specifications live in the Actor, Magic, and Conflict layers).
- Boons/Banes and Die Step-Ups/Downs **modify** the final pool at steps 5–6 ([Batch 3 specification](03_boons_banes_and_die_steps.md)).
- Class features, Feats, Spells, and Equipment **grant** additional pool dice (Enhanced Dice Pool) or Access/Exceptions touching pool construction.
- Exert **modifies** the ladder ceiling (`d12` → `d20`) under its own procedure.
- No content may bypass or alter the core procedure without an explicit Exception (DEC-103 rule hierarchy).

Formal edges live in the [Framework Registry](../../00_architecture/framework_registry.yaml), not in this file.

## Open Definitions and Deferred Content <a id="open-definitions"></a>

1. **Cross-reference debt:** Boons, Banes, Die Step-Up/Down, Difficulty Vectors, Required Successes, opposed contests, Exert, and Competency Ranks are referenced by name; precise links are added when their specifications migrate (Batches 2–4 and the Actor layer).
2. **Exert's owning specification** (resource or maneuver home: Actor vs. Conflict layer) is undecided.
3. **Source fidelity note:** the archived source jumps from §2 to §4 (no §3), a historical numbering artifact; no content was lost.
4. **Pool-range boundary:** "generally `1dX` to `6dX`" is treated as a guideline with content-controlled exceptions, exactly as written; if a stricter hard limit is intended, that is an open rule decision.

## References <a id="references"></a>

- Decisions: [DEC-102](../../02_decisions/01_master_decision_log.md) (terminology), DEC-103 (rule hierarchy), DEC-104 (link policy), DEC-109 (this migration), DEC-110 (prose voice), DEC-111 (statement and example).
- [Migration Manifest](../../00_architecture/migration_manifest.md) — migration provenance.
- Archived source: `ttrpg_idealization_pre_reorganization_archive_2026-08-07/03_core_baseline_system/01_resolution_engine.md` (§1–2).
- Vocabulary: per DEC-109, the term definitions above (Natural/Enhanced Dice Pool) are canonical here; the archived `00_baseline_framework_glossary.md` remains archived and non-canonical.
