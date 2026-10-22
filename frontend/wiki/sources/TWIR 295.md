---
type: source
evidence: mixed
evidence_reviewed: 2026-10-22
status: active
updated: 2026-10-22
tags: [twir, digest, frontend]
---

# TWIR 295

TWIR #295 (2026-09-02): styling migration contracts and browser-only rendering.

## Summary

- StyleX and Linear migration summaries reinforce the existing styling case study; reuse that case rather than create another Linear page.
- The durable styling theme is predictable composition, build-time work, and constrained customization, with migration tooling and team adoption treated together.
- The original browser() documentation and type-PR summaries disagree about stability. The recovered primary reference now supplies the mechanism and boundaries; exact package availability still needs version-specific verification.
- Next.js security, jsdom/RTL profiling, Vite SSG, and Nitro deployment are retained as issue references pending stronger extraction.

## Notable Articles

- [[../../raw/twir/295/articles/02 - Styling Linear for the future with StyleX|02 - Styling Linear for the future with StyleX]] — Extends the existing Linear case; extraction missing.
- [[../../raw/twir/295/articles/03 - A deep dive into StyleX|03 - A deep dive into StyleX]] — StyleX atomic extraction tutorial; summary-only.
- [[../../raw/twir/295/articles/05 - React Types PR - Types for React 19.3|05 - React Types PR - Types for React 19.3]] — Type-package PR does not by itself establish runtime stability.
- [[../../raw/twir/295/articles/06 - React DOM Docs - New use(browser(reason)) API|06 - React DOM Docs - New use(browser(reason)) API]] — Browser-only rendering under Suspense; summary-only.
- [[../../raw/twir/295/articles/09 - Making React Testing Library Tests 43% Faster|09 - Making React Testing Library Tests 43% Faster]] — Testing speedup reported in the summary; full measurement context unavailable.
- [[../../raw/twir/295/articles/10 - SSG for React with Vite|10 - SSG for React with Vite]] — Build-time prerendering as an alternative to CSR defaults; summary-only.

## Why This Source Matters

- Routes durable material into the related pages below while keeping thin announcements, missing extractions, and proposals at the digest/reference layer.

## Caveats

- Reviewed against the local issue MOC and 11 article notes on 2026-10-22; 11 notes lack extracted full text. Summary-only items remain references, not independently verified article readings.
- The August security note lacks full content here; no affected-version matrix or upgrade prescription is promoted from its summary.
- Release, PR, RFC, and security claims describe the captured source at its publication time. Check first-party material before using version-sensitive details operationally.

## Related Pages

- [[../case-studies/Linear StyleX Migration|Linear StyleX Migration]]
- [[../tools/StyleX|StyleX]]
- [[../patterns/Resilient React Components|Resilient React Components]]
- [[../patterns/Testing Strategy for React Apps|Testing Strategy for React Apps]]

- [[../tools/Nitro|Nitro]]

## Raw Source

- [[../../raw/twir/295/2026-09-02-TWIR-295|2026-09-02-TWIR-295]]

## Recovered Source Snapshots

Retrieved on 2026-10-22. These are later source snapshots; original intake failures remain preserved. A pending snapshot is available for review and does not validate earlier summaries. See [[../../system/Source Evidence|Source Evidence]].

- [[../../raw/twir/295/recovered/01 - StyleX|01 - StyleX]] — editorial review: insufficient.
- [[../../raw/twir/295/recovered/02 - Styling Linear for the future with StyleX|02 - Styling Linear for the future with StyleX]] — editorial review: pending.
- [[../../raw/twir/295/recovered/03 - A deep dive into StyleX|03 - A deep dive into StyleX]] — editorial review: pending.
- [[../../raw/twir/295/recovered/04 - Syntax.fm - Why everyone is moving to Stylex|04 - Syntax.fm - Why everyone is moving to Stylex]] — editorial review: pending.
- [[../../raw/twir/295/recovered/05 - React Types PR - Types for React 19.3|05 - React Types PR - Types for React 19.3]] — editorial review: pending.
- [[../../raw/twir/295/recovered/06 - React DOM Docs - New use(browser(reason)) API|06 - React DOM Docs - New use(browser(reason)) API]] — editorial review: reviewed.
- [[../../raw/twir/295/recovered/07 - How to Deploy a TanStack Start app to Vercel|07 - How to Deploy a TanStack Start app to Vercel]] — editorial review: reviewed.
- [[../../raw/twir/295/recovered/08 - Next.js August 2026 Security Release|08 - Next.js August 2026 Security Release]] — editorial review: pending.
- [[../../raw/twir/295/recovered/09 - Making React Testing Library Tests 43% Faster|09 - Making React Testing Library Tests 43% Faster]] — editorial review: pending.
- [[../../raw/twir/295/recovered/10 - SSG for React with Vite|10 - SSG for React with Vite]] — editorial review: pending.
- [[../../raw/twir/295/recovered/11 - This Month in React - Release candidate season; is that an asteroid hitting web educators|11 - This Month in React - Release candidate season; is that an asteroid hitting web educators]] — editorial review: pending.
