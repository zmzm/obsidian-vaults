---
id: backend/api/response-structure
name: backend/api/response-structure
kind: reference
domain: backend
topics: [api, response structure]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Response Structure

## When to use

Use this document when:

- Designing API response formats
- Implementing pagination responses
- Returning single vs collection resources
- Adding metadata to responses

## Rules

- Return entities directly for single resources
- Return arrays for collections
- Use pagination for large datasets
- Include metadata when helpful (total count, page info)

## Examples

### Good example

```typescript
// Single resource
@Get(':id')
async findOne(@Param('id') id: string): Promise<User> {
  return this.usersService.findOne(id);
}

// Collection (simple)
@Get()
async findAll(): Promise<User[]> {
  return this.usersService.findAll();
}

// Collection (paginated)
@Get()
async findAll(
  @Query('page') page = 1,
  @Query('limit') limit = 10
): Promise<PaginatedResponse<User>> {
  return this.usersService.findAllPaginated(page, limit);
}

// Paginated response type
interface PaginatedResponse<T> {
  data: T[];
  meta: {
    total: number;
    page: number;
    limit: number;
    totalPages: number;
  };
}

// Service implementation
async findAllPaginated(page: number, limit: number): Promise<PaginatedResponse<User>> {
  const skip = (page - 1) * limit;

  const [data, total] = await Promise.all([
    this.prisma.user.findMany({ skip, take: limit }),
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

### Bad example

```typescript
// ❌ Bad: Inconsistent response formats
@Get()
async findAll() {
  return {
    success: true, // ❌ Unnecessary wrapper
    data: await this.usersService.findAll(),
  };
}

@Get(':id')
async findOne(@Param('id') id: string) {
  return await this.usersService.findOne(id); // ❌ Different format than findAll
}
```

## Anti-patterns

- Wrapping responses in `{ success: true, data: ... }`
- Inconsistent response formats across endpoints
- Missing pagination for large collections
- Not including total count in paginated responses

## Notes

- Keep response format consistent across all endpoints
- Use interfaces/types for response structures
- Consider cursor-based pagination for very large datasets
