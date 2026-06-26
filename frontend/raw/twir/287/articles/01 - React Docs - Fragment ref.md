---
type: twir-item
issue: 287
item: 1
item_type: featured
date: 2026-06-24
source: https://react.dev/reference/react/Fragment
tags:
  - "Fragmentref"
status: auto
quality: keep
---

[[2026-06-24-TWIR-287|Index]]

# Item 1: React Docs - <Fragment ref>

Source: [https://react.dev/reference/react/Fragment](https://react.dev/reference/react/Fragment)

Summary:
The React documentation for <Fragment> has been updated, including details about the new canary-only ref support. Fragments allow grouping elements without adding extra nodes to the DOM, and now, with the canary release, you can attach refs to Fragments to manage focus, events, and visibility across their children. The docs cover usage patterns, caveats, and the API for the new FragmentInstance, which provides imperative methods for interacting with grouped elements.

Key takeaways:
- Fragments group elements without extra DOM nodes; <>...</> is shorthand for <Fragment></Fragment>.
- Only the explicit <Fragment> syntax (not <>) supports key and (in canary) ref props.
- Canary-only: Passing a ref to a Fragment gives access to a FragmentInstance with methods for event handling, focus management, scrolling, and observation.
- State is not reset when toggling between Fragment and array/element at a single level, but deeper changes do reset state.

Recommendation:
Read fully

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
