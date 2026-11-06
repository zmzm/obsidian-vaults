---
type: twir-item
issue: 304
item: 7
item_type: item
date: 2026-11-04
source: https://github.com/vercel/next.js/pull/100130
tags:
  - "Nextjs"
  - "PR"
  - "routego"
status: auto
quality: keep
---

[[2026-11-04-TWIR-304|Index]]

# Item 7: Next.js PR - Experimental Go Route Handlers with route.go files

Source: [https://github.com/vercel/next.js/pull/100130](https://github.com/vercel/next.js/pull/100130)

Summary:
Next.js adds experimental support for App Router route handlers written in Go, enabled with experimental.goRoutes: true and Turbopack. Go handlers can define HTTP methods directly and integrate with Next.js routing, metadata, and deployment adapters. The implementation includes robust compilation, caching, and lifecycle management, with comprehensive test coverage.

Key takeaways:
- Developers can write route handlers in Go for Next.js App Router (experimental).
- Go handlers support automatic HEAD/OPTIONS and signature validation.
- Integration covers development, production, and deployment scenarios.
- Still experimental; not all features or platforms may be fully supported.

Recommendation:
Read fully (read fully if interested in Go/Next.js integration or experimental features)

Why it matters:
read fully if interested in Go/Next.js integration or experimental features

Content:
# [experiment] support App Router route.go handlers by timneutkens · Pull Request #100130 · vercel/next.js · GitHub

```
Resolve conflicts with #100130 (App Router route.go handlers). Keep this branch's AppPage route shape (app_paths, is_internal), runtime route identities and native route publication, together with canary's AppGoRoute route, Go endpoint and native route listeners.

Turbopack dev now gets its route inventory from the native snapshot instead of the removed route watcher, so Go routes need the same treatment there that canary gave them in the watcher:
- the snapshot turns app-route-go routes into APP_ROUTE_GO identities, and napi sends their runtime page and pathname as for other route handlers;
- ensurePage and pathname lookups count APP_ROUTE_GO as an App route (isAppRouteKind). Without this, every Go route returned 404 in Turbopack dev;
- AppGoRouteRouteDefinition gains a matching identity type;
- the Go route set updates only after install() accepts an entrypoints update.
```
