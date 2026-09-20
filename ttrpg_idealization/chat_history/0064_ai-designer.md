---
turn: 64
role: "AI-Designer"
source: chat_history.json
---

# Turn 64 — AI-Designer

[SET] stands for "Special Effect Tokens" (or "Maneuver Tokens").

It was our initial mechanism for adapting Mythras’s differential combat maneuvers (Case Study 5) into our mathless step-pool engine.

🔍 Exactly What [SET] Is Right Now (And How It Works)

In Mythras, whenever an attacker beats a defender's parry by 1 or 2 levels of success (e.g., Critical vs. Failure), the winner immediately earns 1 or 2 "Special Effects" that they can spend right at the table to perform maneuvers (Impale, Bleed, Disarm, Trip, Riposte) without needing class feats.

To translate that into our 2dX keep highest step pools without percentile math, we built the [SET] token loop:

The Hit Check: You roll your attack pool (3d10) vs the enemy's Parry pool (2d8). You compare the highest faces (say, your 9 vs their 6). 9 > 6 
→
→ You hit!
The Multi-Beat Count: You then look at your other/remaining rolled dice (say, you also rolled a 7 and an 8). Because both 7 and 8 also beat the enemy's 6, each extra beating die awards 
+
1
 Special Effect Token (‘[SET]‘)
+1 Special Effect Token (‘[SET]‘).
The Table Spend: Right at that moment before rolling damage, you hold your temporary [SET] tokens (say, 2 tokens) and choose how to spend them from a universal table of maneuvers:
1 [SET] 
→
→ Bleed (Target takes 1 Vitality loss/round) OR Trip (Target knocked Prone) OR Disarm (Weapon dropped) OR Bypass Absorption (Armor stepped down two ranks -> d10 to d6).
2 [SET] 
→
→ Called Shot (Force an immediate Anatomical 1d8 Wound even on a non-crit hit) OR Riposte (Free un-parriable counter-strike).
⚠️ Why You Rightfully Mentioned Trimming It Earlier

While [SET] tokens accurately capture Mythras's tactical maneuvers, it creates a cognitive "Token Currency / Shopping List" loop right in the middle of every single weapon swing!

Look at the friction it introduces at the table:

Instead of simply saying "I hit for 14 damage against your Absorption d8," the player has to pause, count extra beating dice ("Okay, my second die was 7, that beats 6, so that's 1 token..."), look at an 8-item table, and decide how to spend temporary tokens every single turn.
Furthermore, it borders on feeling like a temporary meta-currency, which rubs against our Strict Zero Meta-Currencies (DEC-006) and Zero Table Arithmetic (DEC-001) design pillars!
✂️ Two Clean Ways to Trim & Replace [SET] Tokens Right Now (DEC-042)

If we want to trim [SET] tokens completely so that combat plays lightning fast while keeping 100% of our tactical maneuvers (Disarm, Trip, Bleed, Called Shots), here are the two cleanest architectural replacements:

Alternative 1: The Direct Weapon & Feat Trigger Model (No Tokens, No Counting!)

Instead of counting extra dice for tokens, maneuvers become Discrete Weapon Traits and Class Feats that trigger directly via our existing 3-Action Economy ([1A], [2A]) and 
𝑑
100
d100 Critical Hits (DEC-034):

Standard Hits (Damage > Absorption): Deals normal Vitality (HP) loss. If you want to perform a tactical maneuver (Trip, Disarm, Feint, Shove), you declare it as a Specific Action ([1A] Maneuver) OR you declare a Called Shot (taking +1 Bane Die [-1 die volume] on your attack check). If the attack hits, the maneuver happens automatically! Zero tokens needed.
Critical Hits (via d100 Crit Profile OR Called Shot): Automatically deals double Vitality loss AND forces an Anatomical Wound Condition (Roll 1d8 Location Matrix)! The localized wound (Head Concussion, Dropped Weapon, Prone Legs) is the dramatic special effect!
Alternative 2: The Multi-Success Direct Trigger (DEC-036 Multi-Beats without Tokens)

Using our Multi-Success Complex Checks (DEC-036):

1 Success (Highest face beats opponent): Standard Hit (Damage vs Absorption).
2 Successes (Two dice beat opponent): Hit + Automatic Weapon Property (e.g., Flail knocks Prone; Dagger inflicts Bleed; Halberd pushes back). You don't count tokens or check a table; if your second die also beat the opponent, your weapon's innate property just happens automatically!
🎯 What Would You Like to Do?

Should we officially trim and remove [SET] tokens from the system right now (DEC-042) and replace them with Alternative 1 (Clean Action/Feat Maneuvers + d100 Crits/1d8 Wounds) or Alternative 2 (Multi-Success Weapon Properties)?

That would instantly streamline combat, speed up every turn, and remove the last bit of token bookkeeping from our baseline rules!
