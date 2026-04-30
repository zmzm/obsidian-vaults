---
type: twir-item
issue: 230
item: 8
item_type: item
date: 2025-04-16
source: https://ondrejvelisek.github.io/avoid-state-synchronization-trap/
tags:
status: auto
quality: keep
---

[[2025-04-16-TWIR-230|Index]]

# Item 8: Avoid the State Synchronization Trap

Source: [https://ondrejvelisek.github.io/avoid-state-synchronization-trap/](https://ondrejvelisek.github.io/avoid-state-synchronization-trap/)

Summary:
This post examines common pitfalls in state management, particularly the challenges of synchronizing related pieces of state (e.g., columns and filters in a data table). It advocates for shaping state to minimize synchronization needs, such as splitting state and recombining it in selectors or render functions. The article walks through a real-world example, showing how direct state synchronization leads to bugs and maintenance headaches.

Key takeaways:
- Synchronizing related state (e.g., columns and filters) leads to bugs and complexity.
- Prefer splitting state and merging it in selectors or hooks, rather than keeping multiple sources in sync.
- State normalization and careful state shape design remain important, even in modern React.
- The pattern applies beyond React, to any frontend framework.

Recommendation:
Read fully (read fully if you struggle with complex state dependencies or want to refactor for maintainability)

Why it matters:
read fully if you struggle with complex state dependencies or want to refactor for maintainability

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
