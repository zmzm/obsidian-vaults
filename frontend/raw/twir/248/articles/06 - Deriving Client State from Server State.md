---
type: twir-item
issue: 248
item: 6
item_type: item
date: 2025-09-03
source: https://tkdodo.eu/blog/deriving-client-state-from-server-state
tags:
status: auto
quality: keep
---

[[2025-09-03-TWIR-248|Index]]

# Item 6: Deriving Client State from Server State

Source: [https://tkdodo.eu/blog/deriving-client-state-from-server-state](https://tkdodo.eu/blog/deriving-client-state-from-server-state)

Summary:
The article advocates for deriving client state directly from server state rather than synchronizing them via effects, using a custom hook as an example. This approach leads to simpler, more declarative code, reduces bugs, and improves UX by ensuring state validity is always based on the latest server data. The pattern is broadly applicable, especially when dealing with selections or defaults that depend on server-fetched data.

Key takeaways:
- Prefer deriving client state from server state instead of syncing via useEffect.
- Reduces imperative code and potential for stale or invalid state.
- Enhances maintainability and flexibility in UI logic.
- Pattern applies to selections, form defaults, and similar scenarios.

Recommendation:
Read fully (read fully for practical code examples or if using state management libraries like Zustand)

Why it matters:
read fully for practical code examples or if using state management libraries like Zustand

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
