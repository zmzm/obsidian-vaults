---
type: case-study
status: active
updated: 2026-04-30
tags:
  - nextjs
  - migration
  - tanstack-router
---

# ComfyDeploy Off Next.js

This case study captures a client-heavy product dashboard moving from Next.js to plain React with TanStack Router and Rspack because the framework's server-oriented features did not fit the team's workload.

## Summary

- The team reported much faster builds and hot reload after leaving Next.js for a simpler React stack.
- The migration traded away built-in server actions, caching, pre-rendering, and colocated server/client conventions.
- For their dashboard, those lost features were less valuable than clearer architecture, faster iteration, and more intentional API design.
- The story does not argue that Next.js is broadly bad; it narrows the fit question to product dashboards that do not need the full App Router/RSC feature set.

## Why This Case Matters

- It adds an early client-heavy counterexample to the Next.js platform branch.
- It supports `Next.js vs TanStack Start` and related fit discussions without making the `Next.js` hub itself anti-framework.
- It pairs well with later migration stories such as Railway's move away from Next.js.

## Caveats

- This is one team's dashboard context, not a general framework benchmark.
- The source predates later Next.js and TanStack Start changes, so use it as a fit case rather than a current feature comparison.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../tools/React Router|React Router]]
- [[../syntheses/Next.js vs TanStack Start|Next.js vs TanStack Start]]
- [[Railway Off Next.js]]
- [[../sources/TWIR 215|TWIR 215]]

## Sources

- [[../../raw/twir/215/articles/03 - You don't need Next.js|You don't need Next.js]]
- [[../../raw/twir/215/2025-01-02-TWIR-215|TWIR #215]]
