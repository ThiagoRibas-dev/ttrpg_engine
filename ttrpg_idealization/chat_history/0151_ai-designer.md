---
turn: 151
role: "AI-Designer"
source: chat_history.json
---

# Turn 151 — AI-Designer

used
Bash
91ms

An 
AGENTS.md
 should function as a project constitution and handoff guide. It should allow a new agent—or a future version of us—to understand the project’s current state without reconstructing the entire conversation.

It should not become another giant design document. Its job is to explain:

What the project is.
Which decisions are canonical.
Which documents are authoritative.
Which questions remain open.
How future design work should be conducted.
Which terminology and constraints must never be violated.
Main Considerations
1. Make it operational, not encyclopedic

The file should answer:

What should an agent do first?
Which files should it read?
What rules are locked?
What decisions are still open?
How should new decisions be recorded?
What should happen before changing canonical rules?

It should avoid duplicating entire rules systems. Instead, it should link to canonical documents.

2. Establish document authority

The project now has several document categories:

Canonical rules

Current rules and architecture.

Primary locations:

text
03_core_baseline_system/
04_simulationist_subsystems/
Research and comparative analysis

Inspiration, mathematical investigation, simulations, and reference-system studies.

Primary locations:

text
01_design_philosophy_and_pillars/
02_comparative_system_analysis/
Conversion and content procedures

Rules for converting D&D, PF2e, SotDL/WW, Mythras, and other material.

text
05_conversion_and_content_engine/
Discussion and decision history

Brainstorming logs, decision records, and outstanding issues.

text
06_brainstorming_logs_and_roadmap/
Archive

Deprecated and historical documents.

text
07_archive/

The 
AGENTS.md
 should explicitly state:

Archived or historical documents must not override canonical rules.

3. Record design constraints prominently

The most important constraints should appear near the beginning:

Zero table-side arithmetic.
No linear modifiers.
No meta-currencies.
Universal Actor Schema.
Six Attributes.
Competency Ranks independent from Character Level.
Three-action economy.
High Fantasy Tier structure.
In-world resource tracks.
Exact terminology for Die Step-Up, Die Step-Down, Boons, and Banes.

These constraints are more important than any individual subsystem because they prevent future design drift.

4. Summarize canonical architectural decisions

The file should contain a compact decision summary, not every detail.

Important current decisions include:

Resolution
2dX keep highest baseline.
Fixed DCs.
Opposed rolls.
Boons and Banes.
Competency Floors.
Multi-success outcomes.
Natural Crits versus Called Shots.
Character structure
text
Race/Ancestry
Background/Origin
Class and Prestige Classes
Skills
Feats
Skills
Domains are game entities.
Skills represent transferable domains.
Activities and procedures are not automatically skills.
Lore is open-ended.
Knowledge is formal and technical.
Craft uses specialties.
Magic Traditions are individual skills.
Magic
Eight D&D-compatible Schools.
Modular Traditions.
Ardent-inspired Mantles.
Practical Spell Traits.
Fixed spell list per Tradition.
Classes grant Tradition access rather than class-owned spell lists.
Alchemy is Knowledge/Craft, not a magical Tradition.
Psychic/Psionic power is provisionally separate and Essence-based.
Spell slots
Shared daily Spell Slot pool.
Reference Good Slot Progression.
Spell Slot Advancement shown level by level in class tables.
Multiclassing adds all completed Spell Slot Advancements.
Tradition Competency controls spell access and intrinsic scaling.
Mythic adds Epic Traditions and Spells rather than ordinary new slot rows.
5. Clearly distinguish locked, provisional, and open decisions

Every significant decision should have one of three statuses:

Locked

The architecture should not be changed casually.

Example:

text
DEC-051 — Unified Tradition Spellcasting and Multiclassing
DEC-052 — Spellcasting Progression Level and Shared Slot Table
Provisional

The direction is accepted, but implementation or balance remains open.

Example:

text
Psychic/Psionic power as a separate Essence-based system.
Open

The design must still be discussed before implementation.

Example:

text
OD-001B — Preparation and Learned-Spell Limits
OD-001C — Acquisition Stacking and Multiclassing
OD-001D — Essence Expenditure and Casting Stability

The 
AGENTS.md
 should direct agents to consult:

text
06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md

before beginning new architectural work.

6. Include a decision-making protocol

The file should tell future agents how to handle new design proposals.

Recommended process:

Identify which existing decision or subsystem the proposal affects.
Search the workspace for relevant terms and older options.
Check the Outstanding Definitions Index.
Compare at least two viable alternatives when the issue is architectural.
Identify compatibility, complexity, balance, and conversion consequences.
Present the trade-offs before locking a major decision.
Once approved, update:
The canonical rule document.
The decision log.
The Outstanding Definitions Index.
Any affected research or conversion documents.
The README if the project structure or top-level architecture changes.
Mark superseded documents or sections as historical instead of deleting useful design history.
7. Prevent stale-document drift

This is especially important because the project has evolved substantially.

The file should instruct agents to look for:

Old terminology.
Deprecated mechanics.
Sections still presenting locked choices as open.
References to archived files.
Duplicate “canonical” summaries.
Contradictory slot tables.
Old skill taxonomies.
References to removed meta-currencies or tokens.

A useful rule:

If a document contains an old option comparison, it must be labeled as historical or comparative unless that option remains genuinely open.

8. Provide a recommended reading order

A new agent should not read every file immediately.

Suggested order:

text
1. README.md
2. 06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md
3. 06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md
4. 03_core_baseline_system/10_master_top_to_bottom_system_summary.md
5. Relevant canonical subsystem document
6. Relevant comparative or conversion documents

For current magic work:

text
1. 03_core_baseline_system/13_building_block_domains_and_master_skill_system.md
2. 03_core_baseline_system/12_attacks_and_spells_vs_skills_architecture.md
3. 02_comparative_system_analysis/08_shared_spell_slot_progression_comparative_catalog.md
4. 02_comparative_system_analysis/spell_slot_progression_reference_derived.csv
5. OD-001B, OD-001C, or OD-001D in the outstanding-definitions index
9. Define terminology rules

The file should include a short terminology section.

Examples:

Use:

Die Step-Up
Die Step-Down
Up-Shift
Down-Shift
Damage Absorption
Spell Slot Advancement
Spell Slot Progression Level
Spell Circle
Essence
Competency Rank
Tradition Skill

Avoid or flag:

Hyper-Shift
Downshift
Soak, when referring to the canonical Damage Absorption mechanic.
Focus, when referring to the renamed magical resource.
Caster Level, unless explicitly discussing a reference system.
Paths, when the current terminology is Class and Prestige Classes.
Generic “spell list,” when referring to the canonical fixed Tradition lists.
10. Include file-editing expectations

The agent should know that design work is expected to be recorded, not merely discussed.

For every approved major decision:

text
Canonical rule:
  Update the relevant canonical file.

Decision history:
  Add a DEC entry to the master brainstorm log.

Outstanding index:
  Mark the question resolved or update its remaining subquestions.

Research:
  Add comparative artifacts to the relevant research directory.

Archive:
  Move superseded documents rather than leaving them beside canonical files.

README:
  Update only when top-level architecture or navigation changes.
11. Include simulation and validation rules

The project relies heavily on mathematical calibration even though table-side play is mathless.

The 
AGENTS.md
 should tell future agents to:

Use Python simulations for probability-sensitive mechanics.
Keep simulation scripts in the brainstorming or research area.
Record assumptions and outputs.
Never treat an untested probability claim as canonical.
Test:
Time to defeat.
Slot volume.
Resource depletion.
Multi-success frequency.
Crit frequency.
Full/partial/bad class comparison.
Multiclass edge cases.
Spell access and acquisition exploits.
12. Include the current roadmap

The roadmap should be short and dynamic. At present it should identify:

OD-001B — Preparation and learned-spell limits.
OD-001C — Acquisition stacking and multiclass acquisition.
OD-001D — Essence expenditure and casting stability.
Magic Tradition and spell compendium.
Core feat compendium.
Character creation walkthroughs.
Monster and NPC construction.
Canonical consistency audit.
Recommended 
AGENTS.md
 Structure
text
# AGENTS.md

## Project Identity
## Operating Principles
## Canonical Sources of Truth
## Current Canonical Architecture
## Locked Decisions
## Provisional Decisions
## Open Definitions
## Terminology Rules
## Design Workflow
## Decision-Recording Workflow
## Research and Simulation Standards
## File Organization
## Recommended Reading Order
## Current Roadmap
## Common Failure Modes
Important Warning

The file should not contain every decision in exhaustive detail. If it becomes a second README.md, a second decision log, and a second rules summary, it will eventually drift.

A good 
AGENTS.md
 should be:

More authoritative than a brainstorm log.
More operational than the README.
Less detailed than the canonical rule documents.
Explicit about where uncertainty remains.
Updated whenever a major architectural decision changes.

The most important sentence may be:

When chat history and an older document conflict, consult the current canonical documents, the decision log, and the Outstanding Definitions Index; do not infer authority from file age or document length.
