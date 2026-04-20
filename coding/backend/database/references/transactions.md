---
id: backend/database/transactions
name: backend/database/transactions
kind: reference
domain: backend
topics: [database, transactions]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Transactions

## When to use

Use this document when:

- Performing multi-step database operations
- Ensuring data consistency
- Rolling back on failure
- Handling related entity updates

## Rules

- Use transactions for multi-step operations
- All operations succeed or all fail
- Keep transactions short
- Handle errors appropriately

## Examples

### Good example

```typescript
// ✅ Good: Use transaction for related operations
async enrollUserInCourse(userId: string, courseId: string) {
  return this.prisma.$transaction(async (tx) => {
    // Check if course exists
    const course = await tx.course.findUnique({ where: { id: courseId } });
    if (!course) {
      throw new NotFoundException('Course not found');
    }

    // Check if already enrolled
    const existing = await tx.enrollment.findUnique({
      where: {
        userId_courseId: { userId, courseId },
      },
    });
    if (existing) {
      throw new ConflictException('Already enrolled');
    }

    // Create enrollment
    const enrollment = await tx.enrollment.create({
      data: { userId, courseId },
    });

    // Update course enrollment count
    await tx.course.update({
      where: { id: courseId },
      data: {
        enrollmentCount: { increment: 1 },
      },
    });

    return enrollment;
  });
}
```

### Transaction with multiple creates

```typescript
async createCourseWithAssignments(
  courseData: CreateCourseDto,
  assignments: CreateAssignmentDto[],
) {
  return this.prisma.$transaction(async (tx) => {
    // Create course
    const course = await tx.course.create({
      data: courseData,
    });

    // Create all assignments
    await tx.assignment.createMany({
      data: assignments.map((a) => ({
        ...a,
        courseId: course.id,
      })),
    });

    // Return course with assignments
    return tx.course.findUnique({
      where: { id: course.id },
      include: { assignments: true },
    });
  });
}
```

### Transaction options

```typescript
// With timeout and isolation level
await this.prisma.$transaction(
  async tx => {
    // operations
  },
  {
    maxWait: 5000, // max time to acquire connection
    timeout: 10000, // max time for transaction
    isolationLevel: 'Serializable',
  },
);
```

### Bad example

```typescript
// ❌ Bad: No transaction for related operations
async enrollUserInCourse(userId: string, courseId: string) {
  // If this fails after enrollment is created, count is wrong
  const enrollment = await this.prisma.enrollment.create({
    data: { userId, courseId },
  });

  await this.prisma.course.update({
    where: { id: courseId },
    data: { enrollmentCount: { increment: 1 } },
  });

  return enrollment;
}
```

## When to Use Transactions

- Creating related records
- Updating multiple records that depend on each other
- Operations that must all succeed or all fail
- Read-then-write operations (check then create)

## Anti-patterns

- Long-running transactions (keep them short)
- Not using transactions for related operations
- Ignoring transaction failures
- Too many operations in single transaction

## Notes

- Transactions use `tx` parameter for all operations inside
- If any operation throws, all changes are rolled back
- Use appropriate isolation level for your use case
