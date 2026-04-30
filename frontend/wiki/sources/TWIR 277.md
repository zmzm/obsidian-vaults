---
type: source
status: active
updated: 2026-04-21
tags:
  - twir
  - digest
  - server-components
  - react
---

# TWIR 277

TWIR #277 is a high-signal digest for the current Server Components branch: alternative RSC architecture, Flight-protocol security, streaming internals, router ergonomics, and React performance work at scale.

## Summary

- The issue adds a strong new framing for RSCs as stream-shaped data rather than framework-owned trees.
- It captures a serious security event around the Flight protocol and makes the Server Components branch less purely architectural.
- It includes an important Next.js rendering-pipeline change around native Node.js streams.
- It also contributes practical guidance on React Router revalidation control, custom ESLint rules, and large-scale React rendering performance.

## Why This Source Matters

- It materially upgrades the `Server Components` page with new evidence on architecture, transport, and security.
- It adds concrete operational detail to the `Next.js` and `SSR Performance` branches.
- It broadens the React reliability branch with tooling and lint-based enforcement, not just conceptual advice.

## Caveats

- The issue mixes primary and secondary material, so each promoted page should still point to the specific article or PR.
- A few items remain raw-only because they are interesting but not yet central enough for the current wiki graph.

## Related Pages

- [[../concepts/Server Components|Server Components]]
- [[../tools/Next.js|Next.js]]
- [[../tools/TanStack Start|TanStack Start]]
- [[../tools/React Router|React Router]]
- [[../patterns/Type-Driven Frontend Safety|Type-Driven Frontend Safety]]
- [[../topics/React Rendering|React Rendering]]

## Raw Source

- [[../../raw/twir/277/2026-04-15-TWIR-277|2026-04-15-TWIR-277]]
