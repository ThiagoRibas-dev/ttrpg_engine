---
turn: 321
role: "AI-Designer"
source: chat_history.json
---

# Turn 321 — AI-Designer

used
Bash
909ms

Created the revised probability-band table and chart using:

text
Easy:   80–85%
Medium: 60–65%
Hard:   40–45%
Table
text
02_comparative_system_analysis/13_probability_band_calibration.md
Chart
text
02_comparative_system_analysis/13_probability_band_calibration.png
Script
text
06_brainstorming_logs_and_roadmap/sim_band_calibration.py

The table searches for the closest DC X (R) combination at each level, preferring combinations inside the requested probability band. Cells outside the band are marked (nearest).

This is already much more workable than the previous 85/65/55 targets. Several levels now achieve the desired bands exactly or nearly exactly through Required Successes, especially:

text
Level 5:
  Easy: DC 6 (1) → 84.74%
  Hard: DC 8 (1) → 41.38%

Levels 13–16:
  Easy: DC 9 (1) → 83.22%
  Hard: DC 12 (2) → 41.54%

Levels 17–18:
  Easy: DC 11 (1) → 80.62%

Medium remains the most difficult band to hit consistently because the available DC X (R) grid often jumps from the high 50s to the high 60s. That is useful data for the next calibration discussion.
