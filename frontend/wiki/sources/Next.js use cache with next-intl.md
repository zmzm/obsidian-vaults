---
type: source
status: active
updated: 2026-04-14
tags:
  - nextjs
  - use-cache
  - i18n
  - source
---

# Next.js use cache with next-intl

This source captures a practical friction point in the Server Components ecosystem: the mismatch between `use cache` and request-time locale resolution in `next-intl`.

## Summary

- `use cache` depends on avoiding request-time APIs in the cached path.
- `next-intl` commonly relies on request-derived locale resolution, which conflicts with that requirement.
- The current workaround is to move locale into static params and explicit props.
- A future `next/root-params` API is expected to reduce this friction.

## Why This Source Matters

- It turns `use cache` from a generic feature into a concrete architecture tradeoff.
- It is useful for understanding how caching directives interact with framework and i18n design.

## Caveats

- The guidance here is tied to a transitional framework state and may age quickly as Next.js evolves.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../concepts/Server Components|Server Components]]
- [[../concepts/React use()|React use()]]
- [[../patterns/Caching in App Router|Caching in App Router]]

## Raw Sources

- [[../../raw/twir/274/articles/04 - Implementing Next.js 16 'use cache' with next-intl Internationalization|TWIR item note]]
- [[../../raw/twir/274/2026-03-25-TWIR-274|TWIR #274]]
