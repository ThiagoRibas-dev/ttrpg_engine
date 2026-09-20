# Universal Building Blocks & Master Skill System Architecture

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


## 2E. Canonical Magic Architecture (`DEC-050`)

Magic uses several independent classification axes. These axes must not be collapsed into one list.

### Schools

The eight traditional D&D-compatible schools remain the technical classifications of spells:

- Abjuration
- Conjuration
- Divination
- Enchantment
- Evocation
- Illusion
- Necromancy
- Transmutation

A school answers: **What technical operation does this spell perform?**

### Traditions

Traditions are modular magical access and specialization packages. A spell may belong to two or more traditions. Traditions determine who can learn, prepare, and specialize in a spell, while class, path, feat, or other access features determine which traditions a character can use.

Current Magic Mastery traditions:

#### Foundational Traditions

- Arcane / Thaumaturgic
- Divine / Theurgic
- Primal / Natural
- Spirit
- Shadow

#### Specialist Traditions

- Elemental
- Rune
- War
- Dream
- Life
- Death
- Eldritch / Void

#### Advanced or Restricted Traditions

- Time
- Space
- Chaos
- Order
- Creation

The slash terms are development terminology and may be resolved during later setting and spellcasting work. Arcane describes manipulation of raw magic through study, formula, intuition, or will. Divine describes power channeled through a deity, covenant, sacred authority, cosmic principle, or higher power. Celestial may exist as a Divine specialization rather than replacing Divine as the universal category. Natural World may exist as a Primal specialization rather than replacing Primal as the formal tradition.

### Spell Traits

Traits describe practical delivery and interaction, such as:

- Fire
- Healing
- Ritual
- Area
- Projectile
- Touch
- Sustained
- Summoning
- Mind-Affecting
- Language-Dependent
- Movement
- Reaction
- Corpse

### Alchemy

Alchemy is not a Magic Mastery tradition. It is governed by Knowledge — Alchemy and Pharmacology, Craft — Alchemy, tools, reagents, equipment, and downtime. Alchemy may imitate a spell or produce pseudo-magical effects without being a spell.

- Knowledge — Alchemy and Pharmacology identifies, analyzes, and designs compounds.
- Craft — Alchemy physically produces, refines, and prepares compounds.

### Psychic/Psionic Power

Psychic/Psionic power is provisionally a separate non-Vancian supernatural system rather than a Magic Mastery tradition. It may use Focus, disciplines, augmentations, mental exertion, and strain instead of daily Vancian preparation. This remains a future subsystem decision; full Vancian magic and full Psionic flexibility must not be granted together without meaningful opportunity cost.

### Canonical Multi-Axis Spell Record

A spell may be recorded as follows:

```text
Spell: Fireball
School: Evocation
Traditions: Arcane, Elemental, War
Traits: Fire, Area, Projectile
```

```text
Spell: Cure Wounds
School: Necromancy
Traditions: Divine, Life, Primal, Spirit
Traits: Healing, Touch
```

The same School may appear across different Traditions, and the same Tradition may use multiple Schools. This overlap is intentional and supports SotDL-style specialization without sacrificing D&D-compatible spell classification.


## 2F. Unified Spellcasting and Multiclassing (`DEC-051`)

The system uses one universal spellcasting framework. Classes do not own separate spell lists, casting profiles, or spell-slot pools.

### Traditions are individual skills

Each Tradition is an individual skill using the normal Competency Rank system. Classes and modular paths grant access to Tradition skills and may automatically protect or advance a primary Tradition. General investment may specialize secondary Traditions.

A character has one rank in each Tradition, regardless of how many classes or paths grant access to it.

### Fixed Tradition spell lists

Each Tradition has one fixed spell list regardless of source. Death accessed through a Cleric and Death accessed through a Wizard are the same Death Tradition and use the same Death spell list.

A spell may belong to multiple Traditions. A character learns a spell once; if at least one currently active Tradition grants access to that spell, the character may prepare it, subject to the Tradition Competency requirement.

### Shared spell slots

All spellcasters use one shared pool of daily Vancian spell slots organized by Spell Rank. There are no separate Cleric slots, Wizard slots, or Tradition slots.

The universal preparation rule is used by all characters. Classes and paths do not create spontaneous-versus-prepared casting distinctions. Instead, class and path features change how the character acquires spells and what additional casting options they possess.

Examples of acquisition features include:

- A Wizard learns a defined number of spells per Wizard level.
- A Wizard may research, copy, transcribe, or learn spells from scrolls and other spellbooks.
- A Cleric learns a defined number of spells per Cleric level.
- A Cleric may acquire spells through prayer, revelation, religious instruction, or divine source access.
- A Prestige Path may grant specific spells, expand a Tradition list, or provide a special method of acquisition.

These acquisition methods add spells to one unified learned-spell collection. A multiclass character may use all applicable acquisition methods, creating a trade-off between broader class mechanics and deeper Tradition investment.

### Tradition Rank and spell rank

Tradition Competency replaces a separate per-Tradition caster-level statistic. Tradition Rank determines the highest Spell Rank the character can use through that Tradition and determines the spell's intrinsic scaling.

| Tradition Rank | Highest usable Spell Rank |
|---|---|
| Untrained | None |
| Trained | Novice |
| Expert | Expert |
| Master | Master |
| Legendary | Heroic/Legendary, subject to the final high-tier spell framework |

The character must satisfy both requirements:

1. Have sufficient Tradition Competency for the spell.
2. Spend an available shared slot of the spell's Spell Rank.

A character may know a spell above their current Tradition Rank, but cannot currently prepare or cast it through that Tradition. If the Tradition later advances, the already-learned spell becomes usable.

### D&D 3.5e-style intrinsic scaling

Spells automatically improve according to the caster's relevant Tradition Competency. Casting a lower-rank spell in a higher-rank slot does not automatically improve it.

```text
Death: Trained  → use the Trained version of a Death spell
Death: Expert   → use the Expert version of that Death spell
Death: Master   → use the Master version of that Death spell
```

Spell Rank determines the slot consumed. Tradition Competency determines the spell's intrinsic scale and casting quality.

### Shared Traditions between classes

If both Cleric and Wizard grant Death, the character has one Death skill and one Death spell list. Both classes may contribute access and acquisition options; neither creates a separate Death version.

```text
Cleric/Wizard:
  Death: Expert
  Death spell list: one shared list
  Spell slots: one shared pool
  Spell acquisition: Cleric methods plus Wizard methods
```

The character does not track Death — Cleric, Death — Wizard, separate caster levels, or separate slot pools.

### Essence

The former Focus resource is renamed **Essence**. Essence remains separate from Stamina.

Essence powers:

- 0th-rank spells, cantrips, and orisons.
- Metamagic feats.
- Casting stability under distraction, injury, adjacency, or other interference.
- Emergency casting.
- Supernatural class features such as Turn or Rebuke Undead, Smites, and certain Devotion Feats.

### Psychic/Psionic power

Psychic/Psionic power is provisionally a separate Essence-based supernatural system rather than a Vancian Tradition. Its disciplines, augmentation rules, strain, and interaction with ordinary spellcasting remain future work.


## 2G. Spellcasting Progression and Shared Slot Table (`DEC-052`)

The system uses one shared daily Spell Slot pool. A character's **Spellcasting Progression Level** determines their position on the shared slot table. This value is distinct from Character Level, High Fantasy Tier, Tradition Competency, Spell Circle, and Essence.

### Spellcasting Progression Level

A full caster whose spellcasting advances at every class level has Spellcasting Progression Level equal to Character Level. A multiclass character may have a lower Progression Level than Character Level.

The baseline Good/Reference Spellcasting Progression uses the modified D&D 3.5e-style table below. “Good,” “Mediocre,” and “Bad” are design guidelines for comparing class advancement cadences; they are not separate player-facing resources or tracks.

| Tier | Progression Level | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Trained | 1 | 4 | — | — | — | — | — | — | — | — |
| Trained | 2 | 4 | — | — | — | — | — | — | — | — |
| Trained | 3 | 4 | 2 | — | — | — | — | — | — | — |
| Trained | 4 | 4 | 2 | — | — | — | — | — | — | — |
| Veteran | 5 | 5 | 2 | 2 | — | — | — | — | — | — |
| Veteran | 6 | 5 | 3 | 2 | — | — | — | — | — | — |
| Veteran | 7 | 5 | 3 | 2 | 2 | — | — | — | — | — |
| Veteran | 8 | 5 | 3 | 3 | 2 | — | — | — | — | — |
| Master | 9 | 5 | 4 | 3 | 2 | 2 | — | — | — | — |
| Master | 10 | 5 | 4 | 3 | 3 | 2 | — | — | — | — |
| Master | 11 | 5 | 4 | 4 | 3 | 2 | 2 | — | — | — |
| Master | 12 | 5 | 4 | 4 | 3 | 3 | 2 | — | — | — |
| Hero | 13 | 5 | 5 | 4 | 4 | 3 | 2 | 2 | — | — |
| Hero | 14 | 5 | 5 | 4 | 4 | 3 | 3 | 2 | — | — |
| Hero | 15 | 5 | 5 | 5 | 4 | 4 | 3 | 2 | 2 | — |
| Hero | 16 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 2 | — |
| Legend | 17 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 2 | 2 |
| Legend | 18 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 2 |
| Legend | 19 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 |
| Legend | 20 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 |

### Level-by-level class advancement

Every Base Class and Prestige Class includes a **Spellcasting Advancement** column in its level-by-level table. The table explicitly marks each level that grants one advancement. Class descriptions may summarize the cadence, but the level-by-level table is authoritative.

Examples:

- Wizard: `+1` advancement at every Wizard level.
- Paladin: `+1` advancement at selected levels, such as levels 2, 4, 6, 8, and 10.
- Eldritch Knight: `+1` advancement at selected levels, such as levels 3, 6, and 9.
- Fighter: no Spellcasting Advancement unless a specific class feature grants one.

Prestige Classes use exactly the same procedure as Base Classes. Their entry requirements, not a different multiclassing system, distinguish them.

### Multiclassing

Add all completed Spellcasting Advancements from all Base Classes and Prestige Classes. The total is the character’s Spellcasting Progression Level, and the character uses that row of the shared slot table.

```text
Wizard 4 / Fighter 4:
  4 + 0 = Spellcasting Progression Level 4

Wizard 4 / Paladin 4:
  4 + 2 = Spellcasting Progression Level 6

Wizard 4 / Eldritch Knight 3:
  4 + 1 = Spellcasting Progression Level 5

Wizard 4 / Cleric 4:
  4 + 4 = Spellcasting Progression Level 8
```

The arithmetic occurs during advancement or character creation, not during ordinary action resolution. During play, the sheet simply records the final Progression Level and shared slot quantities.

### Tradition Competency does not gate slot access

Spellcasting Progression determines daily slot volume. Tradition Competency determines spell access, casting quality, and intrinsic spell scaling. A character may possess a high Spellcasting Progression Level while having only shallow investment in a particular Tradition.

Using a higher-Circle slot does not automatically improve a lower-Circle spell. A spell improves only when its entry explicitly provides a Heightened version. Its normal intrinsic scaling comes from the relevant Tradition Competency.

### Mythic advancement

Mythic advancement does not automatically add new ordinary Spell Slots beyond the Level 20 table. It grants access to Epic Traditions and Epic Spells that use the existing shared slot framework, potentially alongside Essence, rituals, rare components, or other in-world requirements.


### Derived cadence tables

The Reference Good Slot Progression is the only universal slot table. The Mediocre and Bad examples are derived views, not separate player-facing tracks:

- **Full cadence:** advance to the next Reference row every class level.
- **Mediocre cadence:** advance to the next Reference row every two class levels.
- **Bad cadence:** advance to the next Reference row every four class levels.

The derived CSV catalogue records these views by **Character Level**. The Reference table is indexed by **Spell Slot Progression Level**; the derived views show which Reference row each class level currently uses.

The design principle is that every Reference row should differ meaningfully from the preceding row, so every Spell Slot Advancement produces a visible change in slot volume or Spell Circle access.

## 3. The 5 Competency Ranks (`Investment-Driven Step, Volume & Floor`)

When a character levels up and allocates their **Class Skill Allocations (`DEC-035 Track 5`)**, they invest points directly into **Specific Individual Skills** (`e.g., investing into *Diplomacy* to reach `Expert (+1B, +1 Step, Floor 5)`, while leaving *Deception* under the same Social umbrella at `Untrained (Floor 0)`!).

Advancing a specific skill rank transforms your check pool across all three check variables (`Die Size X, Pool Volume N, and Competency Floor F`):

| Competency Rank (`Investment Level`) | Check Pool Modification (`Die Size X & Pool Volume N`) | Competency Floor (`F`) | Multi-Success Maneuver Permissions (`DEC-043`) | What This Represents Physically & Conceptually |
| :--- | :--- | :---: | :--- | :--- |
| **0. Untrained** (`Zero Investment`) | **Base Pool `2dX keep highest`**<br>*(Attribute Die only — $+0B, +0 Steps*)* | **Floor = 0**<br>*(Pure random roll)* | Can execute `1 Success` Standard Hits (`Damage vs ABS`). *No multi-success maneuver triggers (`Prone, Disarm, Wounds`).* | Raw, unassisted civilian capability without technical technique (`11.1% whiff rate on 2d6 vs routine DC 3`). |
| **1. Trained** (`Basic Focus — 1 Allocation`) | **Pool Volume `3dX` (`+1B`)**<br>*(Rolls 3 dice of base Attribute size)* | **Floor = 3**<br>*(Guaranteed min face 3)* | **Immune to failing `DC 3 Routine` checks (`100%`).** Can trigger standard default maneuvers on `2+ Successes` (`Trip, Disarm, Shove`). | Professional competence (`e.g., proper edge alignment, basic diplomatic etiquette, or silent footwork`). |
| **2. Expert** (`Specialist — 2 Allocations`) | **Pool Volume `3dX` (`+1B`) + `1 Die Step-Up` (`X+1`)**<br>*(e.g., Attribute d8 $\to$ rolls `3d10`)* | **Floor = 5**<br>*(Guaranteed min face 5)* | **Immune to failing `DC 5 Challenging` checks (`100%`).** Can execute `Called Shot Anatomical Wounds` (`3 Successes`). | Dedicated specialization (`e.g., veteran regional champion, master surgeon, or elite spy`). Surpasses basic physical limits via technique! |
| **3. Master** (`Grandmaster — 3 Allocations`) | **Pool Volume `4dX` (`+2B`) + `2 Die Step-Ups` (`X+2`)**<br>*(e.g., Attribute d8 $\to$ rolls `4d12`)* | **Floor = 7**<br>*(Guaranteed min face 7)* | **Immune to failing `DC 7 Formidable` checks (`100%`).** Unlocks `Whirlwind Strike [3A]` and `Shatter Absorption` multi-beats. | Realm-renowned grandmastery. The character's technique is so precise they literally never miss formidable obstacles (`Floor 7`). |
| **4. Legendary** (`Mythic Apex — 4 Allocations`)| **Pool Volume `5dX` (`+3B`) + `3 Die Step-Ups` (`X+3`)**<br>*(e.g., Attribute d8 $\to$ rolls `5d12 over-cap`)* | **Floor = 9**<br>*(Guaranteed min face 9)* | **Immune to failing `DC 9 Heroic` checks (`100%`).** All standard hits in this specific skill automatically gain `+1 Multi-Success beat` for free! | Mythic mortal apex (`DEC-014`). Multiversal legends whose skills reshape physical, social, or arcane reality across the planes. |

---

## 4. Concrete Examples (`Specific Skill Checks in Action`)

To see how our 5-Block high fantasy setup (`Race + Background + Class + Skills + Feats`) and specific skill competency ranks operate without arithmetic, look at these four real-time checks across our domains:

### 4.1 Subterfuge Check (`Level 6 Expert Rogue vs. DC 7 Formidable Mechanical Lock`)
- **Character Setup:** Level 6 Elven Rogue (`AGI d10, DEX d10, INT d8`). Background: `Street Urchin (`Primary DEX d10`)`. Class: `Rogue (`Okay BAB, Good Skill Allocations — DEC-035`)`.
- **Specific Skill Investment:** Invested 2 skill allocations into **`Lockpicking`** $\to$ **`Expert Rank (+1B, +1 Die Step-Up, Floor 5)`**. *(Note: She left `Trap Disarming` at `Trained Floor 3` and `Sailing` at `Untrained Floor 0`!)*
- **Rolling the Check (`Zero Math`):** Her base `DEX` is `d10`. Because she is an `Expert` in *Lockpicking*, her die size steps up (`d10` $\to$ `d12`), and she gains `+1B` volume (`2d` $\to$ `3d`). She rolls **`3d12 keep highest (Floor 5)` vs `DC 7`**.
- **Outcome:** She rolls `4, 8, 11`. Highest face is `11` (`11 >= DC 7 -> Success!`). Furthermore, because `8` also beats `7`, she achieves **2 Successes (`Multi-Beat Complex Check — DEC-036`)**, picking the complex lock in half the time without making a sound!

### 4.2 Social Check (`Level 10 Master Paladin vs. Hostile King's Willpower Defense Pool`)
- **Character Setup:** Level 10 Human Paladin (`STR d10, CON d10, WIS d8, CHA d10`). Background: `High Noble (`Primary CHA d10, stepped up to d12 at Lvl 9`)`. Class: `Paladin (`Full Martial, Good Fort/Will`)`.
- **Specific Skill Investment:** Invested 3 allocations into **`Diplomacy`** $\to$ **`Master Rank (+2B, +2 Die Step-Ups, Floor 7)`**.
- **Rolling the Check (`Zero Math`):** His base `CHA` is `d12`. Because he is a `Master` in *Diplomacy*, his die steps twice (`d12` $\to$ `over-cap d12`), and he gains `+2B` volume (`2d` $\to$ `4d`). He rolls **`4d12 keep highest (Floor 7)`** directly against the King's opposed **Willpower Pool (`1dWIS + 1dCHA keep highest -> 2d10`)**.
- **Outcome:** The Paladin rolls `6, 9, 12, 14`. Because his Competency Floor is `7`, his `6` becomes `7`. The King rolls `4, 8`. The Paladin's `14` crushes the King's `8` (`Success!`). Because `12` and `9` *also* beat the King's `8`, the Paladin scores **3 Successes (`Overwhelming Social Dominance`)**, forging an immediate binding treaty and rallying the King's army to his cause right at the table!
