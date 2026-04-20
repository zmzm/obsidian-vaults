---
id: backend/versioning/deprecation
name: backend/versioning/deprecation
kind: reference
domain: backend
topics: [versioning, deprecation]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Deprecation Strategy

## When to use

Use this document when:

- Deprecating old API versions
- Adding deprecation headers
- Planning version sunset
- Communicating timeline to consumers

## Deprecation Headers

```typescript
@Controller('v1/users')
export class UsersV1Controller {
  private readonly logger = new Logger(UsersV1Controller.name);

  @Get(':id')
  async findOne(@Param('id') id: string, @Res({ passthrough: true }) res: Response) {
    // Add deprecation headers
    res.setHeader('X-API-Deprecation', 'This endpoint will be removed on 2026-01-01');
    res.setHeader('X-API-Sunset', '2026-01-01');
    res.setHeader('Link', '</v2/users>; rel="successor-version"');

    this.logger.warn(`V1 API called: GET /v1/users/${id} - deprecated`);

    return this.usersService.findOne(id);
  }
}
```

## Deprecation Middleware

```typescript
// middleware/deprecation.middleware.ts
@Injectable()
export class DeprecationMiddleware implements NestMiddleware {
  private readonly logger = new Logger(DeprecationMiddleware.name);

  use(req: Request, res: Response, next: NextFunction) {
    if (req.path.startsWith('/v1/')) {
      res.setHeader('X-API-Deprecation', 'V1 API deprecated. Migrate to V2 by 2026-01-01');
      res.setHeader('X-API-Sunset', '2026-01-01');

      this.logger.warn(`Deprecated V1 API called: ${req.method} ${req.path}`);
    }
    next();
  }
}

// app.module.ts
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(DeprecationMiddleware).forRoutes('v1/*');
  }
}
```

## Version Lifecycle Policy

| Phase      | Duration          | Action                                      |
| ---------- | ----------------- | ------------------------------------------- |
| Active     | Current           | Full support, recommended                   |
| Deprecated | 6-12 months       | Works, deprecation headers, migration guide |
| Sunset     | After deprecation | Removed, returns 410 Gone                   |

### Timeline Example

```
Jan 2025: V2 released, V1 deprecated
Jul 2025: V1 sunset warning increased (emails, dashboard notices)
Jan 2026: V1 removed (returns 410 Gone)
```

## Sunset Response

```typescript
// After sunset date
@Controller('v1/users')
export class UsersV1Controller {
  @All('*')
  sunset(@Res() res: Response) {
    res.status(410).json({
      statusCode: 410,
      message: 'This API version has been sunset. Please use /v2/users',
      documentation: 'https://docs.mentory.com/api/v2',
      migrationGuide: 'https://docs.mentory.com/migration/v1-to-v2',
    });
  }
}
```

## Communication Timeline

1. **At deprecation:**

   - Add deprecation headers
   - Update documentation
   - Email major consumers
   - Blog post announcement

2. **3 months before sunset:**

   - Increase warning visibility
   - Personal outreach to active V1 users
   - Dashboard notifications

3. **1 month before sunset:**

   - Final warning emails
   - Rate limit V1 requests
   - Support team prepared for questions

4. **At sunset:**
   - Return 410 Gone
   - Redirect to migration guide
   - Remove V1 code (optional, can keep for reference)

## Notes

- Never remove without deprecation period
- Minimum 6 months deprecation for public APIs
- Log all deprecated endpoint usage for planning
- Provide clear migration documentation
