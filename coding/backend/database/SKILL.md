---
name: be-database
description:

  Guide for Prisma ORM patterns and PostgreSQL database operations for efficient queries, transactions, migrations, and data management. Use
  when working with database operations, writing Prisma queries, implementing transactions, creating migrations, or optimizing queries with
  indexes and pagination.
---

# Backend Database Skill

## When to use this knowledge

Use this skill when you are:

- Writing Prisma queries with proper field selection
- Implementing transactions for multi-step operations
- Creating and running migrations
- Optimizing queries with indexes and pagination
- Handling relationships and aggregations
- Managing database seeding

## When not to use this knowledge

- **Security concerns** → See `be-security` skill (SQL injection prevention)
- **Testing with mocks** → See `be-testing` skill (Prisma mocking)

## What this skill covers

This skill provides guidance for:

- Efficient Prisma queries with select/include
- Transaction patterns for data consistency
- Pagination and filtering
- Indexing strategies
- Migration best practices
- Seeding for development

## Knowledge map

Always start here, then follow references as needed:

- Queries → `references/queries.md`
- Transactions → `references/transactions.md`
- Pagination → `references/pagination.md`
- Indexing → `references/indexing.md`
- Migrations → `references/migrations.md`
- Seeding → `references/seeding.md`

## Fast decision hints

- If the task is mainly about Writing Prisma queries with proper field selection, start with this skill.
- If the task also involves Implementing transactions for multi-step operations, follow the most relevant reference page.
- If the work drifts into Creating and running migrations, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Use Prisma for all database operations (no raw SQL unless necessary)
- `<default>` Default: Use `select` to limit returned fields (exclude sensitive data)
- `<heuristic>` Heuristic: Use transactions for multi-step operations
- `<exception>` Exception: Handle unique constraint violations

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **database operations**. For:

- **Security concerns** → See `be-security` skill (SQL injection prevention)
- **Testing with mocks** → See `be-testing` skill (Prisma mocking)

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
