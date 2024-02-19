# Build Speeds Benchmarks

Codemagic released the powerful Mac mini M2 for the developers to build and test their apps faster. This document contains tests run on popular open-source native iOS projects to give you an idea about the fast speed in a real-world scenario and the comparison with M2 and M1 machines.

> Benchmark builds last updated: January 15th, 2024

## [Xcode Benchmark](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-xcodeBenchmark/tree/master)

The first project is the famous `XcodeBenchmark` used to provide an idea about the performance of Mac mini M2 and Mac mini M1. It is a framework that includes **42 popular CocoaPods** libraries and **70+ dependencies** in total.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac mini M1)**
--- | --- | ---
Running Benchmark Tests | [**3m 56s**](https://codemagic.io/app/65a681d3ce3bc23535e15f5e/build/65cb2af809fc021e9b576435) | [4m 32s](https://codemagic.io/app/65a681d3ce3bc23535e15f5e/build/65d3442850c4be477f48f124)

- [`codemagic.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-xcodeBenchmark/blob/master/codemagic.yaml)

## [Signal iOS](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-signal_ios)

Signal is a free, open source, messaging app for simple private communication with friends. It is a great project for testing out benchmarks that replicates a real-world application.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac mini M1)**
--- | --- | ---
Building and Testing | [**6m 14s**](https://codemagic.io/app/65a69265a20054f6b1f50029/build/65cb2c0164a6a4ccfcc19c10) | [7m 10s](https://codemagic.io/app/65a69265a20054f6b1f50029/build/65aa991199bb5a43bbcb6cb5)

- [`codemagic.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-signal_ios/blob/main/codemagic.yaml)

## [Mastodon iOS](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios)

The official Mastodon iOS app's repository is available as open-source.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac mini M1)** | Bitrise M1 Medium | Bitrise M1 Large | GitHub Actions 
--- | --- | --- | --- | --- | ---
Building Project | [**3m 35s**](https://codemagic.io/app/65a42cf8f3786c75977de546/build/65a6521d9fe349444cb79888) | [4m 19s](https://codemagic.io/app/65a42cf8f3786c75977de546/build/65a664cc1f4be010c58152bd) | [3m 58s](https://app.bitrise.io/build/fa2a2e0b-a786-4992-9193-439648e94bcc) | [3m 29s](https://app.bitrise.io/build/7b0aef88-d2fa-401a-a775-696f3cfc4e1c) | [9m 3s](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios/actions/runs/7585480789)

- [`codemagic.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios/blob/develop/codemagic.yaml)
- [`bitrise.yml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios/blob/develop/bitrise.yml)
- [`build.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios/blob/develop/.github/workflows/build.yml)

## Contact Us
If you want to try out the new powerful M2 machines, you can use the [contact form here](https://codemagic.io/contact/).
