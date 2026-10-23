---
id: backend/refactor/permission-required
name: backend/refactor/permission-required
kind: reference
domain: backend
topics: [refactor, permission required]
priority: medium
status: stable
canonical: false
updated: 2026-10-23
---

# Refactoring Scope and Permission

## When to use

Use this document when:

- Making breaking changes
- Modifying public APIs
- Changing database schema
- Renaming public-facing elements

## Rules

First check the existing task authorization. These changes need additional approval only when their impact or execution falls outside the approved scope. Routine authorized work does not require repeated permission. See the canonical [verification and change safety](../../../common/engineering/references/verification-and-change-safety.md) guidance and [contracts and validation](../../../common/engineering/references/contracts-and-validation.md).

Inspect the impact of:

- Changing endpoint routes
- Renaming DTOs that affect exported or generated contracts
- Modifying public method signatures
- Database schema changes
- Adding new dependencies

## Changing Endpoint Routes

```typescript
// Internal parameter rename: update bindings; the concrete URL is unchanged.
// Check generated client/schema impact separately.
@Get('users/:id')  →  @Get('users/:userId')

// Check authorization and compatibility - route change
@Get('user-profiles')  →  @Get('profiles')
```

**Why:** External consumers depend on the URL structure.

## Renaming DTOs

```typescript
// Internal rename unless imports or generated schemas expose this name
export class CreateUserDto { ... }  →  export class RegisterUserDto { ... }

// Check authorization and compatibility - field name change
export class CreateUserDto {
  userName: string;  →  displayName: string;
}
```

**Why:** A class rename alone need not change serialized data. It can affect imports, generated clients, or schema names if exposed; a serialized field rename changes the wire contract. Update internal callers together, and check actual consumers before classifying the change.

## Modifying Public Method Signatures

```typescript
// Check authorization and compatibility - breaking change for other modules
async findOne(id: string): Promise<User>
  →
async findOne(id: string, includeDeleted: boolean): Promise<User>

// Check authorization and compatibility - return type change
async findOne(id: string): Promise<User>
  →
async findOne(id: string): Promise<User | null>
```

**Why:** Other modules depend on these signatures.

## Database Schema Changes

```prisma
// Check authorization and compatibility - migration needed
model User {
  email String  →  emailAddress String
}

// Check authorization and compatibility - data loss possible
model User {
  middleName String?  // Removing this field
}

// Check authorization and compatibility - making optional required
model User {
  phone String?  →  phone String
}
```

**Why:** Migrations affect all environments and data.

## Adding New Dependencies

```bash
# Check authorization - affects bundle size and security
pnpm add new-package
```

**Why:** New dependencies affect security, bundle size, and maintenance.

## How to Request Permission

When the required change is outside existing authorization:

1. **Explain the change:** What you want to change and why
2. **Show the impact:** What will break and who is affected
3. **Propose migration:** How to handle the transition
4. **Wait for approval:** Don't proceed without explicit OK

```markdown
⚠️ Breaking Change Request:

**Change:** Rename the serialized request field `userName` to `displayName`. **Reason:** Align the public contract. **Impact:** Existing clients sending `userName` would fail. **Migration:** Temporarily accept both names and update clients before removal. **Approval needed:** This public contract change is outside the approved internal refactor.

Proceed? [y/n]
```

## Notes

- Clarify missing authorization when necessary; preserve existing approval for routine work already in scope
- Breaking changes should be batched when possible
- Consider deprecation period for public APIs
- Document all breaking changes in CHANGELOG
