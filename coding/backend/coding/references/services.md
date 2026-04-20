---
id: backend/coding/services
name: backend/coding/services
kind: reference
domain: backend
topics: [coding, services]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Services

## When to use

Use this document when:

- Creating service layer business logic
- Implementing database operations via Prisma
- Handling external service integrations
- Managing error handling in services

## Rules

- Contain all business logic for the feature
- Inject PrismaService for database operations
- Return typed promises (Promise<Type>)
- Let NestJS exception filters handle Prisma errors
- Use try/catch for external operations only (email, APIs, file I/O)
- Return null for not-found cases (let controller decide response)

## Examples

### Good example

```typescript
@Injectable()
export class UsersService {
  constructor(private readonly prisma: PrismaService) {}

  async create(createUserDto: CreateUserDto): Promise<User> {
    return this.prisma.user.create({
      data: {
        email: createUserDto.email,
        role: createUserDto.role,
      },
      select: {
        id: true,
        email: true,
        role: true,
        createdAt: true,
      },
    });
  }

  async sendWelcomeEmail(userId: string): Promise<void> {
    try {
      // External operation - use try/catch
      const user = await this.prisma.user.findUnique({ where: { id: userId } });
      await this.emailService.send(user.email, 'Welcome!');
    } catch (error) {
      this.logger.error(`Failed to send welcome email: ${error.message}`);
      throw new InternalServerErrorException('Failed to send email');
    }
  }
}
```

### Bad example

```typescript
@Injectable()
export class UsersService {
  async create(data: any) {
    // ❌ No typing
    try {
      return await this.prisma.user.create({ data }); // ❌ Unnecessary try/catch for Prisma
    } catch (error) {
      return null; // ❌ Swallowing errors
    }
  }
}
```

## Anti-patterns

- Using `any` type for parameters or returns
- Wrapping Prisma operations in try/catch
- Swallowing errors (return null/undefined without throwing)
- Mutating input parameters
- Missing Logger for important events

## Notes

- Keep methods focused (single responsibility)
- Use Logger for important events
- Services are injectable and can be used by other modules if exported
