---
type: twir-item
issue: 287
item: 3
item_type: item
date: 2026-06-24
source: https://www.skovhus.dev/blog/moving-linear-from-styled-components-to-stylex
tags:
  - "StyleX"
status: auto
quality: keep
---

[[2026-06-24-TWIR-287|Index]]

# Item 3: Moving Linear from styled‑components to StyleX

Source: [https://www.skovhus.dev/blog/moving-linear-from-styled-components-to-stylex](https://www.skovhus.dev/blog/moving-linear-from-styled-components-to-stylex)

Summary:
Linear migrated from styled-components to StyleX to improve performance and enforce stricter styling contracts. The migration was prompted by styled-components entering maintenance mode and not adopting React’s useInsertionEffect, leading to performance issues. The team developed a codemod and agent-assisted workflow to incrementally migrate components, focusing on minimizing runtime, encapsulating styles, and maintaining a healthy developer experience.

Key takeaways:
- StyleX offers build-time style generation, deterministic resolution, and strong encapsulation, but restricts some flexible CSS patterns.
- Migration required defining a new styling foundation, incremental adoption, aggressive linting, and escape hatches via CSS Modules.
- Agent-assisted codemods automated much of the migration, but manual intervention was needed for complex cases.
- The process improved maintainability and performance, but required significant upfront investment.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
