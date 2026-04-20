---
id: backend/refactor/safe-refactorings
name: backend/refactor/safe-refactorings
kind: reference
domain: backend
topics: [refactor, safe refactorings]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Safe Refactorings (No Permission Needed)

## When to use

Use this document when:

- Refactoring without breaking changes
- Extracting utilities or constants
- Improving type safety
- Simplifying logic

## Extract Utility Functions

**Before:**

```typescript
@Injectable()
export class UsersService {
  async create(dto: CreateUserDto): Promise<User> {
    const hashedPassword = await bcrypt.hash(dto.password, 10);
    return this.prisma.user.create({
      data: { ...dto, password: hashedPassword },
    });
  }

  async updatePassword(userId: string, newPassword: string) {
    const hashedPassword = await bcrypt.hash(newPassword, 10);
    return this.prisma.user.update({
      where: { id: userId },
      data: { password: hashedPassword },
    });
  }
}
```

**After:**

```typescript
// users.util.ts
export async function hashPassword(password: string): Promise<string> {
  return bcrypt.hash(password, 10);
}

// users.service.ts
@Injectable()
export class UsersService {
  async create(dto: CreateUserDto): Promise<User> {
    const hashedPassword = await hashPassword(dto.password);
    return this.prisma.user.create({
      data: { ...dto, password: hashedPassword },
    });
  }

  async updatePassword(userId: string, newPassword: string) {
    const hashedPassword = await hashPassword(newPassword);
    return this.prisma.user.update({
      where: { id: userId },
      data: { password: hashedPassword },
    });
  }
}
```

## Improve Type Safety

**Before:**

```typescript
async findByCriteria(criteria: any): Promise<User[]> {
  return this.prisma.user.findMany({ where: criteria });
}
```

**After:**

```typescript
interface FindUserCriteria {
  email?: string;
  role?: UserRole;
  isActive?: boolean;
}

async findByCriteria(criteria: FindUserCriteria): Promise<User[]> {
  return this.prisma.user.findMany({ where: criteria });
}
```

## Extract Constants

**Before:**

```typescript
if (failedAttempts >= 5) {
  await this.lockAccount(userId, 30 * 60 * 1000);
}
```

**After:**

```typescript
// auth.constant.ts
export const MAX_FAILED_ATTEMPTS = 5;
export const ACCOUNT_LOCKOUT_DURATION_MS = 30 * 60 * 1000; // 30 minutes

// auth.service.ts
if (failedAttempts >= MAX_FAILED_ATTEMPTS) {
  await this.lockAccount(userId, ACCOUNT_LOCKOUT_DURATION_MS);
}
```

## Simplify Complex Logic

**Before:**

```typescript
async getUserStatus(userId: string): Promise<string> {
  const user = await this.prisma.user.findUnique({ where: { id: userId } });
  if (!user) {
    return 'not_found';
  }
  if (user.lockedUntil && user.lockedUntil > new Date()) {
    return 'locked';
  }
  if (!user.emailVerified) {
    return 'unverified';
  }
  if (user.role === UserRole.ADMIN) {
    return 'admin';
  }
  return 'active';
}
```

**After:**

```typescript
enum UserStatus {
  NOT_FOUND = 'not_found',
  LOCKED = 'locked',
  UNVERIFIED = 'unverified',
  ADMIN = 'admin',
  ACTIVE = 'active',
}

async getUserStatus(userId: string): Promise<UserStatus> {
  const user = await this.prisma.user.findUnique({ where: { id: userId } });

  if (!user) return UserStatus.NOT_FOUND;
  if (this.isAccountLocked(user)) return UserStatus.LOCKED;
  if (!user.emailVerified) return UserStatus.UNVERIFIED;
  if (user.role === UserRole.ADMIN) return UserStatus.ADMIN;

  return UserStatus.ACTIVE;
}

private isAccountLocked(user: User): boolean {
  return !!user.lockedUntil && user.lockedUntil > new Date();
}
```

## Rename Internal Variables

```typescript
// ✅ Safe: Rename internal variable
private async processUser(u: User) { ... }  →  private async processUser(user: User) { ... }

// ✅ Safe: Rename private method
private validateData() { ... }  →  private validateUserData() { ... }
```

## Notes

- These changes don't affect external consumers
- Always run tests after each change
- Keep commits small and focused
- Document non-obvious changes with comments
