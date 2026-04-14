---
type: twir-item
issue: 271
item: 7
item_type: item
date: 2026-03-04
source: https://react.dev/reference/react/ViewTransition#animating-enter-exit-with-activity
tags:
  - "Activity"
  - "ViewTransition"
status: auto
---

[[2026-03-04-TWIR-271|Index]]

# Item 7: <ViewTransition> docs - New example - Animating enter/exit with Activity

Source: [https://react.dev/reference/react/ViewTransition#animating-enter-exit-with-activity](https://react.dev/reference/react/ViewTransition#animating-enter-exit-with-activity)

Summary:
The <ViewTransition> API, available in React Canary/Experimental, enables smooth animations for component tree transitions, including enter/exit, shared elements, and list reordering. The documentation details how React coordinates these animations, lifecycle hooks involved, and caveats for usage. The new example demonstrates animating enter/exit transitions with the <Activity> component.

Key takeaways:
- <ViewTransition> provides a declarative way to animate complex UI changes in React.
- Integrates with Suspense, Transitions, and the new <Activity> component for seamless UX.
- React manages animation triggers, batching, and lifecycle coordination internally.
- Currently DOM-only, with plans for React Native support.

Recommendation: Summary sufficient (read docs for implementation specifics)
