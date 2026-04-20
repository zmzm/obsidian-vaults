---
id: backend/api/query-parameters
name: backend/api/query-parameters
kind: reference
domain: backend
topics: [api, query parameters]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Query Parameters

## When to use

Use this document when:

- Implementing filtering on list endpoints
- Adding sorting capabilities
- Setting up pagination parameters
- Validating query parameters with DTOs

## Rules

- Use @Query() for filtering, sorting, pagination
- Validate query parameters with DTOs
- Provide sensible defaults
- Use @Transform for type coercion

## Examples

### Good example

```typescript
// dto/query-courses.dto.ts
import { IsEnum, IsString, IsInt, IsOptional, Min, Max } from 'class-validator';
import { Transform } from 'class-transformer';
import { CourseDifficulty } from '@mentory/db';

export class QueryCoursesDto {
  @IsEnum(CourseDifficulty)
  @IsOptional()
  difficulty?: CourseDifficulty;

  @IsString()
  @IsOptional()
  search?: string;

  @IsInt()
  @Min(1)
  @IsOptional()
  @Transform(({ value }) => parseInt(value, 10))
  page?: number = 1;

  @IsInt()
  @Min(1)
  @Max(100)
  @IsOptional()
  @Transform(({ value }) => parseInt(value, 10))
  limit?: number = 10;

  @IsString()
  @IsOptional()
  sortBy?: string = 'createdAt';

  @IsEnum(['asc', 'desc'])
  @IsOptional()
  sortOrder?: 'asc' | 'desc' = 'desc';
}

// Controller
@Get()
async findAll(@Query() query: QueryCoursesDto): Promise<Course[]> {
  return this.coursesService.findAll(query);
}

// Service
async findAll(query: QueryCoursesDto): Promise<Course[]> {
  const { difficulty, search, page, limit, sortBy, sortOrder } = query;

  return this.prisma.course.findMany({
    where: {
      ...(difficulty && { difficulty }),
      ...(search && {
        OR: [
          { title: { contains: search, mode: 'insensitive' } },
          { description: { contains: search, mode: 'insensitive' } },
        ],
      }),
    },
    skip: (page - 1) * limit,
    take: limit,
    orderBy: { [sortBy]: sortOrder },
  });
}
```

### Bad example

```typescript
// ❌ Bad: No validation, no defaults, no type coercion
@Get()
async findAll(
  @Query('page') page: string,     // ❌ String, not number
  @Query('limit') limit: string,   // ❌ String, not number
  @Query('difficulty') difficulty: string,  // ❌ Not validated
) {
  return this.coursesService.findAll(+page, +limit, difficulty);
}
```

## Anti-patterns

- Not validating query parameters
- Missing default values
- Not handling type coercion (query params are strings)
- Unlimited results without pagination

## Notes

- Query parameters always come as strings from HTTP
- Use @Transform decorator for number/boolean coercion
- Set reasonable max limits (e.g., 100) to prevent abuse
