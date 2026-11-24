# Expensify (New Expensify, standalone NewDot, iOS)

| | |
|---|---|
| Upstream | https://github.com/Expensify/App |
| Commit | `d9731a30e203be2db8a4e87acb6d90371c6884d6` (2026-11-09) |
| Changes | remove the private `Mobile-Expensify` submodule (standalone NewDot); add `codemagic.yaml` |
| Timed step | `xcodebuild build`, scheme `New Expensify Dev`, `DebugDevelopment`, `generic/platform=iOS`, code signing disabled |
| Not timed | Node/npm/bun install, `npm ci`, `pod install` (logged as `TOOLING_SECONDS`, `NPM_SECONDS`, `PODS_SECONDS`) |
| Workflow file | [`../workflows/expensify.codemagic.yaml`](../workflows/expensify.codemagic.yaml) |

## Why this commit

The next upstream commit (d6cf1cff, 2026-11-09) adds native code that uses iOS 27.1 SDK APIs
(`HybridVerticalBarModule.swift`). That does not compile with Xcode 26.6, the only Xcode on the
Codemagic image at the time. `d9731a30` is its parent. It is a merge commit on a contributor's branch, not a commit on `main`.

## Reproduce

```bash
git clone https://github.com/Expensify/App.git
cd App
git checkout d9731a30e203be2db8a4e87acb6d90371c6884d6
git rm -q .gitmodules Mobile-Expensify      # private submodule: run standalone NewDot instead
cp /path/to/this/repo/2026-11-apple-silicon/workflows/expensify.codemagic.yaml codemagic.yaml
git add codemagic.yaml && git commit -m "Add Codemagic benchmark workflows"
```

Push to your own GitHub account, add the repo in Codemagic and run the `expensify-*` workflow for the machine you want.

## Notes

- React Native is built from source (`BUILD_RN_FROM_SOURCE=1`). Expensify's default path downloads patched prebuilt
  artifacts from a private registry, and a download would measure the network, not the Mac.
- Node 26.12.1, npm 11.20.0 and bun 1.4.4 are installed in the first step (the repo enforces exact versions).
- Run `expensify-env-check` once first: it takes about 3 minutes and confirms the setup before a full build.
