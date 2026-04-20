---
type: twir-item
issue: 240
item: 2
item_type: item
date: 2025-06-25
source: https://nextjs.org/docs/app/getting-started/linking-and-navigating
tags:
  - "Nextjs"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-06-25-TWIR-240|Index]]

# Item 2: Linking and Navigating

Source: [https://nextjs.org/docs/app/getting-started/linking-and-navigating](https://nextjs.org/docs/app/getting-started/linking-and-navigating)

Summary:
This Next.js documentation explains how navigation works in the app directory, covering server rendering, prefetching, streaming, and client-side transitions. It details optimizations for dynamic routes and slow networks, emphasizing the use of `loading.tsx` for better user experience. The guide also discusses how Next.js leverages React Server Components and Suspense boundaries to provide fast, responsive navigation.

Key takeaways:
- Next.js uses server rendering by default, with prefetching and streaming to minimize navigation delays.
- Prefetching is automatic for static routes; dynamic routes benefit from partial prefetching if `loading.tsx` is present.
- Streaming enables immediate feedback by sending parts of a page as soon as they're ready.
- Client-side transitions preserve state and interactivity, making navigation seamless.

Recommendation:
Read fully (for those building or optimizing Next.js apps)

Why it matters:
for those building or optimizing Next.js apps

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
