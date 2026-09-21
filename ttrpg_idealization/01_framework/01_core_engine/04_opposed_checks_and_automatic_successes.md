# Opposed Checks and Automatic Successes

**Status:** Locked canonical specification.  
**Spine:** 01 Core Engine, Batch 4 of 5 ([DEC-109](../../02_decisions/01_master_decision_log.md)).  
**Source:** Migrated 2026-09-20 from archived `03_core_baseline_system/01_resolution_engine.md` §7–8; archived glossary Automatic Success entry cross-checked for consistency.  
**Voice:** [DEC-110](../../02_decisions/01_master_decision_log.md), [DEC-111](../../02_decisions/01_master_decision_log.md) — rules and meaning unchanged.

## Purpose <a id="purpose"></a>

When two characters pit themselves directly against each other — a pickpocket's fingers against a sentry's ears, or a fencer's lunge against a duelist's parry — neither side rolls against a number on the wall. Both build pools, both roll, and the dice settle it between them.

This specification also owns Automatic Successes: successes that a specific rule grants you outright, with no die involved. For example, an expert burglar's climb spell might guarantee one success on the wall she's scaling, so she only needs to roll for the rest.

## Scope <a id="scope"></a>

**Owns:**
- The opposed-check procedure: pool construction, positional comparison, and tie-breaking.
- The defender-wins-ties rule and the neutral-contest exception.
- The base outcome of an opposed contest (success or failure, nothing more).
- Automatic Successes: what they are, when they resolve, what they count toward, and the pre-roll comparison in opposed contests.

**Does not own:**
- The final-pool construction procedure both sides use: [Core Checks and Dice Pools](01_checks_and_dice_pools.md).
- What counts as a neutral contest: each specific contest's rule states it.
- Defense procedures, maneuvers, and the Required Successes procedure: Conflict Framework, pending migration.
- Automatic Success sources: the specific Classes, Feats, Spells, Equipment, Traditions, Ancestries, and Mythic effects that grant them.

## Canonical Procedure <a id="canonical-procedure"></a>

### Opposed Checks <a id="opposed-checks"></a>

An opposed check uses the same final-pool construction procedure for both participants.

1. Identify the initiator as the attacker for that contest.
2. Identify the responding party as the defender.
3. Compare the highest rolled faces.
4. If tied, compare the remaining dice in descending order.
5. If the pools remain identical through all comparable dice, the defender wins the tie.
6. Apply the contest's success or failure consequence.

For example, your rogue sneaks past a sentry. You roll 4d6 and get 6, 5, 5, 2; the sentry rolls 3d6 and gets 6, 5, 4. Best dice first: 6 against 6, a tie. Next: 5 against 5, still tied. Next: your second 5 beats the sentry's 4, so the sneak succeeds. The sentry's fourth die doesn't exist to compare, and your 2 was never reached.

The defender wins ties in ordinary opposed contests. A specific neutral contest, such as a race, may explicitly allow a tie instead of requiring a victor.

The base opposed framework is success or failure. Superior defensive results, counterattacks, ripostes, or other exceptional outcomes require an explicit Exception granted by a Class, Feat, Equipment, Spell, or other rule.

> **Terminology note (DEC-102):** the archived source granted these outcomes and abilities through "Permissions" (deprecated). They are expressed here as Exceptions and granted capabilities; the rules themselves are unchanged.

### Automatic Successes <a id="automatic-successes"></a>

An Automatic Success is granted directly by a specific effect. It is not a die.

Automatic Successes are resolved after the final pool has been constructed, including all Boons, Banes, and Die Steps, and when that pool is rolled. They do not alter the pool itself.

An Automatic Success:

- Counts toward Required Successes.
- Is not affected by Boons, Banes, Die Step-Ups, or Die Step-Downs.
- May be granted by the same effect that grants a Boon or Bane.
- May exceed the number of Required Successes under the base framework.

In opposed contests, compare Automatic Success totals before rolling dice. The side with more Automatic Successes wins. If both sides have the same number, roll the pools and resolve the ordinary opposed procedure.

For example, a duel opens with 3 Required Successes at DC 9, and your swordsman has +1 Automatic Success from his training: he needs only two successful rolled faces, because one success is already guaranteed.

The base framework does not itself grant sources of Automatic Successes or directly alter Required Successes. Specific Classes, Feats, Spells, Equipment, Traditions, Ancestries, or Mythic effects provide them.

## State Changes and Results <a id="state-changes"></a>

An opposed check resolves to one side's success and the other's failure (or an explicit tie in a neutral contest). Automatic Successes count toward success totals during the check they were granted for. Neither creates persistent state; ongoing consequences belong to the rule that called for the contest or granted the success.

## Rule Interactions <a id="rule-interactions"></a>

- Both sides of an opposed check build their pools with [Core Checks and Dice Pools](01_checks_and_dice_pools.md); Boons, Banes, and Die Steps apply to those pools per the [Batch 3 specification](03_boons_banes_and_die_steps.md), but never to Automatic Successes.
- Vectors and DCs from [Difficulty and Target Numbers](02_difficulty_and_target_numbers.md) govern the unopposed mode; Required Successes in maneuvers will use this specification's counting rules (Conflict Framework, pending).
- Defense procedures will resolve as opposed checks; the defender-wins-ties rule carries into them (Conflict Framework, pending).

Formal edges live in the [Framework Registry](../../00_architecture/framework_registry.yaml), not in this file.

## Open Definitions and Deferred Content <a id="open-definitions"></a>

1. **Cross-reference debt:** Required Successes procedure, defense procedures, and maneuvers (Conflict Framework) are referenced by name; precise links land when that layer migrates.
2. **Required Successes notation:** the source's example uses the shorthand `DC 9 (3)` for three Required Successes at DC 9. That shorthand is not defined anywhere in canon; the defined multi-success form is the difficulty vector (for example, `DC 9,9,9`). A notation decision is needed; nothing was changed silently.
3. **Excess Automatic Successes:** the source allows Automatic Successes to exceed the number of Required Successes without stating what the surplus does. Preserved as written; a future decision should say whether surplus successes carry any effect.
4. **Glossary cross-check:** the archived glossary's Automatic Success entry matches this specification and adds that Automatic Successes are unaffected by opposed-roll tiebreaking, consistent with the pre-roll comparison rule here. Noted for the eventual glossary migration.

## References <a id="references"></a>

- Decisions: [DEC-102](../../02_decisions/01_master_decision_log.md) (terminology), DEC-103 (rule hierarchy), DEC-104 (link policy), DEC-109 (this migration), DEC-110 and DEC-111 (voice).
- Related specifications: [Core Checks and Dice Pools](01_checks_and_dice_pools.md), [Difficulty and Target Numbers](02_difficulty_and_target_numbers.md), [Boons, Banes, and Die Steps](03_boons_banes_and_die_steps.md).
- [Migration Manifest](../../00_architecture/migration_manifest.md) — migration provenance.
- Archived source: `ttrpg_idealization_pre_reorganization_archive_2026-08-07/03_core_baseline_system/01_resolution_engine.md` (§7–8).
