---
turn: 331
role: "AI-Designer"
source: chat_history.json
---

# Turn 331 — AI-Designer

used
Bash
timeout 30s
Write
ttrpg_idealization/06_brainstorming_logs_and_roadmap/plot_provisional_tier_vectors.py
27 lines
open
plot_provisional_tier_vectors.py
PYTHON
from collections import defaultdict
from pathlib import Path
import matplotlib.pyplot as plt

def dist(sides,pool,keep):
 states={():1}
 for _ in range(pool):
  nxt=defaultdict(int)
  for state,c in states.items():
   for face in range(1,sides+1): nxt[tuple(sorted(state+(face,),reverse=True)[:keep])]+=c
  states=nxt
 return states

def pvec(sides,pool,vec):
 req=sorted(vec,reverse=True); d=dist(sides,pool,len(req)); total=sides**pool
 return sum(c for vals,c in d.items() if all(vals[i]>=req[i] for i in range(len(req))))/total
rows=[(1,'Trained',8,3,(5,),(5,4),(5,5)),(5,'Veteran',8,4,(6,),(6,5),(6,6)),(9,'Master',10,6,(8,),(9,7),(10,)),(13,'Hero',10,8,(9,),(9,8),(9,9)),(17,'Legend',12,9,(11,),(11,10),(12,))]
curves={k:[] for k in ['Easy','Medium','Hard']}
for lvl,tier,sides,pool,e,m,h in rows:
 for name,vec in [('Easy',e),('Medium',m),('Hard',h)]: curves[name].append(pvec(sides,pool,vec)*100)
plt.figure(figsize=(11,6.5)); colors={'Easy':'#2ca02c','Medium':'#ff9900','Hard':'#d62728'}
for name in curves:
 plt.plot([r[0] for r in rows],curves[name],marker='o',linewidth=2,color=colors[name],label=name)
 for x,y in zip([r[0] for r in rows],curves[name]): plt.annotate(f'{y:.1f}%',(x,y),textcoords='offset points',xytext=(0,8),ha='center',fontsize=8)
for y in [82.5,62.5,42.5]: plt.axhline(y,ls='--',alpha=.25,color='gray')
plt.xticks([r[0] for r in rows],[f'L{r[0]}\n{r[1]}' for r in rows]); plt.ylim(0,100); plt.ylabel('Probability of Success (%)'); plt.xlabel('Representative Tier Entry Level'); plt.title('Provisional Difficulty Vectors — Fully Equipped Progression\nRaw Dice Probability, No Floor Applied'); plt.grid(axis='y',alpha=.25); plt.legend(); plt.tight_layout(); out=Path('/home/user/ttrpg_idealization/02_comparative_system_analysis/15_provisional_tier_difficulty_vectors.png'); plt.savefig(out,dpi=180); print(out)

Open
used
Bash
983ms

Created and plotted:

text
02_comparative_system_analysis/15_provisional_tier_difficulty_vectors.png

The chart uses the representative Tier-entry levels:

text
Level 1  — Trained
Level 5  — Veteran
Level 9  — Master
Level 13 — Hero
Level 17 — Legend

It plots the success probability of your provisional vectors using the fully equipped pools:

Tier	Pool	Easy	Medium	Hard
Trained	3d8	DC 5	DC 5,4	DC 5,5
Veteran	4d8	DC 6	DC 6,5	DC 6,6
Master	6d10	DC 8	DC 9,7	DC 10
Hero	8d10	DC 9	DC 9,8	DC 9,9
Legend	9d12	DC 11	DC 11,10	DC 12

The chart uses raw dice probability without applying Floors, since you are reconsidering whether Floors are necessary.

The plotting script is:

text
06_brainstorming_logs_and_roadmap/plot_provisional_tier_vectors.py

This chart should make it easier to decide whether the vector progression is producing the intended curve before we commit to keeping or removing Floors.
