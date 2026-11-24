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
    """Range lanes: a pill from fastest to slowest run, dots for every run, a ring marker at the median."""
    rows = sorted([(m, S[(app, m)]) for m, *_ in MACHINES if (app, m) in S], key=lambda x: x[1]["med"])
    if not rows:
        return ""
    W, LEFT, RIGHT, LANE = 760, 150, 70, 62
    xmax = max(s["hi"] for _, s in rows) * 1.06
    scale = (W - LEFT - RIGHT) / xmax
    base = S.get((app, "m2"), {}).get("med")
    H = LANE * len(rows) + 34
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Fastest to slowest build time and median per machine">']
    step = next(s for s in (30, 60, 120, 180, 300, 600, 900, 1200, 1800) if xmax / s <= 7)
    t = 0
    while t <= xmax:
        x = LEFT + t * scale
        out.append(f'<line class="grid" x1="{x:.1f}" y1="4" x2="{x:.1f}" y2="{LANE * len(rows)}"/>')
        out.append(f'<text class="tick" x="{x:.1f}" y="{H - 8}" text-anchor="middle">{fmt(t) if t else "0"}</text>')
        t += step
    for i, (m, s) in enumerate(rows):
        y = 8 + i * LANE
        cy = y + 34
        out.append(f'<text class="lbl" x="{LEFT - 14}" y="{cy - 3}" text-anchor="end">{html.escape(MNAME[m])}</text>')
        c, r = MSPEC[m]
        out.append(f'<text class="sub" x="{LEFT - 14}" y="{cy + 13}" text-anchor="end">{c} cores, {r} GB</text>')
        x1, x2 = LEFT + s["lo"] * scale, LEFT + s["hi"] * scale
        out.append(f'<line class="pill p-{m}" x1="{x1:.1f}" y1="{cy}" x2="{max(x2, x1 + 1):.1f}" y2="{cy}"/>')
        for v in s["runs"]:
            out.append(f'<circle class="dot d-{m}" cx="{LEFT + v * scale:.1f}" cy="{cy}" r="4"><title>{v:.1f} s</title></circle>')
        mx = LEFT + s["med"] * scale
        out.append(f'<circle class="med d-{m}" cx="{mx:.1f}" cy="{cy}" r="9"><title>median {s["med"]:.1f} s</title></circle>')
        out.append(f'<text class="mval" x="{mx:.1f}" y="{cy - 17}" text-anchor="middle">{fmt(s["med"])}</text>')
        if base and m != "m2":
            out.append(f'<text class="chip" x="{W - 6}" y="{cy + 4}" text-anchor="end">{base / s["med"]:.1f}x</text>')
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

    # headline tiles: fastest machine per app and its speedup over Mac mini M2
    tiles = []
    for app, label, _ in APPS:
        best = min(((m, S[(app, m)]) for m, *_ in MACHINES if (app, m) in S), key=lambda x: x[1]["med"], default=None)
        base = S.get((app, "m2"))
        if best:
            m, st = best
            sub = f"{base['med'] / st['med']:.1f}x faster than Mac mini M2" if base and m != "m2" else "baseline"
            tiles.append(f'<div class="tile"><div class="tl">{html.escape(label.split(" (")[0])}</div><div class="tn">{fmt(st["med"])}</div>'
                         f'<div class="ts">{html.escape(MNAME[m])}</div><div class="tc">{sub}</div></div>')

    # speed ladder: median speedup against M2 per app
    ladder = []
    for m, name, *_ in MACHINES:
        cells = []
        for app, label, _ in APPS:
            b, x = S.get((app, "m2")), S.get((app, m))
            cells.append(f"<td>{b['med'] / x['med']:.1f}x</td>" if b and x else "<td></td>")
        ladder.append(f'<tr><td><span class="sw s-{m}"></span>{html.escape(name)}</td>{"".join(cells)}</tr>')
    ladder_head = "".join(f"<th>{html.escape(l.split(' (')[0])}</th>" for _, l, _ in APPS)

    sections = []
    for app, label, desc in APPS:
        sections.append(f'<section id="{app}"><h2>{html.escape(label)}</h2><p class="lede">{html.escape(desc)}</p>'
                        f'<div class="chart">{chart(app, S)}</div>'
                        '<p class="legend"><span><i class="lg pillk"></i>fastest to slowest run</span><span><i class="lg dotk"></i>each run</span>'
                        '<span><i class="lg medk"></i>median</span><span><b>1.0x</b> = Mac mini M2 median</span></p>'
                        f'<div class="wrap">{table(app, S)}</div></section>')

    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Codemagic Apple silicon build speeds, November 2026</title>
<meta name="description" content="Build times for Mac mini M2, M4, M4 Pro and Mac Studio M4 Max on Codemagic, measured on three open-source iOS projects.">
<style>
@font-face {{ font-family:Metropolis; font-weight:400; font-style:normal; font-display:swap; src:url(assets/Metropolis-400.woff2) format('woff2') }}
@font-face {{ font-family:Metropolis; font-weight:500; font-style:normal; font-display:swap; src:url(assets/Metropolis-500.woff2) format('woff2') }}
@font-face {{ font-family:Metropolis; font-weight:600; font-style:normal; font-display:swap; src:url(assets/Metropolis-600.woff2) format('woff2') }}
@font-face {{ font-family:Metropolis; font-weight:700; font-style:normal; font-display:swap; src:url(assets/Metropolis-700.woff2) format('woff2') }}
:root {{ --bg:#fff; --fg:#000626; --body:#06225D; --mut:#5a6a8f; --line:#dfe5f3; --card:#f4f7ff; --blue:#0031EA; --acc:#0031EA;
  --m2:#00CEFF; --m4:#008BF7; --m4-pro:#0031EA; --m4-max:#FE19FF; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#000626; --fg:#f2f5ff; --body:#c9d4f5; --mut:#8c9bc4; --line:#1a2552; --card:#0a1236; --acc:#5aa9ff; --m4-pro:#4d7bff; }} }}
* {{ box-sizing:border-box }}
body {{ margin:0; background:var(--bg); color:var(--body); font:16px/1.6 Metropolis,"Avenir Next","Segoe UI",system-ui,-apple-system,sans-serif }}
.hero {{ background:linear-gradient(135deg,#0031EA 0%,#008BF7 100%); color:#fff; padding:28px 16px 120px; position:relative }}
.hero::after {{ content:""; position:absolute; left:0; right:0; bottom:-1px; height:90px; background:var(--bg);
  -webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 90' preserveAspectRatio='none'%3E%3Cpath d='M0 60C240 10 480 0 720 30s600 55 720 10V90H0z'/%3E%3C/svg%3E") center/100% 100% no-repeat;
  mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 90' preserveAspectRatio='none'%3E%3Cpath d='M0 60C240 10 480 0 720 30s600 55 720 10V90H0z'/%3E%3C/svg%3E") center/100% 100% no-repeat }}
.in {{ max-width:920px; margin:0 auto }}
.brand {{ display:flex; align-items:center; gap:14px; margin-bottom:56px }} .brand img {{ display:block; height:28px; width:auto }}
.brand span {{ opacity:.8; font-weight:500; font-size:1.05rem; border-left:1px solid rgba(255,255,255,.5); padding-left:14px }}
h1 {{ font-size:clamp(2rem,5vw,3rem); line-height:1.1; margin:0 0 14px; font-weight:600; max-width:680px }}
.sub1 {{ max-width:600px; font-size:1.1rem; opacity:.92; margin:0 0 20px }}
.chip1 {{ display:inline-block; border:1px solid rgba(255,255,255,.6); border-radius:99px; padding:3px 12px; font-size:.85rem; color:#fff; text-decoration:none }}
main {{ max-width:920px; margin:-40px auto 0; padding:0 16px 64px; position:relative }}
h2 {{ color:var(--fg); font-size:1.6rem; font-weight:500; margin:56px 0 4px }} h3 {{ color:var(--fg); margin:0 0 4px; font-size:1.05rem; font-weight:600 }}
.lede, .small, small {{ color:var(--mut); font-size:.95rem }} a {{ color:var(--acc) }} .lede {{ margin:0 0 8px }}
.tiles {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:14px }}
.tile {{ background:var(--card); border:1px solid var(--line); border-radius:16px; padding:18px 20px; border-top:4px solid var(--blue) }}
.tl {{ color:var(--mut); font-size:.85rem; text-transform:uppercase; letter-spacing:.06em }} .tn {{ color:var(--fg); font-size:2.6rem; font-weight:600; line-height:1.15 }}
.ts {{ color:var(--fg); font-weight:600 }} .tc {{ color:var(--mut); font-size:.9rem }}
.grid3 {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:14px; margin-top:12px }}
.card {{ background:var(--card); border:1px solid var(--line); border-radius:14px; padding:14px 18px }} .card p {{ margin:2px 0 0 }}
.step {{ counter-increment:s }} .step h3::before {{ content:counter(s); display:inline-block; width:24px; height:24px; line-height:24px; text-align:center; border-radius:50%; background:var(--blue); color:#fff; font-size:.8rem; margin-right:8px }}
.steps {{ counter-reset:s }}
.chart {{ overflow-x:auto }} svg {{ width:100%; min-width:640px; height:auto; margin:10px 0 0 }}
.grid {{ stroke:var(--line); stroke-width:1 }} .tick, .sub {{ fill:var(--mut); font-size:11px }} .lbl {{ fill:var(--fg); font-size:13px; font-weight:600 }}
.mval {{ fill:var(--fg); font-size:12px; font-weight:600 }} .chip {{ fill:var(--fg); font-size:15px; font-weight:700 }}
.pill {{ stroke-width:12; stroke-linecap:round; opacity:.28 }} .dot {{ stroke:var(--bg); stroke-width:1.5 }} .med {{ stroke:var(--bg); stroke-width:3 }}
.p-m2 {{ stroke:var(--m2) }} .p-m4 {{ stroke:var(--m4) }} .p-m4-pro {{ stroke:var(--m4-pro) }} .p-m4-max {{ stroke:var(--m4-max) }}
.d-m2 {{ fill:var(--m2) }} .d-m4 {{ fill:var(--m4) }} .d-m4-pro {{ fill:var(--m4-pro) }} .d-m4-max {{ fill:var(--m4-max) }}
.legend {{ display:flex; flex-wrap:wrap; gap:6px 18px; font-size:.82rem; color:var(--mut); margin:4px 0 8px }} .legend i {{ display:inline-block; vertical-align:middle; margin-right:6px }}
.pillk {{ width:22px; height:8px; border-radius:4px; background:var(--m4); opacity:.35 }} .dotk {{ width:8px; height:8px; border-radius:50%; background:var(--m4) }} .medk {{ width:14px; height:14px; border-radius:50%; background:var(--m4); border:3px solid var(--bg); box-shadow:0 0 0 1px var(--m4) }}
table {{ width:100%; border-collapse:collapse; font-size:.92rem; margin:8px 0 }} th,td {{ text-align:right; padding:7px 8px; border-bottom:1px solid var(--line); white-space:nowrap }}
th:first-child, td:first-child {{ text-align:left }} th {{ color:var(--mut); font-weight:600 }} td b {{ color:var(--fg) }}
.wrap {{ overflow-x:auto }} code {{ background:var(--card); padding:1px 6px; border-radius:5px; font-size:.88em }}
.sw {{ display:inline-block; width:12px; height:12px; border-radius:50%; margin-right:8px; vertical-align:-1px }} .s-m2 {{ background:var(--m2) }} .s-m4 {{ background:var(--m4) }} .s-m4-pro {{ background:var(--m4-pro) }} .s-m4-max {{ background:var(--m4-max) }}
nav {{ display:flex; gap:14px; flex-wrap:wrap; margin:18px 0 0; font-size:.95rem }} nav a {{ text-decoration:none; font-weight:600 }}
footer {{ border-top:1px solid var(--line); margin-top:56px; padding-top:16px; color:var(--mut); font-size:.85rem }}
</style></head><body>
<header class="hero"><div class="in">
<div class="brand"><img src="assets/logo-white.svg" alt="Codemagic" width="150" height="28"><span>build speeds</span></div>
<h1>Apple silicon build speeds, November 2026</h1>
<p class="sub1">How fast Mac mini M2, M4, M4 Pro and Mac Studio M4 Max build three real iOS projects on Codemagic.</p>
<a class="chip1" href="#method">Method v1</a></div></header>
<main>
<div class="tiles">{"".join(tiles)}</div>
<nav><a href="#xcodebenchmark">XcodeBenchmark</a><a href="#signal">Signal iOS</a><a href="#expensify">Expensify</a><a href="#method">Method</a><a href="#repeat">Repeat it</a></nav>

<section><h2>Speedup over Mac mini M2</h2>
<p class="lede">Median build time of Mac mini M2 divided by the median of each machine. Higher is faster.</p>
<div class="wrap"><table><thead><tr><th>Machine</th>{ladder_head}</tr></thead><tbody>{"".join(ladder)}</tbody></table></div></section>

{"".join(sections)}

<section id="method"><h2>Method v1</h2>
<p class="lede">Every number on this page was produced the same way. The full write-up is in <a href="{REPO}/METHOD.md">METHOD.md</a>.</p>
<div class="grid3 steps">
<div class="card step"><h3>Pick a project</h3><p class="small">Three open-source iOS projects, each pinned to one exact upstream commit and built with Xcode 26.6 on macOS 26.5.1.</p></div>
<div class="card step"><h3>Start from scratch</h3><p class="small">Each build runs on a fresh build machine with no cache, so every run is a clean build.</p></div>
<div class="card step"><h3>Prepare, untimed</h3><p class="small">Downloads and installs (package resolution, npm, pods) run first and are not part of the result.</p></div>
<div class="card step"><h3>Time the compile</h3><p class="small">Only the compile step is timed, from first command to <code>BUILD SUCCEEDED</code>.</p></div>
<div class="card step"><h3>Repeat five times</h3><p class="small">Five runs per project and machine. The headline is the median; fastest and slowest runs are shown too.</p></div>
<div class="card step"><h3>Real conditions</h3><p class="small">Builds ran in the shared production build pools our customers use, during normal working hours.</p></div>
</div></section>

<section><h2>Build machines</h2>
<p class="lede">Hardware available to your build on each machine type.</p>
<div class="wrap"><table><thead><tr><th>Machine</th><th>Cores</th><th>Memory</th></tr></thead><tbody>
{"".join(f'<tr><td><span class="sw s-{m}"></span>{n}</td><td>{c}</td><td>{r} GB</td></tr>' for m, n, c, r in MACHINES)}
</tbody></table></div></section>

<section><h2>Reading the results</h2>
<ul>
<li>Use the median. Treat the fastest run as a best case.</li>
<li>Times on the most popular machine types, such as Mac mini M2 and Mac mini M4, vary from run to run with overall demand.</li>
<li>Five runs per project and machine is a small sample.</li>
<li>Results reflect the whole build machine (chip, cores and memory available to the build), not the chip alone.</li>
<li>Expensify is pinned to a commit that builds with Xcode 26.6 and runs without its private submodule. React Native is built from source.</li>
</ul></section>

<section id="repeat"><h2>Repeat it yourself</h2>
<ul>
<li>Method: <a href="{REPO}/METHOD.md">METHOD.md</a>, and how to run: <a href="{REPO}/README.md">README</a>.</li>
<li>Projects at pinned commits: <a href="{REPO}/apps/xcodebenchmark.md">XcodeBenchmark</a>, <a href="{REPO}/apps/signal-ios.md">Signal iOS</a>, <a href="{REPO}/apps/expensify.md">Expensify</a>.</li>
<li>Workflows, one per machine type: <a href="{REPO}/workflows">workflows folder</a>.</li>
<li>All runs: <a href="{REPO}/data/runs.csv">data/runs.csv</a>. Summary script: <code>python3 tools/summarize.py</code>.</li>
<li>Confirm the chip in the "Environment info" step of each build.</li>
</ul></section>
<footer>Measured 23 and 24 November 2026. Codemagic is a registered trademark of Nevercode Ltd.</footer>
</main></body></html>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page)
    print("wrote", OUT, len(page), "bytes")


if __name__ == "__main__":
    main()
