from fractions import Fraction
from math import comb
from pathlib import Path

OUT=Path('/home/user/ttrpg_idealization/02_comparative_system_analysis/22_all_probability_band_vector_combinations.md')
PROFILES=[('3d8',8,3),('4d8',8,4),('6d10',10,6),('8d10',10,8),('9d12',12,9)]
BANDS={'Easy':(Fraction(80,100),Fraction(95,100)), 'Medium':(Fraction(60,100),Fraction(75,100)), 'Hard':(Fraction(40,100),Fraction(55,100))}
LOWEST_CUTOFF=Fraction(40,100)

def binom_pmf(n,k,p):
    if k<0 or k>n:return Fraction(0)
    return Fraction(comb(n,k)) * p**k * (1-p)**(n-k)

def extend_state(state, sides, pool, previous_threshold, threshold, required):
    """Add one threshold using conditional binomial thinning.

    state maps the number of dice already assigned to higher threshold bands
    to the exact probability that the prefix constraints have been met.
    """
    if previous_threshold == sides + 1:
        q=Fraction(sides-threshold+1, sides)
    else:
        q=Fraction(previous_threshold-threshold, previous_threshold-1)
    nxt={}
    for used,weight in state.items():
        remaining=pool-used
        for take in range(remaining+1):
            new_used=used+take
            if new_used < required: continue
            value=weight*binom_pmf(remaining,take,q)
            nxt[new_used]=nxt.get(new_used,Fraction(0))+value
    return nxt

def classify(probability):
    return [name for name,(low,high) in BANDS.items() if low<=probability<=high]

def profile_matches(sides,pool):
    results={name:[] for name in BANDS}
    def dfs(prefix, max_threshold, previous_threshold, state):
        if len(prefix)>=pool:return
        for threshold in range(max_threshold,1,-1):
            required=len(prefix)+1
            next_state=extend_state(state,sides,pool,previous_threshold,threshold,required)
            probability=sum(next_state.values(),Fraction(0))
            if probability < LOWEST_CUTOFF:
                continue
            vector=tuple(prefix+[threshold])
            for name in classify(probability):
                results[name].append((vector,probability))
            dfs(list(vector),threshold,threshold,next_state)
    dfs([],sides,sides+1,{0:Fraction(1)})
    return results

text='# All Difficulty-Vector Combinations Within Probability Bands\n\n**Status:** Phase 1 research artifact; exhaustive exact multinomial/thinning-DP calculation.\n\n**Bands:** Easy 80–95%; Medium 60–75%; Hard 40–55%.\n\n**Thresholds:** DC 2 through DC 12 only.\n\n**Vectors:** Every length from one threshold through the full Dice Pool length. Repeated thresholds are retained as meaningful requirements; internally, repeated values are handled by the required-count state.\n\nThe calculation uses one depth-first traversal per pool profile. Each child vector receives the parent’s exact thinning-DP state, and branches below the 40% cutoff are pruned. Exact rational arithmetic makes band-boundary inclusion deterministic.\n\n'
for label,sides,pool in PROFILES:
    text+=f'## {label}\n\n'
    results=profile_matches(sides,pool)
    for name,(low,high) in BANDS.items():
        ms=results[name]; text+=f'### {name} ({float(low)*100:.0f}–{float(high)*100:.0f}%)\n\n**Matching vectors:** {len(ms)}\n\n| Vector | Probability | Length |\n|---|---:|---:|\n'
        for v,p in ms:text+=f'| DC {",".join(map(str,v))} | {float(p)*100:.2f}% | {len(v)} |\n'
        text+='\n'
OUT.write_text(text); print(OUT)
