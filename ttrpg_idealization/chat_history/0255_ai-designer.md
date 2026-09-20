---
turn: 255
role: "AI-Designer"
source: chat_history.json
---

# Turn 255 — AI-Designer

used
Bash
83ms
Write
ttrpg_idealization/04_simulationist_subsystems/02_skills_and_generic_capabilities.md
69 lines
open
Generic Skill Capabilities
MD
Generic Skill Capabilities

Status: Canonical reference for generic skill capability gates and clocks.
Scope: Generic capability permissions, training gates, and task clocks. The canonical Skill and Activity taxonomy is maintained in ../03_core_baseline_system/09_domains_skills_activities_and_crafting.md.

1. Capability Gates

Some activities require a minimum Skill Competency, Attribute Die, tool, or Permission before they can be attempted.

Examples:

A delicate masterwork mechanism may require Master Thievery or a suitable specialist Permission.
A heavy portcullis may require an appropriate Athletics Competency, Attribute Die, leverage, or assistance.
A complex medical procedure may require suitable Anatomy and Healing Competency and tools.

A Requirement is recorded explicitly by the relevant Activity, Class, Feat, Equipment, or other content. This file does not create universal Attribute thresholds for individual activities.

2. Generic Activity Resolution

Use the following procedure:

Identify the Activity and the actor’s method.
Select the primary Skill from the canonical Domains and Skills document.
Identify any Requirements, Tools, assistance, or Permissions.
Build and resolve the check using ../03_core_baseline_system/01_resolution_engine.md.
Apply the Activity’s consequence, progress, or complication.

Additional Skills may establish separate stages, provide assistance, or change consequences. They do not automatically create linear numerical modifiers.

3. Complex Tasks and Clocks

Long or technically complex activities may use a progress clock. A clock defines:

The required number of successful stages.
The relevant DC or opposed procedure for each stage.
Time spent per attempt.
Consequences of failure.
Required tools, materials, or conditions.

The notation DC X (Y) is defined by the Resolution Engine. This file does not create a separate success-counting system.

4. Examples of Generic Capabilities

These are examples of capability categories, not finalized content:

Crafting and repair.
Research and investigation.
Wilderness travel and camp preparation.
Medical treatment.
Vehicle operation.
Lock and mechanism handling.
Document production and forgery.
Social negotiation.
Escape and restraint handling.

The exact Skill, Activity, Requirement, Tool, and Permission for each case belongs to the canonical Domains and Skills document or the relevant future content entry.

5. Source Links
Vocabulary and resolution: ../03_core_baseline_system/00_baseline_framework_glossary.md, ../03_core_baseline_system/01_resolution_engine.md
Attributes and derived statistics: ../03_core_baseline_system/02_attributes_and_derived_statistics.md
Skills, Domains, Activities, Lore, Knowledge, and Craft: ../03_core_baseline_system/09_domains_skills_activities_and_crafting.md
Character structure: ../03_core_baseline_system/03_character_schema_and_actor_creation.md
Conditions and resources: 03_resources_conditions_and_wounds.md
6. Current Scope Boundary

This file does not finalize individual Classes, Feats, Spells, Ancestries, Equipment, or detailed Activity catalogues. Open definitions remain tracked in the Outstanding Definitions Index.

Open
used
Bash
196ms

Completed the R13 cleanup pass.

Historical/deprecation references removed

Removed from canonical files:

Explicit Hyper-Shift deprecation notes.
Explicit Soak deprecation notes.
Explicit Focus-renaming notes.
[SET] references used only to explain that the mechanic was removed.
Historical-status wording from the canonical executive summary.

Canonical files now use the current terms directly:

text
Die Step-Up
Die Step-Down
Damage Absorption
Essence
Required Successes
Requirements
Permissions
Stale examples normalized

The outdated generic capability file was rewritten:

text
04_simulationist_subsystems/02_skills_and_generic_capabilities.md

It now contains only:

Capability gates.
Generic Activity resolution.
Requirements.
Tools.
Generic clocks.
Links to the canonical Skills/Domains and Resolution Engine files.

The obsolete examples using:

text
AGI
MIG
WIL
d10+
old tactical procedures

were removed.

Ownership issue resolved

The ownership problem was handled by making:

text
03_core_baseline_system/09_domains_skills_activities_and_crafting.md

the authority for:

Skills.
Domains.
Activities.
Procedures.
Craft.
Lore.
Knowledge.
Vehicle proficiencies.

The generic capabilities file now references that document instead of duplicating its taxonomy or procedures.

R13 status

Updated:

DOCUMENTATION_REFACTOR_PLAN.md
DOCUMENTATION_REFACTOR_AUDITS.md
DOCUMENTATION_REFACTOR_R13_REPORT.md

R13 is now marked complete.

The final active canonical scan found:

No [SET] references.
No Hyper-Shift references.
No d12+ references.
No obsolete AGI, MIG, or WIL examples.
No missing active Markdown links.

The Documentation Refactor is now complete through R13.
