---
id: backend/database/pagination
name: backend/database/pagination
kind: reference
domain: backend
topics: [database, pagination]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Pagination

## When to use

Use this document when:

- Implementing paginated list endpoints
- Returning large datasets efficiently
- Adding cursor-based pagination
- Combining pagination with filters

## Rules

- Use pagination for large datasets
- Include total count for UI
- Set reasonable page size limits
- Use cursor pagination for very large datasets

## Examples

### Good example - Offset pagination

```typescript
interface PaginatedResponse<T> {
  data: T[];
  meta: {
    total: number;
    page: number;
    limit: number;
    totalPages: number;
  };
}

async findAllPaginated(
  page: number = 1,
  limit: number = 10,
): Promise<PaginatedResponse<User>> {
  const skip = (page - 1) * limit;

  const [data, total] = await Promise.all([
    this.prisma.user.findMany({
      skip,
      take: limit,
      orderBy: { createdAt: 'desc' },
      select: {
        id: true,
        email: true,
        role: true,
        createdAt: true,
      },
    }),
    this.prisma.user.count(),
  ]);

  return {
    data,
    meta: {
      total,
      page,
      limit,
      totalPages: Math.ceil(total / limit),
    },
  };
}
```

### Pagination with filters

```typescript
async findAllPaginated(query: QueryCoursesDto): Promise<PaginatedResponse<Course>> {
  const { page = 1, limit = 10, difficulty, search } = query;
  const skip = (page - 1) * limit;

  const where = {
    ...(difficulty && { difficulty }),
    ...(search && {
      OR: [
        { title: { contains: search, mode: 'insensitive' } },
        { description: { contains: search, mode: 'insensitive' } },
      ],
    }),
  };

  const [data, total] = await Promise.all([
    this.prisma.course.findMany({
      where,
      skip,
      take: limit,
      orderBy: { createdAt: 'desc' },
    }),
    this.prisma.course.count({ where }),
  ]);

  return {
    data,
    meta: {
      total,
      page,
      limit,
      totalPages: Math.ceil(total / limit),
    },
  };
}
```

### Cursor-based pagination

```typescript
// For very large datasets or real-time data
async findAllCursor(cursor?: string, limit: number = 10) {
  const items = await this.prisma.notification.findMany({
    take: limit + 1, // Fetch one extra to check if more exist
    ...(cursor && {
      skip: 1, // Skip the cursor item
      cursor: { id: cursor },
    }),
    orderBy: { createdAt: 'desc' },
  });

  const hasMore = items.length > limit;
  const data = hasMore ? items.slice(0, -1) : items;
  const nextCursor = hasMore ? data[data.length - 1].id : null;

  return {
    data,
    nextCursor,
    hasMore,
  };
}
```

### Bad example

```typescript
// ❌ Bad: No pagination for potentially large list
async findAll() {
  return this.prisma.user.findMany(); // Could return thousands!
}

// ❌ Bad: Missing total count
async findAllPaginated(page: number, limit: number) {
  return this.prisma.user.findMany({
    skip: (page - 1) * limit,
    take: limit,
  }); // No total count for UI pagination controls
}
```

## Offset vs Cursor Pagination

| Offset                         | Cursor                 |
| ------------------------------ | ---------------------- |
| Simple implementation          | More complex           |
| Allows jumping to any page     | Sequential only        |
| Can have duplicates on inserts | Consistent results     |
| Slow on large offsets          | Consistent performance |

## Anti-patterns

- No pagination on list endpoints
- Missing total count
- No page size limits
- Using offset pagination on very large datasets

## Notes

- Set max limit (e.g., 100) to prevent abuse
- Use Promise.all to fetch data and count in parallel
- Consider cursor pagination for infinite scroll UIs
