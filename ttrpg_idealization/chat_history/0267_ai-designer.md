---
turn: 267
role: "AI-Designer"
source: chat_history.json
---

# Turn 267 — AI-Designer

Yes. The checklist should point to the canonical destination for each task, especially when distinguishing:

A framework that is already established.
A procedure that still needs definition.
A content catalogue that is intentionally deferred.
A calibration task that belongs in research or simulation artifacts.

This would make the checklist useful even if the conversation context is lost.

Recommended Checklist Format

Each relevant task should include a Source or Owner link.

For example:

Markdown
- [x] Establish Attribute capacity derivations.
  - Owner: `03_core_baseline_system/02_attributes_and_derived_statistics.md`

- [~] Finalize Stamina expenditure and recovery.
  - Owner: `04_simulationist_subsystems/03_resources_conditions_and_wounds.md`
  - Status: Capacity is established; procedures remain open.

- [ ] Calibrate probability targets.
  - Research: `02_comparative_system_analysis/`
  - Simulation notes: `06_brainstorming_logs_and_roadmap/02_probability_and_dice_simulations.md`
Specific Checklist Updates
1. Resources

Separate capacity derivation from resource procedures.

Attributes file
text
03_core_baseline_system/02_attributes_and_derived_statistics.md

Owns:

Vitality capacity derivation.
Stamina capacity derivation.
Essence capacity derivation.
Paired defense derivations.
Resource subsystem
text
04_simulationist_subsystems/03_resources_conditions_and_wounds.md

Owns:

Resource expenditure.
Recovery.
Depletion.
Zero-resource consequences.
Conditions caused by resource depletion.

The checklist should reflect these as separate tasks.

2. Reference Good Slot Progression

The checklist should add:

Markdown
- [ ] Place the authoritative Reference Good Slot Progression table in its canonical home.
  - Owner: `03_core_baseline_system/06_leveling_and_tier_progression.md`

The CSV should remain a research/reference artifact unless we explicitly decide that it is the canonical table source.

3. Magic and Progression Cross-Reference

Add:

Markdown
- [x] Link the canonical Magic framework to the Spell Slot Progression owner.
  - Magic: `03_core_baseline_system/10_magic_schools_traditions_and_spellcasting.md`
  - Progression: `03_core_baseline_system/06_leveling_and_tier_progression.md`

And:

Markdown
- [x] Link the canonical Progression framework to the Magic Spell Slot rules.
  - Progression: `03_core_baseline_system/06_leveling_and_tier_progression.md`
  - Magic: `03_core_baseline_system/10_magic_schools_traditions_and_spellcasting.md`

The current cross-reference exists conceptually, but the checklist should track both directions.

4. Automatic Successes

The checklist should distinguish:

Markdown
- [x] Establish Automatic Success as a universal framework concept.
  - Owner: `03_core_baseline_system/01_resolution_engine.md`
  - Vocabulary: `03_core_baseline_system/00_baseline_framework_glossary.md`

- [~] Define which Classes, Feats, Spells, Equipment, and Mythic effects grant Automatic Successes.
  - Owners: Relevant future content files.
  - Status: Open.

- [ ] Calibrate Automatic Success frequency and impact.
  - Research: `02_comparative_system_analysis/`
  - Simulation notes: `06_brainstorming_logs_and_roadmap/02_probability_and_dice_simulations.md`
5. Skills and Domains

The checklist should distinguish the architecture from the content catalogue.

Markdown
- [x] Establish the eight-Domain architecture.
  - Owner: `03_core_baseline_system/09_domains_skills_activities_and_crafting.md`

- [x] Establish the Skill/Activity/Procedure distinction.
  - Owner: `03_core_baseline_system/09_domains_skills_activities_and_crafting.md`

- [~] Finalize Craft, Lore, Knowledge, and Vehicle specialty procedures.
  - Owner: `03_core_baseline_system/09_domains_skills_activities_and_crafting.md`
  - Status: Framework exists; detailed procedures remain open.

- [ ] Create complete Skill, Craft, Lore, and Activity catalogues.
  - Future content task.

This prevents the phrase “Skill architecture completed” from being misread as “all Skills and specialties are finished.”

Recommended General Rule

Every checklist item should answer three questions:

text
What has been done?

Where is it defined?

What remains open?

For example:

Markdown
- [~] Define Essence expenditure and recovery.
  - Capacity owner: `03_core_baseline_system/02_attributes_and_derived_statistics.md`
  - Procedure owner: `04_simulationist_subsystems/03_resources_conditions_and_wounds.md`
  - Magic interaction: `03_core_baseline_system/10_magic_schools_traditions_and_spellcasting.md`
  - Status: Capacity framework established; costs and recovery procedures open.

That would make PHASE_1_CHECKLIST.md a reliable project-control document rather than merely a list of broad aspirations.
