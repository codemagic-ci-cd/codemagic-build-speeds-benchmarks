# Build Speeds Benchmarks

Codemagic released the powerful Mac mini M2 for the developers to build and test their apps faster. This document contains tests run on popular open-source native iOS projects to give you an idea about the fast speed in a real-world scenario and the comparison with M2 and M1 machines.

> Benchmark builds last updated: January 15th, 2024

## [Xcode Benchmark](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-xcodeBenchmark/tree/master)

The first project is the famous `XcodeBenchmark` used to provide an idea about the performance of Mac mini M2 and Mac mini M1. It is a framework that includes **42 popular CocoaPods** libraries and **70+ dependencies** in total.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac mini M1)**
--- | --- | ---
Running Benchmark Tests | [**3m 45s**](https://codemagic.io/app/65a681d3ce3bc23535e15f5e/build/66167c6ec43448ce8901e144) | [4m 24s](https://codemagic.io/app/65a681d3ce3bc23535e15f5e/build/66167c745aa21421344e44dc)

- [`codemagic.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-xcodeBenchmark/blob/master/codemagic.yaml)

## [Signal iOS](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-signal_ios)

Signal is a free, open source, messaging app for simple private communication with friends. It is a great project for testing out benchmarks that replicates a real-world application.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac mini M1)**
--- | --- | ---
Building and Testing | [**6m 10s**](https://codemagic.io/app/65a69265a20054f6b1f50029/build/66167fb0cbb2090ae8f57a6e) | [6m 34s](https://codemagic.io/app/65a69265a20054f6b1f50029/build/66167fb2eb88ec68bf2bc41e)

- [`codemagic.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-signal_ios/blob/main/codemagic.yaml)

## [Mastodon iOS](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios)

The official Mastodon iOS app's repository is available as open-source.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac mini M1)** | GitHub Actions 
--- | --- | --- | ---
Building Project | [**3m 6s**](https://codemagic.io/app/65a42cf8f3786c75977de546/build/66167cc8f33970f5ab6b0803) | [3m 54s](https://codemagic.io/app/65a42cf8f3786c75977de546/build/66167cd0d007004d270a9ebf) | [9m 3s](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios/actions/runs/7585480789)

- [`codemagic.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios/blob/develop/codemagic.yaml)
- [`build.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios/blob/develop/.github/workflows/build.yml)

## Contact Us
If you want to try out the new powerful M2 machines, you can use the [contact form here](https://codemagic.io/contact/).
