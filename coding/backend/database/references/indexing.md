---
id: backend/database/indexing
name: backend/database/indexing
kind: reference
domain: backend
topics: [database, indexing]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Indexing

## When to use

Use this document when:

- Optimizing query performance
- Adding indexes to schema
- Working with frequently queried fields
- Implementing composite indexes

## Rules

- Add indexes on frequently queried fields
- Use composite indexes for multi-column filters
- Unique fields are automatically indexed
- Consider read/write tradeoffs

## Examples

### Good example - Schema indexes

```prisma
// schema.prisma

model User {
  id        String   @id @default(cuid())
  email     String   @unique  // Automatically indexed
  role      UserRole
  createdAt DateTime @default(now())
  deletedAt DateTime?

  @@index([role])              // Index for filtering by role
  @@index([createdAt])         // Index for sorting
  @@index([deletedAt])         // Index for soft delete queries
  @@index([email, role])       // Composite index
}

model Course {
  id         String           @id @default(cuid())
  title      String
  difficulty CourseDifficulty
  published  Boolean          @default(false)
  mentorId   String
  createdAt  DateTime         @default(now())

  @@index([difficulty])
  @@index([published])
  @@index([mentorId])
  @@index([difficulty, published])  // Composite for filtered queries
  @@index([createdAt])              // For sorting
}

model Enrollment {
  id        String   @id @default(cuid())
  userId    String
  courseId  String
  createdAt DateTime @default(now())

  @@unique([userId, courseId])  // Composite unique (auto indexed)
  @@index([userId])             // For user's enrollments
  @@index([courseId])           // For course's enrollments
}
```

### When to add indexes

| Query Pattern                                        | Index Needed                       |
| ---------------------------------------------------- | ---------------------------------- |
| `where: { role: 'ADMIN' }`                           | `@@index([role])`                  |
| `orderBy: { createdAt: 'desc' }`                     | `@@index([createdAt])`             |
| `where: { difficulty: 'BEGINNER', published: true }` | `@@index([difficulty, published])` |
| `where: { email: 'x' }`                              | `@unique` on email (auto indexed)  |

### Soft delete index

```prisma
model User {
  deletedAt DateTime?

  @@index([deletedAt])  // For filtering active users
}
```

```typescript
// Query benefits from index
async findAllActive() {
  return this.prisma.user.findMany({
    where: { deletedAt: null },
  });
}
```

### Bad example

```prisma
// ❌ Bad: No indexes on frequently queried fields
model Course {
  id         String @id
  difficulty String  // No index, but frequently filtered
  published  Boolean // No index, but frequently filtered
}
```

## Index Types

| Type          | Use Case                       |
| ------------- | ------------------------------ |
| Single column | Simple equality/range queries  |
| Composite     | Multi-column filters           |
| Unique        | Enforcing uniqueness + lookups |

## Anti-patterns

- No indexes on frequently filtered columns
- Too many indexes (slow writes)
- Wrong column order in composite indexes
- Indexing rarely queried columns

## Notes

- @unique and @id are automatically indexed
- Composite index column order matters
- Too many indexes slow down writes
- Use EXPLAIN ANALYZE to verify index usage
