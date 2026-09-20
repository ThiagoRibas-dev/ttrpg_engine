import matplotlib.pyplot as plt
from math import comb
from pathlib import Path

def p_at_least(sides, pool, dc, required):
    floor=min(pool,sides-1)
    p=1.0 if dc<=floor else (sides-dc+1)/sides
    return sum(comb(pool,k)*p**k*(1-p)**(pool-k) for k in range(required,pool+1))
profiles=[(1,'Trained',8,3),(2,'Trained',8,3),(3,'Trained',8,3),(4,'Trained',8,3),(5,'Veteran',8,4),(6,'Veteran',8,4),(7,'Veteran',8,5),(8,'Veteran',8,5),(9,'Master',10,6),(10,'Master',10,6),(11,'Master',10,6),(12,'Master',10,6),(13,'Hero',10,8),(14,'Hero',10,8),(15,'Hero',10,8),(16,'Hero',10,8),(17,'Legend',12,9),(18,'Legend',12,9),(19,'Legend',12,10),(20,'Legend',12,10)]
targets={'Easy':.85,'Medium':.65,'Hard':.55}
actual={k:[] for k in targets}; labels={k:[] for k in targets}
for lvl,tier,sides,n in profiles:
 for name,target in targets.items():
  opts=[]
  for dc in range(2,13):
   for r in range(1,n+1):
    p=p_at_least(sides,n,dc,r)
    opts.append((abs(p-target),dc,r,p))
  err,dc,r,p=min(opts)
  actual[name].append(p); labels[name].append(f'DC {dc} ({r})')
out=Path('02_comparative_system_analysis/12_target_band_calibration_line_chart.png')
plt.figure(figsize=(13,7))
colors={'Easy':'#2ca02c','Medium':'#ff9900','Hard':'#d62728'}
for name in targets:
 plt.plot([x[0] for x in profiles], [p*100 for p in actual[name]], marker='o', label=f'{name} actual', color=colors[name])
 plt.axhline(targets[name]*100, linestyle='--', alpha=.45, color=colors[name], label=f'{name} target {targets[name]*100:.0f}%')
plt.xticks(range(1,21)); plt.ylim(0,105); plt.xlabel('Character Level'); plt.ylabel('Probability of Success (%)')
plt.title('Target-Band Calibration with Required Successes\nFully Equipped Progression; Closest DC X (R) Combination')
plt.grid(True, axis='y', alpha=.25); plt.legend(ncol=2, fontsize=9); plt.tight_layout(); plt.savefig(out,dpi=180); print(out)
