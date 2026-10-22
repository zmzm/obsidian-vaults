---
type: twir-item
issue: 295
item: 9
item_type: item
date: 2026-09-02
source: https://sigh.dev/posts/making-react-testing-library-faster/
tags:
  - "43"
status: auto
quality: keep
---

[[2026-09-02-TWIR-295|Index]]

# Item 9: Making React Testing Library Tests 43% Faster

Source: [https://sigh.dev/posts/making-react-testing-library-faster/](https://sigh.dev/posts/making-react-testing-library-faster/)

Summary:
This post details how targeted improvements to jsdom and React Testing Library internals led to a 43% speedup in test execution, especially for large forms and accessibility queries. The author describes the process of profiling, patching, and upstreaming fixes to jsdom, focusing on label indexing, selector matching, and event path optimizations.

Key takeaways:
- Major speedup achieved by caching label lookups, fixing selector fast paths, and optimizing event dispatch in jsdom.
- Improvements benefit test suites with large forms, deep DOM trees, and heavy use of getByRole and userEvent.
- Changes are being upstreamed to jsdom, with some fixes pending release.
- The process relied on profiling, iterative patching, and collaboration with maintainers.

Recommendation:
Read fully (for teams with slow React test suites or interest in testing library internals/performance)

Why it matters:
for teams with slow React test suites or interest in testing library internals/performance

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
