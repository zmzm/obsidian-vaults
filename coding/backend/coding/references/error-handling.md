---
id: backend/coding/error-handling
name: backend/coding/error-handling
kind: reference
domain: backend
topics: [coding, error handling]
priority: medium
status: stable
canonical: true
updated: 2026-04-16
---

# Error Handling

## When to use

Use this document when:

- Deciding when to use try/catch blocks
- Handling errors in services vs controllers
- Working with external service integrations
- Understanding NestJS exception filters

## Rules

- Let NestJS exception filters handle Prisma errors
- Use try/catch for external operations only
- Controllers throw HTTP exceptions (NotFoundException, ConflictException)
- Services return null for not-found, let controller decide response
- Log errors with context using NestJS Logger

## When to Use Try/Catch

### ✅ Use for external operations

- External API calls
- File system operations
- Email sending
- Third-party service integrations

### ❌ Don't use for

- Prisma database operations (let exception filters handle)
- Simple validation (use DTOs and pipes)
- Business logic errors (throw appropriate exceptions)

## Examples

### Good example

```typescript
// Service - external operation with try/catch
@Injectable()
export class NotificationService {
  private readonly logger = new Logger(NotificationService.name);

  async sendPushNotification(userId: string, message: string): Promise<void> {
    try {
      const user = await this.prisma.user.findUnique({ where: { id: userId } });
      await this.pushService.send(user.deviceToken, message);
    } catch (error) {
      this.logger.error(`Push notification failed: ${error.message}`, error.stack);
      throw new InternalServerErrorException('Failed to send notification');
    }
  }
}

// Service - database operation without try/catch
@Injectable()
export class UsersService {
  async findOne(id: string): Promise<User | null> {
    // No try/catch - let exception filters handle Prisma errors
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
// ❌ Bad: Unnecessary try/catch for Prisma
async create(dto: CreateUserDto) {
  try {
    return await this.prisma.user.create({ data: dto });
  } catch (error) {
    return null; // ❌ Swallowing error
  }
}

// ❌ Bad: No error handling for external call
async sendEmail(email: string) {
  await this.emailService.send(email); // ❌ No try/catch for external
}
```

## Anti-patterns

- Wrapping all operations in try/catch
- Swallowing errors (return null instead of throwing)
- Missing Logger for error context
- Throwing generic Error instead of NestJS exceptions
- Not handling external service failures

## Notes

- NestJS exception filters transform Prisma errors to HTTP responses
- Use appropriate HTTP exceptions: NotFoundException, ConflictException, BadRequestException
- Always log errors with context (user ID, operation, etc.)
- See `security` skill for security-related error handling
