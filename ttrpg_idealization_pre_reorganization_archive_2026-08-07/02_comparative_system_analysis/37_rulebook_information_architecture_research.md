# Rulebook Information Architecture Research

**Status:** Research / reorganization-preparation artifact; non-canonical.  
**Purpose:** Identify proven rulebook organization and reference-design patterns before archiving and rewriting the project documentation. This does not yet move, archive, rewrite, or alter any rules.

## 1. Research Question

The project has accumulated framework, research, conversion, decision, and content-modeling material across many files. The next documentation architecture should accomplish two different jobs:

```text
Learn:
  A new reader can understand the game from first principles
  in a natural play-oriented order.

Look up:
  A player, GM, designer, or future agent can find an exact
  rule, definition, ownership record, or historical decision quickly.
```

A strong rulebook cannot optimize one job by sacrificing the other. The best recurring pattern is a readable main sequence plus separate reference tools.

## 2. Research Examples

### Pathfinder 2e Remaster: role-based core books and navigable complexity

**Observed pattern**

- Separate Player Core, GM Core, and Monster Core divide reader roles instead of placing all material in one enormous general book.
- Clear sections, broad index, navigation aids, and consistent repeated content templates reduce the perceived burden of a complex ruleset.
- The GM book is organized as a usable preparation-and-play toolbox rather than pure theory.

**Transferable lesson**

```text
Separate player-facing rules, GM procedures, and content catalogues.

A complex framework can remain usable when every rule has one clear owner,
repeated entry formats, predictable chapter placement, and strong navigation.
```

**Caution**

Do not scatter a procedure across role books merely to preserve a division. A player needs all ordinary player-facing consequences in the Player book; a GM needs complete adjudication procedure in the GM book.

### Ironsworn / Starforged: primer first, deep dive second, reference separate

**Observed pattern**

- A quick, visual, complete rules primer teaches the game loop before detailed constituent chapters.
- The book repeatedly exposes its own structure through a detailed table of contents, chapter summaries, diagrams, examples, icons, and page-specific cross-references.
- A separate reference guide holds at-table moves, procedures, and generators.

**Transferable lesson**

```text
Teach the complete gameplay loop early.

Then explain each subsystem in depth.

Publish a separate at-table reference that can be used without reopening
hundreds of pages of explanatory prose.
```

**Caution**

A primer must be genuinely complete for ordinary play, not a marketing overview that forces immediate cross-reference.

### Mothership: sheet-as-instruction and information density

**Observed pattern**

- The character sheet itself teaches character creation and exposes the information needed to play.
- The Player’s Survival Guide uses dense but deliberate layouts, inside-cover reference material, visual relationships, and short linked rules.

**Transferable lesson**

```text
The character sheet, class table, spell record, item card, and reference page
are part of the rules interface—not merely data containers.

Make the most frequently used procedure visible where it is used.
```

**Caution**

Excellent print layout is not sufficient for a digital document. One review specifically notes that a lack of PDF bookmarks and hyperlinks made an otherwise excellent dense document difficult to navigate digitally.

### Old-School Essentials and Mausritter: spread-contained reference

**Observed pattern**

- Community discussion repeatedly identifies their compact presentation, two-page-spread containment, and high table usability as strengths.
- A topic’s procedure, exceptions, and examples are kept together instead of split across distant chapters.

**Transferable lesson**

```text
Design each common procedure to fit within one bounded reference unit:
a spread, a screen panel, a one-page handout, or a digital section.

Do not require an ordinary combat, spell, or Activity procedure to bounce
across multiple owners during play.
```

**Caution**

Spread containment is an editorial objective, not an excuse to omit needed explanation or shrink text excessively.

### Dragonbane: procedural flow and visual readability

**Observed pattern**

- Character creation and basic procedures flow step by step.
- Concise chapters, readable typography, action charts, cards, and a compact scope support fast onboarding.

**Transferable lesson**

```text
Order instruction in the order a reader builds and uses a character:
concept → sheet → core check → turn → consequences → recovery → advancement.

Use tables and visual procedure summaries for repeated play loops.
```

**Caution**

A positive visual flow does not guarantee complete reference organization. Reviews also note some rules being scattered; therefore, every rewrite must be audited for duplicated or split ownership.

### GURPS and old D&D 4e: redundancy can be usability

**Observed pattern**

- Community commentary praises GURPS for repeating relevant rules where they are used.
- D&D 4e-era products are often praised for finding rules quickly and for structured entries.

**Transferable lesson**

```text
Single-source ownership does not prohibit concise operational reminders.

Keep the complete rule in one owner, but repeat a short “use this rule now”
reference in a dependent procedure when it eliminates harmful page-flipping.
```

**Caution**

Repeated text must be clearly marked as a summary / cross-reference and checked during updates. Do not create two independently editable authoritative procedures.

## 3. Common Rulebook Architecture Pattern

Across conventional Player Handbooks, GM Guides, and highly usable indie books, a durable learning order is:

```text
1. What this game is / play agenda / required materials.
2. Quickstart: the full gameplay loop in miniature.
3. Core vocabulary and resolution.
4. Character creation, in sheet order.
5. Ordinary play procedures: exploration, social, downtime, Activities.
6. Encounter and combat procedure.
7. Consequences, Conditions, Wounds, recovery, and rest.
8. Advancement, Classes, Feats, Skills, and magic access.
9. Equipment, crafting, and campaign logistics.
10. Player-facing reference tables and glossary.

Separate GM material:
  adjudication, Difficulty setting, encounter building, creatures,
  treasure / rewards, campaign procedures, and optional content tools.

Separate content catalogues:
  Classes, Feats, Spells, equipment, creatures, ancestries, adventures.

Separate design / developer material:
  decisions, research, probability, conversion, implementation notes,
  and archive history.
```

The exact order must be adapted to the project’s gameplay loop; it should not imitate a traditional book merely by habit.

## 4. Organization Principles for the Rewrite

### A. Rulebook order is not repository order

A repository needs both a **reader-facing order** and a **maintenance order**.

| Need | Best structure |
|---|---|
| A new player learning the game | Player Rulebook sequence. |
| A GM running an encounter | GM procedures and quick-reference material. |
| A designer changing a rule | One canonical owner, decision record, tests, and dependent-reference audit. |
| A future agent recovering context | Governance index, architecture map, decision log, and archive. |
| A content writer creating a spell or Class | Stable templates, canonical interfaces, content catalogues, and conversion references. |

The rewrite should not force all of these audiences through the same directory order.

### B. Distinguish four document types visibly

```text
Rulebook text:
  Player / GM-readable procedures and explanations.

Reference text:
  Tables, glossary, quick procedures, character sheets, indexes.

Development text:
  Research, simulations, design rationale, conversion notes, open questions.

Archive text:
  Superseded documents preserved for history only.
```

The current project has many of these types, but their filenames and directory adjacency do not always make the distinction immediately obvious.

### C. One owner, many signposts

```text
One complete canonical procedure.

Short operational reminder where it is used.

A specific named link to the owner.

A glossary term for search and index.
```

### D. Design for print and digital from the beginning

Every final rulebook / reference release should have:

```text
Detailed linked table of contents.
PDF bookmarks.
Hyperlinked internal cross-references.
Alphabetical index with multiple natural-language entry points.
Glossary.
One-page or two-page quick references.
Sheet / table / card interfaces that expose frequent rules.
```

### E. Separate core procedure from optional complexity

```text
Main procedure:
  The smallest complete rule needed for ordinary play.

Advanced / optional / content-specific material:
  A clearly labeled later section or separate entry.

Historical rationale:
  Development documentation only.
```

This directly supports the project’s low-memory feature policy.

## 5. Candidate Future Publication Set

This is an ideation scaffold, not a decided file plan.

| Publication / repository layer | Reader | Possible contents |
|---|---|---|
| **Core Rules / Player Guide** | Every player and GM | Quickstart, vocabulary, resolution, character creation, Activities, combat basics, Conditions, recovery, advancement, Skills, magic access, equipment basics. |
| **GM Guide** | GM | Difficulty setting, adjudication, encounter / scenario procedures, NPC / monster guidance, rewards, campaign tools, optional procedures. |
| **Reference Guide** | At-table users | Turn sequence, defense sequence, Conditions, maneuvers, recovery, Skill ranks, Tags / Traits, Difficulty tables, indexes. |
| **Content Compendia** | Players and GMs | Classes, Feats, Spells, equipment, creatures, ancestries, recipes, adventures. |
| **Developer Vault** | Designers / agents | Decisions, open definitions, research, simulations, conversion methods, content templates, change log. |
| **Archive** | Historians / recovery only | The full current repository snapshot and later superseded rewrites. |

## 6. Rewrite Success Criteria

Before moving any files, define tests such as:

```text
A new reader can find and understand the first complete gameplay loop
without reading design history.

A player can create a Level 1 character without opening GM material.

A GM can resolve an Attack, a Wound, recovery, and an Activity by following
one procedure each, without hunting through research documents.

A designer can identify the sole owner of every core procedure.

A PDF user can reach every referenced rule through a link, bookmark, table
of contents, or index entry.

No active rule depends on an archived document.
```

## 7. Sources

- Pathfinder Player Core organization commentary: <https://www.goodreads.com/book/show/194925825-pathfinder-rpg>; Player / GM Core navigation discussion: <https://pocgamer.com/archives/2777>
- Ironsworn / Starforged information-architecture discussion: <https://www.reddit.com/r/rpg/comments/15ffgu9/the_ironsworn_rulebooks_are_the_most/>
- Mothership Player’s Survival Guide information-design review: <https://www.rpg.net/reviews/archive/18/18927.phtml>; official presentation notes: <https://www.tuesdayknightgames.com/pages/mothership-rpg>
- Dragonbane layout and instructional-flow review: <https://gamingtrend.com/reviews/dragonbane-rulebook-review-lightweight-but-super-fun/>
- Community examples: Old-School Essentials, Mausritter, GURPS, D&D 4e, and others: <https://www.reddit.com/r/rpg/comments/15i4u87/whats_best_organized_rpg_rulebook_you_have_read/>; <https://www.reddit.com/r/rpg/comments/22e7mk/best_organized_rpg_rulebook/>
- General rulebook organization and indexing discussion: <https://www.reddit.com/r/RPGdesign/comments/1k1jbnv/how_to_organize_the_document_for_my_RPG/>; <https://www.reddit.com/r/rpg/comments/14yl5v0/is_having_an_index_a_must_for_a_core_rulebook/>; <https://www.ttrpg-games.com/blog/formatting-rulebooks-for-homebrew-rpgs>

## 8. Next Research / Design Questions

1. Should the rewrite target a single Core Rules book first, or a Player Guide + GM Guide pair from the start?
2. Which currently canonical material belongs in the ordinary player gameplay loop, and which belongs only in a GM / developer layer?
3. Which parts need a quick-reference counterpart before prose rewriting begins?
4. Which current documents are canonical but historically structured, duplicated, or too detailed for a player-facing rulebook?
5. What archive snapshot and migration manifest are required so no decision history is lost?
