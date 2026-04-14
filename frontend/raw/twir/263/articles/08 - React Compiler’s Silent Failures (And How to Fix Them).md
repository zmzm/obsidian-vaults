---
type: twir-item
issue: 263
item: 8
item_type: item
date: 2025-12-17
source: https://acusti.ca/blog/2025/12/16/react-compiler-silent-failures-and-how-to-fix-them/
tags:
  - "ReactCompiler"
status: auto
---

[[2025-12-17-TWIR-263|Index]]

# Item 8: React Compiler’s Silent Failures (And How to Fix Them)

Source: [https://acusti.ca/blog/2025/12/16/react-compiler-silent-failures-and-how-to-fix-them/](https://acusti.ca/blog/2025/12/16/react-compiler-silent-failures-and-how-to-fix-them/)

Summary:
The article discusses how React Compiler silently fails to optimize components it cannot handle, potentially leading to unnoticed performance regressions. The author describes discovering an undocumented ESLint rule (react-hooks/todo) that can break the build when compilation fails, ensuring that critical components are actually optimized. Practical configuration advice is provided for integrating this check into your workflow.

Key takeaways:
- React Compiler falls back silently if it cannot compile a component, risking unnoticed performance issues.
- Manual memoization is now largely obsolete, but reliance on the compiler requires confidence in its coverage.
- Enabling the react-hooks/todo ESLint rule surfaces unoptimized components as build errors.
- Proper linting ensures critical components are compiled and optimized as intended.

Recommendation: Read fully

Related notes: [[React Compiler]]
