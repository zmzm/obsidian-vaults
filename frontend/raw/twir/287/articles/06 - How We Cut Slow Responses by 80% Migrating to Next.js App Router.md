---
type: twir-item
issue: 287
item: 6
item_type: item
date: 2026-06-24
source: https://dev.to/subito/how-we-cut-slow-responses-by-80-migrating-to-nextjs-app-router-37da
tags:
  - "80"
  - "Nextjs"
  - "ServerComponents"
status: auto
quality: keep
---

[[2026-06-24-TWIR-287|Index]]

# Item 6: How We Cut Slow Responses by 80% Migrating to Next.js App Router

Source: [https://dev.to/subito/how-we-cut-slow-responses-by-80-migrating-to-nextjs-app-router-37da](https://dev.to/subito/how-we-cut-slow-responses-by-80-migrating-to-nextjs-app-router-37da)

Summary:
Subito migrated its high-traffic ad detail page from Next.js Pages Router to App Router, reducing slow responses by 80%. The migration was incremental, reusing client components and introducing server components for data fetching and streaming. Challenges included handling HTTP 410 responses and HTML streaming behind Nginx/Akamai, both of which were solved via Express middleware and CDN configuration.

Key takeaways:
- Incremental migration allowed product work to continue and avoided code duplication.
- Server components and React’s cache() enabled efficient data fetching and deduplication.
- HTML streaming required disabling buffering in Nginx and Akamai to display Suspense skeletons.
- Custom Express middleware handled HTTP 410 responses for expired ads, ensuring proper SEO signals.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
