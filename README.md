
> [!NOTE]
> Benchmark result last updated: September 4th, 2025

# iOS and Xcode speed benchmarks

Platform | Xcode Benchmark | Signal | Mastodon | Expensify | Speedup (avg)
--- | --- | --- | --- | --- | ---
Mac Studio M4 Max | [1m 42s](https://codemagic.io/app/65a681d3ce3bc23535e15f5e/build/68bafad1e09b545a3bb10363) | [3m 59s](https://codemagic.io/app/67adbb042083e60da9a98395/build/68bae7ed07e933bf9cda224c) | [1m 18s](https://codemagic.io/app/65a42cf8f3786c75977de546/build/68bae407fa533b8901524a95) | [2m 38s](https://codemagic.io/app/660936c197f2bee5b7353663/build/68baf78a4ddd122b3138bfaf) | ****
Mac mini M4 Pro | [1m 55s](https://codemagic.io/app/65a681d3ce3bc23535e15f5e/build/67ada5ec9db86a6dda96f61b) | [4m 15s](https://codemagic.io/app/67adbb042083e60da9a98395/build/67adc0c81809a963f9589c2f) | [1m 29s](https://codemagic.io/app/65a42cf8f3786c75977de546/build/67acc9fa766d68168119eecc) | [3m 1s](https://codemagic.io/app/660936c197f2bee5b7353663/build/67acc2f30de29e74152c81cc) |
Mac mini M4 | [2m 35s](https://codemagic.io/app/65a681d3ce3bc23535e15f5e/build/67ada648d5e5fc402a5d8d65) | [4m 42s](https://codemagic.io/app/67adbb042083e60da9a98395/build/67adc085a7f578f13d09be0b) | [1m 42s](https://codemagic.io/app/65a42cf8f3786c75977de546/build/67accb9b300c3f169e4bac01) | [3m 56s](https://codemagic.io/app/660936c197f2bee5b7353663/build/67acc37c97e6a0538526180a) |
Mac mini M2 (baseline) | [3m 45s](https://codemagic.io/app/65a681d3ce3bc23535e15f5e/build/66167c6ec43448ce8901e144) | [6m 53s](https://codemagic.io/app/67adbb042083e60da9a98395/build/67adbceac7740942d4f4443e) | [3m 6s](https://codemagic.io/app/65a42cf8f3786c75977de546/build/66167cc8f33970f5ab6b0803) | [4m 23s](https://codemagic.io/app/660936c197f2bee5b7353663/build/673654731bd5c81d4bac8598) | -
GitHub Actions | N/A | N/A | [9m 3s](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios/actions/runs/7585480789) | N/A | -
Expo EAS Build | N/A | N/A | N/A | [7m 53s](https://expo.dev/accounts/icarusduz/projects/newexpensify/builds/0b4aaef9-139b-4c01-b983-4547dc6658ed) | -

# Android speed benchmarks

Platform | Signal | Speedup (avg)
--- | --- | ---
Linux X4 | [6m 6s](https://codemagic.io/app/68a446079dc90741beb93701/build/68aefbd77ed34178e54e3f60) | **21%**
Linux X2 (baseline) | [7m 24s](https://codemagic.io/app/68a446079dc90741beb93701/build/68aefbb3f4e6c76e6a021c6c) | -

# About the projects

1. The first project is the famous [Xcode Benchmark](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-xcodeBenchmark/tree/master). It is a framework that includes **42 popular CocoaPods** libraries and **70+ dependencies** in total.
2. [Signal](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-signal_ios) is a free, open source, messaging app for simple private communication with friends. It is a great project for testing out benchmarks that replicate a real-world application.
3. The official [Mastodon](https://github.com/codemagic-ci-cd/codemagic-benchmarks-projects-mastodon-ios) app's repository is available as open-source.
4. The official [Expensify](https://github.com/codemagic-ci-cd/codemagic-benchmarks-project-expensify_chat_app) React Native app's repository is available as open-source.

# Contact Us
If you want to try out the new powerful Mac mini M4 Pro, Mac Studio M2 Max, and M2 Ultra machines, you can use the [contact form here](https://codemagic.io/contact/).
