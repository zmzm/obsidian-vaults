---
id: backend/refactor/anti-patterns
name: backend/refactor/anti-patterns
kind: reference
domain: backend
topics: [refactor, anti patterns]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Anti-Patterns to Fix

## When to use

Use this document when:

- Reviewing code for quality issues
- Identifying common problems
- Refactoring legacy code
- Improving code maintainability

## God Classes

**Problem:**

```typescript
@Injectable()
export class UsersService {
  // 50+ methods doing everything
  async create() { ... }
  async sendEmail() { ... }
  async generateReport() { ... }
  async processPayment() { ... }
  async updateNotifications() { ... }
  // ... many more
}
```

**Solution:**

```typescript
// Split into focused services
@Injectable()
export class UsersService {
  async create() { ... }
  async findOne() { ... }
  async update() { ... }
}

@Injectable()
export class EmailService {
  async sendWelcomeEmail() { ... }
  async sendPasswordReset() { ... }
}

@Injectable()
export class ReportService {
  async generateUserReport() { ... }
}
```

## Swallowing Errors

**Problem:**

```typescript
async create(dto: CreateUserDto) {
  try {
    return await this.prisma.user.create({ data: dto });
  } catch {
    return null; // ❌ Swallowing error
  }
}
```

**Solution:**

```typescript
async create(dto: CreateUserDto): Promise<User> {
  // Let NestJS exception filters handle Prisma errors
  return this.prisma.user.create({ data: dto });
}
```

## Magic Numbers

**Problem:**

```typescript
if (age < 18) { ... }
if (price > 1000) { ... }
if (attempts >= 5) { ... }
```

**Solution:**

```typescript
const MIN_AGE = 18;
const PREMIUM_PRICE_THRESHOLD = 1000;
const MAX_LOGIN_ATTEMPTS = 5;

if (age < MIN_AGE) { ... }
if (price > PREMIUM_PRICE_THRESHOLD) { ... }
if (attempts >= MAX_LOGIN_ATTEMPTS) { ... }
```

## Using `any` Type

**Problem:**

```typescript
async processData(data: any): Promise<any> {
  return data.something;
}
```

**Solution:**

```typescript
interface ProcessedData {
  result: string;
  timestamp: Date;
}

async processData(data: InputData): Promise<ProcessedData> {
  return {
    result: data.value,
    timestamp: new Date(),
  };
}
```

## Long Methods

**Problem:**

```typescript
async processOrder(orderId: string) {
  // 100+ lines doing multiple things
  // validation
  // ...
  // inventory check
  // ...
  // payment processing
  // ...
  // email notification
  // ...
}
```

**Solution:**

```typescript
async processOrder(orderId: string) {
  await this.validateOrder(orderId);
  await this.checkInventory(orderId);
  await this.processPayment(orderId);
  await this.sendConfirmation(orderId);
}

private async validateOrder(orderId: string) { ... }
private async checkInventory(orderId: string) { ... }
private async processPayment(orderId: string) { ... }
private async sendConfirmation(orderId: string) { ... }
```

## Nested Conditionals

**Problem:**

```typescript
if (user) {
  if (user.isActive) {
    if (user.role === 'ADMIN') {
      if (user.permissions.includes('DELETE')) {
        // do something
      }
    }
  }
}
```

**Solution:**

```typescript
if (!user) return;
if (!user.isActive) return;
if (user.role !== 'ADMIN') return;
if (!user.permissions.includes('DELETE')) return;

// do something
```

## Best Practices

1. **Refactor in small steps** - One change at a time
2. **Run tests after each change** - Ensure nothing breaks
3. **Commit frequently** - Small, focused commits
4. **Document non-obvious changes** - Add comments for complex logic
5. **Seek review for large refactors** - Get feedback early

## Notes

- Keep methods under 50 lines
- Each class should have a single responsibility
- Extract repeated code into utilities
- Use descriptive names for variables and methods
