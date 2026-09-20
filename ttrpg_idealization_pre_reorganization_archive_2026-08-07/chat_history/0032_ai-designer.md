---
turn: 32
role: "AI-Designer"
source: chat_history.json
---

# Turn 32 — AI-Designer

You are 100% correct.

Let’s take a clean step back and look at the exact physics of our check pool. When a character makes any roll (say, a Melee Strike or a Lore check), there are precisely Three Mechanical Knobs (Variables) that dictate the outcome without table-side arithmetic:

text
[ Assembling a Check Pool: The 3 Mechanical Knobs ]
  ├── Knob 1: Die Size (`X` — d4 to d12+) ──────────────► Governs the Capability Ceiling & Kinetic Power (`Damage vs Soak`)
  ├── Knob 2: Pool Volume (`N` — 1d to 5d) ─────────────► Governs Reliability, Consistency & Maneuver Token (`[SET]`) Count
  └── Knob 3: Competency Floor (`F` — 0, 3, 5, 7, 9) ──► Governs Guaranteed Minimum Mastery (`Whiff Immunity`)

You are completely right about where things currently stand:

We have locked down Knob 1 (Die Size — X) primarily to the Core Ability Scores (STR, DEX, CON, INT, WIS, CHA).
We have locked down Knob 3 (Competency Floor — F) directly to the 5 Competency Ranks (Untrained 0, Trained 3, Expert 5, Master 7, Legendary 9).
Everything else—specifically, how and what exactly determines Knob 2 (Pool Volume / Number of Dice Rolled), and whether Competency Rank also modifies Knob 1 (Die Size)—is up in the air right now for us to explicitly lock down!
🏛️ The Two Cleanest Ways to Map "Everything Else"

To finalize how a player builds and rolls their pool from their Race + Class + Skills (Competency Ranks) + Feats, we have two primary architectural options:

Option 1: The "Pure Role Separation" Model (Cleanest & Most Intuitive)

In this model, each building block on the character sheet has one distinct, exclusive job:

Core Attribute (STR, DEX, CON, INT, WIS, CHA) 
→
→ Governs Die Size (X).
If your STR is d10, any Strength check (or Melee Strike) rolls d10s (unless you spend 1 Stamina for a Die Step-Up to d12).
Competency Rank (Untrained to Legendary) 
→
→ Governs BOTH Pool Volume (Number of Dice) AND the Competency Floor (Minimum Face) simultaneously!
When you invest skill domain points/feats into an Action Mastery Domain (say, Combat Mastery or Lore), that rank dictates your dice count and floor:
0. Untrained (Civilian): Roll 2dX keep highest, Floor = 0 (Pure random 2-die roll).
1. Trained (Basic Hero): Roll 3dX keep highest (+1 die boon), Floor = 3.
2. Expert (Specialist): Roll 3dX keep highest (+1 die boon), Floor = 5 (Guaranteed immunity to standard DC 5 misses).
3. Master (Grandmaster): Roll 4dX keep highest (+2 dice boons), Floor = 7.
4. Legendary (Paragon): Roll 5dX keep highest (+3 dice boons — Maximum Pool Cap), Floor = 9.
Class Archetype & Feats 
→
→ Governs Action Economy ([A]), Exertion (Stamina/Focus), and Maneuvers ([SET] triggers).
Your Class dictates how easily you buy Competency Ranks (e.g., Fighters start Trained in Combat at Level 1), and gives you active feats (Power Strike [1A], Cleave [0A], Riposte [SET]).

(Why Option 1 is amazing: It is super clean to remember at the table! "My Attribute tells me what size die to grab (d10); my Competency Rank tells me how many of those dice to grab (4 dice) and what my minimum floor is (Floor 7)!")

Option 2: The "Hybrid Tri-Vector" Model (Attribute + Competency = Die Size | Class + Tactics = Pool Volume)

In this model (which we explored in our earlier progression checks), we split things across both axes:

Die Size (X): Governed by Core Attribute (STR d8) + Competency Rank Step Upgrades (Untrained = +0 steps, Trained = +1 Die Step-Up to d10, Master = +2 Die Step-Ups to d12).
Pool Volume (Dice Count): Governed by your Class Baseline (Martial Class = Base 3 dice, Civilian/Caster Class = Base 2 dice) plus Tactical Situations (Flanking +1 die, High Ground +1 die).
Competency Floor (F): Governed by your Competency Rank (0, 3, 5, 7, 9).
⚖️ Which Mapping Should We Lock In?

Do you prefer Option 1 (Pure Role Separation: Attribute = Die Size | Competency Rank = Dice Count + Floor | Class = Feats/Maneuvers) because it gives players exact, granular, self-contained control over their dice count via training while keeping attributes purely responsible for kinetic impact?

Or do you prefer Option 2 (Hybrid Tri-Vector: Attribute + Competency = Die Size | Class + Tactics = Dice Count)? Once we pick one right here, our baseline check engine is 100% concrete and finalized across the board!
