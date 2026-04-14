---
type: case-study
status: active
updated: 2026-04-14
tags:
  - nextjs
  - app-router
  - migration
  - server-components
---

# Next.js App Router Exit

This case study captures a team's decision to move away from Next.js App Router after a year of real production use.

## Context

- The team spent a meaningful period working with Next.js App Router and React Server Components in a professional setting.
- The article frames the eventual migration as a response to structural friction, not isolated bugs.

## What Broke Down

- Optimistic updates felt awkward or poorly supported.
- Data fetching on navigation created too much redundancy and complexity.
- Layout and component-boundary constraints made the architecture harder to reason about.
- Turbopack and surrounding framework ergonomics did not meet expectations.

## Why It Matters

- This is useful as a practice-oriented counterweight to framework release optimism.
- It gives the wiki a concrete migration narrative for when App Router and RSC do not fit a team’s workflow.
- It strengthens the comparison branch between Next.js and TanStack Start with a real operational story.

## Main Lesson

- Framework tradeoffs become clearest under sustained real-world usage, especially when data flows, optimistic UI, and architectural flexibility matter.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../tools/TanStack Start|TanStack Start]]
- [[../concepts/Server Components|Server Components]]
- [[../patterns/Caching in App Router|Caching in App Router]]
- [[../syntheses/Next.js vs TanStack Start|Next.js vs TanStack Start]]

## Raw Source

- [[../../raw/twir/255/articles/07 - One Year with Next.js App Router — Why We're Moving On|TWIR item note]]
- [[../../raw/twir/255/2025-10-22-TWIR-255|TWIR #255]]
