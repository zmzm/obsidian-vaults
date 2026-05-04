---
type: source
status: active
updated: 2026-04-30
tags:
  - react
  - compiler
  - rust
  - source
---

# React Compiler Rust Port

This source captures the work-in-progress Rust port of the React Compiler and is currently one of the most important implementation-level references for the topic in this vault.

## Summary

- The Rust port mirrors the TypeScript implementation while adapting internals to Rust-oriented data and ownership constraints.
- Early performance numbers are strong, with reported speedups both as a Babel plugin and in transformation-heavy paths.
- The work is explicitly positioned as an integration-friendly path for tools such as OXC and SWC.
- Correctness looks promising because the current fixture set passes, although some lower-level analysis pieces are still early.
- TWIR #279 adds a newer note that integrations with Babel, OXC, and SWC remain part of the strategic direction for the Rust implementation.

## Why This Source Matters

- It moves the React Compiler topic from abstract direction into concrete implementation.
- It suggests that compiler adoption may increasingly depend on tooling ecosystem integration rather than React alone.
- It provides evidence that compiler infrastructure is becoming a strategic part of frontend build pipelines.

## Caveats

- This is still WIP and should not be treated as a stable implementation baseline.
- Performance claims and implementation details may shift significantly before maturity.

## Related Pages

- [[../concepts/React Compiler|React Compiler]]
- [[../topics/React Rendering|React Rendering]]
- [[../tools/Next.js|Next.js]]

## Raw Sources

- [[../../raw/twir/275/articles/02 - React Compiler PR - WIP port of React Compiler to Rust|TWIR item note]]
- [[../../raw/twir/275/2026-04-01-TWIR-275|TWIR #275]]
- [[../../raw/twir/279/articles/02 - WIP port of React Compiler to Rust|TWIR #279 item note]]
- [[../../raw/twir/279/2026-04-29-TWIR-279|TWIR #279]]
