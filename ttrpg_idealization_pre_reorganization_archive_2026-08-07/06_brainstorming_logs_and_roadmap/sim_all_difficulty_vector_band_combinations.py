from collections import defaultdict
from itertools import combinations_with_replacement
from pathlib import Path
import matplotlib.pyplot as plt

ROOT=Path('/home/user/ttrpg_idealization')
OUT=ROOT/'02_comparative_system_analysis/22_all_probability_band_vector_combinations.md'
IMG=ROOT/'02_comparative_system_analysis/22_all_probability_band_combinations.png'
PROFILES=[('3d8',8,3),('4d8',8,4),('6d10',10,6),('8d10',10,8),('9d12',12,9)]
BANDS={'Easy':(.80,.95),'Medium':(.60,.75),'Hard':(.40,.55)}

def dist(sides,pool,keep):
 states={():1}
 for _ in range(pool):
  nxt=defaultdict(int)
  for state,c in states.items():
   for face in range(1,sides+1): nxt[tuple(sorted(state+(face,),reverse=True)[:keep])]+=c
  states=nxt
 return states

def all_matches(sides,pool,low,high):
 matches=[]
 for length in range(1,pool+1):
  d=dist(sides,pool,length); total=sides**pool
  for v in combinations_with_replacement(range(2,sides+1),length):
   req=tuple(sorted(v,reverse=True))
   p=sum(c for vals,c in d.items() if all(vals[i]>=req[i] for i in range(length)))/total
   if low<=p<=high: matches.append((req,p))
 return matches

text='''# All Difficulty-Vector Combinations Within Probability Bands\n\n**Status:** Phase 1 research artifact; exploratory calibration only.\n\n**Target bands:**\n\n```text\nEasy:   80–95%\nMedium: 60–75%\nHard:   40–55%\n```\n\n**Profiles:** `3d8`, `4d8`, `6d10`, `8d10`, and `9d12`.\n\nVectors may contain from one threshold up to as many thresholds as there are dice in the pool. Thresholds are sorted from highest to lowest and compared positionally against the sorted Dice Pool.\n\nThis artifact is intentionally exhaustive. It is meant to let designers choose a useful subset of vectors rather than prescribe one final difficulty table.\n\n'''
results={}
for label,sides,pool in PROFILES:
 results[label]={}
 text+=f'## {label}\n\n'
 for name,(lo,hi) in BANDS.items():
  ms=all_matches(sides,pool,lo,hi); results[label][name]=ms
  text+=f'### {name} ({lo*100:.0f}–{hi*100:.0f}%)\n\n**Matching vectors:** {len(ms)}\n\n| Vector | Probability | Length |\n|---|---:|---:|\n'
  for v,p in ms: text+=f'| DC {",".join(map(str,v))} | {p*100:.2f}% | {len(v)} |\n'
  text+='\n'
text+='''## Selection Guidance\n\n- Short vectors create difficulty through high individual thresholds.\n- Long vectors create difficulty through the need for several successful dice.\n- Vectors with similar probabilities may gate different capabilities: high Die Size versus high Dice Pool Volume.\n- This artifact does not apply Floors, Automatic Successes, Boons, Banes, opposed contests, equipment-specific eligibility, or content Permissions.\n'''
OUT.write_text(text)
# Holistic visualization: all matching vectors as probability strips by vector length.
fig,axes=plt.subplots(len(PROFILES),1,figsize=(14,18),sharex=True)
if len(PROFILES)==1: axes=[axes]
colors={'Easy':'#2ca02c','Medium':'#ff9900','Hard':'#d62728'}
for ax,(label,sides,pool) in zip(axes,PROFILES):
 for name,(lo,hi) in BANDS.items():
  ms=results[label][name]
  xs=[len(v)+(i%7-3)*.012 for i,(v,p) in enumerate(ms)]
  ys=[p*100 for v,p in ms]
  ax.scatter(xs,ys,s=7,alpha=.45,color=colors[name],label=name if label==PROFILES[0][0] else None)
  ax.axhspan(lo*100,hi*100,color=colors[name],alpha=.06)
 ax.set_title(label); ax.set_ylim(0,100); ax.set_ylabel('%')
 ax.grid(axis='y',alpha=.2)
axes[-1].set_xlabel('Difficulty Vector Length (number of thresholds)')
axes[0].legend(loc='upper right'); fig.suptitle('All Difficulty Vectors Within Target Probability Bands',y=.995); fig.tight_layout(); fig.savefig(IMG,dpi=180)
print(OUT); print(IMG)
