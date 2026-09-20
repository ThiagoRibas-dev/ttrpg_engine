# AI Designer — 0768

Confirmed the user's statement/example principle and recorded it as **DEC-111 — Voice Refinement, Statement and Example**: each claim is stated once and shown once with a concrete example; no restating the same fact in different words; no nested multi-restatement parentheticals; prefer examples that carry the most content per sentence (the user's 4d4 example covers both die-size ceiling and pool-size reliability in one sentence).

Applied it:
- Rewrote the Batch 1 spec's Purpose to the user's supplied text verbatim (removed the "A die showing an 8 is an 8" / "bigger die is a higher ceiling (novice… grandmaster…)" restatements).
- Added a "Statement and example" section to `voice_and_style_guide.md` with the user's don't/do pair; restatement added to the ban list; header references DEC-111.
- Appended DEC-111 to the decision log (refining DEC-110, which stays as recorded — append-only) and added the DEC-111 line to `PROJECT_STATUS.md`'s voice section.

Validation: full pass — user text present verbatim, restated version gone, all rule content/steps/anchors/sections intact, 4d4 example sanity-checked (P(at least one 3+) on 4d4 = 93.75%, so "reliably" is accurate), em-dashes at 4, no banned AI-isms, log clean through DEC-111, links and anchors resolve. Spec re-presented.
