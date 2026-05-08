---
type: twir-item
issue: 193
item: 6
item_type: item
date: 2024-07-24
source: https://reacttraining.com/blog/use-useid-instead-of-hand-making-ids
tags:
  - "useId"
  - "Hand-Making"
  - "IDs"
  - "ES"
status: auto
quality: keep
---

[[2024-07-24-TWIR-193|Index]]

# Item 6: Use useId() Instead Of Hand-Making IDs

Source: [https://reacttraining.com/blog/use-useid-instead-of-hand-making-ids](https://reacttraining.com/blog/use-useid-instead-of-hand-making-ids)

Summary:
This article advocates for using the useId() hook (React 18+) instead of manually generating IDs for accessibility or DOM associations. It explains the pitfalls of hand-made IDs, including uniqueness issues and SSR rehydration bugs, and contrasts useId() with useRef() for direct DOM access. The article also provides guidance for projects not yet on React 18, recommending the Reach auto-id package as a fallback.

Key takeaways:
- useId() ensures unique, hydration-safe IDs for accessibility and DOM associations.
- Hand-made IDs are error-prone and can break in SSR scenarios.
- useRef() is preferable for direct DOM access from JavaScript.
- Reach’s auto-id can be used as a polyfill for non-React 18 projects.

Recommendation:
Read fully (read fully if unfamiliar with useId or SSR pitfalls)

Why it matters:
read fully if unfamiliar with useId or SSR pitfalls

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
