---
turn: 233
role: "AI-Designer"
source: chat_history.json
---

# Turn 233 — AI-Designer

Explored
2 reads
Read
02_attributes_and_derived_statistics.md
Read
03_character_schema_and_actor_creation.md
Canonical Glossary Consistency Report — Expanded Findings

Scope checked:

text
03_core_baseline_system/
04_simulationist_subsystems/

Changes made: None.

The audit confirms that the glossary is current, but several canonical files still contain duplicated or superseded content. The main issue is now structural rather than merely terminological.

1. 01_resolution_engine.md
Major procedural conflicts
Bane table is obsolete

The file still contains the older model:

text
-1 Bane → 1dX
-2 Banes → 2dX keep lowest
-3 Banes → 3dX keep lowest

This conflicts with the current canonical rule:

text
Each Bane removes one die.

If only one die remains:
  One Bane causes one Die Step-Down.

Further Banes:
  No additional worsening.
Floor interaction is inconsistent

The appended DEC-055 section says:

Banes clip the pool ceiling but do not remove the Floor.

The current approved interpretation is:

The Floor remains active as a concept.
A Bane may lower the effective Floor after reducing the final pool state.

The wording needs to distinguish:

text
Floor remains part of the check

from:

text
Floor value cannot be lowered
[SET] mechanics remain active

The file still uses [SET] tokens for:

Extra successes.
Maneuver resolution.
Complex task outcomes.
Historical combat examples.

Those procedures need to be replaced with:

Required Successes.
Automatic Successes.
Explicit Permissions.
Class, Feat, or Equipment effects.
Old resource terminology remains

The Die Step-Up section still refers to:

text
Focus

The canonical resource is:

text
Essence
Old Damage Absorption terminology remains

The Bypass Absorption example still uses:

text
Soak 0

The current term is:

text
No Damage Absorption
Ownership recommendation

This file should remain the sole owner of universal:

Pool construction.
Boons and Banes.
DCs.
Required Successes.
Opposed checks.
Tiebreaks.
Automatic Successes.
Requirements and Permissions.
2. 02_attributes_and_derived_statistics.md

This file is now in the correct structural location, but it still contains old and duplicated mechanics.

Terminology conflicts

Still uses:

text
Soak Rank
Focus

These should eventually become:

text
Damage Absorption
Essence
Duplicated defense rules

This file contains a complete four-layer defense model, including:

Reflexes.
Parry.
Fortitude.
Willpower.
Soak/Damage Absorption.

That duplicates material belonging to:

text
04_simulationist_subsystems/01_defenses_and_damage_modeling.md

Recommended future division:

02_attributes_and_derived_statistics.md
Owns derivations.
Explains how Reflexes, Fortitude, and Willpower are calculated.
Defense subsystem
Owns what each defense does.
Owns attack targeting.
Owns Parry.
Owns Damage Absorption.
Owns defense procedures.
Duplicated resource rules

This file contains complete rules for:

Vitality.
Stamina.
Focus.
Vancian casting.
Concentration.
Metamagic.
Durability.
Sunder.

Most of that belongs elsewhere.

Recommended future division:

02_attributes_and_derived_statistics.md
Defines how resource capacities are derived.
04_simulationist_subsystems/03_resources_conditions_and_wounds.md
Defines resource expenditure and recovery.
Equipment owner
Defines Durability and Sunder.
Magic owner
Defines Essence, spell slots, concentration, and metamagic.
3. 03_character_schema_and_actor_creation.md

This file remains substantially duplicated and historically stale.

Duplicated Attributes

It repeats the complete six-Attribute definitions already owned by:

text
02_attributes_and_derived_statistics.md
Old Domain Architecture

It still presents the former five Domain Umbrellas, including old skill groupings such as:

Lockpicking.
Trap Disarming.
Sailing/Piloting.
Old Lore/Crafting structure.
Old Social structure.

This conflicts with the current eight-Domain model owned by the new Domains file.

Old Defense Terminology

It still uses:

text
Soak Rank

and duplicates defense derivations and procedures.

Old Resource Terminology

It still uses:

text
Focus

rather than Essence.

Old Actor Schema

It describes a four-block schema:

text
Race + Class + Skills + Feats

The current schema is:

text
Race/Ancestry
Background/Origin
Class/Prestige Classes
Skills
Feats
Old Attributes

Examples still use:

text
MIG
AGI

instead of:

text
STR
DEX
Old [SET] content

The actor and feat examples still mention [SET] triggers.

Ownership recommendation

This file should eventually focus only on:

Universal Actor Schema.
Character record structure.
Building-block relationships.
PC/NPC/monster application.

It should link outward for Attributes, Skills, Combat, Resources, and Magic.

4. 04_action_economy_and_turn_structure.md
Terminology conflicts

Still uses:

text
Soak Rank

for armor-related effects.

Procedure duplication

It contains effects that should belong to:

Defense and Damage Absorption.
Equipment and Durability.
Conditions and Resources.

The Action Economy file should own:

Actions.
Reactions.
Free Guard.
Multiple attacks.
Full Defense.
Action costs.

It should link outward for the effects of armor, shields, conditions, and wounds.

5. 05_spatial_and_distance_engine.md

This file is comparatively clean.

Potential ambiguity

It uses “Shift” for spatial movement:

text
Shift one Distance Tier
Tier Shift Down
Tier Shift Up

This is not inherently wrong, but it should be clearly distinguished from:

text
Die Step-Up
Die Step-Down

A future consistency edit should standardize spatial phrasing, perhaps using:

text
Move one Distance Tier

where practical.

6. 06_leveling_and_tier_progression.md
Legacy terminology

Still contains:

text
Focus
Soak
[SET]
over-cap d12
Duplicated progression rules

This file contains material that overlaps with:

Attribute advancement.
Competency advancement.
Spell Slot Progression.
Resource progression.
Class advancement.

The final ownership should be clarified:

Level/Tier file owns level milestones and tier structure.
Attribute file owns Attribute advancement.
Class tables own class-specific advancement.
Spell Slot Progression belongs either here or in the Magic framework.
Resource procedures belong in the Resource subsystem.
Historical examples

Several examples still present older mechanics as if current:

[SET] tokens.
Focus progression.
Over-cap dice.
Old Domain advancement language.

These should eventually be labeled historical or rewritten.

7. 07_check_pool_generation_and_class_differentiation.md

This file is in the correct structural position but duplicates the Resolution Engine.

Duplicated rules

It repeats:

Attribute-to-die-size logic.
Competency-to-pool logic.
Step effects.
Pool ceilings.
Example check construction.

The final ownership should be:

Resolution Engine owns how a pool is resolved.
Attribute file owns Attribute Dice.
This file owns the statistical relationship between:
Attributes.
Competency.
Class.
Pool volume.
Class differentiation.
Legacy examples

Some examples still use:

text
over-cap
d12+
Hyper-Shift

or equivalent older concepts.

8. 08_statistical_framework_and_check_modes.md

This new file is appropriately positioned, but currently acts only as a scaffold.

Current status

It correctly points to:

Resolution Engine.
Attributes.
Combat.
Domains.
Magic.
Pending work

It should eventually consolidate, without duplicating procedures:

Fixed DC versus opposed checks.
Attack versus defense statistical relationships.
Required Successes.
Pool-size expectations.
The bounded d12/DC 12 model.
The role of Automatic Successes.
Probability-calibration references.

It should not become a second Resolution Engine.

9. 09_domains_skills_activities_and_crafting.md

This is structurally correct as the future owner, but inherited historical content remains.

Current conflicts

The file still contains:

The old five-umbrella matrix.
Historical 65-skill material.
Old Path terminology.
Old Focus references.
Old class examples.
Historical option architecture.
Recommended consolidation

Keep:

Current eight Domains.
Current Skills.
Lore.
Knowledge.
Craft.
Activities.
Procedures.
Tools.
Vehicle proficiencies.

Move or label:

Old five-umbrella model.
Historical 65-skill matrix references.
SotDL Path architecture.
Deprecated class examples.
10. 10_magic_schools_traditions_and_spellcasting.md

This is now the correct structural owner for magic, but the split inherited some outdated material.

Terminology conflicts

Still uses:

text
Focus

in the provisional Psychic/Psionic discussion.

The current term is:

text
Essence
Architecture status

The file correctly reflects:

Schools.
Traditions.
Traits.
Shared spell lists.
Shared Spell Slots.
Spell Slot Advancement.
Spell Slot Progression Level.
Universal preparation.

However, it also contains some historical language about:

Paths.
Prestige Paths.
Older profile models.
Earlier Tradition access models.

Those should be labeled historical or removed from the active canonical sections.

11. 11_master_top_to_bottom_system_summary.md

This file currently duplicates too much of the entire ruleset.

It contains old versions of:

Core resolution.
Attributes.
Defenses.
Resources.
Skills.
[SET].
Soak.
Focus.
Over-cap terminology.
Old class and path assumptions.
Recommended future role

Reduce it to:

One-page or short executive overview.
A subsystem map.
Links to canonical owners.
No independent numerical procedures.
No duplicate tables.
No independent examples that can drift from the rules.

This should be one of the highest-priority consolidation tasks after the Attribute and Resolution files.

12. Simulationist Subsystems
04_simulationist_subsystems/01_defenses_and_damage_modeling.md

This should own:

What Reflexes, Parry, Fortitude, and Willpower do.
Damage Absorption.
Damage-versus-Absorption.
Natural Criticals.
Called Shots.
Anatomical wounds.

It should not redefine how general opposed rolls or Boons/Banes work.

04_simulationist_subsystems/02_skills_and_generic_capabilities.md

This currently overlaps with the Domains file.

It should eventually own:

Generic skill procedure guidance.
Skill-gated capability rules.
Training requirements.
Complex task procedures.
Crafting clocks, if those remain generic.

It should link to the Domains file for the actual Skill list.

04_simulationist_subsystems/03_resources_conditions_and_wounds.md

This currently overlaps with:

Attribute derivations.
Character schema.
Defense and Damage Absorption.
Magic and Focus/Essence.

It should eventually own:

Resource expenditure.
Resource recovery.
Conditions.
Wound consequences.
Recovery and treatment.

It should not redefine resource capacity formulas.

13. Most Important Conflicts to Resolve First

The highest-priority consolidation targets are:

01_resolution_engine.md

Old Bane table.
[SET].
Floor/Bane wording.
Focus.
Soak.

02_attributes_and_derived_statistics.md

Duplicated defense, resource, and equipment rules.

03_character_schema_and_actor_creation.md

Old schema.
Old Domains.
Old Attributes.
Old resources.
Old terminology.

06_leveling_and_tier_progression.md

Old over-cap values.
Old progression vectors.
Old Focus and [SET].

11_master_top_to_bottom_system_summary.md

Broad duplication of nearly every subsystem.

09_domains_skills_activities_and_crafting.md

Current and historical skill systems mixed together.
Overall Result

The current canonical set is structurally improved after the R1/R2 moves, but it is not yet internally synchronized.

The main issue is not that the glossary is unclear. The issue is that several canonical files still function as older, parallel versions of the rules.

The next consolidation phase should therefore begin with:

text
R3 — Attributes and Derived Statistics Consolidation

and should:

Move derived-stat authority into 02.
Reduce Character Schema to actor structure in 03.
Remove duplicated Attribute, Defense, Resource, and Equipment procedures.
Preserve unresolved questions by linking to the Outstanding Definitions Index.
Record the focused R3 audit afterward.

No changes were made during this report.
