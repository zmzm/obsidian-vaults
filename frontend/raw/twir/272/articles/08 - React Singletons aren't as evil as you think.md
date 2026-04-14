---
type: twir-item
issue: 272
item: 8
item_type: item
date: 2026-03-11
source: https://dev.to/link2twenty/react-singletons-arent-as-evil-as-you-think-44m8
tags:
  - "TypeScript"
status: auto
---

[[2026-03-11-TWIR-272|Index]]

# Item 8: React: Singletons aren't as evil as you think

Source: [https://dev.to/link2twenty/react-singletons-arent-as-evil-as-you-think-44m8](https://dev.to/link2twenty/react-singletons-arent-as-evil-as-you-think-44m8)

Summary:
The article challenges the negative perception of singletons in React, arguing that they can be a powerful and lightweight solution for global state when implemented correctly. It demonstrates how to synchronize singleton state with React components using event listeners and shows how to build a type-safe, event-driven singleton class (e.g., a toast manager) using native JavaScript features. The post emphasizes leveraging native classes and event systems for robust, testable singleton patterns.

Key takeaways:
- Singletons can be cleanly integrated with React using event-driven patterns.
- Extending native classes (like EventTarget) enables type-safe, scalable singleton implementations.
- Properly designed singletons can decouple global state from component trees without extra libraries.
- Includes practical TypeScript examples for building a notification system.

Recommendation: Read fully (read fully for implementation details or if considering singletons for global state)
