---
type: twir-item
issue: 202
item: 8
item_type: item
date: 2024-09-25
source: https://sunilpai.dev/posts/ppr-for-everyone/
tags:
  - "Nextjs"
  - "PPR"
  - "ServerComponents"
status: auto
quality: keep
---

[[2024-09-25-TWIR-202|Index]]

# Item 8: Partial Prerendering for Everyone with Cloudflare Workers

Source: [https://sunilpai.dev/posts/ppr-for-everyone/](https://sunilpai.dev/posts/ppr-for-everyone/)

Summary:
This post explains how to implement Next.js-style Partial Prerendering (PPR) in any React SSR app using Cloudflare Workers. It leverages React’s new prerender() API to freeze rendering at Suspense boundaries and streams the static shell from the edge, resuming dynamic rendering from the origin. The approach improves initial load performance and can be adopted incrementally.

Key takeaways:
- Demonstrates PPR using React’s prerender() and resumeToPipeableStream().
- Streams static shell from edge, continues dynamic rendering from origin.
- Works with any React SSR stack, not limited to Next.js or RSCs.
- Improves performance by combining edge delivery and dynamic data fetching.

Recommendation:
Read fully

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
