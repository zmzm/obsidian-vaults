---
type: twir-item
issue: 266
item: 6
item_type: item
date: 2026-01-28
source: https://github.com/adobe/react-spectrum/pull/9499
tags:
  - "ReactAria"
  - "PR"
  - "DOM"
status: auto
---

[[2026-01-28-TWIR-266|Index]]

# Item 6: React Aria PR – Add render prop to allow customizing DOM element

Source: [https://github.com/adobe/react-spectrum/pull/9499](https://github.com/adobe/react-spectrum/pull/9499)

Summary:
This PR adds a render prop to React Aria Components, enabling developers to customize the rendered DOM element and merge behaviors/styles with custom components. The feature is designed with guardrails to prevent breaking accessibility or behavior, such as requiring the correct element type and passing through props and refs. The PR addresses common use cases (router links, animation libraries, overriding DOM props) and provides detailed documentation and examples for correct usage.

Key takeaways:
- Introduces a render prop for customizing DOM elements in React Aria Components.
- Guardrails enforce correct element type, single root element, and prop/ref passthrough.
- Addresses integration with routers, animation libraries, and advanced DOM prop overrides.
- Documentation and dev warnings help prevent accessibility regressions.

Recommendation: Read fully (important for teams using React Aria Components or building accessible, customizable UI libraries)
