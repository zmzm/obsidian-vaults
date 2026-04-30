---
type: source
status: active
updated: 2026-04-21
tags:
  - twir
  - digest
  - server-components
  - vite
---

# TWIR 232

TWIR #232 is a valuable issue for RSC portability, deployment neutrality, optimistic querying, and subtle React runtime behavior.

## Summary

- The issue includes work on `react-server-dom-vite`, making RSC support in Vite a more explicit goal.
- It surfaces a Next.js documentation shift away from unnecessary Vercel-centric framing.
- It also covers serialized promises, `useEffect` execution order, and concurrent optimistic updates in Query.

## Why This Source Matters

- It strengthens the vault's archive around framework-neutral RSC support and data-flow mechanics.
- It also supports Query and effect-order reasoning with useful raw references.

## Caveats

- The issue spans platform policy, internals, and app patterns, so it is more routing than synthesis.

## Related Pages

- [[../concepts/Server Components|Server Components]]
- [[../tools/TanStack Query|TanStack Query]]
- [[../patterns/Effects and Cleanup Discipline|Effects and Cleanup Discipline]]

## Raw Source

- [[../../raw/twir/232/2025-04-30-TWIR-232|2025-04-30-TWIR-232]]
