---
type: source
status: active
updated: 2026-06-26
tags:
  - react
  - compiler
  - toolchain
  - source
---

# React Compiler Toolchain Adoption

This source page normalizes the TWIR #286 cluster showing React Compiler support moving into linting and build-tool pipelines.

## Summary

- Oxlint can run React Compiler analysis in lint-only mode, surfacing React rule violations and optional compiler bailouts.
- Rolldown, SWC, Rspack, Next.js Turbopack, and Bun all show the Rust React Compiler moving closer to default build infrastructure.
- The adoption story is not only "turn on memoization"; it includes diagnostics, transform ordering, supported code surfaces, and bailout visibility.

## Why This Source Matters

- It updates the `React Compiler` concept from implementation signal to ecosystem integration signal.
- It supports the `React Compiler Silent Failures` case study by showing why diagnostics and bailouts matter.
- It reminds framework users that compiler behavior can differ across client, SSR, and Server Component code paths.

## Caveats

- Most integrations are experimental or early.
- Toolchain support does not mean application code is automatically compiler-compatible.

## Related Pages

- [[../concepts/React Compiler|React Compiler]]
- [[../topics/React Rendering|React Rendering]]
- [[../tools/Next.js|Next.js]]
- [[../case-studies/React Compiler Silent Failures|React Compiler Silent Failures]]
- [[React Compiler Rust Port]]
- [[React Compiler Adoption Maturity]]

## Raw Sources

- [[../../raw/twir/286/articles/01 - Oxlint 1.70 - Add a react react-compiler rule|Oxlint React Compiler rule]]
- [[../../raw/twir/286/articles/02 - Rolldown PR - Expose React Compiler options|Rolldown React Compiler options]]
- [[../../raw/twir/286/articles/03 - SWC PR - Add React Compiler|SWC React Compiler support]]
- [[../../raw/twir/286/articles/04 - Rspack PR - Bump SWC to support the React Compiler|Rspack React Compiler support]]
- [[../../raw/twir/286/articles/05 - Next.js PR - Add experimental Turbopack React Compiler support|Next.js Turbopack React Compiler support]]
- [[../../raw/twir/287/articles/02 - Bun PR - React Compiler integration|Bun React Compiler integration]]
- [[../../raw/twir/286/2026-06-17-TWIR-286|TWIR #286]]
- [[../../raw/twir/287/2026-06-24-TWIR-287|TWIR #287]]
