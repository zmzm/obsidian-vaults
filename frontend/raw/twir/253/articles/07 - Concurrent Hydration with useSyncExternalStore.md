---
type: twir-item
issue: 253
item: 7
item_type: item
date: 2025-10-08
source: https://kurtextrem.de/posts/react-uses-hydration
tags:
  - "useSyncExternalStore"
status: auto
quality: keep
---

[[2025-10-08-TWIR-253|Index]]

# Item 7: Concurrent Hydration with useSyncExternalStore

Source: [https://kurtextrem.de/posts/react-uses-hydration](https://kurtextrem.de/posts/react-uses-hydration)

Summary:
This article explores how to avoid hydration mismatches in SSR React apps using useSyncExternalStore, especially in combination with Suspense. It highlights pitfalls of synchronous hydration (like UI flashes and blocking renders) and proposes a concurrent pattern using useDeferredValue to improve UX and performance. The post provides code examples and discusses the trade-offs of different hydration strategies.

Key takeaways:
- useSyncExternalStore’s third parameter allows for correct SSR/client hydration state, avoiding mismatches.
- Synchronous hydration can cause UI flashes, hydration errors, and poor INP (Interaction to Next Paint) scores.
- Combining useSyncExternalStore with useDeferredValue enables concurrent hydration, reducing blocking and improving user experience.
- The approach is relevant for apps using SSR, Suspense, and external stores.

Recommendation:
Read fully (for SSR apps, advanced hydration, or performance tuning)

Why it matters:
for SSR apps, advanced hydration, or performance tuning

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
