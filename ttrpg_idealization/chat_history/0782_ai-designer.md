# AI Designer — 0782

Executed **Core Engine Batch 3 — Boons, Banes, and Die Steps** (DEC-109 plan; user-approved this turn).

Re-read the archived source fresh (`01_resolution_engine.md` §5–6) rather than trusting memory, and cross-checked the archived glossary's Boon/Bane entries against it (consistent; noted in-spec). Wrote `01_framework/01_core_engine/03_boons_banes_and_die_steps.md` in the DEC-110/111 voice: final-pool timing, cancellation, the five typed-stacking categories with all four stacking rules (same-type, different-type, Untyped, same-source), Boon adds a die, Bane removes one with the one-die-pool Step-Down and `d4` automatic-failure chain, Die Step-Up/Down with ordering-before-Boons/Banes, `d12` ceiling with the Exert exception, and the `d4` floor rules. New worked example for typed stacking (pinned enemy + high ground vs. war chant), consistent with the rules.

Flagged, not silently changed: the source's notation collision (`X` = Bane marker in `+1X` but die-size variable in `2dX`) — recorded as an open definition.

Wiring: registry node `core.boons-banes-and-die-steps` (15 nodes / 15 edges now; new `uses` edge to checks-and-pools); manifest Batch 3 row (Batch 4 marked next); Core Engine README table; PROJECT_STATUS; architecture map spine row and §10; cross-links from Batch 1 (both mentions) and Batch 2 (its Rule Interactions mention — the first edit attempt targeted the wrong line and failed cleanly; corrected to the actual wording).

Validation: 27-check pass plus manual confirmation of the 28th (case-sensitive check string vs. "Final-Pool Effects" heading; content present). Voice clean (3 em-dashes, no banned patterns, no deprecated terms); all links and anchors resolve; layering rule holds (no `requires` from core specs).

Committed locally as "Core Engine Batch 3: boons, banes, and die steps" — **not pushed**: presented to the user for review first, per the agreed batch workflow.
