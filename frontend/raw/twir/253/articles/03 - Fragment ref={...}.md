---
type: twir-item
issue: 253
item: 3
item_type: item
date: 2025-10-08
source: https://react.dev/reference/react/Fragment#fragmentinstance
tags:
status: auto
quality: keep
---

[[2025-10-08-TWIR-253|Index]]

# Item 3: <Fragment ref={...}>

Source: [https://react.dev/reference/react/Fragment#fragmentinstance](https://react.dev/reference/react/Fragment#fragmentinstance)

Summary:
React’s <Fragment> component, commonly used as <></>, now supports refs in the Canary channel, exposing a FragmentInstance for DOM interaction. This enables event handling, layout, focus, and observer methods on grouped elements without adding extra DOM nodes. There are caveats regarding usage with keys and refs, especially when using the shorthand syntax.

Key takeaways:
- <Fragment> can now accept refs (Canary only), providing methods for event handling, layout, focus, and observation on its children.
- The shorthand <>...</> cannot be used when passing keys or refs; explicit <Fragment> syntax is required.
- State preservation and reset behaviors are nuanced when switching between Fragment and array or single element renderings.
- Useful for advanced DOM manipulation and accessibility scenarios without extra markup.

Recommendation:
Read fully (if you need advanced DOM interactions with Fragments or are exploring Canary features)

Why it matters:
if you need advanced DOM interactions with Fragments or are exploring Canary features

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
