---
type: source
status: active
updated: 2026-04-14
tags:
  - nextjs
  - ppr
  - caching
  - source
---

# Partial Prerendering Architecture

This source explains how Partial Prerendering evolved from error-based dynamic detection toward a promise-driven architecture.

## Summary

- PPR combines static shells with dynamic content fetched in parallel.
- Earlier error-based detection of dynamic access produced migration pain and unreliable behavior.
- Promise-based request APIs make dynamic dependency detection more explicit and more robust.

## Why This Source Matters

- It gives the `Caching in App Router` pattern page a much stronger architectural foundation.
- It clarifies why request-time APIs became async and how prerendering behavior is shaped by dynamic data access.

## Caveats

- The source is highly valuable for framework mechanics, but less directly useful for teams not using App Router or PPR-style rendering.

## Related Pages

- [[../patterns/Caching in App Router|Caching in App Router]]
- [[../tools/Next.js|Next.js]]
- [[../concepts/Server Components|Server Components]]

## Raw Sources

- [[../../raw/twir/257/articles/03 - Partial Prerendering - From error-based detection to promise-driven architecture for optimal web performance|TWIR item note]]
- [[../../raw/twir/257/2025-11-05-TWIR-257|TWIR #257]]
