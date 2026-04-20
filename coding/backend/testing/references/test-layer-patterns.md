---
id: backend/testing/test-layer-patterns
name: backend/testing/test-layer-patterns
kind: reference
domain: backend
topics: [testing, controller tests, service tests]
priority: high
status: stable
canonical: true
updated: 2026-04-16
---

# Backend Test Layer Patterns

## When to use

Use this document when:

- deciding how controller tests should differ from service tests
- setting up NestJS testing modules for unit tests
- choosing what to mock and what behavior to verify
- keeping backend tests focused on the correct layer boundary

## Decision Table

| If... | Prefer... | Why |
| ----- | ---------- | --- |
| the unit under test is a controller | mock services and override guards | controllers should mainly prove transport behavior and delegation |
| the unit under test is a service | mock Prisma or other downstream dependencies | services own business logic and data access behavior |
| the test is mostly about serialization, params, or HTTP flow | controller-level assertions | this belongs to the transport boundary |
| the test is mostly about transformations, branching, or persistence calls | service-level assertions | this belongs to business logic |

## Rules

### Mandatory

- keep controller tests focused on transport behavior, guard setup, and delegation
- keep service tests focused on business logic and dependency interaction
- clear mocks between tests

### Default

- use `TestingModule` from `@nestjs/testing`
- override guards in controller tests rather than exercising auth internals
- mock Prisma with a nested object or deep mock in service tests
- test both success paths and failure paths

### Heuristics

- verify exact dependency call arguments when the contract matters
- prefer one representative happy path and one representative failure path over large repetitive matrices
- split test data builders or mock factories out only when repetition becomes real

### Exceptions

- allow broader integration-style tests only when the layer boundary itself is the thing under risk

## Good Example

```ts
// Controller: verify delegation and HTTP-facing behavior
const module = await Test.createTestingModule({
  controllers: [UsersController],
  providers: [{ provide: UsersService, useValue: { findOne: jest.fn() } }],
})
  .overrideGuard(JwtAuthGuard)
  .useValue({ canActivate: jest.fn(() => true) })
  .compile();

// Service: verify business logic and Prisma interaction
const serviceModule = await Test.createTestingModule({
  providers: [
    UsersService,
    { provide: PrismaService, useValue: mockDeep<PrismaClient>() },
  ],
}).compile();
```

## Bad Example

```ts
// Bad: controller test that re-tests business logic instead of delegation
// Bad: service test that asserts framework routing concerns
```

## Anti-patterns

- testing business logic deeply in controller tests
- testing Nest routing details in service tests
- forgetting to override guards in controller tests
- asserting too little about dependency calls in service tests when that contract matters

## Notes

- Controllers should stay thin.
- Services should own branching, transformations, and persistence behavior.
- Use `mocking-patterns.md` for dependency mocking specifics.
