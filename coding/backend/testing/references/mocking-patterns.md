---
id: backend/testing/mocking-patterns
name: backend/testing/mocking-patterns
kind: reference
domain: backend
topics: [testing, mocking patterns]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Common Mocking Patterns

## When to use

Use this document when:

- Setting up mocks for tests
- Mocking Prisma database calls
- Mocking external services
- Mocking environment variables

## Mock PrismaService

```typescript
import { mockDeep, DeepMockProxy } from 'jest-mock-extended';
import { PrismaClient } from '@prisma/client';

let prisma: DeepMockProxy<PrismaClient>;

beforeEach(async () => {
  const module = await Test.createTestingModule({
    providers: [
      YourService,
      {
        provide: PrismaService,
        useValue: mockDeep<PrismaClient>(),
      },
    ],
  }).compile();

  prisma = module.get(PrismaService);
});

// Usage in tests
prisma.user.findUnique.mockResolvedValue(mockUser);
prisma.user.create.mockResolvedValue(createdUser);
prisma.user.findMany.mockResolvedValue([user1, user2]);
prisma.$transaction.mockImplementation(fn => fn(prisma));
```

## Mock External Services

```typescript
// Email service mock
const mockEmailService = {
  send: jest.fn().mockResolvedValue(true),
  sendTemplate: jest.fn().mockResolvedValue(true),
};

// HTTP service mock
const mockHttpService = {
  get: jest.fn().mockReturnValue(of({ data: mockResponse })),
  post: jest.fn().mockReturnValue(of({ data: mockResponse })),
};

// Usage in module
providers: [
  {
    provide: EmailService,
    useValue: mockEmailService,
  },
  {
    provide: HttpService,
    useValue: mockHttpService,
  },
];
```

## Mock Guards

```typescript
// Override guards in test module
const module = await Test.createTestingModule({
  controllers: [UsersController],
  providers: [UsersService],
})
  .overrideGuard(JwtAuthGuard)
  .useValue({ canActivate: jest.fn(() => true) })
  .overrideGuard(RolesGuard)
  .useValue({ canActivate: jest.fn(() => true) })
  .compile();

// Mock guard to reject
.overrideGuard(JwtAuthGuard)
.useValue({ canActivate: jest.fn(() => false) })
```

## Mock Environment Variables

```typescript
// Set before tests
beforeEach(() => {
  process.env.JWT_SECRET = 'test-secret';
  process.env.DATABASE_URL = 'postgresql://test';
});

// Clean up after tests
afterEach(() => {
  delete process.env.JWT_SECRET;
  delete process.env.DATABASE_URL;
});

// Or use ConfigService mock
const mockConfigService = {
  get: jest.fn((key: string) => {
    const config = {
      JWT_SECRET: 'test-secret',
      JWT_EXPIRES_IN: 3600,
    };
    return config[key];
  }),
};
```

## Mock Request/Response

```typescript
// Mock Express Request
const mockRequest = {
  user: { id: '1', role: UserRole.ADMIN },
  params: { id: '1' },
  body: createUserDto,
} as unknown as Request;

// Mock Express Response
const mockResponse = {
  status: jest.fn().mockReturnThis(),
  json: jest.fn().mockReturnThis(),
  cookie: jest.fn().mockReturnThis(),
  clearCookie: jest.fn().mockReturnThis(),
} as unknown as Response;
```

## Mock Date/Time

```typescript
beforeEach(() => {
  jest.useFakeTimers();
  jest.setSystemTime(new Date('2025-01-05T12:00:00Z'));
});

afterEach(() => {
  jest.useRealTimers();
});
```

## Spying on Methods

```typescript
// Spy on service method
const createSpy = jest.spyOn(service, 'create').mockResolvedValue(mockUser);

// Verify call
expect(createSpy).toHaveBeenCalledWith(createDto);
expect(createSpy).toHaveBeenCalledTimes(1);

// Restore original implementation
createSpy.mockRestore();
```

## Reset Mocks

```typescript
afterEach(() => {
  jest.clearAllMocks(); // Clear call history, keep implementation
  // OR
  jest.resetAllMocks(); // Reset to undefined, remove implementation
  // OR
  jest.restoreAllMocks(); // Restore original implementation (for spies)
});
```

## Anti-patterns

- Not clearing mocks between tests
- Over-mocking (mocking what you're testing)
- Missing mock for async operations
- Not restoring original implementations

## Notes

- Use `mockDeep` from jest-mock-extended for Prisma
- Always clear mocks in afterEach
- Mock at the boundary (services, external APIs)
- Don't mock the unit under test
