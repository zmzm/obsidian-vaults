---
type: case-study
status: active
updated: 2026-04-21
tags:
  - nextjs
  - migration
  - tanstack
  - vite
---

# Railway Off Next.js

This case study preserves a production migration from Next.js to a Vite- and TanStack-based frontend stack driven by iteration speed, explicit control, and better fit for a client-heavy product.

## Context

- Railway's application was highly stateful, real-time, and predominantly client-driven.
- Build times and framework mismatch had become structural friction rather than isolated inconvenience.

## What Changed

- The team first removed Next.js-specific APIs and then swapped the framework in a second large migration step.
- Routing and layouts moved toward TanStack-style primitives with more explicit control and generated route safety.
- Deployment behavior stayed stable while build speed, dev-loop speed, and asset-level caching improved significantly.

## Why It Matters

- This is stronger comparison evidence than a generic "frameworks are different" essay because it is tied to production constraints and migration work.
- It shows that framework fit depends on product shape: a client-heavy app can experience Next.js complexity as a tax instead of leverage.
- It also adds fresh support for the explicit-architecture side of the `Next.js vs TanStack Start` branch.

## Main Lesson

- Framework choice becomes clearest when measured against real product topology, iteration speed, and where rendering work actually belongs.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../tools/TanStack Start|TanStack Start]]
- [[../topics/SSR Performance|SSR Performance]]
- [[../syntheses/Next.js vs TanStack Start|Next.js vs TanStack Start]]
- [[../syntheses/Next.js Portability Boundaries|Next.js Portability Boundaries]]
- [[../sources/TWIR 276|TWIR 276]]

## Raw Source

- [[../../raw/twir/276/articles/04 - Moving Railway's Frontend Off Next.js|TWIR item note]]
- [[../../raw/twir/276/2026-04-08-TWIR-276|TWIR #276]]
