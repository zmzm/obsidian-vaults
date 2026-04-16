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
quality: keep
---

[[2026-01-28-TWIR-266|Index]]

# Item 6: React Aria PR - Add render prop to allow customizing DOM element

Source: [https://github.com/adobe/react-spectrum/pull/9499](https://github.com/adobe/react-spectrum/pull/9499)

Summary:
This PR adds a render prop to React Aria Components, enabling users to customize the rendered DOM element and merge behaviors/styles with custom components. While React Aria has discouraged this due to potential accessibility risks, the new API addresses common use cases like router links, animation libraries, and advanced DOM prop overrides. The implementation includes guardrails to prevent breaking accessibility and development warnings for misuse.

Key takeaways:
- New render prop allows explicit customization of the rendered element in React Aria Components.
- Supports advanced use cases (e.g., router links, animation wrappers, custom DOM props).
- Guardrails ensure correct element type and prop/ref pass-through for accessibility.
- Documentation and warnings help avoid common pitfalls; some edge cases remain tricky.

Recommendation:
Read fully (especially for teams using React Aria or building accessible, customizable component libraries)

Why it matters:
especially for teams using React Aria or building accessible, customizable component libraries

Content:
# Add `render` prop to allow customizing DOM element by devongovett · Pull Request #9499 · adobe/react-spectrum · GitHub

```
# Conflicts:
#	packages/@react-spectrum/s2/src/Menu.tsx
#	packages/react-aria-components/src/Menu.tsx
#	packages/react-aria-components/src/Tabs.tsx
#	packages/react-aria-components/src/TagGroup.tsx
```
