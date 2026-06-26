---
type: twir-item
issue: 286
item: 10
item_type: item
date: 2026-06-17
source: https://www.jayfreestone.com/writing/module-level-dependency-injection-react/
tags:
  - "TanStack"
status: auto
quality: keep
---

[[2026-06-17-TWIR-286|Index]]

# Item 10: Module System Dependency Injection in React & Friends

Source: [https://www.jayfreestone.com/writing/module-level-dependency-injection-react/](https://www.jayfreestone.com/writing/module-level-dependency-injection-react/)

Summary:
The article explores dependency injection (DI) patterns in React, especially in meta-frameworks like TanStack Start and Next.js. It discusses static, runtime, and compile-time DI, focusing on using Node.js module system features (conditional exports, subpath imports) for compile-time DI. While this approach can optimize bundles and enforce global dependencies, it limits testability and flexibility compared to context-based or runtime DI.

Key takeaways:
- React meta-frameworks often lack clean DI entry points outside component trees.
- Compile-time DI via module system (e.g., conditional exports) enables global dependency swapping.
- This approach can reduce bundle size but hinders inline overrides and testability.
- Turbopack requires extra configuration to support Node-style import conditions.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
