---
type: twir-item
issue: 199
item: 5
item_type: item
date: 2024-09-04
source: https://codehike.org/blog/build-time-components
tags:
  - "MDX"
  - "ServerComponents"
status: auto
quality: keep
---

[[2024-09-04-TWIR-199|Index]]

# Item 5: Build-time Components

Source: [https://codehike.org/blog/build-time-components](https://codehike.org/blog/build-time-components)

Summary:
This post explores how React Server Components and build-time plugins can transform content-driven sites by enabling data enrichment (e.g., adding Open Graph images to links) at build time instead of client-side. It compares client-side fetching with build-time transformations using remark/rehype plugins, demonstrating the tradeoffs in performance, user experience, and code complexity. The article walks through the Markdown-to-JSX pipeline and how to inject additional data during build.

Key takeaways:
- Build-time plugins can enrich content without client-side overhead.
- React Server Components enable more efficient, content-driven transformations.
- Client-side approaches are simpler but less performant and may leak logic to the client.
- Understanding the Markdown/MDX pipeline is key for advanced content workflows.

Recommendation:
Read fully (for those building content-heavy React/Next.js sites)

Why it matters:
for those building content-heavy React/Next.js sites

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
