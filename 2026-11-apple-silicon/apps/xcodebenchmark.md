# XcodeBenchmark

| | |
|---|---|
| Upstream | https://github.com/devMEremenko/XcodeBenchmark |
| Commit | `c1a951ac67` (merge of PR #681, 2026-10-16) |
| Changes | none, other than adding `codemagic.yaml` |
| Timed step | `sh benchmark.sh` (clean `xcodebuild` of a 42-CocoaPods project; Pods are checked in, no network step) |
| Workflow file | [`../workflows/xcodebenchmark.codemagic.yaml`](../workflows/xcodebenchmark.codemagic.yaml) |

## Reproduce

```bash
git clone https://github.com/devMEremenko/XcodeBenchmark.git
cd XcodeBenchmark
git checkout c1a951ac67
cp /path/to/this/repo/2026-11-apple-silicon/workflows/xcodebenchmark.codemagic.yaml codemagic.yaml
git add codemagic.yaml && git commit -m "Add Codemagic benchmark workflows"
```

Push the result to your own GitHub account, add it as an app in Codemagic, then run the
`xcodebenchmark-*` workflow for the machine you want to measure (see the top-level README).
