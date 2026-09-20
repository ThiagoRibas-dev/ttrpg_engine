---
turn: 18
role: "AI-Designer"
source: chat_history.json
---

# Turn 18 — AI-Designer

Write
ttrpg_idealization/06_brainstorming_logs_and_roadmap/sim_competency_floors.py
96 lines
open
sim_competency_floors.py
PYTHON
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

Open
used
Bash
5.8s
Edited files
6
01_master_brainstorm_log.md
MD
01_resolution_engine.md
MD
02_probability_and_dice_simulations.md
MD
used
Bash
85ms

We have simulated and mathematically engineered your Hybrid Fixed Die Floor (Competency Floor) engine across the 5 Proficiency Tiers and locked it into our core ruleset (03_core_baseline_system/01_resolution_engine.md) and probability archives (06_brainstorming_logs_and_roadmap/02_probability_and_dice_simulations.md, presented above, alongside our executable script sim_competency_floors.py).

🏛️ The Competency Floor Formula (Engineered Hard Caps)

When rolling a check pool (2dX to 5dX keep highest), a character's Proficiency Tier (Untrained to Legendary) sets a guaranteed minimum floor (F) on their highest die face:

Final Check Result
=
max
⁡
(
max
⁡
(
Rolled Pool Faces
)
,
Competency Floor
)
Final Check Result=max(max(Rolled Pool Faces),Competency Floor)

1. The 5 Competency Levels (Step & Floor Scaling)
0. Untrained (Civilian Lvl 0): 2d6 keep highest, Floor = 0 (Pure random roll)
1. Trained (Tier 1 Lvl 1-4): 3d8 keep highest, Floor = 3 (Guaranteed minimum result of 3)
2. Expert (Tier 2 Lvl 5-8): 3d10 keep highest, Floor = 5 (Guaranteed minimum result of 5)
3. Master (Tier 3/4 Lvl 9-15): 4d12 keep highest, Floor = 7 (Guaranteed minimum result of 7)
4. Legendary (Tier 5/6 Lvl 16+): 5d12 keep highest, Floor = 9 (Guaranteed minimum result of 9)
📊 Part 1: Fixed DC Check Guarantees (Engineered Immunity to Whiffing)

Look at how the Competency Floor (0 -> 3 -> 5 -> 7 -> 9) creates exact, engineered hard caps against static Target Numbers:

Competency Level & Pool	DC 3 (Routine)	DC 5 (Challenging)	DC 7 (Formidable)	DC 9 (Heroic)	DC 11 (Legend)	Engineered Mastery Guarantee
0. Untrained (2d6, Floor 0)	88.9%	55.6%	0.0%	0.0%	0.0%	Can fail routine tasks (11.1% whiff rate).
1. Trained (3d8, Floor 3)	100.0%	87.5%	57.8%	0.0%	0.0%	Immune to failing routine checks (DC 3 = 100%).
2. Expert (3d10, Floor 5)	100.0%	100.0%	78.4%	48.8%	0.0%	Immune to failing standard checks (DC 5 = 100%).
3. Master (4d12, Floor 7)	100.0%	100.0%	100.0%	80.2%	51.8%	Immune to failing formidable checks (DC 7 = 100%).
4. Legendary (5d12, Floor 9)	100.0%	100.0%	100.0%	100.0%	59.8%	Immune to failing heroic checks (DC 9 = 100%).

Why this is brilliant design: An Expert (Floor 5) is mathematically immune to failing DC 3 and DC 5 checks. A Master (Floor 7) is immune to failing DC 7 checks. The dice still roll for differential Special Effect Tokens ([SET]) (Did I roll a 10 or 12 to earn maneuvers?), but the character never whiffs below their competency floor!

⚔️ Part 2: Opposed Combat Contests (Attacker vs Defender Matchups)

In opposed rolls (Attacker Pool vs Defender Pool), Competency Floors create clean dominance curves without adding numerical modifiers:

Attacker vs Defender Matchup	Attacker Win %	Defender Win %	Exact Tie %	Tactical & Simulationist Reality
1. Trained vs 0. Untrained	77.7%	11.7%	10.6%	Trained hero easily out-fences civilian (~78% win rate).
2. Expert vs 1. Trained	69.3%	18.8%	11.9%	Expert out-duels trained fighter (~70% win rate).
3. Master vs 2. Expert	75.3%	14.7%	10.0%	Master completely outclasses regional champion (~75% win rate).
4. Legendary vs 3. Master	46.5%	32.0%	21.5%	Epic clash between titans (high pools produce ~21.5% ties broken by secondary dice).
4. Legendary vs 0. Untrained	100.0%	0.0%	0.0%	Total Demigod Dominance (Guaranteed floor 9 vs max die face 6).
Mirror: Expert vs Expert	40.7%	40.4%	18.9%	50/50 split (~19% ties broken by secondary die or active defense priority).
Why ~20% Ties in Mirror Matches are a Feature, Not a Bug

In our system, when an opposed roll ties (Max vs Max), we check the Secondary Tiebreaker (second highest die in the pool)! And if still tied after checking the secondary die, the Active Defender wins the clash (Defensive Advantage)! This means mirror duels between grandmasters turn into intense multi-die face comparisons where edge alignment (second/third highest face) breaks the deadlock!

🚀 What Would You Like to Build Next?

Now that the Competency Floors (DEC-019), Tri-Vector Matrix (DEC-018), Tri-Modal Engine (DEC-015), and 6-Tier High Fantasy Scale (DEC-014) are locked into our vault, where should we focus our design work next?

Build the Core Feat Compendium (General, Combat, and Racial Feats): Let's convert 30 iconic D&D 3.5e feats (Power Attack, Cleave, Combat Reflexes, Dodge, Improved Initiative, Toughness, Weapon Focus) into clean 1-sentence mathless vector traits (Die Step-Up, [SET] tokens, and 3-action costs) across the 6 tiers.
Flesh out the 5 Action Mastery Domains (Skill Taxonomy & Maneuver Lists): Let's detail all 5 domains (Combat, Survival, Subterfuge, Lore, Social), building their exact proficiencies, capability thresholds (Untrained vs Trained vs Master vs Legend), and maneuver options (Shove, Trip, Grapple, Disarm, Feint, Demoralize).
Build the Magic & Spellcasting Engine: Let's define the exact rules for casting across our 5 Traditions using Focus points, spell interruption via anatomical head/chest hits, and convert 15 classic spells (Fireball, Cure Wounds, Invisibility, Haste, Hold Person).
Build a Step-by-Step Character & Monster Walkthrough: Let's build a Tier 2 Veteran (Level 6) PC and a Tier 3 Master (Level 10) Boss monster from scratch to show the exact mathless formulas in action.

Which of these would you like to tackle next?
