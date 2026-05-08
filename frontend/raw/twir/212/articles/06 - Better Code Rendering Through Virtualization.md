---
type: twir-item
issue: 212
item: 6
item_type: item
date: 2024-12-04
source: https://sentry.engineering/blog/better-code-rendering-through-virtualization
tags:
  - "Virtualization"
status: auto
quality: keep
---

[[2024-12-04-TWIR-212|Index]]

# Item 6: Better Code Rendering Through Virtualization

Source: [https://sentry.engineering/blog/better-code-rendering-through-virtualization](https://sentry.engineering/blog/better-code-rendering-through-virtualization)

Summary:
This post details how Codecov rebuilt its code renderer using virtualization to efficiently handle files with tens of thousands of lines, addressing performance bottlenecks caused by React rendering large lists. By integrating @tanstack/react-virtual and the useWindowVirtualizer hook, the renderer now only mounts visible lines, drastically reducing render blocking time and preventing browser crashes. The article includes implementation details and discusses requirements like maintaining native search and scroll-to-line features.

Key takeaways:
- Rendering large lists in React can cause severe performance issues; virtualization is the recommended solution.
- @tanstack/react-virtual enables efficient rendering by only mounting visible items, preserving UX features like search and scrolling.
- The approach is broadly applicable to any React app displaying large datasets or code files.
- Implementation is straightforward with existing virtualization libraries.

Recommendation:
Read fully (if you deal with large lists or code rendering in React; otherwise, summary is sufficient)

Why it matters:
if you deal with large lists or code rendering in React; otherwise, summary is sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
