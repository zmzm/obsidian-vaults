---
type: source
status: active
updated: 2026-07-27
tags:
  - twir
  - digest
  - security
  - tanstack
  - ai
---

# TWIR 291

TWIR #291 is a digest around React and Next.js security patches, ReactBench for production React agent evaluation, TanStack Start TSRX experience, TanStack Table V9 reactivity, form state models, state-management reconsideration, composition patterns, and state boundaries in real Next.js apps.

## Summary

- React Server Functions received denial-of-service patches across the React Server Components packages, extending the existing RSC security branch beyond the earlier Flight-protocol DoS item.
- Next.js published July 2026 security updates covering Server Actions, App Router, Turbopack, Image Optimization, SSRF, middleware/proxy bypass, and cache confusion issues.
- ReactBench evaluates AI coding agents on realistic React work and checks quality beyond behavioral tests through React Doctor rules, accessibility checks, and maintainability constraints.
- TanStack Table V9 adds fine-grained atom-based reactivity behind mostly familiar APIs, complementing the earlier memory-refactor case study.
- React Hook Form versus TanStack Form and state-boundary articles reinforce a recurring theme: performance-sensitive React state design depends on subscription shape, scope, and ownership boundaries.

## Why This Source Matters

- It makes the security branch current again for both React Server Functions and Next.js framework surfaces.
- It adds a strong AI-assisted engineering quality source that fits the existing framework-and-agent synthesis.
- It deepens the TanStack branch from memory layout into reactivity and form-state modeling.

## Caveats

- Security version guidance is time-sensitive; use these notes for wiki routing, not as final upgrade advice without checking current advisories.
- TanStack Form and Table do not yet need separate tool hubs, but they are now stronger candidates if more sources accumulate.

## Related Pages

- [[../concepts/Server Components|Server Components]]
- [[../tools/Next.js|Next.js]]
- [[../tools/TanStack|TanStack]]
- [[../tools/TanStack Start|TanStack Start]]
- [[../patterns/Client-First Data Sync|Client-First Data Sync]]
- [[../patterns/Testing Strategy for React Apps|Testing Strategy for React Apps]]
- [[../patterns/Resilient React Components|Resilient React Components]]
- [[../sources/React2DoS|React2DoS]]
- [[Next.js Server Actions Security]]
- [[ReactBench]]
- [[../case-studies/TanStack Table Memory Refactor|TanStack Table Memory Refactor]]
- [[../syntheses/Frameworks as Constraints in the AI Era|Frameworks as Constraints in the AI Era]]

## Raw Source

- [[../../raw/twir/291/2026-07-22-TWIR-291|2026-07-22-TWIR-291]]
