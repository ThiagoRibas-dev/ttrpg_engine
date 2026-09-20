# Craft, Downtime, Materials, Workshops, and Repair — Research Draft

**Status:** Research and design draft; non-canonical.  
**Purpose:** Compare crafting and repair models from relevant RPGs and propose a low-arithmetic Craft framework compatible with the established Activity procedure, separate Craft specialty ranks, Equipment Durability, and project boundary.

This document does not establish a Craft, repair, material, workshop, downtime, project, batch, or success-level rule.

## 1. Design Inputs Already Settled

```text
Craft specialties:
  Alchemy
  Armorsmithing
  Cooking
  Engineering
  Jewelcrafting
  Leatherworking
  Tailoring
  Weaponsmithing

Each Craft specialty:
  Has its own Competency Rank.

Activity default:
  One primary Skill check.
  Specific Activity states Requirements, tools, cost/time,
  resolution, success, failure, and Tags.

Materials:
  Hybrid model preferred.
  Ordinary materials may be abstract.
  Exceptional materials are named.

Workshop tiers:
  Desired.

Projects:
  Desired as long-duration/batch activities with only a few
  consequential rolls rather than a roll for every produced item.
```

## 2. Reference-System Patterns

| System | Craft pattern | Repair pattern | Useful lesson | Avoid importing |
|---|---|---|---|---|
| D&D 3.5e | Pay materials; make daily/weekly Craft checks; check × DC creates numerical progress | Same DC as creation; repair cost based on item price | Separate specialty, tools, materials, complexity, and repair type | Progress arithmetic, repeated weekly rolls, price-driven time |
| Pathfinder 2e | Supply materials; spend setup time; Craft check; pay remainder or spend downtime to reduce it; batch consumables | Ten-minute Repair with toolkit, check, stated item recovery | Item formula, rank, tools, material, and downtime are distinct Requirements | Currency arithmetic and full degrees-of-success structure |
| PF1e Unchained alternate Craft | Complexity category determines time; one check after the interval | Complexity determines repair time | Complexity/time is more intuitive than market-price progress | Exact DC tables and recurring arithmetic |
| Starfinder | Skill rank gates item level; materials, tools, workshop, and time are required | Crafted items can receive repair advantages | Rank gate plus recipe/workshop requirements cleanly express capability | Detailed price/UPB accounting unless campaign needs it |
| Forbidden Lands / Year Zero | Craft/repair uses a discrete skill roll; advanced items require specialization; repair restores item reliability | A successful roll restores a discrete gear value | One meaningful roll after time is fast and readable | Routine gear degradation and destructive repair failure if not desired |
| Blades in the Dark | Long-term projects use clocks; crafting can be a specific downtime outcome | Projects and formulas are distinct from ordinary items | A project abstraction can replace repeated production rolls | Narrative clocks if they do not fit the simulationist presentation |

## 3. Recommended Craft Activity Families

### A. Improvised work

```text
Use when:
  A character makes a simple expedient object, meal, field repair,
  shelter adjustment, or similar low-stakes work.

Specialty:
  Not required if the Activity explicitly permits improvised work.

Tools:
  Improvised or Helpful as stated.

Resolution:
  One primary Activity check if uncertainty matters.

Output:
  Temporary, limited, or fiction-defined.
```

### B. Standard recipe or item

```text
Use when:
  A character creates a defined ordinary item, batch, meal,
  alchemical product, repair, garment, weapon, or armor piece.

Specialty:
  Required as stated by the recipe or item.

Requirements:
  Recipe/plan, materials, tools, workshop tier, Rank, and downtime interval.

Resolution:
  One check after the stated interval.

Output:
  The stated item or batch.
```

### C. Project Downtime Activity

```text
Use when:
  A character spends extended downtime on a large order,
  construction project, complex item, masterwork work, research,
  large batch, workshop improvement, or other multi-interval task.

Requirements:
  Project entry defines specialty, Rank, materials, workshop,
  intervals, assistants, and output.

Procedure:
  Spend the listed downtime intervals.
  Make only the stated consequential check or checks.
  The project entry defines output, delay, material loss, quality,
  or other outcome.
```

This supports the desired “long time, few consequential rolls” approach.

## 4. Workshop Tiers — Draft Model

| Tier | Fictional examples | Draft role |
|---|---|---|
| Improvised | Campfire, borrowed table, scavenged tools | Permits only Activities that explicitly allow improvised work; may impose Circumstance Bane |
| Portable | Artisan tools, healer’s kit, thieves’ tools, travel alchemy kit | Supports field work, simple repair, and portable recipes |
| Standard | Forge, kitchen, alchemy lab, tailor’s bench, leatherworker station | Required for ordinary professional production or repair as stated |
| Specialized | Siege forge, gem-cutting studio, advanced laboratory, shipyard, magical workshop | Required for complex, high-Rank, masterwork, unusual-material, or project-scale work |

A workshop Tier should normally be a **Requirement or Permission**, not a generic numerical modifier. A specific workspace can grant an Enhancement Boon, reduced time, or expanded output when its rule says so.

## 5. Hybrid Materials Model

| Material type | Tracking approach | Examples |
|---|---|---|
| Ordinary | Abstract material units stated by recipe/project | Metal, timber, leather, cloth, reagents, food supplies |
| Exceptional | Named material or component | Adamantine, dragon scale, rare herb, venom gland, celestial feather |
| Magical | Named component, formula, ritual, Tradition, or special workshop Requirement | Enchanted core, rune ink, soul crystal, divine relic |

The recipe or project states the material type and quantity. The system does not require universal gold-piece-to-progress arithmetic.

## 6. Repair Models for Evaluation

### Model A — Fixed repair output

```text
Repair entry states:
  Craft specialty.
  Tools/workshop.
  Time.
  Difficulty Vector.
  Fixed Durability restored on success.
```

**Pros:** Fast, predictable, easy to calibrate.  
**Cons:** Item entries need a repair value.

### Model B — Rank-based repair output

```text
Success restores Durability based on the relevant Craft Rank.
```

**Pros:** Rank visibly improves repair.  
**Cons:** Creates a universal progression formula and may trivialize low-Durability items at high rank.

### Model C — Item-state repair

```text
A successful repair restores an item from nonfunctional to functional.
Further repair requires another specific procedure or downtime.
```

**Pros:** Very simple; fits current minimal Durability scope.  
**Cons:** Less granular if Durability becomes strategically important.

### Model D — Project repair

```text
Simple field repair:
  One standard Repair Activity.

Major / magical / destroyed repair:
  Project Downtime Activity.
```

**Pros:** Scales naturally and keeps exceptional repairs exceptional.  
**Cons:** Requires each item/project to classify repair scope.

## 7. Recommended Hybrid Procedure

```text
Ordinary item creation or repair:
  Standard recipe/item Activity.
  One check after a stated downtime interval.

Improvised work:
  Allowed only when the Activity says so.
  Usually temporary or limited.

Large orders, masterwork work, unusual materials,
magical items, structures, and major repairs:
  Project Downtime Activity.
  Spend stated intervals, then make only the stated
  consequential check or checks.

Workshop:
  Requirement / Permission tier.

Materials:
  Ordinary abstract units; exceptional named components.
```

For current minimal Durability scope, **Model D** was recommended and is now represented by the canonical repair baseline:

```text
Ordinary repair:
  Repair Activity restores the amount stated by the item.

0-Durability / nonfunctional item:
  Its item entry states whether ordinary Repair can restore it
  or whether it requires a Project Downtime Activity.
```

## 8. Success Levels and Project Outcomes

The current universal resolution engine resolves success/failure through Difficulty Vectors. It does not yet define a universal success-level or degree-of-success procedure.

Therefore, a Project cannot yet rely on unspecified “success levels” as a global rule.

Two compatible future approaches:

| Approach | Procedure |
|---|---|
| Project-defined outcomes | The project entry defines what ordinary success, specified multi-threshold success, or failure produces |
| Explicit project stages | The project lists a small number of stages, each with its own check and output |

Recommended current boundary:

```text
Do not create universal Craft success levels.

A specific project may define:
  multiple thresholds;
  stages;
  batch output;
  quality tiers;
  material loss;
  reduced time;
  or other outcomes.
```

## 9. Project / Recipe Template

```text
Name:
Category: improvised work / standard recipe / project
Relevant Craft Specialty:
Minimum Rank:
Plan, recipe, or formula:
Materials:
Tools:
Workshop Tier:
Downtime interval or project intervals:
Difficulty Vector / opposed check:
Assistance:
Success:
Failure:
Output / batch:
Repair interaction:
Tags:
Special requirements or permissions:
```

## 10. Decisions Needed Before Canonization

1. Is the three-family Craft model—Improvised, Standard, Project—accepted?
2. Are the four workshop tiers accepted?
3. Is the ordinary/exceptional hybrid material model accepted?
4. Which repair model applies to current Durability points?
5. What is the standard downtime interval vocabulary: minutes, hours, days, weeks, and project-defined intervals?
6. Should recipes require a plan/formula by default, or only for complex/specialized work?
7. Do project outcomes use project-defined multi-threshold results, explicit stages, or both?

## 11. Reference Notes

- D&D 3.5e Craft: materials, tools, daily/weekly progress, repair: [1](https://www.dandwiki.com/wiki/3e_SRD:Craft_Skill)
- PF2e Crafting and Repair: materials, setup, formulas, downtime, tools: [1](https://2e.aonprd.com/Skills.aspx?ID=37&Redirected=1)
- PF1e alternate Craft: complexity/time alternative: [4](https://legacy.aonprd.com/unchained/skillsAndOptions/craftingAndProfession.html)
- Starfinder: rank, tools, workshop, materials, time: [4](https://aonsrd.com/Rules.aspx?ID=92)
- Forbidden Lands: discrete Craft/repair roll and specialty requirements: [3](https://anyflip.com/sctrd/ymcf/basic/51-100)
- Blades in the Dark: long-term project structure: [5](https://keeper.farirpgs.com/resources/one-seven-design/blades-in-the-dark/crafting/)
