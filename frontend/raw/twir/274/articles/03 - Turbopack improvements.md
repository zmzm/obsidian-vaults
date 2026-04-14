---
type: twir-item
issue: 274
item: 3
item_type: item
date: 2026-03-25
source: https://nextjs.org/blog/next-16-2-turbopack
tags:
  - "Nextjs"
  - "TypeScript"
status: auto
---

[[2026-03-25-TWIR-274|Index]]

# Item 3: Turbopack improvements

Source: [https://nextjs.org/blog/next-16-2-turbopack](https://nextjs.org/blog/next-16-2-turbopack)

Summary:
Turbopack, the default Next.js bundler, receives significant upgrades in 16.2: server fast refresh, SRI support, tree shaking for dynamic imports, inline loader configuration, and over 200 bug fixes. These changes enhance build performance, security, and developer ergonomics, with a focus on parity and stability.

Key takeaways:
- Server Fast Refresh is now fine-grained and much faster, reloading only changed modules.
- Subresource Integrity (SRI) can be enabled for JS files, improving security.
- Tree shaking now applies to dynamic imports, reducing bundle size.
- Inline loader config via import attributes allows per-import customization.
- TypeScript support for `postcss.config.ts` and experimental Lightning CSS configuration added.

Recommendation: Read fully
