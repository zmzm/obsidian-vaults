---
type: twir-item
issue: 261
item: 7
item_type: item
date: 2025-12-03
source: https://www.epicreact.dev/use-react-view-transition-to-smoothly-transition-images-and-titles-lu6ks
tags:
  - "ViewTransition"
status: auto
---

[[2025-12-03-TWIR-261|Index]]

# Item 7: Use React <ViewTransition /> to Smoothly Transition Images and Titles

Source: [https://www.epicreact.dev/use-react-view-transition-to-smoothly-transition-images-and-titles-lu6ks](https://www.epicreact.dev/use-react-view-transition-to-smoothly-transition-images-and-titles-lu6ks)

Summary:
Kent C. Dodds introduces React 19’s <ViewTransition> component, which leverages the platform View Transition API to animate elements across page transitions. By wrapping elements with the same name prop, React automatically animates them between routes, supporting multiple elements and custom CSS transitions. The article covers usage patterns, naming requirements, and integration with routers and transitions.

Key takeaways:
- <ViewTransition> enables native, smooth transitions between matching elements on navigation.
- Requires unique name props per element instance.
- Works seamlessly with routers and startTransition.
- Customizable via CSS for advanced animations.

Recommendation: Read fully (for teams seeking polished navigation and page transitions)
