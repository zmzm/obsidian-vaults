---
type: twir-item
issue: 262
item: 13
item_type: item
date: 2025-12-10
source: https://certificates.dev/blog/controlled-vs-uncontrolled-components-in-react
tags:
status: auto
---

[[2025-12-10-TWIR-262|Index]]

# Item 13: Controlled vs Uncontrolled Components in React

Source: [https://certificates.dev/blog/controlled-vs-uncontrolled-components-in-react](https://certificates.dev/blog/controlled-vs-uncontrolled-components-in-react)

Summary:
This article demystifies the concepts of controlled and uncontrolled components in React, both for form inputs and general component patterns. It explains that the distinction centers on state ownership—whether the parent or the component manages the state. Examples illustrate how to implement both patterns and how to support flexible usage in custom components.

Key takeaways:
- Controlled components receive state via props; uncontrolled components manage their own state.
- For forms, controlled inputs use value/onChange; uncontrolled use defaultValue and DOM state.
- The same pattern applies to custom components, not just inputs.
- Components can support both modes by checking for prop presence.

Recommendation: Read fully (read fully for onboarding or clarifying team understanding)
