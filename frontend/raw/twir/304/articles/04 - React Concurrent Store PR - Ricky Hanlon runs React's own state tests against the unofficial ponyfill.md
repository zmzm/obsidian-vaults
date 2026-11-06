---
type: twir-item
issue: 304
item: 4
item_type: item
date: 2026-11-04
source: https://github.com/thejustinwalsh/react-concurrent-store/pull/27
tags:
  - "PR"
status: auto
quality: keep
---

[[2026-11-04-TWIR-304|Index]]

# Item 4: React Concurrent Store PR - Ricky Hanlon runs React's own state tests against the unofficial ponyfill

Source: [https://github.com/thejustinwalsh/react-concurrent-store/pull/27](https://github.com/thejustinwalsh/react-concurrent-store/pull/27)

Summary:
Ricky Hanlon adapted React's internal state-related tests to run against the unofficial react-concurrent-store ponyfill. The process surfaced several test failures, some expected due to known differences, but others indicating potential concurrency bugs in the ponyfill implementation.

Key takeaways:
- React's state tests were ported to validate the concurrent store ponyfill.
- Some failures are expected (e.g., related to fixups), but others suggest real concurrency issues.
- Failing tests were added to highlight behavioral differences.

Recommendation:
Summary sufficient (unless you are evaluating or contributing to concurrent state libraries)

Why it matters:
unless you are evaluating or contributing to concurrent state libraries

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Python clipper extracted too little content. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
