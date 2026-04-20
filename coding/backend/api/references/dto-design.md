---
id: backend/api/dto-design
name: backend/api/dto-design
kind: reference
domain: backend
topics: [api, dto design]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# DTO Design

## When to use

Use this document when:

- Creating DTOs for complex queries
- Designing DTOs with nested validation
- Setting up transformation and default values
- Implementing optional fields with validation

## Rules

- Use class-validator for validation
- Use PartialType for update DTOs
- Keep DTOs in a dedicated `dto/` folder
- Return typed values from the service layer
- Use @Transform for type coercion from query strings

## Examples

### Good example

```typescript
// dto/create-course.dto.ts
import { IsString, IsEnum, IsOptional, IsUrl } from 'class-validator';
import { CourseDifficulty } from '@mentory/db';

export class CreateCourseDto {
  @IsString()
  title: string;

  @IsString()
  description: string;

  @IsEnum(CourseDifficulty)
  difficulty: CourseDifficulty;

  @IsUrl()
  @IsOptional()
  videoUrl?: string;
}

// dto/update-course.dto.ts
import { PartialType } from '@nestjs/mapped-types';
import { CreateCourseDto } from './create-course.dto';

export class UpdateCourseDto extends PartialType(CreateCourseDto) {}

// dto/create-user-with-profile.dto.ts (nested validation)
import { ValidateNested, Type } from 'class-validator';

class ProfileDto {
  @IsString()
  bio: string;

  @IsUrl()
  @IsOptional()
  avatarUrl?: string;
}

export class CreateUserWithProfileDto {
  @IsEmail()
  email: string;

  @ValidateNested()
  @Type(() => ProfileDto)
  profile: ProfileDto;
}
```

### Bad example

```typescript
// ❌ Bad: No validation, no typing
export class CreateCourseDto {
  title: string;
  description: string;
  difficulty: string; // Should be enum
}

// ❌ Bad: Business logic in DTO
export class CreateUserDto {
  email: string;

  formatEmail() {
    return this.email.toLowerCase();
  }
}
```

## Anti-patterns

- Missing validation decorators
- Business logic in DTOs
- Not using PartialType for updates
- Missing @Type decorator for nested objects
- Not handling type coercion for query params

## Notes

- Query parameters come as strings - use @Transform for numbers/booleans
- Use @Type from class-transformer for nested object validation
- See `query-parameters.md` for pagination and filtering DTOs
