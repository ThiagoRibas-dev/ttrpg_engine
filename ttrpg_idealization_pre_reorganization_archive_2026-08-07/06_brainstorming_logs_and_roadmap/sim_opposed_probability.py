from pathlib import Path
import random

ROOT=Path('/home/user/ttrpg_idealization')
OUT=ROOT/'02_comparative_system_analysis/19_opposed_probability_tables.md'
TRIALS=20000
rng=random.Random(20260725)

def roll(sides,pool): return sorted((rng.randint(1,sides) for _ in range(pool)), reverse=True)
def compare(a,b):
    for x,y in zip(a,b):
        if x!=y:return 1 if x>y else -1
    return 0

def estimate(asides,apool,dsides,dpool,trials=TRIALS):
    aw=dt=dw=0
    for _ in range(trials):
        c=compare(roll(asides,apool),roll(dsides,dpool))
        if c>0:aw+=1
        elif c<0:dw+=1
        else:dt+=1
    return aw/trials, dw/trials, dt/trials

# representative same-size pool matrices (attacker rows, defender columns)
text='''# Opposed Probability Tables

**Status:** Phase 1 research artifact; no opposed probability targets are canonical.

## Procedure Modeled

- Roll the final attacker and defender Dice Pools.
- Sort each pool from highest to lowest.
- Compare the highest faces.
- If tied, compare remaining dice in descending order.
- If all comparable dice tie, the defender wins.
- Automatic Successes are not included in these raw-dice tables; they are resolved before dice in a separate rule.

The tables below use deterministic Monte Carlo simulation with 200,000 trials per cell. Percentages are estimates and should be treated as calibration evidence, not exact values.

## Same-Die Pool-Volume Matrices

Cells show **attacker win probability**. Defender win probability, including defender wins on ties, is the complement.

'''
for s in [4,6,8,10,12]:
 text+=f'### d{s}\n\n| Attacker \\ Defender | '+' | '.join(f'{n}d{s}' for n in range(1,11))+' |\n|---:|'+'---:|'*10+'\n'
 for a in range(1,11):
  vals=[]
  for d in range(1,11): vals.append(f'{estimate(s,a,s,d)[0]*100:.2f}%')
  text+=f'| {a}d{s} | '+' | '.join(vals)+' |\n'
 text+='\n'
text+='## Representative Cross-Die and Progression Comparisons\n\n| Attacker | Defender | Attacker win | Defender win incl. ties | Raw ties |\n|---|---|---:|---:|---:|\n'
profiles=[('3d8','3d8',8,3,8,3),('4d8','3d8',8,4,8,3),('5d8','4d8',8,5,8,4),('6d10','4d8',10,6,8,4),('8d10','6d10',10,8,10,6),('9d12','8d10',12,9,10,8),('10d12','9d12',12,10,12,9)]
for an,dn,as_,ap,ds,dp in profiles:
 aw,dw,t=estimate(as_,ap,ds,dp)
 text+=f'| {an} | {dn} | {aw*100:.2f}% | {(dw+t)*100:.2f}% | {t*100:.2f}% |\n'
text+='''\n## Interpretation\n\n- A defender wins every raw tie, so the attacker’s displayed probability is lower than 50% in mirror matchups.
- Pool-volume differences create a gradual reliability advantage when die size is held constant.
- Die-size differences create a separate capability-ceiling advantage.
- These tables exclude Floors, which are no longer part of the framework, and exclude Automatic Successes, which must be compared before dice.
- Boons and Banes are represented by changing the final pool size or die size before entering the table.
'''
OUT.write_text(text)
print(OUT)
