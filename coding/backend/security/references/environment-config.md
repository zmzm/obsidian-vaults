---
id: backend/security/environment-config
name: backend/security/environment-config
kind: reference
domain: backend
topics: [security, environment config]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Environment Configuration

## When to use

Use this document when:

- Managing secrets and credentials
- Configuring database connections
- Setting up JWT secrets
- Handling environment-specific settings

## Rules

- Use environment variables for all secrets
- Never hardcode credentials
- Validate required environment variables
- Use ConfigModule for type-safe access

## Examples

### Good example

```typescript
// app.module.ts
import { ConfigModule, ConfigService } from '@nestjs/config';

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
      validate: validateEnv,
    }),
  ],
})
export class AppModule {}

// env.validation.ts
import { plainToInstance } from 'class-transformer';
import { IsString, IsInt, validateSync, Min } from 'class-validator';

class EnvironmentVariables {
  @IsString()
  DATABASE_URL: string;

  @IsString()
  JWT_SECRET: string;

  @IsInt()
  @Min(1)
  JWT_EXPIRES_IN: number;

  @IsString()
  CLERK_SECRET_KEY: string;

  @IsString()
  FRONTEND_URL: string;
}

export function validateEnv(config: Record<string, unknown>) {
  const validatedConfig = plainToInstance(EnvironmentVariables, config, {
    enableImplicitConversion: true,
  });

  const errors = validateSync(validatedConfig, {
    skipMissingProperties: false,
  });

  if (errors.length > 0) {
    throw new Error(errors.toString());
  }

  return validatedConfig;
}

// Using in service
@Injectable()
export class AuthService {
  constructor(private configService: ConfigService) {}

  async generateToken(user: User): Promise<string> {
    const secret = this.configService.get<string>('JWT_SECRET');
    const expiresIn = this.configService.get<number>('JWT_EXPIRES_IN');

    return this.jwtService.sign({ userId: user.id }, { secret, expiresIn });
  }
}
```

### Required Environment Variables

```bash
# .env.example (commit this, not .env)
DATABASE_URL=postgresql://user:password@localhost:5432/mentory
JWT_SECRET=your-secret-key-here
JWT_EXPIRES_IN=86400
CLERK_SECRET_KEY=your-clerk-secret
FRONTEND_URL=http://localhost:4200
```

### Bad example

```typescript
// ❌ Bad: Hardcoded secrets
const JWT_SECRET = 'my-secret-key';

// ❌ Bad: No validation
const secret = process.env.JWT_SECRET; // Could be undefined

// ❌ Bad: Committing .env file
// .gitignore should include .env
```

## Anti-patterns

- Hardcoding secrets in code
- Missing .env from .gitignore
- Not validating required variables
- Using process.env directly instead of ConfigService
- Committing production secrets

## Notes

- Use .env.example for documenting required variables
- Different .env files for different environments
- ConfigService provides type-safe access
- Validate all required variables at startup
