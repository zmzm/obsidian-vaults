---
id: backend/database/queries
name: backend/database/queries
kind: reference
domain: backend
topics: [database, queries]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Prisma Queries

## When to use

Use this document when:

- Writing Prisma queries
- Selecting specific fields
- Including related data
- Filtering and searching

## Rules

- Use `select` to limit returned fields
- Use `include` for relations explicitly
- Avoid fetching all fields when only few are needed
- Use proper where clauses for filtering

## Examples

### Good example - Select specific fields

```typescript
// ✅ Good: Only fetch needed fields
async findAll(): Promise<Partial<User>[]> {
  return this.prisma.user.findMany({
    select: {
      id: true,
      email: true,
      role: true,
      // password excluded!
    },
  });
}

// ❌ Bad: Fetch all fields
async findAll() {
  return this.prisma.user.findMany(); // Returns everything including password!
}
```

### Good example - Include relations

```typescript
// ✅ Good: Explicitly include relations
async findCourseWithAssignments(id: string) {
  return this.prisma.course.findUnique({
    where: { id },
    include: {
      assignments: true,
      enrollments: {
        select: {
          userId: true,
          enrolledAt: true,
        },
      },
    },
  });
}
```

### Filtering and searching

```typescript
// Text search
async searchCourses(query: string) {
  return this.prisma.course.findMany({
    where: {
      OR: [
        { title: { contains: query, mode: 'insensitive' } },
        { description: { contains: query, mode: 'insensitive' } },
      ],
    },
  });
}

// Multiple filters
async findUsers(filters: { role?: UserRole; isActive?: boolean }) {
  return this.prisma.user.findMany({
    where: {
      ...(filters.role && { role: filters.role }),
      ...(filters.isActive !== undefined && { isActive: filters.isActive }),
    },
  });
}
```

### Aggregations

```typescript
// Count
const userCount = await this.prisma.user.count({
  where: { role: UserRole.LEARNER },
});

// Average
const avgScore = await this.prisma.submission.aggregate({
  _avg: { grade: true },
  where: { assignmentId: '123' },
});

// Group by
const coursesByDifficulty = await this.prisma.course.groupBy({
  by: ['difficulty'],
  _count: { id: true },
});
```

### Raw queries (when necessary)

```typescript
// ✅ Good: Parameterized raw query
const users = await this.prisma.$queryRaw<User[]>`
  SELECT * FROM "User"
  WHERE role = ${UserRole.ADMIN}
  AND "createdAt" > ${startDate}
`;

// ❌ Bad: String interpolation (SQL injection risk)
const users = await this.prisma.$queryRaw`
  SELECT * FROM "User"
  WHERE email = '${email}'
`;
```

## Anti-patterns

- Fetching all fields when only few are needed
- Not using select to exclude sensitive fields
- N+1 queries (not using include)
- String interpolation in raw queries

## Notes

- Relations are not loaded by default - use `include` explicitly
- Use `select` and `include` together when needed
- See `pagination.md` for paginated queries
