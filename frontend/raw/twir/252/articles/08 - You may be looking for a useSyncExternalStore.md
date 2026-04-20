---
type: twir-item
issue: 252
item: 8
item_type: item
date: 2025-10-01
source: https://swizec.com/blog/you-may-be-looking-for-a-useSyncExternalStore/
tags:
  - "useSyncExternalStore"
status: auto
quality: keep
---

[[2025-10-01-TWIR-252|Index]]

# Item 8: You may be looking for a useSyncExternalStore

Source: [https://swizec.com/blog/you-may-be-looking-for-a-useSyncExternalStore/](https://swizec.com/blog/you-may-be-looking-for-a-useSyncExternalStore/)

Summary:
The article highlights a common pattern where useEffect and useState are used to subscribe to external sources, which can cause hydration jank and multiple renders in SSR scenarios. It recommends replacing this pattern with useSyncExternalStore, which provides a cleaner API, better SSR compatibility, and reduces jank by synchronizing external state more efficiently.

Key takeaways:
- useSyncExternalStore is preferable for subscribing to external sources, especially in SSR/hydration contexts.
- The pattern reduces unnecessary renders and improves user-perceived performance.
- The API separates subscription, value retrieval, and server-side defaults for clarity.
- Adopting this hook can lead to more robust and less janky React apps.

Recommendation:
Read fully (read fully if you manage subscriptions to external sources or want to optimize SSR hydration)

Why it matters:
read fully if you manage subscriptions to external sources or want to optimize SSR hydration

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
