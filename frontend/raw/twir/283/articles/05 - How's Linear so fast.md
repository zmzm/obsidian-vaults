---
type: twir-item
issue: 283
item: 5
item_type: item
date: 2026-05-27
source: https://performance.dev/how-is-linear-so-fast-a-technical-breakdown
tags:
  - "TanStack"
  - "Performance"
  - "TanStackQuery"
status: auto
quality: keep
---

[[2026-05-27-TWIR-283|Index]]

# Item 5: How's Linear so fast?

Source: [https://performance.dev/how-is-linear-so-fast-a-technical-breakdown](https://performance.dev/how-is-linear-so-fast-a-technical-breakdown)

Summary:
This technical breakdown analyzes how Linear achieves exceptional UI performance, focusing on local-first data storage, optimistic updates, and a streamlined tech stack. The article explains how Linear minimizes perceived latency by updating the UI from a local IndexedDB database and syncing changes in the background, rather than waiting for network responses.

Key takeaways:
- Linear uses IndexedDB as the local source of truth, syncing changes asynchronously to the server.
- Optimistic updates and minimal loading states make the app feel instant.
- The stack is simple (React, MobX, TypeScript), with a focus on local-first architecture and granular reactivity.
- Many performance gains are achievable in typical apps using libraries like TanStack Query or SWR.

Recommendation:
Read fully (especially for those interested in frontend performance and local-first architectures)

Why it matters:
especially for those interested in frontend performance and local-first architectures

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[TanStack Query]]
