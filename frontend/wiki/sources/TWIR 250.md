---
type: source
status: active
updated: 2026-04-21
tags:
  - twir
  - digest
  - activity
  - server-components
---

# TWIR 250

TWIR #250 is a mixed but valuable issue around `<Activity />`, framework support matrices for RSC, and a real outage caused by effect misuse.

## Summary

- The issue captures `<Activity />` reaching canary.
- It includes a matrix of framework and library support for React Server Components.
- It also documents a Cloudflare outage caused by a bad `useEffect` dependency pattern.

## Why This Source Matters

- It strengthens both the async rendering branch and the effect-discipline branch with concrete real-world evidence.
- It also helps situate RSC support as an ecosystem-wide capability question rather than just a React-core one.

## Caveats

- The issue is broad and only some items warrant future standalone promotion.

## Related Pages

- [[../topics/React Rendering|React Rendering]]
- [[../concepts/Server Components|Server Components]]
- [[../patterns/Effects and Cleanup Discipline|Effects and Cleanup Discipline]]

## Raw Source

- [[../../raw/twir/250/2025-09-17-TWIR-250|2025-09-17-TWIR-250]]
