---
type: source
status: active
updated: 2026-04-30
tags:
  - react
  - compiler
  - migration
---

# React Compiler Adoption Maturity

This source captures the React Compiler branch after early release excitement: the important questions are now compatibility, migration behavior, ecosystem readiness, and tooling integration.

## Summary

- React Compiler automates memoization-oriented optimization but still depends on code following React's rules and supported patterns.
- Greenfield adoption is framed as easier than brownfield migration because older code and dependencies often contain patterns the compiler cannot safely transform.
- The source emphasizes that compiler optimization does not solve unrelated bottlenecks such as network latency, bundle size, or poor data architecture.
- The same TWIR issue also refreshes the Rust-port signal, showing that implementation work is moving toward faster toolchain integration with Babel, OXC, and SWC.

## Why This Source Matters

- It gives `React Compiler` a migration-oriented source, not only an implementation-oriented source.
- It helps separate compiler benefits from overclaiming: fewer manual memoization patterns are plausible, but architecture and data-flow bottlenecks remain.
- It strengthens the reliability branch because compiler adoption requires workflow checks, opt-outs, and awareness of unsupported patterns.

## Caveats

- This is ecosystem commentary, not an official React compatibility matrix.
- The exact maturity level of React Compiler and its Rust implementation may change quickly, so this page should be refreshed when official docs or release notes shift.

## Related Pages

- [[../concepts/React Compiler|React Compiler]]
- [[../topics/React Rendering|React Rendering]]
- [[React Compiler Rust Port]]
- [[../case-studies/React Compiler Silent Failures|React Compiler Silent Failures]]
- [[TWIR 279]]

## Raw Sources

- [[../../raw/twir/279/articles/03 - The React Compiler at Eighteen Months The Arc, the Debates, and What's Next|The React Compiler at Eighteen Months]]
- [[../../raw/twir/279/articles/02 - WIP port of React Compiler to Rust|WIP port of React Compiler to Rust]]
- [[../../raw/twir/279/2026-04-29-TWIR-279|TWIR #279]]
