---
type: twir-item
issue: 262
item: 12
item_type: item
date: 2025-12-10
source: https://shramko.dev/blog/react-elements-children
tags:
  - "Re-Renders"
status: auto
---

[[2025-12-10-TWIR-262|Index]]

# Item 12: React Elements, Children as Props, and Re-Renders

Source: [https://shramko.dev/blog/react-elements-children](https://shramko.dev/blog/react-elements-children)

Summary:
The article explains how passing React elements as children props can prevent unnecessary re-renders in scenarios where state must live at a higher level. By extracting stateful logic into a wrapper component and passing expensive children as props, React can skip reconciling unchanged subtrees, resulting in smoother UI updates. The distinction between components and elements, and how JSX transforms children, is clarified.

Key takeaways:
- Passing elements as children props enables stable references and avoids re-rendering expensive components.
- This pattern is useful when state cannot be moved down but performance is critical.
- React compares element references, not their visual position, for reconciliation.
- Understanding JSX transformation helps apply this optimization flexibly.

Recommendation: Read fully (read fully if optimizing render performance in complex layouts)
