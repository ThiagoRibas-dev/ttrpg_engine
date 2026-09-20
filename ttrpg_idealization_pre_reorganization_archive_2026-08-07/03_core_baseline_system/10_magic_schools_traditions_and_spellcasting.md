# Magic Schools, Traditions, and Spellcasting

**Status:** Canonical magic-framework owner.  
**Scope:** Schools, Traditions, Traits, Tradition access, shared Vancian preparation, spell acquisition, Spell Slot Progression, spellcasting-specific Essence expenditure, and the future Psychic/Psionic boundary.

## 1. Universal Spell Classification

Each spell uses three universal classifications:

```text
School
Tradition(s)
Trait(s)
```

A Spell Trait is a persistent Trait under the shared Tag / Trait taxonomy in `00_baseline_framework_glossary.md`. A spell or effect may also create Activities, Attacks, or effects carrying operational Tags.

### Schools

The eight traditional D&D-compatible Schools classify what technical operation a spell performs:

- Abjuration
- Conjuration
- Divination
- Enchantment
- Evocation
- Illusion
- Necromancy
- Transmutation

### Traditions

Traditions are modular magical access and specialization packages. A spell may belong to two or more Traditions. Classes and Prestige Classes grant access to Tradition Skills; they do not create separate class-owned spell lists.

The canonical Tradition catalogue contains 28 individual Tradition Skills:

```text
Arcane       Divine       Nature       Spirit
Darkness     Artifice     War          Life
Death        Void         Time         Space
Chaos        Law          Creation     Air
Earth        Fire         Water        Sound
Destruction  Light        Mind         Fate
Protection   Knowledge    Good         Evil
```

The complete Tradition scopes and Divine-Domain-to-Tradition access reference belong to:

```text
14_divine_domains_and_tradition_access.md
```

A Tradition is not automatically restricted to divine access: Classes, Prestige Classes, Ancestries, Feats, paths, items, and other content may grant it when explicitly stated. Alchemy is not a Tradition.

### Traits

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

The complete Skill and Domain framework, including Knowledge — Magic and Spellcrafting, is maintained in:

```text
09_domains_skills_activities_and_crafting.md
```

## 2. Fixed Tradition Spell Lists

Each Tradition has one fixed spell list regardless of the source that grants access.

Death accessed through a Cleric and Death accessed through a Wizard are the same Death Tradition and use the same Death spell list.

A spell may belong to multiple Traditions. A character learns a spell once. If at least one currently active Tradition grants access to that spell, the character may prepare it subject to the relevant Tradition Competency requirement.

## 3. Tradition Skills and Spell Access

Each Tradition is an individual Skill using the normal Competency Rank system. Classes and Prestige Classes grant access to one or more Tradition Skills and may protect or advance a primary Tradition through their level-by-level tables. A Class does not own one separate spell list: its available spell access is assembled from the individual Traditions it grants.

The canonical catalogue and Divine-Domain access procedure, including Cleric base access to Divine and each Divine Domain’s additional specified Tradition, are owned by:

```text
14_divine_domains_and_tradition_access.md
```

Tradition Competency determines:

- Whether the character can use a spell through that Tradition.
- The highest Spell Rank usable through that Tradition.
- The intrinsic scaling of the spell.
- The character’s casting quality through that Tradition.

Tradition Competency does not determine the character’s daily slot volume. That is determined by Spell Slot Progression.

The general Skill and Competency framework is owned by:

```text
09_domains_skills_activities_and_crafting.md
```

## 4. Universal Preparation and Acquisition

All ordinary spellcasters use one universal preparation system. There is no separate spontaneous-versus-prepared casting chassis.

Classes and Prestige Classes provide acquisition methods rather than class-owned spell lists. Examples may include:

- Learning a defined number of spells per class level.
- Research.
- Copying spellbooks or scrolls.
- Prayer.
- Revelation.
- Religious instruction.
- Mentors, institutions, relics, or special paths.

These methods add spells to one unified learned-spell collection. A multiclass character may use all applicable acquisition methods.

Exact learned-spell limits, preparation limits, duplicate acquisition, and downtime acquisition remain tracked in the Outstanding Definitions Index.

## 5. Shared Spell Slots

All ordinary spellcasters use one shared daily Vancian Spell Slot pool organized by Spell Circle. There are no separate Cleric, Wizard, or Tradition slot pools.

Spell Slot Progression and its level-by-level Class/Prestige Class advancement entries are defined in:

```text
06_leveling_and_tier_progression.md
```

### Spell Slot Advancement

An entry on a Class or Prestige Class table granting one advancement toward the character’s shared Spell Slot Progression.

### Spell Slot Progression Level

The character’s accumulated position on the Reference Good Slot Progression.

## 6. Spell Circle and Tradition Scaling

A character must satisfy both requirements to cast a prepared spell:

1. Sufficient Tradition Competency for the spell.
2. An available shared slot of the spell’s Spell Circle.

A character may know a spell above their current Tradition Competency, but cannot currently prepare or cast it through that Tradition. If the Tradition later advances, the learned spell may become usable.

Spells intrinsically scale with the relevant Tradition Competency. Casting a lower-Circle spell in a higher-Circle slot does not automatically improve it. Any heightened version must be explicitly defined in the spell entry.

## 7. Essence

Essence is the magical and supernatural exertion resource. Essence remains separate from Stamina.

This document owns whether and how spellcasting spends Essence, including 0th-Circle spells, cantrips, orisons, and metamagic. Each spell declares its own Action and Essence cost and may also declare a Stamina cost. Ordinary 0th-Circle spells, cantrips, and orisons generally cost 1 or 2 Essence, but their individual entries are authoritative. Metamagic declares its own cost. Spell-specific augmentation is defined by the relevant spell rather than by a universal augmentation procedure.

### Tagged Disruption

Ordinary spellcasting has no universal casting-stability expenditure or generic Concentration check. Damage alone does not automatically interrupt a spell.

An Activity Tag identifies spellcasting or another Activity that an effect may restrict or interrupt. A Spell, Condition, Feat, Class feature, item, monster ability, or other explicit effect must state its **Disrupt Permission** and the Tags it affects. Only such an explicit rule may interrupt a tagged Activity.

A spell that requires ongoing focus states its own Action, Tags, duration, interruption rule, and cost. There is no universal Emergency Casting procedure; Reaction casting, casting while restrained, component exceptions, and other exceptional timing or casting permissions belong to the specific effect granting them.

Spell Slots remain a shared daily resource. Recovery and preparation occur during and after a Long Rest. There is no default Essence-based Slot recovery and no default exceptional Slot restoration.

Non-spell supernatural abilities—such as Turn or Rebuke Undead, Smites, Devotion Feats, and Class, Ancestry, Tradition, or Equipment effects—declare their own Essence costs in their specific rules.

Essence capacity, recovery, and zero-resource state belong to `02_attributes_and_derived_statistics.md` and `../04_simulationist_subsystems/03_resources_conditions_and_wounds.md`.

## 8. Psychic/Psionic Boundary

Psychic/Psionic power is provisionally a separate Essence-based supernatural system rather than a Vancian Magic Mastery Tradition. Its disciplines, augmentation, strain, and interaction with ordinary spellcasting remain future work.

## 9. Canonical Spell Record

A spell record uses:

```text
Spell: Fireball
School: Evocation
Traditions: Arcane, Elemental, War
Traits: Fire, Area, Projectile
```

The same School may appear across different Traditions, and the same Tradition may use multiple Schools. This overlap supports modular specialization while preserving D&D-compatible classification.

## 10. Source Links

- Vocabulary and resolution: `00_baseline_framework_glossary.md`, `01_resolution_engine.md`
- Attributes and Essence capacity: `02_attributes_and_derived_statistics.md`
- Actor structure: `03_character_schema_and_actor_creation.md`
- Spell Slot Progression: `06_leveling_and_tier_progression.md`
- Statistical framework: `08_statistical_framework_and_check_modes.md`
- General Skills and Domains: `09_domains_skills_activities_and_crafting.md`
- Essence expenditure and recovery: `../04_simulationist_subsystems/03_resources_conditions_and_wounds.md`
- Equipment and magical items: `12_equipment_durability_and_economy.md`
- Divine Domains and canonical Tradition catalogue: `14_divine_domains_and_tradition_access.md`
