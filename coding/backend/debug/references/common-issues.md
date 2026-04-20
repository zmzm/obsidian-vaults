---
id: backend/debug/common-issues
name: backend/debug/common-issues
kind: reference
domain: backend
topics: [debug, common issues]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Common Issues & Solutions

## When to use

Use this document when:

- Encountering common NestJS bugs
- Looking for quick solutions
- Verifying fix patterns

## Missing `await` Keyword

**❌ Problem:**

```typescript
async create(dto: CreateUserDto): Promise<User> {
  // Missing await - returns Promise<User> instead of User
  const user = this.prisma.user.create({ data: dto });
  return user; // Error: Type mismatch
}
```

**✅ Solution:**

```typescript
async create(dto: CreateUserDto): Promise<User> {
  const user = await this.prisma.user.create({ data: dto });
  return user;
}
```

## DTO/Schema Mismatch

**❌ Problem:**

```typescript
// DTO has 'userName' but Prisma schema has 'username'
export class CreateUserDto {
  @IsString()
  userName: string; // Wrong field name
}
```

**✅ Solution:**

```typescript
export class CreateUserDto {
  @IsString()
  username: string; // Match Prisma field exactly
}
```

**How to verify:** Check `libs/db/prisma/schema.prisma`

## Incorrect Prisma Model Name

**❌ Problem:**

```typescript
// Typo in model name
await this.prisma.users.findMany(); // 'users' doesn't exist
```

**✅ Solution:**

```typescript
// Use exact Prisma model name (singular, lowercase in client)
await this.prisma.user.findMany();
```

## Guard Not Working

**❌ Problem:**

```typescript
@Post()
@UseGuards(JwtAuthGuard)
async create(@Body() dto: CreateUserDto) { }

// Wrong import
import { JwtAuthGuard } from '@nestjs/passport'; // ❌
```

**✅ Solution:**

```typescript
// Correct import from your common module
import { JwtAuthGuard } from '../../common/guards/jwt-auth.guard';
```

## Service/Controller Signature Mismatch

**❌ Problem:**

```typescript
// Service
async findOne(id: string): Promise<User | null> { ... }

// Controller - type error
async findOne(@Param('id') id: string): Promise<User> {
  return this.service.findOne(id); // null is not assignable to User
}
```

**✅ Solution:**

```typescript
// Controller handles null case
async findOne(@Param('id') id: string): Promise<User> {
  const user = await this.service.findOne(id);
  if (!user) {
    throw new NotFoundException(`User with ID ${id} not found`);
  }
  return user;
}
```

## Relationship Not Loaded

**❌ Problem:**

```typescript
const course = await this.prisma.course.findUnique({
  where: { id: courseId },
});
// course.assignments is undefined
console.log(course.assignments);
```

**✅ Solution:**

```typescript
const course = await this.prisma.course.findUnique({
  where: { id: courseId },
  include: {
    assignments: true, // Explicitly include relation
  },
});
```

## Environment Variable Not Loaded

**❌ Problem:**

```typescript
// process.env.JWT_SECRET is undefined
const secret = process.env.JWT_SECRET;
```

**✅ Solution:**

1. Check `.env` file exists
2. Verify variable name matches exactly
3. Restart server after changing `.env`
4. Use ConfigModule for type safety:

```typescript
import { ConfigService } from '@nestjs/config';

constructor(private config: ConfigService) {}

const secret = this.config.get<string>('JWT_SECRET');
```

## Notes

- Most issues are DTO/schema alignment problems
- Always restart server after .env changes
- Prisma model names are case-sensitive
- Check guard import paths carefully
