---
turn: 2
role: "AI-Designer"
source: chat_history.json
---

# Turn 2 — AI-Designer

Explored
2 reads
Read
ttrpg_architecture_matrix.md
Read
bespoke mathless system report.md
Ran commands
2
Edited files
15
Master Brainstorm Log & Development Roadmap
MD
Master Brainstorm Log & Development Roadmap

This document maintains our running log of design decisions, open architectural questions, and actionable roadmap items for the iterative evolution of our idealized mathless TTRPG system.

1. Core Design Decisions Log
Decision ID	Date	Architectural Topic	Resolution / Decision Made	Core Rationale
DEC-001	2026-07-20	Core Resolution Engine	Adopt 2dX keep highest (Step Pools) as the universal baseline check engine.	Eliminates all modifier addition/subtraction while delivering immediate, tactile satisfaction inspired by D&D Advantage and SotDL Boons.
DEC-002	2026-07-20	Target Numbers (DCs)	Lock fixed DCs from 2 to 12, mapped against die step ceilings (d4 
→
→ d12).	Transparent physical boundaries; immediately communicates whether an action is routine (DC 3), challenging (DC 6), or heroic (DC 9).
DEC-003	2026-07-20	Boons & Banes (+B / +X)	Convert SotDL boons from +d6 addition into Pool Volume Shifts (+1d / -1d).	Preserves the elegance of mutual cancellation without reintroducing table-side arithmetic (3d8 keep highest).
DEC-004	2026-07-20	Overcoming Cap Ceilings	Implement Stamina-Driven Hyper-Shifting (Up-Shift). Spending 1 Stamina steps up check dice (2d6 
→
→ 2d8).	Replaces static +2 bonuses with an in-world physical exertion choice, ensuring scrappy characters can hit high DCs without mathematical bloat.
DEC-005	2026-07-20	Defense & AC Replacement	Replace single Armor Class with 4 Physical/Mental Layers: Evasion, Parry, Soak Rank, and Resilience.	Respects physical simulationism (Soak is NOT armor class); armor absorbs kinetic impact (Damage Die vs Soak Die) after a hit occurs.
DEC-006	2026-07-20	Meta-Currencies	Strict ZERO Meta-Currency policy. All heroic luck/effort runs on Stamina, Focus, and Durability Sacrifice.	Preserves 100% in-world character immersion for simulationist players.
2. Open Architectural Questions & Dilemmas
Dilemma 1: Managing Pool Size Bloat vs Counting Fatigue
The Issue: While 2dX base pools with up to 
+
3
 Boons (‘5dX‘)
+3 Boons (‘5dX‘) are fast and tactile, what happens when a character has legendary domain mastery (+3B), flanking (+1B), high ground (+1B), and a spell buff (+1B) simultaneously? Does rolling 8dX keep highest slow down table play or obscure dice faces?
Proposed Solution: Establish a strict Pool Volume Ceiling (Max 5 Dice in any check pool). Any excess Boons beyond 5dX automatically convert into a free Hyper-Shift (Up-Shift die size: 5d8 
→
→ 5d10) or grant an immediate Secondary Action / Stride ([1A]) due to overwhelming tactical dominance.
Dilemma 2: Magic Item & Equipment Scaling
The Issue: In D&D 3.5e and PF2e, characters scale from normal steel swords up to 
+
5
 Vorpal Greatswords
+5 Vorpal Greatswords and 
+
5
 Full Plate
+5 Full Plate. If we eliminate 
+
1
/
+
2
+1/+2 enhancement bonuses, how do masterwork and magical weapons scale?
Proposed Solution: Magic weapons scale across Three Concrete Vectors:
Durability Slot Expansion: (Standard: 2 Slots 
→
→ Adamantine: 4 Slots, allowing more heroic sacrifices).
Soak Penetration: (Mithril/Magic blades automatically step down enemy Soak Ranks by 1 rank).
Embedded Keyword / Trigger Traits: ([Vorpal], [Searing], [Vampiric]), which trigger concrete status effects on Critical Successes without altering core numbers.
3. Immediate Next Steps & Iteration Roadmap
 Phase 1 Verification: Run probability simulation scripts (02_probability_and_dice_simulations.md) across all step sizes (d4 to d12) vs DCs 3, 5, 7, 9, 11 to confirm success curves and critical hit distributions.
 Phase 2 — Bestiary Expansion: Create a modular 10-monster bestiary converting iconic 3.5e creatures (Red Dragon, Mind Flayer, Beholder, Displacer Beast, Iron Golem) into mathless step blocks.
 Phase 3 — Spellbook Translation: Translate 20 core 3.5e / SotDL spells across the five Traditions (Arcana, Divine, Primal, Shadow, Time) into mathless opposed checks and zone conditions.
 Phase 4 — Playtest Module: Build a self-contained, 3-encounter tactical playtest module (The Crypt of the Iron Lord) complete with pre-generated characters, printable reference sheets, and step-by-step GM instructions.
Open
Pathfinder 2e & General Content Conversion Guidelines
MD
Pathfinder 2e & General Content Conversion Guidelines

Pathfinder 2e (PF2e) revolutionized modern tactical TTRPGs through its structured 3-Action Economy and its comprehensive Keyword / Trait Taxonomy. While PF2e still uses numerical modifiers (+2 Circumstance, -1 Status, Proficiency Level + 2), its structural architecture ports directly into our mathless engine with near-zero friction.

This document establishes the exact conversion guidelines for PF2e traits, 3-action feats, and general OSR / board game content.

1. Translating PF2e Weapon & Action Traits (Keyword Mapping)

In PF2e, every weapon, spell, and ability carries modular tags that dictate how it interacts with the rules ([Agile], [Reach], [Forceful]). We translate these keywords directly into Mathless Step and Pool Interactions:

PF2e Trait / Keyword	Traditional PF2e Rule	Converted Mathless Mechanical Effect
[Agile]	-4 MAP penalty instead of -5 on second attacks.	Stamina Efficiency: When making a second Strike ([1A]) on the same turn, you can spend 1 Stamina to ignore the +1 Bane multi-attack penalty entirely, rolling a full 2dX keep highest pool.
[Finesse]	Use Dexterity modifier instead of Strength for attack rolls.	Agility Substitution: You can roll your Agility Pool (2dAGI) instead of Might (2dMIG) when making melee attack checks.
[Forceful]	Gain circumstance bonus to damage (+2 / +4) on subsequent attacks on the same turn.	Momentum Step: When you hit with a second or third attack on the same turn, the weapon's Damage Die is stepped up one rank (d6 
→
→ d8 
→
→ d10) against the target's Soak Rank.
[Reach]	Weapon can attack targets 10 feet away (2 squares).	Zone Reach: You can make melee Strikes against targets in adjacent tactical sub-zones (up to 10-15 ft) without needing to spend [1A] to Stride closer.
[Sweep]	Gain +1 circumstance bonus on attacks against a different target than your last attack.	Multi-Target Advantage: When you Strike a different target than your previous action on the same turn, you gain 
+
1
 Boon Die (‘3dX keep highest‘)
+1 Boon Die (‘3dX keep highest‘).
[Deadly d8/d10]	On a critical hit, add an extra 1d8 or 1d10 damage roll.	Critical Severance: When your attack achieves a Critical Success (Rolled Max Face or Multi-Beat), your weapon automatically bypasses the target's Soak Rank entirely AND inflicts 2 Wound Conditions (Severed Tendon or Fractured Rib).
[Fatal d10/d12]	On a critical hit, the weapon's damage die size increases to d10 or d12 and rolls extra dice.	Lethal Overdrive: On a Critical Success, your weapon’s damage die steps up to d12 (Damage Die d12 vs Soak), guaranteeing maximum structural trauma (Mortal Wound Check triggered if Vitality < 8).
[Parry]	Can spend an action to raise defense (+1 AC).	Defensive Guard: When wielding this weapon, you can declare Raise Guard ([1A]) to roll your Parry Pool (2dParry) against incoming strikes, even if you are not wielding a shield.
2. Converting PF2e Class Feats & Action Abilities

Let's convert three signature PF2e tactical class feats into our mathless action budget ([1A], [2A], [3A], [R]):

Case Study 1: Sudden Charge (Barbarian / Fighter Feat)
PF2e Original Rule: [2 Actions] You Stride twice. If you end your movement within melee reach of at least one enemy, you can make a melee Strike against that enemy.
Mathless Converted Rule (Sudden Charge - Combat Maneuver):
Action Cost: [2A] Activity
Mathless Mechanic: You Stride (Move up to 2 Combat Zones / 60 ft) in a straight line toward an enemy. Upon stopping within reach, you immediately make a melee Strike ([0A] free) against them. Due to the built-up kinetic velocity, your attack pool gains 
+
1
 Boon Die (‘3dX keep highest‘)
+1 Boon Die (‘3dX keep highest‘) AND your Damage Die is stepped up one rank (d8 
→
→ d10) vs their Soak Rank.
Case Study 2: Flurry of Blows (Monk Class Feature)
PF2e Original Rule: [1 Action] Make two unarmed Strikes. If both hit the same monster, combine their damage.
Mathless Converted Rule (Flurry of Blows - Monk Talent):
Action Cost: [1A] Activity (Cost: 1 Stamina)
Mathless Mechanic: You unleash a rapid volley of martial strikes. Make two separate unarmed Strikes against a target within reach. Neither attack suffers the multi-attack Bane penalty (Both roll base 2dAGIor2dMIG keep highest). If both attacks hit, the target’s Soak Rank is stepped down one rank (Soak d8 
→
→ Soak d6) against the second hit due to cumulative physical shock.
Case Study 3: Shield Block (General Reaction Feat)
PF2e Original Rule: [Reaction] Trigger: While you have your shield raised, you take physical damage. You snap your shield in place to deflect a blow. Your shield prevents damage equal to your shield’s Hardness. You and the shield each take any remaining damage.
Mathless Converted Rule (Active Shield Block - Defense Reaction):
Action Cost: [1R] Reaction (Trigger: An attack beats your Evasion/Parry)
Mathless Mechanic: You interpose your raised shield to absorb the kinetic brunt of the blow. You make an immediate Soak Check using your Shield's Die (d8 or d10) instead of your armor. If the attack still beats your Shield Die, you can declare a Heroic Item Sacrifice, absorbing 100% of the remaining impact by splintering 1 Durability Slot off your shield (0 HP lost, 0 Wounds).
3. General OSR / d20 & Board Game Porting Guidelines

Our mathless engine is designed to act as a Universal Translation Layer for tabletop content. When porting content from Old School Renaissance (OSR) adventures, Gloomhaven, or Lands of Evershade, apply these simple heuristics:

3.1 OSR Adventures (OSRIC, B/X, Old-School Essentials)
Target DCs & Saving Throws: Convert old-school target numbers (Save vs Poison 14, Open Doors 1-2 on d6) into mathless DCs:
Easy/Routine task = DC 3 to 5
Standard/Challenging task = DC 6 to 7
Hard/Severe task = DC 8 to 9
Lethality & Traps: OSR traps (Pit Trap - 2d6 damage) directly test vs Evasion (2dAGI vs DC 7). If failed, the fall inflicts a Sprained Joint or Fractured Rib Wound Condition plus d8 Damage vs Soak.
3.2 Board Game Card Abilities (Gloomhaven / Lands of Evershade)
When adapting a tactical card ability (e.g., Gloomhaven: Attack 4, Range 3, Pull 2), convert the card into a Mathless Action Option ([1A] or [2A]) with a concrete Stamina cost:
Converted Ability: [2A] Grappling Harpoon (Cost: 1 Stamina). Make a ranged Strike (3 Zones). If hit (Damage Die d8 vs Soak), you immediately pull the target 1 Combat Zone closer to you without an opposed check.
Open
Demon Lord System (SotDL / Weird Wizard) Conversion Procedure
MD
Demon Lord System (SotDL / Weird Wizard) Conversion Procedure

Robert J. Schwalb’s Shadow of the Demon Lord (SotDL) and Shadow of the Weird Wizard serve as our secondary architectural anchors. Their signature contribution—replacing flat numerical modifiers (+2 / -2) with dynamic Boons and Banes (Nd6)—and their 3-Tier Modular Path Architecture (Novice -> Expert -> Master) provide the exact modular blueprint needed to build a high-content, option-rich mathless system.

This document details the exact procedures for translating SotDL/Weird Wizard content into our Mathless Step Pool Engine.

1. Translating Boons & Banes Without 
𝑑
6
d6 Addition

In SotDL, when a character has a situational advantage, they roll 
1
𝑑
20
+
Attribute Modifier
+
Highest of 
𝑁
𝑑
6
1d20+Attribute Modifier+Highest of Nd6. While vastly cleaner than 3.5e, this still requires table-side addition (
𝑑
20
±
𝑑
6
d20±d6).

We port the SotDL boon/bane engine into our system by converting the extra 
𝑑
6
d6 into Step Pool Volume Adjustments (+1d / -1d of your base step die):

SotDL / Weird Wizard Mechanic	Mathless Converted Pool Shift	Tactical & Mathematical Equivalent
+1 Boon (Roll 
+
1
𝑑
6
+1d6, add highest)	
+
1
 Boon Die (‘+1B‘)
+1 Boon Die (‘+1B‘): Add 
+
1
 die
+1 die of your current step rank to the pool (2dX 
→
→ 3dX keep highest).	Increases your average rolled face by 
≈
20
%
≈20%, virtually eliminating critical fumbles without changing the max ceiling.
+2 Boons (Roll 
+
2
𝑑
6
+2d6, add highest)	
+
2
 Boon Dice (‘+2B‘)
+2 Boon Dice (‘+2B‘): Roll 4dX keep highest.	Represents overwhelming advantage; standard DC 5-7 checks become almost guaranteed successes.
+3 Boons or more	
+
3
 Boon Dice (‘+3B‘)
+3 Boon Dice (‘+3B‘): Roll 5dX keep highest.	Maximum pool volume cap.
-1 Bane (Roll 
+
1
𝑑
6
+1d6, subtract highest)	
+
1
 Bane Die (‘+1X‘)
+1 Bane Die (‘+1X‘): Remove 
−
1
 die
−1 die from your check pool (2dX 
→
→ 1dX single die roll).	Strips away safety net; forces the character to rely purely on raw die size (X).
-2 Banes (Roll 
+
2
𝑑
6
+2d6, subtract highest)	
+
2
 Bane Dice (‘+2X‘)
+2 Bane Dice (‘+2X‘): Roll 2dX keep LOWEST (Disadvantage).	Represents severe tactical impairment (blindness, heavy cover, physical restraint).
-3 Banes or more	
+
3
 Bane Dice (‘+3X‘)
+3 Bane Dice (‘+3X‘): Roll 3dX keep LOWEST.	Extreme tactical jeopardy; clearing anything above DC 4 requires extreme luck or Hyper-Shifting.
2. Converting the 3-Tier Path Architecture (Novice, Expert, Master)

In place of 20-level linear classes or rigid prestige class prerequisite chains, our system adopts SotDL's 3-Tier Path architecture. A character's identity is constructed by layering three modular Paths chosen at specific milestones.

text
[ Character Build: Modular Path Layering ]
  ├── Novice Path (Chosen at Milestone 1: Core Archetype)
  │     └── Grants baseline step dice, core domain proficiencies, and basic combat recovery.
  ├── Expert Path (Chosen at Milestone 3: Professional Specialization)
  │     └── Grants domain `+2B` mastery, specialized maneuvers, or intermediate spell traditions.
  └── Master Path (Chosen at Milestone 6: High-Concept Paragon)
        └── Grants legendary capability unlocks, free `Hyper-Shifting`, and mythic powers.
2.1 Sample Converted Path: The Berserker (Expert Path)

Let's convert the iconic SotDL Berserker path into our mathless mechanics:

Path Tier: Expert Combat Path
Entry Requirement: Trained (+1B) in Combat Mastery and MIG d8+.
Level 3 Talent: Berserk Fury (Stamina Surge)
Mathless Mechanic: As a [0A] Free Trigger on your turn, you can spend 2 Stamina to enter a Berserk Fury. For the next round, all of your melee Strikes gain 
+
2
 Boon Dice (‘4dX keep highest‘)
+2 Boon Dice (‘4dX keep highest‘) and your Soak Rank steps up one step (d8 
→
→ d10). However, your blind aggression leaves you exposed: all incoming attacks targeting your Evasion or Parry gain 
+
1
 Boon Die (‘3dX‘)
+1 Boon Die (‘3dX‘).
Level 6 Talent: Unstoppable Juggernaut (Wound Resistance)
Mathless Mechanic: While in a Berserk Fury, you are completely immune to the Shaken, Prone, and Muddled status conditions. Furthermore, when an enemy strike inflicts a Severe Lethal Wound (0 Vitality or Critical Hit), you can make a Resilience Check (DC 7). On a success, you ignore the wound condition entirely and stabilize at 1 Vitality, continuing your onslaught.
3. Translating Spell Traditions & Dark Fantasy Tracks

SotDL organizes magic into discrete Traditions (Fire, Shadow, Time, Forbidden, Necromancy) rather than massive generic spell lists. We adopt this directly: each Tradition operates as a distinct Action Mastery Domain linked to Intellect or Will.

3.1 The Corruption & Insanity Tracks (Zero Math Degradation)

To capture SotDL’s gritty dark fantasy atmosphere without numerical tracking (Tracking 1 to 20 Insanity points), we implement them as In-World Step Degradation Tracks:

The Insanity Clock (6-Step Mental Stress)

Whenever a character witnesses cosmic horror, reads forbidden tomes, or experiences immense psychological trauma, the GM requires a Will Resilience Check (2dWIL keep highest vs Horror DC 6-9).

On a Failure: Check off 1 Step on your personal Insanity Clock ([●] [○] [○] [○] [○] [○]).
Mechanical Effect: When your clock reaches 3 Steps (Halfway), your Intellect and Will step dice suffer a permanent Down-Shift (d10 
→
→ d8) during social and analytical tasks. When all 6 Steps fill, your character suffers a Permanent Quirky Madness / Mania (or rolls on the Weird Wizard Quirks table) and the clock resets to zero.
The Corruption Track (Dark Magic & Moral Decay)

Whenever a character casts a spell from the Forbidden or Necromancy traditions, or commits an unspeakable act of cruelty, they gain a Corruption Mark.

Mathless Effect: Each Corruption Mark grants 
+
1
 Boon Die (‘+1B‘)
+1 Boon Die (‘+1B‘) when rolling intimidation or casting dark magic, BUT imposes 
+
1
 Bane Die (‘+1X‘)
+1 Bane Die (‘+1X‘) when interacting with natural beasts, holy sanctuaries, or healing miracles. At 3 Corruption Marks, the character develops a physical Gothic Deformity (Horns, Pale eyes, Necrotic scent).
Open
D&D 3.5e Conversion Procedure & Translation Pipeline
MD
D&D 3.5e Conversion Procedure & Translation Pipeline

Dungeons & Dragons 3.5e is our primary architectural anchor due to its unmatched library of character options, feats, prestige classes, and monster ecologies. However, 3.5e relies on heavy linear arithmetic (+X / -X modifiers).

This document provides exact, step-by-step conversion formulas to translate any 3.5e mechanical element into our Mathless Step Pool Engine (2dX keep highest) while preserving its tactical identity and simulationist flavor.

1. The Master Conversion Pipeline

To convert any 3.5e rule, identify its numerical vector and map it directly onto one of our five mathless mechanical vectors:

text
[ 3.5e Numerical / Arithmetic Rule ]
                 │
                 ▼
     [ What vector is modified? ]
                 │
   ┌─────────────┼─────────────┬─────────────┐
   ▼             ▼             ▼             ▼
[Flat +Bonus] [Feat/Maneuver] [Spell DC/Mod] [Monster Stat]
   │             │             │             │
   ▼             ▼             ▼             ▼
Pool Boon     Step Shift /  Resilience   Step Die &
(`+1d/2d`)    Action Cost   Opposed Pool  Soak Rank
1.1 Numerical Translation Matrix
3.5e Numerical Concept	Mathless Equivalent / Translation Rule	Why This Works Without Math
+1 to +2 Attack / Skill Bonus<br>(e.g., Weapon Focus, Skill Focus)	
+
1
 Boon Die (‘+1B‘)
+1 Boon Die (‘+1B‘) added to the pool (3dX keep highest).	Adds reliability and higher average face rolls without raising the mathematical DC threshold.
+3 to +5 Attack / Skill Bonus<br>(e.g., Greater Weapon Focus, Synergy)	
+
2
 Boon Dice (‘+2B‘)
+2 Boon Dice (‘+2B‘) added to the pool (4dX keep highest).	Extremely consistent performance; virtually eliminates low whiffs (rolling below 5).
-1 to -2 Attack / Skill Penalty	
+
1
 Bane Die (‘+1X‘)
+1 Bane Die (‘+1X‘) (1dX face roll).	Removes redundancy; forces the character to rely on raw unassisted die size.
-4 or greater Severe Penalty	
+
2
 Bane Dice (‘+2X‘)
+2 Bane Dice (‘+2X‘) (2dX keep lowest / Disadvantage).	Represents severe impairment or attacking through heavy cover/blindness.
Permanent Attribute Increase<br>(e.g., +2 Strength from leveling/belt)	Step Up Die Size (Up-Shift) of that Attribute (d6 
→
→ d8).	Raises the absolute capability ceiling, allowing the character to hit higher natural DCs.
Damage Bonus (+2 to +6 Damage)<br>(e.g., Weapon Specialization, High Str)	Step Up Weapon Damage Die (d6 
→
→ d8 
→
→ d10).	Higher die face easily overcomes heavier armor Soak Ranks without arithmetic addition.
Armor Class Bonus (+1 to +4 AC)<br>(e.g., Dodge feat, Ring of Protection)	Step Up Evasion or Parry Die (d8 
→
→ d10) OR add 
+
1
 Boon Die
+1 Boon Die when making defensive checks.	Directly elevates the number the attacker must beat on an opposed check.
Damage Reduction (DR 5/magic)	Soak Step Upgrade (+1 Soak Step) OR Immunity to d6/d8 weapons without critical hits.	Kinetic force below the threshold is cleanly absorbed (0 Wounds).
2. Feat Conversion Case Studies (Before & After)

Let's apply our conversion formulas to five iconic D&D 3.5e combat feats to demonstrate how mathematical chains become clean, mathless tactical choices:

Case Study 1: Power Attack
3.5e Original Text: On your action, before making attack rolls for a round, you may choose to subtract a number from all melee attack rolls and add the same number to all melee damage rolls. This number may not exceed your base attack bonus.
Mathless Converted Rule (Power Strike - Combat Feat):
Action Cost: [1A] Strike (Modified)
Mathless Mechanic: Before rolling a melee Strike with a two-handed or heavy weapon, you can declare a Power Strike. You take 
+
1
 Bane Die (‘1dMIG‘)
+1 Bane Die (‘1dMIG‘) on your attack roll. If the attack hits, your weapon's Damage Die is stepped up two ranks (d8 
→
→ d12) against the target's Soak Rank, and any hit is automatically treated as beating Soak by 
≥
1
≥1 step (Guaranteeing at least 1 Wound Condition).
Case Study 2: Cleave & Great Cleave
3.5e Original Text: If you deal a creature enough damage to make it drop (typically by dropping it to below 0 hit points or killing it), you get an immediate, extra melee attack against another creature within reach.
Mathless Converted Rule (Cleaving Momentum - Combat Feat):
Action Cost: [0A] Free Trigger
Mathless Mechanic: Whenever your melee Strike inflicts a Severe Lethal Wound OR drops an enemy's Vitality to 0, your weapon's momentum carries through. You immediately make one free melee Strike against an adjacent enemy within your reach. Great Cleave: If that secondary hit also drops a target, the cleave continues to a third target without spending action points.
Case Study 3: Combat Expertise
3.5e Original Text: When you use the attack action or full attack action in melee, you can take a penalty of up to -5 on your attack roll and add the same number (+5 or less) as a dodge bonus to your Armor Class.
Mathless Converted Rule (Defensive Blade Stance - Combat Feat):
Action Cost: [1A] Stance / Active Defense
Mathless Mechanic: You adopt a defensive fencing stance. Until your next turn, all of your offensive melee Strikes roll with 
+
1
 Bane Die (‘1dX‘)
+1 Bane Die (‘1dX‘), but whenever an enemy attacks your Evasion or Parry, you roll your Parry Pool (2dParry) with 
+
2
 Boon Dice (‘4dParry keep highest‘)
+2 Boon Dice (‘4dParry keep highest‘), making your guard nearly impenetrable.
Case Study 4: Dodge & Mobility
3.5e Original Text: During your action, you designate an opponent and receive a +1 dodge bonus to Armor Class against attacks from that opponent. Mobility adds a +4 dodge bonus to Armor Class against attacks of opportunity caused when you move out of or within a threatened area.
Mathless Converted Rule (Skirmisher's Footwork - Combat Feat):
Action Cost: [0A] Passive Feature
Mathless Mechanic: Your agility in close quarters is legendary. Whenever you take a Stride ([1A]) action through an enemy's reach, any Attacks of Opportunity ([R]) made against you suffer 
+
2
 Bane Dice (‘2dX keep lowest‘ / Disadvantage)
+2 Bane Dice (‘2dX keep lowest‘ / Disadvantage). Furthermore, if an enemy misses you with an Attack of Opportunity, you gain 
+
1
 Boon Die
+1 Boon Die on your next check against them.
Case Study 5: Weapon Focus & Weapon Specialization
3.5e Original Text: Choose one type of weapon. You gain a +1 bonus on all attack rolls you make using the selected weapon. Specialization adds +2 bonus on all damage rolls.
Mathless Converted Rule (Weapon Master - Path Talent):
Action Cost: [0A] Passive Mastery
Mathless Mechanic: Choose a weapon category (Longswords, Bows). When attacking with this weapon, you automatically gain 
+
1
 Boon Die (‘+1B‘)
+1 Boon Die (‘+1B‘) to your attack pool (3dX keep highest). Furthermore, your mastery allows you to strike structural weak points: your weapon's Damage Die is permanently stepped up one rank (d8 
→
→ d10) against enemy Soak Ranks.
3. Spell & Magic Conversion Case Studies (Before & After)

In 3.5e, spellcasters calculate exact spell DCs (DC = 10 + Spell Level + Attribute Modifier) and roll large handfuls of damage dice (10d6 Fireball). We convert spells into Mathless Opposed Checks and Concrete Area Conditions.

Case Study 1: Fireball (3rd-Level Arcane Spell)
3.5e Original Text: A fireball spell generates a searing explosion of flame that detonates with a low roar and deals 1d6 points of fire damage per caster level (maximum 10d6) to every creature within the area. A Reflex save halves the damage.
Mathless Converted Rule (Searing Fireball - Arcane Spell):
Action Cost: [2A] Cast Spell (2 Focus cost)
Range & Area: Long Range (3 Zones / 120 ft); 1 Combat Zone Radius.
Mathless Mechanic: You unleash a detonation of searing flame across the target zone. You make an Arcane Power Check (2dINT keep highest) opposed separately by the Evasion Pool (2dAGI) of every creature in the zone.
Critically Failed Evasion (Or Rolled 1): The target takes Searing Lethal Fire (Damage Die d12 vs Soak) AND catches On Fire (Severe Burn Wound Condition - lose 2 Vitality per turn until doused).
Failed Evasion (Power > Evasion): The target takes Fire Damage (Damage Die d10 vs Soak) AND loses 2 Stamina from heat shock.
Successful Evasion (Evasion >= Power): The target dives for cover, absorbing the blast. They take zero Wounds (0 HP lost), but lose 1 Stamina from the physical exertion of dodging.
Case Study 2: Stinking Cloud (3rd-Level Conjuration Spell)
3.5e Original Text: Stinking cloud creates a bank of fog like that created by fog cloud, except that the vapors are nauseating. Living creatures in the cloud become nauseated (unable to attack, cast spells, or concentrate; can only take a single move action per turn) as long as they remain in the cloud and for 1d4+1 rounds after.
Mathless Converted Rule (Nauseating Fog - Conjuration Spell):
Action Cost: [2A] Cast Spell (2 Focus cost)
Range & Area: Medium Range (2 Zones); 1 Zone Radius Clock (Sustained via 1 Focus/round).
Mathless Mechanic: A dense, putrid yellow fog fills the zone, obscuring sight (All targets Blinded). Every living creature starting their turn inside the cloud must make an opposed Resilience Check (2dMIG keep highest vs your 2dINT Power Pool):
Failed Resilience: The target is overcome by violent retching (Muddled Condition). They immediately lose 2 Stamina and can only spend [1A] total on their turn (Cannot Strike or Cast Spells). This condition persists for 2 rounds after exiting the fog.
Successful Resilience: The target holds their breath and resists the nausea (0 Conditions), but still suffers the visual blinding of the fog while inside.
4. Monster & Bestiary Conversion Pipeline

To convert a 3.5e monster block into our mathless engine in under 2 minutes, apply this structured mapping blueprint:

text
[ 3.5e Monster Profile (`Hit Dice, Armor Class, Attacks, Saves`) ]
                                 │
     ┌───────────────────────────┼───────────────────────────┐
     ▼                           ▼                           ▼
[ Attribute Steps ]     [ Defense & Soak Ranks ]   [ Attack & Damage Pools ]
3.5e Stat `10-13` -> `d6`  Armor Class -> Evasion/Parry  Attack Bonus -> Pool Boons
3.5e Stat `14-17` -> `d8`  Natural Armor -> Soak Step  Damage -> Step Die
3.5e Stat `18-21` -> `d10` Spell Resistance -> Will      (`2d6` -> `d8 Strike`)
3.5e Stat `22+`   -> `d12` DR -> Soak `d10-d12`
Case Study: Converting the Classic 3.5e Ogre
3.5e Base Stats: Large Giant (HD 4d8+12, HP 29), AC 16 (-1 Size, +1 Dex, +5 Natural, +1 Hide), Attack: Greatclub +8 melee (2d8+7), Fort +6, Ref +2, Will +1, Str 21 (+5), Dex 12 (+1), Con 15 (+2), Int 6 (-2), Wis 10 (0), Cha 7 (-2).
Converted Mathless Profile: Ogre Brute (Threat Level: Formidable)
Core Attribute Steps:
MIG d10 (Heroic giant muscle) | AGI d6 (Standard speed)
INT d4 (Impaired logic) | WIL d6 (Standard morale)
Defense & Soak Ranks:
Evasion Pool: 2d6 (Average dodge due to large frame)
Parry Pool: 2d8 (Heavy club parry)
Soak Rank: Soak d10 (Thick giant hide + leather apron. Impervious to basic d6 daggers without critical hits).
Resilience Pool: 2d10 keep highest (Massive metabolic fortitude against poisons/stun).
In-World Resource Pools:
Vitality (HP): 16 Vitality (MIG d10 + WIL d6)
Stamina Pool: 20 Stamina (Can Hyper-Shift checks 4 times before tiring)
Mathless Attack Actions ([1A]):
Crushing Greatclub ([1A] Melee Strike): Roll Combat Pool (2d10 + 1 Boon = 3d10 keep highest) vs Target Evasion or Parry.
Impact vs Soak: If hit, deals Damage Die d12 vs Soak Rank. On a critical hit (rolling 12), the blow knocks the target Prone and inflicts a Fractured Rib Wound Condition.
Sweeping Cleave ([2A] Area Surge): The Ogre swings its massive club in a wide arc across the zone. Make a single 3d10 check opposed by the Evasion Pool (2dAGI) of up to 3 adjacent targets simultaneously. All who fail take d10 Damage vs Soak and are pushed back 10 feet.
Open
In-World Resources, Conditions & Injury Modeling
MD
In-World Resources, Conditions & Injury Modeling

In strict accordance with our design philosophy, our system contains zero out-of-character meta-currencies. All survivability, stamina depletion, tactical trade-offs, and physical injuries are tracked using concrete in-world biological, psychological, and material tracks.

1. Master In-World Resource Tracks

Every character sheet tracks five physical/mental pools:

Resource Track	Maximum Capacity	Depleted By	Recovered By
1. Vitality (HP)	MIG Die Max + WIL Die Max<br>(e.g., 
8
+
6
=
14
8+6=14)	Weapon strikes that beat Soak Rank, environmental hazards, falling, blood loss.	Medical bandaging, natural rest, or divine miracles.
2. Stamina (Poise)	2 x MIG Die Max<br>(e.g., 
2
×
8
=
16
2×8=16)	Hyper-Shifting checks (1 Stamina), physical surges/reactions (1-2 Stamina), absorbing minor kinetic impacts (1 Stamina/wound).	Short Breather / Rally (10 minutes): Recover 100% Stamina instantly once out of immediate danger.
3. Focus (Acuity)	2 x INT or WIL Die Max<br>(e.g., 
2
×
10
=
20
2×10=20)	Casting complex spells (1-3 Focus), sustaining arcane concentration (1 Focus/round), Hyper-Shifting mental/social checks.	Short Breather / Meditation (10 minutes): Recover 100% Focus when resting quietly without distraction.
4. Durability Slots	1 to 4 Slots per Item<br>(Based on item material)	Heroic Item Sacrifice (Absorb Critical Hit), critical parry clashes, acid/rust hazards.	Blacksmith repair at a forge (Downtime project clock).
5. Provisions (Rations)	Encumbrance Slots<br>(Typically 6 to 10 slots)	Daily wilderness travel, forced marches, surviving harsh climates (1 Provision per day/shift).	Foraging (Survival & Athletics check) or purchasing supplies in towns.
2. The Physiological Injury Model (Wound Conditions)

When a character takes damage that exceeds their Soak Rank (Damage Die > Soak Die), or when their Vitality (HP) reaches 0, they sustain a concrete Wound Condition.

Unlike abstract HP loss, every Wound Condition represents physical trauma that imposes specific Down-Shifts or Banes on relevant physical systems until treated.

2.1 Wound Taxonomy & Mechanical Effects
Wound Condition	Severity	Trigger / Source	Mathless Mechanical Penalty
Bleeding Cut	Minor	Slashing/piercing weapons exceeding Soak by 1 step.	Blood Loss: At the start of your turn, lose 1 Vitality. Removed immediately by a quick bandaging Interact ([1A]) action.
Sprained / Strained Joint	Minor	Bludgeoning weapons, falls, forced grapples.	Impaired Mobility: Your Speed is reduced by 10 feet. All Subterfuge & Navigation checks roll with 
+
1
 Bane Die (‘1dX‘)
+1 Bane Die (‘1dX‘).
Concussion / Head Trauma	Moderate	Bludgeoning critical hits, psychic blasts, explosions.	Sensory Disruption: Your Intellect and Will step dice suffer an immediate Down-Shift (d10 
→
→ d8). You cannot sustain concentration spells (Focus lock).
Fractured Rib / Cracked Armor	Moderate	Crushing blows beating Soak by 
≥
2
≥2 steps.	Respiratory Pain: Every time you spend Stamina to Hyper-Shift, you take 2 Vitality damage due to physical agony. Your armor loses 1 Durability Slot.
Severed / Punctured Tendon	Severe	Critical hits with bludgeoning/piercing weapons at 0 Vitality.	Lethal Impairment: One limb is rendered non-functional. If an arm, drop what you hold (Cannot wield 2-handed weapons or shields). If a leg, fall Prone (Cannot Stride normally).
Mortal Wound / Bleeding Out	Critical	Taking ANY damage while sitting at 0 Vitality.	Death Timer (3 Round Clock): You fall unconscious (Speed 0, zero actions). At the end of each round, make a Resilience Check (DC 6). On 3 successes, you stabilize at 1 Vitality with a severe injury. On 3 failures, your character expires.
3. Core Status Conditions (Binary & Step Flags)

To ensure clean tactical play, temporary status effects operate as binary flags or step overrides without modifier math:

Blinded: You cannot see. All checks relying on sight automatically fail. Melee and ranged attacks targeting you gain 
+
2
 Boon Dice (‘4dX keep highest‘)
+2 Boon Dice (‘4dX keep highest‘). Your attacks against others roll with 
+
2
 Bane Dice (‘2dX keep lowest‘)
+2 Bane Dice (‘2dX keep lowest‘).
Deafened: You cannot hear auditory cues or verbal spell commands. You roll with **$+1\text{ Bane Die}** on perception checks and cannot cast spells requiring vocal pitch precision without Will d8+`.
Exhausted / Fatigued: Your aerobic resources are completely spent (Stamina hit 0 after strenuous labor). All check pools suffer an immediate Down-Shift (d8 
→
→ d6). You cannot Hyper-Shift until you complete a Long Rest.
Muddled / Confused: Your thoughts are clouded by toxins or illusions. You cannot spend Focus or cast spells requiring more than [1A].
Prone: You are lying on the ground. You gain 
+
1
 Boon Die
‘
𝑣
𝑠
𝑟
𝑎
𝑛
𝑔
𝑒
𝑑
𝑎
𝑡
𝑡
𝑎
𝑐
𝑘
𝑠
(
‘
𝑆
𝑚
𝑎
𝑙
𝑙
𝑒
𝑟
𝑡
𝑎
𝑟
𝑔
𝑒
𝑡
‘
)
,
𝑏
𝑢
𝑡
𝑒
𝑛
𝑒
𝑚
𝑖
𝑒
𝑠
𝑚
𝑎
𝑘
𝑖
𝑛
𝑔
𝑚
𝑒
𝑙
𝑒
𝑒
𝑠
𝑡
𝑟
𝑖
𝑘
𝑒
𝑠
𝑎
𝑔
𝑎
𝑖
𝑛
𝑠
𝑡
𝑦
𝑜
𝑢
𝑔
𝑎
𝑖
𝑛
∗
∗
+1 Boon Die‘vsrangedattacks(‘Smallertarget‘),butenemiesmakingmeleestrikesagainstyougain∗∗+2\text{ Boon Dice (4dX)}$**. You can spend [1A] to Stand Up.
Restrained / Grappled: You are bound or held fast (Speed 0). You cannot use physical movement or two-handed weapons. Attacks against you roll with 
+
1
 Boon Die (‘3dX‘)
+1 Boon Die (‘3dX‘).
Shaken / Frightened: Your poise is broken by fear. You roll with 
+
1
 Bane Die (‘1dX‘)
+1 Bane Die (‘1dX‘) on all attack and check pools as long as the source of your fear is within line of sight.
4. Rest & Recovery Mechanics (In-World Healing)

Because our system rejects magical meta-currencies, recovering from injuries requires time, rest, and concrete medical or magical intervention.

text
[ Character Sustains Injury & Depletion ]
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
[ Short Breather / Rally ] [ Long Rest / Sleep ]
 (10 Minutes Out of Combat) (8 Hours Camp / Inn)
         │                   │
         ▼                   ▼
 Recover 100% Stamina      Recover 100% Vitality
 Recover 100% Focus        Heal 1 Minor Wound Condition
 (Does NOT heal Wounds)    (Requires Medical Care for Severe Wounds)
4.1 Short Breather / Rally (10 Minutes)
Requirement: The party stops resting, binds minor scrapes, and catches their breath in a secure area (0 combat activity).
Effect: Every character recovers 100% of their Stamina and Focus pools immediately.
Limit: Does not restore lost Vitality (HP) or cure concrete Wound Conditions.
4.2 Long Rest / Encampment (8 Hours)
Requirement: 8 hours of uninterrupted sleep or light watch duties, consuming 1 Provision Unit (Rations) per character.
Effect:
Recover 100% of maximum Vitality (HP).
Automatically cure all Minor Wound Conditions (Bleeding Cut, Sprained Joint).
If treated by a character with Trained/Mastered in Medicine (Lore & Crafting), cure one Moderate or Severe Wound Condition. Without medical treatment, severe injuries (Fractured Rib, Severed Tendon) persist across days until treated or magically healed.
Open
Skills, Complex Maneuvers & Generic Capabilities
MD
Skills, Complex Maneuvers & Generic Capabilities

In many d20 systems, skills are treated as abstract numerical buckets (+15 in Stealth, +22 in Crafting) that are rolled against increasingly inflated DCs. Our system models skills as Concrete Capabilities that govern what a character can physically or intellectually attempt, unlocking specific combat maneuvers and professional disciplines without arithmetic.

1. Skill Taxonomy & Mastery Tiers

Skills are specialized proficiencies within our five Action Mastery Domains (Combat, Survival & Athletics, Subterfuge & Navigation, Lore & Crafting, Social & Influence).

1.1 The Four Mastery Ranks

Investing character advancement into a skill elevates your Proficiency Tier, directly granting Boon Dice (+B) and unlocking Capability Thresholds:

Proficiency Tier	Pool Boon Granted	Capability Threshold & Narrative Permission
0. Untrained	0 (2dX base pool)	Can only attempt general tasks (Climb a tree, Recall common folklore). Cannot attempt complex specialized tasks (Open-heart surgery, Pick masterwork locks).
1. Trained	
+
1
 Boon Die
+1 Boon Die (3dX)	Competent professional (Craft iron weapons, Track through light rain). Unlocks baseline domain maneuvers.
2. Mastered	
+
2
 Boon Dice
+2 Boon Dice (4dX)	Elite specialist (Forging steel/mithril, Translating ancient runes, Disarming complex mechanical traps).
3. Legendary	
+
3
 Boon Dice
+3 Boon Dice (5dX) + Free Hyper-Shift	Mythic grandmaster (Forging adamantine/artifact blades, Surviving planar void, Performing impossible acrobatics). Once per scene, check pool is automatically stepped up (Up-Shift) for free.
2. Generic Capability Thresholds (Gating Without Math)

To preserve grounded simulationism, certain actions cannot be attempted by simply rolling lucky on a d20. They require an Explicit Capability Threshold (Minimum Step Die OR Minimum Proficiency Tier).

text
[ Attempting Complex Task: Disarm Masterwork Clockwork Trap ]
                          │
     ┌────────────────────┴────────────────────┐
     ▼                                         ▼
[ Untrained / d4 Rank ]                 [ Mastered Tier / d8+ Rank ]
     │                                         │
     ▼                                         ▼
AUTOMATIC FAILURE                      ASSEMBLE `4d8` POOL
(Lack of technical knowledge)          (Proceed to mathless check vs DC 8)
2.1 Sample Capability Gating
Deciphering Draconic Runes: Requires Trained in Arcana/Lore OR INT d8+. Untrained characters see only gibberish.
Picking a Master-Tumbler Lock: Requires Mastered in Subterfuge OR AGI d10+. Without the required tactile sensitivity, tools snap (Automatic Failure + Broken Lockpicks).
Lifting a Heavy Portcullis: Requires MIG d10+ OR spending 2 Stamina to Hyper-Shift from d8 to d10. A character with MIG d4 physically cannot lift it regardless of rolled faces.
3. Combat & Tactical Maneuver Unlocks

Investing in Combat Mastery or Survival & Athletics does not just add dice; it unlocks specific Combat Maneuvers that operate seamlessly inside the 3-action economy ([1A]).

3.1 Physical Maneuvers (Opposed Base Checks)
Shove / Push ([1A]):
Requirement: Trained in Athletics/Combat.
Mechanic: Opposed check (Attacker MIG Pool vs Defender MIG or AGI Pool). If Attacker wins, the defender is pushed back 1 Combat Zone (30 ft) or knocked off balance (Takes +1 Bane Die on next check).
Grapple / Restrain ([1A]):
Requirement: Trained in Athletics/Combat.
Mechanic: Opposed check (Attacker MIG Pool vs Defender Evasion or MIG Pool). If Attacker wins, the defender becomes Restrained (Speed 0, all attacks against them gain 
+
1
 Boon Die
+1 Boon Die). To escape, the defender must spend [1A] and win an opposed check on their turn.
Trip / Sweep ([1A]):
Requirement: Trained in Athletics/Combat.
Mechanic: Opposed check (Attacker AGI or MIG Pool vs Defender Evasion Pool). If Attacker wins, the defender falls Prone (Melee attacks against them roll 4dX keep highest).
Disarm ([1A]):
Requirement: Mastered in Combat.
Mechanic: Opposed check (Attacker Combat Pool vs Defender Parry Pool). If Attacker wins, the defender's weapon flies into an adjacent zone (Unarmed).
3.2 Subterfuge & Psychological Maneuvers
Feint ([1A]):
Requirement: Trained in Subterfuge.
Mechanic: Opposed check (Attacker AGI Pool vs Defender INT/Perception Pool). If Attacker wins, the defender is thrown off guard; the attacker's next melee Strike against them completely bypasses their Parry layer (testing directly against Evasion or Soak).
Demoralize / Intimidate ([1A]):
Requirement: Trained in Social/Influence.
Mechanic: Opposed check (Attacker WIL Pool vs Defender Resilience/Will Pool). If Attacker wins, the defender is Shaken (Takes +1 Bane Die on all checks for 1 round). If Attacker rolls a Critical Success, the defender flees or drops their weapon in terror.
4. Crafting & Project Resolution (Mathless Step Clocks)

Instead of calculating gold piece progress formulas (Item cost x DC x Check result in silver pieces), crafting weapons, armor, or alchemical remedies uses Mathless Step Clocks (4-Step or 6-Step Clocks).

text
[ Masterwork Sword Crafting Clock: 6 Steps ]
  [○] [○] [○] [○] [○] [○]
The GM sets a Project Clock Size based on item complexity (4 Steps for iron blades/potions, 6 Steps for steel/masterwork, 8 Steps for adamantine/enchanted gear).
The character spends a Work Unit (1 Day or 1 Downtime Shift) and makes a Lore & Crafting check against the item's baseline DC (DC 5 to 9).
Mathless Clock Progression:
Critical Success: Fill 3 Clock Steps ([●] [●] [●]).
Standard Success: Fill 1 Clock Step ([●]).
Standard Failure: Fill 0 Steps. No progress made, but materials are safe.
Critical Failure: Lose 1 Clock Step (Ruined progress) OR ruin half of the raw materials (Material Loss).
Once all steps on the clock are filled ([●] [●] [●] [●] [●] [●]), the item is completed and added to the character's inventory with full Durability Slots.
Open
Simulationist Defense Architecture & Damage Modeling
MD
Simulationist Defense Architecture & Damage Modeling

In our idealized system, resolving an attack does not rely on comparing a single 
𝑑
20
d20 roll against an abstract Armor Class number. Instead, combat resolution respects the physical reality of an attack’s trajectory, momentum, and impact across Four Defensive Layers.

1. The Four Defensive Layers

When an attacker declares an offensive action, the target checks the layer appropriate to the attack's nature:

text
                      [ Incoming Attack Declared ]
                                   │
              ┌────────────────────┴────────────────────┐
              ▼                                         ▼
    [ Physical Kinetic Strike ]                 [ Magical / Metabolic Threat ]
              │                                         │
     ┌────────┴────────┐                       ┌────────┴────────┐
     ▼                 ▼                       ▼                 ▼
[ Evasion Layer ] [ Parry Layer ]      [ Resilience Layer ] [ Soak Layer ]
 (Ranged/Area/Fast) (Melee Clash)       (Poison/Mind/Curse)  (Direct Energy Hit)
1.1 Layer 1: Evasion (AGI-Derived Dodge Pool)
Used Against: Ranged weapon projectiles (arrows, bolts, thrown spears), area explosions (Fireball, Alchemical Bomb), and sweeping environmental hazards.
Mechanic: The attacker rolls their AGI + Weapon pool. The defender rolls their Evasion Pool (2dAGI keep highest).
If Attacker Highest 
≥
≥ Defender Highest: The projectile lands in the target's space (Hit $\to$ Check Soak).
If Attacker Highest < Defender Highest: The defender dodges cleanly (Miss / 0 Impact).
1.2 Layer 2: Parry (Combat Mastery Intercept)
Used Against: Melee weapon strikes (swords, axes, polearms, unarmed brawling).
Mechanic: If the defender has Raised Shield ([1A]) or spends 1 Stamina ([1R]) to react, they make an opposed Parry Check using their Combat Mastery pool (2dParry).
If Defender Highest 
≥
≥ Attacker Highest: The weapon is deflected, blocked, or parried cleanly (0 Impact). If the defender rolls a Critical Success on Parry, they can instantly perform a free Disarm or Shove against the attacker (Riposte).
If Attacker Highest > Defender Highest: The attack breaks past the parry (Hit $\to$ Check Soak).
1.3 Layer 3: Soak Rank (Armor & Physical Hide Step)
Used Against: Any physical or kinetic attack that beats Evasion or Parry.
Mechanic: Unlike AC, Soak is checked after a hit occurs. Every piece of armor provides a Soak Step Die (d4 Cloth 
→
→ d12 Full Plate). The attacker rolls their Weapon Damage Die against the defender's Soak Die.
2. Mathless Damage & Wound Resolution (Damage vs Soak)

In traditional d20 games, damage resolution involves subtracting armor damage reduction (DR) from rolled HP (8 damage - 3 DR = 5 HP lost). We eliminate subtraction entirely by comparing the Attacker's Damage Die Face against the Defender's Soak Die Face:

Impact Check: 
max
⁡
(
Weapon Damage Die Faces
)
 vs 
max
⁡
(
Soak Die Faces
)
Impact Check: max(Weapon Damage Die Faces) vs max(Soak Die Faces)

2.1 The Mathless Wound Matrix
Damage Die vs Soak Die	Physical Outcome & Wound Severity
Damage Face < Soak Face	Absorbed (0 Wounds): The armor or thick hide absorbs the kinetic impact. The defender loses 1 Stamina due to jarring vibration, but suffers zero physical tissue damage (No HP loss).
Damage Face == Soak Face	Superficial Impact (Minor Shock): The blow bruises tissue through the armor. The defender loses 2 Stamina (or 2 Vitality if Stamina is 0), but takes no structural Wound Condition.
Damage Face > Soak Face<br>(By normal face roll)	Standard Hit (1 Wound Condition): The strike penetrates or bludgeons through armor. The defender loses Vitality equal to the Damage Die face AND sustains 1 Minor Wound Condition (Bleeding Cut, Sprained Joint, Bruised Rib).
Critical Damage Hit<br>(Damage Die rolled Max Face OR 
≥
2
≥2 steps over Soak)	Severe Lethal Wound (2 Wound Conditions + Impairment): The strike cleaves deep. The defender loses Double Vitality (Max Face x 2) AND sustains a Severe Wound Condition (Severed Tendon, Cracked Skull, Punctured Lung), imposing an immediate Down-Shift on all physical actions until treated.
3. Armor Taxonomy & Soak Step Table

Different armor categories provide distinct trade-offs between physical Soak Step Ranks, Evasion Banes (due to bulk and weight), and Durability Slots.

Armor Category	Soak Step Die	Evasion / Agility Modifier	Durability Slots	Tactical Role
Unarmored / Clothing	d4	Normal (0 Banes)	0	High mobility, spellcaster baseline.
Light Armor (Leather/Hide)	d6	Normal (0 Banes)	1	Skirmishers, rogues, rangers (Soak d6).
Medium Armor (Chain/Scale)	d8	
+
1
 Evasion Bane Die (‘1dAGI‘)
+1 Evasion Bane Die (‘1dAGI‘)	2	Balanced infantry, warriors (Soak d8).
Heavy Plate Armor	d10	
+
2
 Evasion Bane Dice (‘2dAGI keep lowest‘)
+2 Evasion Bane Dice (‘2dAGI keep lowest‘)	3	Frontline juggernauts; almost immune to d6 weapons without crits (Soak d10).
Adamantine / Mythic Plate	d12	
+
2
 Evasion Bane Dice (‘2dAGI keep lowest‘)
+2 Evasion Bane Dice (‘2dAGI keep lowest‘)	4	Legendary defensive bastion (Soak d12).
4. Layer 4: Resilience (WIL / MIG Fortitude Pool)

When targeted by non-kinetic or internal threats (poisons, disease, mind blasts, petrification, divine curses), physical Evasion and armor Soak are irrelevant (Soak = 0 vs Mind Blast).

Opposed Resilience Check: The caster or hazard rolls its Power Pool (2dINT or 2dPower) against the defender's Resilience Pool (2dWIL or 2dMIG keep highest).
Outcome:
Resilience 
≥
≥ Power: The defender shrugs off the effect (0 Conditions).
Resilience < Power: The effect takes hold (Poisoned, Charmed, Paralyzed).
Critical Failure on Resilience: The effect's duration doubles or escalates to a lethal stage (Petrified, Dying).
Open
Action Economy & Turn Structure
MD
Action Economy & Turn Structure

To achieve the tactical depth and combat fluidity of Pathfinder 2e without tracking numerical modifiers across multiple turns, our system adopts a streamlined 3-Action Economy supported by Mathless Tactical Positioning and Dynamic Reactions.

1. Initiative & Round Structure

Combat is divided into Rounds, each representing roughly 6 seconds of intense tactical exchange. Within a round, characters take Turns based on initiative order.

1.1 Mathless Initiative Check

At the start of a combat encounter, every participant makes an Initiative Check:

Physical Ambush / Quick Reflexes: Roll your base Agility Pool (2dAGI).
Tactical Assessment / Prepared Trap: Roll your base Intellect Pool (2dINT).

Instead of writing down numbers (24, 18, 12), initiative order is sorted directly by the Highest Rolled Face Value from highest (12) to lowest (2).

Ties: Break ties by checking the second die in the pool (Secondary Tiebreaker). If still tied, player characters act before NPCs.
2. The 3-Action Economy ([A] [A] [A])

On their turn, every character has exactly Three Action Points (3 Actions) to spend. They can spend these points in any order, choosing from Single Actions ([1A]), Two-Action Activities ([2A]), or Three-Action Surges ([3A]).

text
[ Character Turn Budget: 3 Action Points ]
  ├── [1A] Move / Stride (Move 1 zone / 30 ft)
  ├── [1A] Strike (Melee/Ranged weapon attack pool)
  ├── [1A] Tactical Maneuver (Shove, Disarm, Feint, Demoralize)
  ├── [1A] Raise Shield / Prepare Parry (Activate Parry Defense pool)
  ├── [2A] Cast Standard Spell (Channel arcane/divine magic)
  └── [3A] Devastating Flourish (Special attack + movement surge)
2.1 Why No Multiple Attack Penalty (MAP) Arithmetic?

In Pathfinder 2e, making a second attack on the same turn imposes a -5 penalty (-4 with agile weapons), and a third attack imposes -10. While effective for balancing actions, this requires heavy numerical subtraction every round.

2.2 Our Mathless Multi-Action Solution: Pool Fatigue (Banes)

Instead of subtracting numbers (-5 / -10), making multiple physical attacks or strenuous checks within the same turn imposes Stamina / Pool Fatigue:

First Attack / Check ([1A]): Rolled with normal pool (2dX keep highest).
Second Attack on Same Turn ([1A]): Rolled with 
+
1
 Bane Die
+1 Bane Die (1dX face roll, or spend 1 Stamina to Hyper-Shift back to 2dX).
Third Attack on Same Turn ([1A]): Rolled with 
+
2
 Bane Dice
+2 Bane Dice (2dX keep lowest / Disadvantage, representing physical exhaustion and overextension).
3. Core Action Catalog
Single Actions ([1A])
Stride / Move ([1A]): Move up to your character's Speed (Standard: 30 feet or 1 Combat Zone).
Strike ([1A]): Make a melee or ranged attack against a target within reach/range using your Combat Mastery pool against their Evasion or Parry.
Raise Shield / Active Defense ([1A]): Position your shield or weapon defensively until the start of your next turn. While active, you can roll your Parry Pool (2dParry) to intercept any incoming melee or ranged physical attacks without spending Stamina.
Tactical Maneuver ([1A]): Attempt an opposed check (Shove, Grapple, Trip, Disarm, or Demoralize).
Grapple / Trip vs Evasion: If successful, the target is Prone or Restrained.
Demoralize vs Will: If successful, the target takes 
+
1
 Bane Die
+1 Bane Die on their next action due to fear/shaken poise.
Interact / Use Item ([1A]): Draw a weapon, drink an elixir, open a door, or pull a lever.
Two-Action Activities ([2A])
Cast a Spell ([2A]): Channel arcane, divine, or primal energy to manifest a standard spell (Fireball, Cure Wounds).
Charge / Pounce ([2A]): Stride up to double your Speed in a straight line and immediately make a melee Strike with 
+
1
 Boon Die
+1 Boon Die (3dX keep highest) due to built-up kinetic momentum.
Aim / Careful Shot ([2A]): Spend [1A] aiming and [1A] firing. Your ranged Strike gains 
+
2
 Boon Dice
+2 Boon Dice (4dX keep highest), almost guaranteeing a high face hit on distant targets.
Three-Action Surges ([3A])
Full Defense Stance ([3A]): Forfeit all offensive actions to brace yourself. Until your next turn, all attacks targeting your Evasion or Parry roll with 
+
2
 Bane Dice
+2 Bane Dice (2dX keep lowest), and your Soak Rank is stepped up (d6 
→
→ d8).
4. Tactical Positioning Without Numerical Modifiers (No +2s)

In 3.5e, tactical positioning adds small conditional bonuses (+2 Flanking, +4 Cover, -2 High Ground). We convert these directly into Pool Volume Boons and Banes:

Tactical Situation	Traditional d20 Modifier	Our Mathless Pool Interaction
Flanking / Surrounding	+2 to Attack	Attacker gains 
+
1
 Boon Die
+1 Boon Die (3dX keep highest). The defender’s attention is split across multiple threat angles.
Partial Cover (Obstacle / Trees)	+4 to AC	Attacker takes 
+
1
 Bane Die
+1 Bane Die (1dX). The obstacle breaks line of sight or deflects projectiles.
Heavy Cover / Arrow Slit	+8 to AC	Attacker takes 
+
2
 Bane Dice
+2 Bane Dice (2dX keep lowest). Hitting the exposed area requires incredible luck.
High Ground / Elevated Strike	+1 to Attack	Attacker gains 
+
1
 Boon Die
+1 Boon Die (3dX). Gravity and reach favor the downward strike.
Prone Target (Melee Attack)	+4 to Attack	Melee Attacker gains 
+
2
 Boon Dice
+2 Boon Dice (4dX). Target cannot easily evade on the ground.
Prone Target (Ranged Attack)	-4 to Attack	Ranged Attacker takes 
+
1
 Bane Die
+1 Bane Die (1dX). Target presents a significantly smaller profile.
5. Reactions & Out-of-Turn Interventions ([R])

Every character gets exactly One Reaction Slot ([1R]) per round, which resets at the start of their turn. Reactions allow out-of-turn tactical counter-play without requiring meta-currencies.

5.1 Standard Reactions
Attack of Opportunity ([R]): Triggered when an adjacent enemy leaves your melee reach without using a careful Step/Disengage action ([1A]), or when they cast a spell without defensive casting. You make an immediate single melee Strike ([1A]) against them.
Active Parry Intercept ([R]): If you did not Raise Shield ([1A]) on your turn, you can spend your [1R] slot and 1 Stamina to instantly make an opposed Parry Check against an incoming strike.
Shield Block / Armor Sacrifice ([R]): When an attack hits and beats your Soak Rank, you can spend your [1R] to absorb the blow using your shield/armor's Hardness, potentially splintering 1 Durability Slot to prevent a severe Wound Condition entirely (Sacrifice Item).
Open
Character Schema & Core Stat Architecture
MD
Character Schema & Core Stat Architecture

This document maps out the comprehensive data schema for player characters and NPCs in our idealized TTRPG system. Every character attribute, capability, defense, and resource is structured to operate seamlessly with our mathless 2dX resolution engine.

1. Core Innate Attributes (Step Dice)

Every character is defined by four fundamental Attributes. Each Attribute is rated as a Step Die (d4 to d12), representing the character's natural biological, intellectual, or spiritual potential.

Attribute	Abbr.	Represents	Typical Applications
Might	MIG	Raw physical strength, muscle density, kinetic force, and carrying capacity.	Melee weapon strikes, lifting/breaking doors, resisting forced movement.
Agility	AGI	Reflexes, balance, manual dexterity, coordination, and speed.	Ranged weapon attacks, dodging/evasion, acrobatics, sleight of hand, stealth.
Intellect	INT	Memory, deduction, sensory perception, education, and arcane resonance.	Investigating clues, recalling ancient lore, casting complex arcane spells.
Will	WIL	Mental fortitude, emotional poise, spiritual resolve, and social presence.	Resisting fear/mind control, casting divine/primal miracles, commanding respect.
Attribute Step Scale
d4 (Impaired / Childlike): Below average capacity; requires Hyper-Shifting (Stamina spend) to accomplish standard DC 6 tasks.
d6 (Standard Adult): Normal baseline competence.
d8 (Professional / Athlete): Advanced training and innate vigor.
d10 (Heroic / Elite): Peak mortal prowess; routinely clears DC 8-9 challenges.
d12 (Legendary / Paragon): Superhuman or mythological mastery.
2. Action Mastery Domains & Skills

To prevent skill list bloat while maintaining 3.5e/PF2e depth, our system groups skills into five Action Mastery Domains. Each domain has a baseline Domain Rank (Step Die) linked to an Attribute, plus specific Skill Proficiencies that grant Pool Volume Boons (+B).

2.1 The Five Mastery Domains
Combat Mastery (Linked to MIG or AGI): Covers all weapon categories, martial arts, shield techniques, and battlefield maneuvers (Shove, Disarm, Grapple).
Survival & Athletics Domain (Linked to MIG or WIL): Covers climbing, swimming, jumping, tracking, foraging, and enduring harsh climates.
Subterfuge & Navigation Domain (Linked to AGI or INT): Covers stealth, lockpicking, trap disarming, acrobatics, and sailing/piloting.
Lore & Crafting Domain (Linked to INT): Covers history, arcana, medicine, alchemy, blacksmithing, engineering, and deciphering languages.
Social & Influence Domain (Linked to WIL or INT): Covers diplomacy, intimidation, deception, leadership, insight, and performance.
2.2 Skill Proficiency Interaction (Pool Volume Additions)

When a character attempts an action within a domain:

Untrained: Roll the base domain Attribute step pool (2dX keep highest).
Trained (+1B): If you possess a specific skill proficiency relevant to the task (e.g., Trained in Blacksmithing inside Lore & Crafting), add 
+
1
 Boon Die
+1 Boon Die (3dX keep highest).
Mastered (+2B): Elite specialization grants 
+
2
 Boon Dice
+2 Boon Dice (4dX keep highest).
Legendary Specialization (+3B + Free Hyper-Shift): Grandmastery grants 5dX keep highest AND allows a free Hyper-Shift once per scene without spending Stamina.
3. The Four Defense Scores (Mathless Mitigation Layers)

Instead of calculating a single abstract "Armor Class" (AC = 10 + Dex + Armor + Shield), characters possess four distinct defensive ranks. When an attacker declares a strike or spell, the GM or player checks which defense layer is targeted.

text
       [ Incoming Attack / Threat ]
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
  [ Physical Attack ]     [ Magical / Metabolic Threat ]
         │                   │
   ┌─────┴─────┐       ┌─────┴─────┐
   ▼           ▼       ▼           ▼
[Evasion]   [Parry] [Soak Rank] [Resilience]
  (Dodge)  (Deflect) (Armor Hit)  (Save vs Effect)
Defense Layer	Primary Attribute / Source	Target Comparison / Mechanics
1. Evasion	Derived directly from AGI Die size (e.g., AGI d8 
→
→ Evasion d8).	Used when dodging ranged projectiles, traps, or area explosions. The attacker's highest roll must meet or exceed the defender's Evasion face roll/rank.
2. Parry	Derived from Combat Mastery Die + Shield quality (d6 to d12).	Used when actively deflecting melee strikes. Opposed roll (Attacker Pool vs Defender Parry Pool). If Defender wins or ties, attack is deflected cleanly.
3. Soak Rank	Derived exclusively from Equipped Armor & Physical Hide (d4 Cloth 
→
→ d12 Plate).	Soak is checked ONLY when an attack hits. Compare the attacker's Damage Die against the defender's Soak Die (Damage vs Soak). If Damage <= Soak, the kinetic impact is absorbed completely (0 Wounds, minor Stamina loss). If Damage > Soak, a physical Wound Condition is sustained.
4. Resilience	Derived from WIL or MIG (d6 to d12).	Replaces 3.5e Fortitude/Will saves. Used to resist poisons, disease, mind control, and death curses via opposed 2dX check.
4. In-World Resource Tracks (Zero Meta-Currencies)

All spendable resources exist strictly within the fictional reality of the character. There are no out-of-character tokens (Inspiration, Fate Points).

4.1 Vitality Pool & Wound Conditions (HP & Injury)
Vitality (HP): Represents minor scrapes, cuts, physical shock, and luck. Starting Vitality equals MIG Die Max + WIL Die Max (e.g., d8 + d6 = 14 Vitality).
Wound Conditions (Concrete Injuries): When an attack beats a character's Soak Rank (Damage Die > Soak Die), or when Vitality drops to 0, the character takes a Wound Condition (Bleeding Cut, Fractured Arm, Concussion). Each Wound imposes a specific mechanical Down-Shift or Bane on relevant physical tasks until treated.
4.2 Stamina & Poise Pool (Exertion & Heroics)
Stamina Pool: Represents aerobic capacity, breath, muscle glucose, and tactical balance. Starting Stamina equals 2 x MIG Die Max (e.g., 2 x 8 = 16 Stamina).
Stamina Expenditures:
Hyper-Shift Action (1 Stamina): Step your check pool up one die rank (2d6 
→
→ 2d8) before rolling.
Emergency Evasion / Surge (2 Stamina): Take an immediate out-of-turn reaction to dodge or move 5 feet when targeted by an attack.
Absorb Kinetic Shock (1 Stamina per point): When an attack beats your Soak, you can burn Stamina to absorb the excess impact and prevent a severe Wound Condition.
4.3 Focus Track (Mental Acuity & Arcane Channeling)
Focus Pool: Represents mental discipline and magical energy concentration. Starting Focus equals 2 x INT or WIL Die Max.
Focus Expenditures: Used to cast spells, sustain magical concentration, or Hyper-Shift intellectual/social checks.
4.4 Equipment Durability & Sacrifice Slots
Durability Slots: Every weapon, shield, and armor piece has Durability Slots (1 to 4).
Heroic Sacrifice (In-World Tradeoff): When facing a lethal strike or critical hit, a character can declare an Armor/Shield Sacrifice. This instantly absorbs 100% of the incoming attack damage without costing Vitality or Wounds, but permanently destroys 1 Durability Slot of the item (e.g., Shield Splinters). If all slots are lost, the item breaks and is useless until repaired at a forge.
Open
Core Baseline System: The Mathless Resolution Engine
MD
Core Baseline System: The Mathless Resolution Engine

This document formalizes the rules for resolving all checks, attacks, spellcasting attempts, and opposed contests in our idealized TTRPG system. Every rule below operates without table-side arithmetic.

1. The Core Check Formula (2dX Keep Highest)

Whenever a character attempts an action with a chance of failure, the Game Master (GM) assigns a Target Number (DC) from 2 to 12.

To resolve the check:

Identify the character’s Die Size (X) for the relevant Attribute or Skill (d4, d6, d8, d10, or d12).
Assemble the Base Pool of two dice (2dX).
Apply any Boons or Banes to adjust pool volume (
+
1
𝑑
/
−
1
𝑑
+1d/−1d).
Roll the assembled dice and look at the single highest face value shown.
If the highest face value is greater than or equal to the DC, the check succeeds. No addition or subtraction is performed.

Result
=
max
⁡
(
Rolled Pool Faces
)
≥
Target DC
Result=max(Rolled Pool Faces)≥Target DC

2. Target Numbers & Capability Ceiling

Because there are no numerical modifiers added to the dice, the Target Number (DC) represents an absolute physical threshold:

Target Number (DC)	Difficulty Description	Required Die Size to Succeed Naturally
DC 3	Routine / Easy: A basic task under stress.	Any (d4+)
DC 5	Challenging: Requires competence or focus.	d6+ (Or d4 with Hyper-Shift)
DC 7	Formidable: Professional mastery required.	d8+ (Or d6 with Hyper-Shift)
DC 9	Heroic / Severe: A feat of elite prowess.	d10+ (Or d8 with Hyper-Shift)
DC 11	Legendary: Almost superhuman execution.	d12 (Or d10 with Hyper-Shift)
DC 12	Mythic / Absolute Ceiling: Peak mortal limit.	d12 only
3. Boons & Banes (Pool Volume Manipulation)

Instead of numerical adjustments (+2 / -2), situational factors, spells, and equipment quality grant Boons (+B) or impose Banes (+X).

3.1 Applying Boons and Banes

Before rolling, count all applicable Boons and Banes. They cancel each other out 1-to-1:

Net Pool Shift
=
Total Boons
−
Total Banes
Net Pool Shift=Total Boons−Total Banes

3.2 Pool Resolution Table
Net Shift	Pool Rolled	How to Determine Result
+3 Boons or more (+3B)	5dX	Roll 5 dice of your rank 
→
→ Keep the Single Highest Face.
+2 Boons (+2B)	4dX	Roll 4 dice of your rank 
→
→ Keep the Single Highest Face.
+1 Boon (+1B)	3dX	Roll 3 dice of your rank 
→
→ Keep the Single Highest Face.
0 (Normal Roll)	2dX (Base)	Roll 2 dice of your rank 
→
→ Keep the Single Highest Face.
-1 Bane (+1X)	1dX	Roll 1 die of your rank 
→
→ Take the Face Value Shown.
-2 Banes (+2X)	2dX	Roll 2 dice of your rank 
→
→ Keep the Single LOWEST Face (Disadvantage).
-3 Banes or more (+3X)	3dX	Roll 3 dice of your rank 
→
→ Keep the Single LOWEST Face.
4. Hyper-Shifting & Downshifting (Die Size Manipulation)

To allow characters to overcome hard mathematical caps (such as a 2d6 character attempting a DC 7 check) or push beyond normal limits through sheer physical exertion, characters can Hyper-Shift their die size.

4.1 Hyper-Shifting (Up-Shift)
Cost: Spend 1 point of physical Stamina (or mental Focus).
Effect: Step up the size of every die in your check pool by one rank for this single roll (d4 
→
→ d6 
→
→ d8 
→
→ d10 
→
→ d12).
Limit: A pool can normally only be Hyper-Shifted once per action unless a special mastery feat or class capability allows Double Hyper-Shifting.
4.2 Downshifting (Down-Shift)
Trigger: Certain severe conditions (Exhausted, Muddled, Suppressed) or enemy curses impose a Down-Shift rather than a Bane.
Effect: Step down the size of every die in your check pool by one rank (d10 
→
→ d8). If a d4 pool is Down-Shifted, the check automatically fails unless the character spends Stamina to Hyper-Shift back up to d4.
5. Opposed Rolls (Zero-Math Contests)

When two characters directly oppose one another (e.g., an attacker swinging a sword against a defender attempting to parry, or a grappler wrestling an opponent), no static DC is used.

Both characters assemble their pools (Attacker Pool vs Defender Pool), applying their respective Boons, Banes, and Stamina shifts.
Both roll simultaneously.
Compare the Highest Face Value of the Attacker against the Highest Face Value of the Defender:
Attacker Highest > Defender Highest: Attacker wins and achieves their action.
Attacker Highest < Defender Highest: Defender wins and completely intercepts/avoids the action.
Tie (Equal Highest Faces): Look at the Second-Highest Face Value in each pool (if available). The higher second face wins the tie (Secondary Tiebreaker). If still tied or neither has a second die, the Defender / Active Reactor wins the clash.
6. Degrees of Success & Mathless Criticals

Our system incorporates PF2e-style 4 Degrees of Success without requiring "+10 over the DC" arithmetic.

6.1 Determining Degrees of Success
Degree of Success	Mathless Trigger Condition
Critical Success	Condition A: Your highest die rolls its Maximum Face Value (8 on a d8, 12 on a d12) AND meets or exceeds the DC.<br>Condition B (Multi-Beat): Two or more dice in your pool independently meet or exceed the Target DC (e.g., rolling 7 and 8 against DC 6).
Standard Success	Exactly one die in your pool meets or exceeds the Target DC without rolling maximum face value.
Standard Failure	All dice in your pool roll lower than the Target DC, but none roll a 1.
Critical Failure	All dice in your pool roll lower than the Target DC AND your highest rolled die shows a 1 (or multiple dice in the pool roll 1s simultaneously).
6.2 Combat & Narrative Impact of Criticals
Critical Success in Combat: Double weapon damage dice (2d8 
→
→ 4d8), bypass armor/Soak entirely (Direct Strike), or inflict a severe physical condition (Stunned, Bleeding, Prone).
Critical Failure in Combat: The attacker overextends (loses 1 action next turn), drops their weapon, or triggers an immediate free counter-attack reaction (Attack of Opportunity) from the defender.
Open
Mathless Resolution Engine: Comparative Case Studies
MD
Mathless Resolution Engine: Comparative Case Studies

To ensure our resolution mechanics are fast, tactile, mathematically sound, and genuinely mathless (zero arithmetic during play), we analyzed four critical case studies in modern TTRPG design.

Case Study 1: The Bespoke Mathless System Report (bespoke mathless system report.md)
1.1 The Design Journey & Evolution

The uploaded developer report documents a 6-month open playtest of a bespoke system built to eliminate mental math entirely while preserving tactical excitement:

Phase 1: 2d10 Keep Highest. Inspired by D&D 5e Advantage, the designer noted that picking up two dice and keeping the higher result delivers immediate "lizard-brain gut satisfaction." However, static 2d10 without modifiers felt too swingy and lacked character progression.
Phase 2: Cascading Step-Down Dice & Exploding Dice. To allow characters with small dice (d4 or d6) to hit higher Target Numbers (DCs 2-12) or bounce back from failure, the designer experimented with:
Exploding Dice (Savage Worlds style): If you roll maximum (6 on a 
𝑑
6
d6), roll again and add. Result: Introduced heavy math and erratic, lethal swinginess.
Cascading Step-Downs: If a check failed or hit a max face, pick up the next die size down (d8 after d10) and roll/add. Result: Mathematically functional but clunky, slow to explain, and destroyed table momentum.
Phase 3: "Kill Your Darlings" — The 2dX Step Pool with Hyper-Shifting.
The designer cut cascading and exploding mechanics entirely right before open playtesting. Instead, they established:
Base Pool: Every character rolls 2d(Rank) keep highest (2d6, 2d8, 2d10, 2d12).
Glitch / Bane: Remove a die (1d(Rank)).
Advantage / Boon: Add a die (3d(Rank) or 4d(Rank) keep highest).
Hyper-Shifting: To overcome the hard mathematical ceiling of small dice (e.g., 2d4 cannot hit DC 6), players spend an in-world stamina resource (Hyper-Shift) to step their pool up one die size (2d4 
→
→ 2d6) before the roll.
1.2 Key Takeaways for Our System
Immediate Visual Transparency: When a player rolls 3d8 and sees 2, 5, 8, they instantly know their result is 8. There is zero latency between the die landing and the narrative outcome.
Stamina-Driven Hyper-Shifting: Hyper-Shifting replaces the abstract "+2 modifier" with a concrete physical exertion choice: "Do I spend my character's Stamina to step my 2d6 pool up to 2d8 to ensure I can clear DC 7?"
Case Study 2: Daggerheart & The 2d12 Hope/Fear Engine
2.1 Mechanical Summary

Darrington Press’s Daggerheart uses a dual-die system where players roll 1d12 Hope + 1d12 Fear (2d12 total), add an attribute modifier (+1 to +5), and compare to a DC.

If Hope die > Fear die: Roll with Hope (gain Hope token, positive narrative spin).
If Fear die > Hope die: Roll with Fear (GM gains Fear token, complication occurs).
If Hope die == Fear die: Critical Success.
2.2 Why We Diverge from Daggerheart

While Daggerheart's dual-die narrative axis is engaging, it violates two of our core design pillars:

Requires Double-Step Arithmetic: Players must add two $d12$s (8 + 7 = 15), then add a numerical modifier (15 + 3 = 18), and then compare vs DC (18 vs DC 16 = Success).
Relies on Meta-Currencies: "Hope" and "Fear" tokens are abstract out-of-character currencies tracked by players and the GM to trigger powers and twists.
2.3 What We Adopt (In a Mathless Format)

We adopt the concept of Die Face Matching & Color/Designation Checks without addition:

If a player rolls a multi-die pool (3d8), if two dice roll the same high number (8 and 8), it triggers a Mathless Critical Surge or weapon mastery effect without checking numerical thresholds over the DC.
Case Study 3: Shadow of the Demon Lord (SotDL) Boons & Banes
3.1 The SotDL +d6 Engine

In Robert J. Schwalb's system, whenever a character has an advantage or disadvantage, they roll 
𝑁
𝑑
6
Nd6 alongside their 
𝑑
20
d20:

Boon (+1 Boon): Roll 
1
𝑑
6
1d6, add to 
𝑑
20
d20. If +3 Boons, roll 
3
𝑑
6
3d6, keep the single highest 
𝑑
6
d6, and add it to the 
𝑑
20
d20.
Bane (+1 Bane): Same, but subtract the highest 
𝑑
6
d6.
Cancellation: Boons and Banes cancel 1-to-1 before rolling.
3.2 Translating SotDL Boons into Our Mathless Step Engine

Because our baseline resolution uses step dice (2dX keep highest) rather than 
𝑑
20
+
math
d20+math, we adapt SotDL's brilliance directly into pool volume:

1 Boon (+1B): Add 
+
1
 die
+1 die of your current step rank (2d8 
→
→ 3d8).
2 Boons (+2B): Add 
+
2
 dice
+2 dice (4d8 keep highest).
1 Bane (+1X): Remove 
−
1
 die
−1 die from the pool (2d8 
→
→ 1d8).
Severe Bane (+2X or more): If a pool is reduced below 1d, you roll 2d(Rank) and keep the lowest result (Disadvantage).
Case Study 4: Step Dice vs Dice Pools vs Hybrid Engine
4.1 The Dilemma

In designing a mathless game that models both Innate Talent/Power (Strength, Arcana power) and Tactical Training/Reliability (Skill ranks, teamwork, positioning), we must decide how step dice and dice pools interact:

Pure Step Dice (1dX): (e.g., Kids on Bikes, Savage Worlds). Fast, but 1d12 is too swingy (1/12th chance to roll a 1).
Pure Dice Pools (Nd6 count 6s): (e.g., Vampire V5, Shadowrun). Great for reliability, but counting successes slows play down when pools hit 8-12 dice.
Our Hybrid Blueprint (NdX Keep Highest):
Step Die Size (X = d4, d6, d8, d10, d12): Represents Absolute Capability & Peak Mastery. A character with Arcana d10 can hit a DC 10 spell, whereas a d6 apprentice physically cannot without Hyper-Shifting.
Pool Volume (N = 1d to 4d+): Represents Consistency, Training & Tactical Positioning. A master swordsman might roll 3d10 (High rank, high consistency), ensuring they almost never whiff on basic DC 5 strikes while frequently hitting high DC 9-10 targets.
Summary Resolution Matrix
Scenario	Pool Architecture	Target Comparison	Math Required
Standard Check	2d(Attribute/Skill Rank) keep highest	Compare highest face vs DC (2 to 12)	ZERO
With Tactical Advantage (Boon)	3d(Rank) or 4d(Rank) keep highest	Compare highest face vs DC	ZERO
With Severe Penalty (Bane)	1d(Rank) or 2d(Rank) keep lowest	Compare result vs DC	ZERO
Desperate Push against High DC	Spend 1 Stamina 
→
→ Hyper-Shift (2d6 
→
→ 2d8)	Compare new higher faces vs DC	ZERO
Opposed Check (Parry vs Strike)	Attacker rolls NdX vs Defender's MdY	Compare Attacker Highest vs Defender Highest	ZERO (Higher face wins; ties favor active defender or trigger lock)
Open
TTRPG & Tactical Game Architectural Analysis Matrix (v3 Expanded)
MD
TTRPG & Tactical Game Architectural Analysis Matrix (v3 Expanded)

This document serves as an expanded architectural analysis of 22 tabletop roleplaying games and hybrid tactical board games. It builds upon our base 17-system reference matrix by integrating our primary and secondary anchors (D&D 3.5e, Pathfinder 2e, Shadow of the Demon Lord / Weird Wizard) as well as narrative/tactical board game engines (Gloomhaven, Lands of Evershade).

Furthermore, we introduce Four New Vectors of Analysis across all systems: Resolution Engine & Arithmetic Load, Defense & Damage Mitigation Model, Meta-Currency vs In-World Resource Dependency, and Content Extensibility & Conversion Surface.

1. Master Category Mapping across 22 Reference Systems
Category	Contains	Boundary Rule
meta	Sheet/system metadata	Would change if porting to different system/campaign
identity	Biographical, descriptive	Static description with no direct mechanical rating
attributes	Core innate stats	Fundamental ratings, rarely change through play
skills	Learned/developed capabilities	Improve through use/advancement, rolled for actions
resources	Pools, tracks, conditions	Fluctuates during play; spent/recovered
features	Discrete capabilities	You have it or you don't (though may have sub-properties)
inventory	Physical possessions	Tangible things the character owns
connections	Relationships to entities	Links to NPCs, factions, PCs, organizations
narrative	Story with mechanical hooks	Text that gets USED mechanically during play
progression	Advancement state	Tracks growth; actual gains go to their respective categories
NEW: resolution_engine	Dice/Card engine & math load	How actions are randomized and evaluated against targets
NEW: defense_model	Mitigation & armor mechanics	How attacks are avoided, deflected, or absorbed
NEW: meta_currency	Out-of-world vs in-world fuel	Whether player tokens or character stamina power abilities
NEW: extensibility	Modular content architecture	How feats, spells, and items plug into the baseline engine
2. Detailed Data Schema Mappings by Category
Meta
All Games: system_id, system_version, schema_version, created_at, modified_at, player_name, campaign_name.
Ars Magica: saga_name, covenant_name, current_year, current_season.
Scum and Villainy: crew_reference (link to shared crew sheet).
Burning Wheel: campaign_belief_artha_log (optional).
NEW — D&D 3.5e: campaign_setting, edition_3_5, splatbook_sources_allowed[].
NEW — Pathfinder 2e: pfs_number, society_faction, rarity_access_level.
NEW — Shadow of the Demon Lord: chronicle_name, group_patron.
NEW — Gloomhaven: party_name, campaign_sheet_reference, prosperity_level.
NEW — Lands of Evershade: chronicle_book, story_act, lead_character_slot.
Identity
Kids on Bikes: name, age_bracket (kid/teen/adult), trope, physical_description.
Burning Wheel: name, stock (human/elf/dwarf/orc), lifepath_summary, age, appearance.
Ars Magica: name, house, birth_year, apparent_age, gender, nationality, covenant_role.
Ryuutama: name, class, type, hometown, appearance, favorite_thing, personal_item.
Twilight 2000: name, nationality, branch, rank, age, appearance, big_dream.
Call of Cthulhu: name, occupation, age, birthplace, residence, portrait, player.
Sword of Serpentine: name, ancestry, concept, appearance.
Scum and Villainy: name, alias, playbook, heritage, background, look.
Fate Core: name, description, high_concept_label.
Pathfinder 1e: name, race, class_levels[], alignment, deity, age, height, weight, appearance.
Apocalypse World: name, look, playbook.
Vampire V5: name, concept, ambition, desire, clan, generation, sire, predator_type.
Cypher System: name, descriptor, type, focus, portrait, background.
Genesys: name, species, career, portrait, notable_features.
GURPS: name, race/species, tech_level, cultural_background, appearance.
Troika!: name, background_name, appearance.
Castle Falkenstein: name, social_rank, nationality, profession, appearance, diary_title.
NEW — D&D 3.5e: name, race, class_levels_and_prestige[], alignment, deity, size_category, age, appearance.
NEW — Pathfinder 2e: name, ancestry, heritage, background, class, size, alignment/edicts, deity.
NEW — Shadow of the Demon Lord: name, ancestry, age, build, appearance, personality, background_detail.
NEW — Gloomhaven: character_name, class_archetype (e.g., Brute, Spellweaver), personal_quest_summary.
NEW — Lands of Evershade: name, origin_story, character_archetype, personal_destiny_card.
Attributes (Core Innate Stats)
Kids on Bikes: Brains, Brawn, Fight, Flight, Charm, Grit (d4-d20 assigned by trope).
Burning Wheel: Will, Perception, Power, Forte, Agility, Speed (Numeric 1-8 + Shade).
Ars Magica: Int, Per, Pre, Com, Str, Sta, Dex, Qik (Numeric -3 to +5).
Ryuutama: STR, DEX, INT, SPI (d4-d12, paired for rolls).
Twilight 2000: Strength, Agility, Intelligence, Empathy (d6-d12).
Call of Cthulhu: STR, CON, SIZ, DEX, APP, INT, POW, EDU (Numeric 15-90).
Sword of Serpentine: None (uses abilities only).
Scum and Villainy: Insight, Prowess, Resolve (Derived 0-4 based on action dots).
Fate Core: None (Approaches in FAE: Careful, Clever, Flashy, Forceful, Quick, Sneaky).
Pathfinder 1e: Str, Dex, Con, Int, Wis, Cha (Numeric 3-18+, modifier = floor((N-10)/2)).
Apocalypse World: Cool, Hard, Hot, Sharp, Weird (-2 to +3).
Vampire V5: Physical, Social, Mental attributes (Dots 1-5).
Cypher System: Might, Speed, Intellect (Numeric pool max, Edge).
Genesys: Brawn, Agility, Intellect, Cunning, Willpower, Presence (1-5).
GURPS: Strength, Dexterity, Intelligence, Health (Numeric 1-20+).
Troika!: Skill, Stamina, Luck.
Castle Falkenstein: None (Abilities only).
NEW — D&D 3.5e: Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma (Numeric score 3-30+, modifier -5 to +15+).
NEW — Pathfinder 2e: Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma (Attribute Modifiers -1 to +7 directly; raw scores deprecated in Remaster).
NEW — Shadow of the Demon Lord: Strength, Agility, Intellect, Will (Numeric score 8-15+, modifier score - 10).
NEW — Gloomhaven: Hand Size (Card limit), Max Hit Points (scales by class level).
NEW — Lands of Evershade: Might, Agility, Insight, Spirit (d4 to d12 step ratings).
Skills (Learned/Developed Capabilities)
Kids on Bikes: None.
Burning Wheel: Flat list with roots (Exponent 1-10 + Shade, 200+ skills).
Ars Magica: Abilities (0-10+), Techniques + Forms (Arts; 0-40+).
Ryuutama: Fixed list (~12 skills).
Twilight 2000: Grouped under attributes (d6-d12, 12 total).
Call of Cthulhu: Flat list (Percentile 0-99, 60+ skills).
Sword of Serpentine: Investigative + General (Pool points, ~20 skills).
Scum and Villainy: Actions under attributes (Dots 0-4, 12 actions total).
Fate Core: Flat or pyramidal list (Ladder +0 to +4, 18 skills).
Pathfinder 1e: Flat list (Ranks 0 to level, 35 skills).
Apocalypse World: None (uses moves instead).
Vampire V5: Flat list (Dots 0-5, 27 skills).
Cypher System: Flat list (Trained/Specialized binary tiers).
Genesys: Flat list linked to attributes (Ranks 0-5, ~30 skills).
GURPS: Flat list (Numeric, cost based on difficulty and attribute; 100+ skills).
Troika!: Freeform + background-granted (Numeric 1-6+).
Castle Falkenstein: Abilities (Card rank Poor to Extraordinary, 20+ abilities).
NEW — D&D 3.5e: Class & Cross-class skill list (Skill Ranks up to Level + 3, added to Attribute Modifier + Synergy Bonuses + Feats).
NEW — Pathfinder 2e: Core Skill List (Proficiency Tiers: Untrained +0, Trained +2+Lvl, Expert +4+Lvl, Master +6+Lvl, Legendary +8+Lvl).
NEW — Shadow of the Demon Lord: Professions instead of fixed skills (Having a relevant profession grants +Boon on attribute checks).
NEW — Gloomhaven: None (Actions are determined by specific ability cards in hand).
NEW — Lands of Evershade: Action Mastery domains (Combat, Navigation, Social, Crafting step dice pools).
Resources (Depletable Pools, Tracks, & Conditions)
Kids on Bikes: Adversity Tokens.
Burning Wheel: Artha, Tax (magic fatigue), Wounds track.
Ars Magica: Fatigue levels, Wounds track, Confidence pool, Warping total, Vis.
Ryuutama: HP, MP, Conditions, Carrying Capacity slots.
Twilight 2000: Hit Capacity, Stress, Radiation exposure, Critical Injuries, Ammo.
Call of Cthulhu: HP, MP, Sanity, Luck.
Sword of Serpentine: Health, Morale, Sway, Investigative Pools.
Scum and Villainy: Stress (0-9), Trauma boxes, Harm slots, Armor uses.
Fate Core: Physical Stress, Mental Stress, Consequences slots, Fate Points.
Pathfinder 1e: HP, Nonlethal damage, Spell Slots, Class Resources, Conditions flags.
Apocalypse World: Harm clock, Barter units, Hold points.
Vampire V5: Health, Willpower, Hunger (0-5), Humanity, Stains.
Cypher System: Might Pool, Speed Pool, Intellect Pool, Recovery Rolls.
Genesys: Wounds threshold, Strain threshold, Critical Injuries, Story Points.
GURPS: HP, FP (Fatigue), Conditions flags.
Troika!: Stamina, Luck, Provisions.
Castle Falkenstein: Wounds track, Cards in hand.
NEW — D&D 3.5e: Hit Points, Vancian Spell Slots per level, Daily Use class features (Rage, Turn Undead), Temporary HP, Exhaustion/Fatigue flags, Action Points (Unearthed Arcana).
NEW — Pathfinder 2e: Hit Points, Focus Points (Max 3), Spell Slots, Hero Points (0-3), Condition levels (Clumsy 1-3, Enfeebled 1-3, Frightened 1-4, Wounded 1-4).
NEW — Shadow of the Demon Lord: Health, Damage taken, Insanity, Corruption, Fortune token, Daily spell/talent castings.
NEW — Gloomhaven: Current HP, Active Hand Cards, Discarded Cards, Lost/Burned Cards, Active Conditions (Poison, Wound, Stun, Muddle, Strengthen).
NEW — Lands of Evershade: Vitality (HP), Stamina (Effort spend), Fate tokens, Exhaustion counters.
Features (Discrete Binary Capabilities)
Kids on Bikes: Trope abilities, Powered abilities.
Burning Wheel: Character/Call-on/Die Traits.
Ars Magica: Virtues/Flaws, Spells list.
Ryuutama: Class abilities, Type abilities.
Twilight 2000: Specialties, Talents.
Call of Cthulhu: Occupational abilities, Spells list.
Sword of Serpentine: Ability special uses, Spheres, Corruption.
Scum and Villainy: Playbook abilities, Crew abilities.
Fate Core: Stunts, Extras.
Pathfinder 1e: Feats, Class features, Racial traits, Spells known/Spellbook.
Apocalypse World: Playbook moves, Gangs, Holdings.
Vampire V5: Discipline powers, Advantages, Flaws, Clan weaknesses.
Cypher System: Type/Focus/Descriptor abilities by tier.
Genesys: Talents (tree structures), Species abilities.
GURPS: Advantages, Disadvantages, Perks, Quirks, Techniques.
Troika!: Background abilities, Spells list.
Castle Falkenstein: Suit-based abilities, Sorcery/Magick.
NEW — D&D 3.5e: Feats (General, Combat, Metamagic, Item Creation), Class Features (Ex, Su, Sp), Racial Traits, Prestige Class unlocks, Domain powers.
NEW — Pathfinder 2e: Ancestry Feats, Class Feats, General Feats, Skill Feats, Archetype Feats, Spells list, Class features.
NEW — Shadow of the Demon Lord: Novice/Expert/Master Path talents, Ancestry traits, Spell Traditions and learned spells.
NEW — Gloomhaven: Deck of 10-15 unique Class Ability Cards (top/bottom actions), Perks unlocked via checkmarks (Remove two -1 cards, Add one +2 Fire card).
NEW — Lands of Evershade: Action Cards, Narrative Talent unlocks, Equipment mastery traits.
3. The Four New Analytical Vectors Across All Systems
Vector 11: Resolution Engine & Arithmetic Load

How actions are randomized, what math is required at the table, and how targets are evaluated.

System	Primary Resolution Engine	Tabletop Arithmetic Load	Target / Evaluation Method
D&D 3.5e	
1
𝑑
20
+
∑
(
Modifiers
)
1d20+∑(Modifiers)	Very High: Addition of 4-8 distinct modifiers (BAB + Str + Feats + Buffs - Penalties).	Compare total vs static/dynamic Armor Class (AC) or Difficulty Class (DC).
Pathfinder 2e	
1
𝑑
20
+
Mod
+
Proficiency
+
Bonuses/Penalties
1d20+Mod+Proficiency+Bonuses/Penalties	Medium-High: Strict typing (Circumstance, Status, Item) prevents wild stacking, but still adds large linear numbers up to 
+
40
+40.	Compare vs static AC/DC. 4 Degrees of Success: Beats/fails target by 
±
10
±10 is a Crit/Crit Fail.
Shadow of the Demon Lord	
1
𝑑
20
+
Att Mod
±
Highest of 
𝑁
𝑑
6
1d20+Att Mod±Highest of Nd6 (Boons/Banes)	Low-Medium: Add small attribute modifier (
±
0
 to 
+
5
±0 to +5), then roll 
𝑁
N extra $d6$s (Boons or Banes), keep highest 
𝑑
6
d6, add/subtract it.	Compare vs target Defense score or static DC 10 for attribute challenges.
Gloomhaven	Card-Based: Top/Bottom card action value 
±
± Modifier Deck Draw	Low: Card base attack value (e.g., Attack 3) plus drawn modifier card (+1, -1, 2x, Null).	Compare vs enemy Shield value (subtract shield from damage).
Lands of Evershade	Hybrid Step Pool / Card: Step dice check + Action Card	Minimal: Compare rolled dice directly against target thresholds or narrative challenge tracks.	Dice checks evaluated against narrative outcome matrices.
Bespoke Mathless Report	Step Dice Pools (
2
𝑑
𝑋
2dX Base Pool): Keep Highest	Zero Arithmetic: Roll pool of step dice (2d6 to 2d12+), apply Up-Shift or +1d Boon, keep highest face value.	Direct comparison of highest face value vs Fixed DC (2 to 12) or Opposed Die.
Vampire V5	Dice Pool (
𝑁
𝑑
10
Nd10): Count Successes (6-10)	Low (Counting): Assemble pool equal to Attribute + Skill, roll all $d10$s, count dice showing 6+.	Compare number of successes vs Difficulty (1 to 5+) or Opposed successes.
Call of Cthulhu	Percentile Roll-Under (
1
𝑑
100
1d100):	Minimal: Roll 
𝑑
100
d100; compare against target skill number directly.	Regular (<Skill), Hard (<Skill/2), Extreme (<Skill/5), Impale (1/5th Extreme).
Kids on Bikes	Single Step Die (
1
𝑑
𝑋
+
Tokens
1dX+Tokens): Exploding	Low: Roll assigned die (d4 to d20). If max face, roll again and add. Add Adversity Tokens directly.	Compare vs GM-assigned difficulty number (2 to 20+).
Vector 12: Defense & Damage Mitigation Model

How systems handle avoiding attacks, deflecting strikes, and reducing physical/mental injury.

System	Defense Architecture	Armor Interaction	Injury / Wound Representation
D&D 3.5e	Armor Class (AC): Single target number (10 + Armor + Shield + Dex + Size + Deflection + Natural). Also Touch AC & Flat-Footed AC.	Armor increases AC (binary hit/miss). Only rare Damage Reduction (DR 5/magic) reduces incoming damage after hit.	Hit Points (HP): Abstract pool of meat/luck/stamina. Zero HP = bleeding out (-1 to -10).
Pathfinder 2e	Armor Class (AC): 10 + Dex (capped) + Proficiency + Item + Bonuses. Shield requires active Raise a Shield action (+2 AC).	Armor grants item bonus to AC. Shields can Shield Block reaction to absorb damage up to Hardness before breaking.	HP + Wounded/Dying Tracks: At 0 HP, gain Dying 1-4. Recovering leaves Wounded condition.
Shadow of the Demon Lord	Defense Score: Agility-based (if light/unarmored) or fixed Armor score (Heavy Plate = Defense 17).	Heavy armor overrides Agility completely. Certain shields/talents grant +1 Defense or impose Banes on attackers.	Health & Damage Track: Damage accumulates upward (0 to Health). At max, make Fate roll or die/fall unconscious.
Gloomhaven	Active Shield Bonuses & Positioning: Cards grant temporary Shield (Shield 1 this round).	Shields subtract flat value from incoming attack damage (Attack 4 - Shield 1 = 3 damage).	HP Pool + Card Burning: When taking lethal or unwanted damage, players can permanently burn/lose 1 card from hand or 2 from discard to negate 100% of the attack damage.
Lands of Evershade	Narrative / Tactical Mitigation: Action card defense steps and stamina spending.	Armor items provide passive absorption counters or stamina conservation during defense.	Vitality Pool & Wound Tokens: Critical damage inflicts persistent debuff cards or condition tokens.
Our Idealized System (Blueprint)	Multi-Layer Mathless Defense: Evasion Pool (dodge), Parry Pool (intercept), Soak Rank (armor), Resilience Die (fortitude).	Soak Rank is NOT Armor Class. It is a physical step threshold (Soak d8). If hit, compare attack impact die vs Soak die to determine wound severity without math.	Stamina Pool + Physical Wounds: Stamina absorbs effort/minor kinetic shocks. Exceeding Stamina or triggering lethal strikes inflicts concrete Wound Conditions (Severed Tendon, Cracked Rib).
Vector 13: Meta-Currency vs In-World Resource Dependency

How games fuel heroic effort, luck, and emergency survival.

System	Meta-Currencies (Out-of-World Player Tokens)	In-World Character Resources	Impact on Simulationist Immersion
D&D 3.5e	Action Points (Unearthed Arcana option; spent after roll to add 
1
𝑑
6
1d6).	Spell Slots, Turn Undead charges, Barbarian Rage rounds, HP.	High Simulationism: Mostly relies on in-world daily resources; minimal narrative hand-waving.
Pathfinder 2e	Hero Points: Earned per session; spent to reroll a 
𝑑
20
d20 (keep second result) or stabilize from dying.	Focus Points (recovered via 10-min rest/meditation), Spell Slots, Alchemical Infusions.	Tactical Hybrid: Hero points act as a slight player safety valve, but 95% of abilities run on concrete rest-based tracks.
Shadow of the Demon Lord	Fortune Tokens: Awarded for great roleplay/heroics; spend to turn roll into 20, grant 2 Boons, or negate dying.	Daily spell castings, class ability daily charges, Health pool.	Grounded Dark Fantasy: Fortune is rare; most survivability depends on brutal resource conservation and positioning.
Gloomhaven	None.	Card Hand Size & Stamina: Hand cards double as character lifespan and stamina. Every rest burns cards.	Pure Tactical Simulation: Zero external luck tokens; survival is 100% governed by resource management and positioning.
Fate Core	Fate Points: The core economy. Spend to invoke Aspects (+2 or reroll), compel flaws, and declare story details.	Physical & Mental Stress boxes, Consequences slots.	Narrative Priority: High meta-currency dependence; character action is co-authored rather than strictly simulated.
Our Idealized System (Blueprint)	Strictly ZERO Meta-Currencies: No out-of-character tokens, Inspiration chips, or Fate Points.	Stamina Pool, Poise, Focus, & Equipment Sacrifices: Players can Hyper-Shift dice or avert death by burning physical/mental Stamina or splintering physical shields/weapons (Sacrifice Item).	100% Simulationist Immersion: Every mechanical expenditure directly corresponds to physical exertion, adrenaline, concentration, or material degradation in the game world.
Vector 14: Content Extensibility & Conversion Surface

How modular content (Feats, Spells, Monsters) is architected and ported across systems.

System	Core Option Granularity	Extensibility Mechanism	Conversion Surface Difficulty
D&D 3.5e	Hyper-Modular Feats & 10-Level Prestige Classes: Thousands of discrete atomic traits and prerequisite chains.	Feats alter numerical modifiers (+2), grant action options (Cleave), or unlock sub-rules.	High Numerical Burden: Porting 3.5e requires converting mathematical chains into non-numerical dice upgrades or pool boons.
Pathfinder 2e	Trait-Tagged Feat Trees: Ancestry, Skill, General, and Class feats organized by level (1, 2, 4...20).	Keyword tags ([Stance], [Flourish], [Press]) govern action interaction without text ambiguity.	Clean Structural Surface: Trait tags and 3-action costs map cleanly across systems once numerical proficiency bonuses are stripped out.
Shadow of the Demon Lord	3-Tier Path System: Novice (Lvl 1-2), Expert (Lvl 3-6), Master (Lvl 7-10).	Paths grant self-contained talents at exact levels (+1 Boon on attacks with axes, Spell discovery).	Highly Elegant Porting: SotDL boons (+1d6) map 1-to-1 into our mathless Boon Pool (+1d) mechanics.
Gloomhaven	Card Decks by Class Archetype: Every character has ~15 unique top/bottom action cards.	Leveling up allows selecting 1 of 2 advanced cards to permanently add to the available pool.	Unique Card Mechanics: Converts well into discrete Maneuver Cards/Abilities that cost Stamina or action slots.
Our Idealized System (Blueprint)	Mathless Modular Vector Traits: Every feat, path ability, and spell operates across 5 vectors: Up-Shift, +Boon Pool, Face Trigger (Max/Min), Action Cost, or Defense Override.	Because options modify Dice Architecture rather than arithmetic equations, any 3.5e feat or SotDL path talent can be translated cleanly into a 1-sentence mathless rule.	Built for Seamless Conversion: Structured formulas translate numerical prerequisites and bonuses into step ranks (
𝑑
6
→
𝑑
8
d6→d8) and dice volume additions.
4. Key Architectural Takeaways for Our Idealized System
Adopt 
2
𝑑
𝑋
2dX Base Pools with "Keep Highest" (from Bespoke Report & SotDL Boons):
To avoid the arithmetic weight of 3.5e/PF2e while maintaining reliability, baseline skill checks start at two step dice (2d6, 2d8, 2d10, 2d12) where the player rolls and keeps the single highest result. Boons add 
+
1
𝑑
+1d to the pool (3d8 keep highest), zeroing out cognitive math load while delivering immediate physical satisfaction.
Replace AC with 4 Physical Defense Steps (from 3.5e Touch/Flat-Footed & Gloomhaven Shields):
Instead of a single AC number, characters have concrete step ratings for Evasion (d8), Parry (d10), Soak (d6), and Will (d8). Attacks test directly against the relevant defense rank or pool without modifier subtraction.
Internalize Heroics via Stamina & Hyper-Shifting (Replacing Meta-Currencies):
To achieve 3.5e-style heroic resilience without breaking simulationism via Fate points, players spend Stamina to Hyper-Shift (step up 2d6 to 2d8) before a roll, or Sacrifice Armor/Weapons to absorb critical hits that beat their defenses.
Keyword Tagging & Modular Path Architecture (from PF2e & SotDL):
All converted 3.5e feats, spells, and classes will utilize clean PF2e-style keyword tags ([Maneuver], [Stance], [Arcane], [Reaction]) combined with SotDL's 3-Tier progression (Novice -> Expert -> Master) to organize character builds.
Open
System Inspirations & Anchor Analysis
MD
System Inspirations & Anchor Analysis

To build our idealized TTRPG system, we draw upon specific mechanical philosophies and structural lessons from four primary anchors: Dungeons & Dragons 3.5e, the Demon Lord System (Shadow of the Demon Lord / Weird Wizard), Pathfinder 2e, and a Bespoke Mathless System Case Study.

1. Primary Anchor: Dungeons & Dragons 3.5e
1.1 What We Inherit & Celebrate
Unrivaled Build Diversity & Option Wealth: D&D 3.5e remains the gold standard for high-granularity character customization. Feats, skill synergies, prestige classes, and template stacking allow players to realize distinct, hyper-specific character fantasies.
Concrete Simulationist Distinctions: 3.5e introduced nuanced distinctions such as Touch Armor Class (defending against attacks where armor thickness is irrelevant, like magical rays) vs Flat-Footed Armor Class (defending when unable to react or dodge), as well as three distinct Fortitude, Reflex, and Will saving throw categories.
Deep Monster Ecology & Capabilities: Monsters have distinct extraordinary (Ex), supernatural (Su), and spell-like (Sp) abilities that interact with physical and magical realities in detailed ways.
1.2 What We Strip Away & Reform
The 
+
𝑋
/
−
𝑋
+X/−X Modifier Treadmill: In 3.5e, high-level play bogs down under massive arithmetic chains (Base Attack +14 / +9 / +4, +5 strength, +2 enhancement, -4 power attack, +1 haste, +2 flanking, -2 shaken). We strip away the numbers entirely.
Linear Attack / Defense Scaling: Instead of AC scaling from 10 to 45+ while attack bonuses scale from +0 to +35, our system uses bounded Step Dice (d4 to d12) and Pool Volumes (1d to 4d), ensuring every roll remains transparent and immediate.
2. Secondary Anchor: The Demon Lord System (Shadow of the Demon Lord / Weird Wizard)
2.1 What We Inherit & Celebrate
Boons & Banes as Dynamic Dice: Robert J. Schwalb’s brilliant alternative to static modifiers (+2 / -2) was introducing Boons and Banes—rolling extra 
𝑑
6
d6 dice alongside the 
𝑑
20
d20 and adding/subtracting the highest 
𝑑
6
d6 result. While SotDL still uses basic arithmetic (
𝑑
20
±
𝑑
6
d20±d6), the concept of situational dice canceling each other out (
1
 Boon
+
1
 Bane
=
Normal Roll
1 Boon+1 Bane=Normal Roll) is mathematically clean and tactile.
Modular 3-Tier Path Progression: Character growth split into Novice Paths (Level 1-2: Core archetype like Warrior or Rogue), Expert Paths (Level 3-6: Specialized profession like Berserker, Paladin, or Wizard), and Master Paths (Level 7-10+: High-concept mastery like Blade Dancer or Chronomancer). This provides 3.5e-level prestige class customization without dead levels or prerequisite traps.
2.2 Our Mathless Evolution of Boons & Banes

In our system, because we do not add a 
𝑑
6
d6 to a 
𝑑
20
d20, Boons and Banes directly manipulate the Dice Pool:

Boon Dice (+B): Add an extra die of your skill/attribute rank (
+
1
𝑑
+1d) to your pool. When resolving the check, you keep the highest result across the entire pool.
Bane Dice (+X): Add a "Bane Die" or force the drop of your highest die, effectively requiring you to keep the second-highest (or lowest) result, or step down your die rank for that roll.
Mutual Cancellation: As in SotDL, Boons and Banes cancel each other out 1-to-1 before any dice are picked up.
3. Tactical & Architectural Anchor: Pathfinder 2e
3.1 What We Inherit & Celebrate
The 3-Action Economy: PF2e revolutionized turn structure by giving characters exactly 3 Actions per turn to spend flexibly between Moving, Striking, Casting, Defending (Raise Shield), or performing tactical maneuvers (Demoralize, Feint, Shove). We adopt this clean, highly tactical action budget.
Trait & Tag Taxonomy: Every weapon, spell, action, and monster ability in PF2e is governed by explicit keywords ([Agile], [Forceful], [Reach], [Auditory], [Fear]). This modular keyword architecture allows thousands of items and abilities to interact cleanly without ambiguous natural language.
Degrees of Success: Critical Success, Success, Failure, and Critical Failure produce dynamic combat where every check has four potential outcomes rather than a binary hit/miss.
3.2 Our Mathless Implementation of Degrees of Success

Instead of checking if a roll is "+10 over the DC" (which requires subtraction), degrees of success are determined directly by Dice Faces and Pool Overflows:

Critical Success: Rolling your die's Maximum Face Value AND beating the DC, OR having multiple dice in your pool beat the DC simultaneously (e.g., rolling two 8s against DC 6).
Success: At least one die in your pool meets or exceeds the Target Number (DC).
Failure: All dice in your pool roll lower than the Target Number.
Critical Failure: All dice roll lower than the DC AND your highest die rolls a 1 (or multiple 1s are rolled in the pool).
4. Case Study Anchor: Bespoke Mathless System Report
4.1 Key Lessons from the Developer Self-Report

An uploaded developer self-report detailing six months of open playtesting of a custom mathless step-pool system (bespoke mathless system report.md) provides critical real-world validation and design guardrails:

The Power of "Keep Highest":
The developer discovered that players instinctively love picking up multiple dice and keeping the highest (2d10 keep highest or 3d8 keep highest). It triggers an intuitive, "lizard-brain gut satisfaction" inherited from D&D's Advantage mechanic, zeroing out cognitive load.

Why Exploding & Cascading Dice Fail (Kill Your Darlings):
The developer initially implemented Cascading Step-Down Dice (if you roll maximum on a 
𝑑
10
d10, you pick up a 
𝑑
8
d8 and add/roll it, down to 
𝑑
4
d4) and Exploding Dice (Savage Worlds style). In thorough playtesting, this proved:

Too Swingy: Exploding dice created erratic lethal one-shots that broke grounded simulationism.
Too Clunky to Explain & Execute: Cascading step-down checks slowed play down dramatically, destroying the very intuitive speed the mathless engine was built to achieve.
The Elegant Fix: Dropping cascades entirely and setting the base pool to two step dice (2d6, 2d8, etc.) keep highest. Adding boons increases pool volume (3d8, 4d8), while glitches/banes remove a die (1d8) or step it down.

Hyper-Shifting (In-World Effort vs Static Caps):
A major challenge of step dice (d4 to d12) against fixed DCs (2 to 12) is that a character rolling 2d4 literally cannot beat a DC of 6. To prevent frustration while preserving simulationist realism, the developer introduced Hyper-Shifting:

Mechanic: A character can spend an in-world stamina/resource point to Hyper-Shift their dice pool up one die rank for a single crucial action (e.g., boosting 2d6 to 2d8, or 2d8 to 2d10).
Our Adoption: We adopt Hyper-Shifting (Up-Shift) and Downshifting (Down-Shift) as core mechanics driven by physical stamina and tactical positioning, allowing scrappy heroics without altering mathematical DC targets.
Summary of Anchor Integration
Anchor / Inspiration	Core Feature Adopted	Mathless / Simulationist Adaptation
D&D 3.5e	Massive Feat/Class options, Touch/Flat-Footed AC concepts, Monster ecologies	Converted into Step Die modifiers, Pool volume additions, and Multi-Layer Defense checks.
Demon Lord System	Boons & Banes (+B / +X), 3-Tier Paths (Novice/Expert/Master)	Boons add dice to the pool (+1d); Banes force secondary drop/keep lower results; paths grant discrete traits.
Pathfinder 2e	3-Action Economy, Trait/Tag Architecture, 4 Degrees of Success	Actions spent flexibly; tags govern interactions; crits triggered by max faces or multi-die DC beats without math.
Bespoke Mathless Report	Step-Pools (2dX keep highest), Fixed DCs (2-12), Hyper-Shifting via Stamina	Base rolls are 2d(Rank) keep highest; Stamina spend shifts die size up (Up-Shift); zero cascading or math.
Open
Core Design Pillars
MD
Core Design Pillars

This document establishes the foundational design philosophy of our idealized TTRPG system. Every mechanical rule, character feature, and conversion procedure must align with these four pillars.

Pillar 1: The Mathless Resolution Engine
1.1 The Problem with Modifier Arithmetic

In traditional d20-based systems like D&D 3.5e or Pathfinder 2e, action resolution relies on linear equation building at the gaming table:

Total
=
𝑑
20
+
Base Attack Bonus
+
Attribute Modifier
+
Feat Bonus
+
Buffs
−
Penalties
+
Situational Modifiers
Total=d20+Base Attack Bonus+Attribute Modifier+Feat Bonus+Buffs−Penalties+Situational Modifiers

While mathematically expressive, this creates significant friction:

Cognitive Load & Latency: Players and Game Masters (GMs) spend valuable seconds before and after every die roll recalculating dynamic numbers.
Mental Math Fatigue: Over a 4-hour session, tracking temporary +1s, -2s, and conditional modifiers leads to exhaustion and missed bonuses.
Abstract Detachment: Numbers become disconnected from the physical action; a "+2 from flanking" is just an arithmetic adjustment rather than a tactile advantage.
1.2 The Mathless Solution: Tactile Dice Manipulation

Our system eliminates arithmetic entirely during active play. Action checks compare raw die face values directly to a Target Number (DC) or to an Opponent's Defense Die/Roll.

No Addition or Subtraction: A die showing an 8 is simply an 8. You never add your Strength or subtract an enemy's cover bonus.
Step Dice for Capability Ceiling (
𝑑
4
→
𝑑
12
d4→d12): Your die size dictates your absolute potential and mastery. A novice rolls 
𝑑
4
d4 (can never naturally exceed DC 4 without special effort), while a grandmaster rolls 
𝑑
12
d12.
Pool Volume for Reliability (
1
𝑑
→
4
𝑑
+
1d→4d+): Having multiple dice in your pool represents redundancy, training, or superior positioning. You roll the pool and keep the highest result.
Boons & Banes (Dice Swaps & Additions): Instead of adding 
+
2
+2 or 
−
2
−2, situational advantages add Boon Dice (extra dice rolled into the pool where the highest is kept, or step upgrades to existing dice), while penalties introduce Bane Dice (dice that force you to keep lower results or cancel out high dice).
Pillar 2: Grounded Simulationism & Concrete Capabilities
2.1 Multi-Layered Defenses Over Abstract Armor Class

In D&D 3.5e, "Armor Class" (AC) conflates dodging an attack, deflecting it with a shield, absorbing it with heavy steel plate, and magical warding into a single binary pass/fail number.

In our system, combat resolution respects the physical reality of an attack's trajectory:

Evasion (Mobility & Reflexes): Can the target completely dodge out of the path of the attack?
Parry / Deflection (Weapon & Shield Mastery): Can the target actively intercept or redirect the incoming strike?
Soak / Absorption (Armor & Physical Hide): If the strike connects, how much physical kinetic impact or cutting power is negated before tissue damage occurs?
Resilience / Will (Metabolic & Mental Fortitude): How well does the body/mind resist poison, shock, magic, or psychological trauma?
2.2 Skills as Generic & Specific Capabilities

Skills are not merely abstract ratings rolled once per scene. They model concrete proficiencies and specialized capabilities:

Capability Thresholds: Certain complex tasks (e.g., forging a masterwork blade, picking a tumbler lock, performing surgery) cannot be attempted without specific skill ranks (
𝑑
6
+
d6+).
Maneuver Unlocks: Investing in Athletics doesn't just increase your jump roll; it unlocks physical maneuvers like Shove, Grapple, Disarm, and Tackle, each operating seamlessly on the core mathless pool engine.
Pillar 3: Strict Elimination of Meta-Currencies
3.1 Why Meta-Currencies Break Simulation

Many modern RPGs utilize out-of-world meta-currencies (e.g., Fate Points, 5e Inspiration, Savage Worlds Bennies, Burning Wheel Artha) that allow players to reroll dice, edit narrative reality, or negate damage simply by spending an abstract out-of-character token.

While great for narrative control, meta-currencies fracture immersion for simulationist players because the character does not know what a "Fate Point" is. Why did the warrior suddenly survive a lethal axe blow? Because the player spent a red poker chip.

3.2 In-World Resource Replacement

In our system, every spendable resource must exist within the fiction:

Stamina / Poise Pool: Physical stamina, breath, and balance. Characters spend Stamina to execute strenuous combat maneuvers, Hyper-Shift their dice pool for a desperate surge of power, or absorb kinetic shock. When Stamina hits zero, the character is exhausted and vulnerable.
Focus / Concentration: Mental acuity used by scholars, scouts, and spellcasters to maintain spells or precision actions.
Equipment Durability & Wear: Shields can be splintered (Sacrifice Armor) to absorb a blow that would otherwise cause a severe wound. This is an in-world physical tradeoff, not a meta-currency spend.
Pillar 4: Wealth of Content & High Option-Density
4.1 The Option-Density Challenge

D&D 3.5e and Pathfinder 2e are beloved for their massive character customization options: thousands of feats, spells, prestige classes, character ancestries, and equipment builds. However, in those games, 80% of these options boil down to numerical modifiers (+1 to attack with swords, +2 to saves vs fear).

4.2 Mathless Content Architecture

To support an enormous library of character options (Feats, Paths, Spells, Maneuvers) without collapsing into mathematical bloat, every content piece in our system is built from Discrete Mechanical Vectors:

Step Upgrades / Hyper-Shifting: A trait permanently upgrades a specific die step under specific conditions (e.g., Weapon Master (Swords): Roll 
𝑑
8
d8 instead of 
𝑑
6
d6 when attacking with longswords).
Pool Volume Expansion (Advantage / Boons): A feat grants an extra die (+1d) to the pool in defined tactical contexts (e.g., Pack Hunter: Add 
+
1
𝑑
+1d to your melee attack pool when an ally threatens the same target).
Dice Face Manipulation / Rerolls: Traits allow interacting with specific dice results without math (e.g., Cleaving Strike: If your attack die rolls its maximum face value [an 'explode' condition without addition], immediately apply your second-highest die in the pool as a separate hit against an adjacent foe).
Action Economy / Tactical Positioning: Abilities grant unique action types, free steps, or reaction triggers.
Defense Layer Modification: Traits alter how defenses interact (e.g., Shield Wall: You can apply your Parry die to defend an adjacent ally against ranged attacks).
Open
Project Vault: Idealized Mathless Simulationist TTRPG System
MD
Project Vault: Idealized Mathless Simulationist TTRPG System

Welcome to the master brainstorming and architectural workspace for our New Idealized TTRPG System.

This system bridges a unique gap in tabletop roleplaying game design: delivering the vast character build options, tactical depth, and content wealth of D&D 3.5e and Pathfinder 2e while completely eliminating numerical modifier math.

🏛️ Core System Pillars

Mathless Core Resolution Engine

Zero Arithmetic at the Table: No addition, subtraction, or modifier stacking (+2 base attack + 3 strength + 1 flanking - 2 power attack).
Step Dice & Dice Pools: Character attributes and capabilities are represented by dice sizes (
𝑑
4
→
𝑑
12
d4→d12) and pool volumes (
1
𝑑
→
4
𝑑
+
1d→4d+).
Direct DC Comparison: Players roll their pool, apply Boons/Banes (extra dice where high/low results replace or modify the pool), and directly compare the highest result (or specific dice faces) against a fixed/GM-assigned Target Number (DC).
Intuitive Lizard-Brain Feedback: Inspired by the tactile satisfaction of rolling advantage/disadvantage and small pools, ensuring instant clarity the moment dice stop spinning.

Simulationist & Grounded Capabilities

Multi-Layered Defenses: No single abstract "Armor Class" number. Attacks interact with distinct defensive layers: Parry/Deflection (weapon/shield interception), Evasion/Dodge (reflexive mobility), Soak/Absorption (physical armor/hide reducing injury severity), and Resilience/Will (mental/metabolic fortitude).
Generic & Specific Skill Capabilities: Skills are not just abstract checks; they model realistic proficiencies, combat maneuvers, crafting disciplines, and survival techniques.
Strictly No Meta-Currencies: No "Inspiration," "Fate Points," "Bennies," or out-of-world player reroll tokens. All heroic effort, stamina, and magical power flow through concrete, in-world character resources (Stamina, Focus, Mana, Poise, Equipment Wear).

Massive Content Compatibility & Conversion Pipeline

Primary Anchor — D&D 3.5e: A structured mathematical and structural translation pipeline to port over thousands of Feats, Prestige Classes, Spells, and Monsters into mathless dice-pool/step-die mechanics.
Secondary Anchor — Demon Lord System: Direct adaptation of Shadow of the Demon Lord / Weird Wizard boons/banes (d6 modifiers adapted into pool upgrades/replacements) and modular 3-tier path progression (Novice, Expert, Master).
Tactical Richness — Pathfinder 2e: Translation of 3-action tactical flexibility, trait tags, and deep character customization without the 
+
1
/
+
2
/
−
2
+1/+2/−2 status/circumstance modifier tracking.
📁 Workspace & Directory Structure
text
/home/user/ttrpg_idealization/
├── README.md                                         # [This File] Master overview, architecture, and roadmap
├── 01_design_philosophy_and_pillars/
│   ├── 01_core_design_pillars.md                     # Deep-dive into mathless resolution, simulationism, and no-meta-currency design
│   └── 02_inspirations_and_anchors.md                # Analysis of D&D 3.5e, SotDL, PF2e, and the Bespoke Mathless Report
├── 02_comparative_system_analysis/
│   ├── 01_architecture_matrix_v3_expanded.md         # Expanded 22+ system matrix (incorporating 3.5e, PF2e, SotDL, Gloomhaven, Lands of Evershade + 4 new analysis vectors)
│   └── 02_mathless_resolution_case_studies.md        # Case studies: Daggerheart, 2d10, Cascading vs Hyper-Shifting, Boons/Banes
├── 03_core_baseline_system/
│   ├── 01_resolution_engine.md                       # The baseline mathless engine: Step pools, DCs, Boons/Banes, and Opposed rolls
│   ├── 02_character_schema_and_stats.md              # Master data schema for attributes, skills, defenses, and features
│   └── 03_action_economy_and_turn_structure.md       # Action economy, tactical positioning, and initiative resolution
├── 04_simulationist_subsystems/
│   ├── 01_defenses_and_damage_modeling.md            # Multi-layered defense rules (Parry, Evasion, Soak, Resilience) & wound states
│   ├── 02_skills_and_generic_capabilities.md         # Skill taxonomy, complex maneuvers, lore, and crafting without arithmetic
│   └── 03_resources_conditions_and_wounds.md         # In-world resource tracks (Stamina/Poise), fatigue, and injury mechanics
├── 05_conversion_and_content_engine/
│   ├── 01_dnd_3_5e_conversion_procedure.md           # Step-by-step conversion manual for 3.5e Feats, Classes, Spells, and Bestiary
│   ├── 02_demon_lord_conversion_procedure.md         # Conversion manual for SotDL/Weird Wizard Paths, Boons/Banes, and Spells
│   └── 03_pf2e_and_general_content_guidelines.md     # Translating PF2e tactical actions, traits, and general OSR/d20 content
└── 06_brainstorming_logs_and_roadmap/
    ├── 01_master_brainstorm_log.md                   # Running development log, design dilemmas, and open questions
    └── 02_probability_and_dice_simulations.md        # Probability models and test cases for pool sizes, step caps, and DCs
🚀 Recommended Next Steps & Roadmap
Review & Validate the Expanded Matrix (02_comparative_system_analysis/01_architecture_matrix_v3_expanded.md):
We have expanded the initial 17-game matrix to include D&D 3.5e, Pathfinder 2e, Shadow of the Demon Lord, Gloomhaven, and Lands of Evershade, adding 4 crucial new analytical vectors: Math Load & Resolution Engine, Defense & Mitigation Granularity, Meta-Currency Dependency, and Content Extensibility.
Refine the Core Resolution Engine (03_core_baseline_system/01_resolution_engine.md):
Establish the precise interaction between Step Dice (die size representing capability rank) and Dice Pool Volume (number of dice representing training/effort), alongside how Boons/Banes function without numerical additions.
Draft the Simulationist Defense Architecture (04_simulationist_subsystems/01_defenses_and_damage_modeling.md):
Formalize how attacks test against Evasion vs Parry vs Soak mathlessly (e.g., matching or exceeding defense dice ranks or thresholds).
Iterate on the 3.5e & SotDL Conversion Pipelines (05_conversion_and_content_engine/):
Take classic 3.5e feats (e.g., Power Attack, Combat Expertise, Cleave) and SotDL boons to demonstrate exact before/after mathless conversions.
Open
Ran commands
2
Write
ttrpg_idealization/06_brainstorming_logs_and_roadmap/02_probability_and_dice_simulations.md
133 lines
open
Probability & Mathematical Simulations of the Mathless Engine
MD
Probability & Mathematical Simulations of the Mathless Engine

To ensure our mathless 2dX keep highest engine is mathematically balanced across all character tiers (
𝑑
4
→
𝑑
12
d4→d12) against Target Numbers (DCs 
2
→
12
2→12), we conducted precise combinatorial probability simulations.

This document archives our exact mathematical probability tables, explains the statistical behavior of Boons, Banes, and Hyper-Shifting, and provides an executable Python verification script.

1. Master Probability Tables (Success Rate %)
1.1 Base Pool: 2dX Keep Highest (Standard Check)

This table shows the exact probability of achieving or exceeding the Target Number (DC) when rolling two step dice and keeping the single highest face shown.

Target Number (DC)	2d4	2d6	2d8	2d10	2d12	Tactical Interpretation
DC 3 (Routine)	75.0%	88.9%	93.8%	96.0%	97.2%	Even novices (d4) usually succeed; professionals almost never whiff.
DC 5 (Challenging)	0.0%	55.6%	75.0%	84.0%	88.9%	The standard adventure baseline. d6 is a coin flip; d8+ is reliable.
DC 7 (Formidable)	0.0%	0.0%	43.8%	64.0%	75.0%	Requires professional training (d8+) or Hyper-Shifting.
DC 9 (Heroic)	0.0%	0.0%	0.0%	36.0%	55.6%	Elite capabilities only (d10+).
DC 11 (Legendary)	0.0%	0.0%	0.0%	0.0%	30.6%	Paragon mastery required (d12).
1.2 Boon Pool: +1 Boon (+1B->3dX Keep Highest)

Adding 
+
1
 Boon Die
+1 Boon Die (
+
1
𝑑
+1d) increases pool volume from 2 to 3 dice. Note how this dramatically boosts consistency across challenging DCs without changing the hard mathematical ceiling.

Target Number (DC)	3d4	3d6	3d8	3d10	3d12	Boon Impact Analysis
DC 3 (Routine)	87.5%	96.3%	98.4%	99.2%	99.5%	Near-guaranteed success across all ranks.
DC 5 (Challenging)	0.0%	70.4%	87.5%	93.6%	96.3%	+1 Boon jumps 3d6 from 55.6% to 70.4%, making training tangible.
DC 7 (Formidable)	0.0%	0.0%	57.8%	78.4%	87.5%	3d8 jumps from 43.8% to 57.8%; 3d10 reaches near 80%.
DC 9 (Heroic)	0.0%	0.0%	0.0%	48.8%	70.4%	3d10 jumps from 36.0% to 48.8% (+12.8% boost).
DC 11 (Legendary)	0.0%	0.0%	0.0%	0.0%	42.1%	3d12 jumps from 30.6% to 42.1%.
1.3 Major Boon Pool: +2 Boons (+2B->4dX Keep Highest)

Rolling 4 dice (e.g., Flanking + Master Proficiency) represents overwhelming tactical dominance.

Target Number (DC)	4d4	4d6	4d8	4d10	4d12
DC 3 (Routine)	93.8%	98.8%	99.6%	99.8%	99.9%
DC 5 (Challenging)	0.0%	80.2%	93.8%	97.4%	98.8%
DC 7 (Formidable)	0.0%	0.0%	68.4%	87.0%	93.8%
DC 9 (Heroic)	0.0%	0.0%	0.0%	59.0%	80.2%
DC 11 (Legendary)	0.0%	0.0%	0.0%	0.0%	51.8%
1.4 Bane Pool: -1 Bane (+1X->1dX Single Roll)

Removing 
−
1
 die
−1 die strips away the "keep highest" safety net, reducing the check to a single die roll (1dX).

Target Number (DC)	1d4	1d6	1d8	1d10	1d12
DC 3 (Routine)	50.0%	66.7%	75.0%	80.0%	83.3%
DC 5 (Challenging)	0.0%	33.3%	50.0%	60.0%	66.7%
DC 7 (Formidable)	0.0%	0.0%	25.0%	40.0%	50.0%
DC 9 (Heroic)	0.0%	0.0%	0.0%	20.0%	33.3%
DC 11 (Legendary)	0.0%	0.0%	0.0%	0.0%	16.7%
1.5 Severe Bane Pool: -2 Banes (+2X->2dX Keep LOWEST)

Forcing the player to roll two dice and keep the lowest face (Disadvantage) represents extreme tactical jeopardy (e.g., Blinded or attacking through arrow slits).

Target Number (DC)	2d4 (Low)	2d6 (Low)	2d8 (Low)	2d10 (Low)	2d12 (Low)
DC 3 (Routine)	25.0%	44.4%	56.2%	64.0%	69.4%
DC 5 (Challenging)	0.0%	11.1%	25.0%	36.0%	44.4%
DC 7 (Formidable)	0.0%	0.0%	6.2%	16.0%	25.0%
DC 9 (Heroic)	0.0%	0.0%	0.0%	4.0%	11.1%
DC 11 (Legendary)	0.0%	0.0%	0.0%	0.0%	2.8%
2. Mathematical Impact of Hyper-Shifting (Stamina Spend)

Because a character with 2d6 literally cannot beat DC 7 (0.0% chance), Hyper-Shifting (spending 1 Stamina to step up die size: 2d6 
→
→ 2d8) is our system's mathematical bridge:

Initial Check Scenario	Initial Probability	After Hyper-Shift (1 Stamina Spend)	New Probability	Net Probability Gain
2d4 vs DC 5 (Challenging)	0.0%	Shift to 2d6	55.6%	+55.6% (Impossible -> Competent)
2d6 vs DC 7 (Formidable)	0.0%	Shift to 2d8	43.8%	+43.8% (Impossible -> Viable)
2d8 vs DC 9 (Heroic)	0.0%	Shift to 2d10	36.0%	+36.0% (Impossible -> Possible)
2d10 vs DC 11 (Legendary)	0.0%	Shift to 2d12	30.6%	+30.6% (Impossible -> Heroic)
2d6 vs DC 5 (Standard Boost)	55.6%	Shift to 2d8	75.0%	+19.4% (Reliability Surge)
3. Embedded Python Verification Script

To independently verify or extend these combinatorial simulations right from the terminal, save and run the script below:

Python
#!/usr/bin/env python3
"""
Mathless Step-Pool Probability Verification Script
Run directly via bash: python3 simulation_verify.py
"""
import itertools

def calculate_probabilities():
    dice_sizes = [4, 6, 8, 10, 12]
    target_dcs = [3, 5, 7, 9, 11]
    pool_configs = [
        ("Base Pool (2dX Keep Highest)", 2, max),
        ("+1 Boon (3dX Keep Highest)", 3, max),
        ("+2 Boons (4dX Keep Highest)", 4, max),
        ("-1 Bane (1dX Single Die)", 1, max),
        ("-2 Banes (2dX Keep Lowest)", 2, min)
    ]

    for label, num_dice, eval_func in pool_configs:
        print(f"\n--- {label} ---")
        header = f"{'DC':<6}" + "".join([f"d{d}:<8" for d in dice_sizes])
        print(header)
        print("-" * len(header))
        for dc in target_dcs:
            row_str = f"DC {dc:<3}"
            for die in dice_sizes:
                total_outcomes = die ** num_dice
                successes = sum(
                    1 for roll in itertools.product(range(1, die + 1), repeat=num_dice)
                    if eval_func(roll) >= dc
                )
                prob = (successes / total_outcomes) * 100
                row_str += f"{prob:>6.1f}%  "
            print(row_str)

if __name__ == "__main__":
    calculate_probabilities()
Open
used
Bash
90ms

I have organized and structured our entire brainstorm into a comprehensive, modular project workspace under /home/user/ttrpg_idealization/.

Every directory and markdown file has been built with exact mechanical specifications, translation tables, probability simulations, and analytical depth. We incorporated all insights from your uploaded reference documents (ttrpg_architecture_matrix.md and bespoke mathless system report.md) and expanded upon them by adding D&D 3.5e, Pathfinder 2e, Shadow of the Demon Lord / Weird Wizard, Gloomhaven, and Lands of Evershade alongside four new analytical vectors.

🏛️ Master Workspace Architecture & File Index
text
/home/user/ttrpg_idealization/
├── README.md                                         # [Presented] Project overview, core pillars & navigation index
├── 01_design_philosophy_and_pillars/
│   ├── 01_core_design_pillars.md                     # The 4 pillars: Mathless Engine, Simulationism, Zero Meta-Currencies, High Option-Density
│   └── 02_inspirations_and_anchors.md                # Deep analysis of D&D 3.5e, SotDL, PF2e, and the Bespoke Mathless Report
├── 02_comparative_system_analysis/
│   ├── 01_architecture_matrix_v3_expanded.md         # Expanded 22+ system schema matrix with 4 new analytical vectors across all games
│   └── 02_mathless_resolution_case_studies.md        # Case studies: Daggerheart vs SotDL Boons vs 2d10 vs Step Pools (`2dX keep highest`)
├── 03_core_baseline_system/
│   ├── 01_resolution_engine.md                       # The baseline engine: `2dX keep highest`, DCs 2-12, Boons/Banes (`+1d / -1d`), Opposed checks
│   ├── 02_character_schema_and_stats.md              # Master data schema: MIG/AGI/INT/WIL, Mastery Domains, 4 Defenses, Resource tracks
│   └── 03_action_economy_and_turn_structure.md       # Turn phases, 3-action budget (`[A][A][A]`), tactical positioning (`Flanking = +1B`), Reactions
├── 04_simulationist_subsystems/
│   ├── 01_defenses_and_damage_modeling.md            # Multi-layer defense rules (Evasion vs Parry vs Soak vs Resilience) & mathless wound matrix
│   ├── 02_skills_and_generic_capabilities.md         # Skill taxonomy, capability gating (`d8+ required`), 6-step crafting clocks & combat maneuvers
│   └── 03_resources_conditions_and_wounds.md         # In-world tracks (`Vitality`, `Stamina`, `Focus`), concrete injuries (`Severed Tendon`), and recovery
├── 05_conversion_and_content_engine/
│   ├── 01_dnd_3_5e_conversion_procedure.md           # Exact conversion manual for 3.5e Feats (`Power Attack`, `Cleave`), Spells (`Fireball`), Bestiary (`Ogre`)
│   ├── 02_demon_lord_conversion_procedure.md         # Converting SotDL/Weird Wizard Boons/Banes, 3-Tier Paths (`Berserker`), Insanity/Corruption clocks
│   └── 03_pf2e_and_general_content_guidelines.md     # Translating PF2e weapon traits (`[Agile]`, `[Reach]`, `[Fatal]`), 3-action feats, OSR/board game porting
└── 06_brainstorming_logs_and_roadmap/
    ├── 01_master_brainstorm_log.md                   # Running decision log (`DEC-001 to 006`), architectural dilemmas, and step-by-step roadmap
    └── 02_probability_and_dice_simulations.md        # Exact combinatorial success rates (% tables), Hyper-Shift gain analysis, and executable Python script
🔥 Key Architectural Highlights & Breakthroughs

The Core Resolution Engine (2dX Keep Highest)

Why it works: Directly addressing the insights from bespoke mathless system report.md, rolling two step dice (
2
𝑑
6
→
2
𝑑
12
2d6→2d12) and keeping the single highest face eliminates mental addition completely while delivering the tactile satisfaction of Advantage.
Boons & Banes without Math: Instead of adding 
𝑑
6
d6 modifiers (SotDL style), Boons add dice to the pool (+1B 
→
→ 3dX keep highest, +2B 
→
→ 4dX). Banes remove dice (+1X 
→
→ 1dX single die, +2X 
→
→ 2dX keep lowest). They cancel out 1-to-1 before rolling.
Hyper-Shifting (Stamina Spend): A character with 2d6 literally cannot roll above a 6. To overcome high Target Numbers (DC 7 to 12) without linear modifiers, players spend 1 Stamina to Hyper-Shift their check pool up one die step (2d6 
→
→ 2d8) before rolling.

Simulationist Multi-Layer Defenses (Replacing Single Armor Class)

Instead of abstract AC (10 + Dex + Armor + Shield), incoming attacks interact with realistic physical layers:
Evasion (AGI Pool vs Attack): Dodging projectiles, explosions, or area sweeps.
Parry (Combat Pool vs Attack): Active opposed weapon/shield interception.
Soak Rank (Armor Step Die: d4 Cloth -> d12 Plate): Checked after a hit connects. Compare the attacker's Weapon Damage Die Face directly against the defender's Soak Die Face (Damage Die vs Soak Die). If Damage <= Soak, kinetic force is absorbed cleanly (0 Wounds). If Damage > Soak, the target loses Vitality and takes a concrete Wound Condition (Bleeding Cut, Fractured Rib).

Expanded Architectural Matrix (v3 Expanded)

In 02_comparative_system_analysis/01_architecture_matrix_v3_expanded.md, we mapped all 17 original reference systems along with D&D 3.5e, Pathfinder 2e, Shadow of the Demon Lord / Weird Wizard, Gloomhaven, and Lands of Evershade across 14 comprehensive categories, introducing:
Vector 11: Resolution Engine & Arithmetic Load
Vector 12: Defense & Damage Mitigation Model
Vector 13: Meta-Currency vs In-World Resource Dependency
Vector 14: Content Extensibility & Conversion Surface

Ready-to-Use 3.5e & SotDL Conversion Pipelines

In 05_conversion_and_content_engine/01_dnd_3_5e_conversion_procedure.md, we built complete before/after conversions for classic 3.5e elements:
Power Attack: Take 
+
1
 Bane Die (‘1dX‘)
+1 Bane Die (‘1dX‘) on attack to step up weapon Damage Die two ranks (d8 
→
→ d12) and guarantee 
≥
1
≥1 step Soak penetration.
Cleave: On inflicting a lethal wound or dropping an enemy, immediately gain a free melee Strike against an adjacent target (Great Cleave chains indefinitely).
Combat Expertise: Take 
+
1
 Bane Die
+1 Bane Die on melee attacks to gain 
+
2
 Boon Dice (‘4dParry keep highest‘)
+2 Boon Dice (‘4dParry keep highest‘) on active Parry checks.
Fireball: [2A] Arcane check vs all targets' 2dAGI Evasion pools. Failed evasion inflicts d10 Fire vs Soak + heat shock (-2 Stamina).
Ogre Profile: Converted into a complete mathless block (MIG d10, Soak d10 apron, 2d10 Greatclub pool).
🎲 Exact Probability Verification (From our Python Combinatorial Engine)

Here is a preview of the exact mathless success rates (% to meet/exceed DC) documented in 06_brainstorming_logs_and_roadmap/02_probability_and_dice_simulations.md:

Check Scenario	2d4	2d6	2d8	2d10	2d12
Base Pool (2dX keep highest) vs DC 5	0.0%	55.6%	75.0%	84.0%	88.9%
With +1 Boon (3dX keep highest) vs DC 5	0.0%	70.4%	87.5%	93.6%	96.3%
Base Pool (2dX keep highest) vs DC 7	0.0%	0.0%	43.8%	64.0%	75.0%
After Hyper-Shift (+1 Stamina) vs DC 7	0.0%	43.8% (Shift to 2d8)	64.0% (Shift to 2d10)	75.0% (Shift to 2d12)	80.0%+ (Mythic)
🚀 Where Should We Focus Our Brainstorm Next?

Now that the baseline architecture, philosophy, and comparative matrices are completely established and verified in our vault, how would you like to proceed? We can:

Deep-Dive into Class & Path Conversions: Take 3-5 iconic D&D 3.5e classes (e.g., Fighter, Wizard, Rogue, Barbarian, Cleric) and convert them into our modular 3-Tier Path structure (Novice -> Expert -> Master).
Expand the Bestiary & Combat Encounters: Convert a full roster of iconic 3.5e / SotDL monsters (Red Dragon, Mind Flayer, Troll, Demon Lord) and walk through a round-by-round mathless combat simulation.
Refine Magic & Spellcasting Traditions: Build out the exact rules for Focus channeling, spell interruption, and translate 20 core spells into mathless domain checks.
Iterate on Specific Subsystems: Focus on the detailed mechanics of crafting, stealth/subterfuge, or social intrigue without numbers.

Let me know which direction or files you'd like to explore next!
