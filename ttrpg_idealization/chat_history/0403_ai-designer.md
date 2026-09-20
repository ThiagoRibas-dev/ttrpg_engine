---
turn: 403
role: "AI-Designer"
source: chat_history.json
---

# Turn 403 — AI-Designer

Write
ttrpg_idealization/06_brainstorming_logs_and_roadmap/sim_all_difficulty_vector_band_combinations_exact.py
79 lines
open
sim_all_difficulty_vector_band_combinations_exact.py
PYTHON
from functools import lru_cache
from math import comb
from pathlib import Path

OUT=Path('/home/user/ttrpg_idealization/02_comparative_system_analysis/22_all_probability_band_vector_combinations.md')
PROFILES=[('3d8',8,3),('4d8',8,4),('6d10',10,6),('8d10',10,8),('9d12',12,9)]
BANDS={'Easy':(.80,.95),'Medium':(.60,.75),'Hard':(.40,.55)}


def binom_pmf(n,k,p):
    if k<0 or k>n:return 0.0
    return comb(n,k)*(p**k)*((1-p)**(n-k))

@lru_cache(None)
def prob_vector(sides,pool,thresholds):
    """Exact probability via nested category binomial thinning."""
    thresholds=tuple(thresholds)
    # Collapse repeated thresholds; the last occurrence gives the highest required count.
    distinct=[]
    for i,t in enumerate(thresholds,1):
        if distinct and distinct[-1][0]==t: distinct[-1]=(t,i)
        else: distinct.append((t,i))
    # categories: >= first threshold, then each interval down to the next threshold
    state={0:1.0} # cumulative dice in accepted upper categories
    previous_lower=1.0 # remaining probability mass below the prior threshold, normalized later
    previous_threshold=sides+1
    for threshold,required in distinct:
        upper=threshold
        lower=previous_threshold-1
        # interval [threshold, previous_threshold-1], or [threshold,sides] initially
        if previous_threshold==sides+1:
            interval_faces=sides-threshold+1
            remaining_faces=sides
        else:
            interval_faces=previous_threshold-threshold
            remaining_faces=threshold-1+interval_faces
        # More directly, conditional interval probability among values below prior threshold.
        if previous_threshold==sides+1:
            q=interval_faces/sides
        else:
            q=interval_faces/(previous_threshold-1)
        nxt={}
        for used,weight in state.items():
            remaining=pool-used
            for take in range(remaining+1):
                new_used=used+take
                if new_used < required: continue
                val=weight*binom_pmf(remaining,take,q)
                nxt[new_used]=nxt.get(new_used,0)+val
        state=nxt
        if not state:return 0.0
        previous_threshold=threshold
    return sum(state.values())


def all_matches(sides,pool,low,high):
    matches=[]
    def dfs(prefix,max_threshold):
        # Record current nonempty vector.
        if prefix:
            p=prob_vector(sides,pool,tuple(prefix))
            if low<=p<=high: matches.append((tuple(prefix),p))
            # Monotonic pruning: extensions cannot increase probability.
            if p<low:return
        if len(prefix)>=pool:return
        for t in range(max_threshold,1,-1):
            dfs(prefix+[t],t)
    dfs([],sides)
    return matches

text='# All Difficulty-Vector Combinations Within Probability Bands\n\n**Status:** Phase 1 research artifact; exhaustive exact multinomial/thinning-DP calculation.\n\n**Bands:** Easy 80–95%; Medium 60–75%; Hard 40–55%.\n\n**Thresholds:** DC 2 through DC 12 only.\n\n**Vectors:** Every length from one threshold through the full Dice Pool length. Repeated thresholds are retained as meaningful requirements; internally, repeated values are collapsed to their highest required count for probability calculation.\n\nThe calculation uses nested binomial thinning and monotonic branch pruning rather than enumerating ordered rolls or full sorted-roll tables.\n\n'
for label,sides,pool in PROFILES:
    text+=f'## {label}\n\n'
    for name,(lo,hi) in BANDS.items():
        ms=all_matches(sides,pool,lo,hi); text+=f'### {name} ({lo*100:.0f}–{hi*100:.0f}%)\n\n**Matching vectors:** {len(ms)}\n\n| Vector | Probability | Length |\n|---|---:|---:|\n'
        for v,p in ms:text+=f'| DC {",".join(map(str,v))} | {p*100:.2f}% | {len(v)} |\n'
        text+='\n'
OUT.write_text(text); print(OUT); print('cache entries',prob_vector.cache_info())

Open
Ran commands
3

Implemented the exact optimized multinomial/thinning-DP approach.

Script
text
06_brainstorming_logs_and_roadmap/sim_all_difficulty_vector_band_combinations_exact.py
Research artifact
text
02_comparative_system_analysis/22_all_probability_band_vector_combinations.md
Parameters

The exhaustive search uses:

text
Thresholds:
  DC 2 through DC 12

Vector lengths:
  1 through the full pool length

Pools:
  3d8
  4d8
  6d10
  8d10
  9d12

Bands:
  Easy:   80–95%
  Medium: 60–75%
  Hard:   40–55%
Calculation method

The script now uses:

Nested threshold categories.
Exact binomial thinning.
Multinomial probability logic.
Memoization.
Monotonic branch pruning.

It no longer enumerates full sorted-roll tables.

The complete run finished successfully in approximately six seconds.

The number of matching vectors found was:

Pool	Easy	Medium	Hard
3d8	7	10	15
4d8	18	19	38
6d10	164	215	482
8d10	611	885	1,755
9d12	3,319	5,104	10,732

This gives us the exhaustive design space needed to select practical subsets of vectors later.

The Phase 1 Checklist was also updated to record this completed research pass.
