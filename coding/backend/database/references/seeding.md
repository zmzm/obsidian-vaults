---
id: backend/database/seeding
name: backend/database/seeding
kind: reference
domain: backend
topics: [database, seeding]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Database Seeding

## When to use

Use this document when:

- Setting up development data
- Creating test fixtures
- Populating initial reference data
- Resetting development database

## Rules

- Use upsert for idempotent seeds
- Separate seed data by environment
- Hash passwords in seed data
- Keep seeds maintainable

## Examples

### Good example

```typescript
// libs/db/prisma/seed.ts
import { PrismaClient, UserRole, CourseDifficulty } from '@prisma/client';
import * as bcrypt from 'bcrypt';

const prisma = new PrismaClient();

async function main() {
  console.log('Starting seed...');

  // Create admin user (upsert for idempotency)
  const adminPassword = await bcrypt.hash('admin123', 10);
  const admin = await prisma.user.upsert({
    where: { email: 'admin@mentory.com' },
    update: {},
    create: {
      email: 'admin@mentory.com',
      password: adminPassword,
      role: UserRole.ADMIN,
    },
  });
  console.log(`Created admin: ${admin.email}`);

  // Create mentor
  const mentorPassword = await bcrypt.hash('mentor123', 10);
  const mentor = await prisma.user.upsert({
    where: { email: 'mentor@mentory.com' },
    update: {},
    create: {
      email: 'mentor@mentory.com',
      password: mentorPassword,
      role: UserRole.MENTOR,
    },
  });
  console.log(`Created mentor: ${mentor.email}`);

  // Create sample courses
  const courses = [
    {
      title: 'Introduction to JavaScript',
      description: 'Learn the basics of JavaScript programming',
      difficulty: CourseDifficulty.BEGINNER,
      mentorId: mentor.id,
    },
    {
      title: 'Advanced TypeScript',
      description: 'Master TypeScript for enterprise applications',
      difficulty: CourseDifficulty.ADVANCED,
      mentorId: mentor.id,
    },
  ];

  for (const courseData of courses) {
    const course = await prisma.course.upsert({
      where: { title: courseData.title },
      update: {},
      create: courseData,
    });
    console.log(`Created course: ${course.title}`);
  }

  console.log('Seeding completed!');
}

main()
  .catch(e => {
    console.error('Seed failed:', e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
```

### Running seeds

```bash
# Run seed
pnpm nx run db:seed

# Reset and reseed
pnpm nx run db:reset
```

### Environment-specific seeds

```typescript
async function main() {
  // Always seed reference data
  await seedRoles();
  await seedCategories();

  // Only seed test data in development
  if (process.env.NODE_ENV !== 'production') {
    await seedTestUsers();
    await seedTestCourses();
  }
}
```

### Bad example

```typescript
// ❌ Bad: Not using upsert (fails on re-run)
await prisma.user.create({
  data: { email: 'admin@mentory.com' },
});

// ❌ Bad: Plain text password
await prisma.user.create({
  data: {
    email: 'admin@mentory.com',
    password: 'admin123', // ❌ Not hashed!
  },
});

// ❌ Bad: No error handling
async function main() {
  await seedUsers();
  await seedCourses();
  // No .catch() or .finally()
}
```

## Anti-patterns

- Using create instead of upsert
- Plain text passwords in seeds
- No error handling
- Seeding production data to development
- Hard-coded IDs that may conflict

## Notes

- Use upsert to make seeds idempotent (can run multiple times)
- Always hash passwords
- Use transactions for related seed data
- Keep seed data minimal but useful
