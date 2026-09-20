#!/usr/bin/env python3
from fractions import Fraction
from math import comb
from pathlib import Path
import argparse

ROOT=Path('/home/user/ttrpg_idealization')
OUT=ROOT/'02_comparative_system_analysis/12_multi_success_probability_matrices.md'

def at_least(n,s,t,r):
    p=Fraction(max(s-t+1,0),s)
    return sum(Fraction(comb(n,k))*p**k*(1-p)**(n-k) for k in range(r,n+1))

def pct(x): return f'{float(x)*100:.2f}%'

def matrix(s):
    lines=[f'## d{s}: Probability of at least R successes\n\n', '| Pool | Required | '+ ' | '.join(f'≥ {t}' for t in range(2,s+1))+' |\n', '|---:|---:|'+'---:|'*(s-1)+'\n']
    for n in range(1,s+1):
      for r in range(1,n+1):
        lines.append(f'| {n}d{s} | {r} | '+' | '.join(pct(at_least(n,s,t,r)) for t in range(2,s+1))+' |\n')
      lines.append('|  |  | '+' | '.join('' for _ in range(s-1))+' |\n')
    return ''.join(lines)

def calibrate():
    profiles=[(1,'Trained',8,2,1),(2,'Trained',8,2,1),(3,'Trained',8,2,1),(4,'Trained',8,2,1),(5,'Veteran',8,3,1),(6,'Veteran',8,3,1),(7,'Veteran',8,3,2),(8,'Veteran',8,3,2),(9,'Master',10,4,2),(10,'Master',10,4,2),(11,'Master',10,4,2),(12,'Master',10,4,2),(13,'Hero',10,5,3),(14,'Hero',10,5,3),(15,'Hero',10,5,3),(16,'Hero',10,5,3),(17,'Legend',12,6,3),(18,'Legend',12,6,3),(19,'Legend',12,6,4),(20,'Legend',12,6,4)]
    targets=[('Easy',.85),('Medium',.65),('Hard',.55)]
    lines=['## Target-Band Calibration with Required Successes\n\n','This table searches `DC X (R)` combinations using the supplied fully equipped progression. It reports the closest combination within DC 2–12 and Required Successes 1 through the final pool size. `NA` means no combination is within ±2 percentage points; the nearest combination is shown for diagnosis.\n\n','| Level | Tier | Final Pool | Floor | Easy | Medium | Hard |\n|---:|---|---:|---:|---|---|---|\n']
    for lvl,tier,s,base,b in profiles:
      n=base+b; floor=min(n,s-1)
      cells=[]
      for name,target in targets:
       opts=[]
       for dc in range(2,13):
        pface=Fraction(max(s-dc+1,0),s) if dc>floor else Fraction(1,1)
        for r in range(1,n+1):
         p=sum(Fraction(comb(n,k))*pface**k*(1-pface)**(n-k) for k in range(r,n+1))
         opts.append((abs(float(p)-target),dc,r,p))
       e,dc,r,p=min(opts)
       label=f'DC {dc} ({r}) → {pct(p)}' if e<=.02 else f'NA; nearest DC {dc} ({r}) → {pct(p)}'
       cells.append(label)
      lines.append(f'| {lvl} | {tier} | {n}d{s} | {floor} | '+' | '.join(cells)+' |\n')
    return ''.join(lines)

def main(max_s):
 text='# Multi-Success Probability Matrices\n\n**Status:** Phase 1 research artifact; no DC target or Required Success target is canonical.\n\n## Definition\n\nEach cell answers:\n\n> What is the probability that at least `R` dice in an `NdS` pool meet or exceed threshold `T`?\n\nFormula:\n\n```text\nP(at least R successes) = Σ[k=R..N] C(N,k) p^k (1−p)^(N−k)\np = (S−T+1)/S\n```\n\nThis is the mathematical model for `DC T (R)`. It is distinct from “keep highest R”; Required Successes count every die face meeting the Target Number.\n\nThe matrices cover standard dice d4, d6, d8, d10, and d12, with pools from 1dS through SdS and Required Successes from 1 through the pool size.\n\n'
 for s in [4,6,8,10,12]:
  if s<=max_s: text+=matrix(s)
 text+=calibrate()
 OUT.write_text(text)
 print(OUT)

if __name__=='__main__':
 ap=argparse.ArgumentParser(); ap.add_argument('--sides',type=int,default=12); main(ap.parse_args().sides)
