# Signal iOS

| | |
|---|---|
| Upstream | https://github.com/signalapp/Signal-iOS |
| Commit | `45372289a9387cd4271a2f7a47dba8ba92951e41` (2026-11-19) |
| Changes | none, other than adding `codemagic.yaml` |
| Timed step | `xcodebuild build`, scheme `Signal`, Debug, `generic/platform=iOS`, code signing disabled |
| Not timed | Metal toolchain download and Swift package resolution (both depend on the network) |
| Workflow file | [`../workflows/signal-ios.codemagic.yaml`](../workflows/signal-ios.codemagic.yaml) |

## Reproduce

```bash
git clone https://github.com/signalapp/Signal-iOS.git
cd Signal-iOS
git checkout 45372289a9387cd4271a2f7a47dba8ba92951e41
cp /path/to/this/repo/2026-11-apple-silicon/workflows/signal-ios.codemagic.yaml codemagic.yaml
git add codemagic.yaml && git commit -m "Add Codemagic benchmark workflows"
```

Push to your own GitHub account, add the repo in Codemagic and run the `signal-*` workflow for the machine you want.

## Notes

- Xcode 26.6 on every machine. Signal's own `.xcode-version` may ask for a newer Xcode; the pinned commit above built with 26.6.
