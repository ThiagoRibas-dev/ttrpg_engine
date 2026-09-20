---
turn: 237
role: "AI-Designer"
source: chat_history.json
---

# Turn 237 — AI-Designer

used
Bash
79ms
Write
ttrpg_idealization/03_core_baseline_system/07_check_pool_generation_and_class_differentiation.md
78 lines
open
Check-Pool Generation and Class Differentiation
MD
Check-Pool Generation and Class Differentiation

Status: Canonical statistical relationship framework.
Scope: Explains which progression vectors affect Die Size, pool volume, Floors, and permissions. The universal rolling procedure belongs to 01_resolution_engine.md.

1. Three Core Pool Variables

A final check is described by three primary variables:

text
Die Size (X)
Pool Volume (N)
Competency Floor (F)
Die Size

Die Size represents the relevant Attribute’s capability ceiling:

text
d4 → d6 → d8 → d10 → d12

Attribute advancement, relevant Competency Step-Ups, equipment, spells, or specific Permissions may affect Die Size. Ordinary resolution does not exceed d12.

Pool Volume

Pool Volume represents the number of dice rolled. It is affected by Competency Rank, Boons, Banes, Class features, Feats, Equipment, tactics, and other explicit effects.

The ordinary natural pool is generally 2dX to 5dX. Content may exceed the natural range through explicit high-tier effects, but such effects are controlled by their granting content.

Competency Floor

Competency Floor represents the minimum result produced by a Competency Rank. The Resolution Engine defines how Floors interact with final Boons and Banes.

2. Progression-Vector Separation
Source	Primary mathematical job
Attribute	Die Size and capability ceiling
Competency Rank	Pool Volume, Die Step-Up, and Floor
Class/Prestige Class	Class features, protected primary competency, Spell Slot Advancement, and permissions
Feat	Discrete permissions, actions, traits, and specialized effects
Equipment	Material capability, Damage Absorption, Traits, durability, and explicit permissions
Tactics and circumstances	Boons, Banes, actions, positioning, and conditions
Stamina/Essence	Content-specific exertion and supernatural permissions

No source should silently duplicate another source’s job through linear modifiers.

3. Universal Resolution Reference

For the actual procedure for assembling and resolving a pool, see:

text
01_resolution_engine.md

That document owns:

Natural Dice Pool and Enhanced Dice Pool.
Boons and Banes.
Die Step-Up and Die Step-Down.
Competency Floors.
Difficulty Classes.
Required Successes.
Opposed rolls and Defender Wins Ties.
Automatic Successes.
4. Class and Actor Differentiation

Classes, Prestige Classes, Ancestries, Feats, Equipment, and Monsters differentiate actors through the progression vectors above rather than through incompatible resolution engines.

A Fighter, Wizard, Ogre, and Dragon may have different Attributes, Skills, Traditions, Equipment, and Permissions, but their uncertain actions still use the same universal pool procedure.

5. Current Scope Boundary

This file describes the statistical model only. Final probability targets, equipment scaling, high-tier pool expansion, and detailed class/content effects remain tracked in the Phase 1 Checklist and Outstanding Definitions Index.

Open
used
Bash
183ms

Completed Phase R4 — Universal Resolution Consolidation.

Updated canonical files
03_core_baseline_system/01_resolution_engine.md

Replaced the previous mixed-version document with one consolidated procedure covering:

Natural Dice Pools.
Enhanced Dice Pools.
2dX keep highest.
Competency Floors.
Boons and typed stacking.
One-for-one Boon/Bane cancellation.
Bane die removal.
One-die Bane Die Step-Down.
d4 Bane automatic failure.
Die Step-Up and Die Step-Down ordering.
Difficulty Classes.
Required Successes.
DC X (Y).
Opposed checks.
Secondary die tiebreaking.
Defender Wins Ties.
Automatic Successes.
Requirements.
Permissions.
Complex checks and maneuvers.

Obsolete [SET], old Bane tables, Soak terminology, Focus terminology, and over-cap dice were removed from the active Resolution Engine.

03_core_baseline_system/07_check_pool_generation_and_class_differentiation.md

Reduced this document to its proper role:

Die Size.
Pool Volume.
Competency Floor.
Progression-vector separation.
Class and actor differentiation.
Links to the Resolution Engine.

It no longer duplicates the complete universal resolution procedure.

Preserved pre-consolidation versions

Saved under:

text
02_comparative_system_analysis/archived_core_reference/r4_pre_consolidation/
01_resolution_engine_PRE_R4.md
07_check_pool_generation_PRE_R4.md
Tracking updated
Marked R4 tasks complete in DOCUMENTATION_REFACTOR_PLAN.md.
Recorded the focused R4 audit in DOCUMENTATION_REFACTOR_AUDITS.md.
Documented that no new mechanical decisions were introduced.
Left probability calibration, content-specific resource costs, high-tier Automatic Success progression, and detailed combat consequences deferred.

R4 is now complete.
