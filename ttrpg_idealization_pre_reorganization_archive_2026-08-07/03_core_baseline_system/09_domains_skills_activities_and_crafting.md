# Domains, Skills, Activities, and Crafting

**Status:** Canonical skill-framework owner.  
**Scope:** Domains, Skills, Lore, Knowledge, Craft, Activities, Procedures, Tools, and vehicle proficiencies.

## 1. Core Distinctions

- **Skill:** A transferable field of learned competence.
- **Specialty:** A narrower field beneath Craft, Lore, or another designated Skill family.
- **Activity:** An objective resolved using one or more appropriate Skills.
- **Activity Tag:** A Tag carried by an Activity. See `00_baseline_framework_glossary.md` for the shared Tag / Trait taxonomy.
- **Procedure:** The rules for resolving an Activity.
- **Maneuver:** A tactical action such as Trip, Disarm, Grapple, or Called Shot.
- **Tool/Equipment:** An object that enables, constrains, or changes an Activity without becoming a universal Skill.

Domains are canonical categories that organize Skills. Other mechanics, effects, and content may reference a Domain. Domains do not provide a second proficiency rank.

Universal check construction and resolution belong to `01_resolution_engine.md`.

### Baseline Activity Tags

- **Concentrate:** The Activity requires mental focus, careful magical shaping, or sustained attention.
- **Manipulate:** The Activity requires handling, drawing, using, activating, adjusting, or physically manipulating an object, component, weapon, shield, tool, or similar item.
- **Movement:** The Activity spends the creature’s movement allowance or changes its position.

An Activity may have multiple Tags. Its specific rule states which Tags it has. A Tag has no automatic effect unless another rule refers to it.


## 2. Authoritative Domains and Skills

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

Finesse, Throwable, Reach, Sweep, Forceful, Loading, and Fatal are weapon Traits, not Skills. Grappling, Wrestling, Trip, Disarm, Shove, Overextend, Bleed, Feint, and Called Shot are maneuvers or Activities using an appropriate Combat Mastery Skill.

### Domain II: Athletics, Movement, and Survival

- Athletics
- Acrobatics
- Swimming
- Riding
- Survival
- Beast Handling
- Sailing

Climbing, Sprinting, Forced Marching, and Jumping are Activities. Flying, burrowing, swimming, and similar capabilities are movement modes provided by Ancestry, Equipment, Feats, Spells, Skills, or creature design; they are not automatically universal Skills.

### Domain III: Subterfuge and Perception

- Moving Silently
- Hide
- Listen
- Spot
- Sleight of Hand
- Thievery

Spot and Listen remain separate sensory Skills. There is no universal Investigation Skill. Investigation is an Activity whose primary Skill depends on the method.

Thievery covers locks, mundane traps, delicate mechanisms, thieves’ tools, and technical criminal manipulation. It does not replace Athletics, Acrobatics, Martial Arts, Craft, or Knowledge when those are the actual approach.

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

Knowledge represents formal, systematic, technical, or academic understanding.

Languages and Scripts covers reading, writing, translation, alphabets, ancient scripts, ciphers, and linguistic structure. Craft — Scribing physically produces manuscripts, scrolls, seals, calligraphy, and documents.

Nobility, Courts, and Etiquette covers heraldry, titles, precedence, court protocol, introductions, dress codes, gift customs, diplomacy, and bureaucratic formalities.

Knowledge — Magic and Spellcrafting covers general magical theory and is separate from the ability to cast through a Magic Mastery Tradition.

### Domain V: Lore and Cultural Familiarity

- Lore — Player-Named Specialty

Lore represents focused familiarity acquired through experience, culture, travel, faction membership, apprenticeship, or repeated exposure.

Each Lore specialty has its own Competency Rank and is recorded as `Lore — X`. The GM adjudicates each specialty’s scope; a Lore specialty is less broad than a Knowledge Skill.

Background, Ancestry, Class, faction membership, and other content state their own Lore grants. The base framework does not assign them.

Knowledge asks, “How does this work?” Lore asks, “What do I know about this particular people, place, creature, group, tradition, or subject?”

### Domain VI: Social and Influence

- Leadership
- Diplomacy
- Intimidation
- Deception
- Insight
- Performance

Treaty negotiation, interrogation, rallying, impersonation, and social manipulation are Activities using these Skills plus relevant Knowledge, Lore, tools, and Class or Feat Permissions.

### Domain VII: Magic Mastery

Magic Mastery is a distinct Skill Domain separate from Knowledge — Magic and Spellcrafting. Its spellcasting procedure, Tradition Competency, and fixed Tradition spell-list framework are defined in:

```text
10_magic_schools_traditions_and_spellcasting.md
```

The canonical 28-Skill Tradition catalogue and the Divine-Domain access mapping are defined in:

```text
14_divine_domains_and_tradition_access.md
```

Tradition Skills determine the ability to perform or channel a magical Tradition. They do not automatically provide comprehensive academic knowledge of magic.

### Domain VIII: Craft and Production

Each Craft specialty has its own separate Competency Rank. Craft specialties are recorded as `Craft — X`.

Crafting uses the following defined specialties:

- Craft — Alchemy
- Craft — Armorsmithing
- Craft — Cooking
- Craft — Engineering
- Craft — Jewelcrafting
- Craft — Leatherworking
- Craft — Tailoring
- Craft — Weaponsmithing

Knowledge — Engineering can design or analyze a structure; Craft — Engineering physically constructs or repairs it. Knowledge — Alchemy and Pharmacology understands compounds; Craft — Alchemy produces them.

## 3. Vehicle Proficiencies

Vehicle operation is a family of proficiencies rather than one universal Skill:

- Mounts — Riding
- Wagons and Carriages — Driving
- Ships — Sailing
- Airships — Piloting
- Siege Engines — Siegecraft
- Other setting-specific vehicles

Vehicle operation may combine with Sailing, Cartography, Leadership, Survival, Craft, or Combat Mastery depending on the Activity.

## 4. Activities and Procedures

An Activity is an objective resolved with one or more appropriate Skills. Every defined Activity states its own primary Skill, relevant Attribute, Requirements, helpful sources, cost or time, resolution, success, failure, and Tags.

### Default Procedure

```text
Default:
  One primary Skill check.

Resolution:
  The Activity states a Difficulty Vector or opposed check.

Failure:
  The Activity states its own consequence.
  If no special consequence is stated, the Activity simply fails.
```

A second relevant Skill does not automatically add dice, successes, or a separate check. An Activity may explicitly permit a secondary Skill to provide an alternative approach, satisfy a Requirement or Permission, assist another Actor, or create a separate stage.

### Assistance

An Activity states whether assistance is possible and the Action or time it costs. An assistant must plausibly contribute with a relevant Skill, tool, Permission, or fictional position.

On a successful supporting check, the primary Actor gains 1 **Competence Boon** to the Activity. On failure, the assistant provides no benefit unless the Activity states another consequence. Multiple assistants do not automatically stack because typed Boon rules apply.

### Tools and Equipment

An Activity states the status of relevant tools:

| Tool status | Procedure |
|---|---|
| Required | The Activity cannot be attempted normally without the tool or an explicit substitute Permission |
| Improvised | The Activity may be attempted with 1 Circumstance Bane if its entry permits improvisation |
| Helpful | The Activity states a specific Permission or typed Boon |
| Specialized / masterwork | The specific tool grants an Enhancement Boon, Trait, Permission, reduced time, expanded output, or other stated effect |
| Consumed | The Activity states when and how much is consumed |

### Failure and Stages

There is no universal complication table. An Activity may state a simple failure, time cost, resource cost, exposure, escalation, or another specific consequence.

An Activity uses a staged procedure only when its entry explicitly states separate tasks. Multiple Skills alone do not create stages.

### Outcome Roll

An Activity, recipe, or project may explicitly call for an **Outcome Roll** when it needs degrees of output, quality, time, materials, or setback. Routine Activities do not use an Outcome Roll unless their entry says so.

```text
Die:
  1d10.

Outcome Target:
  Set by the relevant Competency Rank.
```

| Competency Rank | Outcome Target |
|---|---:|
| Untrained | 9 |
| Trained | 8 |
| Veteran | 7 |
| Master | 6 |
| Hero | 5 |
| Legend | 4 |

After a successful primary Activity check:

```text
Below Outcome Target:
  Standard success.

Meet or exceed Outcome Target:
  Enhanced success.

Natural 10:
  Exceptional success.
```

The Activity, recipe, or project states the applicable standard, enhanced, and exceptional outcomes.

After a failed primary check, the Activity states its own failure. It may explicitly call for an Outcome Roll to distinguish ordinary failure from a mitigated failure, delay, partial salvage, or other stated result. A natural 1 causes a severe setback only when the Activity explicitly says so.

### Activity Examples

- **Investigation:** Spot, Listen, Insight, Diplomacy, Intimidation, Survival, Thievery, Knowledge, or Lore.
- **Disguise and Impersonation:** Deception, Performance, Insight, Craft — Tailoring, Lore, and Languages and Scripts.
- **Forgery and Document Fraud:** Languages and Scripts, Craft — Scribing, Deception, Lore, Knowledge — Nobility, or Thievery.
- **Escape Artistry:** Athletics, Acrobatics, Thievery, Craft, or Martial Arts.
- **Lockpicking and Trap Disarming:** primarily Thievery, with Spot, Knowledge — Engineering, Craft — Engineering, or Lore as appropriate.
- **Shadowing and Tailgating:** Moving Silently, Hide, Spot, Survival, Deception, or local Lore.
- **Camp Defense and Fortifying:** Survival, Knowledge — Engineering, Craft — Engineering, Spot, or Leadership.
- **Beast Taming and Training:** Beast Handling, with Survival, Insight, Riding, or Leadership as support.

### Craft Activities

Craft uses three Activity families:

| Family | Procedure |
|---|---|
| Improvised Work | Only an Activity that explicitly permits improvised work may use it. The output is temporary, limited, or fiction-defined. |
| Standard Recipe or Item | A defined ordinary item, batch, meal, alchemical product, garment, repair, weapon, armor piece, or service uses one consequential check after its stated interval. |
| Project Downtime Activity | A large order, structure, masterwork work, unusual-material item, magical work, complex item, workshop improvement, research task, major repair, or other extended task uses stated downtime intervals and only its stated consequential check or checks. |

A recipe or project states:

```text
Name and Activity family.
Relevant Craft specialty and minimum Rank.
Plan, recipe, formula, blueprint, or required Permission.
Ordinary and exceptional materials.
Tools and workshop tier.
Downtime interval or project intervals.
Difficulty Vector and optional Outcome Roll.
Assistance.
Success, failure, output or batch, repair interaction, Tags,
and special requirements.
```

### Workshops

| Workshop Tier | Role |
|---|---|
| Improvised | Permits only Activities that explicitly allow improvised work; may impose a Circumstance Bane |
| Portable | Supports field work, Simple Repair, and portable recipes |
| Standard | Supports ordinary professional production or repair when required by a recipe |
| Specialized | Supports complex, high-Rank, masterwork, unusual-material, magical, or project-scale work when required |

A workshop normally acts as a Requirement or Permission. A specific workspace grants an Enhancement Boon, reduced time, expanded output, or another benefit only when its entry says so.

### Materials

Ordinary Craft materials use abstract units stated by the recipe or project, such as metal, timber, leather, cloth, reagents, or food supplies. Exceptional or magical work uses named materials, components, formulas, rituals, Traditions, or specialized workshop Requirements when stated.

### Craft Specialty Application

Each `Craft — X` specialty uses the same Activity framework.

```text
Create or produce:
  The item, recipe, project, or service states required Rank,
  plan, materials, tools, workshop, time, resolution, output,
  and failure consequences.

Repair:
  Use the Durability and repair procedure in
  `12_equipment_durability_and_economy.md`.
  The item recipe states its specific requirements and outcomes.
```

Knowledge — Engineering and Knowledge — Alchemy and Pharmacology may analyze, design, diagnose, or supply a Permission. Craft — Engineering and Craft — Alchemy construct, produce, refine, or repair as their respective Activities state.

### Lore and Knowledge Activities

A Recall Knowledge Activity uses the relevant `Knowledge — X` Skill to learn systematic facts, principles, capabilities, vulnerabilities, or procedures within its scope.

A Recall Lore Activity uses the relevant `Lore — X` specialty to learn specific cultural, historical, local, factional, experiential, or subject-specific facts within its scope.

The specific Activity determines what a success reveals in the current situation.

## 5. Source Links

- Vocabulary: `00_baseline_framework_glossary.md`
- Universal resolution: `01_resolution_engine.md`
- Actor structure: `03_character_schema_and_actor_creation.md`
- Progression: `06_leveling_and_tier_progression.md`
- Statistical model: `08_statistical_framework_and_check_modes.md`
- Magic Traditions: `10_magic_schools_traditions_and_spellcasting.md`
- Equipment: `12_equipment_durability_and_economy.md`
- Generic conditions and recovery: `../04_simulationist_subsystems/03_resources_conditions_and_wounds.md`

## 6. Current Scope Boundary

This document establishes the canonical framework and taxonomy. It does not finalize individual Classes, Feats, Ancestries, spells, equipment items, or the complete Craft, Lore, or vehicle catalogue.
