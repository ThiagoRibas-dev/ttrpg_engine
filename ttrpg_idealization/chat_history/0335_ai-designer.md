---
turn: 335
role: "AI-Designer"
source: chat_history.json
---

# Turn 335 — AI-Designer

Understood. Before recording DEC-064 or changing canonical rules, I reviewed the relevant current files and mapped the required updates.

Current Relevant Sources
Canonical framework
text
03_core_baseline_system/
├── 00_baseline_framework_glossary.md
├── 01_resolution_engine.md
├── 02_attributes_and_derived_statistics.md
├── 06_leveling_and_tier_progression.md
├── 07_check_pool_generation_and_class_differentiation.md
├── 08_statistical_framework_and_check_modes.md
├── 09_domains_skills_activities_and_crafting.md
├── 10_magic_schools_traditions_and_spellcasting.md
└── 12_equipment_durability_and_economy.md
Research
text
02_comparative_system_analysis/
├── 09_at_least_probability_matrices.md
├── 11_floor_equipment_dc_target_calibration.md
├── 12_multi_success_probability_matrices.md
├── 13_probability_band_calibration.md
├── 14_difficulty_vector_probability_matrices.md
└── 15_provisional_tier_difficulty_vectors.png
Tracking
text
PHASE_1_CHECKLIST.md
06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md
06_brainstorming_logs_and_roadmap/03_outstanding_definitions_index.md
Proposed Canonical Changes
1. 00_baseline_framework_glossary.md
Change

Revise:

text
Competency Floor

from a canonical active definition into one of two possible states:

Recommended version

Remove it from the active resolution vocabulary entirely and add a short historical note only if needed:

The former Competency Floor mechanic has been removed from the current framework. Final Dice Pool Size now determines probability directly; no separate Floor is applied.

However, because you asked to remove historical references from canonical files, the cleaner version is probably:

Delete the Competency Floor glossary entry.
Remove Floor from the active universal glossary terms.
Leave the historical Floor decision in the archived decision/report material.
Other glossary updates

Clarify:

text
Competency Rank:
  Determines baseline Dice Pool Size.

Attribute:
  Determines Die Size.

Equipment, Boons, Banes, Feats, and other effects:
  May modify final Dice Pool Size or grant Permissions.

The glossary should not define the full difficulty-vector procedure. That belongs in the Resolution Engine.

2. 01_resolution_engine.md

This is the main canonical update.

Remove
Competency Floor section.
Floor column from the Competency table.
Floor calculation steps.
Floor cap at die size − 1.
References to Banes lowering Floors.
References to Automatic Successes being compared against a Floor.
Any remaining Floor language in procedure examples.
Replace Competency table

Current model:

text
Competency Rank | Baseline Dice Pool | Base Floor
Untrained       | 1dX              | 1
Trained         | 2dX              | 2
Veteran         | 3dX              | 3
Master          | 4dX              | 4
Hero            | 5dX              | 5
Legend          | 6dX              | 6

New model:

text
Competency Rank | Baseline Dice Pool
Untrained       | 1dX
Trained         | 2dX
Veteran         | 3dX
Master          | 4dX
Hero            | 5dX
Legend          | 6dX
Update pool procedure

The final sequence should become:

Determine Attribute Die Size.
Determine baseline Dice Pool Size from Competency Rank.
Apply Class, Feat, Equipment, Spell, circumstance, and other pool-volume effects.
Apply Die Step-Ups and Die Step-Downs.
Resolve Boon/Bane cancellation and stacking.
Add remaining Boon dice.
Remove remaining Bane dice.
Apply the one-die Bane-induced Die Step-Down if necessary.
Roll the final Dice Pool.
Resolve the selected Difficulty Vector or opposed contest.

No Floor calculation occurs.

Keep
d12 ordinary ceiling.
Pool volume beyond natural baseline where content grants it.
Boon/Bane types.
One-for-one cancellation.
Same-source non-stacking.
Bane removal procedure.
d4 Bane Step-Down automatic failure.
Automatic Successes.
Requirements and Permissions.
Defender Wins Ties.
Replace difficulty notation

Remove active use of:

text
DC X (Y)

Replace with:

text
DC X
DC X,Y
DC X,Y,Z

The procedure should define:

Sort rolled dice from highest to lowest.
Sort vector thresholds from highest to lowest.
Compare them positionally.
Extra dice are ignored for that particular vector.
The check succeeds only when every threshold in the vector is met.

Example:

text
Pool: 8, 6, 3
Difficulty: DC 5,4

8 ≥ 5
6 ≥ 4

Success.
Automatic Successes

No change to the previous decision that higher pools simply continue adding dice.

Automatic Successes remain a separate content-provided effect. They do not replace excess dice.

3. 02_attributes_and_derived_statistics.md
Change

Remove any references to:

Competency Floors.
Floor caps.
Floors on paired defenses.
Keep
Attributes determine Die Size.
Paired defenses use their paired Attribute Dice.
A paired defense has a number of dice based on its paired pool construction.
The paired pool does not need a separate Floor mechanic.

Example:

text
STR d8 + CON d10:
  1d8 + 1d10, keep highest

This file should not define Difficulty Vectors or Boon/Bane resolution.

4. 06_leveling_and_tier_progression.md
Change

Remove any references to:

Fixed Competency Floors.
Floor-based Tier progression.
Floor 3, Floor 5, Floor 7, or Floor 9 advancement.
Keep
Competency Rank progression.
Tier-aligned rank names:
Trained.
Veteran.
Master.
Hero.
Legend.
Spell Slot Advancement.
Level-by-level class advancement.
Mythic boundary.

The level document should state:

Competency Rank increases baseline Dice Pool Size. Attribute Die Size and external effects remain separate progression vectors.

No probability targets should be added here.

5. 07_check_pool_generation_and_class_differentiation.md

This becomes the main relationship document for the revised model.

Change the three variables

Current:

text
Die Size
Pool Volume
Competency Floor

New:

text
Die Size
Baseline Dice Pool Size
Final Dice Pool Size
Canonical relationship
text
Attribute → Die Size
Competency Rank → Baseline Dice Pool Size
Equipment/Boons/Banes/Feats/Spells → Final Dice Pool Size
Final Dice Pool → Probability profile

This file should explicitly state:

Attribute controls the numerical ceiling. Competency and external effects control the number of attempts made against the difficulty vector.

Remove
Floor references.
Floor-based progression claims.
Floor-based class differentiation.
Keep
The separation of progression vectors.
The normal pool range.
The possibility of content-controlled pools above the natural range.
The distinction between Attribute Die Size and Dice Pool Size.
6. 08_statistical_framework_and_check_modes.md

This is the main conceptual owner for the new probability model.

Add
text
Attribute Die Size:
  Determines the face-value ceiling.

Dice Pool Size:
  Determines how many ordered results are available.

Difficulty Vector:
  Determines the thresholds those results must satisfy.

Equipment:
  Expands the pool according to the current provisional equipment profile.

Competency:
  Expands the baseline pool through Rank.
Add difficulty-vector examples
text
DC 5
DC 5,4
DC 5,5
DC 6,5,3
Add calibration pointer

Point to:

text
02_comparative_system_analysis/14_difficulty_vector_probability_matrices.md
02_comparative_system_analysis/15_provisional_tier_difficulty_vectors.png

The Statistical Framework should not duplicate the matrices. It should explain how to use them.

7. 09_domains_skills_activities_and_crafting.md
Change

Remove references to:

Fixed Floors by Competency Rank.
Floor-based Skill examples.
Floor-based Skill gating.
Keep
Skill structure.
Competency Rank.
Activity and Procedure ownership.
Requirements and Permissions.
Craft, Lore, Knowledge, and vehicle framework.

The document should reference:

text
07_check_pool_generation_and_class_differentiation.md
01_resolution_engine.md

for pool construction and difficulty resolution.

8. 10_magic_schools_traditions_and_spellcasting.md
Change

Remove any implication that Tradition Rank grants a Floor.

Tradition Competency should now affect:

Tradition access.
Baseline casting Dice Pool Size.
Spell scaling where the spell explicitly uses Tradition Competency.
Requirements and Permissions.
Keep
Spell Schools.
Traditions.
Traits.
Shared spell lists.
Shared Spell Slots.
Spell Slot Progression.
Essence.
Preparation and acquisition framework.

Difficulty Vectors should be referenced through the Resolution Engine, not redefined here.

9. 12_equipment_durability_and_economy.md

No equipment rules need to be created yet.

Add only a scope statement

Equipment may modify final Dice Pool Size through:

Typed Boons.
Additional dice.
Traits.
Requirements.
Permissions.

The current provisional equipment progression should remain in the research artifact:

text
02_comparative_system_analysis/13_probability_band_calibration.md

Do not turn it into canonical equipment rules yet.

Research Artifact Changes
Keep and update
14_difficulty_vector_probability_matrices.md

This remains the primary matrix artifact for:

Single-threshold vectors.
Two-threshold vectors.
Three-threshold vectors.
Representative pool sizes.

Remove any mention of Floors from its active model.

15_provisional_tier_difficulty_vectors.png

Keep as a visual calibration artifact, but label it:

text
Raw Dice Probability
No Floor Applied
Provisional Equipment Progression
13_probability_band_calibration.md

Update its description to remove Floor references.

Its assumptions become:

text
Final Dice Pool:
  Baseline Competency Pool + Equipment Boons

Probability:
  Difficulty Vector against final raw Dice Pool
Tracking Artifact Changes
Decision log

Add a new decision entry:

text
DEC-064 — Difficulty Vectors and Removal of Explicit Floors

It should record:

Explicit Floors are removed.
Competency Rank determines baseline Dice Pool Size.
Attribute determines Die Size.
Equipment and other external effects modify final Dice Pool Size.
Difficulty uses comma-separated vectors.
DC X is a one-threshold vector.
DC X,Y is a two-threshold vector.
No DC X (Y) notation remains.
Larger pools continue adding dice rather than converting excess dice into Automatic Successes.
Difficulty vectors are pre-calibrated by Tier and content profile.
Probability bands are provisional.
Outstanding Definitions Index

Mark as resolved:

Competency-based versus pool-based Floor choice.
Explicit Floor removal.
Difficulty-vector architecture.
Larger pools continuing to add dice.

Keep open:

Exact per-Tier vector catalogue.
Equipment progression.
How many vector thresholds ordinary content may use.
Automatic Success sources and limits.
Probability targets after further calibration.
Phase 1 Checklist

Update:

text
Competency Rank → Baseline Dice Pool Size
Final Dice Pool → Difficulty Vector Probability

Mark Floor tasks as superseded and add:

 Remove explicit Floor mechanic.
 Establish comma-separated Difficulty Vectors.
 Establish DC X as a single-threshold vector.
 Establish DC X,Y as a two-threshold vector.
 Establish that larger pools continue adding dice.
[~] Calibrate per-Tier Easy, Medium, and Hard vectors.
[~] Calibrate equipment progression and final Dice Pools.
Recommended Execution Order
Update the glossary.
Update the Resolution Engine.
Update Pool Generation and Statistical Framework documents.
Update Attributes and Derived Statistics.
Update Progression, Skills, and Magic references.
Update research artifact descriptions.
Update the Decision Log.
Update the Outstanding Definitions Index.
Update the Phase 1 Checklist.
Re-run the canonical consistency scan.

The important consolidation principle is:

The Resolution Engine owns how difficulty vectors resolve; the Statistical Framework owns how pool size and vectors relate; the research artifacts own the probability tables; other canonical files reference those owners.
