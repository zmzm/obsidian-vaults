---
type: twir-item
issue: 266
item: 7
item_type: item
date: 2026-01-28
source: https://github.com/TanStack/router/pull/6277
tags:
  - "TanStack"
  - "PR"
status: auto
---

[[2026-01-28-TWIR-266|Index]]

# Item 7: TanStack PR – New @tanstack/meta package

Source: [https://github.com/TanStack/router/pull/6277](https://github.com/TanStack/router/pull/6277)

Summary:
TanStack introduces a new @tanstack/meta package for unified SEO and meta tag management across its router libraries. The package provides utilities for building meta tags, JSON-LD schema, merging strategies, and filtering, with comprehensive TypeScript types and tests. It is now the recommended way to manage SEO/meta in TanStack-powered apps, with updated documentation and migration away from legacy helpers.

Key takeaways:
- New @tanstack/meta package centralizes meta/SEO management for React, Solid, and Vue routers.
- Includes meta builders (title, description, openGraph, twitter, etc.) and JSON-LD schema generators.
- Provides merge utilities and filtering for complex meta scenarios.
- Comprehensive documentation, usage examples, and tests included.

Recommendation: Summary sufficient (read PR/docs if you use TanStack Router and need advanced SEO/meta handling)
