---
type: source
status: active
updated: 2026-04-22
tags:
  - tanstack-db
  - tanstack-query
  - sync
  - source
---

# TanStack DB Query-Driven Sync

This source captures TanStack DB's stronger claim beyond "faster client state": data access can be described as live queries over normalized collections, with the sync layer automatically deciding what to fetch, update, and recompute.

## Summary

- TanStack DB moves from embedded client database framing toward query-driven sync, where UI data requirements are declared as queries over collections.
- The model combines normalized local data, incremental live-query maintenance, and automatic request deduplication or pushdown against existing APIs.
- The practical promise is that teams can keep broad existing backends while moving more responsiveness and consistency into the client data layer.

## Why This Source Matters

- It gives the `TanStack DB` page a clearer architectural anchor than performance language alone.
- It also sharpens the distinction between TanStack Query as a fetch/cache tool and TanStack DB as a richer client-side data runtime.
- The source matters most for teams evaluating whether they need a query cache, a client database, or a fuller local-first sync layer.

## Caveats

- The framing is ambitious and direction-setting, so it should be read as an evolving model rather than settled mainstream practice.
- Many teams will still need to validate whether the complexity savings hold outside demos and data-heavy applications.

## Related Pages

- [[../tools/TanStack DB|TanStack DB]]
- [[../tools/TanStack Query|TanStack Query]]
- [[../patterns/Client-First Data Sync|Client-First Data Sync]]
- [[TWIR 245]]
- [[TWIR 249]]
- [[TWIR 258]]

## Raw Sources

- [[../../raw/twir/245/articles/01 - Stop Re-Rendering — TanStack DB, the Embedded Client Database for TanStack Query|Stop Re-Rendering — TanStack DB, the Embedded Client Database for TanStack Query]]
- [[../../raw/twir/249/articles/01 - An Interactive Guide to TanStack DB|An Interactive Guide to TanStack DB]]
- [[../../raw/twir/258/articles/01 - TanStack DB 0.5 — Query-Driven Sync|TanStack DB 0.5 — Query-Driven Sync]]
