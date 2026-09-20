#!/usr/bin/env python3
"""
Simulate Competency Floors (Fixed Die Floor) across the 5 Competency Levels over 20 levels.
Evaluates both Fixed DC Success Rates (%) and Opposed Roll Win/Tie/Loss Rates (%).
"""
import itertools

# Define the 5 Competency Levels across the 20 levels
# Format: (Name, Die Size, Pool Volume, Competency Floor)
COMPETENCY_LEVELS = [
    ("0. Untrained (Lvl 0 Civilian)", 6, 2, 0),
    ("1. Trained (Tier 1 Lvl 1-4)", 8, 3, 3),
    ("2. Expert (Tier 2 Lvl 5-8)", 10, 3, 5),
    ("3. Master (Tier 3/4 Lvl 9-15)", 12, 4, 7),
    ("4. Legendary (Tier 5/6 Lvl 16+)", 12, 5, 9)
]

DCS = [3, 5, 7, 9, 11]

def simulate_fixed_dcs():
    print("=== PART 1: FIXED DC SUCCESS RATES WITH COMPETENCY FLOORS (%) ===")
    header = f"{'Competency Level':<35}" + "".join([f"DC {dc}:<8" for dc in DCS])
    print(header)
    print("-" * len(header))
    
    for name, die, num_dice, floor in COMPETENCY_LEVELS:
        row = f"{name:<35}"
        total_outcomes = die ** num_dice
        for dc in DCS:
            if floor >= dc:
                row += f"{'100.0%':<8}"
            elif die < dc:
                row += f"{'0.0%':<8}"
            else:
                successes = sum(
                    1 for roll in itertools.product(range(1, die + 1), repeat=num_dice)
                    if max(max(roll), floor) >= dc
                )
                prob = (successes / total_outcomes) * 100.0
                row += f"{prob:<7.1f}% "
        print(row)

def simulate_opposed_contests():
    print("\n=== PART 2: OPPOSED COMBAT CONTESTS (ATTACKER VS DEFENDER) ===")
    print("Shows Attacker Win % | Defender Win (Intercept) % | Exact Tie %")
    header = f"{'Attacker vs Defender Matchup':<45} | Att Win % | Def Win % | Tie %"
    print(header)
    print("-" * len(header))
    
    # Select key matchups to demonstrate differential floors
    matchups = [
        (1, 0), # Trained vs Untrained
        (2, 1), # Expert vs Trained
        (3, 2), # Master vs Expert
        (4, 3), # Legendary vs Master
        (4, 0), # Legendary vs Untrained (Total Dominance)
        (1, 1), # Trained vs Trained (Mirror Match)
        (2, 2), # Expert vs Expert (Mirror Match)
        (3, 3), # Master vs Master (Mirror Match)
        (1, 2), # Trained vs Expert (Underdog)
    ]
    
    for att_idx, def_idx in matchups:
        att_name, att_die, att_num, att_floor = COMPETENCY_LEVELS[att_idx]
        def_name, def_die, def_num, def_floor = COMPETENCY_LEVELS[def_idx]
        
        att_short = att_name.split(" (")[0]
        def_short = def_name.split(" (")[0]
        label = f"{att_short} vs {def_short}"
        
        # We can simulate via Monte Carlo (100,000 trials) or full exact combinatorial depending on size
        # Since 12^5 * 12^4 = 248,832 * 20,736 = ~5 billion outcomes, Monte Carlo 150,000 trials is extremely accurate!
        import random
        random.seed(42)
        trials = 150000
        att_wins = 0
        def_wins = 0
        ties = 0
        
        for _ in range(trials):
            att_roll = max(max(random.randint(1, att_die) for _ in range(att_num)), att_floor)
            def_roll = max(max(random.randint(1, def_die) for _ in range(def_num)), def_floor)
            
            if att_roll > def_roll:
                att_wins += 1
            elif def_roll > att_roll:
                def_wins += 1
            else:
                ties += 1
                
        print(f"{label:<45} | {att_wins/trials*100:<9.1f}% | {def_wins/trials*100:<9.1f}% | {ties/trials*100:<6.1f}%")

if __name__ == "__main__":
    simulate_fixed_dcs()
    simulate_opposed_contests()
