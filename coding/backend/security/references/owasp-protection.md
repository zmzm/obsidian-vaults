---
id: backend/security/owasp-protection
name: backend/security/owasp-protection
kind: reference
domain: backend
topics: [security, owasp protection]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# OWASP Top 10 Protection

## When to use

Use this document when:

- Implementing security features
- Reviewing code for vulnerabilities
- Setting up authentication/authorization
- Handling sensitive data

## OWASP Top 10 Patterns

### 1. Broken Access Control

```typescript
// ✅ Good: Use guards and roles
@Get('admin/users')
@UseGuards(JwtAuthGuard, RolesGuard)
@Roles(UserRole.ADMIN)
async getAdminUsers() {
  return this.usersService.findAll();
}

// ❌ Bad: No authorization check
@Get('admin/users')
async getAdminUsers() {
  return this.usersService.findAll();
}
```

### 2. Cryptographic Failures

```typescript
// ✅ Good: Hash passwords with bcrypt
import * as bcrypt from 'bcrypt';

async hashPassword(password: string): Promise<string> {
  const salt = await bcrypt.genSalt(10);
  return bcrypt.hash(password, salt);
}

// ❌ Bad: Storing plain text passwords
async createUser(dto: CreateUserDto) {
  return this.prisma.user.create({
    data: { ...dto, password: dto.password }, // ❌ Plain text!
  });
}
```

### 3. Injection (SQL Injection)

```typescript
// ✅ Good: Use Prisma (parameterized queries)
async findByEmail(email: string): Promise<User> {
  return this.prisma.user.findUnique({
    where: { email }, // Safe - Prisma parameterizes
  });
}

// ❌ Bad: Raw SQL with string interpolation
async findByEmail(email: string) {
  return this.prisma.$queryRaw`SELECT * FROM users WHERE email = '${email}'`;
  // ❌ Vulnerable to SQL injection!
}
```

### 4. Sensitive Data Exposure

```typescript
// ✅ Good: Exclude sensitive fields
async findOne(id: string): Promise<Partial<User>> {
  return this.prisma.user.findUnique({
    where: { id },
    select: {
      id: true,
      email: true,
      role: true,
      // password excluded!
      // tokens excluded!
    },
  });
}

// ❌ Bad: Return all fields
async findOne(id: string) {
  return this.prisma.user.findUnique({ where: { id } });
  // ❌ Returns password, tokens, etc!
}
```

### 5. Security Misconfiguration

```typescript
// ✅ Good: Proper CORS configuration
const corsOptions: CorsOptions = {
  origin: process.env.FRONTEND_URL,
  credentials: true,
  methods: ['GET', 'POST', 'PATCH', 'DELETE'],
};
app.enableCors(corsOptions);

// ❌ Bad: Allow all origins
app.enableCors(); // ❌ Security risk!
```

### 6. Vulnerable Components

```bash
# ✅ Good: Regular dependency updates
pnpm audit
pnpm update
pnpm audit --audit-level=moderate
```

### 7. Identification & Authentication Failures

```typescript
// ✅ Good: Account lockout after failed attempts
const MAX_ATTEMPTS = 5;
const LOCKOUT_DURATION_MS = 30 * 60 * 1000; // 30 minutes

if (user.failedLoginAttempts >= MAX_ATTEMPTS) {
  if (user.lockedUntil && user.lockedUntil > new Date()) {
    throw new UnauthorizedException('Account is locked');
  }
}

// ❌ Bad: Unlimited login attempts
```

### 8. Software & Data Integrity Failures

```typescript
// ✅ Good: Verify JWT signatures
async verifyToken(token: string) {
  try {
    return this.jwtService.verify(token, {
      secret: process.env.JWT_SECRET,
    });
  } catch (error) {
    throw new UnauthorizedException('Invalid token');
  }
}
```

### 9. Security Logging & Monitoring

```typescript
// ✅ Good: Log security events
@Injectable()
export class AuthService {
  private readonly logger = new Logger(AuthService.name);

  async login(email: string, password: string) {
    const user = await this.findByEmail(email);

    if (!user) {
      this.logger.warn(`Failed login attempt for email: ${email}`);
      throw new UnauthorizedException('Invalid credentials');
    }

    const isValid = await bcrypt.compare(password, user.password);

    if (!isValid) {
      this.logger.warn(`Invalid password for user: ${user.id}`);
      await this.incrementFailedAttempts(user.id);
      throw new UnauthorizedException('Invalid credentials');
    }

    this.logger.log(`Successful login for user: ${user.id}`);
    return this.generateToken(user);
  }
}
```

### 10. Server-Side Request Forgery (SSRF)

```typescript
// ✅ Good: Validate URLs before fetching
async fetchExternalData(url: string) {
  const allowedDomains = ['api.example.com', 'cdn.example.com'];
  const parsedUrl = new URL(url);

  if (!allowedDomains.includes(parsedUrl.hostname)) {
    throw new BadRequestException('Invalid URL domain');
  }

  return fetch(url);
}
```

## Notes

- Always follow the principle of least privilege
- Log security events without sensitive data
- Regular security audits and penetration testing
