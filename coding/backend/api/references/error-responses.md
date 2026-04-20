---
id: backend/api/error-responses
name: backend/api/error-responses
kind: reference
domain: backend
topics: [api, error responses]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Error Responses

## When to use

Use this document when:

- Handling error cases in controllers
- Defining error response formats
- Choosing appropriate HTTP status codes
- Writing user-friendly error messages

## Rules

- Use NestJS built-in exceptions
- Return appropriate status codes
- Include helpful error messages (but not sensitive data)
- Be consistent with error format

## Examples

### Good example

```typescript
@Get(':id')
async findOne(@Param('id') id: string): Promise<User> {
  const user = await this.usersService.findOne(id);

  if (!user) {
    throw new NotFoundException(`User with ID ${id} not found`);
  }

  return user;
}

@Post()
async create(@Body() dto: CreateUserDto): Promise<User> {
  const exists = await this.usersService.findByEmail(dto.email);

  if (exists) {
    throw new ConflictException(`User with email ${dto.email} already exists`);
  }

  return this.usersService.create(dto);
}

@Patch(':id')
async update(
  @Param('id') id: string,
  @Body() dto: UpdateUserDto,
): Promise<User> {
  const user = await this.usersService.findOne(id);

  if (!user) {
    throw new NotFoundException(`User with ID ${id} not found`);
  }

  return this.usersService.update(id, dto);
}
```

### NestJS Exception Classes

```typescript
// Common exceptions
import {
  NotFoundException, // 404 - Resource not found
  ConflictException, // 409 - Resource already exists
  BadRequestException, // 400 - Invalid input
  UnauthorizedException, // 401 - Not authenticated
  ForbiddenException, // 403 - Not authorized
  InternalServerErrorException, // 500 - Server error
} from '@nestjs/common';
```

### Bad example

```typescript
// ❌ Bad: Generic error, exposes sensitive info
@Get(':id')
async findOne(@Param('id') id: string) {
  try {
    return await this.usersService.findOne(id);
  } catch (error) {
    throw new Error(error.stack); // ❌ Exposes stack trace
  }
}

// ❌ Bad: Wrong status code
@Post()
async create(@Body() dto: CreateUserDto) {
  const exists = await this.usersService.findByEmail(dto.email);
  if (exists) {
    throw new BadRequestException('Email exists'); // ❌ Should be 409 Conflict
  }
}
```

## Error Response Format

NestJS exceptions produce consistent JSON:

```json
{
  "statusCode": 404,
  "message": "User with ID abc123 not found",
  "error": "Not Found"
}
```

## Anti-patterns

- Exposing stack traces or internal errors
- Using wrong status codes
- Generic error messages without context
- Inconsistent error formats

## Notes

- Don't include sensitive data (passwords, tokens) in error messages
- Use specific exceptions for specific cases
- Let validation pipe handle DTO validation errors automatically
