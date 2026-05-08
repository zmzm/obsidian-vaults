---
type: twir-item
issue: 209
item: 2
item_type: item
date: 2024-11-13
source: https://github.com/facebook/react/pull/31452
tags:
  - "PR"
  - "TS"
status: auto
quality: keep
---

[[2024-11-13-TWIR-209|Index]]

# Item 2: React PR - Make prerendering always non-blocking

Source: [https://github.com/facebook/react/pull/31452](https://github.com/facebook/react/pull/31452)

Summary:
This pull request addresses issues with React's prerendering, ensuring it is always non-blocking, especially when synchronous updates suspend rendering. Previously, certain internal apps experienced infinite render loops due to external store state updates during render, particularly with libraries like Recoil. The fix ensures that when prerendering siblings after a sync update suspends, React switches from a synchronous to a concurrent work loop, enabling time slicing and preventing crashes. Additional unit tests are being added to cover these scenarios.

Key takeaways:
- Fixes infinite render loops caused by useSyncExternalStore during render phase updates.
- Ensures prerendering is always non-blocking, improving reliability for apps using Suspense and external stores.
- Switches to concurrent rendering when needed, enabling time slicing for better performance.
- The fix has been tested on local reproductions and will be covered by new unit tests.

Recommendation:
Read fully (for those maintaining or debugging React internals or external store integrations)

Why it matters:
for those maintaining or debugging React internals or external store integrations

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
