---
type: source
status: active
updated: 2026-04-30
tags:
  - react
  - server-components
  - bundling
---

# RSC Bundle Boundaries

This source captures the bundler-facing side of React Server Components and Server Actions: directives, client references, manifests, code splitting, and hydration metadata are part of the architecture.

## Summary

- RSC requires bundlers to distinguish server components, client components, and server actions through directives and package metadata.
- Client components are represented as references in server output rather than bundled as ordinary server-rendered implementation code.
- Runtime hydration depends on generated manifests and code-splitting metadata.
- This makes RSC adoption partly a framework and bundler integration problem, not just a React authoring problem.

## Why This Source Matters

- It strengthens `Server Components` with implementation evidence below the framework API layer.
- It supports `Server Components Beyond Next.js` by showing what any non-Next RSC stack must still solve.
- It connects to Next.js and Turbopack-style work where compiler/bundler behavior shapes application semantics.

## Caveats

- The source is a technical discussion rather than stable docs.
- Exact bundler behavior differs by webpack, Turbopack, Vite, Parcel, and custom RSC stacks.

## Related Pages

- [[../concepts/Server Components|Server Components]]
- [[../syntheses/Server Components Beyond Next.js|Server Components Beyond Next.js]]
- [[../tools/Next.js|Next.js]]
- [[TWIR 216]]

## Raw Sources

- [[../../raw/twir/216/articles/02 - RSC and Server Action Bundle Practice|RSC and Server Action Bundle Practice]]
- [[../../raw/twir/216/2025-01-08-TWIR-216|TWIR #216]]
