#!/usr/bin/env python3
"""Generate the static results page (docs/index.html) from data/runs.csv.

Usage: python3 tools/build_site.py
No dependencies. The output is a single self-contained HTML file with inline SVG charts.
"""
import csv
import html
import statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # 2026-11-apple-silicon/
OUT = ROOT.parent / "docs" / "index.html"
REPO = "https://github.com/codemagic-ci-cd/codemagic-build-speeds-benchmarks/blob/main/2026-11-apple-silicon"

APPS = [
    ("xcodebenchmark", "XcodeBenchmark", "Clean build of a 42-CocoaPods project, compile only."),
    ("signal", "Signal iOS", "Debug build of the Signal iOS app, dependencies resolved beforehand."),
    ("expensify", "Expensify (New Expensify)", "React Native app, iOS native build only; npm and pod install are not timed."),
]
MACHINES = [  # key, name, vCPU seen by the build, RAM
    ("m2", "Mac mini M2", 7, 12),
    ("m4", "Mac mini M4", 9, 16),
    ("m4-pro", "Mac mini M4 Pro", 13, 32),
    ("m4-max", "Mac Studio M4 Max", 15, 32),
]
MNAME = {k: n for k, n, _, _ in MACHINES}
MSPEC = {k: (c, r) for k, _, c, r in MACHINES}


def fmt(s):
    if s < 100:
        return f"{s:.0f} s"
    return f"{int(s // 60)}m {int(round(s % 60)):02d}s"


def load():
    runs = defaultdict(list)
    with open(ROOT / "data" / "runs.csv", newline="") as f:
        for row in csv.DictReader(f):
            if row["run"] == "smoke" or not row["build_seconds"]:
                continue
            key = (row["app"], row["machine"])
            runs[key].append(float(row["build_seconds"]))
    return runs


def stats(v):
    return dict(n=len(v), med=statistics.median(v), lo=min(v), hi=max(v), spread=100 * (max(v) - min(v)) / min(v), runs=v)


def chart(app, S):
    rows = sorted([(m, S[(app, m)]) for m, *_ in MACHINES if (app, m) in S], key=lambda x: x[1]["med"])
    if not rows:
        return ""
    W, LEFT, RIGHT, ROW = 760, 190, 150, 46
    xmax = max(s["hi"] for _, s in rows) * 1.04
    scale = (W - LEFT - RIGHT) / xmax
    base = S.get((app, "m2"), {}).get("med")
    out = [f'<svg viewBox="0 0 {W} {ROW * len(rows) + 30}" role="img" aria-label="Median build time per machine">']
    step = next(s for s in (30, 60, 120, 180, 300, 600, 900, 1200, 1800) if xmax / s <= 6)
    t = 0
    while t <= xmax:
        x = LEFT + t * scale
        out.append(f'<line class="grid" x1="{x:.1f}" y1="6" x2="{x:.1f}" y2="{ROW * len(rows) + 6}"/>')
        out.append(f'<text class="tick" x="{x:.1f}" y="{ROW * len(rows) + 22}" text-anchor="middle">{fmt(t) if t else "0"}</text>')
        t += step
    for i, (m, s) in enumerate(rows):
        y = 12 + i * ROW
        out.append(f'<text class="lbl" x="{LEFT - 12}" y="{y + 15}" text-anchor="end">{html.escape(MNAME[m])}</text>')
        c, r = MSPEC[m]
        out.append(f'<text class="sub" x="{LEFT - 12}" y="{y + 30}" text-anchor="end">{c} cores, {r} GB</text>')
        out.append(f'<rect class="bar b-{m}" x="{LEFT}" y="{y + 4}" width="{s["med"] * scale:.1f}" height="26" rx="3"/>')
        for v in s["runs"]:
            out.append(f'<circle class="dot" cx="{LEFT + v * scale:.1f}" cy="{y + 17}" r="4.5"><title>{v:.1f} s</title></circle>')
        label = fmt(s["med"])
        if base and m != "m2":
            label += f" · {base / s['med']:.1f}x"
        out.append(f'<text class="val" x="{LEFT + max(s["hi"], s["med"]) * scale + 12:.1f}" y="{y + 22}">{label}</text>')
    out.append("</svg>")
    return "\n".join(out)


def table(app, S):
    base = S.get((app, "m2"), {}).get("med")
    out = ['<table><thead><tr><th>Machine</th><th>Runs</th><th>Median</th><th>Fastest</th><th>Slowest</th><th>Spread</th><th>vs M2</th></tr></thead><tbody>']
    for m, name, c, r in MACHINES:
        s = S.get((app, m))
        if not s:
            continue
        vs = f"{base / s['med']:.2f}x" if base else ""
        out.append(f"<tr><td>{html.escape(name)}<small> {c} cores, {r} GB</small></td><td>{s['n']}</td><td><b>{s['med']:.1f} s</b></td>"
                   f"<td>{s['lo']:.1f} s</td><td>{s['hi']:.1f} s</td><td>{s['spread']:.0f}%</td><td>{vs}</td></tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def ratio(S, app, a, b):
    if (app, a) in S and (app, b) in S:
        return S[(app, a)]["med"] / S[(app, b)]["med"]
    return None


def main():
    runs = load()
    S = {k: stats(v) for k, v in runs.items()}
    cards = []
    for title, a, b in [("M4 Pro vs M4", "m4", "m4-pro"), ("M4 Max vs M4 Pro", "m4-pro", "m4-max"), ("M4 vs M2", "m2", "m4")]:
        parts = []
        for app, label, _ in APPS:
            r = ratio(S, app, a, b)
            if r:
                parts.append(f"<li>{html.escape(label.split(' (')[0])}: <b>{r:.2f}x</b></li>")
        if parts:
            cards.append(f'<div class="card"><h3>{title}</h3><p class="small">Median build time ratio, faster machine first</p><ul>{"".join(parts)}</ul></div>')
    sections = []
    for app, label, desc in APPS:
        sections.append(f'<section><h2>{html.escape(label)}</h2><p class="small">{html.escape(desc)} Bars are the median, dots are individual runs; the multiplier is the speedup against Mac mini M2.</p>'
                        f'<div class="chart">{chart(app, S)}</div><div class="wrap">{table(app, S)}</div></section>')

    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Codemagic Apple silicon build speeds, November 2026</title>
<style>
:root {{ --bg:#fff; --fg:#17202a; --mut:#5b6673; --line:#e2e6ea; --card:#f5f7f9; --acc:#0b6bcb;
  --m2:#9aa5b1; --m4:#6aa3d9; --m4-pro:#0b6bcb; --m4-max:#0a3d7a; --dot:#17202a; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#0f1419; --fg:#e8edf2; --mut:#9aa7b4; --line:#27303a; --card:#171e26; --acc:#5aa9f0;
  --m2:#6b7785; --m4:#4d86bd; --m4-pro:#5aa9f0; --m4-max:#a9d3ff; --dot:#e8edf2; }} }}
* {{ box-sizing:border-box }}
body {{ margin:0; background:var(--bg); color:var(--fg); font:16px/1.55 system-ui,-apple-system,Segoe UI,Roboto,sans-serif }}
main {{ max-width:900px; margin:0 auto; padding:32px 16px 64px }}
h1 {{ font-size:1.9rem; line-height:1.2; margin:0 0 8px }} h2 {{ font-size:1.35rem; margin:40px 0 4px }} h3 {{ margin:0 0 4px; font-size:1rem }}
.small, small {{ color:var(--mut); font-size:.9rem }} a {{ color:var(--acc) }}
.cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:12px; margin:24px 0 }}
.card {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:14px 16px }} .card ul {{ margin:8px 0 0; padding-left:18px }}
.tiles {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:12px }}
.chart {{ overflow-x:auto }} svg {{ width:100%; min-width:620px; height:auto; margin:12px 0 }} .grid {{ stroke:var(--line); stroke-width:1 }} .tick, .sub {{ fill:var(--mut); font-size:11px }}
.lbl {{ fill:var(--fg); font-size:13px; font-weight:600 }} .val {{ fill:var(--fg); font-size:13px }} .dot {{ fill:var(--dot); fill-opacity:.7; stroke:var(--bg); stroke-width:1 }}
.b-m2 {{ fill:var(--m2) }} .b-m4 {{ fill:var(--m4) }} .b-m4-pro {{ fill:var(--m4-pro) }} .b-m4-max {{ fill:var(--m4-max) }}
table {{ width:100%; border-collapse:collapse; font-size:.92rem; margin:8px 0 }} th,td {{ text-align:right; padding:6px 8px; border-bottom:1px solid var(--line); white-space:nowrap }}
th:first-child, td:first-child {{ text-align:left }} th {{ color:var(--mut); font-weight:600 }}
.wrap {{ overflow-x:auto }} code {{ background:var(--card); padding:1px 5px; border-radius:4px; font-size:.88em }}
</style></head><body><main>
<h1>Codemagic Apple silicon build speeds, November 2026</h1>
<p class="small">Mac mini M2, M4, M4 Pro and Mac Studio M4 Max on Codemagic, building three real projects. Status: first release, method v1.</p>
<div class="cards">{"".join(cards)}</div>

{"".join(sections)}

<section><h2>What was measured</h2>
<div class="tiles">
<div class="card"><h3>Clean builds</h3><p class="small">Every build starts on a fresh build machine with no cache.</p></div>
<div class="card"><h3>Five runs, median</h3><p class="small">Each app and machine was built five times. Tables show median, fastest, slowest and spread.</p></div>
<div class="card"><h3>Real-world conditions</h3><p class="small">All builds ran on the same shared build machine pools our customers use, during normal working hours.</p></div>
<div class="card"><h3>Same code, same Xcode</h3><p class="small">Xcode 26.6 on macOS 26.5.1 everywhere. Each app is pinned to a fixed upstream commit.</p></div>
<div class="card"><h3>Timed step only</h3><p class="small">The headline is the compile step. Downloads, package resolution, npm and pod installs are logged but excluded.</p></div>
</div></section>

<section><h2>Machines</h2>
<p class="small">Hardware available to your build on each machine type.</p>
<div class="wrap"><table><thead><tr><th>Machine</th><th>Cores</th><th>Memory</th></tr></thead><tbody>
{"".join(f"<tr><td>{n}</td><td>{c}</td><td>{r} GB</td></tr>" for _, n, c, r in MACHINES)}
</tbody></table></div></section>

<section><h2>Notes on reading the results</h2><ul>
<li>These are production results, measured on the same shared build machine pools customers use and during normal working hours. Build times on the most popular machine types, such as Mac mini M2 and Mac mini M4, can vary from run to run with overall demand. Use the median, and treat the fastest run as a best case.</li>
<li>Five runs per app and machine is a small sample.</li>
<li>Results reflect the whole build machine (chip, cores and memory available to the build), not the chip alone.</li>
<li>Expensify is pinned to a commit that builds with Xcode 26.6 and runs without its private submodule. React Native is built from source.</li>
</ul></section>

<section><h2>Repeat it yourself</h2>
<ul>
<li>Each app is a public upstream project at a pinned commit: <a href="{REPO}/apps/xcodebenchmark.md">XcodeBenchmark</a>, <a href="{REPO}/apps/signal-ios.md">Signal iOS</a>, <a href="{REPO}/apps/expensify.md">Expensify</a>.</li>
<li>Workflows (one per machine type): <a href="{REPO}/workflows">workflows folder</a>.</li>
<li>All runs: <a href="{REPO}/data/runs.csv">data/runs.csv</a>. Summary script: <code>python3 tools/summarize.py</code>.</li>
<li>Confirm the chip in the "Environment info" step of each build.</li>
</ul></section>
</main></body></html>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page)
    print("wrote", OUT, len(page), "bytes")


if __name__ == "__main__":
    main()
