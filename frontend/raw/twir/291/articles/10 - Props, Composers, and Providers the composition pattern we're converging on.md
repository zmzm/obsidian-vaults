---
type: twir-item
issue: 291
item: 10
item_type: item
date: 2026-07-22
source: https://backstage.orus.eu/react-composition-patterns-at-orus
tags:
status: auto
quality: keep
---

[[2026-07-22-TWIR-291|Index]]

# Item 10: Props, Composers, and Providers: the composition pattern we're converging on

Source: [https://backstage.orus.eu/react-composition-patterns-at-orus](https://backstage.orus.eu/react-composition-patterns-at-orus)

Summary:
This article outlines a compositional "ladder" for React components, progressing from plain props to compound components, composers/providers, and lifted state. The approach encourages starting with the simplest pattern and only introducing more abstraction when real pain points arise. Practical examples show how to evolve components from prop-based to slot-based APIs, and when to introduce context and providers for data or state sharing.

Key takeaways:
- Start with plain props; only add complexity (compound components, context, providers) when justified by requirements.
- Compound components and slots help manage prop bloat and increase flexibility.
- Context should be kept as an internal detail unless state must cross boundaries or be shared.
- Abstraction should be earned, not preemptively introduced.

Recommendation:
Read fully (read fully if designing component APIs or refactoring a large React codebase)

Why it matters:
read fully if designing component APIs or refactoring a large React codebase

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
