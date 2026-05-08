---
type: twir-item
issue: 195
item: 3
item_type: item
date: 2024-08-07
source: https://yongseok.me/blog/en/react_compiler_1/
tags:
  - "Compiler"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2024-08-07-TWIR-195|Index]]

# Item 3: React Compiler, How Does It Work?

Source: [https://yongseok.me/blog/en/react_compiler_1/](https://yongseok.me/blog/en/react_compiler_1/)

Summary:
This article offers a deep dive into the newly open-sourced React Compiler (formerly React-Forget), focusing on its Babel plugin integration and compilation process. It explains how the compiler traverses AST nodes, skips class-based constructs, and applies memoization to function components. The post provides annotated code samples and sets the stage for further exploration of the compiler's internals and future direction.

Key takeaways:
- React Compiler automates optimal memoization for React code via Babel.
- Compilation is skipped if files use directives like "use no forget" or "use no memo".
- Class components are skipped due to unsafe references to this; focus is on function components.
- The article is part one of a series, promising deeper analysis in future posts.

Recommendation:
Read fully (for those interested in React internals, compiler design, or performance optimization)

Why it matters:
for those interested in React internals, compiler design, or performance optimization

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
