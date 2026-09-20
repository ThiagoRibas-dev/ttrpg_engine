---
turn: 197
role: "AI-Designer"
source: chat_history.json
---

# Turn 197 — AI-Designer

Write
ttrpg_idealization/03_core_baseline_system/00_baseline_framework_glossary.md
137 lines
open
Baseline Framework Glossary
MD
Baseline Framework Glossary

Status: Canonical framework vocabulary
Decision: DEC-056

This document defines shared terms used across the baseline framework. It does not replace the procedural rules in the relevant subsystem documents.

Resolution Vocabulary
Natural Pool

The check pool produced by the actor's ordinary Attribute, Competency, Class, and other persistent factors before temporary or special enhancements are applied.

Enhanced Pool

A Natural Pool modified by temporary or special sources such as feats, spells, equipment, circumstances, class features, or other explicit effects.

Die Step-Up

An increase in die size along the ordinary ladder:

text
d4 → d6 → d8 → d10 → d12
Die Step-Down

A decrease in die size along the ordinary ladder:

text
d12 → d10 → d8 → d6 → d4

The former Hyper-Shift terminology is deprecated.

Boon

A final-pool effect that adds one die of the same size after ordinary pool construction and after applicable Die Step-Ups and Die Step-Downs. Boons use typed stacking rules. Boons from the same named source do not stack with one another.

Bane

A final-pool effect that removes one die after ordinary pool construction and after applicable Die Step-Ups and Die Step-Downs. Banes from the same named source do not stack with one another.

If a Bane is applied to a one-die pool, it causes one Die Step-Down instead. Further Banes do not cause additional Die Step-Downs. If a d4 would be stepped down by this rule, the check is an automatic failure.

Competency Floor

The minimum result imposed by a character's Competency Rank. Banes may reduce the effective Floor when they reduce the final pool state, but a Floor remains active after pool reduction.

Automatic Success

A success granted directly by an effect rather than produced by a die. An Automatic Success counts toward the required-success total but is not a die and is not affected by Boons, Banes, Die Step-Ups, Die Step-Downs, or opposed-roll tiebreaking.

Requirement

A condition that must be satisfied before an action, spell, ability, or effect can be used.

Examples:

text
Requires Expert Death Tradition.
Requires a visible target.
Requires a weapon with the Reach Trait.
Permission

An explicit rule allowing an actor to perform something outside the ordinary baseline procedure.

Examples:

text
May cast as a Reaction.
May affect an immune target.
May choose one die result after rolling.
May affect an additional creature.
Required Successes

The number of successful faces required by a complex difficulty. A difficulty written as:

text
DC 9 (3)

means Target Number 9 and three required successes. Each die face meeting or exceeding 9 counts as one success.

Defender Wins Ties

The default opposed-contest rule. After comparing the highest faces and all applicable secondary dice, the defender wins if the results remain tied.

The party that initiates an opposed contest is the attacker for that contest; the responding party is the defender. Some contests, such as races, may explicitly allow a neutral tie instead of requiring a victor.

Spellcasting Vocabulary
Spell School

The technical classification of what a spell does. The baseline system preserves the eight traditional D&D-compatible Schools:

Abjuration
Conjuration
Divination
Enchantment
Evocation
Illusion
Necromancy
Transmutation
Spell Tradition

A magical field governing access to and specialization in a spell. A spell may belong to multiple Traditions. Classes and Prestige Classes grant access to Tradition Skills; Traditions have fixed shared spell lists.

Spell Trait

A practical descriptor governing a spell's delivery, interaction, targeting, or special behavior.

Spell Slot Advancement

An entry on a Base Class or Prestige Class table granting one advancement toward the character's shared Spell Slot Progression.

Spell Slot Progression Level

The character's accumulated position on the Reference Good Slot Progression.

Reference Good Slot Progression

The universal table showing the shared daily Spell Slot pool at Spell Slot Progression Levels 1–20.

Governance Note

This glossary defines vocabulary only. Complete procedures belong in the relevant canonical subsystem documents, especially:

01_resolution_engine.md
02_character_schema_and_stats.md
13_building_block_domains_and_master_skill_system.md
Open
used
Bash
157ms
Edit
ttrpg_idealization/03_core_baseline_system/02_character_schema_and_stats.md
02_character_schema_and_stats.md
MD

Recorded.

Created canonical glossary
text
03_core_baseline_system/00_baseline_framework_glossary.md

It now defines:

Natural Pool.
Enhanced Pool.
Die Step-Up.
Die Step-Down.
Boon.
Bane.
Competency Floor.
Automatic Success.
Requirement.
Permission.
Required Successes.
Defender Wins Ties.
Spell School.
Spell Tradition.
Spell Trait.
Spell Slot Advancement.
Spell Slot Progression Level.
Reference Good Slot Progression.
Updated related documents

03_core_baseline_system/01_resolution_engine.md

Added a glossary cross-reference.

03_core_baseline_system/02_character_schema_and_stats.md

Added a glossary cross-reference.

README.md

Added a pointer to the canonical glossary.

AGENTS.md

Added the glossary to the single-source-of-truth guidance.

06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md

Added DEC-056.

06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md

Added OD-004A — Baseline Framework Glossary as resolved.

PHASE_1_CHECKLIST.md

Marked the glossary task completed.

The glossary is now the canonical vocabulary reference, while the subsystem documents remain responsible for the actual procedures.
