# Activity, Assistance, Tool, and Craft Procedure Model — Draft

**Status:** Design draft; non-canonical.  
**Purpose:** Model a lightweight universal Activity procedure using D&D 3.5e and Pathfinder 2e as conversion references while preserving the project’s Difficulty Vectors, Boon/Bane types, Requirements, Permissions, and no-linear-modifier philosophy.

This document does not establish Activity, Craft, Lore, tool, assistance, downtime, repair, or failure rules.

## 1. Design Goal

```text
Default activity:
  One primary Skill check.

Complexity:
  Added only when the specific Activity needs it.

Support:
  A relevant Skill, tool, ally, or permission changes the procedure
  only when the Activity explicitly says how.
```

This takes useful structural lessons from D&D 3.5e skill checks and PF2e Skill Activities without importing linear bonuses, arithmetic crafting progress, universal degrees of success, or a generic complication table.

## 2. Recommended Universal Activity Entry

Every defined Activity should use this template:

| Field | Purpose |
|---|---|
| Name | Player-facing Activity name |
| Category | Exploration, downtime, encounter, combat, social, crafting, research, travel, or another stated category |
| Primary Skill | The one Skill that makes the ordinary check |
| Relevant Attribute | The Attribute used to determine die size |
| Requirements | Required Rank, tool, material, position, target state, time, permission, or Tag |
| Helpful sources | Skills, tools, allies, equipment, spells, or circumstances that can alter the procedure when stated |
| Cost / time | Actions, minutes, hours, days, materials, Stamina, Essence, money, or another stated resource |
| Resolution | Difficulty Vector or opposed check |
| Success | What succeeds, is learned, is produced, is repaired, or becomes permitted |
| Failure | Specific consequence; absence of a special consequence means the Activity simply fails |
| Tags | Relevant Activity Tags or effect Tags |

## 3. Default Resolution Model

### One primary check

```text
Default:
  Choose one primary Skill.
  Use its Competency Rank and the relevant Attribute Die.
  Resolve one Difficulty Vector or opposed check.
```

This should handle most activities:

```text
Open a lock.
Recall a fact.
Identify a heraldic device.
Cook a meal.
Treat a Wound.
Forge a simple item.
Track a creature.
Impersonate an official.
```

### No automatic multi-skill stacking

A second relevant Skill does not automatically add dice, successes, or a separate check. It has one of four roles only when the specific Activity says so:

| Supporting role | Effect |
|---|---|
| Alternative approach | Replaces the primary Skill when the fiction supports it |
| Requirement / Permission | Makes the Activity possible, legal, safe, or more specific |
| Assistance | Supports another Actor under the Assist procedure |
| Explicit stage | Adds a separate step because the Activity genuinely has multiple tasks |

## 4. Assistance Model

### Draft Assist Activity

```text
Assist
Cost:
  The time or Action stated by the supported Activity.

Requirement:
  The assistant can plausibly contribute using a relevant Skill,
  tool, Permission, or fictional position.

Resolution:
  The assistant makes the stated supporting check.

Success:
  The primary Actor gains 1 Competence Boon to the Activity.

Failure:
  No benefit unless the supported Activity states another consequence.
```

Multiple assistants can attempt to help only if the Activity permits it. Competence Boons follow ordinary typed-stacking rules, so multiple successful assistants do not automatically stack.

### D&D / PF2e conversion reference

| Source system | Structural lesson | Project adaptation |
|---|---|---|
| D&D 3.5e Aid Another | A helper makes a related check; limited helpers and plausibility matter | One supporting check grants a Competence Boon rather than a linear +2 |
| PF2e Aid | Assistance is a discrete action with a specific trigger and outcome | An Activity can state when Assist is available and what it costs |

## 5. Tool Model

Tools should be described by the Activity, not granted a universal always-on bonus.

| Tool status | Draft procedure |
|---|---|
| Required | The Activity cannot be attempted normally without the tool or an explicit substitute Permission |
| Improvised | The Activity may be attempted with 1 Circumstance Bane if its entry permits improvisation |
| Helpful | The Activity states a specific benefit, commonly a Permission or 1 typed Boon |
| Specialized / masterwork | The specific tool entry grants an Enhancement Boon, Trait, Permission, reduced time, expanded output, or other stated effect |
| Consumed | The Activity states the quantity consumed on attempt, success, or failure |

This preserves the D&D 3.5e intuition that ordinary tools enable Craft, improvised tools are worse, and masterwork tools help, while using Tags, Requirements, and typed Boons instead of static `±2` modifiers. [2](https://stellardragons.com/srd/dnd-3-5-srd/dnd-3-5-srd-skills-i/)

## 6. Failure and Complications

```text
There is no universal failure-complication table.

Each Activity states its own failure result.
```

Recommended failure categories:

| Failure type | Examples |
|---|---|
| Simple failure | Lock remains closed; fact is not recalled; item is not produced |
| Time cost | Another interval is spent; pursuit advances; daylight is lost |
| Resource cost | Ingredients are consumed; tool is strained; Essence is spent |
| Exposure | Noise alerts guards; trail is disturbed; disguise becomes suspicious |
| Escalation | Trap activates; a social target becomes hostile; hazard worsens |
| False result | Use only when an Activity explicitly permits misleading or uncertain information |

## 7. When to Use Stages

A staged procedure should be exceptional and named explicitly.

| Activity | Default | When stages are justified |
|---|---|---|
| Investigation | One primary check | A complex scene with separate discovery, interpretation, and access problems |
| Lockpicking | One Thievery check | A trapped, magical, or multipart lock with distinct components |
| Disguise | One Deception or Performance check | Crafting disguise materials, maintaining cover identity, and social verification are distinct challenges |
| Crafting | One downtime Craft Activity | Design, rare-material acquisition, construction, and final attunement are separate project tasks |
| Treat Wounds | Current stabilization/recovery procedure | Surgery, poison treatment, disease treatment, or a special Wound requires different steps |

## 8. Craft Activity Model

Each `Craft — X` specialty has its own Competency Rank. Craft Procedures should use the following model.

### Create or produce

```text
Primary Skill:
  Relevant Craft — X specialty.

Requirements:
  Recipe, plan, materials, tools, workshop, Rank, or Permission
  as stated by the item or project.

Cost / time:
  Defined by the item, recipe, project, or downtime procedure.

Success:
  Produce the listed item, batch, service, or project step.

Failure:
  Defined by the project; default is no progress beyond spent time.
```

### Repair

```text
Primary Skill:
  Relevant Craft — X specialty.

Requirements:
  Repair tools and access to the item.

Resolution:
  The item or effect states the Difficulty Vector, time,
  and Durability restored.

Limit:
  A destroyed or 0-Durability item follows its own repair rule.
```

This adapts D&D 3.5e’s tool/material/time emphasis and PF2e’s discrete Repair Activity while rejecting arithmetic progress-by-price formulas. PF2e Repair uses a specific Craft check, a repair toolkit, and a stated time/result. [1](https://2e.aonprd.com/Actions.aspx?ID=2384&Redirected=1)

### Knowledge and Craft support

| Pair | Recommended relationship |
|---|---|
| Knowledge — Engineering / Craft — Engineering | Knowledge analyzes, designs, diagnoses, or supplies a Permission; Craft constructs or repairs |
| Knowledge — Alchemy and Pharmacology / Craft — Alchemy | Knowledge identifies, analyzes, diagnoses, or supplies a Permission; Craft produces, refines, or repairs alchemical material |
| Lore / Craft | Lore supplies local, historical, cultural, or trade-specific Permission where relevant |

## 9. Lore and Knowledge Activities

### Recall Knowledge

```text
Primary Skill:
  Relevant Knowledge — X.

Success:
  Learn systematic facts, principles, capabilities,
  vulnerabilities, or procedures within the Skill’s scope.
```

### Recall Lore

```text
Primary Skill:
  Lore — X.

Success:
  Learn specific historical, cultural, local, factional,
  experiential, or subject-specific facts within the Lore scope.
```

A Lore specialty has its own Rank and is narrower than a Knowledge Skill. The Activity, not the base Lore rule, determines what a success reveals in the current situation.

## 10. Example Activity Profiles

| Activity | Primary Skill | Typical Requirements | Support examples | Default failure |
|---|---|---|---|---|
| Stabilize | Knowledge — Anatomy and Healing | Adjacent Incapacitated Actor | Healer’s tools; assistant | Actor remains unstabilized |
| Repair armor | Craft — Armorsmithing | Repair tools; item access | Knowledge — Engineering | No Durability restored |
| Brew alchemical item | Craft — Alchemy | Formula; alchemical tools; ingredients | Knowledge — Alchemy and Pharmacology | No product; project states material loss if any |
| Forge weapon | Craft — Weaponsmithing | Workshop; materials; plan | Knowledge — Engineering | No progress beyond time spent by default |
| Identify relic | Knowledge or Lore | Object access | Relevant Lore / tools | No reliable identification |
| Investigate scene | Skill chosen by method | Time / access if stated | Spot, Listen, Knowledge, Lore, tools | No clue or only stated partial result |
| Lockpick | Thievery | Thieves’ tools | Knowledge — Engineering; assistant | Lock remains closed; trap/alert only if stated |

## 11. Decisions Still Needed

1. Does Assist cost 1 Action in encounters and an Activity’s stated interval outside encounters?
2. Does a successful Assist always grant 1 Competence Boon, or do some Activities use a different result?
3. Which tool categories have a standard Helpful or Specialized benefit, if any?
4. Can general Craft be attempted without a specialty, and if so, under what limit?
5. What project or recipe format states Craft time, materials, Difficulty Vectors, and output?
6. What does 0 Durability mean for repairability and replacement beyond the current “cannot perform its function” rule?
7. Which Activities need explicit staged procedures in the first MVP content set?
