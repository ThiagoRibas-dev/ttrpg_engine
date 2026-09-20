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
