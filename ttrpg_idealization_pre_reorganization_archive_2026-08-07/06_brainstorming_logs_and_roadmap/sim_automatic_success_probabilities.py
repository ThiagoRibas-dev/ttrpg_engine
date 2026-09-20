from collections import defaultdict
from pathlib import Path
import matplotlib.pyplot as plt

ROOT=Path('/home/user/ttrpg_idealization')
OUT=ROOT/'02_comparative_system_analysis/20_automatic_success_probability_tables.md'
IMG=ROOT/'02_comparative_system_analysis/20_automatic_success_probability.png'

def dist(sides,pool,keep):
 states={():1}
 for _ in range(pool):
  nxt=defaultdict(int)
  for state,c in states.items():
   for face in range(1,sides+1): nxt[tuple(sorted(state+(face,),reverse=True)[:keep])]+=c
  states=nxt
 return states

def pvec(sides,pool,vec):
 if not vec:return 1.0
 req=tuple(sorted(vec,reverse=True)); d=dist(sides,pool,len(req)); total=sides**pool
 return sum(c for vals,c in d.items() if all(vals[i]>=req[i] for i in range(len(req))))/total

def fmt(p):return f'{p*100:.2f}%'

def reduced(vec,auto):return tuple(sorted(vec,reverse=True)[auto:])

vectors=[(5,),(5,4),(5,5),(6,5,3),(9,8,7),(12,11)]
pools=[(3,8),(4,8),(5,8),(6,10),(8,10),(9,12),(10,12)]
text='''# Automatic Success Probability Tables

**Status:** Phase 1 research artifact; no Automatic Success sources or limits are canonical.

## Model

An Automatic Success satisfies the highest remaining threshold in a Difficulty Vector before ordinary dice are evaluated.

```text
DC 12,11 +1 Automatic Success → DC 11
DC 12,11,9 +2 Automatic Successes → DC 9
```

The remaining vector is resolved using the ordinary Difficulty Vector procedure. If all thresholds are removed, the task succeeds automatically. In opposed contests, compare Automatic Success totals before rolling dice; equal totals proceed to normal dice resolution.

## Vector Reductions

| Original Vector | 0 Auto | 1 Auto | 2 Auto | 3 Auto |
|---|---|---|---|---|
'''
for v in vectors:
 text+=f'| DC {",".join(map(str,v))} | DC {",".join(map(str,v))} | '+ ' | '.join('Automatic Success' if len(reduced(v,a))==0 else 'DC '+','.join(map(str,reduced(v,a))) for a in [1,2,3])+' |\n'
text+='''\n## Pool Probability Tables\n\nEach cell is the probability of completing the remaining vector with the listed pool.\n\n| Pool | Vector | 0 Auto | 1 Auto | 2 Auto | 3 Auto |\n|---|---|---:|---:|---:|---:|\n'''
for sides,pool in pools:
 for v in vectors:
  vals=[fmt(pvec(sides,pool,reduced(v,a))) for a in range(4)]
  text+=f'| {pool}d{sides} | DC {",".join(map(str,v))} | '+' | '.join(vals)+' |\n'
text+='''\n## Interpretation\n\n- Automatic Successes do not add dice or change the Dice Pool.
- They remove the highest thresholds from the Difficulty Vector.
- This pass measures mathematical impact only; it does not decide which future content grants Automatic Successes.
- These results should be read alongside the Difficulty Vector matrices and the full Level 1–20 progression research.
\n## Related Artifacts\n\n- `14_difficulty_vector_probability_matrices.md` — generic vector probabilities.
- `16_generic_pool_volume_probability_matrices.md` — pool-volume effects.
- `17_generic_die_size_probability_matrices.md` — die-size effects.
- `18_full_level_1_20_probability_progression.md` — provisional level progression.
- `19_opposed_probability_tables.md` — opposed checks and ties.
'''
OUT.write_text(text)
# chart: selected vectors DC12,11 and DC6,5,3 over pools
labels=['0 Auto','1 Auto','2 Auto','3 Auto']; vec=(12,11); x=[]
for sides,pool in pools:
 x.append(f'{pool}d{sides}')
vals=[[pvec(sides,pool,reduced(vec,a))*100 for sides,pool in pools] for a in range(4)]
plt.figure(figsize=(11,6));
for i,name in enumerate(labels):plt.plot(x,vals[i],marker='o',label=name)
plt.ylim(0,105);plt.ylabel('Probability of Success (%)');plt.xlabel('Dice Pool');plt.title('Automatic Success Reduction — DC 12,11');plt.grid(axis='y',alpha=.25);plt.legend();plt.tight_layout();plt.savefig(IMG,dpi=180)
print(OUT);print(IMG)
