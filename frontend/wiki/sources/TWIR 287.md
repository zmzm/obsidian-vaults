---
type: source
status: active
updated: 2026-06-26
tags:
  - twir
  - digest
  - react-compiler
  - performance
  - server-components
---

# TWIR 287

TWIR #287 is a digest around Fragment refs, Bun React Compiler integration, StyleX migration, TanStack Table memory reduction, Waku Slices, and Next.js App Router performance migration.

## Summary

- Fragment ref documentation is a React API signal but remains canary-only.
- Bun integrating the upstream React Compiler continues the cross-toolchain compiler-adoption theme.
- Linear's styled-components to StyleX migration and TanStack Table V9's prototype refactor are concrete performance case-study candidates.
- Waku Slices adds another example of RSC-era framework experimentation around reusable render configuration.
- The App Router migration success story balances earlier migration-away-from-Next.js material with a case where App Router reduced slow responses.

## Why This Source Matters

- It rounds out the React Compiler branch by adding Bun to the integration surface.
- It adds strong performance evidence at two levels: styling/runtime contracts and object-allocation shape for large tables.
- It keeps the Next.js fit story balanced: App Router can be a performance win in some server-heavy contexts even when other products leave it.

## Caveats

- Fragment refs are canary-only and should not be generalized as stable API guidance.
- The TanStack Table item is broad engineering evidence but may need a dedicated case-study page only if table/data-grid performance becomes more central.

## Related Pages

- [[../concepts/React Compiler|React Compiler]]
- [[../concepts/Server Components|Server Components]]
- [[../tools/Astro|Astro]]
- [[../tools/Next.js|Next.js]]
- [[../topics/React Rendering|React Rendering]]
- [[../topics/SSR Performance|SSR Performance]]
- [[React Compiler Toolchain Adoption]]
- [[../case-studies/Linear StyleX Migration|Linear StyleX Migration]]
- [[../case-studies/TanStack Table Memory Refactor|TanStack Table Memory Refactor]]
- [[../case-studies/Next.js App Router Slow Responses|Next.js App Router Slow Responses]]

## Raw Source

- [[../../raw/twir/287/2026-06-24-TWIR-287|2026-06-24-TWIR-287]]
