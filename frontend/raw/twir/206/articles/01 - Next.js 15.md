---
type: twir-item
issue: 206
item: 1
item_type: featured
date: 2024-10-23
source: https://nextjs.org/blog/next-15
tags:
  - "Nextjs"
  - "15"
  - "Compiler"
  - "Turbopack"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2024-10-23-TWIR-206|Index]]

# Item 1: Next.js 15

Source: [https://nextjs.org/blog/next-15](https://nextjs.org/blog/next-15)

Summary:
Next.js 15 is now stable, introducing React 19 support, major caching changes, a stable Turbopack for development, new APIs, and improved upgrade tooling. Breaking changes include async request APIs and a shift to uncached defaults for fetches and route handlers. The release emphasizes smoother upgrades (via codemods), enhanced server observability, and improved build and development performance. TypeScript support for config, enhanced forms, and security improvements for server actions are also included.

Key takeaways:
- React 19 is fully supported, including experimental React Compiler and hydration error improvements.
- Async request APIs (headers, cookies, params, searchParams) are now asynchronous, requiring code changes (codemod provided).
- Caching defaults have changed: fetches and GET route handlers are uncached by default, with opt-in for caching.
- Turbopack is now stable for development, and build/dev performance is improved.
- New APIs: static route indicator, instrumentation.js, enhanced forms, and TypeScript support for next.config.
- Security and self-hosting improvements, plus ESLint 9 support.

Recommendation:
Read fully (especially if upgrading or maintaining Next.js apps; breaking changes and new APIs require attention)

Why it matters:
especially if upgrading or maintaining Next.js apps; breaking changes and new APIs require attention

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
