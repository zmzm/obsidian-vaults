---
name: fe-accessibility
description: Web accessibility (a11y). Use for ARIA, keyboard nav, WCAG compliance.
triggers:

  keywords: ['aria-', 'role=', 'tabIndex', 'onKeyDown', 'focus', 'axe', 'a11y']
---

# Frontend Accessibility Skill

## When to use this knowledge

Use this skill when you are:

- Implementing keyboard navigation for interactive elements
- Adding screen reader support with ARIA labels
- Ensuring WCAG AA compliance for color contrast and accessibility
- Creating accessible forms with proper labels and validation
- Managing focus states and focus indicators
- Testing components with screen readers or accessibility tools

## When not to use this knowledge

- Tasks owned more directly by a neighboring skill
- Pure exploration or lookup work without implementation decisions

## What this skill covers

This skill provides guidance for:

- Semantic HTML patterns and ARIA usage
- Keyboard navigation patterns and focus management
- Accessible form design and validation
- WCAG compliance requirements and testing
- Screen reader support and live regions
- Color contrast and visual accessibility

## Knowledge map

Always start here, then follow references as needed:

- Core Principles → `references/core-principles.md`
- Keyboard Navigation → `references/keyboard-navigation.md`
- Forms → `references/forms.md`
- ARIA Patterns → `references/aria-patterns.md`
- Focus Management → `references/focus-management.md`
- Testing → `references/testing.md`

## Fast decision hints

- If the task is mainly about Implementing keyboard navigation for interactive elements, start with this skill.
- If the task also involves Adding screen reader support with ARIA labels, follow the most relevant reference page.
- If the work drifts into Ensuring WCAG AA compliance for color contrast and accessibility, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Prefer documented patterns over ad-hoc solutions
- `<default>` Default: Avoid listed anti-patterns unless explicitly justified
- `<heuristic>` Heuristic: If multiple references apply, compare them explicitly
- `<exception>` Exception: If deviating from the guidelines, clearly explain why and what is being violated

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **its own domain scope**.

This skill is the **canonical source** for all accessibility-related patterns.

| Task                             | Use This Skill | Cross-Referenced From |
| -------------------------------- | -------------- | --------------------- |
| ARIA patterns and usage          | ✅             |                       |
| Keyboard navigation              | ✅             |                       |
| Focus management                 | ✅             |                       |
| Accessible forms                 | ✅             | `fe-ui/forms.md`      |
| Accessibility testing (jest-axe) | ✅             | `fe-testing`          |
| WCAG compliance                  | ✅             |                       |

**Note**: The `fe-testing` skill references `testing.md` from this skill for all accessibility testing patterns (no duplication).

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
