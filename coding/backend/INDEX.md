# Backend Skills Index

Quick reference for selecting the right backend skill.

## Skill Selection Guide

| You're working on...                          | Use skill      |
| --------------------------------------------- | -------------- |
| Controllers, services, modules, DTOs          | `coding`       |
| Endpoint contracts, params, responses, Swagger| `api`          |
| Prisma, schema usage, queries, persistence    | `database`     |
| Runtime issues, failing flows, investigation  | `debug`        |
| Safer refactors and structural cleanup        | `refactor`     |
| Authz, validation hardening, attack surface   | `security`     |
| Unit/integration tests for backend behavior   | `testing`      |
| Git hygiene, change management, release flow  | `versioning`   |

## Decision Hints

### General Backend Work

```
Writing or changing NestJS feature code?
├── Mostly structure, services, modules, DTOs? → coding
├── Mostly request/response contract design? → api
└── Mostly persistence or Prisma usage? → database
```

### Quality and Safety

```
Improving existing backend code?
├── Investigating a bug or odd runtime behavior? → debug
├── Restructuring code without changing behavior? → refactor
├── Hardening auth/validation/security boundaries? → security
└── Expanding or fixing automated tests? → testing
```

## Skill Summaries

| Skill        | Purpose                                                        |
| ------------ | -------------------------------------------------------------- |
| `api`        | API contract design, endpoint shape, request/response clarity  |
| `coding`     | Core NestJS structure, controllers, services, DTOs, modules    |
| `database`   | Prisma usage, persistence patterns, data access discipline     |
| `debug`      | Investigating failures, tracing causes, narrowing error space  |
| `refactor`   | Safer structural changes and cleanup without broad regressions |
| `security`   | Security-sensitive backend patterns and defensive checks       |
| `testing`    | Backend testing strategy and implementation patterns           |
| `versioning` | Git/versioning conventions for backend delivery work           |

## Common Mistakes

| Wrong                                      | Right         | Why                                                |
| ------------------------------------------ | ------------- | -------------------------------------------------- |
| Put Prisma and business logic in controller| Use `coding`  | controllers should stay thin                       |
| Ask `security` for generic Nest structure  | Use `coding`  | security is for hardening, not general architecture|
| Use `api` for schema/query implementation  | Use `database`| transport contract and persistence are separate    |
| Use `debug` for planned cleanup            | Use `refactor`| diagnosis and restructuring are different tasks    |
