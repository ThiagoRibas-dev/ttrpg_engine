---
turn: 167
role: "AI-Designer"
source: chat_history.json
---

# Turn 167 — AI-Designer

Not explicitly enough.

The current state is implied across several places:

README.md describes the workspace and roadmap.
06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md tracks unresolved definitions.
06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md records decisions and next steps.
The canonical files contain the current framework.

However, we do not currently have a dedicated, authoritative project-status record stating:

We are still designing the foundational framework and are not yet developing or locking specific classes, feats, spells, ancestries, or other final content.

That distinction is important and deserves its own status document or explicit status section.

Recommended Status Record

I suggest creating:

text
06_brainstorming_logs_and_roadmap/04_current_project_status.md

Its purpose would be to track the project phase over time without duplicating rules.

It could contain:

Current Phase
text
Phase 1 — Foundational Framework and Scaffolding
Current Focus
Core resolution engine.
Attributes and derived statistics.
Competency Ranks.
Domains, Skills, Activities, and Specialties.
Action economy.
Defenses, Damage Absorption, wounds, and conditions.
Resources and recovery.
Class advancement architecture.
Spellcasting architecture and Spell Slot Progression.
Universal Actor Schema.
Conversion framework.
Document governance and canonical organization.
Explicitly Not Yet in Scope

The project is not yet actively designing or locking:

Complete Base Classes.
Prestige Classes as finalized content.
Feat compendia.
Spell compendia.
Ancestry compendia.
Complete monster or NPC rosters.
Finished equipment catalogs.
Final adventure content.
Complete Psychic/Psionic rules.
Full balance calibration for all content categories.

Classes, feats, spells, and ancestries may be referenced as examples or future implementation targets, but those references do not constitute finalized content decisions.

Exit Criteria for the Current Phase

The framework phase would be complete when:

Core resolution is stable.
Character and actor schemas are stable.
Skill and Domain architecture is stable.
Action and defense systems are stable.
Resource systems are stable.
Advancement and multiclassing are stable.
Spellcasting scaffolding is stable.
Major outstanding framework definitions are resolved.
Canonical documents have undergone a consistency audit.
Update Protocol

The status document should be updated when:

The project moves to a new design phase.
A major framework subsystem is completed.
The scope changes.
Content development formally begins.
A previously provisional subsystem becomes canonical.
A major area is explicitly deferred.

I would keep this out of 
AGENTS.md
, because 
AGENTS.md
 is intentionally a process and governance document rather than a project-state document. The status document should be linked from the README and the Outstanding Definitions Index, while the README itself should only point to it rather than duplicate its contents.
