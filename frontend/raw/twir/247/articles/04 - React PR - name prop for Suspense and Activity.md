---
type: twir-item
issue: 247
item: 4
item_type: item
date: 2025-08-27
source: https://github.com/facebook/react/pull/34135
tags:
  - "PR"
status: auto
quality: keep
---

[[2025-08-27-TWIR-247|Index]]

# Item 4: React PR - name prop for <Suspense> and <Activity>

Source: [https://github.com/facebook/react/pull/34135](https://github.com/facebook/react/pull/34135)

Summary:
A React PR adds a name prop to <Suspense> and <Activity> components, making it easier to identify boundaries in the React DevTools and Components Tree View. Both key and name props become searchable, improving debugging and component identification. The change does not infer names from owners and is an exception to the usual minimal-props-in-tree policy.

Key takeaways:
- name prop improves identification of Suspense and Activity boundaries in DevTools.
- Both key and name are now searchable in the Components Tree View.
- Applies to built-in components; custom components are already identified by their names.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
