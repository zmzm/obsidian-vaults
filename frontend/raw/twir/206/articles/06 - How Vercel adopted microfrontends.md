---
type: twir-item
issue: 206
item: 6
item_type: item
date: 2024-10-23
source: https://vercel.com/blog/how-vercel-adopted-microfrontends
tags:
  - "Microfrontends"
  - "Nextjs"
  - "Turbopack"
status: auto
quality: keep
---

[[2024-10-23-TWIR-206|Index]]

# Item 6: How Vercel adopted microfrontends

Source: [https://vercel.com/blog/how-vercel-adopted-microfrontends](https://vercel.com/blog/how-vercel-adopted-microfrontends)

Summary:
Vercel transitioned its main site from a monolithic Next.js app to vertical microfrontends to improve build times, developer velocity, and end-user performance. The migration leveraged Turborepo, Turbopack, and Next.js Multi-Zones, splitting the app by major sections (marketing, docs, dashboard) while maintaining shared components in a monorepo. The post discusses the trade-offs, migration strategies, and lessons learned, including challenges with navigation and local testing.

Key takeaways:
- Vertical microfrontends (split by path) reduced build times and simplified dependency management.
- Incremental migration and shared monorepo enabled consistency and minimized risk.
- Prefetching and Chromium’s Speculation Rules help mitigate hard navigation performance issues.
- Lessons learned are relevant for large-scale React/Next.js apps considering microfrontends.

Recommendation:
Read fully (for teams architecting large React/Next.js apps or exploring microfrontends)

Why it matters:
for teams architecting large React/Next.js apps or exploring microfrontends

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
