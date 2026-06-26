---
type: twir-item
issue: 285
item: 3
item_type: item
date: 2026-06-10
source: https://github.com/reactjs/rfcs/pull/278
tags:
  - "RFC"
status: auto
quality: keep
---

[[2026-06-10-TWIR-285|Index]]

# Item 3: React RFC - Support using disposable as useEffect cleanup

Source: [https://github.com/reactjs/rfcs/pull/278](https://github.com/reactjs/rfcs/pull/278)

Summary:
This RFC proposes allowing useEffect and useLayoutEffect to return a disposable object (with a [Symbol.dispose] method) as their cleanup function, instead of just a callback. This would align React with upcoming JavaScript language features around resource disposal and could improve integration with APIs that use disposables.

Key takeaways:
- Proposal to support returning a disposable object from effect hooks as cleanup.
- Would enable better integration with future JavaScript resource management patterns.
- Example provided using [Symbol.dispose] for cleanup logic.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
