# Boons, Banes, and Die Steps

**Status:** Locked canonical specification.  
**Spine:** 01 Core Engine, Batch 3 of 5 ([DEC-109](../../02_decisions/01_master_decision_log.md)).  
**Source:** Migrated 2026-09-19 from archived `03_core_baseline_system/01_resolution_engine.md` §5–6; archived glossary Boon/Bane entries cross-checked for consistency.  
**Voice:** [DEC-110](../../02_decisions/01_master_decision_log.md), [DEC-111](../../02_decisions/01_master_decision_log.md) — rules and meaning unchanged.

## Purpose <a id="purpose"></a>

Boons and Banes are how the game says "you have the advantage" or "the odds are against you" without ever writing +2 or -2. A Boon is an extra die rolled into your pool. A Bane is a die taken out of it, or, if you're down to your last die, a smaller die.

For example, attacking an enemy your ally has pinned against a wall might earn +1B on your 3d8 attack pool: you roll 4d8 and keep your highest.

This specification also owns Die Step-Up and Die Step-Down: the mechanics that grow or shrink the dice themselves, and the rule for when that happens relative to Boons and Banes.

## Scope <a id="scope"></a>

**Owns:**
- Boon and Bane definitions and their check notation (`+1B`, `+1X`).
- Final-pool timing: after pool construction and after Die Steps.
- Cancellation.
- The five Boon/Bane types and all stacking rules (same-type, different-type, Untyped, same-source).
- The Boon effect (adds one die of the same size).
- The Bane effect (removes one die; the one-die-pool Step-Down; the `d4` automatic failure).
- Die Step-Up and Die Step-Down definitions, ordering, the `d12` ceiling, and the `d4` floor rules.

**Does not own:**
- The core check and pool construction: [Core Checks and Dice Pools](01_checks_and_dice_pools.md).
- What grants Boons, Banes, or Steps: the specific Classes, Feats, Spells, Equipment, Traditions, and Conditions that carry them (Actor, Magic, and Equipment layers, pending migration).
- Difficulty Classes and vectors: [Difficulty and Target Numbers](02_difficulty_and_target_numbers.md). Boons and Banes change your pool, never the target.
- Automatic Successes: Batch 4 specification.
- Exert's maneuver procedure (the temporary `d12` → `d20` exception): owner undecided, tracked in [Batch 1's open definitions](01_checks_and_dice_pools.md#open-definitions).
- Resource costs and limits: each specific rule that calls for a Step or an Exert provides them.

## Canonical Procedure <a id="canonical-procedure"></a>

### Boons and Banes Are Final-Pool Effects <a id="final-pool-effects"></a>

Boons and Banes are resolved after ordinary pool construction and after applicable Die Step-Ups and Die Step-Downs. In check notation, `+1B` is one Boon and `+1X` is one Bane.

### Cancellation <a id="cancellation"></a>

One Boon cancels one Bane, and one Bane cancels one Boon. Cancel first, then apply what remains:

```text
2d8 +2B +1X → 2d8 +1B → 3d8
```

### Typed Stacking <a id="typed-stacking"></a>

Boon and Bane types follow a PF2e-inspired stacking model:

- **Circumstance:** Immediate situation, environment, positioning, timing, visibility, terrain, or physical conditions.
- **Enhancement:** Direct improvement or degradation of an actor, object, weapon, armor, or spell's performance.
- **Morale:** Emotional force, confidence, fear, inspiration, social pressure, hope, despair, or group cohesion.
- **Competence:** Temporary assistance from training, instruction, advice, preparation, specialized knowledge, coordinated technique, or focused performance.
- **Untyped:** An exceptional effect deliberately excluded from ordinary categories.

Multiple effects of the same type do not stack; use only the largest applicable Boon or Bane dice quantity of that type. Effects of different types stack normally. Untyped effects may stack with typed effects and other Untyped effects unless the source says otherwise.

The same named source cannot apply the same Boon or Bane more than once to the same target or check unless it explicitly says otherwise.

For example, a +1B Circumstance Boon from pinning the enemy and a +2B Circumstance Boon from high ground don't stack; you use the +2B. If the second Boon were instead a +1B Morale Boon from an ally's war chant, it would stack with the +1B Circumstance, for +2B total.

### Boons <a id="boons"></a>

Each remaining Boon adds one die of the same size to the final pool.

```text
2d8 +1B → 3d8
```

Boons participate normally in Required Success counting. A Boon does not grant an Automatic Success unless its specific effect says so.

### Banes <a id="banes"></a>

Each remaining Bane removes one die from the final pool.

```text
3d8 +1X → 2d8
3d8 +2X → 1d8
```

A pool cannot be reduced below one die. If a Bane is applied to a one-die pool, apply one Die Step-Down to that die instead:

```text
1d8 +1X → 1d6
```

Further Banes do not apply additional Die Step-Downs. If the die is already a `d4`, the check is an automatic failure.

### Die Step-Up and Die Step-Down <a id="die-steps"></a>

A Die Step-Up increases the size of every affected die by one step. A Die Step-Down decreases the size of every affected die by one step.

```text
Up-Shift: d8 → d10
Down-Shift: d10 → d8
```

Die Step-Ups and Die Step-Downs are applied before final Boons and Banes. The ordinary ladder ends at `d12`; Exert is the explicit temporary `d12`-to-`d20` exception. Universal resource costs and limits are not defined here; the specific Stamina, Essence, Class, Feat, Spell, Equipment, or Condition rule provides them.

If a Die Step-Down would reduce a `d4` under a specific effect, that effect must state its consequence. A Bane-induced `d4` Step-Down specifically causes automatic failure.

## State Changes and Results <a id="state-changes"></a>

Boons, Banes, and Die Steps modify one check's final pool and nothing else. They create no persistent state. Ongoing sources (a Condition that keeps granting a Boon, an equipment state that steps a die down) belong to their owning rules.

## Rule Interactions <a id="rule-interactions"></a>

- This procedure works on the final pool built by [Core Checks and Dice Pools](01_checks_and_dice_pools.md), at steps 5 and 6 of the core check.
- The modified pool may be read against [Difficulty and Target Numbers](02_difficulty_and_target_numbers.md); Boons and Banes never change the DC or vector.
- Classes, Feats, Spells, Equipment, and Conditions **grant** Boons, Banes, and Steps; their specifications live in the Actor, Magic, Equipment, and Conflict layers.
- Automatic Successes (Batch 4 specification) are not dice and are unaffected by anything here.
- Exert **modifies** the `d12` ceiling under its own procedure (owner pending).

Formal edges live in the [Framework Registry](../../00_architecture/framework_registry.yaml), not in this file.

## Open Definitions and Deferred Content <a id="open-definitions"></a>

1. **Cross-reference debt:** Required Successes procedure (Conflict layer), Automatic Successes (Batch 4), Exert's owning specification, and Conditions (Conflict layer) are referenced by name; precise links are added when their specifications migrate.
2. **Notation collision:** `X` marks a Bane in check notation (`+1X`) and also stands for the die size in the base check (`2dX`). The source uses both meanings; retained as written. If this proves confusing for readers, a notation decision is needed — do not change it silently.
3. **Glossary consistency:** the archived glossary's Boon/Bane entries match this specification (cross-checked 2026-09-19). Per DEC-109 the definitions above are canonical; the archived glossary stays archived.

## References <a id="references"></a>

- Decisions: [DEC-102](../../02_decisions/01_master_decision_log.md) (terminology), DEC-103 (rule hierarchy), DEC-104 (link policy), DEC-109 (this migration), DEC-110 and DEC-111 (voice).
- Related specifications: [Core Checks and Dice Pools](01_checks_and_dice_pools.md), [Difficulty and Target Numbers](02_difficulty_and_target_numbers.md).
- [Migration Manifest](../../00_architecture/migration_manifest.md) — migration provenance.
- Archived source: `ttrpg_idealization_pre_reorganization_archive_2026-08-07/03_core_baseline_system/01_resolution_engine.md` (§5–6).
