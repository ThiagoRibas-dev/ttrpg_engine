from collections import defaultdict
from pathlib import Path
import matplotlib.pyplot as plt

ROOT=Path('/home/user/ttrpg_idealization')
OUT=ROOT/'02_comparative_system_analysis/18_full_level_1_20_probability_progression.md'
IMG=ROOT/'02_comparative_system_analysis/18_full_level_1_20_probability_progression.png'

def dist(sides,pool,keep):
 states={():1}
 for _ in range(pool):
  nxt=defaultdict(int)
  for state,c in states.items():
   for face in range(1,sides+1):
    nxt[tuple(sorted(state+(face,),reverse=True)[:keep])]+=c
  states=nxt
 return states

def pvec(sides,pool,vec):
 req=tuple(sorted(vec,reverse=True)); d=dist(sides,pool,len(req)); total=sides**pool
 return sum(c for vals,c in d.items() if all(vals[i]>=req[i] for i in range(len(req))))/total

profiles=[]
for level in range(1,21):
 if level<=4: tier,rank,sides,base,equip='Trained','Trained',8,2,1
 elif level<=8: tier,rank,sides,base,equip='Veteran','Veteran',8,3,1
 elif level<=12: tier,rank,sides,base,equip='Master','Master',10,4,2
 elif level<=16: tier,rank,sides,base,equip='Hero','Hero',10,5,3
 else: tier,rank,sides,base,equip='Legend','Legend',12,6,3
 profiles.append((level,tier,rank,sides,base,equip,base+equip))
vecs={'Easy':(5,), 'Medium':(5,4), 'Hard':(5,5)}
# tier vectors from provisional per-tier table
vecs_by_tier={
 'Trained':{'Easy':(5,), 'Medium':(5,4), 'Hard':(5,5)},
 'Veteran':{'Easy':(6,), 'Medium':(6,5), 'Hard':(6,6)},
 'Master':{'Easy':(8,), 'Medium':(9,7), 'Hard':(10,)},
 'Hero':{'Easy':(9,), 'Medium':(9,8), 'Hard':(9,9)},
 'Legend':{'Easy':(11,), 'Medium':(11,10), 'Hard':(12,)},
}
rows=[]
for level,tier,rank,sides,base,equip,pool in profiles:
 vals=[]
 for name in ['Easy','Medium','Hard']:
  vals.append(pvec(sides,pool,vecs_by_tier[tier][name]))
 rows.append((level,tier,rank,sides,base,equip,pool,*vals))
text='''# Full Level 1–20 Probability Progression\n\n**Status:** Phase 1 research artifact; no equipment progression or Difficulty Vector assignment is canonical.\n\n**Purpose:** Apply the current provisional fully equipped progression and provisional per-Tier Difficulty Vectors across every Character Level.\n\n**No Floor mechanic is applied.** Probabilities use the final raw Dice Pool and the ordered Difficulty Vectors.\n\n| Level | Tier | Rank | Attribute Die | Baseline Pool | Equipment Dice | Final Pool | Easy Vector | Easy % | Medium Vector | Medium % | Hard Vector | Hard % |\n|---:|---|---|---:|---:|---:|---:|---|---:|---|---:|---|---:|\n'''
for level,tier,rank,sides,base,equip,pool,e,m,h in rows:
 v=vecs_by_tier[tier]
 text+=f'| {level} | {tier} | {rank} | d{sides} | {base}d | +{equip}B | {pool}d{sides} | DC {",".join(map(str,v["Easy"]))} | {e*100:.2f}% | DC {",".join(map(str,v["Medium"]))} | {m*100:.2f}% | DC {",".join(map(str,v["Hard"]))} | {h*100:.2f}% |\n'
text+='''\n## Interpretation\n\n- Consecutive levels within a Tier share the same provisional mathematical profile in this pass.\n- The resulting stair-step chart reflects the current assumption that Attribute Die, Competency Rank, and equipment progression change primarily at Tier boundaries.\n- The table is intended to expose whether later level-by-level Class, Feat, Equipment, or Spell progression needs to create additional probability movement.\n'''
OUT.write_text(text)
colors={'Easy':'#2ca02c','Medium':'#ff9900','Hard':'#d62728'}
plt.figure(figsize=(13,7))
for i,name in enumerate(['Easy','Medium','Hard'],start=0):
 vals=[r[7+i] * 100 for r in rows]
 plt.plot(range(1,21),vals,marker='o',linewidth=2,color=colors[name],label=name)
for x in [4.5,8.5,12.5,16.5]: plt.axvline(x,color='gray',alpha=.35,ls='--')
for y,lab in [(82.5,'Easy band'),(62.5,'Medium band'),(42.5,'Hard band')]: plt.axhline(y,color='gray',alpha=.2,ls=':')
plt.xticks(range(1,21)); plt.ylim(0,100); plt.xlabel('Character Level'); plt.ylabel('Probability of Success (%)'); plt.title('Full Level 1–20 Probability Progression\nProvisional Equipped Pools and Tier Difficulty Vectors'); plt.grid(axis='y',alpha=.25); plt.legend(); plt.tight_layout(); plt.savefig(IMG,dpi=180)
print(OUT); print(IMG)
