# Apple silicon build speeds on Codemagic (November 2026)

Build times for Mac mini M2, Mac mini M4, Mac mini M4 Pro and Mac Studio M4 Max on Codemagic, measured on three open-source projects.
Results page: see `docs/index.html` at the root of this repository. Raw numbers: [`data/runs.csv`](data/runs.csv).

Apps: [XcodeBenchmark](apps/xcodebenchmark.md), [Signal iOS](apps/signal-ios.md), [Expensify](apps/expensify.md).

## Layout

| Path | Contents |
|---|---|
| [`METHOD.md`](METHOD.md) | Method v1: what is timed, how builds run, how to read the results |
| `apps/` | For each app: upstream repo, exact commit, what we changed, how to reproduce the checkout |
| `workflows/` | `codemagic.yaml` per app, with one workflow per machine type |
| `data/runs.csv` | One row per measured build |
| `tools/` | `summarize.py` prints median, fastest and slowest per app and machine; `build_site.py` generates the results page |

## What is measured

- **Headline number**: `BUILD_SECONDS`, the wall-clock time of the compile step only
  (`sh benchmark.sh` for XcodeBenchmark, `xcodebuild build` for Signal and Expensify). Clean build, no cache.
- **Logged but not in the headline**: dependency downloads and installs (Swift package resolution, Metal toolchain,
  Node/npm/bun, `npm ci`, `pod install`). They depend on the network.
- Same Xcode (26.6) and same source commit on every machine.
- Results are the **median of 5 runs** per app and machine.
- All builds ran on the regular shared build machine pools that customers use, during normal working hours.
  Build times on popular machine types can vary from run to run with overall demand.

## Machines

| Machine | Cores available to the build | Memory |
|---|---|---|
| Mac mini M2 (`mac_mini_m2`) | 7 | 12 GB |
| Mac mini M4 (`mac_mini_m4`) | 9 | 16 GB |
| Mac mini M4 Pro (default machine, no `instance_type`) | 13 | 32 GB |
| Mac Studio M4 Max (`mac_studio_m4_max`) | 15 | 32 GB |

Confirm the chip in the "Environment info" step of each build log.

## How to run

1. Check out an app at the pinned commit and add the workflow file as `codemagic.yaml` (see `apps/`).
2. Add the repo in Codemagic.
3. Start one workflow per machine type.
4. After each build, copy the values from the "Stop sampler and summarize" step into `data/runs.csv`
   (`BUILD_SECONDS` is the headline number).
5. Run `python3 tools/summarize.py`.

## Notes

- Five runs per app and machine is a small sample: use the median and treat the fastest run as a best case.
- Expensify is pinned to a commit that builds with Xcode 26.6, not the latest `main`.
