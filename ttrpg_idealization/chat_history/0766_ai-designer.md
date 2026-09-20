# AI Designer — 0766

Confirmed the user's nuance and recorded the voice ruling as **DEC-110 — Framework Prose Voice, Warm Plain English** (2026-09-19): the D&D 3.5e PHB-introduction voice applies to all framework prose *and* project communication (chat replies, reports), while scaffolding (status lines, scope tables, registry data, decision rows) stays clinical. Banned as AI-isms: unnecessary contrasts ("not just X — Y," "zero X"), rule-of-three abuse, punchy taglines and puns, grandiose metaphors, em-dash flourish cadence as default rhythm, synthetic slang.

Created `03_workflows/content_templates/voice_and_style_guide.md` (durable standard: the voice rules, the ban list, the user's do/don't example, enforcement note) and activated the content_templates README.

Re-voiced the Batch 1 specification (`01_checks_and_dice_pools.md`): PHB-style Purpose and procedure prose, one "Important: you don't need to memorize this" mercy aside, concrete examples at first contact. All rules, steps, anchors, links, and the DEC-102 terminology note preserved; header carries a DEC-110 voice provenance line. Updated `PROJECT_STATUS.md` with the DEC-110 section.

Validation: full pass, including an automated AI-ism scan (with the style guide's own quoted examples excluded by design) and an em-dash discipline check — first run flagged 12 em-dashes; reduced to 4 genuine parenthetical asides by switching the rest to colons and parentheses. Decision log clean through DEC-110; chat history through 0765. Spec re-presented to the user.
