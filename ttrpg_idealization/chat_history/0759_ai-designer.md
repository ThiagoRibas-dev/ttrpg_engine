# AI Designer — 0759

Answered the batching question by scoping the archived sources first (`01_resolution_engine.md` 221 lines / 11 sections; 08 boundary doc; 13 probability tables; glossary), then proposing a five-batch plan. User approved all three decision points (recorded as **DEC-109 — Core Engine Migration Batching and Scope**): (1) five batches with review between each; (2) difficulty material split — 08's vector definitions join Batch 2, 13's tables go to `04_research/` as calibration reference; (3) specs own their vocabulary definitions inline, aggregated glossary later in 08 Reference.

Executed **Batch 1** in the same turn:
- New canonical spec `01_framework/01_core_engine/01_checks_and_dice_pools.md` — spec-template structure (Purpose/Scope/Procedure/State/Interactions/Open defs/References), 12 stable anchors, faithful extraction of source §1–2 (10-step procedure, die ladder, base check 2dX keep-highest, Natural/Enhanced pool definitions, pool-range guideline). DEC-102 applied transparently: step 10 "Permission" → "granted capability" with an in-spec terminology note; no unflagged deprecated terms. Cross-reference debt and 4 open definitions recorded in-spec (Exert owner TBD; source §3 numbering skip; pool-range guideline boundary).
- Registry: node `core.checks-and-pools` (locked, publication order 10), `contains` edge from `area.core-engine`; area status planned → in-progress; registry status → active (12 nodes / 10 edges).
- Manifest: Batch 1 row (migrated) + planned rows for Batches 2–5 and the 13-tables research move.
- `01_core_engine/README.md`: batch table with statuses. `PROJECT_STATUS.md`, architecture map (spine row + §10) updated.

Validation (python3, code-fence-aware link check): 19-point pass after one miscalibrated check was corrected — the "stray Permission" check expected a single occurrence, but the deprecation note legitimately names the term three times; verified all occurrences live inside the flagged note. No file changes needed for that. All links resolve across every active file; anchors resolve; log sequence 1..109 clean. Spec presented to user.
