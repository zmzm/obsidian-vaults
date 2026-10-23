---
id: backend/coding/error-handling
name: backend/coding/error-handling
kind: reference
domain: backend
topics: [coding, error handling]
priority: medium
status: stable
canonical: false
updated: 2026-10-23
---

# Error Handling

## When to use

Use this document when:

- Deciding when to use try/catch blocks
- Handling errors in services vs controllers
- Working with external service integrations
- Understanding NestJS exception filters

> **Canonical shared guidance**: [errors and observability](../../../common/engineering/references/errors-and-observability.md) owns error categories, causal context, redaction, and catch decisions. This page owns NestJS boundary translation and filter examples.

## Rules

- Use the project's configured filters for Prisma-to-HTTP mapping when they own that translation; this mapping must be implemented/configured.
- Catch at any layer when translating, recovering, isolating work, or adding useful context; otherwise propagate to the established handler.
- Controllers throw HTTP exceptions (NotFoundException, ConflictException)
- Services return null for not-found, let controller decide response
- Log errors with context using NestJS Logger

## When to Use Try/Catch

Follow the shared catch guidance linked above. In NestJS, prefer configured filters for consistent HTTP translation and pipes for transport validation. A local catch may still be appropriate for a known Prisma conflict or recovery step; an external call may simply propagate when a caller already owns handling.

## Examples

### Good example

```typescript
// Service - external operation with try/catch
@Injectable()
export class NotificationService {
  private readonly logger = new Logger(NotificationService.name);

  async sendPushNotification(userId: string, message: string): Promise<'sent' | 'recipient_missing'> {
    const user = await this.prisma.user.findUnique({ where: { id: userId } });
    if (!user) return 'recipient_missing';
    try {
      await this.pushService.send(user.deviceToken, message);
      return 'sent';
    } catch (error) {
      this.logger.error({ event: 'push_notification_failed', category: 'dependency_failure' });
      throw new InternalServerErrorException('Failed to send notification', { cause: error });
    }
  }
}

// Service - database operation without try/catch
@Injectable()
export class UsersService {
  async findOne(id: string): Promise<User | null> {
    // Propagate to the configured application handler; no local recovery is needed
    return this.prisma.user.findUnique({ where: { id } });
  }
}

// Controller - handle null case
@Controller('users')
export class UsersController {
  @Get(':id')
  async findOne(@Param('id') id: string): Promise<User> {
    const user = await this.usersService.findOne(id);
    if (!user) {
      throw new NotFoundException(`User with ID ${id} not found`);
    }
    return user;
  }
}
```

### Bad example

```typescript
// ❌ Bad: Catch discards the Prisma failure
async create(dto: CreateUserDto) {
  try {
    return await this.prisma.user.create({ data: dto });
  } catch (error) {
    return null; // ❌ Swallowing error
  }
}

// ❌ Bad: Failure is detached from the caller with no owning handler
async sendEmail(email: string) {
  void this.emailService.send(email); // Rejection and delivery outcome are lost
}
```

## Anti-patterns

- Wrapping all operations in try/catch
- Swallowing errors (return null instead of throwing)
- Missing Logger for error context
- Throwing generic Error instead of NestJS exceptions
- Not handling external service failures

## Notes

- Configured application exception filters can translate known Prisma errors into safe HTTP responses
- Use appropriate HTTP exceptions: NotFoundException, ConflictException, BadRequestException
- Log safe structured context at the owning boundary; the configured handler must avoid serializing raw causes or stacks without redaction.
- See `security` skill for security-related error handling
