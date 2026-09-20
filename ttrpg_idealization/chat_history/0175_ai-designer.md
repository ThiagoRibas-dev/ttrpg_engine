---
turn: 175
role: "AI-Designer"
source: chat_history.json
---

# Turn 175 — AI-Designer

I agree. Mythic should remain a bounded placeholder until the Levels 1–20 framework is stable. Otherwise Mythic exceptions can distort the assumptions that should govern ordinary play.

The order should follow dependency depth: define the systems that other systems rely on before defining content that consumes them.

Recommended Order of Operations
Phase 0: Canonical Cleanup and Vocabulary Lock

Before expanding mechanics, eliminate contradictions in active documents.

Tasks:

Remove superseded terminology.
Confirm canonical names for:
Spell Slot Advancement.
Spell Slot Progression Level.
Essence.
Damage Absorption.
Classes and Prestige Classes.
Schools, Traditions, and Traits.
Mark historical comparison sections clearly.
Ensure the README, AGENTS.md, Project Status, decision log, and Outstanding Definitions Index agree.

This prevents later work from being built on obsolete terminology.

Phase 1: Mathematical Core and Probability Framework

This should be the first substantive design phase.

Define
The complete Attribute Die ladder.
Ordinary and over-cap dice.
Pool-size ceiling.
Competency Floors.
Fixed DC categories.
Opposed-roll tie-breaking.
Multi-success counting.
Boon and Bane limits.
Die Step-Up and Die Step-Down.
Resource-driven Die Step-Ups.
Probability targets for ordinary checks.
Key output

A single mathematical reference document answering:

text
What does each Attribute Die mean?

What does each Competency Rank mean?

What is the probability of:
  Untrained vs routine task?
  Trained vs challenging task?
  Expert vs equal-tier task?
  Master vs formidable task?

How much does a Boon matter?
How much does a Bane matter?
How much does a Die Step-Up matter?
How much does an extra die matter?

Do not begin large-scale class or spell design until this is sufficiently stable.

Phase 2: Actor Statistics and Progression Vectors

Once the check engine is stable, define how characters improve.

Define
Attributes.
Attribute advancement.
Vitality.
Stamina.
Essence.
Defenses.
Speed.
Carrying capacity.
Competency Rank advancement.
Class progression.
Feat cadence.
Spell Slot Advancement.
Equipment advancement.
Ancestry advancement.
Mythic placeholder boundaries.
Critical goal

Each progression vector should have one clear job.

For example:

Vector	Primary Function
Attribute Die	Peak capability and raw potential
Competency Rank	Reliability, floors, and skill mastery
Class	Role progression and class features
Feats	Discrete permissions and tactical options
Equipment	Material capability, traits, protection, durability
Spell Slots	Daily magical volume
Tradition Rank	Magical access and intrinsic spell scaling
Essence	Short-term supernatural exertion

This phase should produce the complete Level 1–20 advancement scaffolding before individual classes are written.

Phase 3: Core Combat and Defensive Math

Combat should be stabilized before equipment, feats, or combat-heavy classes.

Define
Attack resolution.
Reflexes and Parry.
Fortitude and Willpower.
Damage Absorption.
Weapon Damage Dice.
Armor and shield behavior.
Vitality loss.
Critical hits.
Called Shots.
Wounds.
Conditions.
Maneuvers.
Active defense Stamina expenditure.
Multiple attacks and multi-action fatigue.
Underlings and Rabble.
Calibration goals
Standard combat should last approximately 3–5 rounds.
Critical hits should be dangerous but not constantly decisive.
Maneuvers should occur frequently enough to matter.
Armor should reduce injury without making attacks pointless.
Equipment should not produce runaway numerical scaling.
Multiple enemies should create pressure without requiring modifier inflation.

This phase should include simulations and small encounter tests.

Phase 4: Equipment and Economic Framework

This should happen before writing large numbers of feats, classes, or monsters because equipment affects every physical actor.

Define
Weapon damage categories.
Damage Die progression.
Weapon Traits.
Armor categories.
Damage Absorption Dice.
Shield rules.
Durability Slots.
Material qualities.
Masterwork equipment.
Magical equipment.
Weapon critical profiles.
Equipment repair and replacement.
Crafting and item creation.
Wealth and expected equipment access by level.
Important framework question

What does “better equipment” mean in this system?

Potential vectors include:

Higher Damage Die.
Higher Damage Absorption Die.
More Durability Slots.
New weapon Traits.
Better Critical Threat Profile.
Special resistance or penetration.
Action-economy permissions.
Expanded environmental capability.

The system should avoid:

text
Sword +1
Armor +3
Ring +2

in favor of discrete capabilities.

Wealth-by-level

We should establish campaign-economic guidance analogous to D&D 3.5e wealth-by-level, but it should probably be expressed as:

Expected equipment quality.
Expected Durability capacity.
Expected number of major magical items.
Expected crafting access.
Expected consumable availability.
Expected replacement and upkeep pressure.

This does not need to be a literal currency table immediately, but the framework needs predictable assumptions.

Phase 5: Skills, Domains, Activities, and Craft

Once core resolution and equipment are stable, finalize the noncombat capability framework.

Define
Full canonical skill list.
Domain interactions.
Skill-to-Attribute pairings.
Lore specialty rules.
Knowledge categories.
Craft specialty rules.
Vehicle proficiencies.
Tools and fictional permissions.
Activity procedures.
Assistance.
Complex tasks.
Training requirements.
Skill-gated activities.
Downtime and crafting clocks.

This phase should resolve:

text
What is a Skill?

What is an Activity?

What is a Procedure?

What is a Maneuver?

What requires a tool?

What requires a class or feat permission?

This should happen before the Feat Compendium because many feats will unlock or modify activities.

Phase 6: Magic Framework

Only after the universal progression, resource, and action systems are stable should we complete magic.

Define
Tradition Skills.
Tradition access.
Fixed Tradition spell lists.
Spell Schools.
Spell Traits.
Spell Circles.
Spell Slot Progression.
Spell preparation.
Spell acquisition.
Learning limits.
Casting actions.
Essence.
Metamagic.
Casting under pressure.
Concentration or sustained spells.
Rituals.
Spell failure and interruption.
Spell scaling by Tradition Competency.
Explicit Heightening rules.
Magical equipment and implements.

The order inside this phase should be:

Spell Slot Progression.
Preparation and learned-spell limits.
Acquisition and multiclass stacking.
Essence and casting stability.
Spell record format.
Spell conversion guidelines.
Individual spells.

Do not write hundreds of spells before the spell record and resource engine are stable.

Phase 7: Feats and Modular Class Framework

After the core systems are stable, design classes and feats as consumers of the framework.

First design the class chassis

Define:

Class table format.
Class skill access.
Tradition access.
Spell Slot Advancement.
Attribute priorities.
Defense progression.
Vitality progression.
Essence progression.
Feat cadence.
Class feature cadence.
Prestige Class requirements.
Then build sample classes

Not a full compendium yet. Begin with test cases:

Warrior or Fighter.
Rogue.
Cleric.
Wizard.
Nature caster.
Paladin or War caster.

Use these to test:

Multiclassing.
Skills.
Spell access.
Equipment.
Feats.
Resource competition.
Advancement pacing.
Then design feats

Start with framework-defining feat categories:

General Feats.
Combat Feats.
Skill Feats.
Domain Feats.
Tradition Feats.
Metamagic Feats.
Racial/Ancestry Feats.
Equipment Feats.

The first feats should test the architecture rather than fill a catalogue.

Phase 8: Universal Actor and Monster Framework

Once PC systems are functional, use the same framework for NPCs and monsters.

Define
Monster skill allocation.
Monster Tradition access.
Monster Spell Slot Progression.
Monster Feats.
Ancestry-like monster traits.
Boss features.
Rabble and Underling templates.
Encounter-level scaling.
Monster equipment assumptions.
Nonhuman resource rules.

Start with:

A common humanoid.
A goblin.
An ogre.
A spellcaster.
A dragon.
A boss.
An Underling squad.

This will reveal whether the Universal Actor Schema is genuinely universal or merely PC-shaped.

Phase 9: Conversion and Content Production

Only after the above framework is sufficiently stable should we conduct broad conversion.

Recommended order:

D&D 3.5e classes and prestige classes.
D&D 3.5e feats.
D&D 3.5e spells.
D&D 3.5e monsters.
Pathfinder content.
SotDL/Weird Wizard paths and Traditions.
Mythras/BRP combatants and special effects.
Gloomhaven-style enemies and abilities.

D&D 3.5e should remain the primary conversion target.

Phase 10: Mythic Expansion

Mythic should come last.

The basic Mythic framework can remain documented as:

Mythic begins beyond Level 20.
Epic Traditions and Spells become available.
Existing Spell Slots remain relevant.
Mythic adds permissions, scale, and exceptional effects rather than simply inflating ordinary numbers.

But we should not yet define:

Mythic slot quantities.
Mythic Attribute values.
Mythic damage.
Mythic DCs.
Divine-scale resource pools.
Reality-altering spell rules.
Mythic class tracks.
Mythic monster math.

Those should be built only after the Level 1–20 system has established stable ceilings and progression expectations.

Recommended Immediate Order

The practical next sequence should be:

Finish mathematical core audit.
Finalize Level 1–20 progression vectors.
Stabilize combat and defense math.
Define equipment and wealth-by-level scaffolding.
Finalize Skills, Domains, Activities, and Craft.
Complete the Magic framework.
Build a few sample Classes and Feats.
Build the Universal Actor and Monster framework.
Begin broad conversion work.
Return to Mythic only after Level 1–20 is stable.

The governing principle should be:

First stabilize the mathematical and progression scaffolding; then define the systems that consume it; then produce content; finally extend beyond the bounded mortal framework into Mythic play.
