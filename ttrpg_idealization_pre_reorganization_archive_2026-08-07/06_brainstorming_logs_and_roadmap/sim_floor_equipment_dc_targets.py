from pathlib import Path

def chance(sides,pool,dc):
    floor=min(pool,sides-1)
    if dc<=floor:return 1.0
    return 1-((dc-1)/sides)**pool
rows=[]
profiles=[(1,'Trained',8,2,1),(2,'Trained',8,2,1),(3,'Trained',8,2,1),(4,'Trained',8,2,1),(5,'Veteran',8,3,1),(6,'Veteran',8,3,1),(7,'Veteran',8,3,2),(8,'Veteran',8,3,2),(9,'Master',10,4,2),(10,'Master',10,4,2),(11,'Master',10,4,2),(12,'Master',10,4,2),(13,'Hero',10,5,3),(14,'Hero',10,5,3),(15,'Hero',10,5,3),(16,'Hero',10,5,3),(17,'Legend',12,6,3),(18,'Legend',12,6,3),(19,'Legend',12,6,4),(20,'Legend',12,6,4)]
targets=[('Easy',.85),('Medium',.65),('Hard',.55)]
for lvl,tier,sides,base,boons in profiles:
 n=base+boons
 vals=[]
 for name,target in targets:
  options=[(abs(chance(sides,n,dc)-target),dc,chance(sides,n,dc)) for dc in range(2,13)]
  err,dc,p=min(options)
  vals.append((name, (dc if err<=.02 else None), p, err, dc))
 rows.append((lvl,tier,sides,base,boons,n,min(n,sides-1),vals))
out=Path('/home/user/ttrpg_idealization/02_comparative_system_analysis/11_floor_equipment_dc_target_calibration.md')
text='# Floor and Equipment Dice: DC Target Mapping\n\n**Status:** Phase 1 research artifact; no DC targets or equipment assumptions are canonical.\n\n**Assumption:** The supplied Equipment Boons are treated as net additional same-size dice after all type and same-source stacking rules.\n\n**Target bands:** Easy 85%, Medium 65%, Hard 55%. A DC is reported only when the closest available fixed DC from 2–12 is within ±2 percentage points. Otherwise the cell is `NA`.\n\n**Probability model:** `P(max ≥ DC)`, with `Floor = min(final pool size, die size − 1)`. Since all listed floors are below the target DCs selected here, the calculated probabilities use the raw maximum-of-pool distribution for those cells.\n\n| Level | Tier | Die | Baseline Pool | Equipment Boons | Final Pool | Floor | Easy DC / Actual | Medium DC / Actual | Hard DC / Actual |\n|---:|---|---:|---:|---:|---:|---:|---|---|---|\n'
for lvl,tier,sides,base,b,final,f,vals in rows:
 cells=[]
 for _,dc,p,err,nearest in vals: cells.append(f'`{dc}` / {p*100:.2f}%' if dc else f'`NA` (nearest DC {nearest}: {p*100:.2f}%)')
 text+=f'| {lvl} | {tier} | d{sides} | {base}d | +{b}B | {final}d{sides} | {f} | {cells[0]} | {cells[1]} | {cells[2]} |\n'
text+='''\n## Interpretation\n\n- `NA` means no single fixed DC from 2–12 lands within ±2 percentage points of the requested target for that level/profile.\n- Equipment increases pool volume and therefore also increases the Floor, subject to the die-size cap.\n- At this stage, Easy/Medium/Hard are target labels only; they are not yet canonical DC categories.\n- This pass uses at-least-one-success probabilities only. Required Successes, Boons/Banes beyond the stated equipment assumption, Automatic Successes, and opposed checks are deferred.\n'''
out.write_text(text)
print(out)
