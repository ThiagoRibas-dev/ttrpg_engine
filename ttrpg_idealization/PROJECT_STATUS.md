# Project Status — Framework Rewrite

**Current phase:** Phase 4 — case-by-case framework migration (reorg model §13).  
**Current operation:** Core Engine migration **complete** (Batches 1–5). Next migration area: 02 Actor Framework.

## Active state

All five Core Engine specifications are live under `01_framework/01_core_engine/`: `01_checks_and_dice_pools.md`, `02_difficulty_and_target_numbers.md`, `03_boons_banes_and_die_steps.md`, `04_opposed_checks_and_automatic_successes.md`, and `05_engine_boundaries.md`, plus the first research artifact, `04_research/probability_and_calibration/tier_difficulty_vector_reference.md` (calibration data, DEC-109), and the entry-format template under `03_workflows/content_templates/`. Archived mechanics remain non-canonical until individually migrated.

## Remote repository

Since 2026-09-19 the project lives in a public git repository: `https://github.com/ThiagoRibas-dev/ttrpg_engine`. Both trees (active root and pre-reorganization archive) were moved into it as siblings, preserving every relative archive link. Publishing procedure, credential handling, and the clone-without-archive command: [AGENTS.md — Git publishing](AGENTS.md). Uploaded reference files stay out of the repo and are incorporated case-by-case.

## Completed reorganization phases

### Phase 1 — Archive snapshot (2026-08-07)

The complete prior root was renamed and preserved at:

```text
/home/user/ttrpg_idealization_pre_reorganization_archive_2026-08-07/
```

Location note (2026-09-19): the archive has since moved into the git repository as a sibling of the active root — see [Remote repository](#remote-repository).

### Phase 2 — Fresh architecture scaffold (2026-08-07)

Framework Spine directories, YAML registry skeleton, architecture-map skeleton, migration manifest, generated-view policy, continuing master decision log, and directory boundaries.

### Phase 4 (first target) — Architecture map and vocabulary (2026-08-29)

- **DEC-106:** nine-term registry relationship vocabulary approved; software terms rejected.
- **DEC-107:** architecture map populated from archived canon; registry seeded.

### Phase 4 (continued) — stable-anchor validation (2026-09-18)

**DEC-108:** DEC-104 anchor syntax validated in VS Code's built-in Markdown preview. `<a id>` heading anchors, auto-slugs, `{#id}` attributes, cross-file `path#anchor` links, and bare anchors all pass; legacy `<a name>` fails and is rejected. Test retained as regression check.

### Phase 4 (continued) — Core Engine Batches 1–4 (2026-09-18/20)

**DEC-109:** five-batch Core Engine plan approved (checks/pools → difficulty → boons/banes/steps → opposed/automatic → boundaries); difficulty tables split to `04_research/`; specs own their definitions inline.

- **Batch 1:** `01_checks_and_dice_pools.md` — locked spec, registry node `core.checks-and-pools`, DEC-102 terminology applied with in-spec note, open definitions listed. Re-voiced per DEC-110/111.
- **Batch 2:** `02_difficulty_and_target_numbers.md` — locked spec (DC scale, vectors, check modes from archived §4 + 08); `13_tier_difficulty_vector_reference.md` relocated to `04_research/` with its dual canonical/research status reduced to research calibration (flagged in manifest); registry nodes `core.difficulty-and-target-numbers` and `research.tier-difficulty-vectors`, with the first `uses` and `tests` edges.
- **Batch 3:** `03_boons_banes_and_die_steps.md` — locked spec (final-pool timing, cancellation, typed stacking, Boon/Bane effects with the one-die `d4` auto-failure chain, Die Step ordering); archived glossary Boon/Bane entries cross-checked consistent. Amended on review by **DEC-112**: notation canonized as `+1B`/`-1B` (source `+1X` collision resolved) and Purpose/Die Steps prose rewritten per user-supplied text. Registry node `core.boons-banes-and-die-steps` + `uses` edge to checks-and-pools.
- **Batch 4:** `04_opposed_checks_and_automatic_successes.md` — locked spec (six-step opposed procedure, defender wins ties, neutral contests; Automatic Successes with timing, properties, and pre-roll opposed comparison); archived glossary entry cross-checked; DEC-102 applied (two "Permission" grants → Exceptions, in-spec note); open definitions: undefined `DC 9 (3)` shorthand flagged, surplus Automatic Successes effect unstated. Registry node `core.opposed-and-automatic-successes` + `uses` edge to checks-and-pools.
- **Batch 5:** `05_engine_boundaries.md` — locked boundary spec (Requirement/Access/Exception vocabulary with DEC-102 translation of the source's "Permission" examples, flagged for review; multi-success principle; complex-check boundary to the Conflict layer; related-owners list translated to four `related` edges). Entry Format Template created (`03_workflows/content_templates/entry_format_template.md`, DEC-103 fields). Registry node `core.engine-boundaries`; **area `core-engine` marked complete.**

### Phase 4 (milestone) — Core Engine complete (2026-10-18)

All five batches of the Core Engine are migrated, registered, and reviewed. The engine's procedures (checks, difficulty, boons/banes/steps, opposed/automatic) and its boundary vocabulary are canonical in the fresh root.

### Phase 4 (continued) — prose voice (2026-09-19/20)

**DEC-110:** house prose voice adopted for all framework prose and project communication — warm plain English modeled on the D&D 3.5e PHB introduction, with an explicit AI-ism ban list. Standard: `03_workflows/content_templates/voice_and_style_guide.md`.

**DEC-111:** voice refined — each claim is stated once and shown once with a concrete example; no restatement, no nested parenthetical re-statements.

**DEC-112:** Boon/Bane check notation canonized as `+1B` / `-1B`.

## Next operation

**02 Actor Framework migration** (reorg model §13 Phase 4 order): batch plan to be proposed from the archived sources — attributes and derived statistics (`02_attributes_and_derived_statistics.md`), leveling and tier progression (DEC-095/100), skills and Competency Ranks, and the actor-creation schema. The user will approve the batching before extraction begins, as with the Core Engine (DEC-109 pattern).

## Open decisions still needed

See reorg model §15 items 2 (partial), 3, 6.
