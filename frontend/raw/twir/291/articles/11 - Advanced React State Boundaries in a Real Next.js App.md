---
type: twir-item
issue: 291
item: 11
item_type: item
date: 2026-07-22
source: https://www.nirtamir.com/articles/advanced-react-questions
tags:
  - "Nextjs"
  - "TanStack"
  - "TanStackQuery"
status: auto
quality: keep
---

[[2026-07-22-TWIR-291|Index]]

# Item 11: Advanced React State Boundaries in a Real Next.js App

Source: [https://www.nirtamir.com/articles/advanced-react-questions](https://www.nirtamir.com/articles/advanced-react-questions)

Summary:
The author shares practical examples of handling complex state boundaries in a Next.js app that mixes server-rendered data, client state, browser APIs, URL state, and cache subscriptions. Scenarios include closing UI elements on route change, safely detecting browser-only APIs with useSyncExternalStore, and deriving reactive state from infinite queries. The focus is on making state ownership and reactivity explicit at each boundary, with code samples illustrating best practices.

Key takeaways:
- Use hooks like usePreviousValue and useSyncExternalStore to bridge between React state, browser APIs, and server/client boundaries.
- Deriving state from caches (e.g., TanStack Query) requires explicit subscriptions for reactivity.
- Advanced state management is about clear ownership and explicit notification across boundaries, not obscure hooks.
- Real-world examples highlight the importance of understanding where state lives and how updates propagate.

Recommendation:
Read fully (especially valuable for advanced React/Next.js developers dealing with hybrid state and reactivity)

Why it matters:
especially valuable for advanced React/Next.js developers dealing with hybrid state and reactivity

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[TanStack Query]]
