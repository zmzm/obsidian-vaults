---
type: twir-item
issue: 245
item: 2
item_type: item
date: 2025-07-30
source: https://github.com/facebook/react/pull/34032
tags:
  - "ReactCore"
  - "PR"
  - "Perf"
status: auto
quality: keep
---

[[2025-07-30-TWIR-245|Index]]

# Item 2: React Core PR - Deprecate "Throw a Promise" technique

Source: [https://github.com/facebook/react/pull/34032](https://github.com/facebook/react/pull/34032)

Summary:
React is deprecating the "throw a Promise" pattern for data fetching and suspense, in favor of the new React.use(promise) API. The old technique had significant drawbacks, including poor debuggability, lack of static analysis, and interference with optimizations like Suspense resume-in-place. The new use() API brings better linting, error handling, and future extensibility, and is enforced by updated ESLint rules.

Key takeaways:
- "Throw a Promise" is being replaced by React.use(promise), which is safer and more predictable.
- The new use() API is enforced by lint rules, especially disallowing its use inside try/catch blocks.
- Deprecation improves performance tooling, debugging, and future React optimizations.
- Existing codebases should plan to migrate to use() for suspenseful data fetching.

Recommendation:
Summary sufficient (read the PR for migration details or if you maintain libraries using suspense)

Why it matters:
read the PR for migration details or if you maintain libraries using suspense

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
