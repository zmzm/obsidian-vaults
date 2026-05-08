---
type: twir-item
issue: 210
item: 8
item_type: item
date: 2024-11-20
source: https://www.nico.fyi/blog/be-careful-with-usesyncexternalstore
tags:
  - "useSyncExternalStore"
  - "IDE"
status: auto
quality: keep
---

[[2024-11-20-TWIR-210|Index]]

# Item 8: Be careful with useSyncExternalStore

Source: [https://www.nico.fyi/blog/be-careful-with-usesyncexternalstore](https://www.nico.fyi/blog/be-careful-with-usesyncexternalstore)

Summary:
The article explores a subtle pitfall when using useSyncExternalStore with non-primitive values, such as objects, which can cause infinite render loops due to reference instability. The author demonstrates the issue and provides a robust solution: serialize data for storage and use stable references, employing a wrapper object and superjson for parsing. The hook also distinguishes between cleared and initial states, and supports legacy data migration.

Key takeaways:
- useSyncExternalStore compares values with Object.is, causing issues with new object references.
- Infinite loops can occur if getSnapshot returns a new object each time.
- Solution: serialize stored values, use stable references, and wrap for state differentiation.
- Includes migration support for legacy localStorage data.

Recommendation:
Read fully (if implementing custom hooks with useSyncExternalStore or localStorage)

Why it matters:
if implementing custom hooks with useSyncExternalStore or localStorage

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
