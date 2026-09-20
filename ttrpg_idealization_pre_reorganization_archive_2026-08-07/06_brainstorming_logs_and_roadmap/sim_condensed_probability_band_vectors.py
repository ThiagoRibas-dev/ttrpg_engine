from collections import defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path

OUT=Path('/home/user/ttrpg_idealization/02_comparative_system_analysis/23_condensed_probability_band_vector_reference.md')
PROFILES=[('3d8',8,3),('4d8',8,4),('6d10',10,6),('8d10',10,8),('9d12',12,9)]
BANDS={'Easy':(Fraction(80,100),Fraction(95,100)), 'Medium':(Fraction(60,100),Fraction(75,100)), 'Hard':(Fraction(40,100),Fraction(55,100))}

def binom(n,k,p):
 return Fraction(comb(n,k))*p**k*(1-p)**(n-k)

def extend(state,sides,pool,previous,threshold,required):
 q=Fraction(sides-threshold+1,sides) if previous==sides+1 else Fraction(previous-threshold,previous-1)
 nxt={}
 for used,w in state.items():
  for take in range(pool-used+1):
   new=used+take
   if new<required:continue
   nxt[new]=nxt.get(new,Fraction(0))+w*binom(pool-used,take,q)
 return nxt

def all_matches(sides,pool,low,high):
 result=[]
 def dfs(prefix,max_t,previous,state):
  if len(prefix)>=pool:return
  for t in range(max_t,1,-1):
   newstate=extend(state,sides,pool,previous,t,len(prefix)+1)
   p=sum(newstate.values(),Fraction(0))
   if p<Fraction(40,100):continue
   vector=tuple(prefix+[t])
   if low<=p<=high:result.append((vector,p))
   dfs(list(vector),t,t,newstate)
 dfs([],sides,sides+1,{0:Fraction(1)})
 return result

def select(matches,low,high):
 midpoint=(low+high)/2; chosen=[]
 for length in range(1,max((len(v) for v,_ in matches),default=0)+1):
  candidates=[(v,p) for v,p in matches if len(v)==length]
  if not candidates:continue
  # midpoint, then highest minimum threshold, then lexicographically highest
  chosen.append(min(candidates,key=lambda vp:(abs(vp[1]-midpoint),-min(vp[0]),tuple(-x for x in vp[0]))))
 return chosen

text='''# Condensed Probability-Band Difficulty Vector Reference

**Status:** Phase 1 research artifact; condensed design reference.\n\n**Source:** `22_all_probability_band_vector_combinations.md`.\n\n**Bands:** Easy 80–95%; Medium 60–75%; Hard 40–55%.\n\nFor each pool, band, and available vector length, this reference selects one representative vector. The selected vector is the valid option closest to the band midpoint. Ties prefer greater threshold variety, then the highest minimum threshold, then the lexicographically highest vector.\n\nThis is a practical subset, not a replacement for the exhaustive artifact.\n\n'''
for label,sides,pool in PROFILES:
 text+=f'## {label}\n\n'
 for name,(low,high) in BANDS.items():
  chosen=select(all_matches(sides,pool,low,high),low,high)
  text+=f'### {name} ({float(low)*100:.0f}–{float(high)*100:.0f}%)\n\n| Vector Length | Vector | Probability |\n|---:|---|---:|\n'
  for v,p in chosen:text+=f'| {len(v)} | DC {",".join(map(str,v))} | {float(p)*100:.2f}% |\n'
  text+='\n'
text+='''## Reading the Reference\n\nShort vectors emphasize high Die Size. Long vectors emphasize Dice Pool Volume and the ability to produce several strong ordered results. Vectors with similar probabilities are intentionally retained as different capability gates.\n'''
OUT.write_text(text); print(OUT)
