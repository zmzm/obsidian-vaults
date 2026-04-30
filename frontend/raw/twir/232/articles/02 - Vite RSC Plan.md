---
type: twir-item
issue: 232
item: 4
item_type: item
date: 2025-04-30
source: https://github.com/hi-ogawa/vite-plugins/issues/748
tags:
  - "Vite"
  - "RSC"
  - "ReactRouter"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-04-30-TWIR-232|Index]]

# Item 4: Vite RSC Plan

Source: [https://github.com/hi-ogawa/vite-plugins/issues/748](https://github.com/hi-ogawa/vite-plugins/issues/748)

Summary:
This issue outlines a plan to improve React Server Components (RSC) support in Vite via a new package, react-server-dom-vite. The goal is to abstract away the complexity of integrating RSC with Vite, making it easier for frameworks and plugins to adopt. The plan includes API alignment with react-server-dom-webpack, minimal plugin implementation, and collaboration with the Vite and React ecosystems.

Key takeaways:
- Seeks to simplify RSC adoption in Vite by hiding async module loading and invalidation logic.
- Aims for compatibility with existing frameworks (Waku, Redwood, Vike, React Router, etc.).
- Some RSC/SSR features will remain userland until Vite adds native support (multi-environment, CSS, transforms).
- Open questions about ESM vs CJS output and official plugin status.

Recommendation:
Read fully (if you work on Vite-based SSR/RSC frameworks or plugins)

Why it matters:
if you work on Vite-based SSR/RSC frameworks or plugins

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
