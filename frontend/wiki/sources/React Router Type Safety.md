---
type: source
status: active
updated: 2026-04-14
tags:
  - react-router
  - types
  - source
---

# React Router Type Safety

This source captures a meaningful shift in React Router ergonomics toward generated types, type-safe route access, and checked navigation helpers.

## Summary

- Generated route types improve access to params, loaders, and actions.
- `useRoute` gives typed access to route data by route ID.
- `href()` makes navigation links safer by checking them against route definitions.
- These capabilities currently belong to framework mode rather than library mode.

## Why This Source Matters

- It gives the `React Router` tool page a concrete direction of travel instead of a generic description.
- It is useful for tracking how routing tools increasingly compete on type systems and generated ergonomics.

## Caveats

- The feature set described here is mode-dependent, which matters when comparing React Router usage styles.

## Related Pages

- [[../tools/React Router|React Router]]
- [[../tools/Next.js|Next.js]]

## Raw Sources

- [[../../raw/twir/274/articles/09 - Type Safety in React Router|TWIR item note]]
- [[../../raw/twir/274/2026-03-25-TWIR-274|TWIR #274]]
