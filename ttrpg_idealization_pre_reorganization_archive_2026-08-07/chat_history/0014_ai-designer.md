---
turn: 14
role: "AI-Designer"
source: chat_history.json
---

# Turn 14 — AI-Designer

Ran commands
3
Write
ttrpg_idealization/06_brainstorming_logs_and_roadmap/sim_boons.py
58 lines
open
sim_boons.py
PYTHON
#!/usr/bin/env python3
"""
Simulate Boons with mixed step dice to test granularity vs redundancy.
"""
import itertools

dice = [4, 6, 8, 10, 12]
dcs = [3, 5, 7, 9, 11]

def get_step_down(d):
    idx = dice.index(d)
    return dice[max(0, idx - 1)]

def get_step_up(d):
    idx = dice.index(d)
    return dice[min(len(dice) - 1, idx + 1)]

def prob_pool(pool, dc):
    if max(pool) < dc:
        return 0.0
    total = 1
    for d in pool:
        total *= d
    successes = sum(1 for roll in itertools.product(*[range(1, d + 1) for d in pool]) if max(roll) >= dc)
    return (successes / total) * 100.0

def main():
    print("=== PROBABILITY OF HITTING TARGET DC (%) ===")
    for base in dice:
        print(f"\n--- Base Die: d{base} ---")
        step_down = get_step_down(base)
        step_up = get_step_up(base)
        
        configs = []
        configs.append((f"1. Base Pool (2d{base})", [base, base]))
        if step_down != base:
            configs.append((f"2. Minor Boon (+1d{step_down}) -> 2d{base}+1d{step_down}", [base, base, step_down]))
        configs.append((f"3. Standard Boon (+1d{base}) -> 3d{base}", [base, base, base]))
        if step_up != base:
            configs.append((f"4. Major Boon (+1d{step_up}) -> 2d{base}+1d{step_up}", [base, base, step_up]))
            configs.append((f"5. Full Die Step-Up Pool -> 2d{step_up}", [step_up, step_up]))
        configs.append((f"6. Double Boon (+2d{base}) -> 4d{base}", [base, base, base, base]))
        
        header_title = f"Config (Base d{base})"
        header = f"{header_title:<45}" + "".join([f"DC {dc}:<8" for dc in dcs])
        print(header)
        print("-" * len(header))
        
        for label, pool in configs:
            row = f"{label:<45}"
            for dc in dcs:
                p = prob_pool(pool, dc)
                row += f"{p:<7.1f}% "
            print(row)

if __name__ == "__main__":
    main()

Open
used
Bash
122ms
Edited files
6
01_resolution_engine.md
MD
01_master_brainstorm_log.md
MD
02_probability_and_dice_simulations.md
MD
used
Bash
91ms

We have formalized both of your decisions, updated our core ruleset (03_core_baseline_system/01_resolution_engine.md), and archived the exact Python simulations in 06_brainstorming_logs_and_roadmap/02_probability_and_dice_simulations.md (presented above) alongside the executable script sim_boons.py.

🏛️ 1. Nomenclature Update (Die Step-Up & Die Step-Down)

You asked whether "stepping the die (Step-Up and Step-Down)" is vastly better and simpler than "Hyper-Shifting and Downshifting."

The Verdict: Yes! In English and across classic tabletop RPG design (Savage Worlds, Earthdawn, Cortex Prime, Forbidden Lands), Die Step-Up (Stepping Up the die/pool: 2d6 -> 2d8) and Die Step-Down (Stepping Down the die/pool: 2d8 -> 2d6) are universal, highly intuitive, and zero out all sci-fi/techno jargon. We have officially replaced all references to "Hyper-Shift / Downshift" across our baseline rules with clean Die Step-Up and Die Step-Down terminology (DEC-016).
📊 2. Python Simulation: Granularity vs. Complexity (Mixed Die Boons)

We wrote and executed a Python script (sim_boons.py) to test what happens if Boons add mixed step dice (e.g., Base 2d8 + an extra d6 step-down die, vs + an extra d10 step-up die) compared to same-size Boons (3d8) and whole-pool Step-Ups (2d10).

Here are our exact combinatorial simulation results for a Base d8 actor (2d8 keep highest):

Configuration (Base d8 Character)	DC 3 (Routine)	DC 5 (Challenging)	DC 7 (Formidable)	DC 9 (Heroic)	DC 11 (Legend)
1. Base Pool (2d8)	93.8%	75.0%	43.8%	0.0%	0.0%
2. Minor Boon (2d8 + 1d6 Step-Down)	97.9%	83.3%	43.8% (+0.0%)	0.0%	0.0%
3. Standard Boon (3d8 Same-Size)	98.4%	87.5%	57.8% (+14.0%)	0.0%	0.0%
4. Major Boon (2d8 + 1d10 Step-Up)	98.8%	90.0%	66.2% (+22.4%)	20.0%	0.0%
5. Full Die Step-Up Pool (2d10)	96.0%	84.0%	64.0% (+20.2%)	36.0%	0.0%
6. Double Boon (4d8 Same-Size)	99.6%	93.8%	68.4%	0.0%	0.0%
Why We Avoid Mixed Die Sizes (The Mathematical Proof)

The simulation proves your intuition right: introducing mixed die sizes into Boons creates unnecessary table complexity while triggering two mathematical traps:

The "Ceiling Trap" of Step-Down Boons (2d8 + 1d6):
Look at what happens against DC 7: adding a +1d6 step-down boon to 2d8 leaves the success probability at exactly 43.8% (+0.0% change over base 2d8). Because a 
𝑑
6
d6 literally cannot roll a 7, a step-down boon provides zero chance of helping against any DC or opposed roll higher than its own max face. This creates a frustrating trap where players roll extra dice that mathematically cannot contribute to passing the check.
Redundancy with Pool Step-Ups (2d8 + 1d10 vs 2d10):
Look at 2d8 + 1d10 (Major Boon) vs simply Stepping Up the base pool (2d10):
At DC 7, the success rates are nearly identical (66.2% vs 64.0%).
At DC 9, stepping up the full pool (2d10 = 36.0%) is significantly more effective and reliable than adding a single mixed d10 (20.0%), while requiring only one die size (two d10s) instead of mixing two d8s with a d10!
🏆 Architectural Rule Established (DEC-017)
Boons (+1B, +2B) always add dice of the SAME SIZE as the check pool (3d8, 4d8). This guarantees clean single-size rolling and maximum reliability.
When a feature, exertion, or spell warrants a higher ceiling or major power boost, we perform a Die Step-Up (2d8 
→
→ 2d10). We do not mix step-up/step-down dice inside the same check pool!
🚀 Summary of Where Our System Stands

We now have:

The Tri-Modal Resolution Engine: (Fixed DC, Pure Opposed, Hybrid DC Floor).
Universal Nomenclature: (Die Step-Up / Die Step-Down, Boons as same-size volume).
6-Tier High Fantasy Scale: (Trained -> Veteran -> Master -> Hero -> Legend -> Mythic [21+]).
Universal Actor Schema: (Race + Class + Skills + Feats universally across all PCs and Monsters).
Dual-Mode Spatial Engine: (Exact grid squares vs 5-Tier zones).
Simulationist Defenses & Wounds: (Evasion, Parry, Soak, Resilience, active 
𝐴
𝑃
AP Stamina burn, and the 1d8 Anatomical Location Matrix).

Where would you like to direct our creative energy next?

Design the Core Feat Compendium (General, Combat, and Racial Feats): Convert 30 iconic D&D 3.5e feats (Power Attack, Cleave, Combat Reflexes, Dodge, Improved Initiative, Toughness, Weapon Focus) into 1-sentence mathless vector traits across the 6 tiers.
Flesh out the 5 Action Mastery Domains (Skill Taxonomy & Maneuver Lists): Detail all 5 domains (Combat, Survival, Subterfuge, Lore, Social), building their proficiencies and maneuver options (Shove, Trip, Grapple, Disarm, Feint, Demoralize).
Build the Magic & Spellcasting Engine: Define the rules for casting across our 5 Traditions using Focus points, spell interruption via anatomical head/chest wounds, and convert 15 classic spells (Fireball, Cure Wounds, Invisibility, Haste, Hold Person).
Build a Step-by-Step Character & Monster Walkthrough: Build a Tier 2 Veteran (Level 6) PC and a Tier 3 Master (Level 10) Boss monster from scratch to show the exact mathless formulas in action.
