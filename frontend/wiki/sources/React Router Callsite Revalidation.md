---
type: source
status: active
updated: 2026-04-21
tags:
  - react-router
  - revalidation
  - routing
  - source
---

# React Router Callsite Revalidation

This source captures a shift in React Router from route-file revalidation policy toward callsite-level control where navigations and mutations are actually triggered.

## Summary

- Loader revalidation can now be opted out of directly from navigation, fetcher, form, and link callsites.
- This reduces the need to duplicate `shouldRevalidate` logic across every active route in a tree.
- The feature keeps React Router's data model but makes control more local and easier to reason about.

## Why This Source Matters

- It strengthens the `React Router` page with a more specific ergonomics signal than typed routes alone.
- It is useful for the vault because it connects routing APIs to maintainability and local reasoning instead of only framework capability.
- It also shows React Router continuing to refine how much implicit refetching behavior should be exposed to application authors.

## Caveats

- The feature was still marked unstable in the captured source, so the exact API shape may evolve.
- It is most useful in apps that already feel friction from broad default revalidation.

## Related Pages

- [[../tools/React Router|React Router]]
- [[React Router Middleware]]
- [[React Router Integration Points]]
- [[TWIR 277]]

## Raw Sources

- [[../../raw/twir/277/articles/07 - Contributing Callsite Revalidation Opt-out to React Router|TWIR item note]]
- [[../../raw/twir/277/2026-04-15-TWIR-277|TWIR #277]]
