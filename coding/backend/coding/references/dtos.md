---
id: backend/coding/dtos
name: backend/coding/dtos
kind: reference
domain: backend
topics: [coding, dtos]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# DTOs (Data Transfer Objects)

> **See also**: For complex DTO patterns (pagination, filtering, nested validation, transformations), see `be-api/references/dto-design.md`.

This document focuses on **basic DTO structure** and Prisma alignment.

## When to use

Use this document when:

- Creating basic Create/Update DTOs
- Ensuring DTO and Prisma schema alignment
- Setting up validation decorators

For complex patterns (Query DTOs, transforms) → see `be-api/dto-design.md`

## Rules

- Use class-validator decorators (@IsString, @IsEmail, etc.)
- Keep DTOs simple and declarative (no methods)
- Use PartialType for update DTOs
- Match Prisma schema field names exactly
- Group related DTOs in `dto/` folder

## Basic DTO Structure

```typescript
import { IsEmail, IsEnum, IsString, MinLength, IsOptional } from 'class-validator';
import { PartialType } from '@nestjs/mapped-types';
import { UserRole } from '@mentory/db';

export class CreateUserDto {
  @IsEmail()
  email: string;

  @IsString()
  @MinLength(8)
  password: string;

  @IsEnum(UserRole)
  role: UserRole;

  @IsString()
  @IsOptional()
  displayName?: string;
}

export class UpdateUserDto extends PartialType(CreateUserDto) {}
```

## DTO Naming Convention

| Type   | Pattern             | Example         |
| ------ | ------------------- | --------------- |
| Create | `Create{Entity}Dto` | `CreateUserDto` |
| Update | `Update{Entity}Dto` | `UpdateUserDto` |
| Query  | `Query{Entity}Dto`  | `QueryUserDto`  |

## Anti-patterns

```typescript
// ❌ Bad: No validation decorators
export class CreateUserDto {
  email: string;
  password: string;
}

// ❌ Bad: Business logic in DTO
export class CreateUserDto {
  hashPassword() {
    this.password = bcrypt.hashSync(this.password, 10);
  }
}

// ❌ Bad: Field name mismatch with Prisma
export class CreateUserDto {
  userName: string; // Prisma has: displayName
}
```

## Notes

- DTOs should be pure data structures
- Optional fields must have `@IsOptional()` decorator
- For Query DTOs with @Transform → see `be-api/dto-design.md`
- For nested validation with @ValidateNested → see `be-api/dto-design.md`
