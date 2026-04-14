---
type: twir-item
issue: 265
item: 5
item_type: item
date: 2026-01-21
source: https://github.com/expo/skills
tags:
  - "ViewTransition"
  - "Navigation"
status: auto
---

[[2026-01-21-TWIR-265|Index]]

# Item 5: View transition types

Source: [https://github.com/expo/skills](https://github.com/expo/skills)

Summary:
The View Transition API now supports specifying transition types, allowing developers to apply different CSS animations based on the nature of the DOM update (e.g., navigating forward, backward, or adding/removing items). The API enables fine-grained control over SPA and MPA transitions, with examples demonstrating how to use types in JavaScript and CSS to orchestrate custom animations for different user actions.

Key takeaways:
- Transition types can be specified in Document.startViewTransition(), enabling context-aware animations.
- CSS pseudo-classes like :active-view-transition-type() allow targeting specific transition types for custom effects.
- The API supports both SPA and MPA scenarios, improving UX consistency during navigation and content updates.
- Developers can modify transition types dynamically and leverage advanced CSS selectors for granular control.

Recommendation: Read fully (for those implementing advanced UI transitions)
