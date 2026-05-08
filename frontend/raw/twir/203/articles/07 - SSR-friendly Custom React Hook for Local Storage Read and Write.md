---
type: twir-item
issue: 203
item: 7
item_type: item
date: 2024-10-01
source: https://www.nico.fyi/blog/ssr-friendly-local-storage-react-custom-hook
tags:
  - "SSR-friendly"
status: auto
quality: keep
---

[[2024-10-01-TWIR-203|Index]]

# Item 7: SSR-friendly Custom React Hook for Local Storage Read and Write

Source: [https://www.nico.fyi/blog/ssr-friendly-local-storage-react-custom-hook](https://www.nico.fyi/blog/ssr-friendly-local-storage-react-custom-hook)

Summary:
The author builds a custom useLocalStorage hook using useSyncExternalStore for SSR compatibility. They discover that the "storage" event only fires on other documents, not the one making the change, so a custom event is needed to update the hook’s state after local changes. The final hook listens to both the native and custom events, ensuring correct reactivity and avoiding hydration mismatches.

Key takeaways:
- useSyncExternalStore is suitable for SSR-friendly local storage hooks.
- The "storage" event does not fire on the same document that changes localStorage.
- A custom event must be dispatched and listened for local updates.
- The hook avoids hydration mismatches by providing a server snapshot.

Recommendation:
Read fully (read fully if implementing or troubleshooting SSR/localStorage hooks)

Why it matters:
read fully if implementing or troubleshooting SSR/localStorage hooks

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
