---
type: twir-item
issue: 218
item: 4
item_type: item
date: 2025-01-22
source: https://www.brenelz.com/posts/why-server-functions-matter-in-a-server-component-world/
tags:
  - "ServerFunctions"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-01-22-TWIR-218|Index]]

# Item 4: Why Server Functions Matter In A Server Component World

Source: [https://www.brenelz.com/posts/why-server-functions-matter-in-a-server-component-world/](https://www.brenelz.com/posts/why-server-functions-matter-in-a-server-component-world/)

Summary:
This article compares server functions (as seen in Tanstack Start) with React Server Components (RSC), clarifying their differences and tradeoffs. Server functions provide a client-centric architecture with transparent RPC for data fetching, while RSCs are server-centric and require a new paradigm. The author discusses data fetching, caching, and the importance of hoisting data fetching to avoid waterfalls, emphasizing that RSCs do not eliminate all data-fetching challenges.

Key takeaways:
- Server functions enable granular, client-driven data fetching and invalidation, while RSCs centralize data fetching on the server.
- RSCs require explicit cache management and can introduce server-side waterfalls if not carefully structured.
- Hoisting data fetching is still necessary in RSCs to avoid blocking unrelated components.
- The choice between architectures depends on project needs and developer preference.

Recommendation:
Read fully (for a nuanced understanding of modern React data-fetching patterns and tradeoffs)

Why it matters:
for a nuanced understanding of modern React data-fetching patterns and tradeoffs

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
