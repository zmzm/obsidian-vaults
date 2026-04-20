---
id: backend/api/restful-conventions
name: backend/api/restful-conventions
kind: reference
domain: backend
topics: [api, restful conventions]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# RESTful Conventions

## When to use

Use this document when:

- Creating new API endpoints
- Naming routes and resources
- Choosing HTTP methods
- Deciding on status codes

## Rules

- Use plural nouns for resources (`/users`, `/courses`)
- Use proper HTTP methods (GET, POST, PATCH, DELETE)
- Keep URLs lowercase with hyphens (not underscores)
- Don't use verbs in URLs (`/getUsers` → `/users`)
- Return appropriate status codes

## Examples

### Good example

```typescript
@Controller('users')
export class UsersController {
  @Get()           // GET /api/users → List all users
  @HttpCode(200)
  async findAll(): Promise<User[]> { ... }

  @Get(':id')      // GET /api/users/:id → Get single user
  @HttpCode(200)
  async findOne(@Param('id') id: string): Promise<User> { ... }

  @Post()          // POST /api/users → Create user
  @HttpCode(201)
  async create(@Body() dto: CreateUserDto): Promise<User> { ... }

  @Patch(':id')    // PATCH /api/users/:id → Update user
  @HttpCode(200)
  async update(
    @Param('id') id: string,
    @Body() dto: UpdateUserDto
  ): Promise<User> { ... }

  @Delete(':id')   // DELETE /api/users/:id → Delete user
  @HttpCode(204)
  async remove(@Param('id') id: string): Promise<void> { ... }
}
```

### Bad example

```typescript
@Controller('users')
export class UsersController {
  @Post('get-all')   // ❌ Wrong: Use GET, not POST
  getUsers() { ... }

  @Get('create')     // ❌ Wrong: Use POST for creation
  createUser() { ... }

  @Post('delete/:id') // ❌ Wrong: Use DELETE method
  deleteUser() { ... }
}
```

## HTTP Status Codes

| Code | Name                  | Usage                    |
| ---- | --------------------- | ------------------------ |
| 200  | OK                    | Successful GET, PATCH    |
| 201  | Created               | Successful POST          |
| 204  | No Content            | Successful DELETE        |
| 400  | Bad Request           | Validation error         |
| 401  | Unauthorized          | Authentication required  |
| 403  | Forbidden             | Insufficient permissions |
| 404  | Not Found             | Resource not found       |
| 409  | Conflict              | Resource already exists  |
| 500  | Internal Server Error | Unexpected error         |

## Anti-patterns

- Using verbs in URLs
- Mixing HTTP method semantics (GET for mutations)
- Inconsistent naming conventions
- Missing status codes

## Notes

- Use @HttpCode() decorator to set explicit status codes
- Use `/api` prefix for all API routes (configured in main.ts)
