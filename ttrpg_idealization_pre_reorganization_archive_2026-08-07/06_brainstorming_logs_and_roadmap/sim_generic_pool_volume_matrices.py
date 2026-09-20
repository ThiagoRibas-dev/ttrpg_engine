from collections import defaultdict
from pathlib import Path

OUT = Path('/home/user/ttrpg_idealization/02_comparative_system_analysis/16_generic_pool_volume_probability_matrices.md')

def top_distribution(sides, pool, keep=3):
    states={():1}
    for _ in range(pool):
        nxt=defaultdict(int)
        for state,count in states.items():
            for face in range(1,sides+1):
                nxt[tuple(sorted(state+(face,),reverse=True)[:keep])]+=count
        states=nxt
    return states

def single(sides,pool,dc):
    # exact P(max >= dc)
    if dc <= 1: return 1.0
    if dc > sides: return 0.0
    return 1-((dc-1)/sides)**pool

def vector(sides,pool,vec):
    req=tuple(sorted(vec,reverse=True))
    if pool < len(req): return None
    dist=top_distribution(sides,pool,len(req)); total=sides**pool
    return sum(c for vals,c in dist.items() if all(vals[i]>=req[i] for i in range(len(req))))/total

def pct(p): return '—' if p is None else f'{p*100:.2f}%'

text='''# Generic Dice-Pool Volume Probability Matrices

**Status:** Phase 1 research artifact; no probability targets or Difficulty Vector assignments are canonical.

**Purpose:** Isolate the effect of Dice Pool Volume while keeping Die Size fixed. These matrices are generic references for Competency, Equipment, Boons, Banes, Feats, Spells, and other effects that add or remove dice.

## Single-Threshold Matrices

Each cell is `P(max ≥ DC)` for an `NdS` pool. No Floor mechanic, Boons, Banes, Automatic Successes, or opposed checks are applied.

'''
for sides in [4,6,8,10,12]:
 text+=f'## d{sides}\n\n| Pool | '+' | '.join(f'DC {d}' for d in range(2,13))+' |\n|---:|'+'---:|'*11+'\n'
 for n in range(1,13):
  text+=f'| {n}d{sides} | '+' | '.join(pct(single(sides,n,d)) for d in range(2,13))+' |\n'
 text+='\n'
text+='''## Representative Difficulty Vectors by Pool Volume

These reference columns show how selected vectors change as pool volume increases. A vector requires at least as many dice as it has thresholds.

'''
for sides in [4,6,8,10,12]:
 text+=f'## d{sides} Vector Curves\n\n| Pool | DC 5,4 | DC 5,5 | DC 6,5,3 |\n|---:|---:|---:|---:|\n'
 for n in range(1,13):
  text+=f'| {n}d{sides} | {pct(vector(sides,n,(5,4)))} | {pct(vector(sides,n,(5,5)))} | {pct(vector(sides,n,(6,5,3)))} |\n'
 text+='\n'
text+='''## Interpretation

- Increasing pool volume improves reliability without changing the numerical face ceiling.
- The same matrices apply regardless of whether extra dice came from Competency, Equipment, Boons, or another source.
- Banes use the same pool-volume rows after removing dice, except for the special one-die Die Step-Down rule.
- Die Step-Up and Die Step-Down are handled by comparing the same pool volume across different die-size sections.
- These tables are raw probability references and are not final target recommendations.
'''
OUT.write_text(text)
print(OUT)
