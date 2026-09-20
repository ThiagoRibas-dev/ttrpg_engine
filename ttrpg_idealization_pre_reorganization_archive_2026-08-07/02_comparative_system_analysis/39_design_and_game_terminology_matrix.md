# Design and Game Terminology Matrix

**Status:** Research / terminology-planning artifact; non-canonical.  
**Purpose:** Compare terminology from selected TTRPG rulebooks and playtest materials with the project’s current game glossary, repository-reorganization model, and Framework Spine. This document identifies terms that should be player-facing, design-facing, deprecated, or avoided during the future rewrite.

## 1. Why Separate Terminology Layers

The project currently needs two deliberately different vocabularies:

```text
Game vocabulary:
  Terms players and GMs use to play the game.

Design vocabulary:
  Terms designers and future agents use to organize, validate,
  migrate, and assemble the game framework.
```

A term may be useful in one layer and confusing in the other.

| Example | Appropriate layer | Reason |
|---|---|---|
| Action | Game vocabulary | A player spends it during a Turn. |
| Condition | Game vocabulary | A player checks its stated effects in play. |
| Framework Spine | Design vocabulary | It organizes documents; it is not a game object. |
| Registry node | Design vocabulary | It identifies a specification in the relationship map. |
| Decision Record | Design vocabulary | It preserves historical rationale, not an in-game decision. |
| Trait | Both, with care | It is a game term and a useful content-classification term. |

## 2. Reference Systems and Documents

| Source | Terminology pattern relevant here |
|---|---|
| **D&D Next / One D&D playtests** | Player-facing packets organized around Races / Classes / Backgrounds / Feats / Equipment / Spells plus a Rules Glossary. Uses Feature, Prerequisite, Property, Requirement, Effect, and Benefit in ordinary language. |
| **Pathfinder 2e** | Defines a generic “rules element” and gives entries structured by Traits, Prerequisites, Frequency, Trigger, Requirements, Effect, and Special. |
| **Dragonbane** | Uses direct, low-jargon player terms: Kin, Profession, Heroic Ability, Action, Reaction, Condition, Willpower, Boon, Bane, and skill checks. |
| **Ironsworn / Starforged** | Separates explanation, visual primer, detailed procedures, and an at-table reference guide; useful for document type rather than borrowing game terms. |
| **Diátaxis** | Separates Tutorial, How-to Guide, Reference, and Explanation by reader need. |
| **arc42** | Separates goals, constraints, scope, solution strategy, building blocks, runtime behavior, cross-cutting concepts, decisions, quality requirements, risks, and glossary. |
| **Architecture Decision Records** | Uses Status, Context, Decision, Consequences, options, and supersession. |

## 3. Player-Facing and Game-Framework Vocabulary

### 3.1 Core game objects and procedures

| Concept | D&D / One D&D usage | Pathfinder 2e usage | Dragonbane usage | Current / proposed project term | Rewrite recommendation |
|---|---|---|---|---|---|
| Person or entity governed by rules | Creature, character, monster, NPC | Creature, character, NPC | Adventurer, creature, monster | **Actor** in schema; creature / character in prose | Keep **Actor** as a technical schema term. Use **character**, **creature**, **NPC**, or **monster** in player / GM prose. |
| Player-controlled character | Character, player character | Character, PC | Adventurer | Character / PC | Keep **Character** and **PC**. |
| GM-controlled character | NPC, monster, creature | NPC, creature | NPC, monster | NPC / monster | Keep. |
| Discrete player option | Feature, Feat, spell, property | Rules element, Feat, action, spell, item | Heroic Ability, ability, spell | Class Feature, Feat, Spell, Ability | Keep specific entry types. Use **Feature** as the broad player-facing category only when needed. |
| General named mechanical object | Rule, game statistic, feature | Rules element | Rule, ability, condition | Rule element (candidate) | Consider **rule element** for a generic formal entry type. It is established PF2 terminology and clearer than “interface.” |
| Action performed in a Turn | Action, bonus action, reaction | Action, free action, reaction, activity | Action, reaction, movement | Action, Reaction, Activity | Keep the current distinction: **Action** is turn currency; **Activity** is a defined objective / procedure; **Reaction** is out-of-turn response. |
| A defined objective / task | Action, check, activity in ordinary prose | Activity | Action / task | Activity | Keep **Activity**; it already has a specific canonical meaning. |
| Roll resolving uncertainty | Ability check, attack roll, saving throw | Check, Strike, saving throw | Skill check | Check; Attack; Strike; Fortitude / Willpower | Keep distinct named checks rather than calling every roll a generic test. |
| Opposed action | Contest / opposed check | Check against DC or opposed procedure | Opposed roll | Opposed check / opposed contest | Keep **opposed check** as the ordinary term; reserve **contest** only if a procedure needs a neutral non-attacker / defender framing. |
| Difficulty | DC, difficulty, target number | DC | Skill value / opposed result | Target Number; Difficulty Class; Difficulty Vector | Keep the current three terms, with concise glossary distinctions. |
| State affecting an Actor | Condition, effect | Condition, effect | Condition | Condition | Keep **Condition** for named player-facing states. |
| Ongoing or immediate result | Effect | Effect | Effect | Effect | Adopt **Effect** as the ordinary broad term for what a rule does. |
| Persistent characteristic | Property, trait | Trait | Ability / trait in ordinary prose | Trait | Keep **Trait** for persistent descriptors. |
| Interaction keyword | Property, keyword | Trait | No single equivalent | Tag | Keep **Tag** as the operational interaction label; explain it early in reference material. |
| Resource | Spell Slot, Hit Points, uses | Cost, Focus Point, frequency | Willpower, HP | Vitality, Stamina, Essence, Spell Slot, Durability | Keep current in-world resource names and use **Cost** for a stated expenditure. |

### 3.2 Rule-entry fields and gating language

| Design job | D&D / One D&D | Pathfinder 2e | Dragonbane | Current rewrite term | Notes |
|---|---|---|---|---|---|
| Must qualify to select an entry | Prerequisite | Prerequisite | Profession / skill gating in ordinary prose | **Prerequisite** | Use for character-build selection only. |
| Must be true to use an entry now | Requirement | Requirement | Direct “must have / cannot” prose | **Requirement** | Use for current fictional / equipment / position conditions. |
| Event allowing out-of-turn use | Trigger | Trigger | Reaction timing | **Trigger** | Use where a Reaction, defense, or special response begins. |
| How often usable | Uses, rest recharge | Frequency | Willpower / action economy / rests | **Frequency** or explicit recovery rule | Use Frequency only where a hard use limit exists; do not add it to resource-paid effects unnecessarily. |
| Resource paid | Spell Slot, charges, uses | Cost | Willpower | **Cost** | Name the actual resource: `Cost: 1 Stamina`. |
| What happens | Effect, benefit | Effect | Effect | **Effect** | Preferred universal consequence label. |
| Exception / special case | Specific beats general; special rule | Special | Direct text | **Exception** or **Special** | Use **Exception** in framework prose; use **Special** only as a compact content-entry field if needed. |
| Restriction / prohibition | Can’t, must, limitation | Restriction in ordinary rule text | Cannot | **Restriction** | State directly: “You cannot…” where player-facing. |
| Access to an option / category | Proficiency, can cast, can use | Access, granted proficiency, ability | Profession training / spell school | **Access** | Use for Traditions, Class Skills, weapon categories, recipes, and similar eligibility. |
| General old project term | “Permission” is not a standard catch-all field | Not used as a generic entry field | Not used as a generic entry field | **Deprecated** | DEC-102: replace by Access, Requirement, Effect, Exception, Restriction, or Disruption according to job. |
| Tagged interruption | Spell / condition text | Trigger, effect, trait | Direct text | **Disruption** | Replaces legacy `Disrupt Permission`. |

### 3.3 Recommended player-facing rule entry format

Not every entry needs every field.

```text
Name
Traits
Prerequisite (if selection-gated)
Requirement (if use-gated)
Trigger (if reactive)
Frequency (if hard-limited)
Cost (if paid)
Effect
Restriction / Exception / Special (only if needed)
```

This borrows the clarity of Pathfinder’s “rules element” presentation without importing Pathfinder’s mechanics.

## 4. Design and Repository Vocabulary

These terms should normally stay outside player-facing rules.

| Design / repository concept | arc42 / ADR / Diátaxis analogue | Proposed project term | Meaning | Player-facing? |
|---|---|---|---|---|
| Whole active design map | Architecture documentation | **Framework Architecture Map** | Goals, constraints, scope, blocks, loops, risks, glossary map. | No |
| Stable ordered subsystem map | Building-block / solution strategy | **Framework Spine** | Core Engine → Actor → Adventure → Conflict → Magic → Equipment → World / GM → Reference. | No |
| One authoritative technical rule file | Reference documentation | **Canonical Specification** | Current complete technical owner for one procedure / subsystem. | No |
| A named thing in the registry | Graph node / building block | **Registry Node** | Metadata identity for a document, procedure, workflow, experiment, or record. | No |
| A formal connection in the registry | Graph edge / dependency | **Rule Relationship** | Requires, uses, grants, modifies, limits, tests, replaces, contains, related. | No |
| Design reason and historical choice | ADR | **Decision Record** | Major decision’s context, outcome, alternatives, and consequences. | No |
| Current concise decision list | ADR index | **Decision Index** | Fast scan of DEC records. | No |
| External evidence / rationale | Explanation | **Research** | Comparative systems, simulations, theory, sources. | No |
| Temporary model | Prototype / validation scenario | **Experiment** | Conversion, playtest, scenario, or temporary mechanic test. | No |
| Repeatable design task | How-to guide | **Workflow** | Create a Class, convert a spell, validate a rule, migrate a file. | No |
| Actual player-facing game entry | Content / implementation | **Content Entry** | A Class, Feat, Spell, item, creature, ancestry, recipe, adventure. | Yes |
| Finished teaching text | Tutorial / publication | **Publication Draft** | Future Player Guide, GM Guide, or reference guide. | Yes |
| Historical material | Superseded / archive | **Archive** | Preserved but inactive material. | No |

## 5. Rule Relationship Vocabulary

This vocabulary is for the registry only. It is not intended to appear as player-facing game language.

| Registry relationship | Direction | Meaning | Example |
|---|---|---|---|
| `requires` | Rule → prerequisite rule | Source cannot function without target. | Deflect requires Stamina. |
| `uses` | Rule → procedure | Source resolves through or invokes target. | Grapple uses the opposed-check procedure. |
| `grants` | Source → rule element / access | Source gives access, a Feature, a Rank, a Trait, or a stated capability. | War Domain grants War Tradition access. |
| `modifies` | Source → baseline procedure | Source explicitly changes a stated baseline part in its own scope. | A shield modifies Deflect by granting 1 Boon. |
| `limits` | Source → affected rule | Source restricts or prohibits target use. | Immobilized limits Movement Activities. |
| `tests` | Experiment / research → rule | Source validates, calibrates, or stress-tests target. | Defense simulation tests Deflect. |
| `replaces` | New → historical | Source supersedes target. | New Wound rule replaces archived Wound draft. |
| `contains` | Parent → child | Structural relationship only. | Conflict Framework contains Deflect. |
| `related` | Either direction | Informational association only. | Light Tradition is related to Destroy Undead. |

### Explicitly avoided registry terms

```text
interface
implements
extension point
constraint
permission
```

They may be useful in software design, but the project has clearer game-design alternatives.

## 6. Mapping Current Project Terms to Rewrite Terms

| Current term / phrase | Status | Rewrite target | Reason |
|---|---|---|---|
| Permission | Deprecated | Access, Effect, Exception, Restriction, or direct wording | Too broad and software / legal sounding. |
| Disrupt Permission | Deprecated | Disruption | Clearer description of the actual effect. |
| Universal Actor Schema | Retain as technical term | Actor Framework / Actor Schema | Useful for framework architecture, not necessarily player prose. |
| Class Skills | Retain | Class Skills | Familiar and clear player-facing term. |
| Framework, Derived-Subsystem, and Content Boundary | Retain concept | Framework Scope Boundary | Simplify heading in new architecture map. |
| Good / Medium / Bad progression | Retain as design calibration term | Progression profile | Keep out of player-facing Class tables. |
| Status: Locked / Provisional / Open | Retain | Status | Design-only metadata. |
| Outstanding Definitions Index | Replace in new structure | Active Risks and Open Definitions | Better aligned with the architecture-map model. |
| Master Brainstorm Log | Replace in new structure | Decision Index + Decision Records + Experiments | One document currently performs too many jobs. |
| Canonical owner | Retain | Canonical owner | Clear design-maintenance term. |
| Framework Spine | New | Framework Spine | Design-only ordered map of active subsystems. |
| Rule interactions | New | Rule interactions | Plain heading for how other rules use, grant, modify, or limit a procedure. |

## 7. Exception-Based Rule Hierarchy and Terminology Policy

The game is explicitly exception-based:

```text
The most specific applicable rule supersedes the more general rule
within its stated scope.

The general rule remains in force everywhere else.
```

This means player-facing rules should use a controlled rules vocabulary rather than avoiding keywords for the sake of conversational prose. Each entry must make its scope legible through terms such as:

```text
Traits
Prerequisite
Requirement
Trigger
Frequency
Cost
Effect
Restriction
Exception
Special
```

The purpose is not jargon for its own sake. It is to let a player answer:

```text
What is the normal rule?
What exact rule changes it?
When does that change apply?
What does it cost?
What does it do?
```

```text
Player-facing rules:
  Use direct concrete game language plus defined rules terms.
  Use “you can / cannot” wording inside an Effect, Restriction,
  or Exception where that is clearest.

Framework specifications:
  Use player-facing terms for game procedures plus design-only metadata
  such as Status, Scope, and Open Definitions.

Registry and architecture map:
  Use technical terms such as Node, Rule Relationship, Requires, and Tests.

Research and decisions:
  May use comparative and rationale vocabulary, but must not redefine
  game terms.
```

## 8. Sources

- Pathfinder 2e rules-element structure: <https://2e.aonprd.com/Rules.aspx?ID=2026&Redirected=1>; rule formatting and Trait conventions: <https://2e.aonprd.com/Rules.aspx?ID=2020&Redirected=1>
- One D&D playtest examples of Prerequisite and Effect language: <https://media.dndbeyond.com/compendium-images/one-dnd/ph-playtest5/owThVp1CESZ1c91y/UA-2023-PH-Playtest5.pdf>; D&D Next packet categories: <https://www.scribd.com/document/212530845/DnD-Playtest-Read-First>
- Dragonbane direct rules terminology and procedure overview: <https://www.drivethrurpg.com/en/product/409397/Dragonbane-Quickstart>; <https://gamingtrend.com/reviews/dragonbane-rulebook-review-lightweight-but-super-fun/>
- Diátaxis documentation categories: <https://egh0bww1.com/republish/2024-06-21-diataxis-documentation/>
- Architecture Decision Record structures: <https://adr.github.io/adr-templates/>

## 9. Open Terminology Decisions

1. Should `Feature` be the preferred broad player-facing name for any discrete non-spell capability, or should it remain Class-specific?
2. Should `rule element` appear in player-facing reference text, or remain a framework / content-template term?
3. Should `Special` be a standard content-entry field, or should all special cases use direct Exception / Restriction prose?
4. Should `Activity` remain the sole term for non-combat procedures, or should the framework distinguish Activity from extended Project / Downtime procedure entries?
5. How should the player-facing glossary introduce Actor-derived terms without requiring players to learn the technical Actor Schema vocabulary?
