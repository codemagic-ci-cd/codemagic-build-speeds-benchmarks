# Benchmarks

Codemagic released the powerful Mac mini M2 for the developers to build and test their apps faster. This document contains tests run on popular open-source native iOS projects to give you an idea about the fast speed in a real-world scenario and the comparison with M2 and M1 machines.

## [Xcode Benchmark](https://github.com/nevercode-rudrank/Benchmarks/tree/benchmark)

The first project is the famous `XcodeBenchmark` used to provide an idea about the performance of Mac mini M2 and Mac mini M1. It is a framework that includes **42 popular CocoaPods** libraries and **70+ dependencies** in total.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac mini M1)**
--- | --- | ---
Running Benchmark Tests | **3m 35s** | 5m 35s

- [`codemagic.yaml`](https://github.com/nevercode-rudrank/Benchmarks/blob/benchmark/codemagic.yaml)

- Codemagic Mac mini M2 Workflow  [![Codemagic build status](https://api.codemagic.io/apps/6269b3cc6248df946a077233/ios-m2-mac-mini-workflow/status_badge.svg)](https://codemagic.io/app/6269b3cc6248df946a077233/build/643fb4210684b3b2706ae810) 
- Codemagic Mac mini M1 Workflow  [![Codemagic build status](https://api.codemagic.io/apps/6269b3cc6248df946a077233/ios-m1-mac-mini-workflow/status_badge.svg)](https://codemagic.io/app/6269b3cc6248df946a077233/build/643fb41cb7c6fae51e9d3a12) 

## [Wikipedia iOS](https://github.com/nevercode-rudrank/wikipedia-ios)

The official Wikipedia iOS app is open-sourced. It also contains multiple dependencies and hundreds of tests.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac mini M1)**
--- | --- | ---
Building Project | **1m 20s** | 1m 42s
Running Tests | **2m 34s** | 3m 27s

- [`codemagic.yaml`](https://github.com/nevercode-rudrank/wikipedia-ios/blob/main/codemagic.yaml)

- Codemagic Mac mini M2 Workflow [![Codemagic build status](https://api.codemagic.io/apps/6267c85aeb4a9a0e7b7eba1b/wikipedia-m2-mini/status_badge.svg)](https://codemagic.io/app/6267c85aeb4a9a0e7b7eba1b/build/643fa4ada6c16df739a8e5c8)
- Codemagic Mac mini M1 Workflow [![Codemagic build status](https://api.codemagic.io/apps/6267c85aeb4a9a0e7b7eba1b/wikipedia-m1-mini/status_badge.svg)](https://codemagic.io/app/6267c85aeb4a9a0e7b7eba1b/build/643fa4ada6c16df739a8e5c7)

## [Signal iOS](https://github.com/nevercode-rudrank/Signal-iOS)

Signal is a free, open source, messaging app for simple private communication with friends. It is a great project for testing out benchmarks that replicates a real-world application.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac mini M1)**
--- | --- | ---
Building and Testing | **6m 51s** | 7m 37s

- [`codemagic.yaml`](https://github.com/nevercode-rudrank/Signal-iOS/blob/main/codemagic.yaml)

- Codemagic Mac mini M2 Workflow [![Codemagic build status](https://api.codemagic.io/apps/626e67f46248df64e0b79f91/ios-m2-mac-mini-workflow/status_badge.svg)](https://codemagic.io/app/626e67f46248df64e0b79f91/build/643fb05d4d88a8c286334f33)
- Codemagic Mac mini M1 Workflow [![Codemagic build status](https://api.codemagic.io/apps/626e67f46248df64e0b79f91/ios-m1-mac-mini-workflow/status_badge.svg)](https://codemagic.io/app/626e67f46248df64e0b79f91/build/643fb0598854fcfe834a8b75)

## [Mastodon iOS](https://github.com/nevercode-rudrank/mastodon-ios)

The official Mastodon iOS app's repository is available as open-source.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac mini M1)** | Bitrise M1 Medium | Bitrise M1 Large | GitHub Actions 
--- | --- | --- | --- | --- | ---
Building Project | **2m 12s** | 2m 50s | 2m 52s | 2m 23s | 4m 58s

- [`codemagic.yaml`](https://github.com/nevercode-rudrank/mastodon-ios/blob/develop/codemagic.yaml)
- [`bitrise.yml`](https://github.com/nevercode-rudrank/mastodon-ios/blob/develop/bitrise.yml)
- [`build.yaml`](https://github.com/nevercode-rudrank/mastodon-ios/blob/develop/.github/workflows/build.yml)

- Codemagic Mac mini M2 Workflow [![Codemagic build status](https://api.codemagic.io/apps/63a21b433246c3f84a9da7d4/mastodon-ios-m2/status_badge.svg)](https://codemagic.io/app/63a21b433246c3f84a9da7d4/build/643faf0fc112ac5cd5e19fb8)
- Codemagic Mac mini M1 Workflow [![Codemagic build status](https://api.codemagic.io/apps/63a21b433246c3f84a9da7d4/mastodon-ios-m1/status_badge.svg)](https://codemagic.io/app/63a21b433246c3f84a9da7d4/build/643faf0fc112ac5cd5e19fb6)
- Bitrise M1 Medium Workflow [![Build Status](https://app.bitrise.io/app/20f9f8b6-adf4-434b-a700-039980a5b5da/status.svg?token=ZDJViEYJT_bmDfhqbskqng&branch=master)](https://app.bitrise.io/build/fe09816a-fbfb-4a52-af39-fcc502606d1a)
- Bitrise M1 Large Workflow [![Build Status](https://app.bitrise.io/app/20f9f8b6-adf4-434b-a700-039980a5b5da/status.svg?token=ZDJViEYJT_bmDfhqbskqng&branch=master)](https://app.bitrise.io/build/fa7e62a8-d9d9-4ad6-a0ef-0126fffddf0f)
- GitHub Actions Workflow [![Build Status](https://github.com/nevercode-rudrank/mastodon-ios/actions/workflows/build.yml/badge.svg)](https://github.com/nevercode-rudrank/mastodon-ios/actions/runs/4796587895)
