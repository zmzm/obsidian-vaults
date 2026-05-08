---
type: twir-item
issue: 206
item: 3
item_type: item
date: 2024-10-23
source: https://www.yoseph.tech/posts/nextjs/server-side-state-management-in-nextjs-a-deep-dive-into-react-cache
tags:
  - "NextJS"
  - "Nextjs"
  - "ServerComponents"
status: auto
quality: keep
---

[[2024-10-23-TWIR-206|Index]]

# Item 3: Server Side State management in NextJS: a deep dive into React Cache

Source: [https://www.yoseph.tech/posts/nextjs/server-side-state-management-in-nextjs-a-deep-dive-into-react-cache](https://www.yoseph.tech/posts/nextjs/server-side-state-management-in-nextjs-a-deep-dive-into-react-cache)

Summary:
This article explores server-side state management in Next.js, focusing on how React’s cache, unstable_cache, and patched fetch enable efficient data handling in server components. It explains the differences between server and client state, the types of caching available, and practical patterns for using cache to avoid prop drilling and redundant fetches. The post includes code examples and discusses trade-offs and best practices for managing server state in modern Next.js apps.

Key takeaways:
- Server state is immutable during a render and fundamentally different from client state (no re-renders).
- React and Next.js provide cache, unstable_cache, and patched fetch for request and data caching.
- Proper use of cache can simplify code and improve performance, but requires a shift from traditional client-side patterns.
- Examples show how to structure code for efficient server-side data access and sharing.

Recommendation:
Read fully (for anyone working with Next.js server components or optimizing server-side data flows)

Why it matters:
for anyone working with Next.js server components or optimizing server-side data flows

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]], [[Next.js]]
