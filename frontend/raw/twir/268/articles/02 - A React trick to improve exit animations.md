---
type: twir-item
issue: 268
item: 2
item_type: item
date: 2026-02-11
source: https://barvian.me/react-exit-animations
tags:
status: auto
---

[[2026-02-11-TWIR-268|Index]]

# Item 2: A React trick to improve exit animations

Source: [https://barvian.me/react-exit-animations](https://barvian.me/react-exit-animations)

Summary:
The author describes a common UX issue where React components update their contents during exit animations, causing distracting UI changes. They explore several workarounds and ultimately leverage React Suspense to "freeze" the exiting component’s DOM, preventing updates during the animation. A custom Freeze component is implemented, using Suspense and React.useInsertionEffect to keep the DOM visible and unchanged while frozen. The solution works well with libraries like React Aria Components, but is acknowledged as a hack that may not be future-proof.

Key takeaways:
- Exit animations can be disrupted by React updates to the exiting component’s content.
- Wrapping the component in a custom Freeze (built on Suspense) prevents DOM updates during exit, improving animation smoothness.
- The approach is clever but relies on internal React behavior and may break in future versions.
- Works best with state-driven UI libraries; not a replacement for official support.

Recommendation: Read fully (if you implement custom animations or care about UX polish)
