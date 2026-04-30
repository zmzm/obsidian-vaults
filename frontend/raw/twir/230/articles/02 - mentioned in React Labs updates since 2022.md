---
type: twir-item
issue: 230
item: 2
item_type: item
date: 2025-04-16
source: https://react.dev/blog/2022/06/15/react-labs-what-we-have-been-working-on-june-2022#offscreen
tags:
  - "2022"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-04-16-TWIR-230|Index]]

# Item 2: mentioned in React Labs updates since 2022

Source: [https://react.dev/blog/2022/06/15/react-labs-what-we-have-been-working-on-june-2022#offscreen](https://react.dev/blog/2022/06/15/react-labs-what-we-have-been-working-on-june-2022#offscreen)

Summary:
This React Labs update outlines ongoing research and development areas for React, including Server Components, asset loading, static server rendering optimizations, the React Optimizing Compiler ("React Forget"), Offscreen rendering, and transition tracing. The post emphasizes that these are not committed roadmaps but areas of active exploration, with many features still experimental or in flux. Key details include the move toward async/await for Server Components, new asset loading APIs, and the Offscreen API for deprioritizing hidden UI.

Key takeaways:
- Server Components are being refined for bundler compatibility and async/await support; stable release depends on ecosystem alignment.
- Asset loading APIs are in development to improve handling of scripts, styles, and images across environments and with Suspense.
- The React Optimizing Compiler aims to automate memoization and optimize re-renders, with a playground for experimentation.
- Offscreen API will allow React to hide UI while preserving state and reducing unnecessary work, enabling instant transitions and better list virtualization.
- Transition Tracing will improve performance profiling by associating slow renders with specific user interactions.

Recommendation:
Summary sufficient (read the full post if you want deep context on React’s future directions or are building on experimental features)

Why it matters:
read the full post if you want deep context on React’s future directions or are building on experimental features

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
