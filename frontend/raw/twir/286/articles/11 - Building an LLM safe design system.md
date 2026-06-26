---
type: twir-item
issue: 286
item: 11
item_type: item
date: 2026-06-17
source: https://polar.sh/blog/orbit-llm-safe-design-system
tags:
  - "LLM"
  - "StyleX"
status: auto
quality: keep
---

[[2026-06-17-TWIR-286|Index]]

# Item 11: Building an LLM safe design system

Source: [https://polar.sh/blog/orbit-llm-safe-design-system](https://polar.sh/blog/orbit-llm-safe-design-system)

Summary:
Polar’s Orbit design system aims to enforce design consistency in an era of LLM-generated UI code by eliminating raw value-based styling (e.g., Tailwind class strings) in favor of intent-based tokens and strict linting. The system uses a <Box /> primitive with typed props for design tokens, and all rules are enforced via ESLint in CI, not just documentation. This approach reduces drift and ensures that both humans and LLMs can only use approved design decisions.

Key takeaways:
- Raw class strings allow LLMs to introduce subtle, off-brand styling drift.
- Orbit uses intent-based tokens (e.g., background-card) instead of values (e.g., bg-gray-100).
- All design rules are enforced via CI linting, not just style guides or docs.
- StyleX and a <Box /> primitive provide a type-safe, token-driven styling API.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
