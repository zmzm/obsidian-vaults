---
type: twir-item
issue: 274
item: 8
item_type: item
date: 2026-03-25
source: https://tkdodo.eu/blog/test-ids-are-an-a11y-smell
tags:
  - "IDs"
  - "a11y"
status: auto
---

[[2026-03-25-TWIR-274|Index]]

# Item 8: Test IDs are an a11y smell

Source: [https://tkdodo.eu/blog/test-ids-are-an-a11y-smell](https://tkdodo.eu/blog/test-ids-are-an-a11y-smell)

Summary:
Relying on `data-testid` attributes for testing is discouraged in favor of role-based selectors, which promote accessibility and more robust, user-centric tests. Role-based selectors ensure your tests reflect real user interactions and help catch accessibility issues early.

Key takeaways:
- `data-testid` selectors can mask accessibility problems and are not user-centric.
- Role-based selectors (e.g., getByRole) align tests with actual user interactions and accessibility standards.
- Using semantic HTML and accessible naming improves both testability and user experience.
- If you can’t select an element by role, your markup likely needs improvement.

Recommendation: Read fully
