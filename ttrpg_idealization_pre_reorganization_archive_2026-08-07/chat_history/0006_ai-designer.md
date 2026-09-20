---
turn: 6
role: "AI-Designer"
source: chat_history.json
---

# Turn 6 — AI-Designer

We used the ttrpg_architecture_matrix.md file as the structural foundation and data schema blueprint for our entire project.

Specifically, we utilized the file across five critical areas of our design and brainstorm:

1. Adopting the 10-Category Master Data Schema

The uploaded document (TTRPG Structural Analysis Matrix v2) established a mapping of character sheets across 17 reference systems (Ars Magica, Burning Wheel, Kids on Bikes, Call of Cthulhu, Fate, Vampire V5, GURPS, etc.) organized into 10 distinct categories.

We adopted these exact 10 categories as the universal data architecture for our own character sheet and baseline system (03_core_baseline_system/02_character_schema_and_stats.md):

meta: System metadata, campaign setting, player name.
identity: Biographical and descriptive traits (Culture, Concept, Age).
attributes: Core innate capabilities (Might, Agility, Intellect, Will as step dice 
𝑑
4
→
𝑑
12
d4→d12).
skills: Learned capabilities (Combat Mastery, Subterfuge, Lore granting 
+
1
𝐵
→
+
3
𝐵
+1B→+3B pool dice).
resources: Depletable tracks that fluctuate during play (Vitality, Stamina, Focus, Durability Slots).
features: Discrete binary capabilities (Feats, 3-Tier Paths, Ancestry traits).
inventory: Physical possessions (Weapons, Armor Soak steps, Rations).
connections: Relationships to NPCs, factions, and party members.
narrative: Story hooks with mechanical weight (Drives, Moral Codes).
progression: Advancement state (Milestones, Path Tiers, XP logs).
2. Applying the Disambiguation & Boundary Rules

The matrix defined strict Boundary Rules and Disambiguation Rules (Attribute vs Skill, Skill vs Feature, Resource vs Attribute, Feature vs Narrative) to prevent design blur. We used these exact boundary rules to govern our Mathless Mechanics:

Attribute vs. Skill Rule: "If it represents innate capability -> Attribute. If it improves through practice/use -> Skill."
Our Application: Attributes (Might, Agility, Intellect, Will) govern the Die Size / Capability Ceiling (
𝑑
4
→
𝑑
12
d4→d12), while Skills (Combat, Lore, Athletics) govern the Pool Volume / Reliability (
+
1
𝐵
→
+
3
𝐵
+1B→+3B).
Skill vs. Feature Rule: "If it has a rating you roll -> Skill. If it's binary (have/don't have) -> Feature."
Our Application: Action domains are rolled (Skills), whereas D&D 3.5e Feats and SotDL Path Talents are structured strictly as binary Features (Power Attack, Cleave, Berserk Fury) that grant specific step upgrades (Up-Shift) or maneuver permissions ([SET] triggers) without adding 
+
𝑋
/
−
𝑋
+X/−X math.
Resource vs. Attribute Rule: "If it depletes during a session and recovers -> Resource."
Our Application: We categorized Stamina (Poise), Focus, and Equipment Durability strictly under Resources, ensuring every spendable asset exists within the fictional world (obeying our Zero Meta-Currencies pillar).
3. Expanding the Reference Systems from 17 to 23 Games

We took the exact 17 games detailed in ttrpg_architecture_matrix.md and used them as our base data layer in 02_comparative_system_analysis/01_architecture_matrix_v3_expanded.md. We then added six new reference systems directly into that same 10-category schema table:

D&D 3.5e (Our primary option-density anchor)
Pathfinder 2e (Our 3-action tactical anchor)
Shadow of the Demon Lord / Weird Wizard (Our boons/banes & path anchor)
Gloomhaven / Frosthaven (Tactical card board game reference)
Lands of Evershade (Hybrid narrative board game reference)
Mythras (BRP / d100 Engine) (Our opposed differential & hit location anchor)
4. Expanding the Analytical Vectors from 10 to 18

The uploaded document concluded with a Structural Pattern Analysis section comparing representation patterns across Attributes, Skills, Resources, and Features.

We used this pattern analysis as the template to introduce Eight New System-Wide Vectors of Analysis (Vectors 11 through 18) across all 23 games:

Vector 11: Resolution Engine & Arithmetic Load: Mapped the table math of all 23 games (from 3.5e's heavy +BAB/+Str/+Feat addition to our mathless 2dX keep highest).
Vector 12: Defense & Mitigation Model: Mapped single abstract 
𝐴
𝐶
AC (D&D/PF2e) versus multi-layer mitigation (Gloomhaven Shields, Mythras Parry/Evade, and our 4-Layer Evasion/Parry/Soak/Resilience model).
Vector 13: Meta-Currency vs. In-World Resource Dependency: Mapped out-of-world player tokens (Fate Points, Hero Points, Artha) versus purely in-world physical/mental tracks (Stamina, Focus).
Vector 14: Content Extensibility & Conversion Surface: Mapped how easily new feats, spells, and path talents plug into the core engine.
Vector 15: Opposed Differential Maneuver Triggers: Mapped how difference in roll success unlocks maneuvers (Mythras Special Effects vs our Mathless [SET] tokens).
Vector 16: Active Defense Action Economy: Mapped whether defense is passive (
𝐴
𝐶
AC) or consumes turn action budget / stamina (Mythras AP spending & our Parry Fatigue).
Vector 17: Hit Location Granularity & Wound Severance: Mapped global HP bars vs anatomical localized injury (Mythras 7 locations & our 1d8 Anatomical Matrix).
Vector 18: GM Cognitive Load & Mob Scaling: Mapped mass combat tracking (3.5e full stat blocks vs Mythras Rabble/Underlings vs our 3-tier mob rules).
5. Serving as our Content Conversion Standard

Finally, ttrpg_architecture_matrix.md acted as our standardization checklist when building our D&D 3.5e and SotDL Conversion Pipelines (05_conversion_and_content_engine/).

Whenever we convert a 3.5e element (such as the Combat Expertise feat, the Fireball spell, or an Ogre's stat block), we run it through the 10-category boundary rules to guarantee that every translated option slots cleanly into its respective category on our mathless character sheet without introducing mathematical clutter.
