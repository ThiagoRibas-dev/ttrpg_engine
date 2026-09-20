# Domains, Skills, Activities, and Crafting

To ensure every choice on a character sheet (`and universal monster stat block — DEC-011`) models a distinct aspect of reality without mechanical overlap, we must clearly define what each building block represents conceptually and mechanically. Furthermore, we must establish our definitive **Master Skill Taxonomy (`Specific Skills grouped under Domain Umbrellas — DEC-030, revised DEC-049`)** across our **Competency Ranks (`DEC-020`)**.

This document evaluates three building block arrangements, establishes our 5-Block High Fantasy baseline, and lays out the complete skill system.

---

## 1. Candidate Building Block Arrangements (`Evaluating the Architecture`)

When structuring what defines an actor (`PC, NPC, or Monster`), we evaluated three candidate arrangements:

### 1.1 Arrangement 1: The Classic 4-Block (`Race + Class + Skills + Feats`)
- **What each block models:**
  - **1. Race / Ancestry (`Biological Reality`):** Size, Speed, Darkvision, natural armor Absorption steps (`ABS`), biological claws/wings.
  - **2. Class Archetype (`Professional Vocation`):** 20-level advancement tracks (`Vitality, Check Pool/Floor, Paired Saves, Vancian/Focus, Skill Allocations — DEC-035`).
  - **3. Skills (`Learned Proficiencies`):** Specific individual capabilities (`Stealth, Lockpicking, Arcana, Diplomacy`) advanced via skill allocations.
  - **4. Feats (`Modular Techniques`):** Discrete rules overrides, action economy permissions (`[1A], [2A], [1R]`), and specialized maneuvers.
- **Pros:** 100% familiar 3.5e/PF2e structural mapping.
- **Cons:** Leaves where a character's automatic primary attribute step growth (`DEC-039`) comes from slightly ambiguous (`does it belong to Race or Class?`).

### 1.2 Arrangement 2: The 5-Block High Fantasy Division (`Race + Background + Class + Skills + Feats — Recommended Baseline`)
- **What each block models:**
  - **1. Race / Ancestry (`Biological Reality`):** Size, Speed, reach tiers, biological hide toughness (`ABS d4-d10`), and genetic immunities.
  - **2. Background / Origin (`Innate Exceptional Focus & Upbringing — DEC-039`):** What you dedicated your life to before adventuring (`Blacksmith, Noble, Soldier, Scholar`). **Designates your ONE Primary Attribute (`starting at d8, stepping up automatically at Lvl 5, 9, 15, 20`)**, and awards 1 specific starting Skill (`e.g., Crafting, Diplomacy, Longswords`) at `Trained (`Floor 3`)` for free!
  - **3. Class / Archetype (`Professional Adventuring Vocation`):** Your 20-level good/okay/bad advancement tracks (`Vitality, Check Pool/Floor, Saves, Vancian/Focus, Skill Allocations — DEC-035`).
  - **4. Skills (`Action Mastery Domain Proficiencies`):** Specific capabilities (`Stealth, Arcana, Athletics`) purchased via your class skill allocations across all 20 levels.
  - **5. Feats (`Modular Vector Techniques`):** Action economy permissions (`[1A], [2A], [1R]`) and specialized combat/magical maneuvers.
- **Pros:** **Absolute conceptual clarity.** Demystifies your primary attribute scaling (`DEC-039`) right into a rich narrative origin (`Background`), while keeping Race strictly biological and Class strictly vocational (`no skill tax — DEC-041`).
- **Cons:** Adds 1 additional selection block at Level 1 (`5 blocks instead of 4`). However, because Background runs on automatic pilot after Level 1 (`stepping up at Lvl 5, 9, 15, 20`), it simplifies campaign math!

### 1.3 Arrangement 3: The SotDL Modular Path Division (`Race + Paths [Novice/Expert/Master/Legend] + Skills + Feats`)
- **Structure:** Replaces the single 20-level linear "Class" block with **Four Layered Paths across our 6 Tiers (`Novice Path at Lvl 1, Expert Path at Lvl 5, Master Path at Lvl 9, Legend Path at Lvl 17 — DEC-013 & DEC-027`)**! Each path (`say, Novice Warrior + Expert Berserker + Master Blade Dancer`) awards specific Vitality increments, skill allocations, and path feats across its 4-level band.
- **Pros:** Unmatched option-density and multiclassing freedom without dead levels or prerequisite traps.
- **Cons:** Can feel more modular/SotDL-centric for traditional 3.5e purists who prefer a single 1-to-20 class identity (`though 3.5e prestige classes operated on a very similar modular principle`).

---

## 2. Historical Skill Taxonomy (`Superseded 5-Umbrella Matrix`)

With **Arrangement 2 (`5-Block High Fantasy Division`)** locked in (`DEC-045`), skills are not broad abstract buckets (`where "Social" makes you equally good at lying and diplomacy — DEC-030`). Instead, our 5 Action Mastery Domains act as **Categorical Umbrellas** organizing **Specific Individual Skills**:

```
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
```


## 2A. Revised Domain-and-Activity Architecture (`DEC-049`)

The earlier five-umbrella matrix is superseded by a more precise architecture. **Domains are game entities**, not merely headings on a list. Individual skills determine ordinary check competence; domains may later interact directly with classes, paths, feats, equipment, prerequisites, and domain-specific actions.

A domain does **not** currently grant a second proficiency rank. Avoiding separate Domain Ranks preserves the strict separation between character level, competency rank, and class/path progression.

### Core distinction

- **Skill:** a transferable field of learned competence.
- **Specialty:** a narrower field beneath Craft, Lore, or another designated skill family.
- **Activity:** an objective resolved using one or more appropriate skills.
- **Procedure:** the specific rules for resolving an activity.
- **Maneuver:** a tactical action such as Trip, Disarm, Grapple, or Called Shot.
- **Tool/Equipment:** an object that enables, constrains, or changes an activity without becoming a universal skill.

Investigation, Disguise, Impersonation, Forgery, Lockpicking, Trap Disarming, Escape Artistry, Shadowing, Tailgating, Treaty Negotiation, Interrogation, and Camp Fortification are activities or procedures, not universal skills.

## 2B. Authoritative Domain List

### Domain I: Combat Mastery

- Heavy Blades
- Light Blades
- Polearms and Spears
- Axes and Picks
- Hammers, Maces, and Flails
- Archery
- Exotic Weapons
- Shield Defense
- Martial Arts

Weapon properties such as **Finesse**, **Throwable**, **Reach**, **Sweep**, **Forceful**, **Loading**, and **Fatal** are weapon tags, not skills. Grappling, Wrestling, Trip, Disarm, Shove, Overextend, Bleed, Feint, and Called Shot are maneuvers or combat activities using an appropriate Combat Mastery skill.

### Domain II: Athletics, Movement, and Survival

- Athletics
- Acrobatics
- Swimming
- Riding
- Survival
- Beast Handling
- Sailing

Climbing, Sprinting, Forced Marching, and Jumping are activities. Athletics handles force, endurance, and power-based movement; Acrobatics handles balance, tumbling, precision movement, controlled falls, and acrobatic escapes. Jumping is not an independent skill.

Climbing and Sprinting are movement activities, while flying, burrowing, swimming, and similar capabilities are movement modes provided by ancestry, equipment, feats, spells, or creature design. They are not automatically skills.

### Domain III: Subterfuge and Perception

- Moving Silently
- Hide
- Listen
- Spot
- Sleight of Hand
- Thievery

Spot and Listen are deliberately separate sensory skills. There is no universal Investigation skill. Investigation is an activity whose skill depends on the method: Spot for visual clues, Listen for sounds, Insight for motives, Diplomacy or Intimidation for questioning, Survival for a wilderness scene, Thievery for mechanisms, and Knowledge or Lore for interpretation.

Thievery covers locks, mundane traps, delicate mechanisms, thieves' tools, and technical criminal manipulation. It does not replace Athletics, Acrobatics, Martial Arts, Craft, or Knowledge when those are the actual approach to an escape or device.

### Domain IV: Knowledge and Technical Practice

- Knowledge — Alchemy and Pharmacology
- Knowledge — Languages and Scripts
- Knowledge — Anatomy and Healing
- Knowledge — Engineering
- Knowledge — Cartography
- Knowledge — Magic and Spellcrafting
- Knowledge — Nature and Ecology
- Knowledge — Religions and Rites
- Knowledge — Nobility, Courts, and Etiquette

Knowledge is formal, systematic, technical, or academic understanding.

**Languages and Scripts** covers reading, writing, translation, alphabets, ancient scripts, ciphers, and linguistic structure. **Craft — Scribing** covers physically producing manuscripts, scrolls, seals, calligraphy, and convincing documents.

**Nobility, Courts, and Etiquette** covers heraldry, titles, precedence, court protocol, formal introductions, dress codes, gift customs, diplomatic etiquette, and bureaucratic or hierarchical formalities. It supports—but does not replace—Diplomacy, Deception, Insight, or Leadership.

**Magic and Spellcrafting** is general magical knowledge: magical theory, spell structure, magical effects, enchantments, rituals, and spell design. It is intentionally separate from the ability to cast spells.

### Domain V: Lore and Cultural Familiarity

- Lore — Player-Named Specialty

Lore is open-ended, focused familiarity acquired through experience, culture, travel, faction membership, apprenticeship, or repeated exposure. Examples include Lore — Undead, Lore — Imperial Law, Lore — Goblin Tribes, Lore — Court Etiquette, Lore — Ancient Ruins, and Lore — Maritime Trade.

Knowledge asks, **“How does this work?”** Lore asks, **“What do I know about this particular people, place, creature, group, tradition, or subject?”**

### Domain VI: Social and Influence

- Leadership
- Diplomacy
- Intimidation
- Deception
- Insight
- Performance

Treaty and legal negotiation, interrogation, rallying, impersonation, and social manipulation are activities using these skills plus relevant Knowledge, Lore, tools, and class or feat abilities.

### Domain VII: Magic Mastery (`Provisional Until Spellcasting Revision`)

Magic proficiency is a distinct skill domain, separate from Knowledge — Magic and Spellcrafting. Provisional tradition skills include:

- Arcana
- Divine
- Primal
- Shadow
- Time
- Additional traditions established by the spellcasting engine

These skills determine the ability to perform or channel a magical tradition. They do not automatically provide comprehensive academic knowledge of magic.

### Domain VIII: Craft and Production

Crafting uses defined specialties. Current provisional specialties include:

- Craft — Blacksmithing
- Craft — Weaponsmithing
- Craft — Armorsmithing
- Craft — Bowyer and Fletching
- Craft — Leatherworking
- Craft — Tailoring
- Craft — Carpentry
- Craft — Masonry
- Craft — Shipwright
- Craft — Engineering
- Craft — Alchemy
- Craft — Scribing
- Craft — Forgery Production
- Craft — Disguise Construction
- Craft — Trapmaking
- Craft — Poisoncraft
- Craft — Jewelry and Gemcutting
- Craft — Glassworking
- Craft — Cooking and Brewing
- Craft — Herbalism
- Craft — Clockwork and Mechanisms
- Craft — Siegecraft

Craft produces, repairs, modifies, or evaluates physical objects. Knowledge — Engineering can design or analyze a structure; Craft — Engineering physically constructs or repairs it. Knowledge — Alchemy and Pharmacology understands compounds; Craft — Alchemy produces them.

## 2C. Vehicle Proficiencies

Vehicle operation is a family of proficiencies rather than one universal skill:

- Mounts — Riding
- Wagons and Carriages — Driving
- Ships — Sailing
- Airships — Piloting
- Siege Engines — Siegecraft
- Other setting-specific vehicles

Vehicle operation may combine with other skills: Sailing plus Cartography to navigate, Sailing plus Leadership to command a crew, Craft — Shipwright to repair a vessel, or a Combat Mastery skill to fight from one.

## 2D. Activity Examples

- **Investigation:** Spot, Listen, Insight, Diplomacy, Intimidation, Survival, Thievery, Knowledge, or Lore depending on method.
- **Disguise and Impersonation:** Deception, Performance, Insight, Craft — Disguise Construction, Lore, and Languages and Scripts.
- **Forgery and Document Fraud:** Languages and Scripts, Craft — Scribing, Deception, Lore — Law, Knowledge — Nobility, or Thievery.
- **Escape Artistry:** Athletics, Acrobatics, Thievery, Craft, or Martial Arts.
- **Lockpicking and Trap Disarming:** primarily Thievery, with Spot, Knowledge — Engineering, Craft, or Lore as appropriate.
- **Shadowing and Tailgating:** Moving Silently, Hide, Spot, Survival, Deception, or local Lore.
- **Camp Defense and Fortifying:** Survival, Knowledge — Engineering, Craft, Spot, or Leadership.
- **Beast Taming and Training:** Beast Handling, with Survival, Insight, Riding, or Leadership as support.

Normally, one skill is primary. Additional skills create separate stages, establish fictional permissions, provide assistance, or change consequences; they do not automatically create linear numerical modifiers.

---


## Magic Cross-Reference

The canonical Magic Schools, Traditions, Traits, Spell Slot Progression, and spellcasting framework are maintained in `10_magic_schools_traditions_and_spellcasting.md`. Magic Traditions remain individual Skills within the Domains architecture.
