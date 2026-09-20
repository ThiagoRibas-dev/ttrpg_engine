# Framework Reorganization Model — Draft

**Status:** Draft organizational model; partially approved for migration planning; non-canonical.  
**Purpose:** Define a proposed structure for rebuilding the project as an active game-design framework. This is not a final player rulebook plan and does not move, archive, rewrite, or alter any current rules by itself.

---

## 1. Problem Statement

The current repository contains valuable canonical rules, research, simulations, conversion exercises, decision history, historical material, and early content modeling. These materials have grown interdependent enough that their present directory structure makes it difficult to answer basic design-maintenance questions:

```text
What is the current rule?

Which document is its sole owner?

What does it require?

What later systems and content does it affect?

What research supports it?

What remains open?

What historical document is safe to ignore?
```

The reorganization must make active design work easier **before** the game is ready for a finished Player Rulebook or GM Guide.

---

## 2. Design Goals

The new framework organization should:

1. **Separate rule, rationale, research, experiment, workflow, content, and archive.**
2. **Give every active core procedure one complete canonical owner.**
3. **Make upstream and downstream rule relationships visible without duplicating dependency lists inside every rule file.**
4. **Follow a stable, rulebook-shaped subsystem order without requiring publication-ready prose.**
5. **Support machine validation, diagrams, impact analysis, and later document assembly.**
6. **Preserve all existing history through an immutable archive snapshot and migration manifest.**
7. **Keep the system usable by a human designer and future AI agents.**

### Approved planning decisions

| Topic | Current decision |
|---|---|
| Target directory structure | Approved as the working target, subject to later file-level migration review. |
| Relationship-registry format | YAML. |
| Existing decision history | Preserve the existing `DEC-###` log and continue appending to it. |
| Initial archive migration | Rename the current root to a dated sibling archive, then create a fresh root at the current project path. |
| Migration order | Case-by-case, phased migration; do not assume every current canonical file is ready at once. |
| Generated outputs | Generate on demand; do not treat generated indexes, diagrams, or reports as hand-maintained sources. |
| Cross-references | Use precise Markdown links and stable anchors under DEC-104. |
| Relationship vocabulary | Still under review; use the terminology matrix before locking the registry vocabulary. |

### Non-goals

```text
This reorganization does not finalize the game.

It does not force a Player / GM book split now.

It does not delete old work.

It does not turn research into canon.

It does not require a complex documentation platform beyond Markdown,
YAML, and optional small scripts.
```

---

## 3. Proposed Operating Model

The model combines four complementary patterns:

| Pattern | Job in this project |
|---|---|
| **Rulebook-shaped framework spine** | Places each subsystem in a logical game-facing order. |
| **Reference / Explanation / Workflow / Experiment separation** | Prevents current rules, rationale, procedures, and tests from becoming one mixed document type. |
| **Architecture map** | Shows the system’s goals, constraints, building blocks, gameplay loops, cross-cutting concepts, risks, and vocabulary. |
| **Decision records** | Preserves why major architectural choices were made and what superseded them. |

### Core principle

```text
Rule files own rules.

The registry owns formal relationships.

Decision records own major rationale.

Research owns evidence and alternatives.

Experiments own temporary tests and models.

Archive owns history.
```

---

## 4. Proposed Repository Structure

This is a target model. It is not an instruction to create or move these directories yet.

```text
project-root/
│
├── 00_architecture/
│   ├── framework_architecture_map.md
│   ├── framework_registry.yaml
│   ├── relationship_vocabulary.md
│   ├── generated/
│   │   ├── architecture_index.md
│   │   ├── impact_reports/
│   │   └── diagrams/
│   └── migration_manifest.md
│
├── 01_framework/
│   ├── 01_core_engine/
│   ├── 02_actor_framework/
│   ├── 03_adventure_framework/
│   ├── 04_conflict_framework/
│   ├── 05_magic_framework/
│   ├── 06_equipment_framework/
│   ├── 07_world_and_gm_framework/
│   └── 08_framework_reference/
│
├── 02_decisions/
│   ├── decision_index.md
│   ├── active/
│   └── superseded/
│
├── 03_workflows/
│   ├── conversion/
│   ├── content_templates/
│   ├── validation/
│   └── maintenance/
│
├── 04_research/
│   ├── comparative_systems/
│   ├── probability_and_calibration/
│   ├── theory_and_process/
│   └── source_material_notes/
│
├── 05_experiments/
│   ├── conversion_exercises/
│   ├── scenario_tests/
│   ├── prototype_models/
│   └── playtest_packets/
│
├── 06_content/
│   ├── classes/
│   ├── feats/
│   ├── spells/
│   ├── ancestries/
│   ├── equipment/
│   ├── creatures/
│   └── adventures/
│
├── 07_publication_drafts/
│   ├── core_rules/
│   ├── gm_guide/
│   └── quick_reference/
│
└── 99_archive/
    ├── README.md (points to initial sibling archive)
    ├── superseded_framework/
    ├── superseded_decisions/
    └── historical_research/
```

### Why this layout

| Area | Responsibility |
|---|---|
| `00_architecture` | The map of the whole system and its formal relationships. |
| `01_framework` | Current technical rule specifications; sole canonical owners. |
| `02_decisions` | Significant design choices and their rationale. |
| `03_workflows` | How to create, convert, validate, update, or migrate material. |
| `04_research` | External evidence, simulations, comparisons, theory, and sources. |
| `05_experiments` | Temporary conversion builds, prototype rules, scenarios, and playtests. |
| `06_content` | Actual game entries built on the framework. |
| `07_publication_drafts` | Future reader-facing texts; not authoritative while framework remains active. |
| `99_archive` | Post-rewrite preserved history with no active authority; its README points to the initial sibling archive snapshot. |

---

## 5. Framework Spine

The active framework follows the previously proposed core-rulebook order, but each file remains a technical specification.

```text
01 Core Engine
   Vocabulary, game loop, resolution, dice, Difficulty, Boons/Banes,
   Tags, Traits, shared Requirements and Permissions.

02 Actor Framework
   Actor schema, Attributes, derived resources, Skills, Domains,
   Character creation, advancement, Class interfaces.

03 Adventure Framework
   Activities, assistance, social play, exploration, travel, downtime,
   Craft, recovery, logistics.

04 Conflict Framework
   Time, distance, initiative, Actions, Reaction, Attack / defense,
   damage, Conditions, Wounds, maneuvers, hazards.

05 Magic Framework
   Traditions, Divine Domains, Spell Slots, Essence, preparation,
   spell records, casting interfaces.

06 Equipment Framework
   Weapons, armor, shields, Durability, tools, crafting interfaces,
   magical-item framework.

07 World and GM Framework
   Difficulty guidance, encounter procedures, NPC / creature schema,
   simplified actors, reward and campaign interfaces.

08 Framework Reference
   Glossary, consolidated tables, procedure summaries, relationship maps,
   quick-reference source material.
```

This answers **where a rule belongs**. It does not yet decide how a final published reader-facing book will be split.

---

## 6. Document Types

Every active document has one primary type.

| Type | Location | Job | Tone |
|---|---|---|---|
| **Canonical specification** | `01_framework/` | Define current technical rule. | Precise, compact, authoritative. |
| **Architecture map** | `00_architecture/` | Explain whole-system structure and relationships. | Structural, navigational. |
| **Decision record** | `02_decisions/` | Record why a major decision was made. | Historical, rationale-focused. |
| **Workflow / how-to** | `03_workflows/` | Explain how to perform a design task. | Procedural. |
| **Research / explanation** | `04_research/` | Present evidence, comparisons, alternatives, and theory. | Analytical, non-authoritative. |
| **Experiment** | `05_experiments/` | Test a hypothesis or conversion. | Explicitly temporary. |
| **Content** | `06_content/` | Implement framework through actual entries. | Entry-specific. |
| **Publication draft** | `07_publication_drafts/` | Teach a stable subset to readers. | Reader-facing. |
| **Archive** | `99_archive/` | Preserve history only. | Historical. |

A document may link to documents of other types, but it should not try to perform their job.

---

## 7. Canonical Specification Template

Canonical framework specifications should follow one compact, repeatable pattern:

```text
# [Procedure or Subsystem]

Status
Purpose
Scope
Canonical procedure
State changes / results
Rule interactions
Open definitions and deferred content
References
```

### Section meanings

| Section | Meaning |
|---|---|
| **Status** | Locked, Provisional, or Open. |
| **Purpose** | The problem this procedure solves in play. |
| **Scope** | What it owns and explicitly does not own. |
| **Canonical procedure** | The complete current rule. |
| **State changes / results** | Conditions, Tags, resource expenditure, permissions, or outcomes created. |
| **Rule interactions** | What other rule elements may require, grant, modify, limit, or use this procedure; player-facing entries express the resulting Exceptions, Restrictions, and Effects explicitly. |
| **Open definitions and deferred content** | Specific unresolved decisions, not general brainstorming. |
| **References** | Decision records, research, and related named terms. Formal relationships live in the registry. |

The specification does **not** manually maintain exhaustive `Requires` or `Used By` lists. Those are generated from the registry.

---

## 8. Master Relationship Registry

### 8.1 Role

`00_architecture/framework_registry.yaml` is the formal single source of truth for:

```text
Node identity.
Current file path.
Document type.
Status.
Framework-spine placement.
Formal relationships between nodes.
Publication-target ordering.
```

It does not contain the full rule text.

### 8.2 Draft YAML shape

```yaml
version: 1

nodes:
  - id: core.resolution.opposed-check
    title: Opposed Checks
    kind: canonical-specification
    status: locked
    path: 01_framework/01_core_engine/02_opposed_checks.md
    tags: [resolution, conflict]
    publication:
      target: core-rules
      part: core-engine
      order: 20

  - id: conflict.deflect
    title: Deflect
    kind: canonical-specification
    status: locked
    path: 01_framework/04_conflict_framework/02_deflect-and-evasion.md
    tags: [conflict, defense, stamina]
    publication:
      target: core-rules
      part: conflict
      order: 20

edges:
  - from: conflict.deflect
    to: core.resolution.opposed-check
    relation: requires

  - from: conflict.deflect
    to: resources.stamina
    relation: requires

  - from: equipment.shields
    to: conflict.deflect
    relation: modifies
```

(Example edges use the DEC-106 approved vocabulary; the earlier draft's `extends` edge is retired with the rejected term.)

### 8.3 Relationship vocabulary — approved (DEC-106)

The relationship vocabulary is locked as of 2026-08-29. The authoritative copy now lives in `00_architecture/relationship_vocabulary.md`. It replaces software-style terms such as `extends`, `implements`, and `constrains`:

| Proposed relationship | Direction | Meaning |
|---|---|---|
| `requires` | Rule → prerequisite rule | The source cannot function without the target. |
| `uses` | Rule → procedure | The source resolves through or invokes the target. |
| `grants` | Source → rule element / access | The source gives access, a Feature, a Rank, a Trait, or stated capability. |
| `modifies` | Source → baseline procedure | The source explicitly changes a stated baseline part in its own scope. |
| `limits` | Source → affected rule | The source restricts or prohibits target use. |
| `tests` | Experiment / research → rule | The source validates, calibrates, or stress-tests target. |
| `replaces` | New → historical | The source supersedes target. |
| `contains` | Parent → child | Structural placement only. |
| `related` | Either direction | Informational association only. |

This table is approved as DEC-106 (2026-08-29); see `relationship_vocabulary.md` for the authoritative copy.

### 8.4 Directional principle

```text
Canonical procedures have one-way ownership.

A core procedure does not depend on future Classes, Feats, Spells,
or equipment content.

Content may require, implement, or extend a framework procedure.

The registry can show both incoming and outgoing edges without creating
bidirectional rule ownership.
```

---

## 9. Generated Views

Scripts should use the registry to create human-facing views. Generated files are not edited manually.

| Generated output | Use |
|---|---|
| `architecture_index.md` | Searchable table of all active nodes, owners, status, and paths. |
| Subsystem dependency tables | See requires, extensions, validation, and impact by framework area. |
| Change-impact report | List direct and indirect dependents of a changed node. |
| Mermaid diagrams | Focused diagrams for a single framework area or cross-system loop. |
| Graphviz export | Optional full-network visualization; not the primary reading view. |
| Completeness report | Detect dangling edges, missing paths, missing status, unresolved nodes, or duplicate owners. |
| Publication build manifest | Order active specifications into a future Core Rules, GM Guide, or quick reference target. |

### Mermaid policy

```text
Mermaid is a generated focused-view format.

Use it for individual subsystem diagrams and gameplay loops.

Do not treat a project-wide Mermaid graph as the primary relationship map;
it becomes unreadable as the network grows.
```

Suggested focused diagrams:

```text
core-engine.mmd
actor-framework.mmd
adventure-framework.mmd
conflict-framework.mmd
magic-framework.mmd
equipment-framework.mmd
resource-interactions.mmd
combat-exchange.mmd
character-advancement.mmd
spellcasting-flow.mmd
```

---

## 10. Cross-Reference and Link Policy

The rewrite uses aggressive, precise Markdown linking as a navigation and maintenance discipline. A link is not merely a citation; it identifies the exact active rule a reader should consult.

### Required linking practice

```text
When a canonical rule refers to a complete procedure owned elsewhere,
link the first meaningful mention to the exact target section.

When a term has a canonical definition and the reader needs that definition
to understand the current procedure, link it to the glossary or owner.

When a document refers to a decision, research artifact, workflow, or
experiment, link the exact record rather than a directory or vague file.
```

Examples:

```markdown
A successful [Deflect](../04_conflict_framework/02_deflect-and-evasion.md#deflect)
spends [Stamina](../02_actor_framework/03_resources.md#stamina).

See [DEC-103 — Exception-Based Rule Hierarchy](../../02_decisions/active/DEC-103-exception-based-rule-hierarchy.md).
```

### Link boundaries

```text
Link to the canonical owner for the complete procedure.

Do not duplicate that procedure merely because it is linked.

Use a short operational reminder only where it prevents harmful page-flipping.

Do not link every repeated occurrence of a word in one paragraph; link the
first meaningful occurrence, then use the defined term consistently.

Do not treat a research link as a canonical rule source.
```

### Stable target policy

The new framework should use stable explicit anchors for major procedures and concepts rather than relying only on auto-generated heading slugs that can change during editing. For example:

```markdown
## Stamina <a id="resource-stamina"></a>

[Stamina](../02_actor_framework/03_resources.md#resource-stamina)
```

The exact rendering convention can be tested during migration, but every registered canonical node should have one stable link target.

### Relationship-map role

Markdown links and the relationship registry serve different jobs:

| Tool | What it establishes |
|---|---|
| Markdown link | A reader-facing path to a relevant exact source. |
| Registry relationship | The formal semantic relationship: requires, uses, grants, modifies, limits, tests, replaces, contains, or related. |

A parser can automatically collect Markdown links into a useful **reference graph**, generate backlinks, identify broken targets, and suggest registry relationships. It cannot reliably infer whether a prose link means `requires`, `uses`, `modifies`, or merely `related`. The YAML registry therefore remains the source of truth for semantic relationships.

### Generated link checks

The validation workflow should check:

```text
Every relative Markdown link resolves to an existing active file.

Every anchor target resolves.

No active canonical document links to an archived rule as authority.

Every canonical registry node has a stable link target.

Registry relationships and prose links do not contradict one another.
```

## 11. Validation Rules

The registry-validation script should eventually enforce:

```text
Every active canonical node has one unique path.

Every referenced node exists.

Every file path exists.

Every relationship uses the controlled vocabulary.

Every active canonical node has Status and framework placement.

`requires` relationships among canonical framework nodes do not form
an unexplained cycle.

Archived nodes are not prerequisites for active canonical nodes.

Research and experiments cannot become canonical dependencies.

A content entry may extend an interface but may not redefine a baseline
procedure without a decision record and owner update.
```

These are design-maintenance checks, not game-mechanics checks.

---

## 12. Decision Record Model

Retain a concise searchable Decision Index, but use full Decision Records for architecture-changing choices.

```text
# DEC-### — [Decision title]

Status
Context
Decision drivers
Considered options
Decision outcome
Consequences
Confirmation / validation
Supersedes / superseded by
Related nodes
```

### Use a full record when a decision changes

```text
Core resolution.
Subsystem boundaries.
Cross-cutting concepts.
Resource roles.
Character advancement architecture.
Terminology.
Repository organization or migration.
A rule with many downstream content consequences.
```

Small copy edits, catalogue entries, or local content values do not need a full record.

---

## 13. Migration Approach

### Phase 0 — Approve the model

```text
Do not move files yet.
Confirm the framework spine, document types, registry approach,
relationship vocabulary, and archive policy.
```

### Phase 1 — Freeze and archive the current repository

```text
Rename the current root to a dated sibling archive, for example:

  /home/user/ttrpg_idealization
    → /home/user/ttrpg_idealization_pre_reorganization_archive_YYYY-MM-DD

Then create a fresh `/home/user/ttrpg_idealization` root.

Do not delete the archived root. Record the archive path, snapshot date,
and manifest checksum / inventory in the new root’s `99_archive/README.md`.
```

### Phase 2 — Create the empty framework architecture

```text
Create the target directories.
Create the registry schema, migration manifest, decision index,
and architecture-map skeleton.
No rule text is rewritten yet.
```

### Phase 3 — Inventory and classify every active document

For every pre-reorganization file, record:

| Old path | Current authority | New type | New node / destination | Action |
|---|---|---|---|---|
| Old canonical rule | Canonical | Specification | Named framework owner | Rewrite / migrate |
| Decision log entry | Decision | Decision Record / Index | `02_decisions/` | Migrate / retain |
| Probability model | Research | Research | `04_research/` | Retain / relink |
| Triel conversion | Experiment | Experiment | `05_experiments/` | Retain / relink |
| Historical draft | Historical | Archive | `99_archive/` | Archive only |

### Phase 4 — Rewrite the framework one spine section at a time

Recommended order:

```text
00 Architecture map and vocabulary
01 Core Engine
02 Actor Framework
04 Conflict Framework
03 Adventure Framework
05 Magic Framework
06 Equipment Framework
07 World / GM Framework
08 Framework Reference
```

For each section:

```text
Extract current rules from the archived snapshot.
Write one clean canonical specification per owner.
Register nodes and edges.
Link relevant decisions and research.
List open definitions explicitly.
Generate and inspect relationship views.
Run consistency audit before moving to the next section.
```

### Phase 5 — Reclassify research, workflows, experiments, and content

```text
Move or copy only after the new canonical owners are stable.
Mark every retained old document as historical, research, experiment,
or workflow; none may silently remain pseudo-canonical.
```

### Phase 6 — Build publication drafts later

```text
Generate reader-facing Core Rules / GM Guide outlines from registry metadata.
Do not make publication drafts canonical while the framework is active.
```

---

## 14. Migration Success Criteria

The reorganization is successful only when:

```text
Every active core procedure has exactly one canonical owner.

Every active canonical node appears in the registry.

Every formal cross-system relationship is represented in the registry.

The architecture index and focused diagrams generate successfully.

No active rule requires an archived file.

Research cannot be mistaken for canon.

Every open issue appears either in the relevant specification or in
an active risk / outstanding-definition view.

A human or agent can identify the rule owner, dependencies, impact,
status, and relevant decision record without reading archive history.
```

---

## 15. Decisions Still Needed Before Migration

1. ~~Approve, revise, or reject the proposed registry relationship vocabulary in Section 8.3.~~ **Resolved — DEC-106 (2026-08-29):** all nine terms approved unchanged.
2. Decide which existing documents should become the initial Framework Architecture Map, versus being preserved only in the sibling archive. *(Partially resolved — DEC-107 populates the map from the archived pillars/canon by pointer; full resolution as rule areas migrate.)*
3. Decide which existing major decisions require a full Decision Record during early migration.
4. ~~Decide which minimal framework subsection is stable enough to migrate first after the architecture skeleton is created.~~ **Resolved — DEC-107 (2026-08-29):** the architecture map + registry seed migrate first; 01 Core Engine is next.
5. ~~Test and approve the exact stable-anchor syntax in the target Markdown renderer before broad migration.~~ **Resolved — DEC-108 (2026-09-18):** validated in VS Code's built-in Markdown preview; DEC-104 confirmed unchanged.
6. Decide whether generated outputs are ignored by version control, locally cached, or published only in selected release builds.
