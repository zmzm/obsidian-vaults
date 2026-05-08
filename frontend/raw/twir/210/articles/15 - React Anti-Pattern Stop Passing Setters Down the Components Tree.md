---
type: twir-item
issue: 210
item: 15
item_type: item
date: 2024-11-20
source: https://matanbobi.dev/posts/stop-passing-setter-functions-to-components
tags:
  - "Anti-Pattern"
status: auto
quality: keep
---

[[2024-11-20-TWIR-210|Index]]

# Item 15: React Anti-Pattern: Stop Passing Setters Down the Components Tree

Source: [https://matanbobi.dev/posts/stop-passing-setter-functions-to-components](https://matanbobi.dev/posts/stop-passing-setter-functions-to-components)

Summary:
The article highlights the anti-pattern of passing useState setter functions as props, which causes abstraction leaks and tightly couples child components to parent implementation details. It demonstrates how this pattern leads to fragility and reduced reusability, especially when switching to useReducer or changing state shape. The recommended solution is to pass encapsulated callback functions instead, improving maintainability and clarity.

Key takeaways:
- Passing setter functions as props couples children to parent state management.
- Leads to abstraction leaks and maintenance headaches during refactors.
- Prefer passing intent-based callbacks (e.g., onChange) over raw setters.
- Enhances component reusability and decouples implementation details.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
