from collections import defaultdict
from itertools import combinations_with_replacement
from pathlib import Path

OUT=Path('/home/user/ttrpg_idealization/02_comparative_system_analysis/21_tier_difficulty_vector_convention_table.md')

def dist(sides,pool,keep):
 states={():1}
 for _ in range(pool):
  nxt=defaultdict(int)
  for state,c in states.items():
   for face in range(1,sides+1): nxt[tuple(sorted(state+(face,),reverse=True)[:keep])]+=c
  states=nxt
 return states
_cache={}
def pvec(sides,pool,vec):
 req=tuple(sorted(vec,reverse=True)); key=(sides,pool,len(req))
 if key not in _cache:_cache[key]=dist(sides,pool,len(req))
 d=_cache[key]; total=sides**pool
 return sum(c for vals,c in d.items() if all(vals[i]>=req[i] for i in range(len(req))))/total

bands={'Easy':(.80,.85,(1,1)),'Medium':(.60,.65,(1,2)),'Hard':(.40,.45,(2,3))}
profiles=[]
for level in range(1,21):
 if level<=4: tier,rank,sides,base,equip='Trained','Trained',8,2,1
 elif level<=8: tier,rank,sides,base,equip='Veteran','Veteran',8,3,1
 elif level<=12: tier,rank,sides,base,equip='Master','Master',10,4,2
 elif level<=16: tier,rank,sides,base,equip='Hero','Hero',10,5,3
 else: tier,rank,sides,base,equip='Legend','Legend',12,6,3
 profiles.append((level,tier,rank,sides,base,equip,base+equip))

def candidates(sides,pool,band):
 lo,hi,lengths=band; out=[]
 for length in range(lengths[0],lengths[1]+1):
  if length>pool:continue
  for vec in combinations_with_replacement(range(2,13),length):
   vec=tuple(sorted(vec,reverse=True)); p=pvec(sides,pool,vec)
   if lo<=p<=hi: out.append((abs(p-(lo+hi)/2),length,vec,p))
 out.sort(key=lambda x:(x[0],x[1],x[2]))
 # choose up to 3 diverse options: closest of each supported length, then closest remaining
 selected=[]
 for length in range(lengths[0],lengths[1]+1):
  matches=[x for x in out if x[1]==length]
  if matches:selected.append(matches[0])
 for x in out:
  if len(selected)>=3:break
  if x not in selected:selected.append(x)
 return selected

text='''# Tier Difficulty-Vector Convention Table\n\n**Status:** Phase 1 research artifact; provisional calibration table.\n\n**Convention:**\n\n- Easy always uses one threshold.\n- Medium uses one or two thresholds.\n- Hard uses two or three thresholds.\n- Multiple viable vectors in one cell are separated by `/`.\n\n**Target bands:** Easy 80–85%; Medium 60–65%; Hard 40–45%.\n\n**Equipment assumption:** Uses the current provisional fully equipped progression. Equipment Boons are represented as additional same-size dice.\n\n**No Floor mechanic is applied.**\n\n| Tier | Character Level | Competency Rank | Dice Size (Attribute) | Pool Size | Equipment Boons | Pool Size + Equipment | Easy DC | Medium DC | Hard DC |\n|---|---:|---|---:|---:|---:|---:|---|---|---|\n'''
for level,tier,rank,sides,base,equip,pool in profiles:
 cells=[]
 for name in ['Easy','Medium','Hard']:
  cs=candidates(sides,pool,bands[name])
  formatted=[]
  for _,_,vec,p in cs: formatted.append(f'DC {",".join(map(str,vec))} ({p*100:.2f}%)')
  cells.append(' / '.join(formatted) if formatted else 'NA')
 text+=f'| {tier} | {level} | {rank} | d{sides} | {base} | +{equip}B | {pool}d{sides} | {cells[0]} | {cells[1]} | {cells[2]} |\n'
text+='''\n## Reading Notes\n\nEach vector is selected from the exact probability matrices in `14_difficulty_vector_probability_matrices.md` and the generic pool-volume references in `16_generic_pool_volume_probability_matrices.md`. The percentages are included for review and are not canonical rules.\n\nThe multiple alternatives show different capability gates with similar probabilities. For example, a one-threshold Medium vector emphasizes reaching a high numerical threshold, while a two-threshold Medium vector requires two strong dice.\n'''
OUT.write_text(text); print(OUT)
