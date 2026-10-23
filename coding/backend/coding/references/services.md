---
id: backend/coding/services
name: backend/coding/services
kind: reference
domain: backend
topics: [coding, services]
priority: medium
status: stable
canonical: false
updated: 2026-10-23
---

# Services

## When to use

Use this document when:

- Creating service layer business logic
- Implementing database operations via Prisma
- Handling external service integrations
- Managing error handling in services

> **Shared principles**: [readability and boundaries](../../../common/engineering/references/readability-and-boundaries.md) and [errors and observability](../../../common/engineering/references/errors-and-observability.md) are canonical for framework-independent decisions. This page covers NestJS service conventions.

## Rules

- Contain all business logic for the feature
- Inject PrismaService where the service directly owns Prisma access; use an existing persistence abstraction where the project has one. Services without database work need neither.
- Return typed promises (Promise<Type>)
- Delegate Prisma-to-HTTP translation to the project's configured exception filter when it owns that policy; NestJS does not automatically supply application-specific Prisma mapping.
- Catch Prisma or other failures when translating, recovering, isolating work, or adding useful context; otherwise let them reach the established handler.
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

  async sendWelcomeEmail(userId: string): Promise<'sent' | 'recipient_missing'> {
    const user = await this.prisma.user.findUnique({ where: { id: userId } });
    if (!user) return 'recipient_missing';
    try {
      await this.emailService.send(user.email, 'Welcome!');
      return 'sent';
    } catch (error) {
      this.logger.error({ event: 'welcome_email_failed', category: 'dependency_failure' });
      throw new InternalServerErrorException('Failed to send email', { cause: error });
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
      return await this.prisma.user.create({ data }); // Catch discards the failure
    } catch (error) {
      return null; // ❌ Swallowing errors
    }
  }
}
```

## Anti-patterns

- Using `any` type for parameters or returns
- Catching Prisma failures only to discard or obscure them
- Swallowing errors (return null/undefined without throwing)
- Mutating input parameters
- Missing Logger for important events

## Notes

- Keep methods focused (single responsibility)
- Use Logger for important events
- Services are injectable and can be used by other modules if exported
