---
type: twir-item
issue: 224
item: 6
item_type: item
date: 2025-03-05
source: https://www.bennett.ink/its-probably-time-to-stop-recommending-redux
tags:
  - "TanStackQuery"
status: auto
quality: keep
---

[[2025-03-05-TWIR-224|Index]]

# Item 6: It's probably time to stop recommending Redux

Source: [https://www.bennett.ink/its-probably-time-to-stop-recommending-redux](https://www.bennett.ink/its-probably-time-to-stop-recommending-redux)

Summary:
The author argues that Redux and similar global state managers are often unnecessary in modern React apps, especially with the rise of hooks and API caching libraries like TanStack Query. Most state needs can be handled with local state, API caches, and props, reserving global state only for truly complex scenarios. The post encourages developers to reconsider defaulting to Redux and to leverage simpler, more modular approaches.

Key takeaways:
- Redux is rarely needed for typical React apps; local state and API caches suffice for most cases.
- Global state can harm modularity and encapsulation.
- Modern libraries and hooks (e.g., useState, useQuery) handle most state needs efficiently.
- Only use complex state management for genuinely complex, collaborative, or performance-critical apps.

Recommendation:
Read fully (read fully if evaluating or debating state management approaches)

Why it matters:
read fully if evaluating or debating state management approaches

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[TanStack Query]]
