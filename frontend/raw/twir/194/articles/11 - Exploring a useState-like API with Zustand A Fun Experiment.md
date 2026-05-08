---
type: twir-item
issue: 194
item: 11
item_type: item
date: 2024-07-31
source: https://www.smallrecipesfordisaster.com/posts/dispatch-zustand
tags:
  - "Zustand"
  - "API"
  - "PPR"
status: auto
quality: keep
---

[[2024-07-31-TWIR-194|Index]]

# Item 11: Exploring a useState-like API with Zustand: A Fun Experiment

Source: [https://www.smallrecipesfordisaster.com/posts/dispatch-zustand](https://www.smallrecipesfordisaster.com/posts/dispatch-zustand)

Summary:
The author experiments with making Zustand's API resemble useState, enabling destructured [value, setValue] patterns for store properties. The article details implementation strategies for functional updates and reducing boilerplate, culminating in a factory for generating such stores.

Key takeaways:
- Zustand selectors allow fine-grained subscriptions, but the default API differs from useState.
- The experiment creates a tuple-based API ([value, setValue]) for each store property.
- Functional updates (prev => next) are supported in the custom dispatchers.
- The approach reduces boilerplate and makes Zustand usage more ergonomic for those familiar with useState.

Recommendation:
Summary sufficient (unless you want to replicate or adapt the pattern)

Why it matters:
unless you want to replicate or adapt the pattern

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
