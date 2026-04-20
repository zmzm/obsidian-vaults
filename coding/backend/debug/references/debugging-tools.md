---
id: backend/debug/debugging-tools
name: backend/debug/debugging-tools
kind: reference
domain: backend
topics: [debug, debugging tools]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Debugging Tools

## When to use

Use this document when:

- Need to enable detailed logging
- Want to inspect request/response data
- Debugging database queries
- Investigating performance issues

## Enable Prisma Query Logging

```typescript
// In DatabaseModule or service
const prisma = new PrismaClient({
  log: ['query', 'info', 'warn', 'error'],
});

// Or with query timing
const prisma = new PrismaClient({
  log: [
    { level: 'query', emit: 'event' },
    { level: 'error', emit: 'stdout' },
  ],
});

prisma.$on('query', e => {
  console.log(`Query: ${e.query}`);
  console.log(`Duration: ${e.duration}ms`);
});
```

## Enable NestJS Debug Logging

```bash
# Start server with debug logs
DEBUG=* pnpm nx serve backend

# Or specific namespace
DEBUG=nest:* pnpm nx serve backend
```

## Inspect Request Data

```typescript
@Post()
async create(@Body() dto: CreateUserDto, @Request() req) {
  console.log('Request body:', dto);
  console.log('User:', req.user);
  console.log('Headers:', req.headers);
  return this.service.create(dto);
}
```

## Custom Logger

```typescript
import { Logger } from '@nestjs/common';

@Injectable()
export class UsersService {
  private readonly logger = new Logger(UsersService.name);

  async create(dto: CreateUserDto) {
    this.logger.log(`Creating user: ${dto.email}`);
    this.logger.debug(`Full DTO: ${JSON.stringify(dto)}`);

    try {
      const user = await this.prisma.user.create({ data: dto });
      this.logger.log(`User created: ${user.id}`);
      return user;
    } catch (error) {
      this.logger.error(`Failed to create user: ${error.message}`, error.stack);
      throw error;
    }
  }
}
```

## VS Code Debugging

```json
// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Debug Backend",
      "runtimeExecutable": "pnpm",
      "runtimeArgs": ["nx", "serve", "backend"],
      "console": "integratedTerminal",
      "skipFiles": ["<node_internals>/**"]
    }
  ]
}
```

## Database Query Analysis

```sql
-- Check actual query in PostgreSQL
EXPLAIN ANALYZE SELECT * FROM "User" WHERE email = 'test@example.com';
```

```typescript
// Log raw query in Prisma
const result = await prisma.$queryRaw`
  EXPLAIN ANALYZE SELECT * FROM "User" WHERE email = ${email}
`;
console.log(result);
```

## Performance Profiling

```typescript
// Simple timing
const start = Date.now();
const result = await this.service.heavyOperation();
console.log(`Operation took: ${Date.now() - start}ms`);

// Using performance hooks
import { performance } from 'perf_hooks';

const start = performance.now();
const result = await this.service.heavyOperation();
const duration = performance.now() - start;
console.log(`Operation took: ${duration.toFixed(2)}ms`);
```

## Postman/API Testing

```bash
# Quick curl test
curl -X POST http://localhost:3000/api/users \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"email": "test@example.com", "role": "LEARNER"}'
```

## Notes

- Remove debug logging before committing
- Use Logger instead of console.log in production code
- Prisma logging can be verbose - use selectively
- VS Code debugger allows setting breakpoints
