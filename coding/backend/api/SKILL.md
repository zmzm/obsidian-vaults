---
name: be-api
description:

  Guide for RESTful API design patterns and conventions for NestJS endpoints. Use when designing or modifying API endpoints,
  request/response structures, query parameters, pagination, nested resources, or error responses. This skill focuses on API design
  conventions, not implementation details covered in coding skill.
---

# Backend API Design Skill

## When to use this knowledge

Use this skill when you are:

- Designing new API endpoints
- Structuring request/response formats
- Implementing filtering, sorting, or pagination
- Handling nested resource relationships
- Defining error response formats
- Planning API versioning strategy

## When not to use this knowledge

- **Implementation patterns** → See `be-coding` skill
- **API versioning** → See `be-versioning` skill
- **Security headers** → See `be-security` skill

## What this skill covers

This skill provides guidance for:

- RESTful naming conventions and HTTP methods
- DTO design for complex queries
- Response structure patterns
- Query parameter handling
- Error response formats
- Nested resource patterns

## Knowledge map

Always start here, then follow references as needed:

- RESTful conventions → `references/restful-conventions.md`
- DTO design → `references/dto-design.md`
- Response structure → `references/response-structure.md`
- Query parameters → `references/query-parameters.md`
- Error responses → `references/error-responses.md`
- Nested resources → `references/nested-resources.md`

## Fast decision hints

- If the task is mainly about Designing new API endpoints, start with this skill.
- If the task also involves Structuring request/response formats, follow the most relevant reference page.
- If the work drifts into Implementing filtering, sorting, or pagination, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Use RESTful naming (plural nouns: `/users`, `/courses`)
- `<default>` Default: Use proper HTTP methods (GET, POST, PATCH, DELETE)
- `<heuristic>` Heuristic: Return appropriate status codes
- `<exception>` Exception: Validate all input with DTOs

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **API design conventions**. For:

- **Implementation patterns** → See `be-coding` skill
- **API versioning** → See `be-versioning` skill
- **Security headers** → See `be-security` skill

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
