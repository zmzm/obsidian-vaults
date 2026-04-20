---
id: backend/versioning/strategies
name: backend/versioning/strategies
kind: reference
domain: backend
topics: [versioning, strategies]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Versioning Strategies

## When to use

Use this document when:

- Choosing a versioning approach
- Implementing version handling
- Comparing versioning options

## Strategies Overview

| Strategy          | Example          | Pros             | Cons           |
| ----------------- | ---------------- | ---------------- | -------------- |
| URI (Recommended) | `/v1/users`      | Clear, cacheable | URL changes    |
| Header            | `Api-Version: 1` | Clean URLs       | Less visible   |
| Query Parameter   | `?version=1`     | Flexible         | Easy to forget |

## URI Versioning (Recommended for Mentory)

```typescript
// v1 endpoints
@Controller('v1/users')
export class UsersV1Controller {
  @Get()
  async findAll(): Promise<User[]> {
    return this.usersService.findAll();
  }
}

// v2 endpoints (with breaking changes)
@Controller('v2/users')
export class UsersV2Controller {
  @Get()
  async findAll(): Promise<UserV2[]> {
    return this.usersService.findAllV2();
  }
}
```

## Header Versioning (Alternative)

```typescript
@Get('users')
async findAll(@Headers('api-version') version: string = 'v1') {
  if (version === 'v2') {
    return this.usersService.findAllV2();
  }
  return this.usersService.findAll();
}
```

## Query Parameter Versioning (Alternative)

```typescript
@Get('users')
async findAll(@Query('version') version: string = 'v1') {
  if (version === 'v2') {
    return this.usersService.findAllV2();
  }
  return this.usersService.findAll();
}
```

## Shared Service with Version Adapters

```typescript
// Core service - version agnostic
@Injectable()
export class UsersService {
  async findOne(id: string): Promise<User> {
    return this.prisma.user.findUnique({ where: { id } });
  }
}

// V1 Adapter
@Injectable()
export class UsersV1Adapter {
  constructor(private usersService: UsersService) {}

  async findOne(id: string): Promise<UserV1Response> {
    const user = await this.usersService.findOne(id);
    return this.toV1Response(user);
  }

  private toV1Response(user: User): UserV1Response {
    return {
      id: user.id,
      name: user.email, // V1 used email as name
      role: user.role,
    };
  }
}

// V2 Adapter
@Injectable()
export class UsersV2Adapter {
  constructor(private usersService: UsersService) {}

  async findOne(id: string): Promise<UserV2Response> {
    const user = await this.usersService.findOne(id);
    return this.toV2Response(user);
  }

  private toV2Response(user: User): UserV2Response {
    return {
      id: user.id,
      email: user.email,
      displayName: user.name || user.email,
      role: user.role,
    };
  }
}
```

## Notes

- URI versioning is recommended for clarity
- Share core logic between versions using adapters
- Only increment version for breaking changes
- Test all versions simultaneously
