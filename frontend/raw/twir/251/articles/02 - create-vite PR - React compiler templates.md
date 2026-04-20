---
type: twir-item
issue: 251
item: 2
item_type: item
date: 2025-09-24
source: https://github.com/vitejs/vite/pull/20704
tags:
  - "Vite"
  - "PR"
  - "ESLint"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2025-09-24-TWIR-251|Index]]

# Item 2: create-vite PR - React compiler templates

Source: [https://github.com/vitejs/vite/pull/20704](https://github.com/vitejs/vite/pull/20704)

Summary:
A Vite pull request discusses integrating React compiler templates and related tooling, including updates to eslint-plugin-react-hooks to bundle the compiler and its dependencies. The conversation covers dependency management, ESM migration, and the implications of bundling the compiler with the ESLint plugin. Concerns are raised about increased dependencies, install size, and the modern approach to custom parsers in ESLint.

Key takeaways:
- React compiler is being integrated into Vite templates, with related ESLint plugin changes.
- Bundling the compiler with eslint-plugin-react-hooks introduces new dependencies (e.g., zod, hermes-parser).
- Discussion about ESM support and dependency inlining for better efficiency and security.
- Modern ESLint practices suggest decoupling parsing from lint rules.

Recommendation:
Summary sufficient (read PR for deep involvement in Vite/React template tooling or ESLint plugin development)

Why it matters:
read PR for deep involvement in Vite/React template tooling or ESLint plugin development

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
