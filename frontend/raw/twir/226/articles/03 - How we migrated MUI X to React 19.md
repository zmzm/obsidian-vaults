---
type: twir-item
issue: 226
item: 4
item_type: item
date: 2025-03-19
source: https://mui.com/blog/react-19-update/
tags:
  - "MUI"
  - "19"
status: auto
quality: keep
---

[[2025-03-19-TWIR-226|Index]]

# Item 4: How we migrated MUI X to React 19

Source: [https://mui.com/blog/react-19-update/](https://mui.com/blog/react-19-update/)

Summary:
MUI X maintainers describe their two-phase migration to React 19: first ensuring compatibility while maintaining React 18 support, then fully upgrading the codebase. They detail handling breaking changes, especially in testing (strict mode, error reporting), and address new ref behavior in React 19 by introducing a forwardRef shim for prop stability. The migration also required updating dependencies, test utilities, and type references to support both React 18 and 19.

Key takeaways:
- Two-phase migration: add React 19 compatibility, then upgrade codebase while supporting React 18.
- Adjustments needed for strict mode, error reporting, and ref handling due to React 19 changes.
- Introduced a forwardRef shim to ensure prop order and type safety across versions.
- Updated test utilities, CI, and type definitions for dual React version support.

Recommendation:
Read fully (if maintaining libraries or supporting multiple React versions)

Why it matters:
if maintaining libraries or supporting multiple React versions

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
