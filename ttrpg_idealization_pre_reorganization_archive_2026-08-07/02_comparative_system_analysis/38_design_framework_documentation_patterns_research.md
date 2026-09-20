# Design-Framework Documentation Patterns Research

**Status:** Research / reorganization-preparation artifact; non-canonical.  
**Purpose:** Compare established documentation and design-record structures that may help organize an unfinished TTRPG framework without prematurely formatting it as a finished player rulebook.

## 1. The Design Problem

The active project needs a documentation system that can hold all of the following without mixing them:

```text
Current rule specification:
  What the game currently does.

Design rationale:
  Why a rule exists and what alternatives were rejected.

Research and experiment:
  What external systems, simulations, and conversion tests reveal.

Open work:
  What remains undecided or blocked.

Future publication text:
  How a finished player or GM book may eventually teach the rule.
```

A final rulebook structure alone cannot do all five jobs cleanly. A pure whiteboard / brainstorm repository also fails once the framework gains dependencies. The most relevant external models therefore come from technical-documentation and architecture practice, adapted carefully for game design.

## 2. Diátaxis: Separate Documentation by Reader Need

### The model

Diátaxis distinguishes four forms of documentation:

| Documentation type | Primary question | Project equivalent |
|---|---|---|
| Tutorial | “Can you teach me?” | Future learn-to-play, first character, first combat, first spellcasting walkthrough. |
| How-to guide | “How do I accomplish this?” | Designer workflows: add a Condition, create a Spell, convert a Class, run a calibration test. |
| Reference | “What is this exactly?” | Canonical procedures, tables, glossary, Tags, Traits, conditions, schema, templates. |
| Explanation | “Why is it this way?” | Design pillars, decision rationale, comparative research, architecture notes. |

### Value for this project

This is likely the cleanest solution to the current “research and framework text are mixed” problem:

```text
Canonical framework files become Reference.

Research / comparisons / rationale become Explanation.

Conversion and design workflows become How-to Guides.

Future onboarding scenarios become Tutorials.
```

### Important caution

Diátaxis categorizes by **reader need**, not by game subsystem. It should be a second axis across the repository, not the only directory order. For example, `Combat` needs a canonical Reference procedure, an Explanation of defensive-resource philosophy, a How-to for writing a new maneuver, and eventually a Tutorial showing a first combat Round.

## 3. arc42: Architecture Map for a Living System

### The model

arc42 is a software-architecture documentation template. Its most useful sections for this project are:

| arc42 concept | TTRPG-framework equivalent |
|---|---|
| Introduction and goals | Design pillars, target play experience, game scope. |
| Constraints | Mathless-at-table rule, bounded d4–d12, no meta-currency, low-memory feature policy. |
| Context and scope | What counts as framework, subsystem, content, research, and archive; external content-conversion boundary. |
| Solution strategy | Core engine and rulebook-shaped framework spine. |
| Building-block view | Subsystem ownership map: resolution, actor, adventure, conflict, magic, equipment, GM framework. |
| Runtime view | Gameplay loops: character creation, Activity, combat exchange, recovery, advancement, spellcasting, Craft. |
| Cross-cutting concepts | Tags / Traits, Actions, resources, Conditions, Requirements, Permissions, terminology. |
| Architecture decisions | Decision Records. |
| Quality requirements | Design acceptance criteria, probability bands, low-memory tests, conversion tests, playtest goals. |
| Risks and technical debt | Outstanding Definitions, stale documents, uncalibrated systems, deferred content. |
| Glossary | Canonical vocabulary. |

### Value for this project

arc42 provides the **missing top-level architecture map**. It does not tell us how to write each rule, but it ensures every rule has a clear place in a map of the whole game.

### Important caution

Do not import the full software template literally. Deployment / infrastructure views are irrelevant. The useful idea is the separation of:

```text
Goals
Constraints
Subsystem building blocks
Gameplay runtime loops
Cross-cutting concepts
Decisions
Quality tests
Known risks
Vocabulary
```

## 4. Architecture Decision Records: Immutable “Why” History

### The model

An Architecture Decision Record (ADR) is a short, numbered record of one significant decision. A minimal structure is:

```text
Status
Context
Decision
Consequences
```

A fuller form also records decision drivers, considered options, rationale, confirmation / test, and the decision that supersedes it.

### Value for this project

The current master decision table records outcomes efficiently, but an individual decision can still hide:

- the exact problem that prompted it;
- alternatives considered;
- dependencies and migration impacts;
- confirmation criteria;
- why a former rule was superseded.

A lightweight ADR pattern would fit major framework decisions such as:

```text
Competency pool-volume architecture.
Resource tracks.
Wound procedure.
Manual Skill Investments.
Magic Tradition catalogue.
Domain Tradition Grants.
Feature-conversion low-memory policy.
Future repository migration architecture.
```

### Recommended adaptation

```text
Keep a one-line Decision Index for fast scanning.

Create a full Decision Record only for a decision that changes
architecture, cross-system interfaces, terminology, or migration scope.

Accepted records are not rewritten.
A changed decision creates a new record that explicitly supersedes it.
```

This preserves the history without forcing every small wording adjustment into a large template.

## 5. Living Game Design Documents: Modular, Not Monolithic

Contemporary game-design practice generally treats the GDD as a living, modular resource rather than a finished specification written before development. The recurring lessons are:

```text
Start with goals, pillars, audience, and core loop.

Split independent systems into smaller updateable documents.

Use visual flowcharts / scenario examples for complex interactions.

Keep only the current implementation details in the active specification.

Preserve earlier concepts in history instead of leaving alternatives
interleaved with active rules.
```

TTRPG design discussion adds an important distinction: the final rulebook can be a rules reference, but designers still need meta-design documents that contain intent, quality criteria, experiments, and rejected alternatives.

## 6. Candidate Hybrid for This Project

The strongest combined model is:

```text
A. Framework Architecture Map (arc42-inspired)
   One top-level document that explains the system’s goals, constraints,
   subsystems, gameplay loops, cross-cutting concepts, quality criteria,
   risks, and vocabulary map.

B. Canonical Rule Specifications (Reference)
   One authoritative owner per procedure, written as technical rules.

C. Design Decision Records (ADR-inspired)
   Immutable rationale for major architectural choices.

D. Research and Explanation
   Comparative systems, simulations, calibration, theory, and rationale.

E. Design Workflows (How-to)
   Conversion procedures, Class / Spell / item / monster templates,
   validation workflows, and migration procedure.

F. Experiments
   Playtest builds, conversion exercises, temporary modeling, and
   scenario tests. Never mistaken for canon.

G. Future Tutorials / Rulebook Drafts
   Kept separate until the framework stabilizes.
```

### Proposed active-framework architecture document

A new `Framework Architecture Map` could use this adapted outline:

```text
1. Purpose and design goals
2. Non-negotiable constraints
3. Scope boundary and document-status model
4. Core solution strategy
5. Subsystem ownership map
6. Gameplay loop map
7. Cross-cutting concepts
8. Decision-record index
9. Quality / validation requirements
10. Active risks and deferred work
11. Vocabulary map
12. Migration map
```

It would not duplicate rules. It would answer:

```text
Where does this rule belong?
What other systems does it touch?
What is open?
How do we know the design is working?
Which document is authoritative?
```

## 7. Canonical Rule Specification Template

A framework rule file should be shorter and more regular than the current mixed prose / history documents.

```text
# [Subsystem / Procedure Name]

Status:
  Locked / Provisional / Open.

Purpose:
  What job the subsystem performs in play.

Scope:
  What it owns and explicitly does not own.

Dependencies:
  Canonical inputs required from other owners.

Canonical procedure:
  The complete current rule.

Outputs / state changes:
  Resources, Conditions, Tags, permissions, or results created.

Interfaces:
  How Classes, Feats, Spells, Equipment, Activities, and creatures
  may extend this procedure.

Validation criteria:
  What needs testing or calibration.

Open definitions / deferred content:
  Precise unresolved items.

References:
  Decision Records, research, and related canonical owners.
```

The important rule is:

```text
Rationale and historical alternatives link outward.
They do not interrupt the canonical procedure.
```

## 8. How This Differs From a Final Rulebook

| Framework design system now | Final rulebook later |
|---|---|
| Technical / precise | Teaches new readers progressively. |
| Status and dependencies visible | Status markers removed; only finished rules shown. |
| Links to research and decisions | Design history omitted or placed in designer notes. |
| Open questions named explicitly | Open questions resolved or excluded. |
| Content interfaces and templates | Actual Classes, Spells, items, creatures, examples. |
| Many files optimized for revision | Chapters optimized for reading, layout, and at-table reference. |

The future Core Rulebook order remains useful as a **subsystem map**, but should not constrain the active framework to publication-ready prose.

## 9. Sources

- Diátaxis documentation types and reader-need separation: <https://egh0bww1.com/republish/2024-06-21-diataxis-documentation/>; overview: <https://www.katara.ai/blog/diataxis>
- arc42 architecture template / section map: <https://docs.arc42.org/section-1/>; overview of solution strategy and building-block view: <https://parserdigital.com/2022/10/18/architecture-documentation-with-arc42/>
- Architecture Decision Record structures and decision rationale: <https://adr.github.io/adr-templates/>; <https://icepanel.io/blog/2023-03-29-architecture-decision-records-adrs>
- Living / modular GDD practice: <https://slite.com/learn/game-design-document>; practitioner discussion: <https://www.reddit.com/r/gamedesign/comments/1nlgdd3/curious_how_other_devs_approach_their_game_design/>
- TTRPG-specific discussion of separate design intent and final rule text: <https://www.reddit.com/r/RPGdesign/comments/91q918/game_design_documents_for_tabletop_rpgs/>; <https://forum.rpg.net/index.php?threads/pen-and-paper-game-design-documents.147036/>

## 10. Next Questions

1. Do we adopt the hybrid model as the rewrite target?
2. Which existing document should become the new Framework Architecture Map, versus being archived and replaced?
3. Which existing decisions deserve full Decision Records before migration?
4. Do we retain the current numeric `DEC-###` convention, or create a new rewrite-era decision-record series with explicit supersession links?
5. What minimal framework spine is needed before any rules are migrated?
