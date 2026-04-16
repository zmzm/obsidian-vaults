---
type: tool
status: active
updated: 2026-04-16
tags:
  - react-router
  - routing
  - types
---

# React Router

React Router is the routing and data-loading tool hub for this vault, especially where routing ergonomics intersect with type safety, framework mode, and server-driven application architecture.

## Key Ideas

- React Router is increasingly shaped not just by route matching but by typed route definitions, data APIs, and framework-oriented workflows.
- Type generation and typed navigation primitives change the reliability story for medium and large applications.
- It is useful to track React Router both against framework competitors and as part of the broader React app architecture space.

## Practical Significance

- This page should collect durable patterns around typed navigation, route data access, and route-module ergonomics.
- It is also a good comparison point against Next.js and TanStack Start where routing and data boundaries overlap.

## Current Signals

- The current raw layer already contains a clear signal around generated route types and typed navigation utilities.
- That is enough to justify treating React Router as a first-class tool page in the vault.
- New raw material also adds architectural guidance for loaders and actions as route-level integration boundaries.

## Related Pages

- [[Next.js]]
- [[../concepts/Server Components|Server Components]]
- [[../patterns/Testing Strategy for React Apps|Testing Strategy for React Apps]]
- [[../syntheses/Testing Modern React - RTL, Browser Mode, RSC, and Integration Boundaries|Testing Modern React - RTL, Browser Mode, RSC, and Integration Boundaries]]
- [[../patterns/Type-Driven Frontend Safety|Type-Driven Frontend Safety]]
- [[../topics/React Rendering|React Rendering]]
- [[../case-studies/Safer Frontend without React.FC|Safer Frontend without React.FC]]
- [[../sources/React Router Type Safety|React Router Type Safety]]
- [[../sources/React Router Integration Points|React Router Integration Points]]
- [[../sources/TWIR 270|TWIR 270]]

## Sources

- [[../../raw/twir/270/2026-02-25-TWIR-270|TWIR #270]]
- [[../../raw/twir/274/2026-03-25-TWIR-274|TWIR #274]]
- [[../sources/React Router Integration Points|React Router Integration Points]]
- [[../sources/React Router Type Safety|React Router Type Safety]]

## Open Questions

- How much of React Router's current advantage comes from framework mode versus core routing primitives.
- Which typed-route patterns should become dedicated pattern pages later.
