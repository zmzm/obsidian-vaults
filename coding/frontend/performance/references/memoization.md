---
id: frontend/performance/memoization
name: frontend/performance/memoization
kind: reference
domain: frontend
topics: [performance, memoization]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Memoization (React.memo, useMemo, useCallback)

## When to use

Use this document when:

- Optimizing expensive computations
- Creating stable callback references
- Preventing unnecessary component re-renders
- Memoizing values used in dependencies

## Rules

- **Profile before optimizing** - Verify benefit before adding memoization
- Use `React.memo` for components that receive same props frequently
- Use `useMemo` for expensive calculations (filtering, sorting, transformations)
- Use `useCallback` for callbacks passed to memoized components
- Use `useCallback` for callbacks used in dependency arrays
- Don't use for simple computations (overhead > benefit)
- Include all dependencies in dependency arrays

## Examples

### React.memo

```typescript
// ✅ Good: Memoize component that receives stable props
import { memo } from 'react';

interface CourseCardProps {
  course: Course;
  onEnroll: (courseId: string) => void;
}

export const CourseCard = memo<CourseCardProps>(({ course, onEnroll }) => {
  return (
    <Card>
      <CardTitle>{course.title}</CardTitle>
      <Button onClick={() => onEnroll(course.id)}>{t('enroll')}</Button>
    </Card>
  );
});

// ✅ Good: Custom comparison for complex props
export const CourseCard = memo<CourseCardProps>(
  ({ course, onEnroll }) => {
    // Component implementation
  },
  (prevProps, nextProps) => {
    // Return true if props are equal (skip re-render)
    return prevProps.course.id === nextProps.course.id;
  },
);

// ❌ Bad: Memoizing component that changes frequently
export const SearchInput = memo(({ value, onChange }) => {
  // value changes on every keystroke, memo adds overhead
});

// ❌ Bad: Memoizing cheap component
export const SimpleLabel = memo(({ text }) => {
  return <label>{text}</label>; // Too simple, overhead > benefit
});
```

### useMemo

```typescript
// ✅ Good: Memoize expensive computation
export const CoursesList: React.FC = () => {
  const { courses } = useCourses();
  const [filter, setFilter] = useState('');

  const filteredCourses = useMemo(() => {
    return courses.filter(course => course.title.toLowerCase().includes(filter.toLowerCase()));
  }, [courses, filter]);

  return (
    <>
      <Input value={filter} onChange={e => setFilter(e.target.value)} />
      {filteredCourses.map(course => (
        <CourseCard key={course.id} course={course} />
      ))}
    </>
  );
};

// ❌ Bad: Memoizing simple computation
const sum = useMemo(() => a + b, [a, b]); // Too simple, overhead > benefit
```

### useCallback

```typescript
// ✅ Good: Memoize callbacks for memoized components
const handleEnroll = useCallback(
  (courseId: string) => {
    enrollInCourse(courseId);
  },
  [enrollInCourse]
);

// Pass to memoized component
<CourseCard course={course} onEnroll={handleEnroll} />

// ❌ Bad: Inline function breaks memo
<CourseCard
  course={course}
  onEnroll={(id) => enrollInCourse(id)} // New function every render
/>
```

## When to Use

### React.memo

| Use When                                       | Avoid When                                   |
| ---------------------------------------------- | -------------------------------------------- |
| Component receives same props frequently       | Props change frequently                      |
| Component is expensive to render               | Component is cheap to render                 |
| Component is in a list that re-renders often   | Adding memo adds more overhead than it saves |
| Parent re-renders but child props don't change | Premature optimization                       |

### useMemo

| Use When                                         | Avoid When                           |
| ------------------------------------------------ | ------------------------------------ |
| Expensive calculations (filter, sort, transform) | Simple computations                  |
| Creating objects used in dependency arrays       | Values that change frequently anyway |
| Heavy data transformations                       | Premature optimization               |

### useCallback

| Use When                                | Avoid When                       |
| --------------------------------------- | -------------------------------- |
| Callbacks passed to memoized components | Callbacks that change frequently |
| Callbacks used in dependency arrays     | Functions not passed to children |
| Event handlers for memoized children    | Premature optimization           |

## Anti-patterns

- Memoizing everything without measurement
- Using memo for components with frequently changing props
- Using useMemo/useCallback for simple operations
- Missing dependencies in dependency arrays
- Premature optimization without profiling
- Inline functions when passing to memo'd components

## Notes

### Profiling First

Always profile before adding memoization:

1. Use React DevTools Profiler
2. Identify components that re-render unnecessarily
3. Add memoization where it provides measurable benefit
4. Re-profile to verify improvement

### Dependency Arrays

```typescript
// Include ALL dependencies
const callback = useCallback(() => {
  doSomething(a, b);
}, [a, b]); // Both a and b must be included

// useMemo same pattern
const value = useMemo(() => {
  return compute(x, y);
}, [x, y]); // Both x and y must be included
```
