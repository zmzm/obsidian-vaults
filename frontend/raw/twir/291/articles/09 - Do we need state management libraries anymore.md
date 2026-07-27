---
type: twir-item
issue: 291
item: 9
item_type: item
date: 2026-07-22
source: https://neciudan.dev/do-we-need-state-management-libraries
tags:
status: auto
quality: keep
---

[[2026-07-22-TWIR-291|Index]]

# Item 9: Do we need state management libraries anymore?

Source: [https://neciudan.dev/do-we-need-state-management-libraries](https://neciudan.dev/do-we-need-state-management-libraries)

Summary:
The article questions the necessity of traditional state management libraries (Redux, Zustand, Jotai, etc.) in modern React apps, given advances like useSyncExternalStore and improved patterns for scoping state. It reviews how popular libraries work under the hood, the types of state in typical apps, and how precise state partitioning can reduce or eliminate the need for external libraries. The author argues that, with correct state separation and modern React hooks, most apps can avoid heavyweight state management solutions.

Key takeaways:
- Modern React (with useSyncExternalStore and selectors) can handle most state needs without extra libraries.
- State should be partitioned: UI (local), server (cache), URL (shareable), global (config), and complex shared state.
- Libraries like Redux and Zustand are now built on the same primitives available to all React apps.
- For most apps, careful state design can replace the need for a dedicated state management library.

Recommendation:
Read fully (read fully if architecting state in a new or existing React app)

Why it matters:
read fully if architecting state in a new or existing React app

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
