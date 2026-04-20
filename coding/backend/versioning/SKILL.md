---
name: be-versioning
description:

  Guide for REST API versioning strategies and patterns for maintaining backward compatibility while introducing breaking changes. Use when
  implementing API versioning, managing version lifecycle, adding deprecation headers, or creating migration guides.
---

# API Versioning Skill

## When to use this knowledge

Use this skill when you are:

- Creating new API versions
- Implementing breaking changes
- Managing deprecation of old versions
- Writing migration guides
- Documenting changelog

## When not to use this knowledge

- **API design** → See `be-api` skill
- **Breaking change process** → See `be-refactor` skill

## What this skill covers

This skill provides guidance for:

- Versioning strategies (URI, header, query param)
- Breaking vs non-breaking changes
- Deprecation strategy
- Module structure for versions
- Version lifecycle management

## Knowledge map

Always start here, then follow references as needed:

- Strategies → `references/strategies.md`
- Breaking changes → `references/breaking-changes.md`
- Deprecation → `references/deprecation.md`
- Module structure → `references/module-structure.md`

## Fast decision hints

- If the task is mainly about Creating new API versions, start with this skill.
- If the task also involves Implementing breaking changes, follow the most relevant reference page.
- If the work drifts into Managing deprecation of old versions, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Maintain backward compatibility (no breaking changes in same version)
- `<default>` Default: Version via URI path (e.g., `/v1/users`, `/v2/users`)
- `<heuristic>` Heuristic: Document all changes in CHANGELOG.md
- `<exception>` Exception: Support previous version for minimum 6 months after new release

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **API versioning**. For:

- **API design** → See `be-api` skill
- **Breaking change process** → See `be-refactor` skill

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
