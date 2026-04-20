---
id: backend/coding/modules
name: backend/coding/modules
kind: reference
domain: backend
topics: [coding, modules]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Modules

## When to use

Use this document when:

- Creating new NestJS modules
- Configuring module imports and exports
- Setting up module dependencies
- Using forRoot/forFeature patterns

## Rules

- Follow Nx feature module structure
- Export services only if needed outside the module
- Import shared modules only when necessary
- Use forRoot/forFeature patterns for configurable modules

## Examples

### Good example

```typescript
// Basic feature module
@Module({
  imports: [DatabaseModule],
  controllers: [UsersController],
  providers: [UsersService],
  exports: [UsersService], // Only if used by other modules
})
export class UsersModule {}

// Configurable module with forRoot
@Module({})
export class EmailModule {
  static forRoot(options: EmailModuleOptions): DynamicModule {
    return {
      module: EmailModule,
      providers: [
        {
          provide: EMAIL_OPTIONS,
          useValue: options,
        },
        EmailService,
      ],
      exports: [EmailService],
    };
  }
}

// Usage in AppModule
@Module({
  imports: [
    DatabaseModule,
    UsersModule,
    EmailModule.forRoot({
      host: process.env.SMTP_HOST,
      port: parseInt(process.env.SMTP_PORT),
    }),
  ],
})
export class AppModule {}
```

### Bad example

```typescript
// ❌ Bad: Exporting everything, unnecessary imports
@Module({
  imports: [
    DatabaseModule,
    AuthModule, // Not needed
    CoursesModule, // Not needed
  ],
  controllers: [UsersController],
  providers: [UsersService, PrismaService], // ❌ Don't provide PrismaService here
  exports: [UsersService, PrismaService], // ❌ Don't export everything
})
export class UsersModule {}
```

## Anti-patterns

- Exporting services that aren't used externally
- Importing modules that aren't needed
- Providing services that should come from shared modules
- Circular dependencies between modules

## Notes

- Keep modules focused on a single feature
- Use DatabaseModule to provide PrismaService
- Avoid circular dependencies (use forwardRef if absolutely necessary)
- Module structure should match the backend file structure in CLAUDE.md
