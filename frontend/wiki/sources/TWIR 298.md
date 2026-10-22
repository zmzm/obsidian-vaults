---
type: source
status: active
updated: 2026-10-22
tags: [twir, digest, frontend]
---

# TWIR 298

TWIR #298 (2026-09-23): image scheduling, activity lifecycle, and flight boundaries.

## Summary

- The captured image reference connects SSR image discovery, preloading, accessibility, and View Transition coordination.
- Flight object references are feature-flagged opaque handles in a PR, not a stable general-purpose client data API.
- The ImageResponse advisory illustrates a runtime/dependency boundary distinct from Server Action authorization.
- The Activity article demonstrates why allocating a subscription during render and relying on later effect cleanup is unsafe: hidden UI may render without an effect mounting.
- The systems-oriented React explainer strengthens the distinction between source state, derived values, and external synchronization.

## Notable Articles

- [[../../raw/twir/298/articles/01 - React docs – New img API ref page|01 - React docs – New img API ref page]] — Canonical image documentation entry; item 2 duplicates it.
- [[../../raw/twir/298/articles/03 - React Flight PR – Server References for arbitrary object types|03 - React Flight PR – Server References for arbitrary object types]] — Experimental object-reference transport proposal.
- [[../../raw/twir/298/articles/04 - Next.js 16.3.6 – Security Update|04 - Next.js 16.3.6 – Security Update]] — Captured first-party security release; historical evidence, not current patch guidance.
- [[../../raw/twir/298/articles/06 - React Activity When A Render No Longer Guarantees an Effect|06 - React Activity When A Render No Longer Guarantees an Effect]] — Concrete lifecycle failure with Activity and legacy store hooks.
- [[../../raw/twir/298/articles/07 - Frontend for systems engineers|07 - Frontend for systems engineers]] — Derive UI from state and keep external synchronization explicit.

## Why This Source Matters

- Routes durable material into the related pages below while keeping thin announcements, missing extractions, and proposals at the digest/reference layer.

## Caveats

- Reviewed against the local issue MOC and 7 article notes on 2026-10-22; 0 notes lack extracted full text. Summary-only items remain references, not independently verified article readings.
- Items 1 and 2 are duplicate image documentation and supply one independent source signal.
- Release, PR, RFC, and security claims describe the captured source at its publication time. Check first-party material before using version-sensitive details operationally.

## Related Pages

- [[../concepts/React Activity|React Activity]]
- [[../patterns/Effects and Cleanup Discipline|Effects and Cleanup Discipline]]
- [[../concepts/React View Transitions|React View Transitions]]
- [[../syntheses/Frontend Security Boundaries in Server-First React|Frontend Security Boundaries in Server-First React]]

## Raw Source

- [[../../raw/twir/298/2026-09-23-TWIR-298|2026-09-23-TWIR-298]]
