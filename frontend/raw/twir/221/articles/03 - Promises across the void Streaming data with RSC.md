---
type: twir-item
issue: 221
item: 5
item_type: item
date: 2025-02-12
source: https://edspencer.net/2024/7/12/promises-across-the-void-react-server-components
tags:
  - "RSC"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-02-12-TWIR-221|Index]]

# Item 5: Promises across the void: Streaming data with RSC

Source: [https://edspencer.net/2024/7/12/promises-across-the-void-react-server-components](https://edspencer.net/2024/7/12/promises-across-the-void-react-server-components)

Summary:
This article demonstrates how React Server Components (RSC) can stream unresolved promises from server to client, enabling progressive data loading. Using the new React use() hook, client components can suspend rendering until server-sent promises resolve, improving perceived performance. The article explains the underlying mechanics, including how Next.js streams HTML and injects resolved data, and provides a live example for experimentation.

Key takeaways:
- RSC enables streaming of unresolved promises for progressive hydration.
- The use() hook allows client components to suspend until data is ready.
- Next.js streams HTML and injects resolved data via script tags for seamless updates.
- Understanding this flow is key for advanced RSC usage and optimizing user experience.

Recommendation:
Read fully (for developers working with RSC, streaming, or advanced SSR patterns)

Why it matters:
for developers working with RSC, streaming, or advanced SSR patterns

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
