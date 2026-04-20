---
id: backend/security/http-headers
name: backend/security/http-headers
kind: reference
domain: backend
topics: [security, http headers]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# HTTP Security Headers

## When to use

Use this document when:

- Configuring security headers
- Setting up Helmet middleware
- Implementing Content Security Policy
- Configuring CORS properly

## Rules

- Use Helmet for security headers
- Configure Content Security Policy
- Set proper CORS origins
- Enable HTTPS in production

## Examples

### Good example

```typescript
// Install: pnpm add helmet

// main.ts
import helmet from 'helmet';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // Helmet for security headers
  app.use(
    helmet({
      contentSecurityPolicy: {
        directives: {
          defaultSrc: ["'self'"],
          styleSrc: ["'self'", "'unsafe-inline'"],
          scriptSrc: ["'self'"],
          imgSrc: ["'self'", 'data:', 'https:'],
        },
      },
    }),
  );

  // CORS configuration
  app.enableCors({
    origin: process.env.FRONTEND_URL,
    credentials: true,
    methods: ['GET', 'POST', 'PATCH', 'DELETE'],
    allowedHeaders: ['Content-Type', 'Authorization'],
  });

  await app.listen(3000);
}
```

### Headers Set by Helmet

| Header                    | Purpose                          |
| ------------------------- | -------------------------------- |
| X-Content-Type-Options    | Prevents MIME type sniffing      |
| X-Frame-Options           | Prevents clickjacking            |
| X-XSS-Protection          | XSS protection (legacy browsers) |
| Strict-Transport-Security | Forces HTTPS                     |
| Content-Security-Policy   | Controls resource loading        |

### CORS Configuration

```typescript
// Development
app.enableCors({
  origin: ['http://localhost:4200'],
  credentials: true,
});

// Production
app.enableCors({
  origin: process.env.FRONTEND_URL, // Single trusted origin
  credentials: true,
  methods: ['GET', 'POST', 'PATCH', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
});

// ❌ Bad: Allow all origins
app.enableCors(); // Security risk!
```

### Bad example

```typescript
// ❌ Bad: No helmet
// Missing security headers

// ❌ Bad: Allow all origins
app.enableCors({
  origin: '*', // Security risk!
});

// ❌ Bad: Overly permissive CSP
helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'", '*'], // ❌ Too permissive
      scriptSrc: ["'unsafe-inline'", "'unsafe-eval'"], // ❌ Dangerous
    },
  },
});
```

## Anti-patterns

- Not using Helmet
- Allowing all CORS origins
- Overly permissive CSP
- Missing HTTPS in production
- Disabling security headers for convenience

## Notes

- Helmet sets multiple security headers automatically
- CSP should be as restrictive as possible
- Test CSP in report-only mode first
- CORS only allows specified origins
