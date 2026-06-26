---
type: source
status: active
updated: 2026-06-26
tags:
  - twir
  - digest
  - react-compiler
  - nextjs
  - tanstack-start
---

# TWIR 286

TWIR #286 is the strongest React Compiler toolchain digest in this batch, covering Oxlint diagnostics, Rolldown, SWC, Rspack, and Next.js Turbopack integration.

## Summary

- Oxlint adds an experimental `react/react-compiler` rule that can surface React rule violations and compiler bailouts without running the full build transform.
- Rolldown, SWC, and Rspack all show the Rust React Compiler moving into lower-level build pipelines.
- Next.js adds experimental Turbopack support for the Rust compiler on client and SSR code, while excluding Server Components.
- TanStack Start mental-model and LLM-safe design-system items are useful secondary signals for framework education and AI-assisted UI constraints.

## Why This Source Matters

- It shifts React Compiler from an isolated React feature into a cross-toolchain integration story.
- It makes compiler diagnostics part of authoring workflow, not only production optimization.
- It clarifies that compiler adoption will vary by code surface: client, SSR, and RSC paths are not identical.

## Caveats

- Most integrations are experimental and should be treated as adoption signals, not stable recommendations.
- Toolchain support does not imply application code is automatically compiler-friendly; bailout visibility remains important.

## Related Pages

- [[../concepts/React Compiler|React Compiler]]
- [[../tools/Next.js|Next.js]]
- [[../tools/TanStack Start|TanStack Start]]
- [[../topics/React Rendering|React Rendering]]
- [[../case-studies/React Compiler Silent Failures|React Compiler Silent Failures]]
- [[React Compiler Toolchain Adoption]]

## Raw Source

- [[../../raw/twir/286/2026-06-17-TWIR-286|2026-06-17-TWIR-286]]
