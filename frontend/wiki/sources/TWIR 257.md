---
type: source
status: active
updated: 2026-04-14
tags:
  - twir
  - digest
  - nextjs
  - ppr
---

# TWIR 257

TWIR #257 is a useful routing source for Partial Prerendering, cache-related request semantics, and the tension between static shells and dynamic request-time data.

## Summary

- The issue contains one of the strongest current sources on Partial Prerendering.
- It reinforces the `use cache` and `next-intl` friction story through the same architectural area.
- It also provides supporting context for how async request APIs affect prerendering behavior.

## Why This Source Matters

- It materially strengthens the caching branch of the wiki.
- It helps move App Router caching discussion beyond isolated feature descriptions and into the mechanics of dynamic dependency detection.

## Limitations

- Only part of the issue maps directly onto the current wiki structure.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../patterns/Caching in App Router|Caching in App Router]]
- [[../concepts/Server Components|Server Components]]

## Raw Source

- [[../../raw/twir/257/2025-11-05-TWIR-257|2025-11-05-TWIR-257]]
