---
id: backend/database/migrations
name: backend/database/migrations
kind: reference
domain: backend
topics: [database, migrations]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Migrations

## When to use

Use this document when:

- Creating database migrations
- Modifying schema safely
- Running migrations in different environments
- Handling breaking schema changes

## Rules

- Run migrations in order (dev → staging → production)
- Test migrations on staging first
- Make breaking changes in steps
- Never edit existing migrations

## Commands

```bash
# Generate Prisma client after schema changes
pnpm nx run db:generate

# Create migration (development)
pnpm nx run db:migrate:dev --name add-user-role

# Apply migrations (production)
pnpm nx run db:migrate:deploy

# Reset database (dev only - deletes all data!)
pnpm nx run db:reset
```

## Examples

### Safe migrations - Adding optional field

```prisma
// Step 1: Add as optional
model User {
  id       String  @id
  newField String? // Optional first
}
```

```bash
pnpm nx run db:migrate:dev --name add-new-field
```

```prisma
// Step 2: Backfill data, then make required
model User {
  id       String @id
  newField String // Now required
}
```

### Safe migrations - Renaming field

```prisma
// Step 1: Add new field
model User {
  oldName String
  newName String?
}
```

```bash
pnpm nx run db:migrate:dev --name add-new-name-field
```

```typescript
// Step 2: Backfill data
await prisma.$executeRaw`UPDATE "User" SET "newName" = "oldName"`;
```

```prisma
// Step 3: Make new field required, drop old
model User {
  newName String
  // oldName removed
}
```

### Dangerous migrations

```prisma
// ⚠️ Dangerous: Dropping column
// Data will be lost!
model User {
  id String @id
  // removedField was here - now gone!
}

// ⚠️ Dangerous: Making optional field required
// Existing null values will cause error
model User {
  id    String @id
  field String // Was String? - will fail if nulls exist
}
```

## Migration Workflow

1. **Development**

   ```bash
   # Edit schema.prisma
   pnpm nx run db:migrate:dev --name descriptive-name
   ```

2. **Staging**

   ```bash
   pnpm nx run db:migrate:deploy
   # Verify everything works
   ```

3. **Production**
   ```bash
   pnpm nx run db:migrate:deploy
   ```

## Anti-patterns

- Editing existing migrations
- Skipping staging environment
- Making breaking changes in one step
- Running migrate:dev in production

## Notes

- Never run `migrate dev` in production
- `migrate deploy` only applies pending migrations
- Keep migration names descriptive
- Backup database before risky migrations
