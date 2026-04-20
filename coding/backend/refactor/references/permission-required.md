---
id: backend/refactor/permission-required
name: backend/refactor/permission-required
kind: reference
domain: backend
topics: [refactor, permission required]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Refactorings Requiring Permission

## When to use

Use this document when:

- Making breaking changes
- Modifying public APIs
- Changing database schema
- Renaming public-facing elements

## Rules

These changes require explicit permission before proceeding:

- Changing endpoint routes
- Renaming DTOs
- Modifying public method signatures
- Database schema changes
- Adding new dependencies

## Changing Endpoint Routes

```typescript
// ⚠️ Requires permission - breaking change for API consumers
@Get('users/:id')  →  @Get('users/:userId')

// ⚠️ Requires permission - route change
@Get('user-profiles')  →  @Get('profiles')
```

**Why:** External consumers depend on the URL structure.

## Renaming DTOs

```typescript
// ⚠️ Requires permission - affects API consumers
export class CreateUserDto { ... }  →  export class RegisterUserDto { ... }

// ⚠️ Requires permission - field name change
export class CreateUserDto {
  userName: string;  →  displayName: string;
}
```

**Why:** API request/response structure changes.

## Modifying Public Method Signatures

```typescript
// ⚠️ Requires permission - breaking change for other modules
async findOne(id: string): Promise<User>
  →
async findOne(id: string, includeDeleted: boolean): Promise<User>

// ⚠️ Requires permission - return type change
async findOne(id: string): Promise<User>
  →
async findOne(id: string): Promise<User | null>
```

**Why:** Other modules depend on these signatures.

## Database Schema Changes

```prisma
// ⚠️ Requires permission - migration needed
model User {
  email String  →  emailAddress String
}

// ⚠️ Requires permission - data loss possible
model User {
  middleName String?  // Removing this field
}

// ⚠️ Requires permission - making optional required
model User {
  phone String?  →  phone String
}
```

**Why:** Migrations affect all environments and data.

## Adding New Dependencies

```bash
# ⚠️ Requires permission - affects bundle size and security
pnpm add new-package
```

**Why:** New dependencies affect security, bundle size, and maintenance.

## How to Request Permission

When you need permission for a breaking change:

1. **Explain the change:** What you want to change and why
2. **Show the impact:** What will break and who is affected
3. **Propose migration:** How to handle the transition
4. **Wait for approval:** Don't proceed without explicit OK

```markdown
⚠️ Breaking Change Request:

**Change:** Rename `CreateUserDto` to `RegisterUserDto` **Reason:** Better semantic naming for registration endpoint **Impact:** Frontend
registration form needs update **Migration:** Update frontend in same PR **Risk:** Low - internal API only

Proceed? [y/n]
```

## Notes

- When in doubt, ask first
- Breaking changes should be batched when possible
- Consider deprecation period for public APIs
- Document all breaking changes in CHANGELOG
