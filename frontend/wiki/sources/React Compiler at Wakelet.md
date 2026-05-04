---
type: source
status: active
updated: 2026-04-30
tags:
  - react
  - compiler
  - performance
---

# React Compiler at Wakelet

This source captures a production React Compiler adoption story where performance improved, but migration success depended on code quality and compatibility rather than blind enablement.

## Summary

- Wakelet reported meaningful INP and LCP improvements after adopting React Compiler.
- Most issues surfaced during adoption were framed as pre-existing code problems rather than compiler defects.
- Bundle size increases were noted but accepted relative to UX improvements.
- The strongest gains appeared in pure React components, which reinforces the compiler's dependency on compatible component patterns.

## Why This Source Matters

- It gives `React Compiler` a production adoption signal, not only implementation or ecosystem commentary.
- It supports `React Compiler Adoption Maturity` by showing that compiler migration can expose latent bugs and unsupported patterns.
- It complements `React Compiler Silent Failures` because both sources point toward workflow checks around compiler adoption.

## Caveats

- This is a single production report, not a general benchmark.
- Reported performance gains depend on app shape and should not be generalized without measurement.

## Related Pages

- [[../concepts/React Compiler|React Compiler]]
- [[React Compiler Adoption Maturity]]
- [[../case-studies/React Compiler Silent Failures|React Compiler Silent Failures]]
- [[TWIR 217]]

## Raw Sources

- [[../../raw/twir/217/articles/07 - Adopting the compiler at Wakelet|Adopting the compiler at Wakelet]]
- [[../../raw/twir/217/2025-01-15-TWIR-217|TWIR #217]]
