---
name: be-coding
description:

  Guide for general NestJS backend development practices, code architecture, and structural patterns. Use when creating or modifying NestJS
  controllers, services, modules, DTOs, or any backend code that involves business logic, validation, dependency injection, or error
  handling. This skill focuses on framework-agnostic patterns, not specific security or testing concerns.
---

# Backend Coding Skill

## When to use this knowledge

Use this skill when you are:

- Writing or refactoring backend code structure
- Creating controllers, services, modules, or DTOs
- Making architectural or structural decisions
- Handling errors and exceptions
- Managing dependency injection
- Reviewing backend code quality and consistency

## When not to use this knowledge

- **Security concerns** → See `be-security` skill
- **Testing patterns** → See `be-testing` skill
- **Database operations** → See `be-database` skill

## What this skill covers

This skill provides guidance for:

- Controller patterns (thin controllers, guards, Swagger)
- Service layer patterns (business logic, Prisma usage)
- DTO validation with class-validator
- Module organization and exports
- Error handling guidelines

## Knowledge map

Always start here, then follow references as needed:

- Controllers → `references/controllers.md`
- Services → `references/services.md`
- DTOs → `references/dtos.md`
- Modules → `references/modules.md`
- Error handling → `references/error-handling.md`

## Fast decision hints

- If the task is mainly about Writing or refactoring backend code structure, start with this skill.
- If the task also involves Creating controllers, services, modules, or DTOs, follow the most relevant reference page.
- If the work drifts into Making architectural or structural decisions, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Controllers remain thin - delegate all business logic to services
- `<default>` Default: Services contain all business logic and inject PrismaService
- `<heuristic>` Heuristic: DTOs use class-validator decorators and match Prisma schema naming
- `<exception>` Exception: Modules follow Nx feature module structure

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **general NestJS development practices**. For:

- **Security concerns** → See `be-security` skill
- **Testing patterns** → See `be-testing` skill
- **Database operations** → See `be-database` skill
- **API design conventions** → See `be-api` skill

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
