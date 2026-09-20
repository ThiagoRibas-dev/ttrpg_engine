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
