---
turn: 4
role: "AI-Designer"
source: chat_history.json
---

# Turn 4 — AI-Designer

Edited files
9
01_master_brainstorm_log.md
MD
03_resources_conditions_and_wounds.md
MD
01_defenses_and_damage_modeling.md
MD
01_resolution_engine.md
MD
TTRPG & Tactical Game Architectural Analysis Matrix (v4 Master Expanded)
MD
TTRPG & Tactical Game Architectural Analysis Matrix (v4 Master Expanded)

This document serves as our definitive architectural analysis of 23 tabletop roleplaying games and hybrid tactical board games. It expands upon our previous reference matrices by integrating our primary and secondary anchors (D&D 3.5e, Pathfinder 2e, Shadow of the Demon Lord / Weird Wizard), board game engines (Gloomhaven, Lands of Evershade), and our newest simulationist cornerstone: Mythras (BRP / 
𝑑
100
d100 System).

Furthermore, we expand our analysis template from 14 to Eighteen Vectors of Analysis across all systems, introducing: Vector 15 (Opposed Differential & Maneuver Triggers), Vector 16 (Active Defense Action Economy), Vector 17 (Hit Location Granularity & Wound Severance), and Vector 18 (GM Cognitive Load & Mob Scaling).

1. Master Category Mapping across 23 Reference Systems
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
resolution_engine	Dice/Card engine & math load	How actions are randomized and evaluated against targets
defense_model	Mitigation & armor mechanics	How attacks are avoided, deflected, or absorbed
meta_currency	Out-of-world vs in-world fuel	Whether player tokens or character stamina power abilities
extensibility	Modular content architecture	How feats, spells, and items plug into the baseline engine
NEW: differential_maneuvers	Opposed success level outcomes	How differential roll results trigger tactical maneuvers
NEW: defense_economy	Action cost of defending	Whether defense is passive or consumes active turn economy
NEW: hit_locations	Anatomical vs global damage	Whether damage targets localized limbs or a global HP pool
NEW: mob_scaling	Minion / Rabble architecture	How the engine reduces GM tracking for large enemy groups
2. Detailed Data Schema Mappings by Category (Including Mythras)
Meta
All Games: system_id, system_version, schema_version, created_at, modified_at, player_name, campaign_name.
Ars Magica: saga_name, covenant_name, current_year, current_season.
Scum and Villainy: crew_reference (link to shared crew sheet).
Burning Wheel: campaign_belief_artha_log (optional).
D&D 3.5e: campaign_setting, edition_3_5, splatbook_sources_allowed[].
Pathfinder 2e: pfs_number, society_faction, rarity_access_level.
Shadow of the Demon Lord: chronicle_name, group_patron.
Gloomhaven: party_name, campaign_sheet_reference, prosperity_level.
Lands of Evershade: chronicle_book, story_act, lead_character_slot.
NEW — Mythras: culture_origin, career_path, cult_brotherhood_membership, magic_tradition.
Identity
Kids on Bikes: name, age_bracket, trope, physical_description.
Burning Wheel: name, stock, lifepath_summary, age, appearance.
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
D&D 3.5e: name, race, class_levels_and_prestige[], alignment, deity, size_category, age, appearance.
Pathfinder 2e: name, ancestry, heritage, background, class, size, alignment/edicts, deity.
Shadow of the Demon Lord: name, ancestry, age, build, appearance, personality, background_detail.
Gloomhaven: character_name, class_archetype, personal_quest_summary.
Lands of Evershade: name, origin_story, character_archetype, personal_destiny_card.
NEW — Mythras: name, gender, age, culture (Barbarian, Civilized, Nomadic, Primitive), social_class, family_background.
Attributes (Core Innate Stats)
Kids on Bikes: Brains, Brawn, Fight, Flight, Charm, Grit (d4-d20).
Burning Wheel: Will, Perception, Power, Forte, Agility, Speed (Numeric 1-8 + Shade).
Ars Magica: Int, Per, Pre, Com, Str, Sta, Dex, Qik (Numeric -3 to +5).
Ryuutama: STR, DEX, INT, SPI (d4-d12, paired for rolls).
Twilight 2000: Strength, Agility, Intelligence, Empathy (d6-d12).
Call of Cthulhu: STR, CON, SIZ, DEX, APP, INT, POW, EDU (Numeric 15-90).
Sword of Serpentine: None (uses abilities only).
Scum and Villainy: Insight, Prowess, Resolve (Derived 0-4).
Fate Core: None (Approaches in FAE: Careful, Clever, Flashy, Forceful, Quick, Sneaky).
Pathfinder 1e: Str, Dex, Con, Int, Wis, Cha (Numeric 3-18+, modifier = floor((N-10)/2)).
Apocalypse World: Cool, Hard, Hot, Sharp, Weird (-2 to +3).
Vampire V5: Physical, Social, Mental attributes (Dots 1-5).
Cypher System: Might, Speed, Intellect (Numeric pool max, Edge).
Genesys: Brawn, Agility, Intellect, Cunning, Willpower, Presence (1-5).
GURPS: Strength, Dexterity, Intelligence, Health (Numeric 1-20+).
Troika!: Skill, Stamina, Luck.
Castle Falkenstein: None (Abilities only).
D&D 3.5e: Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma (Numeric score 3-30+).
Pathfinder 2e: Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma (Attribute Modifiers -1 to +7).
Shadow of the Demon Lord: Strength, Agility, Intellect, Will (Numeric score 8-15+).
Gloomhaven: Hand Size (Card limit), Max Hit Points (scales by class level).
Lands of Evershade: Might, Agility, Insight, Spirit (d4 to d12 step ratings).
NEW — Mythras: Strength (STR), Constitution (CON), Size (SIZ), Dexterity (DEX), Intelligence (INT), Power (POW), Charisma (CHA) (3d6 / 2d6+6 scale 3-18+; derives Action Points, Damage Modifier, Initiative, and localized HP).
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
D&D 3.5e: Class & Cross-class skill list (Skill Ranks up to Level + 3).
Pathfinder 2e: Core Skill List (Proficiency Tiers: Untrained +0, Trained +2+Lvl, Expert +4+Lvl, Master +6+Lvl, Legendary +8+Lvl).
Shadow of the Demon Lord: Professions instead of fixed skills (+Boon on attribute checks).
Gloomhaven: None (Actions are determined by specific ability cards in hand).
Lands of Evershade: Action Mastery domains (Combat, Navigation, Social, Crafting).
NEW — Mythras: Standard Skills (Athletics, Evade, Perception, Stealth, Brawn) + Professional Skills (Lore, Commerce, Mechanisms, Crafting) + Combat Styles (Sword & Shield 65%, Spearmanship 70%). All rated as percentile numbers (0% to 100%+).
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
D&D 3.5e: Hit Points, Vancian Spell Slots, Daily Use class features, Temporary HP, Exhaustion/Fatigue flags.
Pathfinder 2e: Hit Points, Focus Points (Max 3), Spell Slots, Hero Points (0-3), Condition levels (Clumsy 1-3, Frightened 1-4).
Shadow of the Demon Lord: Health, Damage taken, Insanity, Corruption, Fortune token, Daily spell/talent castings.
Gloomhaven: Current HP, Active Hand Cards, Discarded Cards, Lost/Burned Cards, Active Conditions (Poison, Stun, Muddle).
Lands of Evershade: Vitality (HP), Stamina (Effort spend), Fate tokens, Exhaustion counters.
NEW — Mythras: Action Points (AP: 2 to 3), Magic Points (MP), Fatigue levels (Fresh to Exhausted/Debilitated), Luck Points (2 to 3), 7 Localized Hit Location Tracks (Head, Chest, Abdomen, Left/Right Arm, Left/Right Leg) each with Minor, Serious, Major thresholds.
Features (Discrete Binary Capabilities)
(Same 17 base reference systems + 3.5e Feats, PF2e Feats, SotDL Paths, Gloomhaven Ability Cards, Lands of Evershade Talents).
NEW — Mythras: Cult / Brotherhood Gifts, Magic Traditions (Folk Magic, Animism, Mysticism, Sorcery, Theism spells/miracles), Combat Style Traits (Shield Wall, Skirmisher, Mounted Combat). Crucially: Combat Maneuvers (Special Effects) are NOT listed under Features because every character possesses full universal access to them by default!
3. The Four Core Analytical Vectors (Vectors 11 to 14)

(Summary comparison across key systems including Mythras)

System	Vector 11: Resolution Engine & Arithmetic Load	Vector 12: Defense & Mitigation Model	Vector 13: Meta-Currency Dependency	Vector 14: Content Extensibility
D&D 3.5e	
1
𝑑
20
+
∑
(
Modifiers
)
1d20+∑(Modifiers) (High Math)	Single Armor Class (
𝐴
𝐶
AC). DR is rare post-hit reduction.	Low (Action Points optional).	Hyper-Modular Feats & 10-level Prestige Classes (Numerical bloat).
Pathfinder 2e	
1
𝑑
20
+
Prof
+
Mods
1d20+Prof+Mods (Medium-High Math)	Single 
𝐴
𝐶
AC. Active Shield Block absorbs damage (Hardness).	Medium (Hero Points 0-3 for rerolls/stabilize).	Keyword-tagged Feats by level (Clean modular traits).
Shadow of the Demon Lord	
1
𝑑
20
+
Mod
±
𝑁
𝑑
6
 Boons/Banes
1d20+Mod±Nd6 Boons/Banes (Low-Medium Math)	Agility-based or fixed heavy armor Defense score.	Low (Fortune Tokens rare).	3-Tier Paths (Novice/Expert/Master with clean talents).
Gloomhaven	Card base attack 
±
± Modifier draw (+1, -1, 2x) (Low Math)	Active card Shields reduce flat damage; card burning prevents death.	Zero (Card management is lifespan).	10-15 Action Cards per class; checkmark perks.
Mythras	Percentile Roll-Under (
𝑑
100
≤
Skill
%
d100≤Skill%) (Minimal Math)	Active Opposed Roll (Parry/Evade vs Attack) + Localized Armor DR.	Low (Luck Points to reroll or downgrade wound).	Combat Styles, Cults, and 5 distinct Magic traditions (Modular skill groupings).
Our Mathless Engine	Step Pools (2dX keep highest) (ZERO Table Math)	4-Layer Defense Steps (Evasion, Parry, Soak, Resilience). Soak is post-hit reduction.	Strictly ZERO. All heroics powered by in-world Stamina, Focus, & Item Sacrifice.	Mathless Vector Traits (+1Boon pool, Up-Shift die, Action cost, Keyword tag).
4. The Four New Simulationist & Tactical Vectors (Vectors 15 to 18)
Vector 15: Opposed Resolution & Differential Maneuver Triggers

How systems handle contested rolls and how differential outcomes generate tactical maneuvers.

System	Contested Roll Mechanic	Maneuver / Special Effect Access	How Outcomes Are Evaluated
D&D 3.5e	Rare opposed rolls (Grapple = d20 + BAB + Str vs d20 + BAB + Str). Attacks target static 
𝐴
𝐶
AC.	Strictly Class/Feat Gated: You cannot attempt complex maneuvers (Disarm, Trip, Cleave) effectively without specific feats (Improved Disarm) to avoid Attacks of Opportunity.	Binary Hit/Miss against 
𝐴
𝐶
AC. No differential effect beyond rolling a Natural 20 (x2 or x3 critical multiplier).
Pathfinder 2e	Attacks vs static 
𝐴
𝐶
AC. Maneuvers (Shove, Trip) are Athletics vs static Fortitude/Reflex DC.	Universal Basic Maneuvers: Anyone can attempt Shove, Trip, Grapple ([1A]), but advanced maneuvers (Knockdown, Whirlwind Strike) are gated behind Class Feats.	4 Degrees of Success: Beating or failing DC by 
±
10
±10 triggers Critical Success / Critical Failure (e.g., Crit Trip inflicts 1d6 damage + Prone).
Mythras	Continuous Opposed 
𝑑
100
d100 Rolls: Both attacker (Combat Style %) and defender (Parry/Evade %) roll simultaneously.	100% Universal Special Effects: Whenever the winner beats the loser by 1 or 2 Levels of Success (Crit vs Fail, Success vs Fail), they instantly spend those levels to select maneuvers (Impale, Bleed, Overextend, Disarm, Trip, Riposte). Zero feat prerequisites.	Differential Level Comparison: The exact difference in success tiers dictates how many maneuvers are executed, making every single contested roll dynamic for both sides.
Our Mathless Engine (Blueprint)	Opposed Step Pools (Attacker NdX vs Defender MdY): Compare Highest Face Value (Max vs Max).	Universal Mathless Maneuver Tokens ([SET]): When your highest die beats the defender's highest die, every additional die in your pool that also beats their roll (or rolls max face) awards 1 Special Effect Token ([SET]) spent on universal maneuvers (Impale, Cleave, Disarm, Riposte) without math or class gates!	Face Differential & Multi-Beat Count: 1 beating die = Standard Hit; 2+ beating dice or Max Face = Hit + Special Effect Tokens.
Vector 16: Active Defense Action Economy

Whether defending yourself is a passive background stat (Armor Class) or actively consumes your turn's action budget.

System	Passive vs Active Defense	Action Budget Cost to Defend	Outnumbering / Tactical Pressure Impact
D&D 3.5e	100% Passive 
𝐴
𝐶
AC: Characters stand still; attackers roll against static 
𝐴
𝐶
AC.	Zero action cost during enemy turns (except 1 Reaction per round for Attack of Opportunity or Shield Block).	Low-to-Medium (Flanking gives +2 attack to enemies). A high-
𝐴
𝐶
AC character can passively deflect 10 attacks in a round without getting tired.
Pathfinder 2e	Hybrid Passive/Active: 
𝐴
𝐶
AC is baseline passive, but Raise a Shield ([1A]) increases 
𝐴
𝐶
AC by 
+
2
+2, and Shield Block ([R]) absorbs damage.	Requires spending 1 Action ([1A]) on your turn to raise your shield, plus 1 Reaction ([R]) out-of-turn to block.	Medium (Flanking gives Flat-Footed -2 AC). You only get 1 Reaction per round, so you can only Shield Block once per round regardless of how many enemies attack you.
Gloomhaven	Active Card Preparation: Players play Shield/Retaliate cards during their turn (Shield 1 this round).	Consumes card top/bottom actions during turn planning. Emergency defense requires burning/losing cards from hand.	High (Every attack absorbed by burning cards permanently shortens your character's lifespan/timer).
Mythras	100% Active Defense Economy: Defenders must declare active Parry or Evade rolls against incoming attacks.	Every single active Parry or Evade attempt consumes 1 Action Point (
𝐴
𝑃
AP) from your pool (typically 2-3 AP per round).	Extreme Tactical Pressure: Once your 
𝐴
𝑃
AP pool hits 
0
0, you cannot actively parry or evade. You must absorb incoming strikes purely with armor 
𝐷
𝑅
DR. Outnumbering a warrior (
3
𝑣
1
3v1) forces them to burn all 
𝐴
𝑃
AP defending, leaving them helpless to strike back!
Our Mathless Engine (Blueprint)	Hybrid Mathless Tension: Free initial guard slot ([1R]), then Stamina depletion (Stamina Burn).	Every character gets 1 Free Defensive Reaction ([1R]) per round (Parry or Shield Intercept). Additional parries/evasions in the same round cost 1 Stamina per attempt (Parry Fatigue).	Realistic Exhaustion: Outnumbering a fighter forces them to spend Stamina on every incoming blow. When Stamina hits 
0
0, their active defense collapses (Parry Pool = 0), forcing them to rely entirely on their physical Soak Rank (Armor Die).
Vector 17: Hit Location Granularity & Wound Severance

How systems track structural injury, anatomical targeting, and lethal thresholds.

System	Anatomical Targeting	Damage Reduction (
𝐷
𝑅
DR) Integration	Wound & Severance Thresholds
D&D 3.5e	Global HP Bar: Zero anatomical hit locations (150 HP = full fighting capacity until 0 HP).	Rare post-hit reduction (DR 5/magic). Armor strictly increases 
𝐴
𝐶
AC (hit/miss binary).	Zero wound penalties above 
0
𝐻
𝑃
0HP. At 
≤
0
𝐻
𝑃
≤0HP, character falls unconscious (bleeding out -1/round down to -10 death).
Pathfinder 2e	Global HP Bar + Wounded/Dying Conditions: No localized limb damage.	Armor gives item bonus to 
𝐴
𝐶
AC. Shield Hardness absorbs flat damage on a Shield Block reaction.	At 
0
𝐻
𝑃
0HP, gain Dying 1-4 condition. If healed, gain Wounded 1-3 flag (making future dying thresholds lower).
Mythras	7 Localized Hit Locations: (Head, Chest, Abdomen, Left/Right Arm, Left/Right Leg).	Armor applies Localized 
𝐷
𝑅
DR specific to each limb (e.g., Helm = +5 DR Head; Cloth tunic = +1 DR Chest).	3 Anatomical Wound Levels per location:<br>1. Minor Wound (HP > 0): Cuts/bruises (No penalty).<br>2. Serious Wound (HP <= 0): Limb useless/dropped weapon (Arm), Prone (Leg), Unconscious (Head/Chest).<br>3. Major Wound (HP <= -Max HP): Instant Limb Severance / Pulped Organ / Immediate Death.
Our Mathless Engine (Blueprint)	Mathless Anatomical Step Check (1d8 Location Matrix) triggered on Severe Hits.	Soak Rank (d4 to d12) checked post-hit: Compare Damage Die Face vs Soak Die Face. If Damage <= Soak, kinetic force absorbed (0 Wounds).	Wound Condition Escalation: When Damage Die > Soak Die, roll 1d8 Location Die (1-2 Head, 3-4 Chest, 5 Abdomen, 6-7 Arms, 8 Legs). Apply immediate anatomical Down-Shift or Bane (Arm = Drop item; Leg = Prone/Speed cut; Head = Muddled). Critical Hits (Damage rolled Max OR 2+ steps over Soak) inflict Severed Tendon / Fractured Rib / Mortal Wound without calculating HP subtraction!
Vector 18: GM Cognitive Load & Mob Scaling (Minion vs Rabble Architecture)

How the ruleset manages game master tracking when running large groups of enemies (
10
-
20
+
10-20+ monsters).

System	Mob / Minion Tiering	Tracking Required per Mob Unit	Special Ability / Maneuver Access
D&D 3.5e	No Formal Minion Rules: Every monster (even a Goblin) has full Hit Dice (HP 5), 
𝐴
𝐶
AC, attack bonus, and saving throws.	High tracking during mass combat (Tracking individual HP across 15 goblins creates massive GM bookkeeping).	Full access to feats and racial traits (e.g., Orc Ferocity, Goblin Stealth).
Pathfinder 2e	Troop Rules (Swarm/Unit blocks): Groups of low-level enemies combine into a single massive "Troop" creature (Gargantuan size).	Single unified HP bar, area attacks, and shared saving throws for the entire 16-man squad.	Troop uses unified area maneuvers (Form Phalanx, Volley Fire) rather than individual actions.
Mythras	3-Tier Enemy Architecture:<br>1. Rabble (Minions)<br>2. Underlings (Soldiers)<br>3. Iconic Foes (Bosses)	Rabble & Underlings eliminate Hit Locations: They track only a single unified HP threshold (Rabble die on 1st wound; Underlings die on 2nd wound/Serious wound).	Rabble cannot use Special Effects (pure cannon fodder). Underlings use full Special Effects but flee when half their squad drops. Iconic Foes use full 7-location anatomical tracking.
Our Mathless Engine (Blueprint)	3-Tier Mathless Mob Architecture:<br>1. Rabble (Minions)<br>2. Underlings (Soldiers)<br>3. Iconic Champions	Zero HP Bookkeeping for Rabble/Underlings:<br>• Rabble: Defeated/routed on ANY strike that beats their Soak Rank (Damage > Soak = Instant Kill/Flight).<br>• Underlings: Defeated on any Critical Hit OR upon taking 2 standard hits (Checkmark box [○][○]).	Rabble roll base pool (2dX) with zero Boon/Maneuver access. Underlings can earn and spend 1 Maneuver Token ([SET]). Iconic Champions utilize full multi-layer defenses, Hyper-Shifting, and anatomical wound clocks.
Open
Case Study 5: Mythras & The $d100$ Differential Special Effects Engine
MD
Case Study 5: Mythras & The 
𝑑
100
d100 Differential Special Effects Engine

To expand our research template and uncover foundational mechanics that can elevate our idealized mathless system, we conducted a deep structural analysis of Mythras (formerly RuneQuest 6, developed by Lawrence Whitaker and Pete Nash at The Design Mechanism).

Mythras represents the pinnacle of grounded, simulationist d100 combat design. It proves that tactical depth and dramatic stakes do not require class-locked feat trees, escalating 
𝐻
𝑃
HP bloat, or mathematical modifier inflation.

1. Core Architectural Pillars of Mythras
1.1 The 
𝑑
100
d100 Opposed Check & Differential Levels of Success

Unlike passive combat engines where an attacker rolls against a static Armor Class (
𝐴
𝐶
AC), combat in Mythras is actively opposed.

Both attacker and defender roll simultaneously (
𝑑
100
d100 percentile roll under their respective Combat Style % or Evade %).
Every roll achieves one of four Levels of Success:
Critical Success: Rolling 
≤
1
/
10
th
≤1/10th of the skill rating (e.g., Skill 
65
%
→
65%→ Crit on 
1
-
7
1-7).
Standard Success: Rolling between critical threshold and the skill rating (
≤
65
%
≤65%).
Standard Failure: Rolling above skill rating (
66
-
98
%
66-98%).
Fumble: Rolling 
99
-
00
99-00.

Instead of merely checking who hit or missed, Mythras compares the difference in success levels between the combatants. If my attack is a Critical Success (Level 4) and your parry is a Standard Failure (Level 2), I win by Two Levels of Success (
4
−
2
=
2
4−2=2).

text
[ Attacker: Critical Success (Level 4) ]  vs  [ Defender: Standard Failure (Level 2) ]
                                    │
                                    ▼
                [ Differential: +2 Levels of Success ]
                                    │
               ┌────────────────────┴────────────────────┐
               ▼                                         ▼
   [ Spend Level 1: Impale ]                 [ Spend Level 2: Bleed ]
(Drive spear deep; weapon stuck)         (Sever artery; rapid blood loss)
1.2 Universal Special Effects (Maneuvers Without Class Walls)

The "secret sauce" of Mythras is what you do with those differential levels of success: Special Effects.

Whenever a combatant wins an opposed roll by 1 or 2 levels of success, they immediately spend those differential levels to choose from a universal catalog of Special Effects.
No Class Restrictions or Level Gates: A starting character on turn one has access to the exact same pool of maneuvers as a seasoned veteran. If you achieve a critical hit over a failed parry, you don't need a level 12 "Impaling Feat"; you simply choose Impale right at the table.
Active Defense Turns the Tables: If the attacker misses (Failure) and the defender succeeds (Critical Success or Success), the defender gains Special Effects against the attacker. A parrying warrior can instantly Disarm, Overextend, Trip, or Riposte their attacker out-of-turn.
2. Mythras Special Effects Catalog (Offensive vs Defensive)

Every maneuver is succinctly defined in a paragraph or less, allowing rapid table execution:

2.1 Sample Offensive Special Effects
Impale: Drives a piercing weapon deep into the target. Deals maximum weapon damage or rolls twice, and the weapon remains wedged inside, inflicting agonizing pain (penalties to all actions) until wrenched free (causing secondary damage).
Bleed: Severs a major blood vessel. The target loses 
1
1 or 
2
2 Fatigue/HP at the start of every turn until medically sutured or coagulated.
Bypass Armor: The strike slips through a gap in plate armor or thick hide (e.g., eye slit, armpit). The target's armor Damage Reduction (
𝐷
𝑅
DR) is completely ignored for this hit.
Compel Surrender: Instead of striking a lethal blow, the victor holds their blade to the opponent's throat or eye, forcing an immediate morale/surrender check before blood is shed.
Maximize Damage: The kinetic blow strikes squarely on bone. All weapon damage dice automatically yield their maximum face value.
Stun / Bash: A heavy blunt strike rattles the brain or nervous system. Target must pass a Endurance check or drop incapacitated for 
1
𝑑
4
1d4 rounds.
2.2 Sample Defensive Special Effects (Earned via Successful Parry/Evade over Attack)
Overextend Opponent: The defender redirects the attacker’s momentum off-balance. The attacker suffers an immediate penalty on their next defensive roll or loses an Action Point (
𝐴
𝑃
AP).
Disarm: The defender catches the attacker’s blade with a crossguard or shield rim, wrenching it out of their hands (opposed Brawn/Strength check to retain).
Trip / Drop Foe: A quick foot-sweep or shield bash sends the attacker sprawling Prone.
Riposte: If the parry was a Critical Success against a Failure, the defender gets a free, immediate counter-attack strike that cannot be parried.
Damage Weapon: The defender angles their heavy shield or hardened blade to catch the opponent's weapon shaft, inflicting direct structural damage (Hardness/Hit Points) to break the incoming weapon.
3. Hit Locations & The 3-Tier Anatomical Wound System

While most games track a single abstract bar of 
100
+
100+ Hit Points, Mythras uses Localized Hit Locations (Head 13-20, Chest 09-12, Abdomen 07-08, Left Arm 04-06, Right Arm 01-03, Left Leg/Right Leg).

3.1 Static HP & Armor Soak per Location
Each location has its own static pool of Hit Points based on character Size and Constitution (e.g., Head = 5 HP, Chest = 7 HP, Arm = 4 HP). These points do NOT scale with character advancement. A veteran warrior has roughly the same anatomical HP as a novice.
Armor applies local Damage Reduction (
𝐷
𝑅
DR) only to the location it covers (e.g., Steel breastplate = +6 DR on Chest; Leather bracers = +2 DR on Arms).
3.2 The Three Wound Levels

When damage overcomes armor 
𝐷
𝑅
DR, it depletes the local Hit Points and triggers one of three concrete wound states:

Wound Level	Local HP Formula	Anatomical Consequence & Narrative Reality
1. Minor Wound	Local HP > 0	Standard cuts, bruises, and kinetic shock. Causes pain and minor bleeding, but no structural impairment.
2. Serious Wound	Local HP <= 0<br>(but > -Starting HP)	Structural failure of the limb or organ. If an Arm, the limb goes limp (Drop weapon/shield). If a Leg, target falls Prone (Cannot stand/run). If Head, Chest, or Abdomen, target collapses Unconscious and must make Endurance rolls to avoid bleeding out.
3. Major Wound	Local HP <= -Starting HP<br>(Negative local max)	Catastrophic Severance & Destruction. An Arm or Leg is cleanly severed or crushed beyond repair (Instant shock, permanent loss). If Head, Chest, or Abdomen, the skull is crushed or heart punctured 
→
→ Instant Death.
4. Action Points (AP) & Defensive Action Economy

In Mythras, survival is governed by the Action Point (
𝐴
𝑃
AP) Budget:

Characters typically possess 2 or 3 Action Points (
𝐴
𝑃
AP) per combat round.
Active Defense Costs 
𝐴
𝑃
AP: Every offensive strike costs 
1
𝐴
𝑃
1AP. Crucially, every active Parry or Evade also costs 
1
𝐴
𝑃
1AP.
The Outnumbering Dilemma: If you are attacked by three foes and spend all your 
𝐴
𝑃
AP parrying the first two strikes, you have zero 
𝐴
𝑃
AP left when the third strike arrives. You cannot actively parry or evade; you must rely entirely on passive armor 
𝐷
𝑅
DR and luck (Automatic hit against your location). This makes tactical positioning, shield walls, and outnumbering enemies matter deeply without artificial math.
5. Rabble & Underlings (Scaling GM Workload)

To prevent the GM from getting bogged down tracking Hit Locations for a mob of 15 goblins, Mythras categorizes non-iconic enemies into two streamlined tiers:

Enemy Tier	Hit Location Tracking?	Special Effect Access?	Morale & Defeat Threshold
Rabble (Minions)	NO (Single Pool)	NO	Unskilled mobs. They die, flee, or scream upon taking 1 single wound (Any hit past armor drops them).
Underlings (Soldiers)	NO (Single Pool)	YES (Can use & suffer Special Effects)	Competent soldiers. They track a simplified 2-wound threshold and automatically check morale (Flee/Surrender) upon taking a Serious wound or losing half their squad.
Iconic Foes (Bosses)	YES (Full Hit Locations)	YES (Full Mastery)	Major villains, dragons, and rival champions. Built with full anatomical hit locations, armor layers, and high 
𝐴
𝑃
AP pools.
6. How We Adapt Mythras into Our Mathless 2dX Engine

Mythras’s brilliance provides four direct structural upgrades for our idealized mathless system (2dX keep highest):

Mathless Differential Special Effects (Maneuver Tokens):
Instead of checking 
𝑑
100
d100 math differentials, we measure success differentials directly from our Step Pool Faces:

Trigger 1 (Multi-Beat Differential): If your check pool (3d8) rolls 5, 7, 8 against a Target DC 6 (or against an opponent's parry face of 6), you have two dice (7 and 8) that beat the target. Each extra beating die awards 1 Mathless Special Effect Token ([SET]) (2 beating dice = 1 standard hit + 1 Special Effect).
Trigger 2 (Max Face Surge): Rolling the maximum face value (8 on 
𝑑
8
d8) automatically awards +1 Special Effect Token ([SET]).
These tokens ([SET]) are spent instantly from our universal table (Impale, Bleed, Disarm, Overextend, Riposte) without checking class prerequisites!

The Active Defense Economy (Stamina / Reaction Trade-off):
We adopt Mythras's defensive tension: every character has 1 free Reaction slot ([1R]) per round (Raise Shield). If targeted by additional attacks beyond that slot, they must burn 1 Stamina per active parry/evade (Parry Fatigue). If they run out of Stamina, they cannot parry, leaving their physical Soak Rank as their only line of defense.

Hit Location Integration (Anatomical Step Matrix):
We integrate Mythras's anatomical locations into our wound model. When an attack beats Soak by 
≥
1
≥1 step (Severe Wound), the player or GM rolls a single Anatomical Location Die (
1
𝑑
8
1d8) (1-2 Head, 3-4 Chest, 5 Abdomen, 6-7 Arms, 8 Legs) to apply localized structural impairments (Dropped weapon, Prone, Concussion) without adding numerical HP bookkeeping.

Rabble & Underling Mob Management:
We adopt exact Mythras mob tiers for GMs: Rabble die on any hit exceeding Soak; Underlings use Special Effects but collapse after 1 severe wound; Iconic Bosses use full multi-layer defenses and anatomical wound clocks.

Open
used
Bash
79ms

We have fully integrated Mythras (BRP / 
𝑑
100
d100 System) across our entire research template, master comparative matrix, and mathless baseline architecture.

By extracting the mechanics from your transcript and analyzing Mythras’s design (the RuneQuest 6 / BRP engine by Lawrence Whitaker and Pete Nash), we uncovered four game-changing structural patterns that solve traditional d20 combat problems (turn wait times, resource attrition attrition, HP bloat, and class-locked feat walls).

🏛️ What We Added & How We Expanded Our Templates
1. New Dedicated Case Study: 02_comparative_system_analysis/03_mythras_and_brp_case_study.md (Presented Above)

This document dissects Mythras’s core mechanics and demonstrates how we translate them directly into our Mathless 2dX Keep Highest Pool Engine:

The 
𝑑
100
d100 Differential Success Levels: In Mythras, combat is an opposed roll where the difference in success levels (Critical vs Failure = +2 levels difference) generates dynamic outcomes.
Universal Special Effects: Instead of class feat trees, winning an opposed check awards immediate access to universal maneuvers (Impale, Bleed, Bypass Armor, Disarm, Overextend, Riposte). Even defenders gain Special Effects when they out-roll an attacker!
Anatomical Hit Locations & 3-Tier Wounds: Instead of a single 
150
+
𝐻
𝑃
150+HP bar, characters track localized body parts (Head, Chest, Abdomen, Arms, Legs). Armor applies local 
𝐷
𝑅
DR. Damage exceeding local HP triggers concrete Minor, Serious, or Major Wounds (Limb severance, unconsciousness, instant death).
Active Defense Action Economy (
𝐴
𝑃
AP & Stamina): Defending is not passive. Parrying or evading costs Action Points (
𝐴
𝑃
AP). Outnumbering a warrior (
3
𝑣
1
3v1) forces them to exhaust their defensive actions on the first two strikes, leaving them exposed to the third!
Rabble & Underling Architecture: Simplifies GM tracking by removing Hit Locations and HP bars for minion hordes (Rabble die after 1 hit past armor).
2. Expanded Master Architecture Matrix (v4 Master Expanded)

We updated 02_comparative_system_analysis/01_architecture_matrix_v3_expanded.md into a 23-System Schema Matrix across 18 Analytical Vectors, adding Mythras (BRP/$d100$) across all 10 core sheet categories and introducing Four New System Comparison Vectors across all 23 games:

Vector 15: Opposed Differential Maneuvers (The Special Effect Engine)
How outcomes are evaluated and how differential rolls unlock immediate maneuvers without feat tax.
Vector 16: Active Defense Action Economy (Passive vs Active Defense Budget)
Whether defense is a passive background stat (
𝐴
𝐶
AC) or actively consumes action budget / stamina under numerical pressure.
Vector 17: Hit Location Granularity & Wound Severance (Anatomical vs Global Damage)
Whether damage drains a single global HP bar or targets localized anatomical limbs with concrete structural thresholds (Minor/Serious/Major).
Vector 18: GM Cognitive Load & Mob Scaling (Rabble / Underling Architecture)
How the ruleset scales from 1v1 duels to massive battles (
15
+
15+ monsters) without GM math overload.
3. Core Engine Upgrades (Updated Mathless Baseline Rules)

To ensure these Mythras breakthroughs are fully actionable inside our own system, we directly updated three of our core baseline rulesets:

⚔️ 03_core_baseline_system/01_resolution_engine.md (Added Section 7: Mathless Special Effect Tokens - [SET])
Whenever an attacker and defender make an opposed step check (Attacker NdX vs Defender MdY), the character with the Highest Single Face Value wins the clash.
Generating Maneuver Tokens ([SET]):
For every additional die in the winner's pool that meets or exceeds the loser's highest roll, award 
+
1
 Special Effect Token (‘[SET]‘)
+1 Special Effect Token (‘[SET]‘).
If the winner's highest die rolled its Maximum Face Value (8 on 
𝑑
8
d8, 12 on 
𝑑
12
d12), award an extra 
+
1
 [SET]
+1 [SET].
Instant Table Spend: Tokens ([SET]) are spent instantly from our universal catalog without checking class prerequisites:
1 [SET] 
→
→ Impale (Weapon wedged inside; +1 Bane on all target actions)
1 [SET] 
→
→ Bleed (1 Vitality loss every round until sutured)
1 [SET] 
→
→ Bypass Soak (Step down target armor Soak two ranks for this hit)
1 [SET] 
→
→ Disarm / Trip / Overextend (Opponent loses 1 Action Point)
2 [SET] 
→
→ Riposte (Free un-parriable counter-strike) OR Maximize Impact (Automatic max damage face)
🛡️ 04_simulationist_subsystems/01_defenses_and_damage_modeling.md (Added Section 5: The 
1
𝑑
8
1d8 Anatomical Matrix)
When an attack achieves a Standard Hit (Damage > Soak) or Critical Hit (Damage rolled Max Face), the player rolls a single Anatomical Location Die (
1
𝑑
8
1d8) to apply localized structural trauma without calculating HP subtraction:
1 (Head) 
→
→ Concussion / Dazed (Step down INT/WIL d10 -> d8; drop spell concentration)
2-3 (Chest) 
→
→ Winded / Bruised Rib (Lose 3 Stamina instantly; spend Stamina hurts)
4 (Gut) 
→
→ Internal Trauma (+1 Bane on physical checks + Bleeding Cut)
5 (Shield Arm) 
→
→ Limp Shield Arm (Drop shield immediately in adjacent zone)
6 (Weapon Arm) 
→
→ Limp Weapon Arm (Drop weapon instantly; off-hand takes +2 Banes)
7-8 (Legs) 
→
→ Buckled Knee (Fall Prone immediately; Speed 0 until standing up)
📊 04_simulationist_subsystems/03_resources_conditions_and_wounds.md (Added Sections 5 & 6: Active Defense & Mob Scaling)
Parry Fatigue (Active Defense Economy): Every character gets 1 Free Defensive Reaction ([1R]) per round. Additional active parries/evades in the same round cost 1 Stamina per attempt (Active Defense Expenditure). When Stamina hits 
0
0, active defense collapses (Parry Pool = 0), leaving the character's physical Soak Rank (Armor Die) as their sole defense against the swarm.
3-Tier GM Mob Management:
Rabble (Minions): Zero HP & Zero Hit Location tracking. Defeated/routed on ANY strike that rolls higher than their Soak Rank (Damage > Soak). No Special Effect access.
Underlings (Soldiers): Track a simple 2-box checkmark ([○] [○]). Can use 1 Special Effect Token per round.
Iconic Champions (Bosses): Full anatomical hit locations, multi-layer defenses, and Hyper-Shifting.
📝 Updated Master Roadmap (DEC-007 to DEC-010 Logged)

In 06_brainstorming_logs_and_roadmap/01_master_brainstorm_log.md, we formally logged these four architectural decisions (DEC-007 differential tokens, DEC-008 active defense Stamina burn, DEC-009 
1
𝑑
8
1d8 anatomical hit locations, and DEC-010 3-tier mob tiering).

🎯 What Would You Like to Tackle Next?

With Mythras, D&D 3.5e, Pathfinder 2e, Shadow of the Demon Lord, and our hybrid board game vectors fully unified into a cohesive, mathless baseline, we have a world-class foundation. Where should our brainstorm focus next?

Character Creation & Path Progression Walkthrough: Let's create our first complete, step-by-step character creation guide (Step 1: Attributes -> Step 2: Mastery Domains -> Step 3: Novice Path -> Step 4: Defense & Soak -> Step 5: Equipment), building a sample 3.5e fighter/berserker character from scratch.
Round-by-Round Combat Simulation Walkthrough: Let's run a full, detailed play-by-play combat encounter (A party of 3 heroes vs an Ogre Boss and 6 Goblin Rabble) to show exactly how initiative, 3-action budgeting, opposed pool checks, differential [SET] spending, and anatomical 1d8 location rolls play out at the table in real time.
Deep-Dive into Magic, Spells & Focus Channeling: Let's construct the exact mechanics for spellcasting (Arcana, Divine, Primal, Shadow, Time), spell interruption via anatomical hits (Head hit = Focus lost), and convert 10 iconic spells into mathless area conditions.
Feat & Path Translation Compendium: Let's start building a master compendium translating 30+ iconic D&D 3.5e feats (Combat Reflexes, Whirlwind Attack, Spring Attack, Spell Penetration) into clean 1-sentence mathless vector traits.

Let me know what you'd like to dive into next!
