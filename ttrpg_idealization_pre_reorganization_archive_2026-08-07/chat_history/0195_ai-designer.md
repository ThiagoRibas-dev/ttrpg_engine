---
turn: 195
role: "AI-Designer"
source: chat_history.json
---

# Turn 195 — AI-Designer

I recommend creating one new canonical glossary file and using it as the single authoritative home for these terms.

1. New Canonical File

Create:

text
03_core_baseline_system/00_baseline_framework_glossary.md

The 00_ prefix makes it easy to find before the numbered subsystem documents.

This file should define only framework terminology, not complete rules chapters.

Definitions to record there
Spell Slot Advancement

An entry on a Base Class or Prestige Class table granting one advancement toward the character’s shared Spell Slot Progression.

Spell Slot Progression Level

The character’s accumulated position on the Reference Good Slot Progression.

Reference Good Slot Progression

The universal Level 1–20 table that defines the shared Spell Slot pool.

Natural Pool

The pool produced by the character’s ordinary Attribute, Competency, Class, and other permanent factors before temporary enhancements.

Enhanced Pool

A pool modified by temporary or special sources such as:

Class features.
Feats.
Spells.
Equipment.
Circumstances.
Other permissions.
Requirement

A condition that must be satisfied before an action, spell, ability, or effect can be used.

Examples:

text
Requires Expert Death Tradition.
Requires a visible target.
Requires a weapon with Reach.
Permission

An explicit rule allowing an actor to perform something outside the ordinary baseline procedure.

Examples:

text
May cast as a Reaction.
May affect an immune target.
May choose one die result after rolling.
May target an additional creature.
Automatic Success

A success granted directly to the result rather than produced by a die. It counts toward required successes but is not affected by Boons, Banes, Die Step-Ups, Die Step-Downs, or opposed-roll tiebreaking.

Required Successes

The number in parentheses in a difficulty such as:

text
DC 9 (3)

This means:

text
Target Number 9
Requires 3 successful faces
Defender Wins Ties

The default opposed-contest rule: if the attacker and defender remain tied after all applicable tiebreak procedures, the defender succeeds.

Spell School

The technical classification of what a spell does.

Spell Tradition

The magical field governing access to and specialization in a spell.

Spell Trait

A practical descriptor governing delivery, interaction, targeting, or special behavior.

This glossary should also define the relationship between:

text
School
Tradition
Trait

without reprinting complete spellcasting rules.

2. Primary Canonical Rules File

Update:

text
03_core_baseline_system/01_resolution_engine.md

This remains the authoritative procedural document for the mathematical engine.

Add or revise sections covering:

Boon and Bane procedure
One-for-one Boon/Bane cancellation.
PF2e-inspired typed Boons.
Same-source effects do not stack.
Bane dice removal.
One-die Bane Die Step-Down.
d4 Step-Down automatic failure.
No further worsening after the single Bane-induced Die Step-Down.
Floor interaction.
Opposed checks
Highest-face comparison.
Secondary dice tiebreaking.
Defender Wins Ties.
Initiator as attacker and responding party as defender.
Contests that may explicitly end in a neutral tie.
Complex difficulties
DC X (Y) notation.
Counting required successes.
Interaction with Boons and Banes.
Interaction with Automatic Successes.
High-tier resolution
No d12+ notation.
Additional dice as a content-controlled enhancement.
Automatic Successes.
Higher required-success thresholds.
Requirements and Permissions.
Mythic continuation through effects, not larger ordinary dice.

The glossary should define terms; the Resolution Engine should explain how they operate.

3. Character Schema and Progression Files

Update only where these concepts are directly used.

03_core_baseline_system/02_character_schema_and_stats.md

Review and update:

Natural Pool.
Enhanced Pool.
Automatic Success.
Essence and Stamina interactions.
Maximum ordinary die size.

Do not duplicate full definitions. Link to the glossary.

03_core_baseline_system/05_leveling_and_tier_progression.md

Update:

Remove any remaining over-cap or d12+ language.
Link to Spell Slot Advancement and Spell Slot Progression Level.
Clarify that high-tier progression may grant Automatic Successes and Permissions rather than larger dice.
03_core_baseline_system/06_check_pool_generation_and_class_differentiation.md

Update:

Natural versus Enhanced Pools.
Pool volume beyond the normal range.
Automatic Successes as a separate vector from dice.
Removal of old over-cap terminology.
03_core_baseline_system/12_attacks_and_spells_vs_skills_architecture.md

Update:

Spell School / Tradition / Trait terminology.
Requirements and Permissions for attacks and spells.
Remove any remaining Mantle references.
03_core_baseline_system/13_building_block_domains_and_master_skill_system.md

Update:

Spellcasting references.
Spell Traits.
Tradition requirements and permissions.
Remove any remaining Mantle references.
4. Simulationist Subsystem Files
04_simulationist_subsystems/01_defenses_and_damage_modeling.md

Review:

Opposed defense ties.
Defender Wins Ties.
Automatic Successes in defensive checks.
High-tier defensive permissions.
Bane and Floor interactions.
04_simulationist_subsystems/02_skills_and_generic_capabilities.md

Review:

Natural and Enhanced Pools.
Competency Floors after Banes.
Skill-based Requirements.
Skill-based Permissions.
Automatic Successes from Legendary or special content.
04_simulationist_subsystems/03_resources_conditions_and_wounds.md

Review:

Die Step-Up and Die Step-Down resource interactions.
Conditions that alter pools, Floors, reactions, or permissions.
Ensure conditions do not use deprecated Hyper-Shift language.
5. Spellcasting and Progression Files
03_core_baseline_system/13_building_block_domains_and_master_skill_system.md

This remains the canonical home for:

Spell Schools.
Traditions.
Traits.
Essence.
Spell Slot Advancement.
Spell Slot Progression Level.
Shared Spell Slot progression.

The new glossary should link to this file for complete spellcasting rules.

02_comparative_system_analysis/spell_slot_progression_reference_derived.csv

No mathematical glossary definitions need to be added to the CSV. Its column names should remain clear:

text
Reference table:
  Spell Slot Progression Level

Derived tables:
  Character Level

The research catalogue should link to the canonical spellcasting document.

6. Decision Log

Update:

text
06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md

Add a new decision entry, probably:

text
DEC-056 — Baseline Framework Glossary and Resolution Vocabulary

This entry should record:

Establishment of the glossary.
Automatic Success terminology.
Requirement and Permission terminology.
Natural Pool and Enhanced Pool terminology.
DC X (Y) terminology.
Defender Wins Ties.
Universal Boon/Bane interaction.
Removal of deprecated over-cap notation from current rules.

The decision log should summarize the decision, not reproduce the glossary.

7. Outstanding Definitions Index

Update:

text
06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md

The index should:

Link to the new glossary.
Mark the relevant Phase 1 definitions as resolved.
Leave probability calibration open.
Leave content-specific Die Step-Up/Die Step-Down costs open.
Leave Mythic content implementation open.

It should not repeat all the glossary definitions.

8. Phase 1 Checklist

Update:

text
PHASE_1_CHECKLIST.md

Mark as completed once recorded:

 Create Baseline Framework Glossary.
 Formalize Boon/Bane stacking.
 Formalize opposed-roll ties.
 Formalize DC X (Y).
 Formalize Automatic Successes.
 Formalize Requirements and Permissions.
 Remove remaining active d12+ terminology.
 Remove remaining active Hyper-Shift terminology.

Leave as incomplete:

Probability calibration.
Equipment scaling.
Full Mythic framework.
Content-specific resource costs.
9. README

The README should only receive a navigation pointer:

text
The baseline mathematical vocabulary is defined in:

03_core_baseline_system/00_baseline_framework_glossary.md

It should not reproduce any of the definitions.

10. AGENTS.md

AGENTS.md
 already contains the single-source-of-truth rule, but it should gain one example:

Canonical vocabulary such as Automatic Success, Requirement, Permission, Natural Pool, Enhanced Pool, Spell Slot Advancement, and Defender Wins Ties must be defined in their authoritative canonical glossary or subsystem document, not duplicated in README, status files, decision logs, or research notes.

This reinforces the governance rule without turning 
AGENTS.md
 into a mechanics glossary.

Recommended Authority Structure
text
03_core_baseline_system/00_baseline_framework_glossary.md
  Defines framework terminology.

03_core_baseline_system/01_resolution_engine.md
  Defines universal resolution procedures.

03_core_baseline_system/13_building_block_domains_and_master_skill_system.md
  Defines spellcasting, Traditions, Skills, Domains, and progression structures.

06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md
  Records why and when decisions were made.

06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md
  Tracks whether definitions are Locked, Provisional, or Open.

PHASE_1_CHECKLIST.md
  Tracks completion work.

README.md
  Provides navigation only.

This preserves the single-source-of-truth rule while giving the Phase 1 framework a clear vocabulary reference.
