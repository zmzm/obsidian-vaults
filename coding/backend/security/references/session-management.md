---
id: backend/security/session-management
name: backend/security/session-management
kind: reference
domain: backend
topics: [security, session management]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Session Management

## When to use

Use this document when:

- Implementing JWT authentication
- Setting up secure cookies
- Managing token expiration
- Handling logout and token invalidation

## Rules

- Use HttpOnly cookies for tokens when possible
- Set appropriate token expiration
- Implement proper logout
- Consider refresh token strategy

## Examples

### Good example

```typescript
// Secure cookie-based JWT
@Post('login')
async login(
  @Res({ passthrough: true }) res: Response,
  @Body() dto: LoginDto,
) {
  const token = await this.authService.login(dto);

  res.cookie('jwt', token, {
    httpOnly: true,      // Not accessible via JavaScript
    secure: true,        // HTTPS only (in production)
    sameSite: 'strict',  // CSRF protection
    maxAge: 24 * 60 * 60 * 1000, // 24 hours
  });

  return { message: 'Login successful' };
}

// Logout - clear cookie
@Post('logout')
async logout(@Res({ passthrough: true }) res: Response) {
  res.clearCookie('jwt', {
    httpOnly: true,
    secure: true,
    sameSite: 'strict',
  });

  return { message: 'Logout successful' };
}

// JWT with expiration
async generateToken(user: User): Promise<string> {
  return this.jwtService.sign(
    { userId: user.id, role: user.role },
    {
      secret: this.configService.get('JWT_SECRET'),
      expiresIn: '24h',
    },
  );
}
```

### Refresh Token Strategy

```typescript
// Generate both access and refresh tokens
async login(dto: LoginDto) {
  const user = await this.validateUser(dto);

  const accessToken = await this.generateAccessToken(user);
  const refreshToken = await this.generateRefreshToken(user);

  // Store refresh token hash in database
  await this.storeRefreshToken(user.id, refreshToken);

  return { accessToken, refreshToken };
}

// Access token - short lived
async generateAccessToken(user: User): Promise<string> {
  return this.jwtService.sign(
    { userId: user.id, role: user.role },
    { expiresIn: '15m' },
  );
}

// Refresh token - longer lived
async generateRefreshToken(user: User): Promise<string> {
  return this.jwtService.sign(
    { userId: user.id, type: 'refresh' },
    { expiresIn: '7d' },
  );
}

// Token refresh endpoint
@Post('refresh')
async refresh(@Body() dto: RefreshTokenDto) {
  const payload = await this.verifyRefreshToken(dto.refreshToken);
  const user = await this.usersService.findOne(payload.userId);

  if (!user) {
    throw new UnauthorizedException('Invalid refresh token');
  }

  return {
    accessToken: await this.generateAccessToken(user),
  };
}
```

### Cookie Options Explained

```typescript
{
  httpOnly: true,    // Prevents XSS access to cookie
  secure: true,      // Only sent over HTTPS
  sameSite: 'strict', // Prevents CSRF
  maxAge: 86400000,  // 24 hours in milliseconds
  path: '/',         // Cookie path
  domain: '.example.com', // Optional: share across subdomains
}
```

### Bad example

```typescript
// ❌ Bad: Accessible via JavaScript
res.cookie('jwt', token, {
  httpOnly: false, // ❌ XSS vulnerable
});

// ❌ Bad: No expiration
const token = this.jwtService.sign({ userId: user.id }); // ❌ Never expires

// ❌ Bad: Storing token in localStorage
// Frontend: localStorage.setItem('token', token); // ❌ XSS vulnerable
```

## Anti-patterns

- Not using HttpOnly cookies
- Missing token expiration
- Storing tokens in localStorage
- Not invalidating tokens on logout
- Same site 'none' without secure flag

## Notes

- HttpOnly cookies prevent XSS token theft
- Consider refresh token rotation for better security
- Implement token blacklist for logout (Redis recommended)
- Use Clerk for production-ready auth (already integrated)
