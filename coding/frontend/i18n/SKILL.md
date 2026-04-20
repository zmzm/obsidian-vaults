---
name: fe-i18n
description: Internationalization with react-i18next. Use for translations, pluralization, formatting.
triggers:

  paths: ['**/i18n/**', '**/*.locales.ts']
  keywords: ['useTranslation', 't(', 'i18n.', 'Trans ', 'interpolation', 'plural']
---

# Frontend i18n Skill

## When to use this knowledge

Use this skill when you are:

- Localizing UI text and adding translations
- Implementing multilingual support for the platform
- Handling dynamic text with interpolation
- Working with pluralization rules
- Formatting dates, numbers, or currency based on locale
- Organizing translations by namespace

## When not to use this knowledge

- Tasks owned more directly by a neighboring skill
- Pure exploration or lookup work without implementation decisions

## What this skill covers

This skill provides guidance for:

- Core principles and usage patterns
- Namespace organization and selection
- Interpolation for dynamic values
- Pluralization handling
- Common patterns (errors, forms, dates)
- Testing i18n in components
- Translation workflow

## Knowledge map

Always start here, then follow references as needed:

- Core Principles → `references/core-principles.md`
- Interpolation → `references/interpolation.md`
- Pluralization → `references/pluralization.md`
- Patterns → `references/patterns.md`
- Adding Translations → `references/adding-translations.md`
- Testing → `references/testing.md`

## Fast decision hints

- If the task is mainly about Localizing UI text and adding translations, start with this skill.
- If the task also involves Implementing multilingual support for the platform, follow the most relevant reference page.
- If the work drifts into Handling dynamic text with interpolation, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Prefer documented patterns over ad-hoc solutions
- `<default>` Default: Avoid listed anti-patterns unless explicitly justified
- `<heuristic>` Heuristic: If multiple references apply, compare them explicitly
- `<exception>` Exception: If deviating from the guidelines, clearly explain why and what is being violated

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **its own domain scope**. For adjacent concerns, move to the neighboring skill with the clearest ownership.

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
