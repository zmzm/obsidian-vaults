---
type: twir-item
issue: 262
item: 6
item_type: item
date: 2025-12-10
source: https://calendar.perfplanet.com/2025/react-19-2-further-advances-inp-optimization/
tags:
  - "192"
  - "INP"
status: auto
---

[[2025-12-10-TWIR-262|Index]]

# Item 6: React 19.2. Further Advances INP Optimization

Source: [https://calendar.perfplanet.com/2025/react-19-2-further-advances-inp-optimization/](https://calendar.perfplanet.com/2025/react-19-2-further-advances-inp-optimization/)

Summary:
React 19.2 introduces the <Activity> component and new Chrome DevTools Performance Tracks to help developers optimize Interaction to Next Paint (INP). <Activity> enables stateful UI hiding without unmounting or unnecessary re-renders, while Performance Tracks provide granular visibility into React’s scheduling and rendering phases. These features improve performance, state preservation, and debugging for complex React apps.

Key takeaways:
- <Activity> allows hiding UI without losing state or causing unnecessary renders; hidden components are visually removed but retain state.
- Performance Tracks in Chrome DevTools now show React’s scheduler, component, and server activity in a unified timeline.
- Selective hydration and pre-rendering are supported, improving navigation and UI responsiveness.
- SSR omits hidden <Activity> content from HTML, which may impact SEO.

Recommendation: Read fully (for developers interested in advanced React performance optimization)
