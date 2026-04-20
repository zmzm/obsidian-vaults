---
id: backend/coding/controllers
name: backend/coding/controllers
kind: reference
domain: backend
topics: [coding, controllers]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Controllers

## When to use

Use this document when:

- Creating new controller endpoints
- Adding authentication guards to endpoints
- Implementing Swagger documentation
- Handling request/response in controller layer

## Rules

- Controllers remain thin - delegate all business logic to services
- Apply guards to POST, PATCH, DELETE endpoints
- Use Swagger decorators for API documentation
- Validate all input via DTOs (use class-validator)
- Handle null/not found cases explicitly
- Return proper HTTP status codes

## Examples

### Good example

```typescript
@ApiTags('Users')
@Controller('users')
@UseGuards(JwtAuthGuard)
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Post()
  @UseGuards(JwtAuthGuard, RolesGuard)
  @Roles(UserRole.ADMIN)
  @ApiOperation({ summary: 'Create user (Admin only)' })
  @ApiResponse({ status: 201, description: 'User created successfully' })
  @ApiResponse({ status: 401, description: 'Unauthorized' })
  @ApiResponse({ status: 403, description: 'Forbidden - Admin role required' })
  async create(@Body() createUserDto: CreateUserDto) {
    return this.usersService.create(createUserDto);
  }

  @Get(':id')
  @ApiOperation({ summary: 'Find user by ID' })
  @ApiResponse({ status: 200, description: 'User found successfully' })
  @ApiResponse({ status: 404, description: 'User not found' })
  async findOne(@Param('id') id: string) {
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
@Controller('users')
export class UsersController {
  constructor(private readonly prisma: PrismaService) {} // ❌ Don't inject Prisma directly

  @Post()
  async create(@Body() data: any) {
    // ❌ No DTO validation, no guards, business logic in controller
    const hashedPassword = await bcrypt.hash(data.password, 10);
    return this.prisma.user.create({
      data: { ...data, password: hashedPassword },
    });
  }
}
```

## Anti-patterns

- Injecting PrismaService directly in controllers
- Business logic in controller methods
- Missing guards on protected endpoints
- Using `any` type for request body
- Missing Swagger documentation

## Notes

- Use descriptive names for methods (findAll, findOne, create, update, remove)
- Don't return different data structures for same endpoint
- Let controller decide HTTP response, service returns data or null
