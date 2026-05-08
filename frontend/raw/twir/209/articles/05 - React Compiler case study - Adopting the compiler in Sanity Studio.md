---
type: twir-item
issue: 209
item: 5
item_type: item
date: 2024-11-13
source: https://github.com/reactwg/react-compiler/discussions/33
tags:
  - "Compiler"
  - "TS"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2024-11-13-TWIR-209|Index]]

# Item 5: React Compiler case study - Adopting the compiler in Sanity Studio

Source: [https://github.com/reactwg/react-compiler/discussions/33](https://github.com/reactwg/react-compiler/discussions/33)

Summary:
Sanity Studio has been testing the React Compiler to improve performance in its real-time, collaborative content platform. With recent beta support for React 18, several libraries (react-rx, @sanity/ui, @portabletext/editor) are now optimized using the compiler, resulting in significant performance gains and bug detection. The rollout has been smooth, with most issues stemming from code patterns the compiler can't yet optimize, highlighting opportunities for further refactoring and collaboration with the React team.

Key takeaways:
- React Compiler integration led to 20–30% FPS improvements in editing interactions.
- The compiler and its ESLint plugin help uncover both performance bottlenecks and latent bugs.
- Most migration issues are due to unsupported patterns or existing code breaking React rules.
- Incremental adoption is recommended: use the linter, measure impact, refactor, and report issues to the core team.

Recommendation:
Read fully (for teams considering or piloting React Compiler)

Why it matters:
for teams considering or piloting React Compiler

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
