# Build Speeds Benchmarks

Codemagic offers the powerful Mac machines including M2, Mac Studio M2 Max, M2 Ultra machines, M4 and M4 Pro for developers to build and test their apps faster. This document contains tests run on popular open-source native iOS projects to give you an idea about the fast speed in a real-world scenario and the comparison with M2, Mac Studio M2 Max, M4 and M4 Pro machines.

> Benchmark builds last updated: October 8th, 2024

## [Xcode Benchmark](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-xcodeBenchmark/tree/master)

The first project is the famous `XcodeBenchmark` used to provide an idea about the performance of Mac mini M2 and Mac mini M1. It is a framework that includes **42 popular CocoaPods** libraries and **70+ dependencies** in total.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac Studio M2 Max)** | **Codemagic (Mac mini M4)** | **Codemagic (Mac mini M4 Pro)**
--- | --- | --- | --- | ---
Running Benchmark Tests | [**3m 45s**](https://codemagic.io/app/65a681d3ce3bc23535e15f5e/build/66167c6ec43448ce8901e144) | [1m 55s](https://codemagic.io/app/65a681d3ce3bc23535e15f5e/build/6705025a11c8161bba66419d) | [**2m 35s**](https://codemagic.io/app/65a681d3ce3bc23535e15f5e/build/67ada648d5e5fc402a5d8d65) | [**1m 55s**](https://codemagic.io/app/65a681d3ce3bc23535e15f5e/build/67ada5ec9db86a6dda96f61b)

- [`codemagic.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-xcodeBenchmark/blob/master/codemagic.yaml)

## [Signal iOS](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-signal_ios)

Signal is a free, open source, messaging app for simple private communication with friends. It is a great project for testing out benchmarks that replicate a real-world application.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac mini M4)** | **Codemagic (Mac mini M4 Pro)**
--- | --- | --- | ---
Building and Testing | [**6m 53s**](https://codemagic.io/app/67adbb042083e60da9a98395/build/67adbceac7740942d4f4443e) | [**4m 42s**](https://codemagic.io/app/67adbb042083e60da9a98395/build/67adc085a7f578f13d09be0b) | [**4m 15s**](https://codemagic.io/app/67adbb042083e60da9a98395/build/67adc0c81809a963f9589c2f)

- [`codemagic.yaml`](https://github.com/codemagic-ci-cd/Signal-iOS-Benchmark/blob/main/codemagic.yaml)

## [Mastodon iOS](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios)

The official Mastodon iOS app's repository is available as open-source.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac Studio M2 Max)** | **Codemagic (Mac mini M4)** | **Codemagic (Mac mini M4 Pro)**| GitHub Actions 
--- | --- | --- | --- | --- | ---
Building Project | [**3m 6s**](https://codemagic.io/app/65a42cf8f3786c75977de546/build/66167cc8f33970f5ab6b0803) | [2m 24s](https://codemagic.io/app/65a42cf8f3786c75977de546/build/670444ac910902d4e4cfce46) | [**1m 42s**](https://codemagic.io/app/65a42cf8f3786c75977de546/build/67accb9b300c3f169e4bac01) | [**1m 29s**](https://codemagic.io/app/65a42cf8f3786c75977de546/build/67acc9fa766d68168119eecc) | [9m 3s](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios/actions/runs/7585480789)

- [`codemagic.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios/blob/develop/codemagic.yaml)
- [`build.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios/blob/develop/.github/workflows/build.yml)

## [Expensify Chat app](https://github.com/codemagic-ci-cd/codemagic-benchmarks-project-expensify_chat_app)

The official Expensify React Native app's repository is available as open-source.

**Test name** | **Codemagic (Mac mini M2)** | **Codemagic (Mac Studio M2 Max)** | **Codemagic (Mac mini M4)** | **Codemagic (Mac mini M4 Pro)**
--- | --- | --- | --- | ---
Building Project | [**4m 23s**](https://codemagic.io/app/660936c197f2bee5b7353663/build/673654731bd5c81d4bac8598) | [2m 46s](https://codemagic.io/app/660936c197f2bee5b7353663/build/67365494bdb50729da7ac73a) | [**3m 56s**](https://codemagic.io/app/660936c197f2bee5b7353663/build/67acc37c97e6a0538526180a) | [**3m 1s**](https://codemagic.io/app/660936c197f2bee5b7353663/build/67acc2f30de29e74152c81cc) 

- [`codemagic.yaml`](https://github.com/codemagic-ci-cd/codemagic-benchmarks-project-expensify_chat_app/blob/main/codemagic.yaml)

## Contact Us
If you want to try out the new powerful M2, M2 Pro, Mac Studio M2 Max, and M2 Ultra machines, you can use the [contact form here](https://codemagic.io/contact/).
