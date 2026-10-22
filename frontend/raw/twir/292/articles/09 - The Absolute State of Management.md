---
type: twir-item
issue: 292
item: 9
item_type: item
date: 2026-07-29
source: https://infrequently.org/2026/07/state-management/
tags:
status: auto
quality: keep
---

[[2026-07-29-TWIR-292|Index]]

# Item 9: The Absolute State of Management

Source: [https://infrequently.org/2026/07/state-management/](https://infrequently.org/2026/07/state-management/)

Summary:
This essay critiques the term "state management" in the React ecosystem, arguing that most libraries (including React) only propagate state changes rather than truly managing state over time. It distinguishes between propagation tools and real state management systems, which require time and order semantics (e.g., vector clocks, CRDTs) to handle offline and collaborative scenarios. The article calls for more precise language and adoption of time-aware state management patterns.

Key takeaways:
- Most "state management" libraries in React only propagate or encapsulate state, lacking true management semantics.
- Real state management involves handling time, order, and conflict resolution (e.g., via CRDTs or vector clocks).
- The confusion leads to architectural complexity and misapplied abstractions in large apps.
- Encourages adoption of time-aware systems for collaborative and offline use cases.

Recommendation:
Read fully (for architects and teams rethinking state management strategies)

Why it matters:
for architects and teams rethinking state management strategies

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
