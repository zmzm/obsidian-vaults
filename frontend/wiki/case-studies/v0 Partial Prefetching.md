---
type: case-study
status: active
updated: 2026-10-22
tags: [nextjs, prefetching, caching, testing]
---

# v0 Partial Prefetching

v0 improved navigation by defining which destination UI must already be available at click time, then iterating on cache and prefetch boundaries until persistent tests proved that target.

## Context

- The extracted account distinguishes reusable prefetched route content from work intentionally deferred until navigation.
- The instant() test helper holds back navigation-only content so assertions can check what was already prepared, instead of mistaking a fast network response for successful prefetching.
- The workflow establishes a passing baseline, adds target assertions that fail, changes cache/prefetch structure, rebuilds, and keeps the regression test after it passes.
- Adoption also involves freshness, invalidation, repeated visits, and production cost; a passing instant-navigation assertion proves a bounded property rather than the whole user experience.

## Why It Matters

- Turn an optimization goal into a precise availability assertion and retain that assertion as a regression check.
- Use the extracted 16.4 case as the strong reference; the earlier 16.3 v0 note is summary-only.

## Related Pages

- [[../patterns/Caching in App Router|Caching in App Router]]
- [[../patterns/Component Confidence Boundaries|Component Confidence Boundaries]]
- [[../sources/Next.js 16.4|Next.js 16.4]]
- [[../syntheses/Frameworks as Constraints in the AI Era|Frameworks as Constraints in the AI Era]]

## Sources

- [[../../raw/twir/302/articles/06 - Improving navigation experience in v0 with Next.js 16.4|06 - Improving navigation experience in v0 with Next.js 16.4]]
- [[../../raw/twir/294/articles/11 - Making Navigations Instant in v0 (Next.js 16.3 Case Study)|11 - Making Navigations Instant in v0 (Next.js 16.3 Case Study)]] — summary-only earlier account.

## Open Questions

- Which destination elements are worth preparing before a user commits to navigation?
- How should immediate availability be balanced against stale personalized data and cache spend?
