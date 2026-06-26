---
type: source
status: active
updated: 2026-06-26
tags:
  - twir
  - digest
  - server-components
  - security
  - tanstack-start
---

# TWIR 282

TWIR #282 is a high-value digest for React Flight protocol security, TanStack RSC usage, and state-library rerender behavior.

## Summary

- The issue includes two strong protocol-security stories: React2Shell as a Flight protocol RCE narrative and a separate Flight deserializer DoS case.
- TanStack RSC material explains RSC as a complement to data loading and SSR, especially for server-only data access and low-interactivity component trees.
- The Jotai rerender item is useful as a state-management performance note but does not yet need promotion.
- The TeamPCP supply-chain item reinforces npm, GitHub Actions, and editor extensions as connected frontend attack surfaces.

## Why This Source Matters

- It strengthens the Server Components branch by treating Flight as a real network/protocol boundary with validation and deserialization risk.
- It adds TanStack-specific RSC material that is not just a Next.js translation.
- It gives the security branch concrete evidence that modern React framework internals are externally reachable infrastructure.

## Caveats

- The vulnerability details should be treated as patch and architecture signals, not as evergreen exploit guidance.
- The Jotai article is narrower than the current wiki graph and can stay raw-only unless state-library performance becomes a larger branch.

## Related Pages

- [[../concepts/Server Components|Server Components]]
- [[../tools/TanStack Start|TanStack Start]]
- [[React2DoS]]
- [[TanStack RSC as Data Streams]]
- [[../syntheses/Server Components Beyond Next.js|Server Components Beyond Next.js]]

## Raw Source

- [[../../raw/twir/282/2026-05-20-TWIR-282|2026-05-20-TWIR-282]]
