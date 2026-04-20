---
id: backend/versioning/module-structure
name: backend/versioning/module-structure
kind: reference
domain: backend
topics: [versioning, module structure]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Version Module Structure

## When to use

Use this document when:

- Organizing versioned endpoints
- Structuring controllers and DTOs per version
- Setting up module configuration

## Recommended Structure

```
apps/backend/src/modules/users/
├── v1/
│   ├── users-v1.controller.ts
│   ├── users-v1.adapter.ts
│   └── dto/
│       └── user-v1.dto.ts
├── v2/
│   ├── users-v2.controller.ts
│   ├── users-v2.adapter.ts
│   └── dto/
│       └── user-v2.dto.ts
├── users.service.ts      # Shared business logic
├── users.module.ts       # Combines all versions
└── dto/
    └── create-user.dto.ts  # Shared DTOs
```

## Module Configuration

```typescript
// users.module.ts
@Module({
  imports: [DatabaseModule],
  controllers: [UsersV1Controller, UsersV2Controller],
  providers: [UsersService, UsersV1Adapter, UsersV2Adapter],
  exports: [UsersService],
})
export class UsersModule {}
```

## Controller Structure

```typescript
// v1/users-v1.controller.ts
@Controller('v1/users')
@ApiTags('Users V1')
export class UsersV1Controller {
  constructor(private readonly adapter: UsersV1Adapter) {}

  @Get(':id')
  @ApiOperation({ summary: 'Get user (V1)' })
  async findOne(@Param('id') id: string): Promise<UserV1Response> {
    return this.adapter.findOne(id);
  }
}

// v2/users-v2.controller.ts
@Controller('v2/users')
@ApiTags('Users V2')
export class UsersV2Controller {
  constructor(private readonly adapter: UsersV2Adapter) {}

  @Get(':id')
  @ApiOperation({ summary: 'Get user (V2)' })
  async findOne(@Param('id') id: string): Promise<UserV2Response> {
    return this.adapter.findOne(id);
  }
}
```

## DTO Structure

```typescript
// v1/dto/user-v1.dto.ts
export class UserV1Response {
  id: string;
  name: string; // Contains email in V1
  role: string;
}

// v2/dto/user-v2.dto.ts
export class UserV2Response {
  id: string;
  email: string;
  displayName: string;
  role: string;
}

// dto/create-user.dto.ts (shared)
export class CreateUserDto {
  @IsEmail()
  email: string;

  @IsString()
  @MinLength(8)
  password: string;
}
```

## Adapter Pattern

```typescript
// v1/users-v1.adapter.ts
@Injectable()
export class UsersV1Adapter {
  constructor(private readonly usersService: UsersService) {}

  async findOne(id: string): Promise<UserV1Response> {
    const user = await this.usersService.findOne(id);
    if (!user) return null;

    return {
      id: user.id,
      name: user.email, // V1 used email as name
      role: user.role,
    };
  }

  async findAll(): Promise<UserV1Response[]> {
    const users = await this.usersService.findAll();
    return users.map(user => ({
      id: user.id,
      name: user.email,
      role: user.role,
    }));
  }
}

// v2/users-v2.adapter.ts
@Injectable()
export class UsersV2Adapter {
  constructor(private readonly usersService: UsersService) {}

  async findOne(id: string): Promise<UserV2Response> {
    const user = await this.usersService.findOne(id);
    if (!user) return null;

    return {
      id: user.id,
      email: user.email,
      displayName: user.displayName || user.email,
      role: user.role,
    };
  }
}
```

## Testing Multiple Versions

```typescript
describe('Users API V1', () => {
  it('should return user with name field', async () => {
    const response = await request(app.getHttpServer()).get('/v1/users/123').expect(200);

    expect(response.body).toHaveProperty('name');
    expect(response.body).not.toHaveProperty('email');
  });
});

describe('Users API V2', () => {
  it('should return user with email and displayName', async () => {
    const response = await request(app.getHttpServer()).get('/v2/users/123').expect(200);

    expect(response.body).toHaveProperty('email');
    expect(response.body).toHaveProperty('displayName');
    expect(response.body).not.toHaveProperty('name');
  });
});
```

## Notes

- Keep core business logic in shared service
- Use adapters to transform data per version
- Test all versions simultaneously
- Swagger tags help organize documentation by version
