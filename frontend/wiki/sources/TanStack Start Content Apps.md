---
type: source
status: active
updated: 2026-04-30
tags:
  - tanstack-start
  - content
  - routing
---

# TanStack Start Content Apps

This source captures a practical TanStack Start workflow for building content-driven React apps with Markdown, route loaders, server functions, and static prerendering.

## Summary

- The example builds a blog with Markdown files, metadata extraction, dynamic discovery, and route-level loading.
- TanStack loaders are isomorphic, so filesystem access is moved behind server functions rather than being used directly in client-capable code paths.
- The pattern shows TanStack Start as a general app framework, not only as a migration target away from Next.js.
- The source is especially useful for connecting routing, server functions, and content workflows into one explicit framework model.

## Why This Source Matters

- It strengthens the `TanStack Start` hub with a concrete application-building workflow.
- It supports the `Server Components Beyond Next.js` branch indirectly by showing the broader trend toward explicit server/client boundaries outside the Next.js default model.
- It gives the vault a non-comparison TanStack Start example, which keeps the tool page from becoming only an anti-Next.js archive.

## Caveats

- The article is tutorial-oriented, so it should support framework modeling rather than become a central architecture source by itself.
- Deployment and static generation details depend on the follow-up material, not only this first part.

## Related Pages

- [[../tools/TanStack Start|TanStack Start]]
- [[../concepts/Server Components|Server Components]]
- [[../syntheses/Server Components Beyond Next.js|Server Components Beyond Next.js]]
- [[TWIR 278]]

## Raw Sources

- [[../../raw/twir/278/articles/03 - Building a Blog in TanStack|TWIR item note]]
- [[../../raw/twir/278/2026-04-22-TWIR-278|TWIR #278]]
