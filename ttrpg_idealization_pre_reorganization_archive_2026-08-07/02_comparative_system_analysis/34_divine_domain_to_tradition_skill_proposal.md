# Divine Domains to Spell Tradition Skills — Proposal

**Status:** Superseded proposal / design history.  
**Superseded by:** DEC-098 and `03_core_baseline_system/14_divine_domains_and_tradition_access.md`.
**Revision:** 2 — final proposal state before canonization.
**Input:** `cleric_divine_domain_reference.txt`, explicitly authorized for this exercise.  
**Purpose:** Test how D&D 3.5e and Pathfinder-style Divine Domains can grant modular Spell Tradition Skill access without creating one Tradition Skill per Domain.

## 1. Design Rule Being Tested

The established architecture is:

```text
Cleric base:
  Grants access to Divine.

Each granted Divine Domain:
  Grants access to one specified additional Spell Tradition Skill.
  May also grant non-magical Skills, Permissions, Feats, Devotions,
  spell-acquisition rules, or other Features.
```

A Domain is **not** a separate universal spell-record axis. A spell still has one or more Traditions, plus School and Traits.

### Access is not Rank

A Domain opens an eligible Tradition Skill at Untrained unless the Domain or another explicit rule grants a Rank. The character must use protected progression, a Magic Mastery-only Investment, or another explicit grant to improve that Tradition.

### Duplicate access

If two Domains grant the same Tradition, the character gains no duplicate Skill or free Rank. The second Domain still matters because it can grant its own Domain Feature, spell-acquisition permission, or other explicit benefit.

This is important for combinations such as:

```text
War + Strength → War
Healing + Purification → Life
Law + Rune → Order
Sun + Glory → Light
```

## 2. Proposed Catalogue Shape

The current 17-Tradition list is a good starting skeleton, but a Divine-Domain conversion benefits from a few additional broad magical jobs. This revised proposal uses **28 Skills**, including Divine itself. It keeps the four-element split, Sound, and cardinal-alignment Traditions while consolidating several overlapping magical jobs.

### Retained or renamed current Traditions

| Proposed Tradition Skill | Relationship to current catalogue | Core magical job |
|---|---|---|
| Arcane | Retained | Raw formal magic, force, magical manipulation, and draconic arcana. |
| Divine | Retained | Baseline theurgic prayer, sacred rites, general clerical magic. |
| Nature | Rename / consolidation of Primal + Beast | Natural world, plants, animals, seasons, growth, wilderness, and creature affinity. |
| Spirit | Retained | Souls, ancestors, mediums, sacred messengers, incorporeal forces. |
| Darkness | Rename of Shadow | Darkness, deception, concealment, loss, secret paths, and night magic. |
| War | Retained | Battle blessings, tactics, valor, disciplined violence. |
| Life | Retained | Healing, restoration, vitality, renewal. |
| Death | Retained | Death, undeath, repose, mortality, funerary powers. |
| Void | Rename of Eldritch / Void | Cosmic absence, alien power, isolation, dark tapestry. |
| Time | Retained | Time, destiny-adjacent temporal effects, foretelling through time. |
| Space | Retained | Portals, distance, travel, locations, dimensional movement. |
| Chaos | Retained | Entropy, mutation, riot, wildness, liberation. |
| Law | Rename of Order | Law, judgment, hierarchy, oaths, binding rule. |
| Creation | Retained | Making, shaping, summoning matter, generative magic. |

### Proposed additions

| Proposed Tradition Skill | Why it deserves a separate Skill | Domain families it unifies |
|---|---|---|
| Air | Air, wind, sky, lightning, storms, flight, and atmospheric force have a distinct magical job. | Air, Sky, Wind, Cloud, Lightning, Storm, Weather. |
| Earth | Stone, metal, caves, sand, petrification, and seismic magic form a coherent body. | Earth, Caves, Metal, Sand, Petrification. |
| Fire | Flame, ash, smoke, arson, heat, and combustion need not be coupled to every other element. | Fire, Arson, Ash, Smoke. |
| Water | Water, ice, oceans, rivers, cold, and fluid currents have a distinct exploration and control identity. | Water, Cold, Ocean, Seafolk, Rivers, Flowing, Ice, Winter. |
| Sound | Resonance, sonic force, silence, music, voice, language-as-power, and vibration are not merely Air. | Future Sound / music / silence sources; selected Herald, Language, and Storm content when appropriate. |
| Artifice | Constructs, craft, mechanisms, industry, tools, runes, wards, and magical inscriptions share a created-object / encoded-pattern identity. | Artifice, City, Construct, Industry, Toil, Trap, Rune, Wards, Language. |
| Destruction | Destructive sacred power is broader than War and distinct from elemental damage. | Destruction, Catastrophe, Fury, Wrath, Rage, Erosion, Ruins. |
| Light | Sun, revelation, sacred radiance, glory, and anti-undead power are a coherent spell identity. | Sun, Celestial, Glory, Good, Purification, Herald. |
| Mind | Cognition, compulsion, emotion, madness, dream, thought, memory, and inner vision belong to one broad consciousness tradition. | Charm, Mind, Passion, Dream, Madness, Thought, Captivation, Domination, Nightmare, Love, Lust, Joy. |
| Fate | Luck, destiny, oracle, curse, and prophecy work as one intervention / foresight package. | Luck, Destiny, Fate, Oracle, Fortune, Curse. |
| Protection | Wards against harm, sanctuaries, resistance, and fortification are a large distinct spell family. | Protection, Defense, Fortifications, Endurance, Purity. |
| Knowledge | Revelation, memory, education, divination, and secret learning are broader than a mundane Knowledge Skill. | Knowledge, Inquisition, Memory, Education, Revelation. |
| Good | Mercy, redemption, friendship, benevolent outsiders, and altruistic sacred power are distinct from radiance alone. | Good, Redemption, Friendship, Agathion, Archon, Azata. |
| Evil | Infernal, demonic, corruptive, and vile powers should remain legible rather than being dispersed across Death and Shadow. | Evil, Demonic, Diabolic, Corruption, Vile Darkness, Daemon, Devil, Demon, Kyton. |

## 3. Domain Mapping Proposal

The mappings below are a **first-pass conversion guide**, not a final Domain catalogue. A Domain can have a narrow name while sharing a broad Tradition Skill with other Domains.

| Domain names from reference | Proposed Tradition Skill | Typical additional Domain identity beyond access |
|---|---|---|
| Air, Sky, Storm, Weather | Air | Specific wind, cloud, lightning, flight, or atmospheric Feature. |
| Earth, Sand | Earth | Stone, metal, cave, petrification, or seismic Feature. |
| Fire | Fire | Flame, ash, smoke, heat, or combustion Feature. |
| Blackwater, Cold, Ocean, Seafolk, Water, Winter | Water | Ice, river, current, sea, fluid-body, or cold Feature. |
| Sound (future Domain or non-Domain source) | Sound | Resonance, silence, music, spoken command, or vibration Feature. |
| Dragon | Arcane | Draconic arcana, magical bloodline, breath, ancient magical lore, or draconic-language Feature. |
| Animal, Scalykind, Vermin, Plant, Summer, Fey | Nature | Creature affinity, companion permission, senses, growth, thorns, seasonal, or fey-specific Feature. |
| Artifice, City, Rune | Artifice | Craft / Engineering access, construct, mechanism, inscription, ward, or encoded-pattern Permission. |
| Chaos, Entropy, Liberation | Chaos | Riot, freedom, mutation, chance, or anti-binding Feature. |
| Law | Law | Judgment, hierarchy, binding, legislation, or lawful-oath Feature. |
| Tyranny | Evil | Oppression, domination, slavery, fear, or coercion Feature; it may carry a Law Trait where appropriate. |
| Charm, Domination, Madness, Dream, Hunger, Pleasure, Temptation, Thirst, Wealth, Greed, Hatred, Spite, Joy | Mind | Social / mental targeting, emotion, obsession, sleep, nightmare, dream travel, or inner-vision Features. |
| Darkness, Trickery | Darkness | Concealment, deception, infiltration, moon / night Traits. |
| Death, Deathbound, Repose, Undeath | Death | Turning interaction, corpse, psychopomp, or anti-undead Feature. |
| Healing, Purification | Life | Healing / restoration access and explicit Wound / Condition effects. |
| Celestial, Glory, Herald, Sun | Light | Radiance, revelation, anti-undead, holy messenger, or heroism Feature. |
| Good | Good | Redemption, benevolence, friendship, or celestial-alignment Feature. |
| Evil, Demonic, Diabolic, Corruption, Vile Darkness | Evil | Corruption, infernal pact, fear, blight, or vile Traits. |
| Fate, Destiny, Luck, Oracle | Fate | Divination, rerouting consequence, prophecy, curse, or foresight Feature. |
| Force, Magic, Mysticism | Arcane | Magical theory / spellcrafting access, force, counterspell, or ritual Feature. |
| Knowledge, Inquisition | Knowledge | Recall Knowledge, divination, secrets, languages, or investigation Feature. |
| Community, Courage, Nobility, Planning | Protection | Leadership / Diplomacy access, Rallied, oath, formation, sanctuary, or ally-support Feature. |
| Competition, Strength, War | War | Favored weapon access, martial Feat, tactic, Challenge, or Smite Feature. |
| Destruction, Fury, Wrath, Ruins, Erosion | Destruction | Damage, collapse, siege, breakage, or ruin Feature. |
| Endurance, Protection | Protection | Ward, resistance, sanctuary, armor, or fortification Feature. |
| Creation, Summoner | Creation | Conjuration, shaping, crafted manifestation, or summons Feature. |
| Travel | Space | Movement, portal, route, exploration, or trade Feature. |
| Pact | Spirit | Contact, binding, ancestor, outsider, or negotiated-service Feature. |
| Void | Void | Alien, stellar, isolation, or cosmic-horror Feature. |
| Time | Time | Temporal manipulation, delayed effect, or age Feature. |
| Pestilence | Fiendish | Disease and corruption package; Death may be an alternate future mapping if playtests favor mortality over malignancy. |
| Oozes | Nature | Aberrant ecology, acid, consumption, or fluid-body Feature.

### Intentional non-one-to-one examples

```text
Sun, Glory, and Celestial:
  Light.
  They still feel different because each Domain provides its own
  Feature and spell-acquisition permissions.

Death, Repose, Undeath, and Deathbound:
  Death.
  The Domain Feature decides whether the character lays spirits to rest,
  destroys undead, commands them, or alters death magic.

War, Competition, and Strength:
  War.
  War can grant favored-weapon Combat Mastery access;
  Competition can grant Challenge / duel procedure access;
  Strength can grant Athletics or Exert-related Permissions.

Travel:
  Space.
  The Domain provides expedition and route identity; it need not create
  a separate Travel Tradition Skill.
```

## 4. Consolidations Made in Revision 2

| Earlier candidates | Consolidated Tradition | Reason |
|---|---|---|
| Artifice + Rune | Artifice | Created objects, mechanisms, encoded patterns, wards, inscriptions, and constructs all use an external made-form model. |
| Primal + Beast | Nature | Plant, animal, vermin, dragon, fey, growth, and wilderness magic are one living-world practice. |
| Shadow → Darkness | Darkness | The name makes the Domain-to-Tradition relationship immediately legible while retaining deception and secret-path magic in its scope. |
| Mind + Passion + Dream | Mind | Thought, emotion, obsession, madness, sleep, dreams, and mental influence are all operations on consciousness. |
| Protection + Covenant | Protection | Defensive magic naturally includes sanctuary, community, allies, oaths, morale, and mutual preservation. |

**Dragon placement:** Dragon is mapped to Arcane rather than Nature. Scalykind remains Nature; it represents ordinary reptilian / saurian affinity, while Dragon represents the setting’s distinct magical draconic power.

## 5. The Most Important Open Tests

### A. Is 28 Tradition Skills too many?

This is a catalogue size, not a requirement that a character learn them all. Most divine characters would have:

```text
Divine
+ two to four Domain-granted Traditions
+ perhaps one Tradition from ancestry, feat, path, or item
```

A full caster needs enough Magic Mastery advancement to train a secondary Tradition without sacrificing all mundane competence. The proposed Class-specific extra Magic Mastery Investment policy is therefore structurally important.

### B. Good versus Light; Evil versus Void

`Good`, `Evil`, `Law`, and `Chaos` are retained as four first-class Divine Domains. This revision also gives each a matching broad Tradition Skill, rather than forcing Good into Light or Evil into a source-specific `Fiendish` label. `Light` remains sun, radiance, revelation, and anti-undead magic; it is not synonymous with Good. `Void` remains alien, cosmic, and reality-eroding; it is not synonymous with Evil.

### C. Is Sound independent from Air?

**Recommendation: yes.** Air governs wind, weather, atmospheric force, and flight. Sound governs resonance, silence, music, voice, vibration, and sonic force. This leaves room for future Bard, herald, rune-song, and command-magic content without treating every sonic effect as weather magic.

### D. Is Mind too broad?

This revision deliberately makes Mind broad: it handles cognition, control, emotion, temptation, madness, dreams, and inner revelation. That consolidation is promising if spell lists distinguish those effects through Traits and spell entries. If it becomes too broad in actual spell conversion, Dream is the clearest future candidate to split back out.

### E. Catalogue size after consolidation

Twenty-eight Skills is a more manageable first pass. The four element split remains recommended because it produces distinct iconic spell lists and elemental identities. Air, Earth, Fire, Water, Sound, and the four cardinal-alignment Traditions should be tested before being merged away.

### F. Magic Mastery-only Investments

**Not decided.** The current preferred direction is:

```text
Class-specific table decides.

Normal benchmark:
  a meaningful spellcasting Class / Prestige Class level often grants
  1 additional Skill Investment restricted to Domain VII: Magic Mastery.

Likely—but not mandatory—cadence:
  grant it on a level that grants a Spell Slot Advancement.
```

This investment must identify its restriction and eligible Tradition Skills in the Class-table entry. It is not a universal replacement for the 25 baseline Investments.

## 6. Triel Check

Under this proposal, Triel’s initial access package is:

```text
Cleric base: Divine
War Domain: War + Heavy Blades access for Enthariel's favored weapon
Healing Domain: Life
Law Domain: Order
Sun Domain: Light

Alignment Domains remain independently available where a deity grants them:
  Good Domain  → Good
  Evil Domain  → Evil
  Law Domain   → Law
  Chaos Domain → Chaos
```

This removes the earlier incorrect composite `Divine Tradition — Enthariel / War-Light`. Triel instead has several independently ranked Tradition Skills, with `Divine` as the natural candidate for protected high-rank advancement.

## 7. Recommended Next Decision Sequence

1. Review the 28-Skill catalogue and confirm the preferred names, especially `Artifice` versus `Rune` and `Darkness` versus `Shadow`.
2. Confirm Good, Evil, Law, Chaos, Air, Earth, Fire, Water, and Sound as proposed separate Tradition Skills.
3. Test whether the broad Mind and Protection lists stay legible in actual spell conversion.
4. Define a first playable Cleric Domain list: perhaps 12–20 Domains rather than importing every legacy Domain immediately.
5. Define what Domain access grants at Level 1: access only, access plus a named spell, or access plus Trained Rank.
6. After those decisions, test Cleric, Druid, Paladin, and a domain-rich Prestige Class against the Class-specific Magic Mastery Investment cadence.
