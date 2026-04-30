---
type: twir-item
issue: 217
item: 3
item_type: item
date: 2025-01-15
source: https://github.com/facebook/react/pull/32050
tags:
  - "PR"
status: auto
quality: keep
---

[[2025-01-15-TWIR-217|Index]]

# Item 3: React Core PR - View Transition Class Names based on event kind

Source: [https://github.com/facebook/react/pull/32050](https://github.com/facebook/react/pull/32050)

Summary:
This PR adds five new props to <ViewTransition> that allow developers to specify view-transition-class names based on the type of animation event (enter, exit, layout, update, share). This enables fine-grained control over which transitions are applied and when, including the ability to opt out of transitions for specific subtrees. The "none" value deactivates the view transition name for a given event, improving safety and composability.

Key takeaways:
- New props: enter, exit, layout, update, share, each mapping to a specific transition scenario.
- Developers can now limit transitions to only affected DOM nodes, reducing unwanted animations.
- "none" disables transitions for a given event, allowing for precise control.
- Cannot be fully replicated with just CSS or imperative refs; this approach is unique to the API.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
