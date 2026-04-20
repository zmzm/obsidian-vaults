---
id: backend/api/nested-resources
name: backend/api/nested-resources
kind: reference
domain: backend
topics: [api, nested resources]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Nested Resources

## When to use

Use this document when:

- Designing parent-child resource relationships
- Deciding between nested vs flat routes
- Implementing course-assignment relationships
- Handling resource ownership in URLs

## Rules

- Keep routes flat when possible
- Use nested routes for clear parent-child relationships
- Validate parent resource exists before child operations
- Keep nesting to one level maximum

## Examples

### Good example

```typescript
// Nested route for clear parent-child relationship
@Controller('courses/:courseId/assignments')
export class CourseAssignmentsController {
  constructor(private readonly assignmentsService: AssignmentsService, private readonly coursesService: CoursesService) {}

  @Get()
  async findAll(@Param('courseId') courseId: string): Promise<Assignment[]> {
    // Validate parent exists
    const course = await this.coursesService.findOne(courseId);
    if (!course) {
      throw new NotFoundException(`Course ${courseId} not found`);
    }

    return this.assignmentsService.findByCourse(courseId);
  }

  @Post()
  async create(@Param('courseId') courseId: string, @Body() dto: CreateAssignmentDto): Promise<Assignment> {
    const course = await this.coursesService.findOne(courseId);
    if (!course) {
      throw new NotFoundException(`Course ${courseId} not found`);
    }

    return this.assignmentsService.create(courseId, dto);
  }
}

// Flat route when resource is standalone
@Controller('assignments')
export class AssignmentsController {
  @Get(':id')
  async findOne(@Param('id') id: string): Promise<Assignment> {
    return this.assignmentsService.findOne(id);
  }

  @Delete(':id')
  async remove(@Param('id') id: string): Promise<void> {
    return this.assignmentsService.remove(id);
  }
}
```

### When to Use Nested Routes

| Route                           | Use Case                      |
| ------------------------------- | ----------------------------- |
| `GET /courses/:id/assignments`  | List assignments for a course |
| `POST /courses/:id/assignments` | Create assignment in a course |
| `GET /users/:id/enrollments`    | List user's enrollments       |

### When to Use Flat Routes

| Route                     | Use Case              |
| ------------------------- | --------------------- |
| `GET /assignments/:id`    | Get single assignment |
| `PATCH /assignments/:id`  | Update assignment     |
| `DELETE /assignments/:id` | Delete assignment     |

### Bad example

```typescript
// ❌ Bad: Too deeply nested
@Controller('courses/:courseId/assignments/:assignmentId/submissions')
export class SubmissionsController {
  // Avoid nesting more than one level
}

// ❌ Bad: Not validating parent resource
@Post()
async create(
  @Param('courseId') courseId: string,
  @Body() dto: CreateAssignmentDto,
) {
  // ❌ Not checking if course exists
  return this.assignmentsService.create(courseId, dto);
}
```

## Anti-patterns

- Nesting more than one level deep
- Not validating parent resource exists
- Using nested routes when flat would be clearer
- Inconsistent routing patterns

## Notes

- Prefer flat routes for operations on individual resources
- Use nested routes when filtering by parent is the primary use case
- Always validate parent resource exists before child operations
