---
type: twir-item
issue: 292
item: 8
item_type: item
date: 2026-07-29
source: https://sergiodxa.com/tutorials/think-in-remix-ui-instead-of-react
tags:
  - "UI"
status: auto
quality: keep
---

[[2026-07-29-TWIR-292|Index]]

# Item 8: How to Think in Remix UI Instead of React

Source: [https://sergiodxa.com/tutorials/think-in-remix-ui-instead-of-react](https://sergiodxa.com/tutorials/think-in-remix-ui-instead-of-react)

Summary:
This tutorial introduces the Remix UI model, where component functions run once to set up state and return a render closure, instead of re-running on every state change as in React. State is managed via local variables and explicit update calls, with context used for shared state. The article walks through building an interactive gallery, illustrating the differences from React's hooks and reactivity.

Key takeaways:
- Remix UI components set up state once and use explicit handle.update() calls to trigger re-renders.
- Local variables replace hooks for state, and context is used for shared state across components.
- The mental model shifts from implicit reactivity to explicit updates and setup-driven logic.
- Encourages thinking in terms of setup and explicit change propagation, rather than automatic reruns.

Recommendation:
Read fully (for developers exploring Remix UI or alternative component paradigms)

Why it matters:
for developers exploring Remix UI or alternative component paradigms

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
