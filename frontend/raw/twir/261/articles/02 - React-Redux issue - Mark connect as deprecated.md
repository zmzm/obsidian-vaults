---
type: twir-item
issue: 261
item: 2
item_type: item
date: 2025-12-03
source: https://github.com/reduxjs/react-redux/issues/2264
tags:
  - "React-Redux"
  - "Bun"
status: auto
---

[[2025-12-03-TWIR-261|Index]]

# Item 2: React-Redux issue - Mark connect as deprecated

Source: [https://github.com/reduxjs/react-redux/issues/2264](https://github.com/reduxjs/react-redux/issues/2264)

Summary:
The React-Redux team proposes officially marking the connect API as deprecated in favor of useSelector and other modern hooks, as connect will not be updated for upcoming concurrent store APIs. While connect will remain available for now, new code should avoid it due to its larger bundle size, complex TypeScript usage, and lack of future concurrency support. Documentation and release notes will be updated, and a non-deprecated alias may be provided for legacy codebases.

Key takeaways:
- connect will be marked as @deprecated but not removed in the near future.
- Future React-Redux versions will focus on hooks-based APIs compatible with concurrent React.
- connect is less performant and more complex compared to useSelector and modern patterns.
- Developers are strongly encouraged to migrate away from connect.

Recommendation: Summary sufficient (read the issue if you maintain codebases using connect or need migration details)
