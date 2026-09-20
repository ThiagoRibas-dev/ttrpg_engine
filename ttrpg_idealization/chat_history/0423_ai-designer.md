---
turn: 423
role: "AI-Designer"
source: chat_history.json
---

# Turn 423 — AI-Designer

Write
ttrpg_idealization/06_brainstorming_logs_and_roadmap/sim_opposed_tier_profiles.py
64 lines
open
sim_opposed_tier_profiles.py
PYTHON
from itertools import product
from math import factorial
from pathlib import Path
from bisect import bisect_left
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path('/home/user/ttrpg_idealization')
OUT=ROOT/'02_comparative_system_analysis/24_opposed_tier_profile_probability.md'
IMG=ROOT/'02_comparative_system_analysis/24_opposed_tier_profile_probability.png'
PROFILES=[('Trained',8,3),('Veteran',8,4),('Master',10,6),('Hero',10,8),('Legend',12,9)]

def compositions(total,parts,prefix=()):
 if parts==1: yield prefix+(total,); return
 for n in range(total+1): yield from compositions(total-n,parts-1,prefix+(n,))

def distribution(sides,pool):
 rows=[]; weights=[]; facts=[factorial(i) for i in range(pool+1)]
 for counts in compositions(pool,sides):
  vals=[]
  for face,count in enumerate(counts,1): vals += [face]*count
  vals.sort(reverse=True)
  w=factorial(pool)
  for c in counts:w//=facts[c]
  rows.append(tuple(vals)); weights.append(w/(sides**pool))
 pairs=sorted(zip(rows,weights))
 keys=[x[0] for x in pairs]
 prefix=[]; total=0
 for _,w in pairs: total+=w; prefix.append(total)
 return keys,prefix

cache={label:distribution(s,p) for label,s,p in PROFILES}

def compare(a,b):
 ak,ap=cache[a]; bk,bp=cache[b]
 wins=ties=0.0
 for key,w in zip(ak,ap):
  i=bisect_left(bk,key)
  less=bp[i-1] if i else 0.0
  eq=(bp[i]-bp[i-1]) if i<len(bp) else 0.0
  wins+=w*less; ties+=w*eq
 return wins,1-wins,ties

matrix=[]; rows=[]
for a,_,_ in PROFILES:
 vals=[]
 for d,_,_ in PROFILES:
  w,loss,t=compare(a,d); vals.append(w); rows.append((a,d,w,loss,t))
 matrix.append(vals)
text='''# Opposed Probability by Tier Profile\n\n**Status:** Phase 1 research artifact; no opposed probability target is canonical.\n\n## Profiles\n\nThese profiles use the current provisional fully equipped Dice Pools:\n\n| Tier | Die Size | Final Pool |\n|---|---:|---:|\n| Trained | d8 | 3d8 |\n| Veteran | d8 | 4d8 |\n| Master | d10 | 6d10 |\n| Hero | d10 | 8d10 |\n| Legend | d12 | 9d12 |\n\n## Procedure\n\n- Sort each final Dice Pool from highest to lowest.\n- Compare the highest results.\n- Continue through lower results if tied.\n- Defender wins complete ties.\n- No Floors, Boons, Banes, Automatic Successes, or special Class/Equipment Permissions are applied.\n\nThe tables use exact multinomial distributions of sorted dice, not Monte Carlo sampling.\n\n## Attacker Win Probability\n\nRows are Attacker Tier; columns are Defender Tier.\n\n| Attacker \\\ Defender | Trained | Veteran | Master | Hero | Legend |\n|---|---:|---:|---:|---:|---:|\n'''
for (a,_,_),vals in zip(PROFILES,matrix):text+=f'| {a} | '+' | '.join(f'{v*100:.2f}%' for v in vals)+' |\n'
text+='''\n## Raw Tie Probability\n\n| Attacker \\\ Defender | Trained | Veteran | Master | Hero | Legend |\n|---|---:|---:|---:|---:|---:|\n'''
for a,_,_ in PROFILES:
 vals=[]
 for d,_,_ in PROFILES: vals.append(compare(a,d)[2])
 text+=f'| {a} | '+' | '.join(f'{v*100:.2f}%' for v in vals)+' |\n'
text+='''\n## Interpretation\n\n- Because the defender wins ties, mirror matchups produce attacker win rates below 50%.\n- Higher Dice Pool and Die Size progression creates a strong diagonal advantage across Tiers.\n- This artifact isolates the raw opposed-roll engine. Future passes may add equipment variation, Boons, Banes, Automatic Successes, defenses, and Class/Feat Permissions.\n'''
OUT.write_text(text)
arr=np.array(matrix)*100
fig,ax=plt.subplots(figsize=(8,6)); im=ax.imshow(arr,vmin=0,vmax=100,cmap='RdYlGn'); ax.set_xticks(range(5),[x[0] for x in PROFILES]); ax.set_yticks(range(5),[x[0] for x in PROFILES]); ax.set_xlabel('Defender Tier'); ax.set_ylabel('Attacker Tier'); ax.set_title('Attacker Win Probability by Tier Profile\nDefender Wins Ties');
for i in range(5):
 for j in range(5): ax.text(j,i,f'{arr[i,j]:.1f}%',ha='center',va='center',color='black' if 25<arr[i,j]<75 else 'white',fontsize=9)
fig.colorbar(im,ax=ax,label='Attacker win probability'); fig.tight_layout(); fig.savefig(IMG,dpi=180); print(OUT);print(IMG)

Open
Ran commands
5

Completed the opposed Tier-profile probability pass.

Research artifact
text
02_comparative_system_analysis/24_opposed_tier_profile_probability.md
Chart
text
02_comparative_system_analysis/24_opposed_tier_profile_probability.png
Script
text
06_brainstorming_logs_and_roadmap/sim_opposed_tier_profiles.py
Profiles used
Tier	Pool
Trained	3d8
Veteran	4d8
Master	6d10
Hero	8d10
Legend	9d12

The calculation uses exact multinomial distributions of sorted dice.

Procedure modeled
Sort both pools from highest to lowest.
Compare the highest faces.
Continue through lower faces when tied.
Defender wins complete ties.
No Floors, Boons, Banes, Automatic Successes, or special Permissions are included.

The artifact contains:

Attacker-win probability matrix.
Raw tie-probability matrix.
Tier-by-Tier comparisons.
A heatmap showing Attacker win probability by Attacker and Defender Tier.

The Phase 1 Checklist was updated to mark this opposed-probability pass complete.
