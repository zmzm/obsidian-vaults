---
type: source
status: active
updated: 2026-06-26
tags:
  - twir
  - digest
  - nextjs
  - security
  - react-router
---

# TWIR 281

TWIR #281 is a security-heavy digest around a broad Next.js release, the TanStack npm compromise, React projection experiments, and React Router dialog patterns.

## Summary

- The issue captures a coordinated Next.js security release covering multiple vulnerability classes across middleware, request handling, caching, and XSS.
- The TanStack compromise writeup provides a concrete supply-chain incident involving GitHub Actions cache poisoning and malicious package publication.
- `Projecting React` is interesting as a runtime-minimization experiment, but should stay raw-only until similar ideas repeat.
- React Router dialog guidance adds a practical routing/data-loading pattern, but does not yet need a dedicated page.

## Why This Source Matters

- It reinforces that framework security is a platform-maintenance concern, not an occasional patch-note detail.
- It gives the TanStack branch an operational security incident that sits next to the framework's growing production usage.
- It adds a React Router UI-routing example where route state, data loading, and modal behavior are coupled.

## Caveats

- The security release is important, but individual CVEs should only get their own pages if they become recurring architectural evidence.
- Runtime projection is speculative in this vault until there are more independent sources.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../tools/TanStack Start|TanStack Start]]
- [[../tools/React Router|React Router]]
- [[../syntheses/Frameworks as Constraints in the AI Era|Frameworks as Constraints in the AI Era]]
- [[../case-studies/TanStack Supply Chain Hardening|TanStack Supply Chain Hardening]]

## Raw Source

- [[../../raw/twir/281/2026-05-13-TWIR-281|2026-05-13-TWIR-281]]
