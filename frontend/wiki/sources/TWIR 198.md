---
type: source
status: active
updated: 2026-06-26
tags:
  - twir
  - digest
  - server-components
  - react-router
  - ssr
---

# TWIR 198

TWIR #198 is a dense issue around React prerender scheduling, Server Components tooling, React Router route config, TanStack Start server functions, ISR, RSC error handling, and SSR performance.

## Summary

- React core work on scheduling prerender after suspension continues the Suspense/prewarming branch.
- React DevTools Server Components support and RSC error handling make the RSC branch more operational.
- React Router `routes.ts`, TanStack Start server functions, and ISR/App Router material connect routing, server APIs, and framework data behavior.
- SSR performance and CSS-in-JS cost items support existing performance branches.

## Why This Source Matters

- It is one of the strongest old issues for RSC as tooling plus operations rather than only architecture.
- It also gives early support to typed route configuration and server-function framework design.

## Caveats

- Some API details are pre-stabilization and should be read historically.

## Related Pages

- [[../concepts/Server Components|Server Components]]
- [[../tools/React Router|React Router]]
- [[../tools/TanStack Start|TanStack Start]]
- [[../topics/SSR Performance|SSR Performance]]

## Raw Source

- [[../../raw/twir/198/2024-08-28-TWIR-198|2024-08-28-TWIR-198]]
