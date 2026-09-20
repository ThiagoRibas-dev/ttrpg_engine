#!/usr/bin/env python3
"""Exact P(max of N dS >= T) matrices for N=1..S-1 and T=1..S."""
from fractions import Fraction
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "02_comparative_system_analysis" / "09_at_least_probability_matrices.md"

def prob(n: int, sides: int, threshold: int) -> Fraction:
    # P(max >= T) = 1 - P(all dice < T)
    below = Fraction(max(threshold - 1, 0), sides) ** n
    return Fraction(1, 1) - below

def pct(x: Fraction) -> str:
    return f"{float(x) * 100:.2f}%"

def matrix(sides: int) -> str:
    cols = "| Pool | " + " | ".join(f"≥ {t}" for t in range(1, sides + 1)) + " |\n"
    sep = "|---:|" + "---:|" * sides + "\n"
    lines = [f"## d{sides} Matrices\n", cols, sep]
    for n in range(1, sides):
        vals = " | ".join(pct(prob(n, sides, t)) for t in range(1, sides + 1))
        lines.append(f"| {n}d{sides} | {vals} |\n")
    lines.append("\n")
    return "".join(lines)

def write_doc(max_sides: int):
    text = """# At-Least Probability Matrices\n\n**Status:** Phase 1 probability research artifact.\n**Purpose:** Exact probabilities that a pool of `N` same-sized dice produces at least one face meeting or exceeding threshold `T`.\n\n## Definition\n\nEach cell answers:\n\n> What is the probability that the highest face in an `NdS` pool is at least `T`?\n\nFormula:\n\n```text\nP(max ≥ T) = 1 − ((T − 1) / S)^N\n```\n\nThese matrices do not apply Competency Floors, Boons, Banes, DC labels, Automatic Successes, opposed-roll rules, or Required Successes. They are the baseline raw-dice reference.\n\nRows cover `1dS` through `(S−1)dS`, because this artifact examines pool volumes up to one less than the die size. Columns cover every face threshold from 1 through S.\n\n## Reading the Matrices\n\n- `≥ 1` is always 100% because every die has a face of at least 1.\n- `≥ S` is the probability of rolling the maximum face at least once.\n- Increasing pool volume raises reliability without changing the numerical ceiling.\n- Increasing die size raises the possible threshold ceiling.\n\n"""
    for sides in [4, 6, 8, 10, 12]:
        if sides > max_sides: continue
        text += matrix(sides)
    OUT.write_text(text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--sides', type=int, required=True)
    args = parser.parse_args()
    if not 4 <= args.sides <= 12:
        raise SystemExit('--sides must be between 4 and 12')
    write_doc(args.sides)
    print(f"Wrote {OUT}")
