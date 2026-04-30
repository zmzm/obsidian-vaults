---
type: twir-item
issue: 229
item: 9
item_type: item
date: 2025-04-09
source: https://cekrem.github.io/posts/react-memo-when-it-helps-when-it-hurts
tags:
  - "Reactmemo"
status: auto
quality: keep
---

[[2025-04-09-TWIR-229|Index]]

# Item 9: React.memo Demystified: When It Helps and When It Hurts

Source: [https://cekrem.github.io/posts/react-memo-when-it-helps-when-it-hurts](https://cekrem.github.io/posts/react-memo-when-it-helps-when-it-hurts)

Summary:
This post clarifies how React.memo, useMemo, and useCallback work, highlighting common misconceptions and pitfalls. It explains that memoization only prevents re-renders in specific scenarios and can introduce complexity or subtle bugs if misapplied, especially with props spreading and children.

Key takeaways:
- React.memo only prevents re-renders if props are stable (by reference); useMemo/useCallback help maintain reference stability.
- Memoizing props does not prevent child re-renders unless the child is wrapped in React.memo.
- Spreading props or passing non-memoized children can break memoization.
- Overusing memoization can add unnecessary complexity; profiling is essential.

Recommendation:
Read fully (for anyone using or considering React.memo and memoization hooks)

Why it matters:
for anyone using or considering React.memo and memoization hooks

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
