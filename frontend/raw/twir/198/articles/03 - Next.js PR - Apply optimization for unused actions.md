---
type: twir-item
issue: 198
item: 3
item_type: item
date: 2024-08-28
source: https://github.com/vercel/next.js/pull/69178
tags:
  - "Nextjs"
  - "PR"
  - "tree-shaking"
status: auto
quality: keep
---

[[2024-08-28-TWIR-198|Index]]

# Item 3: Next.js PR - Apply optimization for unused actions

Source: [https://github.com/vercel/next.js/pull/69178](https://github.com/vercel/next.js/pull/69178)

Summary:
This Next.js PR optimizes server action endpoints by removing unused actions from the generated manifest. Previously, all server actions in a module were exposed as endpoints, potentially leaking unused or unintended actions. The new approach analyzes module usage to include only actions actually referenced, improving security and reducing unnecessary endpoints.

Key takeaways:
- Only used server actions are exposed as endpoints; unused ones are filtered out.
- Reduces accidental exposure of internal logic and tightens security.
- Standard tree-shaking doesn’t apply due to SWC transformation; custom analysis is implemented.
- Indirect unused imports are not dropped due to module graph limitations.

Recommendation:
Read fully

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
