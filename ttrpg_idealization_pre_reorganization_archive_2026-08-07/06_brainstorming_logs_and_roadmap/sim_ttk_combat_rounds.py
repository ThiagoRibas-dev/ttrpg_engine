#!/usr/bin/env python3
"""
Simulate Time to Kill (TTK) and Round-by-Round Combat across 10,000 fights
to verify that our mathematical calibration matches our desired 3-5 Round TTK Baseline.
"""
import random

def simulate_fight(att_pool, att_floor, att_dmg_die, def_hp, def_soak_die, def_parry_pool, def_floor):
    """
    Simulates a round-by-round combat encounter between an Attacker and a Defender until Defender Vitality <= 0.
    Returns: (total_rounds, total_hits, crits_scored, set_tokens_earned)
    """
    hp = def_hp
    rounds = 0
    hits = 0
    crits = 0
    set_tokens = 0
    
    while hp > 0 and rounds < 20: # Cap at 20 rounds to prevent infinite loops
        rounds += 1
        # Each round, assume Attacker makes 2 Strikes (using 2 of their 3 actions, saving 1 for movement/maneuver)
        # Second strike takes +1 Bane Die (-1 die volume) due to multi-attack unless mitigated
        strikes_this_round = [
            att_pool,
            att_pool[:-1] if len(att_pool) > 1 else att_pool
        ]
        
        for strike_pool in strikes_this_round:
            if hp <= 0:
                break
                
            # Attacker rolls check pool vs Defender Parry pool
            att_faces = [random.randint(1, d) for d in strike_pool]
            att_highest = max(max(att_faces), att_floor)
            
            def_faces = [random.randint(1, d) for d in def_parry_pool]
            def_highest = max(max(def_faces), def_floor)
            
            if att_highest > def_highest:
                # Attack beats Parry -> Hit! Check Damage vs Soak
                hits += 1
                
                # Check for Special Effect Tokens [SET] via multi-beat differential
                beating_dice = sum(1 for face in att_faces if face >= def_highest)
                if beating_dice > 1:
                    set_tokens += (beating_dice - 1)
                # Check max face surge
                if max(att_faces) == max(strike_pool):
                    set_tokens += 1
                
                # Roll Damage vs Soak
                dmg_face = random.randint(1, att_dmg_die)
                soak_face = random.randint(1, def_soak_die)
                
                # Check if hit is a Critical Hit (Rolled Max Damage Die OR 2+ steps over Soak)
                is_crit = (dmg_face == att_dmg_die) or (att_highest == max(strike_pool) and beating_dice >= 2)
                
                if is_crit:
                    crits += 1
                    # Critical hit deals double Vitality (Max face x 2) + Severe Wound
                    hp -= (att_dmg_die * 2)
                elif dmg_face > soak_face:
                    # Standard hit deals Vitality equal to damage die face
                    hp -= dmg_face
                elif dmg_face == soak_face:
                    # Superficial impact (loses 2 Stamina or 2 HP if Stamina gone; let's say 2 HP here)
                    hp -= 2
                else:
                    # Damage < Soak -> Absorbed (0 HP loss)
                    pass

    return rounds, hits, crits, set_tokens

def main():
    print("=== TIME TO KILL (TTK) & COMBAT PACING SIMULATION (10,000 FIGHTS) ===")
    print("Verifying target calibration: 3-5 Rounds for Standard/Elites, 1-2 Rounds on Crits\n")
    
    matchups = [
        ("1. Standard PC vs Standard Elite (`3d10 vs 3d10, 18 HP, Soak d8`)",
         [10, 10, 10], 5, 10, 18, 8, [10, 10, 10], 5),
         
        ("2. Veteran Warrior vs Heavy Knight (`3d10 vs 3d10, 22 HP, Plate Soak d12`)",
         [10, 10, 10], 5, 10, 22, 12, [10, 10, 10], 5),
         
        ("3. Master Hero vs Ogre Boss (`4d12 vs 4d10, 32 HP, Soak d10`)",
         [12, 12, 12, 12], 7, 12, 32, 10, [10, 10, 10, 10], 5),
         
        ("4. PC Warrior vs Underling Squad (`3d10 vs 2d8, 2-Hit Checkbox, Soak d8`)",
         [10, 10, 10], 5, 10, 12, 8, [8, 8], 3) # Using 12 HP as approximate 2-hit proxy for Underling
    ]
    
    random.seed(42)
    trials = 10000
    
    for label, att_pool, att_floor, dmg_die, hp, soak, def_pool, def_floor in matchups:
        results = [simulate_fight(att_pool, att_floor, dmg_die, hp, soak, def_pool, def_floor) for _ in range(trials)]
        
        avg_rounds = sum(r[0] for r in results) / trials
        avg_hits = sum(r[1] for r in results) / trials
        avg_crits = sum(r[2] for r in results) / trials
        avg_set = sum(r[3] for r in results) / trials
        
        # Distribution of TTK rounds
        fast_ttk = sum(1 for r in results if r[0] <= 2) / trials * 100
        target_ttk = sum(1 for r in results if 3 <= r[0] <= 5) / trials * 100
        slog_ttk = sum(1 for r in results if r[0] >= 6) / trials * 100
        
        print(f">>> {label}")
        print(f"    Mean Time to Kill (TTK): {avg_rounds:.1f} Rounds | Mean Successful Hits to Kill: {avg_hits:.1f} Hits")
        print(f"    Mean Crits per Fight:    {avg_crits:.1f} Crits  | Mean [SET] Tokens Earned:   {avg_set:.1f} Tokens")
        print(f"    Round Distribution:      [Fast 1-2 Rds: {fast_ttk:.1f}%] | [Target 3-5 Rds: {target_ttk:.1f}%] | [Long 6+ Rds: {slog_ttk:.1f}%]\n")

if __name__ == "__main__":
    main()
