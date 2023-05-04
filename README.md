# Build Speeds Benchmarks

Codemagic released the powerful Mac mini M2 for the developers to build and test their apps faster. This document contains tests run on popular open-source native iOS projects to give you an idea about the fast speed in a real-world scenario and the comparison with M2 and M1 machines.

> Benchmark builds last updated: April 19th, 2023

## [Xcode Benchmark](https://github.com/nevercode-rudrank/Benchmarks/tree/benchmark)

The first project is the famous `XcodeBenchmark` used to provide an idea about the performance of Mac mini M2 and Mac mini M1. It is a framework that includes **42 popular CocoaPods** libraries and **70+ dependencies** in total.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac mini M1)**
--- | --- | ---
Running Benchmark Tests | [**3m 35s**](https://codemagic.io/app/6269b3cc6248df946a077233/build/643fb4210684b3b2706ae810) | [5m 35s](https://codemagic.io/app/6269b3cc6248df946a077233/build/643fb41cb7c6fae51e9d3a12)

- [`codemagic.yaml`](https://github.com/nevercode-rudrank/Benchmarks/blob/benchmark/codemagic.yaml)

## [Wikipedia iOS](https://github.com/nevercode-rudrank/wikipedia-ios)

The official Wikipedia iOS app is open-sourced. It also contains multiple dependencies and hundreds of tests.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac mini M1)**
--- | --- | ---
Building Project | [**1m 20s**](https://codemagic.io/app/6267c85aeb4a9a0e7b7eba1b/build/643fa4ada6c16df739a8e5c8) | [1m 42s](https://codemagic.io/app/6267c85aeb4a9a0e7b7eba1b/build/643fa4ada6c16df739a8e5c7)
Running Tests | [**2m 34s**](https://codemagic.io/app/6267c85aeb4a9a0e7b7eba1b/build/643fa4ada6c16df739a8e5c8) | [3m 27s](https://codemagic.io/app/6267c85aeb4a9a0e7b7eba1b/build/643fa4ada6c16df739a8e5c7)

- [`codemagic.yaml`](https://github.com/nevercode-rudrank/wikipedia-ios/blob/main/codemagic.yaml)

## [Signal iOS](https://github.com/nevercode-rudrank/Signal-iOS)

Signal is a free, open source, messaging app for simple private communication with friends. It is a great project for testing out benchmarks that replicates a real-world application.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac mini M1)**
--- | --- | ---
Building and Testing | [**6m 51s**](https://codemagic.io/app/626e67f46248df64e0b79f91/build/643fb05d4d88a8c286334f33) | [7m 37s](https://codemagic.io/app/626e67f46248df64e0b79f91/build/643fb05d4d88a8c286334f33)

- [`codemagic.yaml`](https://github.com/nevercode-rudrank/Signal-iOS/blob/main/codemagic.yaml)

## [Mastodon iOS](https://github.com/nevercode-rudrank/mastodon-ios)

The official Mastodon iOS app's repository is available as open-source.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac mini M1)** | Bitrise M1 Medium | Bitrise M1 Large | GitHub Actions 
--- | --- | --- | --- | --- | ---
Building Project | [**2m 12s**](https://codemagic.io/app/63a21b433246c3f84a9da7d4/build/643faf0fc112ac5cd5e19fb8) | [2m 50s](https://codemagic.io/app/63a21b433246c3f84a9da7d4/build/643faf0fc112ac5cd5e19fb6) | [2m 52s](https://app.bitrise.io/build/fe09816a-fbfb-4a52-af39-fcc502606d1a) | [2m 23s](https://app.bitrise.io/build/fa7e62a8-d9d9-4ad6-a0ef-0126fffddf0f) | [4m 58s](https://github.com/nevercode-rudrank/mastodon-ios/actions/runs/4796587895)

- [`codemagic.yaml`](https://github.com/nevercode-rudrank/mastodon-ios/blob/develop/codemagic.yaml)
- [`bitrise.yml`](https://github.com/nevercode-rudrank/mastodon-ios/blob/develop/bitrise.yml)
- [`build.yaml`](https://github.com/nevercode-rudrank/mastodon-ios/blob/develop/.github/workflows/build.yml)

## Contact Us
If you want to try out the new powerful M2 machines, you can use the [contact form here](https://codemagic.io/contact/).
