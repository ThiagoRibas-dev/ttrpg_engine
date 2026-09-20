from math import comb
from pathlib import Path
import matplotlib.pyplot as plt

def prob(s,n,dc,r):
 f=min(n,s-1); p=1 if dc<=f else (s-dc+1)/s
 return sum(comb(n,k)*p**k*(1-p)**(n-k) for k in range(r,n+1))
profiles=[(1,'Trained',8,3),(2,'Trained',8,3),(3,'Trained',8,3),(4,'Trained',8,3),(5,'Veteran',8,4),(6,'Veteran',8,4),(7,'Veteran',8,5),(8,'Veteran',8,5),(9,'Master',10,6),(10,'Master',10,6),(11,'Master',10,6),(12,'Master',10,6),(13,'Hero',10,8),(14,'Hero',10,8),(15,'Hero',10,8),(16,'Hero',10,8),(17,'Legend',12,9),(18,'Legend',12,9),(19,'Legend',12,10),(20,'Legend',12,10)]
bands={'Easy':(.80,.85),'Medium':(.60,.65),'Hard':(.40,.45)}
rows=[]; curves={k:[] for k in bands}
for lvl,tier,s,n in profiles:
 cells=[]
 for name,(lo,hi) in bands.items():
  opts=[]
  for dc in range(2,13):
   for r in range(1,n+1):
    p=prob(s,n,dc,r)
    inband=lo<=p<=hi
    opts.append((0 if inband else min(abs(p-lo),abs(p-hi)),abs(p-(lo+hi)/2),dc,r,p,inband))
  _,_,dc,r,p,ok=min(opts)
  cells.append((name,dc,r,p,ok)); curves[name].append(p)
 rows.append((lvl,tier,s,n,min(n,s-1),cells))
out=Path('/home/user/ttrpg_idealization/02_comparative_system_analysis/13_probability_band_calibration.md')
text='# Probability-Band Calibration with Required Successes\n\n**Status:** Phase 1 research artifact; no bands or DC assignments are canonical.\n\n**Bands:** Easy 80–85%; Medium 60–65%; Hard 40–45%. The supplied fully equipped progression is used. Each row selects the combination closest to the band midpoint, preferring combinations inside the band.\n\n| Level | Tier | Pool | Floor | Easy | Medium | Hard |\n|---:|---|---:|---:|---|---|---|\n'
for lvl,tier,s,n,f,cells in rows:
 text+=f'| {lvl} | {tier} | {n}d{s} | {f} | '+' | '.join(f'DC {dc} ({r}) → {p*100:.2f}%'+(' ✓' if ok else ' (nearest)') for _,dc,r,p,ok in cells)+' |\n'
text+='''\n## Notes\n\n- A check mark means the selected `DC X (R)` result falls inside the requested band.\n- `(nearest)` means no available DC/Required Success combination falls inside the band for that profile.\n- This uses at-least-R-success probabilities with the current Floor model.\n- The bands are calibration targets, not final Difficulty Class definitions.\n'''
out.write_text(text)
plt.figure(figsize=(13,7)); colors={'Easy':'#2ca02c','Medium':'#ff9900','Hard':'#d62728'}
xs=[x[0] for x in profiles]
for name,(lo,hi) in bands.items():
 plt.axhspan(lo*100,hi*100,color=colors[name],alpha=.10)
 plt.plot(xs,[v*100 for v in curves[name]],marker='o',color=colors[name],label=f'{name} selected')
 plt.axhline(lo*100,color=colors[name],ls='--',alpha=.5); plt.axhline(hi*100,color=colors[name],ls='--',alpha=.5)
plt.xticks(range(1,21)); plt.ylim(0,100); plt.xlabel('Character Level'); plt.ylabel('Probability of Success (%)'); plt.title('Probability-Band Calibration with Required Successes'); plt.grid(axis='y',alpha=.25); plt.legend(); plt.tight_layout(); img=Path('/home/user/ttrpg_idealization/02_comparative_system_analysis/13_probability_band_calibration.png'); plt.savefig(img,dpi=180); print(out,img)
