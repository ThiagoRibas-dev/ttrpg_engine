---
turn: 28
role: "AI-Designer"
source: chat_history.json
---

# Turn 28 — AI-Designer

Write
ttrpg_idealization/06_brainstorming_logs_and_roadmap/sim_paired_defenses.py
107 lines
open
sim_paired_defenses.py
PYTHON
#!/usr/bin/env python3
"""
Simulate Paired Defense Pools (e.g., DEX + INT for Reflexes, STR + CON for Fortitude, WIS + CHA for Willpower)
across 5 Investment Configurations vs Fixed DCs and Equivalent Offense Pools.
"""
import itertools
import random

# Define the 5 Defense Investment Configurations
# Format: (Config Name, Attr1 Die, Attr2 Die, Extra Boons on Highest Attr, Competency Floor)
DEFENSE_CONFIGS = [
    ("1. Zero Investment on Either (d6 + d6)", 6, 6, 0, 0),
    ("2. Avg Investment on ONE (d10 + d6, +1B)", 10, 6, 1, 3),
    ("3. Avg Investment on BOTH (d8 + d8, +1B)", 8, 8, 1, 3),
    ("4. Max Investment on ONE (d12 + d6, +2B)", 12, 6, 2, 7),
    ("5. Max Investment on BOTH (d12 + d12, +2B)", 12, 12, 2, 7)
]

DCS = [3, 5, 7, 9, 11]

def build_pool(attr1, attr2, boons):
    """Builds the paired defense dice pool."""
    pool = [attr1, attr2]
    highest = max(attr1, attr2)
    for _ in range(boons):
        pool.append(highest)
    return pool

def simulate_fixed_dcs():
    print("=== PART 1: PAIRED DEFENSE POOL SUCCESS RATES vs FIXED DCs (%) ===")
    header = f"{'Defense Configuration':<44}" + "".join([f"DC {dc}:<8" for dc in DCS])
    print(header)
    print("-" * len(header))
    
    for name, a1, a2, boons, floor in DEFENSE_CONFIGS:
        pool = build_pool(a1, a2, boons)
        row = f"{name:<44}"
        total_outcomes = 1
        for d in pool:
            total_outcomes *= d
            
        for dc in DCS:
            if floor >= dc:
                row += f"{'100.0%':<8}"
            elif max(pool) < dc:
                row += f"{'0.0%':<8}"
            else:
                successes = sum(
                    1 for roll in itertools.product(*[range(1, d + 1) for d in pool])
                    if max(max(roll), floor) >= dc
                )
                prob = (successes / total_outcomes) * 100.0
                row += f"{prob:<7.1f}% "
        print(row)

def simulate_opposed_contests():
    print("\n=== PART 2: OPPOSED CONTESTS vs EQUIVALENT OFFENSE POOLS ===")
    print("Compares Paired Defense Pool vs Attacker Pool (Att Win % | Def Win/Save % | Exact Tie %)")
    print("-" * 88)
    
    # Define Equivalent Offense Tiers to test against
    # Format: (Offense Label, Attacker Pool Dice, Attacker Floor)
    offense_tiers = [
        ("Tier 1 Offense (3d8, Floor 3)", [8, 8, 8], 3),
        ("Tier 2 Offense (3d10, Floor 5)", [10, 10, 10], 5),
        ("Tier 3/4 Offense (4d12, Floor 7)", [12, 12, 12, 12], 7)
    ]
    
    random.seed(42)
    trials = 100000
    
    for off_label, att_pool, att_floor in offense_tiers:
        print(f"\n>>> Against {off_label}:")
        header = f"{'Defender Configuration':<44} | Att Win % | Def Save % | Exact Tie %"
        print(header)
        print("-" * len(header))
        
        for name, a1, a2, boons, def_floor in DEFENSE_CONFIGS:
            def_pool = build_pool(a1, a2, boons)
            
            att_wins = 0
            def_wins = 0
            ties = 0
            
            for _ in range(trials):
                # Roll Attacker
                att_roll = max(random.randint(1, d) for d in att_pool)
                att_roll = max(att_roll, att_floor)
                
                # Roll Defender
                def_roll = max(random.randint(1, d) for d in def_pool)
                def_roll = max(def_roll, def_floor)
                
                if att_roll > def_roll:
                    att_wins += 1
                elif def_roll > att_roll:
                    def_wins += 1
                else:
                    ties += 1
                    
            short_name = name.split(" (")[0] + f" ({a1}+{a2})"
            print(f"{short_name:<44} | {att_wins/trials*100:<9.1f}% | {def_wins/trials*100:<10.1f}% | {ties/trials*100:<7.1f}%")

if __name__ == "__main__":
    simulate_fixed_dcs()
    simulate_opposed_contests()

Open
used
Bash
5.8s
Edited files
4
01_master_brainstorm_log.md
MD
02_probability_and_dice_simulations.md
MD
used
Bash
76ms

I have written and executed the Python simulation script 
sim_paired_defenses.py
 (presented above), archived the full data tables in 06_brainstorming_logs_and_roadmap/02_probability_and_dice_simulations.md Section 6, and recorded decision DEC-023 in our master log.

🧪 What We Simulated (Paired Defenses vs Equivalent Offense)

When making a defense check (Fortitude STR+CON | Reflexes DEX+INT | Willpower WIS+CHA), the defender's check pool is formed by taking 1 die of Attribute 1 + 1 die of Attribute 2 keep highest. Any defense Boons (+1B, +2B) add extra dice matching the highest paired attribute.

We tested the 5 Defense Investment Configurations across both Fixed Target DCs (3, 5, 7, 9, 11) and 100,000 Monte Carlo opposed trials against Equivalent Offense Tiers (Tier 1: 3d8/Floor 3 | Tier 2: 3d10/Floor 5 | Tier 3/4 Master: 4d12/Floor 7):

text
[ Defender Paired Pool: 1d(Attr 1) + 1d(Attr 2) + Boons ]  vs  [ Equivalent Offense Pool: NdX + Competency Floor ]
                                            │
                                            ▼
                    Compare Highest Face vs Highest Face (`Max vs Max`)
                                            │
                ┌───────────────────────────┼───────────────────────────┐
                ▼                           ▼                           ▼
        Attacker Win %               Defender Save %              Exact Tie %
📊 Part 1: Paired Defense Pool Success Rates vs Fixed DCs (%)
Defense Configuration	DC 3 (Routine)	DC 5 (Challenging)	DC 7 (Formidable)	DC 9 (Heroic)	DC 11 (Legend)
1. Zero Investment (d6 + d6, Floor 0)	88.9%	55.6%	0.0%	0.0%	0.0%
2. Avg on ONE (d10 + d6, +1B, Floor 3)	100.0%	89.3%	64.0%	36.0%	0.0%
3. Avg on BOTH (d8 + d8, +1B, Floor 3)	100.0%	87.5%	57.8%	0.0%	0.0%
4. Max on ONE (d12 + d6, +2B, Floor 7)	100.0%	100.0%	100.0%	70.4%	42.1%
5. Max on BOTH (d12 + d12, +2B, Floor 7)	100.0%	100.0%	100.0%	80.2%	51.8%
⚔️ Part 2: Opposed Contests vs Equivalent Offense Pools (Att Win % | Def Save % | Tie %)
Against Tier 1 Offense (3d8, Competency Floor 3)
Defender Configuration	Attacker Win %	Defender Save %	Exact Tie %	Net Defensive Hold (Save + Tie)
1. Zero Investment (6+6)	77.6%	11.7%	10.7%	~22.4% hold (Untrained vulnerable to trained attacks).
2. Avg on ONE (10+6, +1B)	30.3%	57.0%	12.7%	~69.7% hold (Spiky specialist intercepts effectively).
3. Avg on BOTH (8+8, +1B)	39.0%	38.5%	22.5%	~61.0% hold (Balanced 3d8 produces 22.5% mirror ties).
4. Max on ONE (12+6, +2B)	6.6%	85.3%	8.1%	~93.4% hold (Master defense crushes Tier 1 attack).
5. Max on BOTH (12+12, +2B)	3.9%	90.5%	5.6%	~96.1% hold (Paragon almost untouchable).
Against Tier 2 Offense (3d10, Competency Floor 5)
Defender Configuration	Attacker Win %	Defender Save %	Exact Tie %	Net Defensive Hold (Save + Tie)
1. Zero Investment (6+6)	90.5%	3.8%	5.8%	~9.6% hold (Untrained civilian helpless).
2. Avg on ONE (10+6, +1B)	51.7%	32.5%	15.7%	~48.2% hold (Spiky d10 matches enemy d10 ceiling).
3. Avg on BOTH (8+8, +1B)	69.1%	19.1%	11.8%	~30.9% hold (d8 ceiling struggled vs d10 attack).
4. Max on ONE (12+6, +2B)	21.2%	67.7%	11.2%	~78.9% hold (d12 ceiling dominates d10 offense).
5. Max on BOTH (12+12, +2B)	14.7%	75.3%	10.0%	~85.3% hold (Paragon holds firm).
Against Tier 3/4 Master/Hero Offense (4d12, Competency Floor 7)
Defender Configuration	Attacker Win %	Defender Save %	Exact Tie %	Net Defensive Hold (Save + Tie)
1. Zero Investment (6+6)	100.0%	0.0%	0.0%	0.0% hold (Guaranteed hit against untrained defense).
2. Avg on ONE (10+6, +1B)	81.1%	10.9%	8.0%	~18.9% hold (Veteran defense outclassed by Master attack).
3. Avg on BOTH (8+8, +1B)	90.7%	3.8%	5.6%	~9.4% hold (d8 ceiling overwhelmed).
4. Max on ONE (12+6, +2B)	47.8%	34.2%	18.1%	~52.3% hold (Master vs Master clash; ~18% tiebreaker).
5. Max on BOTH (12+12, +2B)	39.9%	40.0%	20.0%	~60.0% hold (True 50/50 mirror deadlock broken by 2nd die).
🔑 The Two Big Simulationist Findings
The "Spiky Specialist" vs. "Balanced Generalist" Dynamics (Config 2 vs Config 3):
Because our pool uses Keep Highest, pushing ONE paired stat high (say, DEX d10 and INT d6 + 1B -> 2d10 + 1d6) gives you two high dice (2d10), which outperforms a balanced generalist (DEX d8 and INT d8 + 1B -> 3d8) whenever the enemy's attack roll exceeds 8. However, the balanced generalist produces a higher rate of exact mirror ties (22.5% vs 12.7%), allowing them to win defensive tiebreakers against lower-level attackers!
Why Pushing Both Stats to Max (Config 4 vs Config 5) Matters:
A character maximizing one paired stat (d12 + d6 + 2B -> 3d12 + 1d6) captures ~85-90% of total defensive power against Master attacks (34.2% save vs 40.0% save). Pushing the second paired stat to max (INT d6 -> d12 -> 4d12) provides that final ~10% elite consistency boost, giving grandmasters the upper hand in Secondary Tiebreaker face comparisons during mirror duels!

Where should our creative energy focus next? We have our complete, mathematically verified foundation. Would you like to:

Design the Core Feat Compendium (General, Combat, and Racial Feats): Convert 30 iconic D&D 3.5e feats (Power Attack, Cleave, Combat Reflexes, Dodge, Improved Initiative, Toughness, Weapon Focus) into clean vector traits?
Detail the 5 Action Mastery Domains (Skill Taxonomy & Maneuver Lists): Flesh out Combat, Survival, Subterfuge, Lore, and Social maneuvers (Shove, Trip, Grapple, Disarm, Feint, Demoralize) across all competency ranks?
Build the Magic & Spellcasting Engine: Detail Focus channeling across our 5 Traditions (Arcana, Divine, Primal, Shadow, Time), spell interruption via anatomical hits, and convert 15 classic spells?
