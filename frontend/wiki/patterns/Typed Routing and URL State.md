---
type: pattern
status: active
updated: 2026-04-22
tags:
  - routing
  - url
  - type-safety
  - react
---

# Typed Routing and URL State

Typed Routing and URL State is the pattern page for treating routes, params, links, and search state as one validated application contract instead of a pile of loosely related strings.

## Key Ideas

- Typed routing is strongest when route params, links, search params, and route-level context all share one coherent contract.
- Static types help, but durable URL safety also needs runtime parsing, serialization, validation, and migration paths.
- The practical goal is not "more generics"; it is making navigation and URL-backed state harder to misuse across the whole application.

## Practical Significance

- This pattern gives the vault a dedicated place for route manifests, typed links, search-param validation, and nested route inheritance.
- It also creates a cleaner bridge between `React Router`, `TanStack Start`, `Next.js`, and the broader `Type-Driven Frontend Safety` branch.

## Current Signals

- The archive now shows multiple frameworks converging on typed routing primitives: generated route types in React Router, route manifests and typed links in Next.js, and type-safe param/search inheritance in TanStack Router.
- The same archive also shows why that is still incomplete: URL state is a public contract that needs schema-aware parsing, throttled writes, and migration thinking.
- That is enough to justify a dedicated pattern page instead of burying routing safety inside generic type-safety discussions.

## Related Pages

- [[../tools/React Router|React Router]]
- [[../tools/TanStack Start|TanStack Start]]
- [[../tools/Next.js|Next.js]]
- [[Type-Driven Frontend Safety]]
- [[../sources/React Router Type Safety|React Router Type Safety]]
- [[../sources/URL State Safety|URL State Safety]]
- [[../sources/TWIR 238|TWIR 238]]
- [[../sources/TWIR 242|TWIR 242]]
- [[../sources/TWIR 243|TWIR 243]]
- [[../sources/TWIR 247|TWIR 247]]
- [[../sources/TWIR 254|TWIR 254]]

## Sources

- [[../../raw/twir/238/articles/03 - Beware The URL Type-Safety Iceberg|Beware The URL Type-Safety Iceberg]]
- [[../../raw/twir/242/articles/03 - Next.js PR – Generate route types manifest|Next.js PR – Generate route types manifest]]
- [[../../raw/twir/243/articles/02 - Next.js draft PR – Initial support for typed links|Next.js draft PR – Initial support for typed links]]
- [[../../raw/twir/247/articles/01 - nuqs 2.5 - Debounce, Standard Schema, TanStack Router, Key isolation, and more|nuqs 2.5 - Debounce, Standard Schema, TanStack Router, Key isolation, and more]]
- [[../../raw/twir/254/articles/03 - Context Inheritance in TanStack Router|Context Inheritance in TanStack Router]]
- [[../sources/React Router Type Safety|React Router Type Safety]]
- [[../sources/URL State Safety|URL State Safety]]

## Open Questions

- Whether frameworks will converge on a shared mental model for typed links, search params, and route manifests or keep exposing incompatible routing contracts.
- How much URL state validation should live in router-level contracts versus separate query-state libraries.
