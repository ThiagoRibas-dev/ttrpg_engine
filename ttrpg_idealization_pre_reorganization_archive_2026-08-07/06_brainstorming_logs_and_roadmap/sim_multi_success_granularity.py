#!/usr/bin/env python3
"""
Simulate Multi-Success Resolution Granularity.
Evaluates check pools across both DC Thresholds (T = 3, 5, 7, 9, 11)
and Required Success Counts (S = 1, 2, 3, 4 dice meeting/exceeding T).
"""
import itertools

DCS = [3, 5, 7, 9, 11]
SUCCESS_COUNTS = [1, 2, 3, 4]

# Candidate pools across 20 levels showing atomic growth of Die Size (X), Volume (N), and Floor (F)
POOLS = [
    ("Lvl 1 Civilian / Untrained (2d6, Floor 0)", 6, 2, 0),
    ("Lvl 1 Trained Hero (3d8, Floor 3)", 8, 3, 3),
    ("Lvl 5 Veteran Expert (3d10, Floor 5)", 10, 3, 5),
    ("Lvl 9 Master Defender (4d12, Floor 7)", 12, 4, 7),
    ("Lvl 15 Legendary Paragon (5d12, Floor 9)", 12, 5, 9),
    ("Lvl 20 Apex Grandmaster (5d12, Floor 9)", 14, 5, 9) # Using d14 as proxy for over-cap d12 pool
]

def simulate_multi_success():
    print("=== MULTI-SUCCESS RESOLUTION GRANULARITY (%) ===")
    print("Shows probability of achieving at least S dice meeting or exceeding DC Threshold T\n")
    
    for pool_name, die, num_dice, floor in POOLS:
        print(f">>> Pool: {pool_name}")
        header = f"{'Required Successes (S)':<26}" + "".join([f"DC {dc}:<9" for dc in DCS])
        print(header)
        print("-" * len(header))
        
        total_outcomes = die ** num_dice
        
        for req_s in SUCCESS_COUNTS:
            if req_s > num_dice:
                row = f"{f'{req_s} Success(es)':<26}" + "".join([f"{'0.0%':<9}" for _ in DCS])
                print(row)
                continue
                
            row = f"{f'{req_s} Success(es)':<26}"
            for dc in DCS:
                if floor >= dc and req_s == 1:
                    row += f"{'100.0%':<9}"
                elif die < dc:
                    row += f"{'0.0%':<9}"
                else:
                    successes = sum(
                        1 for roll in itertools.product(range(1, die + 1), repeat=num_dice)
                        if sum(1 for face in roll if max(face, floor) >= dc) >= req_s
                    )
                    prob = (successes / total_outcomes) * 100.0
                    row += f"{prob:<8.1f}% "
            print(row)
        print()

if __name__ == "__main__":
    simulate_multi_success()
