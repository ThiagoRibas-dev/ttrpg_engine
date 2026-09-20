---
turn: 401
role: "AI-Designer"
source: chat_history.json
---

# Turn 401 — AI-Designer

Write
ttrpg_idealization/06_brainstorming_logs_and_roadmap/sim_all_difficulty_vector_band_combinations_exact.py
49 lines
open
sim_all_difficulty_vector_band_combinations_exact.py
PYTHON
from itertools import combinations_with_replacement
from math import factorial
from pathlib import Path
import numpy as np

OUT=Path('/home/user/ttrpg_idealization/02_comparative_system_analysis/22_all_probability_band_vector_combinations.md')
PROFILES=[('3d8',8,3),('4d8',8,4),('6d10',10,6),('8d10',10,8),('9d12',12,9)]
BANDS={'Easy':(.80,.95),'Medium':(.60,.75),'Hard':(.40,.55)}

def compositions(total, parts, prefix=()):
    if parts==1:
        yield prefix+(total,); return
    for n in range(total+1): yield from compositions(total-n,parts-1,prefix+(n,))

def histogram_states(sides,pool):
    rows=[]; weights=[]; fact=factorial(pool)
    facts=[factorial(i) for i in range(pool+1)]
    for counts in compositions(pool,sides):
        vals=[]
        for face,count in enumerate(counts,1): vals += [face]*count
        vals.sort(reverse=True)
        rows.append(vals)
        w=fact
        for c in counts:w//=facts[c]
        weights.append(w)
    return np.asarray(rows,dtype=np.int8), np.asarray(weights,dtype=np.float64)/(sides**pool)

def matches(sides,pool,low,high):
    allmatches=[]
    for length in range(1,pool+1):
        rolls,weights=histogram_states(sides,pool)
        rolls=rolls[:,:length]
        vectors=list(combinations_with_replacement(range(2,sides+1),length))
        for start in range(0,len(vectors),1024):
            batch=np.asarray([tuple(reversed(v)) for v in vectors[start:start+1024]],dtype=np.int8)
            probs=((rolls[:,None,:]>=batch[None,:,:]).all(axis=2)*weights[:,None]).sum(axis=0)
            for v,p in zip(vectors[start:start+1024],probs):
                if low<=p<=high: allmatches.append((tuple(reversed(v)),float(p)))
    return allmatches

text='# All Difficulty-Vector Combinations Within Probability Bands\n\n**Status:** Phase 1 research artifact; exhaustive exact multinomial calculation.\n\n**Bands:** Easy 80–95%; Medium 60–75%; Hard 40–55%.\n\n**Thresholds:** DC 2 through DC 12 only.\n\n**Vectors:** Every length from one threshold through the full Dice Pool length.\n\nEach pool’s results are generated from exact multinomial counts of all face histograms, avoiding brute-force enumeration of every ordered roll.\n\n'
for label,sides,pool in PROFILES:
    text+=f'## {label}\n\n'
    for name,(lo,hi) in BANDS.items():
        ms=matches(sides,pool,lo,hi); text+=f'### {name} ({lo*100:.0f}–{hi*100:.0f}%)\n\n**Matching vectors:** {len(ms)}\n\n| Vector | Probability | Length |\n|---|---:|---:|\n'
        for v,p in ms:text+=f'| DC {",".join(map(str,v))} | {p*100:.2f}% | {len(v)} |\n'
        text+='\n'
OUT.write_text(text); print(OUT)

Open
used
Bash
exit -1 386s

The exact exhaustive calculation is still too expensive in its current form.

The new script does use a multinomial approach rather than brute-forcing ordered dice rolls, but the requested search space is still enormous:

text
All vectors
× all lengths from 1 through pool size
× DC values 2 through 12
× 9d12 histogram states

The run was terminated after roughly six and a half minutes without completing.

The bottleneck is not individual dice probability. It is evaluating every possible threshold vector against every possible multinomial outcome state, especially for:

text
9d12

with vectors up to length 9.

The script is here:

text
06_brainstorming_logs_and_roadmap/sim_all_difficulty_vector_band_combinations_exact.py

but it did not produce a completed artifact.

The next implementation needs a more specialized dynamic-programming method that calculates the probability of a vector directly from its nested threshold categories, instead of comparing every candidate vector against every outcome histogram.

I do not want to substitute approximate Monte Carlo without your approval, because vectors near the probability-band boundaries could be incorrectly included or excluded.
