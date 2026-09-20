---
turn: 101
role: "AI-Designer"
source: chat_history.json
---

# Turn 101 — AI-Designer

Ran commands
2
Edited files
4
Outstanding Definitions Index
MD
Outstanding Definitions Index

Status: Active meta-document
Purpose: Index unresolved definitions, provisional subsystems, and documents that still contain historical option language. This is a navigation document, not a rules document.

Canonical rules override discussion artifacts. Where an entry is marked Documentation cleanup, the design decision is already made; only the older document wording remains to be revised.

1. Active Architectural Definitions
OD-001 — Magic Mastery tradition skills and spellcasting engine

Status: Open; highest priority.

The current tradition list is established provisionally, but the actual spellcasting engine has not yet been fully written. Still to define:

Tradition access and prerequisites.
Tradition skill progression.
How classes and modular paths grant tradition access.
Vancian preparation and spellbook/repertoire structures.
Spell slots by level and class track.
Focus expenditure, metamagic, concentration, and emergency casting.
Tradition-specific procedures and limited unique rules.
How advanced traditions become available.
Whether Celestial is a Divine specialization or a separate tradition.
Whether Primal remains the formal name while Natural World is a specialization/mantle.

Relevant documents:

Canonical Magic Architecture
Attacks, Spells, and Skill Architecture
Magic and Focus Decision
Magic roadmap
OD-002 — Psychic/Psionic power

Status: Open; intentionally separate from the current Vancian tradition list.

Decide whether Psychic/Psionic power becomes:

A separate non-Vancian discipline system using Focus, disciplines, augmentations, and strain; or
A Magic Mastery tradition using Vancian preparation.

The current direction favors a separate non-Vancian system, but this is not yet mechanically designed.

Relevant documents:

Canonical Magic Architecture
DEC-050
OD-003 — Mantle compendium and mechanics

Status: Open.

The Ardent-inspired Mantle axis is accepted conceptually, but the final Mantle list and mechanics remain undefined. Still to decide:

Which Mantles are official.
Which are merely spell Traits or setting tags.
Whether characters select Mantles directly.
Whether Mantles grant access, feats, bonuses, spell-list permissions, or only classification.
How moral concepts such as Good and Evil differ from Law, Chaos, Justice, and Corruption.
Whether Time, Space, Creation, Order, and Chaos are Mantles, advanced Traditions, or both.

Relevant documents:

Canonical Magic Architecture
Magic tradition consolidation discussion
OD-004 — Craft specialty presentation and rank behavior

Status: Partially defined; implementation open.

Craft is a canonical Domain with defined specialties, but the character-sheet and advancement treatment still need final definition:

Whether Craft specialties are individually ranked skills or specialty entries beneath Craft.
Whether a character can use general Crafting without a specialty.
How Craft — Engineering relates to Knowledge — Engineering.
How Craft — Alchemy interacts with Knowledge — Alchemy and Pharmacology.
How tools, workshops, downtime, ingredients, and equipment durability affect checks.
Whether Craft specialties are selected from a closed list, open list, or campaign list.

Relevant documents:

Revised Domain-and-Activity Architecture
Craft and Production Domain
Crafting specialties
OD-005 — Lore specialty presentation and adjudication

Status: Partially defined; implementation open.

Lore is canonical as an open-ended focused familiarity skill, but still needs:

Character-sheet presentation.
Specialty naming and scope limits.
Whether each Lore field receives its own Competency Rank.
How Lore interacts with formal Knowledge skills.
How broad a Lore specialty may be.
How Background, Race, Class, and faction membership grant Lore.

Relevant documents:

Lore and Cultural Familiarity
Knowledge and Lore distinction
OD-006 — Vehicle proficiency taxonomy

Status: Partially defined; implementation open.

Vehicle operation is a family of proficiencies rather than one universal skill. Still to define:

The final vehicle categories.
Whether vehicle proficiencies are skills, Craft specialties, or equipment permissions.
Which attributes and Domains govern each category.
Crew assistance and command procedures.
Vehicle combat and damage procedures.
How magical, aerial, subterranean, and siege vehicles work.

Relevant documents:

Vehicle Proficiencies
OD-007 — Domain-level mechanics

Status: Open.

Domains are canonical game entities, but no separate Domain Rank currently exists. Still to define:

Domain-level prerequisites.
Domain feats.
Class and path interactions.
Domain equipment tags.
Domain actions and subsystems.
Whether a Domain can grant permission without changing a skill pool.
How Universal Actor blocks use Domains for monsters and NPCs.

Relevant documents:

Revised Domain-and-Activity Architecture
DEC-049
OD-008 — Activity and multi-skill procedure framework

Status: Partially defined; implementation open.

The system has established that Investigation, Forgery, Disguise, Escape Artistry, Lockpicking, Trap Disarming, Shadowing, Treaty Negotiation, Interrogation, and Camp Fortification are activities rather than universal skills. Still to define:

When an activity uses one primary roll versus multiple stages.
Assistance rules.
Tools and fictional permissions.
Failure and complication procedures.
Whether supporting skills grant Boons, create separate stages, or alter consequences.
How complex activities interact with Competency Floors and multi-success checks.

Relevant documents:

Activity Examples
Skills and Generic Capabilities
2. Provisional Content Definitions
OD-009 — Final Magic Mastery tradition list

Status: Provisional list accepted for design work; not yet final rules content.

Current list:

Arcane / Thaumaturgic
Divine / Theurgic
Primal / Natural
Spirit
Shadow
Elemental
Rune
War
Dream
Life
Death
Eldritch / Void
Time
Space
Chaos
Order
Creation

Time, Space, Chaos, Order, and Creation are currently advanced or restricted. Celestial is currently a possible Divine specialization. Natural World is currently a possible Primal specialization or Mantle.

Relevant document:

Canonical Magic Architecture
OD-010 — Spell record and tag vocabulary

Status: Framework accepted; final vocabulary open.

The multi-axis record is established as:

text
School
Traditions
Mantles
Traits

Still to define:

Complete spell Trait list.
Whether Domains and Mantles are distinct in every case.
Whether Delivery is a separate axis or a Trait family.
Spell resistance, defense targeting, range, duration, and action tags.
Tradition-specific versions of the same spell.

Relevant document:

Canonical Multi-Axis Spell Record
OD-011 — Spell conversion catalogue

Status: Open content task.

The roadmap calls for conversion of at least fifteen classic spells and eventually a larger spellbook. Need to define:

Spell levels and Tier equivalents.
Vancian slot requirements.
Tradition tags for each spell.
School classification for legacy spells.
Defense targets and conditions.
Multi-tradition versions.
Ritual versus combat casting.

Relevant documents:

D&D 3.5e conversion procedure
Spellbook translation roadmap
3. Definitions Already Decided but Still Described as Options

These are not open design questions. They are documentation-cleanup items.

DC-001 — Check-pool architecture

Decision: Model A, Pure Role Separation, is locked by DEC-038.

Stale references:

Check-pool architecture comparative matrix
Check-pool generation and class differentiation

These documents should be relabeled as historical comparison or updated to identify Model A as canonical.

DC-002 — Attacks and spells as skills with class-granted advancement

Decision: Option 3, Hybrid Class-Granted Domain Allocations, is locked by DEC-041.

Stale references:

Attacks and spells architecture

The document still presents Options 1–3 at length. Those sections should be retained as design history but clearly marked non-canonical.

DC-003 — Skill architecture and the historical 65-skill matrix

Decision: DEC-049 is canonical. The 65-skill matrix is archived.

Status: The file has already been moved to the archive. Remaining references should point to the archived path and describe it as historical.

DC-004 — Old five-domain skill taxonomy

Decision: The eight-domain architecture in DEC-049 is canonical.

Stale reference:

Historical five-umbrella matrix

This section is correctly retained for provenance but should remain explicitly marked historical.

DC-005 — Old resolution terminology and mechanics

Status: Review required.

Some older documents still contain superseded language such as [SET], “Soak,” “Hyper-Shift,” or older Called Shot thresholds. These are not necessarily open questions; they are consistency errors requiring a canonical-rules audit.

Relevant documents:

Master top-to-bottom summary
Resolution engine
Defenses and damage modeling
4. Historical Calibration Questions

The following questions appear in comparative and simulation documents. They were used to establish the current baseline and should not automatically be treated as open architecture unless a future playtest reopens them.

Competency success curves and target probabilities.
Critical frequency.
Time to defeat and combat pacing.
Offensive versus defensive scaling.
Stamina depletion under repeated active defense.
Resource reset cadence.
Opposed-roll tie frequency.

Relevant document:

Mathematical calibration and TTK vectors

These are calibration targets, not unresolved taxonomy decisions.

5. Recommended Resolution Order
Complete the Magic Mastery and Vancian spellcasting engine.
Resolve Psychic/Psionic power as a separate subsystem or tradition.
Define the character-sheet presentation for Domains, Skills, Specialties, Lore, and Knowledge.
Define domain-level mechanics and class/path interactions.
Define activity procedures and assistance rules.
Finalize Craft, Lore, Vehicle, and Magic specialties.
Build the spell Trait and Mantle compendia.
Perform a canonical-document consistency audit and relabel historical option sections.
Open
used
Bash
120ms

Created the meta-document:

text
06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md

It indexes:

Active architectural definitions.
Provisional Magic Mastery traditions.
Psychic/Psionic power.
Mantle mechanics.
Craft specialties.
Lore specialties.
Vehicle proficiencies.
Domain-level mechanics.
Multi-skill activity procedures.
Spell tags and spell-record structure.
Spell conversion work.
Decisions already locked but still described as options.
Historical calibration questions versus actual unresolved design issues.

Each entry includes:

A unique tracking ID.
Current status.
The definition or decision still needed.
Relevant document links.
Recommended resolution order where appropriate.

I also updated the root README.md so the new index appears in the workspace directory map.
