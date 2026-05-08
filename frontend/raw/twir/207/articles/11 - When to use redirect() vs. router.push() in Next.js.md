---
type: twir-item
issue: 207
item: 11
item_type: item
date: 2024-10-30
source: https://darios.blog/posts/redirect-vs-router-push-in-nextjs
tags:
  - "Nextjs"
  - "vs"
  - "routerpush"
  - "ServerComponents"
status: auto
quality: keep
---

[[2024-10-30-TWIR-207|Index]]

# Item 11: When to use redirect() vs. router.push() in Next.js

Source: [https://darios.blog/posts/redirect-vs-router-push-in-nextjs](https://darios.blog/posts/redirect-vs-router-push-in-nextjs)

Summary:
This article clarifies the differences between redirect() and router.push() in Next.js. router.push() is for client-side navigation in event handlers, while redirect() is for server-side redirection in server components, functions, or route handlers. It also notes subtle behaviors, such as redirect() throwing exceptions and its interaction with Suspense boundaries.

Key takeaways:
- Use router.push() for client-side navigation (event handlers in client components).
- Use redirect() for server-side redirection (server components, functions, route handlers).
- redirect() throws an exception and behaves differently in various contexts (HTTP 307 vs 303).
- Be cautious with Suspense boundaries when using redirect().

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
