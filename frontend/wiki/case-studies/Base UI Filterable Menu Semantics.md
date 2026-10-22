---
type: case-study
status: active
updated: 2026-10-22
tags: [base-ui, accessibility, menu, component-api]
---

# Base UI Filterable Menu Semantics

Base UI designed command filtering as a dialog containing a search field and a menu after comparing the expectations conveyed by combobox and autocomplete semantics.

## Context

- Filtering actions differs from choosing a value: selecting Duplicate executes a command instead of completing the text field.
- The extracted account rejects combobox and aria-autocomplete for this interaction because their completion and popup expectations do not match the behavior.
- The dialog announces a context containing more than the menu. The search field filters commands while the actions retain menu semantics.
- Keyboard editing, highlighted-item navigation, submenus, Escape behavior, and screen-reader discovery must work together; a matching visual appearance does not establish equivalent accessibility.

## Why It Matters

- Choose roles from user expectations and actual behavior, then verify keyboard and assistive-technology interactions.
- This is evidence for this particular command-filtering design, not a rule that all searchable popups should become dialogs.

## Related Pages

- [[../patterns/Resilient React Components|Resilient React Components]]
- [[../patterns/Component Confidence Boundaries|Component Confidence Boundaries]]
- [[../sources/Dropdown Component API|Dropdown Component API]]
- [[../sources/AI-Generated UI Accessibility|AI-Generated UI Accessibility]]

## Sources

- [[../../raw/twir/302/articles/07 - Building a filterable menu that works for everyone|07 - Building a filterable menu that works for everyone]]

## Open Questions

- How does query editing interact with submenu entry and return?
- Which automated interaction assertions need manual screen-reader verification?
