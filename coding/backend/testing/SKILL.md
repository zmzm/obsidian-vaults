---
name: be-testing
description:

  Guide for Jest unit testing patterns for NestJS controllers, services, and utilities following AAA pattern with proper mocking. Use when
  writing or modifying backend tests, setting up test modules, mocking dependencies, or ensuring code coverage.
---

# Backend Testing Skill

## When to use this knowledge

Use this skill when you are:

- Writing unit tests for controllers
- Testing service layer business logic
- Testing utility functions
- Setting up mocks for Prisma and external services
- Ensuring 80%+ code coverage

## When not to use this knowledge

- **Implementation patterns** → See `be-coding` skill
- **Database mocking** → See `mocking-patterns.md` reference

## What this skill covers

This skill provides guidance for:

- Controller testing patterns with guard overrides
- Service testing with Prisma mocking
- Utility/helper function testing
- Common mocking patterns
- Test conventions and best practices

## Knowledge map

Always start here, then follow references as needed:

- Test layer patterns → `references/test-layer-patterns.md`
- Utility tests → `references/utility-tests.md`
- Mocking patterns → `references/mocking-patterns.md`

## Fast decision hints

- If the task is mainly about Writing unit tests for controllers, start with this skill.
- If the task also involves Testing service layer business logic, follow the most relevant reference page.
- If the work drifts into Testing utility functions, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Follow AAA pattern (Arrange → Act → Assert)
- `<default>` Default: Test success and error scenarios
- `<heuristic>` Heuristic: Mock external dependencies (Prisma, services, APIs)
- `<exception>` Exception: Achieve 80% minimum code coverage

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **testing patterns**. For:

- **Implementation patterns** → See `be-coding` skill
- **Database mocking** → See `mocking-patterns.md` reference

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
