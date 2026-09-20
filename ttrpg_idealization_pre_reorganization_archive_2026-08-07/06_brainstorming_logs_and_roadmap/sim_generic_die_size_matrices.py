from collections import defaultdict
from pathlib import Path

OUT=Path('/home/user/ttrpg_idealization/02_comparative_system_analysis/17_generic_die_size_probability_matrices.md')

def dist(sides,pool,keep=3):
 states={():1}
 for _ in range(pool):
  nxt=defaultdict(int)
  for state,count in states.items():
   for face in range(1,sides+1):
    nxt[tuple(sorted(state+(face,),reverse=True)[:keep])]+=count
  states=nxt
 return states

def single(sides,pool,dc):
 if dc<=1:return 1.0
 if dc>sides:return 0.0
 return 1-((dc-1)/sides)**pool

def vec(sides,pool,req):
 if pool<len(req):return None
 req=tuple(sorted(req,reverse=True)); d=dist(sides,pool,len(req)); total=sides**pool
 return sum(c for values,c in d.items() if all(values[i]>=req[i] for i in range(len(req))))/total

def f(x):return '—' if x is None else f'{x*100:.2f}%'
text='''# Generic Die-Size Probability Matrices

**Status:** Phase 1 research artifact; no die-size progression or probability targets are canonical.

**Purpose:** Isolate the effect of Die Size while holding Dice Pool Volume constant. These tables are generic references for Attribute advancement, Die Step-Up, Die Step-Down, Equipment, Spells, Feats, and other effects that change die size.

## Single-Threshold Matrices by Pool Volume

Each section holds pool volume constant while comparing d4, d6, d8, d10, and d12. Cells show `P(max ≥ DC)`. No Floor mechanic, Boons, Banes, Automatic Successes, or opposed checks are applied.

'''
for pool in range(1,13):
 text+=f'## {pool}-Die Pools\n\n| Die Size | '+' | '.join(f'DC {d}' for d in range(2,13))+' |\n|---|'+ '---:|'*11+'\n'
 for s in [4,6,8,10,12]: text+=f'| d{s} | '+' | '.join(f(single(s,pool,d)) for d in range(2,13))+' |\n'
 text+='\n'
 text+='## Representative Difficulty Vectors\n\n| Pool | Die Size | DC 5,4 | DC 5,5 | DC 6,5,3 |\n|---:|---:|---:|---:|---:|\n'
 for pool in range(1,13):
  for s in [4,6,8,10,12]: text+=f'| {pool}d{s} | d{s} | {f(vec(s,pool,(5,4)))} | {f(vec(s,pool,(5,5)))} | {f(vec(s,pool,(6,5,3)))} |\n'
 text+='''\n## Interpretation\n\n- Increasing Die Size raises the numerical ceiling while keeping pool volume constant.\n- Increasing Dice Pool Volume raises reliability while keeping the Die Size ceiling constant.\n- These tables allow direct comparison of Attribute Die Step-Up against additional dice from Competency, Equipment, Boons, or other effects.\n- A Die Step-Up is not a separate probability engine; it is a move between rows in these matrices.\n'''
OUT.write_text(text); print(OUT)
