---
turn: 223
role: "AI-Designer"
source: chat_history.json
---

# Turn 223 — AI-Designer

Your decisions establish the direction for the remaining R1/R2 work. One naming/ownership point remains ambiguous: the current 12_attacks_and_spells_vs_skills_architecture.md.

Summary
Should the current attacks/spells architecture become a canonical statistical-framework file?
Move that one to the research folder and let's create a document that deals specifically with the system's statistical framework based on the other documents that define attributes, defenses, DCs, skills, combat, spells, etc.
Ran commands
4

Completed the approved R1/R2 organizational work.

Moved to reference/research storage

These are no longer treated as canonical rules:

text
08_sources_of_progression_and_conceptual_mapping.md
09_dnd_3_5e_class_advancement_tracks_mapping.md
11_check_pool_architecture_comparative_matrix.md
12_attacks_and_spells_vs_skills_architecture.md

They now reside under:

text
02_comparative_system_analysis/archived_core_reference/

A README was added there explaining their reference-only status.

Created canonical statistical-framework file

Created:

text
03_core_baseline_system/08_statistical_framework_and_check_modes.md

This is currently a canonical scaffold for:

Attribute and Competency pool relationships.
Fixed-DC checks.
Complex difficulties.
Opposed checks.
Attack and defense pool relationships.
Spell and skill check relationships.
The bounded d12/DC 12 model.

It does not create new rules or resolve open probability questions.

Split the former building-block document

The former:

text
13_building_block_domains_and_master_skill_system.md

was split into:

text
03_core_baseline_system/09_domains_skills_activities_and_crafting.md
03_core_baseline_system/10_magic_schools_traditions_and_spellcasting.md

The Magic document now references the Domains, Skills, Activities, and Crafting document rather than duplicating its structure.

Reordered executive summary

Renamed:

text
10_master_top_to_bottom_system_summary.md

to:

text
11_master_top_to_bottom_system_summary.md
Current core ordering
text
00 Baseline Framework Glossary
01 Resolution Engine
02 Attributes and Derived Statistics
03 Character Schema and Actor Creation
04 Action Economy and Turn Structure
05 Spatial and Distance Engine
06 Leveling and Tier Progression
07 Check-Pool Generation and Class Differentiation
08 Statistical Framework and Check Modes
09 Domains, Skills, Activities, and Crafting
10 Magic Schools, Traditions, and Spellcasting
11 Master System Summary

References, README navigation, the inventory, the refactor plan, and the audit records were updated accordingly.

No game mechanics were changed. Further content consolidation and rule-definition work remain separate tasks.
