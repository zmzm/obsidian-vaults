---
type: source
status: active
updated: 2026-07-27
tags:
  - react
  - compiler
  - memoization
  - source
---

# React Compiler Production Memoization

This source captures a production-oriented React Compiler adoption signal: automated memoization can remove manual `useMemo` and `useCallback` work, but it also exposes purity, mutable-reference, and third-party-library compatibility problems.

## Summary

- Enabling the compiler in a production Next.js codebase reduced reliance on manual memoization primitives.
- Subtle failures appeared around mutable refs and libraries whose APIs do not fit React Compiler assumptions cleanly.
- Lint rules, purity discipline, and opt-out directives become part of the adoption workflow, not optional polish.
- React Hook Form-style patterns are a reminder that library internals can be the real compatibility boundary.

## Why This Source Matters

- It complements the existing silent-failure case study with a more adoption-oriented memoization story.
- It shifts the compiler branch from "will it optimize?" toward "which code and libraries are compiler-compatible enough to trust?"
- It keeps React Compiler advice grounded in migration workflow rather than hype around removing memoization.

## Caveats

- The raw note does not include full article content, so details should be rechecked before turning this into prescriptive migration guidance.

## Related Pages

- [[../concepts/React Compiler|React Compiler]]
- [[React Compiler Adoption Maturity]]
- [[React Compiler Toolchain Adoption]]
- [[../case-studies/React Compiler Silent Failures|React Compiler Silent Failures]]
- [[TWIR 289]]

## Raw Source

- [[../../raw/twir/289/articles/04 - I let React Compiler handle memoization Here's what actually broke|I let React Compiler handle memoization]]
