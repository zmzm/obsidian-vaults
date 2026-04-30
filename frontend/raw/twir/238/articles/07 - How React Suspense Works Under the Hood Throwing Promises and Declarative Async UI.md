---
type: twir-item
issue: 238
item: 11
item_type: item
date: 2025-06-11
source: https://www.epicreact.dev/how-react-suspense-works-under-the-hood-throwing-promises-and-declarative-async-ui-plbrh
tags:
  - "UI"
status: auto
quality: keep
---

[[2025-06-11-TWIR-238|Index]]

# Item 11: How React Suspense Works Under the Hood: Throwing Promises and Declarative Async UI

Source: [https://www.epicreact.dev/how-react-suspense-works-under-the-hood-throwing-promises-and-declarative-async-ui-plbrh](https://www.epicreact.dev/how-react-suspense-works-under-the-hood-throwing-promises-and-declarative-async-ui-plbrh)

Summary:
Kent C. Dodds explains how React Suspense enables declarative async UI by "throwing" promises during rendering, which React catches to pause rendering and show fallback UI. The article covers how the use hook (React 19+) works with Suspense, how error boundaries integrate, and provides practical code examples for building Suspense-based data fetchers.

Key takeaways:
- Suspense allows components to declaratively handle loading and error states by catching thrown promises.
- The use hook returns resolved values or throws pending promises, integrating seamlessly with Suspense.
- Error boundaries handle rejected promises, providing a unified error handling mechanism.
- The pattern simplifies async UI code by removing manual state management for loading/errors.

Recommendation:
Read fully (for anyone building modern async UIs in React or adopting Suspense)

Why it matters:
for anyone building modern async UIs in React or adopting Suspense

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
