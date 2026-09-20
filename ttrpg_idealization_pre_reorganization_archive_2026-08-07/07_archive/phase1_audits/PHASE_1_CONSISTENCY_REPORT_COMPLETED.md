# Phase 1 Checklist Consistency Report

**Scope:** Compare `PHASE_1_CHECKLIST.md` against the newly organized canonical rules in:

- `03_core_baseline_system/`
- `04_simulationist_subsystems/`

**Changes made:** None to canonical rules or the checklist.

## Overall Result

The checklist is broadly aligned with the reorganized canonical structure. Most completed items correspond to framework decisions that are represented in the canonical files, and the remaining `[~]` and `[ ]` items generally identify real open implementation or calibration work.

However, several items should be reviewed for precision. The most important issue is that the canonical Spell Slot Progression table is currently referenced by the Magic and Progression documents but is not visibly reproduced in either canonical file; it currently exists primarily in the CSV research/reference artifact.

---

## 1. Governance and Documentation

### Consistent

The checklist’s completed governance items are supported by:

- `AGENTS.md`
- `PROJECT_STATUS.md`
- The archived R0–R13 refactor package.
- `11_master_top_to_bottom_system_summary.md`

The checklist correctly identifies the documentation refactor as completed and the current work as post-refactor Phase 1 framework work.

### Minor issue

The checklist describes the canonical rules generally as being in `03_core_baseline_system/` and `04_simulationist_subsystems/`, which is correct. It should not enumerate individual canonical owners unless those links are maintained alongside future file moves.

---

## 2. Core Resolution Mathematics

### Consistent

The following completed checklist items are represented in `01_resolution_engine.md` and `00_baseline_framework_glossary.md`:

- `2dX keep highest` baseline.
- Fixed Target Numbers and DCs.
- Opposed rolls.
- Defender Wins Ties.
- `d4 → d6 → d8 → d10 → d12` ladder.
- Boon/Bane cancellation.
- Typed Boons.
- Same-source non-stacking.
- Bane die removal.
- One-die Bane Die-Down.
- d4 Bane automatic failure.
- Competency Floors.
- `DC X (Y)` notation.
- Multi-success resolution.
- Deprecated over-cap dice removal.
- Deprecated Hyper-Shift terminology removal.

### Items correctly still open or provisional

- Final Boon/Bane edge cases.
- Opposed-roll secondary tiebreak implementation and edge cases.
- Automatic Success sources and limits.
- Probability calibration.
- Content-specific Die Step-Up and Die Step-Down costs.

### Issue requiring review

The glossary says Banes may lower the effective Floor when reducing the final pool state, while the Resolution Engine says the Floor remains active but may be lowered. This is conceptually compatible but should eventually receive one precise procedural sentence.

---

## 3. Attributes and Actor Statistics

### Consistent

`02_attributes_and_derived_statistics.md` supports the checklist’s completed items concerning:

- Six Attributes.
- Attribute Dice.
- d12 ordinary ceiling.
- Paired defense derivations.
- Vitality, Stamina, and Essence as derived resource capacities.
- Background Primary Attribute and Secondary Attribute advancement references.

`03_character_schema_and_actor_creation.md` supports the Universal Actor Schema and the five actor building blocks.

### Items correctly still open or provisional

- Exact Attribute advancement edge cases.
- Exact resource capacity implementation and recovery.
- Equipment-derived durability and encumbrance.
- Detailed actor content.

### Minor issue

The checklist marks some resource derivation work as completed while the canonical Attributes file intentionally delegates detailed capacity and recovery procedures to the Resources subsystem. This is acceptable if “completed” means the derivation framework is established, but the checklist should distinguish:

```text
Capacity derivation established
versus
Resource procedures finalized
```

---

## 4. Skills, Domains, and Competency

### Consistent

`09_domains_skills_activities_and_crafting.md` supports the checklist’s completed framework items:

- Eight Domains.
- Individual Skills.
- Lore.
- Knowledge.
- Craft specialties.
- Activities and Procedures.
- Tools and vehicle proficiencies.
- Investigation, Forgery, Disguise, Escape Artistry, and related tasks as Activities rather than universal Skills.

`07_check_pool_generation_and_class_differentiation.md` supports the separation between:

- Attribute Die Size.
- Pool Volume.
- Competency Floor.
- Class and content differentiation.

### Items correctly still open or provisional

- Final Craft specialty behavior.
- Final Lore scope and ranking.
- Detailed Activity procedures.
- Domain-level mechanics.
- Complete skill and specialty catalogues.

No significant checklist inconsistency was found in this area.

---

## 5. Character Advancement

### Consistent

`06_leveling_and_tier_progression.md` supports the checklist’s completed items concerning:

- Levels 1–20.
- The five mortal High Fantasy Tiers.
- Mythic as Level 21+.
- Classes and Prestige Classes.
- Level-by-level class tables.
- Spell Slot Advancement.
- Spell Slot Progression Level.
- Mythic remaining bounded and deferred.

### Issue requiring review

The checklist and canonical progression document agree that Spell Slot Advancement and Spell Slot Progression are established, but the actual Reference Good Slot Progression table is not currently present in `06_leveling_and_tier_progression.md`.

The table is represented in:

```text
02_comparative_system_analysis/spell_slot_progression_reference_derived.csv
```

and is referenced conceptually by the Magic document. Since the slot table is a player-facing framework rather than merely research, the canonical owner should eventually contain the authoritative table or explicitly link to a canonical table file.

This is the most important consistency gap found in the audit.

---

## 6. Action, Movement, and Spatial Rules

### Consistent

`04_action_economy_and_turn_structure.md` supports:

- Three-action turns.
- Reactions.
- Free Guard.
- Action categories.
- Repeated-action fatigue as a framework.

`05_spatial_and_distance_engine.md` supports:

- Five Distance Tiers.
- Exact and abstract modes.
- Stride.
- Reach.
- Range.
- Movement modes.
- Spatial Requirements and Permissions.

### Items correctly still open

- Detailed repeated-action fatigue.
- Equipment movement effects.
- Spell-specific Areas of Effect.
- Condition-specific action restrictions.

No major inconsistency was found.

---

## 7. Combat, Defenses, Damage, and Wounds

### Consistent

`04_simulationist_subsystems/01_defenses_and_damage_modeling.md` supports the completed framework items concerning:

- Layered defenses.
- Reflexes.
- Parry.
- Fortitude.
- Willpower.
- Damage Absorption.
- Natural Criticals.
- Called Shots.
- Anatomical Wounds.
- Rabble and Underlings.

`03_resources_conditions_and_wounds.md` supports the resource, Condition, and recovery framework.

### Correctly still open

- Final damage-versus-Damage Absorption calibration.
- Weapon Damage Dice.
- Armor and shield interaction.
- Wound severity and treatment.
- Combat time-to-defeat calibration.
- Exact resource costs.

No major checklist inconsistency was found.

---

## 8. Equipment and Economic Scaffolding

### Consistent

The checklist correctly leaves most equipment work incomplete. `12_equipment_durability_and_economy.md` explicitly functions as an ownership scaffold rather than a finished rules document.

Correctly incomplete items include:

- Weapons.
- Armor.
- Shields.
- Durability Slots.
- Magical and special materials.
- Crafting and repair.
- Wealth and equipment bands.
- Wealth-by-level guidance.

No inconsistency was found.

---

## 9. Magic and Spellcasting

### Consistent

`10_magic_schools_traditions_and_spellcasting.md` supports the completed framework items concerning:

- Eight Schools.
- Traditions.
- Traits.
- Fixed Tradition spell lists.
- Tradition access through Classes and Prestige Classes.
- Universal preparation.
- Shared Spell Slots.
- Spell Slot Progression references.
- Tradition Competency and intrinsic scaling.
- Essence.
- Psychic/Psionic power as provisional and separate.

### Correctly still open

- Preparation limits.
- Learned-spell limits.
- Acquisition stacking.
- Detailed Essence procedures.
- Heightening.
- 0th-Circle/Essence interaction.
- Psychic/Psionic mechanics.
- Mythic magic.
- Individual spells.

### Issue requiring review

The Magic document references the Spell Slot Progression table but does not contain the full table. This is the same canonical-ownership gap identified in the Advancement section.

---

## 10. Conversion Framework

The checklist correctly identifies:

- D&D 3.5e as the foremost compatibility target.
- Other systems as conversion or reference targets.
- Conversion procedures as separate from canonical rules.

The converted reference files moved during the documentation refactor are correctly outside the canonical core directory.

No major inconsistency was found.

---

## 11. Recommended Checklist Adjustments

The checklist is mostly accurate, but the following wording improvements would make it more precise:

1. Change resource-related “completed” items to distinguish capacity derivation from expenditure/recovery procedures.
2. Add a specific open task for placing the Reference Good Slot Progression table in its canonical home.
3. Add a specific cross-reference task ensuring the Magic document and Progression document point to that canonical table.
4. Clarify that Automatic Success is a framework concept, while its sources and limits remain open.
5. Clarify that completed Skill and Domain architecture does not mean the detailed content catalogues are complete.

## Final Assessment

The Phase 1 Checklist is broadly consistent with the reorganized canonical rules. The only substantial structural gap is the missing canonical home for the Reference Good Slot Progression table. Most other differences are appropriate distinctions between:

- Framework established.
- Procedure finalized.
- Content deferred.
- Calibration still open.

No changes were made during this audit.
