---
id: frontend/hook/composition
name: frontend/hook/composition
kind: reference
domain: frontend
topics: [hook, composition]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Hooks Composition

## When to use

Use this document when:

- Composing multiple hooks for complex functionality
- Combining data fetching with mutations
- Building higher-level hooks from simpler ones
- Managing related state across multiple hooks

## Rules

- Compose hooks to build complex functionality
- Keep composed hooks focused on single responsibility
- Return consistent interfaces from composed hooks
- Handle loading states from multiple hooks
- Combine related hooks logically

## Examples

### Good example

```typescript
// Composing multiple hooks
export const useCourseManagement = (courseId: string) => {
  const { course, isLoading } = useCourse(courseId);
  const { updateCourse, isPending: isUpdating } = useUpdateCourse();
  const { deleteCourse, isPending: isDeleting } = useDeleteCourse();
  const deleteDialog = useDialog();

  const handleUpdate = (data: UpdateCourseDto) => {
    updateCourse({ id: courseId, data });
  };

  const handleDelete = () => {
    deleteCourse(courseId, {
      onSuccess: () => {
        deleteDialog.close();
        navigate('/courses');
      },
    });
  };

  return {
    course,
    isLoading,
    isUpdating,
    isDeleting,
    handleUpdate,
    handleDelete,
    deleteDialog,
  };
};

// Combining Data and Mutations
export const useUserProfileManagement = () => {
  const { user, isLoading } = useUserProfile();
  const { updateProfile, isPending } = useUpdateProfile();
  const { uploadAvatar } = useUploadAvatar();

  return {
    user,
    isLoading,
    updateProfile,
    uploadAvatar,
    isUpdating: isPending,
  };
};
```

### Bad example

```typescript
// ❌ Bad: Mixing unrelated concerns
export const useCourseManagement = (courseId: string) => {
  const { course } = useCourse(courseId);
  const [sidebarOpen, setSidebarOpen] = useState(false); // Unrelated concern
  return { course, sidebarOpen, setSidebarOpen };
};

// ❌ Bad: Not handling loading states
export const useCourseManagement = (courseId: string) => {
  const { course } = useCourse(courseId);
  const { updateCourse } = useUpdateCourse();
  // Missing isLoading, isPending states
  return { course, updateCourse };
};
```

## Anti-patterns

- Mixing unrelated concerns in composed hooks
- Not handling loading states from multiple hooks
- Creating overly complex composed hooks
- Not returning consistent interfaces
- Duplicating logic instead of composing

## Notes

- Compose hooks to build higher-level functionality
- Keep composed hooks focused - they should still have single responsibility
- Handle loading states from all composed hooks
- Return consistent interfaces for easy component usage
- Test composed hooks by testing their individual parts
- Place composed hooks in feature directories, not shared

### Testing Hooks

```typescript
import { renderHook, act } from '@testing-library/react';

describe('useCounter', () => {
  it('should increment counter', () => {
    const { result } = renderHook(() => useCounter());
    expect(result.current.count).toBe(0);
    act(() => {
      result.current.increment();
    });
    expect(result.current.count).toBe(1);
  });
});
```
