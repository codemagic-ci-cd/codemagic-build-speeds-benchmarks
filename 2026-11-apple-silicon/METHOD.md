# Method v1

This is how every result in the November 2026 Apple silicon benchmark was produced. If you follow the same steps on your own
Codemagic account, you should see times in the same range. Method v1 applies to this folder only. A later benchmark that
changes any rule below will be called v2 and will get its own folder.

## What we measure

One number per build: **build seconds**, the wall-clock time of the compile step.

- XcodeBenchmark: the `Build Time` the benchmark script itself reports (`sh benchmark.sh`).
- Signal iOS and Expensify: the duration of one clean `xcodebuild build` command, from start to
  `BUILD SUCCEEDED`.

Everything that depends mostly on the network is **not** timed: Metal toolchain download, Swift package resolution,
Node/npm/bun installation, `npm ci` and `pod install`. Their durations are logged in the data file
(`tooling_seconds`, `npm_seconds`, `pods_seconds`) so you can see them, but they are not part of the result.

## What we build

| Project | Source | Notes |
|---|---|---|
| XcodeBenchmark | upstream `devMEremenko/XcodeBenchmark` at a pinned commit | Unmodified; only a `codemagic.yaml` is added |
| Signal iOS | upstream `signalapp/Signal-iOS` at a pinned commit | Unmodified; only a `codemagic.yaml` is added; dependencies resolved before timing |
| Expensify | upstream `Expensify/App` at a pinned commit | Private Mobile-Expensify submodule removed; React Native built from source; `npm ci` and `pod install` before timing |

Exact commits and the steps to reproduce each checkout are in [`apps/`](apps/). Every build uses Xcode 26.6 on
macOS 26.5.1, the same on all machines.

## Where we build

| Machine | Instance type in `codemagic.yaml` | Cores available to the build | Memory |
|---|---|---|---|
| Mac mini M2 | `mac_mini_m2` | 7 | 12 GB |
| Mac mini M4 | `mac_mini_m4` | 9 | 16 GB |
| Mac mini M4 Pro | none: the default Mac machine | 13 | 32 GB |
| Mac Studio M4 Max | `mac_studio_m4_max` | 15 | 32 GB |

Each workflow prints the chip in an "Environment info" step so you can confirm it.

## How we run it

1. **Clean build.** Every build starts on a fresh build machine. There is no cache and no derived data from earlier builds.
2. **Prepare, untimed.** Install the tools and dependencies listed above.
3. **Time the compile.** Run the timed step once and record build seconds.
4. **Repeat.** Each project is built five times on each machine type. We report the **median** of the five, and also the
   fastest and slowest run, so you can see how much runs differ.
5. **Real conditions.** Builds ran in the shared production build pools that customers use, during normal working hours
   (23 and 24 November 2026). We did not reserve machines. Times on the most popular machine types can therefore vary from
   run to run with overall demand.

A run is repeated if its untimed preparation failed before the timed step, or if the build did not run on the machine type
we asked for.

## How to read the results

- Use the median as the typical result and the fastest run as a best case.
- "Speedup over Mac mini M2" is the M2 median divided by the other machine's median for the same project.
- Five runs per project and machine is a small sample. Treat differences of a few percent as noise.
- Results describe the whole build machine (chip, cores, memory), not the chip alone.

## How to repeat it

See the [README](README.md): check out a project at its pinned commit, add the workflow from [`workflows/`](workflows/) as
`codemagic.yaml`, start one workflow per machine type, and copy the numbers from the build summary into your own copy of
[`data/runs.csv`](data/runs.csv). `python3 tools/summarize.py` prints the medians.

## Version history

- **v1** (November 2026): first release. Three projects, four machine types, five runs each, median reported.
