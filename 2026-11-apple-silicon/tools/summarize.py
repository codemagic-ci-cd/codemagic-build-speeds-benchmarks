#!/usr/bin/env python3
"""Print median / fastest / slowest per app and machine from data/runs.csv.

Usage: python3 tools/summarize.py [path/to/runs.csv]
"""
import csv
import statistics
import sys
from collections import defaultdict
from pathlib import Path

APPS = ["xcodebenchmark", "signal", "expensify"]
MACHINES = ["m2", "m4", "m4-pro", "m4-max"]


def load(path):
    runs = defaultdict(list)
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            if row["run"] == "smoke" or not row["build_seconds"]:
                continue
            runs[(row["app"], row["machine"])].append(float(row["build_seconds"]))
    return runs


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "data" / "runs.csv"
    runs = load(path)
    print(f"{'app':16} {'machine':8} {'n':>2} {'median':>8} {'fastest':>8} {'slowest':>8} {'spread':>7}")
    for app in APPS:
        for m in MACHINES:
            v = runs.get((app, m))
            if not v:
                continue
            med, lo, hi = statistics.median(v), min(v), max(v)
            print(f"{app:16} {m:8} {len(v):>2} {med:8.1f} {lo:8.1f} {hi:8.1f} {100 * (hi - lo) / lo:6.0f}%")


if __name__ == "__main__":
    main()
