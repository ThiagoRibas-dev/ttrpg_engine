---
turn: 70
role: "AI-Designer"
source: chat_history.json
---

# Turn 70 — AI-Designer

used
Bash
78ms
Edited files
3
01_master_brainstorm_log.md
MD
Universal Building Blocks & Master Skill System Architecture
MD
Universal Building Blocks & Master Skill System Architecture

To ensure every choice on a character sheet (and universal monster stat block — DEC-011) models a distinct aspect of reality without mechanical overlap, we must clearly define what each building block represents conceptually and mechanically. Furthermore, we must establish our definitive Master Skill Taxonomy (Specific Skills grouped under 5 Domain Umbrellas — DEC-030) across our 5 Competency Ranks (DEC-020).

This document evaluates three building block arrangements, establishes our 5-Block High Fantasy baseline, and lays out the complete skill system.

1. Candidate Building Block Arrangements (Evaluating the Architecture)

When structuring what defines an actor (PC, NPC, or Monster), we evaluated three candidate arrangements:

1.1 Arrangement 1: The Classic 4-Block (Race + Class + Skills + Feats)
What each block models:
1. Race / Ancestry (Biological Reality): Size, Speed, Darkvision, natural armor Absorption steps (ABS), biological claws/wings.
2. Class Archetype (Professional Vocation): 20-level advancement tracks (Vitality, Check Pool/Floor, Paired Saves, Vancian/Focus, Skill Allocations — DEC-035).
3. Skills (Learned Proficiencies): Specific individual capabilities (Stealth, Lockpicking, Arcana, Diplomacy) advanced via skill allocations.
4. Feats (Modular Techniques): Discrete rules overrides, action economy permissions ([1A], [2A], [1R]), and specialized maneuvers.
Pros: 100% familiar 3.5e/PF2e structural mapping.
Cons: Leaves where a character's automatic primary attribute step growth (DEC-039) comes from slightly ambiguous (does it belong to Race or Class?).
1.2 Arrangement 2: The 5-Block High Fantasy Division (Race + Background + Class + Skills + Feats — Recommended Baseline)
What each block models:
1. Race / Ancestry (Biological Reality): Size, Speed, reach tiers, biological hide toughness (ABS d4-d10), and genetic immunities.
2. Background / Origin (Innate Exceptional Focus & Upbringing — DEC-039): What you dedicated your life to before adventuring (Blacksmith, Noble, Soldier, Scholar). Designates your ONE Primary Attribute (starting at d8, stepping up automatically at Lvl 5, 9, 15, 20), and awards 1 specific starting Skill (e.g., Crafting, Diplomacy, Longswords) at Trained (Floor 3) for free!
3. Class / Archetype (Professional Adventuring Vocation): Your 20-level good/okay/bad advancement tracks (Vitality, Check Pool/Floor, Saves, Vancian/Focus, Skill Allocations — DEC-035).
4. Skills (Action Mastery Domain Proficiencies): Specific capabilities (Stealth, Arcana, Athletics) purchased via your class skill allocations across all 20 levels.
5. Feats (Modular Vector Techniques): Action economy permissions ([1A], [2A], [1R]) and specialized combat/magical maneuvers.
Pros: Absolute conceptual clarity. Demystifies your primary attribute scaling (DEC-039) right into a rich narrative origin (Background), while keeping Race strictly biological and Class strictly vocational (no skill tax — DEC-041).
Cons: Adds 1 additional selection block at Level 1 (5 blocks instead of 4). However, because Background runs on automatic pilot after Level 1 (stepping up at Lvl 5, 9, 15, 20), it simplifies campaign math!
1.3 Arrangement 3: The SotDL Modular Path Division (Race + Paths [Novice/Expert/Master/Legend] + Skills + Feats)
Structure: Replaces the single 20-level linear "Class" block with Four Layered Paths across our 6 Tiers (Novice Path at Lvl 1, Expert Path at Lvl 5, Master Path at Lvl 9, Legend Path at Lvl 17 — DEC-013 & DEC-027)! Each path (say, Novice Warrior + Expert Berserker + Master Blade Dancer) awards specific Vitality increments, skill allocations, and path feats across its 4-level band.
Pros: Unmatched option-density and multiclassing freedom without dead levels or prerequisite traps.
Cons: Can feel more modular/SotDL-centric for traditional 3.5e purists who prefer a single 1-to-20 class identity (though 3.5e prestige classes operated on a very similar modular principle).
2. Master Skill Taxonomy (Specific Skills Under 5 Domain Umbrellas)

With Arrangement 2 (5-Block High Fantasy Division) locked in (DEC-045), skills are not broad abstract buckets (where "Social" makes you equally good at lying and diplomacy — DEC-030). Instead, our 5 Action Mastery Domains act as Categorical Umbrellas organizing Specific Individual Skills:

text
[ Universal Skill Ecosystem: The 5 Domain Umbrellas & Specific Skills ]
  ├── 1. Combat Mastery Domain (`STR / DEX`)
  │     ├── Heavy Blades (`Longswords, Greatswords`)   ├── Polearms & Spears (`Halberds, Pikes`)
  │     ├── Finesse Blades (`Rapiers, Daggers, Sabers`)├── Bows & Crossbows (`Shortbows, Longbows`)
  │     ├── Axes & Picks (`Battleaxes, Heavy Picks`)   ├── Thrown Weapons (`Javelins, Axes, Knives`)
  │     ├── Maces & Hammers (`Flails, Morningstars`)   └── Shields & Brawling (`Shield Bash, Martial Arts`)
  │
  ├── 2. Survival & Athletics Domain (`STR / CON`)
  │     ├── Athletics (`Climbing, Swimming, Jumping`)  ├── Beast Handling (`Riding, Taming, Training`)
  │     ├── Endurance (`Forced Marches, Starvation`)   └── Survival (`Tracking, Foraging, Camp Defense`)
  │
  ├── 3. Subterfuge & Navigation Domain (`DEX / INT`)
  │     ├── Stealth (`Moving Silently, Shadowing`)     ├── Lockpicking (`Opening Mechanical/Tumbler Locks`)
  │     ├── Camouflage (`Hiding from View, Disguise`)  ├── Trap Disarming (`Disarming Mechanical/Magical Traps`)
  │     ├── Acrobatics (`Tumbling, Balance, Escaping`) └── Navigation (`Sailing, Piloting, Astrological Mapping`)
  │
  ├── 4. Lore & Crafting Domain (`INT / WIS`)
  │     ├── Arcana Lore (`Draconic, Planar, Magic Theory`)├── Medicine (`First Aid, Surgery, Suture Mastery`)
  │     ├── Nature Lore (`Beasts, Flora, Weather Theory`) ├── Blacksmithing (`Forging Blades, Armor, Tools`)
  │     ├── History Lore (`Ancient Kingdoms, Relics`)     ├── Alchemy (`Brewing Potions, Poisons, Acids`)
  │     ├── Magic Traditions (`Arcana, Divine, Primal...`)└── Engineering (`Siege Engines, Architecture, Clockwork`)
  │
  └── 5. Social & Influence Domain (`WIS / CHA`)
        ├── Diplomacy (`Persuasion, Etiquette, Treaties`)├── Leadership (`Command, Morale Boost, Rallying`)
        ├── Intimidation (`Coercion, Interrogation, Fear`)├── Insight (`Empathy, Detecting Lies, Motives`)
        └── Deception (`Lying, Bluffing, Forgery, Gambling`)└── Performance (`Music, Oratory, Distraction`)
3. The 5 Competency Ranks (Investment-Driven Step, Volume & Floor)

When a character levels up and allocates their Class Skill Allocations (DEC-035 Track 5), they invest points directly into Specific Individual Skills (e.g., investing into *Diplomacy* to reach Expert (+1B, +1 Step, Floor 5), while leaving *Deception* under the same Social umbrella at Untrained (Floor 0)`!).

Advancing a specific skill rank transforms your check pool across all three check variables (Die Size X, Pool Volume N, and Competency Floor F):

Competency Rank (Investment Level)	Check Pool Modification (Die Size X & Pool Volume N)	Competency Floor (F)	Multi-Success Maneuver Permissions (DEC-043)	What This Represents Physically & Conceptually
0. Untrained (Zero Investment)	Base Pool 2dX keep highest<br>(Attribute Die only — $+0B, +0 Steps)*	Floor = 0<br>(Pure random roll)	Can execute 1 Success Standard Hits (Damage vs ABS). No multi-success maneuver triggers (Prone, Disarm, Wounds).	Raw, unassisted civilian capability without technical technique (11.1% whiff rate on 2d6 vs routine DC 3).
1. Trained (Basic Focus — 1 Allocation)	Pool Volume 3dX (+1B)<br>(Rolls 3 dice of base Attribute size)	Floor = 3<br>(Guaranteed min face 3)	Immune to failing DC 3 Routine checks (100%). Can trigger standard default maneuvers on 2+ Successes (Trip, Disarm, Shove).	Professional competence (e.g., proper edge alignment, basic diplomatic etiquette, or silent footwork).
2. Expert (Specialist — 2 Allocations)	Pool Volume 3dX (+1B) + 1 Die Step-Up (X+1)<br>(e.g., Attribute d8 
→
→ rolls 3d10)	Floor = 5<br>(Guaranteed min face 5)	Immune to failing DC 5 Challenging checks (100%). Can execute Called Shot Anatomical Wounds (3 Successes).	Dedicated specialization (e.g., veteran regional champion, master surgeon, or elite spy). Surpasses basic physical limits via technique!
3. Master (Grandmaster — 3 Allocations)	Pool Volume 4dX (+2B) + 2 Die Step-Ups (X+2)<br>(e.g., Attribute d8 
→
→ rolls 4d12)	Floor = 7<br>(Guaranteed min face 7)	Immune to failing DC 7 Formidable checks (100%). Unlocks Whirlwind Strike [3A] and Shatter Absorption multi-beats.	Realm-renowned grandmastery. The character's technique is so precise they literally never miss formidable obstacles (Floor 7).
4. Legendary (Mythic Apex — 4 Allocations)	Pool Volume 5dX (+3B) + 3 Die Step-Ups (X+3)<br>(e.g., Attribute d8 
→
→ rolls 5d12+1 over-cap)	Floor = 9<br>(Guaranteed min face 9)	Immune to failing DC 9 Heroic checks (100%). All standard hits in this specific skill automatically gain +1 Multi-Success beat for free!	Mythic mortal apex (DEC-014). Multiversal legends whose skills reshape physical, social, or arcane reality across the planes.
4. Concrete Examples (Specific Skill Checks in Action)

To see how our 5-Block high fantasy setup (Race + Background + Class + Skills + Feats) and specific skill competency ranks operate without arithmetic, look at these four real-time checks across our domains:

4.1 Subterfuge Check (Level 6 Expert Rogue vs. DC 7 Formidable Mechanical Lock)
Character Setup: Level 6 Elven Rogue (AGI d10, DEX d10, INT d8). Background: Street Urchin (Primary DEX d10). Class: Rogue (Okay BAB, Good Skill Allocations — DEC-035).
Specific Skill Investment: Invested 2 skill allocations into Lockpicking 
→
→ Expert Rank (+1B, +1 Die Step-Up, Floor 5). (Note: She left Trap Disarming at Trained Floor 3 and Sailing at Untrained Floor 0!)
Rolling the Check (Zero Math): Her base DEX is d10. Because she is an Expert in Lockpicking, her die size steps up (d10 
→
→ d12), and she gains +1B volume (2d 
→
→ 3d). She rolls 3d12 keep highest (Floor 5) vs DC 7.
Outcome: She rolls 4, 8, 11. Highest face is 11 (11 >= DC 7 -> Success!). Furthermore, because 8 also beats 7, she achieves 2 Successes (Multi-Beat Complex Check — DEC-036), picking the complex lock in half the time without making a sound!
4.2 Social Check (Level 10 Master Paladin vs. Hostile King's Willpower Defense Pool)
Character Setup: Level 10 Human Paladin (STR d10, CON d10, WIS d8, CHA d10). Background: High Noble (Primary CHA d10, stepped up to d12 at Lvl 9). Class: Paladin (Full Martial, Good Fort/Will).
Specific Skill Investment: Invested 3 allocations into Diplomacy 
→
→ Master Rank (+2B, +2 Die Step-Ups, Floor 7).
Rolling the Check (Zero Math): His base CHA is d12. Because he is a Master in Diplomacy, his die steps twice (d12 
→
→ over-cap d12+2), and he gains +2B volume (2d 
→
→ 4d). He rolls 4d12+2 keep highest (Floor 7) directly against the King's opposed Willpower Pool (1dWIS + 1dCHA keep highest -> 2d10).
Outcome: The Paladin rolls 6, 9, 12, 14. Because his Competency Floor is 7, his 6 becomes 7. The King rolls 4, 8. The Paladin's 14 crushes the King's 8 (Success!). Because 12 and 9 also beat the King's 8, the Paladin scores 3 Successes (Overwhelming Social Dominance), forging an immediate binding treaty and rallying the King's army to his cause right at the table!
Open
used
Bash
99ms

Your spitballed definition (Race = Biology, Class = Heroic Vocation, Skills = General learned proficiencies, Feats = Specific learned techniques) is 100% accurate and simulationist.

To make sure where your automatic primary attribute scaling (DEC-039) comes from is crystal clear, we evaluated three candidate building block arrangements and locked in Arrangement 2 (The 5-Block High Fantasy Division — DEC-045), detailed alongside our complete Master Skill Taxonomy (DEC-046) in 03_core_baseline_system/13_building_block_domains_and_master_skill_system.md (presented above).

🏛️ The 3 Candidate Building Block Arrangements (Pros & Cons)
Arrangement	Structure & Conceptual Boundaries	Pros (Why it works)	Cons (Trade-offs)
1. Classic 4-Block<br>(Our Initial Anchor)	Race + Class + Skills + Feats<br>Race=Biology; Class=Vocation; Skills=Universal proficiencies; Feats=Specific techniques.	100% familiar 3.5e/PF2e structural mapping. Zero overlap between biology, vocation, and techniques.	Leaves where a character's automatic primary attribute step scaling (DEC-039) comes from slightly ambiguous (Race or Class?).
2. 5-Block High Fantasy<br>(Locked Baseline — DEC-045)	Race + Background + Class + Skills + Feats<br>Adds Background (Origin): What you did before adventuring (Blacksmith, Noble, Soldier, Scholar). Designates your ONE Primary Attribute (starting at d8, stepping automatically at Lvl 5, 9, 15, 20), and awards 1 specific starting Skill at Trained (Floor 3) for free!	Absolute conceptual clarity. Demystifies your primary attribute scaling (DEC-039) right into a rich narrative origin (Background), while keeping Race strictly biological and Class strictly vocational (no skill tax — DEC-041).	Adds 1 selection step at Level 1 (5 blocks instead of 4). However, because Background runs automatically after Level 1, it simplifies campaign math!
3. SotDL Modular Path	Race + Paths [Novice/Expert/Master/Legend] + Skills + Feats<br>Replaces linear Class block with Four Layered Paths across our 6 Tiers (Lvl 1, 5, 9, 17) (DEC-013 & DEC-027).	Unmatched option-density and multiclassing freedom without dead levels or prerequisite traps.	Can feel more modular/SotDL-centric for traditional 3.5e purists who prefer a single 1-to-20 class identity.
🌳 Master Skill Taxonomy (Specific Skills Under 5 Domain Umbrellas — DEC-046)

With Arrangement 2 (5-Block High Fantasy Division) locked in, skills are not broad abstract buckets (where "Social" makes you equally good at lying and diplomacy). Instead, our 5 Action Mastery Domains act as Categorical Umbrellas organizing Specific Individual Skills:

text
[ Universal Skill Ecosystem: The 5 Domain Umbrellas & Specific Skills ]
  ├── 1. Combat Mastery Domain (`STR / DEX`)
  │     ├── Heavy Blades (`Longswords, Greatswords`)   ├── Polearms & Spears (`Halberds, Pikes`)
  │     ├── Finesse Blades (`Rapiers, Daggers, Sabers`)├── Bows & Crossbows (`Shortbows, Longbows`)
  │     ├── Axes & Picks (`Battleaxes, Heavy Picks`)   ├── Thrown Weapons (`Javelins, Axes, Knives`)
  │     ├── Maces & Hammers (`Flails, Morningstars`)   └── Shields & Brawling (`Shield Bash, Martial Arts`)
  │
  ├── 2. Survival & Athletics Domain (`STR / CON`)
  │     ├── Athletics (`Climbing, Swimming, Jumping`)  ├── Beast Handling (`Riding, Taming, Training`)
  │     ├── Endurance (`Forced Marches, Starvation`)   └── Survival (`Tracking, Foraging, Camp Defense`)
  │
  ├── 3. Subterfuge & Navigation Domain (`DEX / INT`)
  │     ├── Stealth (`Moving Silently, Shadowing`)     ├── Lockpicking (`Opening Mechanical/Tumbler Locks`)
  │     ├── Camouflage (`Hiding from View, Disguise`)  ├── Trap Disarming (`Disarming Mechanical/Magical Traps`)
  │     ├── Acrobatics (`Tumbling, Balance, Escaping`) └── Navigation (`Sailing, Piloting, Astrological Mapping`)
  │
  ├── 4. Lore & Crafting Domain (`INT / WIS`)
  │     ├── Arcana Lore (`Draconic, Planar, Magic Theory`)├── Medicine (`First Aid, Surgery, Suture Mastery`)
  │     ├── Nature Lore (`Beasts, Flora, Weather Theory`) ├── Blacksmithing (`Forging Blades, Armor, Tools`)
  │     ├── History Lore (`Ancient Kingdoms, Relics`)     ├── Alchemy (`Brewing Potions, Poisons, Acids`)
  │     ├── Magic Traditions (`Arcana, Divine, Primal...`)└── Engineering (`Siege Engines, Architecture, Clockwork`)
  │
  └── 5. Social & Influence Domain (`WIS / CHA`)
        ├── Diplomacy (`Persuasion, Etiquette, Treaties`)├── Leadership (`Command, Morale Boost, Rallying`)
        ├── Intimidation (`Coercion, Interrogation, Fear`)├── Insight (`Empathy, Detecting Lies, Motives`)
        └── Deception (`Lying, Bluffing, Forgery, Gambling`)└── Performance (`Music, Oratory, Distraction`)

When a character levels up (DEC-035 Track 5), they invest Skill Allocations directly into Specific Individual Skills (e.g., reaching Expert (+1B, +1 Step, Floor 5) in Diplomacy, while leaving Deception at Untrained Floor 0!).

🚀 Where Shall We Direct Our Creative Focus Next?

With our 5 Universal Building Blocks (DEC-045), specific skill taxonomy (DEC-046), and 46 total logged decisions across 34 files completely aligned, where would you like to take our design work next?

Design the Core Feat Compendium (General, Combat, and Racial Feats): Convert 30 iconic D&D 3.5e feats (Power Attack, Cleave, Combat Reflexes, Dodge, Improved Initiative, Toughness, Weapon Focus) into clean 1-sentence mathless vector traits across our 6 tiers.
Build the Magic & Spellcasting Engine (Traditions & Vancian Grimoire): Define Vancian daily preparation across our 5 Traditions (Arcana, Divine, Primal, Shadow, Time), detail metamagic Focus costs, and convert 15 classic spells (Fireball, Cure Wounds, Invisibility, Haste, Hold Person).
Build a Complete Step-by-Step Character & Monster Walkthrough: Let's create a Tier 2 Veteran (Level 6) PC (say, a Human Greatsword Fighter or Elven Finesse Rogue) and a Tier 3 Master (Level 10) Boss monster (Ogre Mage or Lich King) from scratch to show the exact mathless formulas in action.

Which of these would you like to explore right now?
