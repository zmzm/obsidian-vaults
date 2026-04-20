---
id: backend/security/rate-limiting
name: backend/security/rate-limiting
kind: reference
domain: backend
topics: [security, rate limiting]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Rate Limiting

## When to use

Use this document when:

- Protecting auth endpoints from brute force
- Preventing API abuse
- Implementing throttling
- Configuring per-endpoint limits

## Rules

- Apply rate limiting to authentication endpoints
- Use stricter limits on sensitive operations
- Provide sensible defaults
- Consider user-based vs IP-based limiting

## Examples

### Good example

```typescript
// Install: pnpm add @nestjs/throttler

// app.module.ts
import { ThrottlerModule, ThrottlerGuard } from '@nestjs/throttler';

@Module({
  imports: [
    ThrottlerModule.forRoot([
      {
        ttl: 60000,  // Time window in milliseconds
        limit: 10,   // Max requests per window
      },
    ]),
  ],
  providers: [
    {
      provide: APP_GUARD,
      useClass: ThrottlerGuard,
    },
  ],
})
export class AppModule {}

// Stricter limits on auth endpoints
@Controller('auth')
export class AuthController {
  @Post('login')
  @Throttle({ default: { limit: 5, ttl: 60000 } }) // 5 attempts per minute
  async login(@Body() dto: LoginDto) {
    return this.authService.login(dto);
  }

  @Post('forgot-password')
  @Throttle({ default: { limit: 3, ttl: 300000 } }) // 3 per 5 minutes
  async forgotPassword(@Body() dto: ForgotPasswordDto) {
    return this.authService.forgotPassword(dto);
  }
}

// Skip throttling for specific endpoints
@Get('health')
@SkipThrottle()
async healthCheck() {
  return { status: 'ok' };
}
```

### Configuration Options

```typescript
ThrottlerModule.forRoot([
  {
    name: 'short',
    ttl: 1000,    // 1 second
    limit: 3,     // 3 requests per second
  },
  {
    name: 'medium',
    ttl: 10000,   // 10 seconds
    limit: 20,    // 20 requests per 10 seconds
  },
  {
    name: 'long',
    ttl: 60000,   // 1 minute
    limit: 100,   // 100 requests per minute
  },
]);

// Use specific throttler
@Throttle({ short: { limit: 1, ttl: 1000 } })
```

### Custom Error Response

```typescript
import { ThrottlerException } from '@nestjs/throttler';

@Catch(ThrottlerException)
export class ThrottlerExceptionFilter implements ExceptionFilter {
  catch(exception: ThrottlerException, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse();

    response.status(429).json({
      statusCode: 429,
      message: 'Too many requests. Please try again later.',
      retryAfter: 60,
    });
  }
}
```

## Recommended Limits

| Endpoint       | Limit | Window    |
| -------------- | ----- | --------- |
| Login          | 5     | 1 minute  |
| Password reset | 3     | 5 minutes |
| Registration   | 3     | 1 minute  |
| General API    | 100   | 1 minute  |
| File upload    | 10    | 1 minute  |

## Anti-patterns

- No rate limiting on auth endpoints
- Same limits for all endpoints
- Not handling 429 responses gracefully
- Rate limiting by IP only (consider user-based)

## Notes

- Return 429 Too Many Requests when limit exceeded
- Include Retry-After header in response
- Consider Redis for distributed rate limiting
