---
type: twir-item
issue: 235
item: 1
item_type: featured
date: 2025-05-21
source: https://remix.run/blog/rsc-preview
tags:
  - "ReactRouter"
  - "RSC"
  - "using"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-05-21-TWIR-235|Index]]

# Item 1: React Router RSC Preview

Source: [https://remix.run/blog/rsc-preview](https://remix.run/blog/rsc-preview)

Summary:
React Router has released a preview of React Server Components (RSC) support, allowing incremental adoption in existing apps and new RSC-first routes. The preview demonstrates RSC integration via loaders/actions, server component routes, and server functions, with middleware for batching and caching. The implementation currently relies on Parcel, with Vite support pending, and aims to make RSC adoption seamless for React Router users.

Key takeaways:
- RSC can be returned from loaders/actions for incremental adoption, especially useful for CMS-backed or dynamic content.
- New "Server Component Routes" allow routes to be server-only, sending only necessary client code.
- Server functions using "use server" are supported, enabling server-side logic.
- Middleware for batching/caching queries is included; stable release awaits Vite RSC support.

Recommendation:
Read fully (for anyone considering RSC or React Router architecture changes)

Why it matters:
for anyone considering RSC or React Router architecture changes

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
