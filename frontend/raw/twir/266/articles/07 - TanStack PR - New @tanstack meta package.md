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
quality: keep
---

[[2026-01-28-TWIR-266|Index]]

# Item 7: TanStack PR - New @tanstack/meta package

Source: [https://github.com/TanStack/router/pull/6277](https://github.com/TanStack/router/pull/6277)

Summary:
TanStack introduces @tanstack/meta, a standalone package for unified SEO and meta tag management across React, Solid, and Vue routers. It provides meta builders (title, description, openGraph, twitter, etc.), JSON-LD builders with type-safe schema.org types, and utilities for merging and filtering meta tags. The package is well-tested, documented, and intended to replace legacy SEO helpers in TanStack projects.

Key takeaways:
- @tanstack/meta centralizes meta/SEO management with composable builders and merge utilities.
- Supports JSON-LD structured data with strong TypeScript types.
- Replaces legacy SEO helpers; encourages direct imports for clarity.
- Comprehensive documentation and tests included.

Recommendation:
Read fully (read fully if managing SEO/meta in TanStack-powered apps)

Why it matters:
read fully if managing SEO/meta in TanStack-powered apps

Content:
# Create composable meta management utility by tannerlinsley · Pull Request #6277 · TanStack/router · GitHub

```
Add a new meta.ts module with comprehensive utilities for managing meta tags:

- Core meta builders: title, description, charset, viewport
- SEO meta builders: robots, canonical, alternate, openGraph, twitter, verification, themeColor, appMeta
- JSON-LD builders with type-safe schema.org types: jsonLdWebsite, jsonLdOrganization, jsonLdArticle, jsonLdProduct, jsonLdBreadcrumbs, jsonLdFaq, jsonLdEvent, jsonLdLocalBusiness, jsonLdSoftwareApp, jsonLdVideo, jsonLdRecipe, jsonLdCourse
- Merge utilities: mergeMeta, mergeMetaWithOptions with configurable deduplication strategies
- Convenience functions: baseMeta for common defaults, excludeMeta and pickMeta for filtering

All utilities return MetaDescriptor arrays that can be spread into route head functions.
JSON-LD integrates seamlessly using the existing 'script:ld+json' descriptor type.

Exports are re-exported from @tanstack/react-router, @tanstack/solid-router, and @tanstack/vue-router for framework users.

Includes comprehensive unit tests (68 tests).
```
