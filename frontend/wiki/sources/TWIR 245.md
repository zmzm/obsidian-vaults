---
type: source
status: active
updated: 2026-04-22
tags:
  - twir
  - digest
  - tanstack-db
  - react
---

# TWIR 245

TWIR #245 is a high-signal issue for TanStack DB, `use()` replacing thrown promises, `cacheSignal()`, and Next.js MCP tooling.

## Summary

- The issue introduces TanStack DB as a client-side database layer.
- It captures React deprecating "throw a Promise" in favor of `React.use(promise)`.
- It also adds `cacheSignal()` and Next.js MCP as important platform signals.

## Why This Source Matters

- It supports several branches that already matter in the vault: async React, data-layer evolution, and Next.js developer tooling.
- It is one of the stronger mid-archive issues for durable promotion work.

## Caveats

- The issue mixes API evolution, product tooling, and architecture patterns, so downstream curation still matters.

## Related Pages

- [[../concepts/React use()|React use()]]
- [[../tools/TanStack DB|TanStack DB]]
- [[../sources/React cacheSignal|React cacheSignal]]
- [[../tools/Next.js|Next.js]]

## Raw Source

- [[../../raw/twir/245/2025-07-30-TWIR-245|2025-07-30-TWIR-245]]
