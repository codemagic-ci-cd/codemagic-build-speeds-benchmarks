# Build Speeds Benchmarks

Codemagic offers the powerful Mac machines including M2, M2 Pro, Mac Studio M2 Max and M2 Ultra machines for the developers to build and test their apps faster. This document contains tests run on popular open-source native iOS projects to give you an idea about the fast speed in a real-world scenario and the comparison with M2 and Mac Studio M2 Max machines.

> Benchmark builds last updated: October 8th, 2024

## [Xcode Benchmark](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-xcodeBenchmark/tree/master)

The first project is the famous `XcodeBenchmark` used to provide an idea about the performance of Mac mini M2 and Mac mini M1. It is a framework that includes **42 popular CocoaPods** libraries and **70+ dependencies** in total.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac Studio M2 Max)**
--- | --- | ---
Running Benchmark Tests | [**3m 45s**](https://codemagic.io/app/65a681d3ce3bc23535e15f5e/build/66167c6ec43448ce8901e144) | [1m 55s](https://codemagic.io/app/65a681d3ce3bc23535e15f5e/build/6705025a11c8161bba66419d)

- [`codemagic.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-xcodeBenchmark/blob/master/codemagic.yaml)

## [Signal iOS](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-signal_ios)

Signal is a free, open source, messaging app for simple private communication with friends. It is a great project for testing out benchmarks that replicates a real-world application.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac Studio M2 Max)**
--- | --- | ---
Building and Testing | [**5m 45s**](https://codemagic.io/app/65a69265a20054f6b1f50029/build/67050a2e7faecbf7ee39fbcd) | [3m 51s](https://codemagic.io/app/65a69265a20054f6b1f50029/build/67050799b135571c9d296673)

- [`codemagic.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-signal_ios/blob/main/codemagic.yaml)

## [Mastodon iOS](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios)

The official Mastodon iOS app's repository is available as open-source.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac Studio M2 Max)** | GitHub Actions 
--- | --- | --- | ---
Building Project | [**3m 6s**](https://codemagic.io/app/65a42cf8f3786c75977de546/build/66167cc8f33970f5ab6b0803) | [2m 24s](https://codemagic.io/app/65a42cf8f3786c75977de546/build/670444ac910902d4e4cfce46) | [9m 3s](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios/actions/runs/7585480789)

- [`codemagic.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios/blob/develop/codemagic.yaml)
- [`build.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios/blob/develop/.github/workflows/build.yml)

## [Expensify Chat app](https://github.com/codemagic-ci-cd/codemagic-benchmarks-project-expensify_chat_app)

The official Expensify React Native app's repository is available as open-source.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac Studio M2 Max)** 
--- | --- | ---
Building Project | [**5m 4s**](https://codemagic.io/app/660936c197f2bee5b7353663/build/6613924355709ef49738d259) | [2m 47s](https://codemagic.io/app/660936c197f2bee5b7353663/build/67044abf89c339e2df0a8d04)

- [`codemagic.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-project-expensify_chat_app/blob/main/codemagic.yaml)

## Contact Us
If you want to try out the new powerful M2, M2 Pro, Mac Studio M2 Max, and M2 Ultra machines, you can use the [contact form here](https://codemagic.io/contact/).
