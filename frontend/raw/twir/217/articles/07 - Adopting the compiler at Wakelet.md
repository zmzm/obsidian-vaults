---
type: twir-item
issue: 217
item: 7
item_type: item
date: 2025-01-15
source: https://github.com/reactwg/react-compiler/discussions/52
tags:
  - "Compiler"
  - "Bun"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2025-01-15-TWIR-217|Index]]

# Item 7: Adopting the compiler at Wakelet

Source: [https://github.com/reactwg/react-compiler/discussions/52](https://github.com/reactwg/react-compiler/discussions/52)

Summary:
Wakelet.com rolled out the React Compiler (React Forget) to 100% of users, seeing significant improvements in INP (Interaction to Next Paint) and modest improvements in LCP (Largest Contentful Paint). The migration surfaced some existing bugs but required only minor workarounds. While bundle size increased for some, the performance gains—especially in pure React elements—were substantial, though not a cure-all for all performance issues.

Key takeaways:
- React Compiler improved INP by ~15% and LCP by ~10% in Wakelet's production app.
- Most issues encountered were due to pre-existing code bugs, not the compiler itself.
- Bundle size increases were noted, but perceived as acceptable given the UX improvements.
- Greatest performance gains observed in pure React components.

Recommendation:
Read fully

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
