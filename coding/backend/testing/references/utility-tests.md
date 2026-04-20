---
id: backend/testing/utility-tests
name: backend/testing/utility-tests
kind: reference
domain: backend
topics: [testing, utility tests]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Utility/Helper Tests

## When to use

Use this document when:

- Testing pure utility functions
- Testing helper functions
- Verifying edge cases and boundary conditions
- Testing transformations

## Rules

- Test pure functions with various inputs
- Include edge cases and boundary conditions
- Test error scenarios
- Keep tests simple and focused

## Examples

### Good example

```typescript
import { formatUserName, calculateAge, validateEmail } from './user.util';

describe('formatUserName', () => {
  it('should format full name correctly', () => {
    expect(formatUserName('john', 'doe')).toBe('John Doe');
  });

  it('should handle empty strings', () => {
    expect(formatUserName('', '')).toBe('');
  });

  it('should handle null values', () => {
    expect(formatUserName(null, null)).toBe('');
  });

  it('should handle single name', () => {
    expect(formatUserName('john', '')).toBe('John');
    expect(formatUserName('', 'doe')).toBe('Doe');
  });

  it('should trim whitespace', () => {
    expect(formatUserName('  john  ', '  doe  ')).toBe('John Doe');
  });
});

describe('calculateAge', () => {
  beforeEach(() => {
    // Mock current date for consistent tests
    jest.useFakeTimers();
    jest.setSystemTime(new Date('2025-01-05'));
  });

  afterEach(() => {
    jest.useRealTimers();
  });

  it('should calculate age correctly', () => {
    const birthDate = new Date('2000-01-05');
    expect(calculateAge(birthDate)).toBe(25);
  });

  it('should handle birthday not yet occurred this year', () => {
    const birthDate = new Date('2000-06-15');
    expect(calculateAge(birthDate)).toBe(24);
  });

  it('should return 0 for future dates', () => {
    const birthDate = new Date('2030-01-01');
    expect(calculateAge(birthDate)).toBe(0);
  });
});

describe('validateEmail', () => {
  it.each([
    ['test@example.com', true],
    ['user.name@domain.co.uk', true],
    ['invalid-email', false],
    ['@domain.com', false],
    ['user@', false],
    ['', false],
  ])('should validate %s as %s', (email, expected) => {
    expect(validateEmail(email)).toBe(expected);
  });
});
```

### Testing Error Cases

```typescript
describe('parseConfig', () => {
  it('should throw on invalid JSON', () => {
    expect(() => parseConfig('invalid json')).toThrow('Invalid JSON');
  });

  it('should throw on missing required fields', () => {
    expect(() => parseConfig('{}')).toThrow('Missing required field: name');
  });
});
```

### Testing Async Utilities

```typescript
describe('fetchWithRetry', () => {
  it('should retry on failure', async () => {
    const mockFetch = jest
      .fn()
      .mockRejectedValueOnce(new Error('Network error'))
      .mockRejectedValueOnce(new Error('Network error'))
      .mockResolvedValue({ data: 'success' });

    const result = await fetchWithRetry(mockFetch, 3);

    expect(result).toEqual({ data: 'success' });
    expect(mockFetch).toHaveBeenCalledTimes(3);
  });

  it('should throw after max retries', async () => {
    const mockFetch = jest.fn().mockRejectedValue(new Error('Network error'));

    await expect(fetchWithRetry(mockFetch, 3)).rejects.toThrow('Network error');
    expect(mockFetch).toHaveBeenCalledTimes(3);
  });
});
```

## Anti-patterns

- Missing edge case tests
- Not testing error scenarios
- Hardcoding dates without mocking
- Complex test setup for simple functions

## Notes

- Use `it.each` for parameterized tests
- Mock dates with `jest.useFakeTimers()`
- Keep utility tests simple and fast
- Test boundary conditions (empty, null, max values)
