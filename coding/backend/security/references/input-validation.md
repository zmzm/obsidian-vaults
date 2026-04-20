---
id: backend/security/input-validation
name: backend/security/input-validation
kind: reference
domain: backend
topics: [security, input validation]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Input Validation

## When to use

Use this document when:

- Creating DTOs with validation
- Implementing password validation rules
- Sanitizing user input
- Preventing injection attacks

## Rules

- Use class-validator decorators on all DTOs
- Validate all input before processing
- Use strong password requirements
- Sanitize output to prevent XSS

## Examples

### Good example

```typescript
import { IsEmail, IsString, MinLength, MaxLength, Matches, IsEnum } from 'class-validator';

export class CreateUserDto {
  @IsEmail()
  email: string;

  @IsString()
  @MinLength(8)
  @MaxLength(50)
  @Matches(/((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/, {
    message: 'Password too weak - must contain uppercase, lowercase, and number/special char',
  })
  password: string;

  @IsEnum(UserRole)
  role: UserRole;
}

// Validation for updates
export class UpdatePasswordDto {
  @IsString()
  currentPassword: string;

  @IsString()
  @MinLength(8)
  @MaxLength(50)
  @Matches(/((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/, {
    message: 'Password too weak',
  })
  newPassword: string;
}
```

### Common Validators

```typescript
import {
  IsEmail,
  IsString,
  IsInt,
  IsUUID,
  IsOptional,
  IsNotEmpty,
  MinLength,
  MaxLength,
  Min,
  Max,
  IsEnum,
  IsUrl,
  IsBoolean,
  Matches,
  IsArray,
  ArrayMinSize,
  ValidateNested,
} from 'class-validator';
```

### Bad example

```typescript
// ❌ Bad: No validation
export class CreateUserDto {
  email: string;
  password: string;
  role: string;
}

// ❌ Bad: Weak password requirements
export class CreateUserDto {
  @IsString()
  @MinLength(4) // ❌ Too weak
  password: string;
}
```

## Password Requirements

For strong passwords, enforce:

- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number or special character

```typescript
@Matches(/((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/, {
  message: 'Password too weak',
})
```

## Anti-patterns

- No validation decorators
- Weak password requirements
- Missing length limits
- Not validating nested objects
- Using `any` type

## Notes

- class-validator runs automatically via ValidationPipe
- Use @Type() from class-transformer for nested objects
- Consider rate limiting on endpoints accepting user input
