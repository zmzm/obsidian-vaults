---
id: frontend/i18n/pluralization
name: frontend/i18n/pluralization
kind: reference
domain: frontend
topics: [i18n, pluralization]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Pluralization

## When to use

Use this document when:

- Handling plural forms in translations
- Displaying counts with proper grammar
- Supporting multiple languages with different plural rules
- Creating messages that depend on quantity

## Rules

- Use `_one`, `_other` suffixes for English
- Use `_zero`, `_one`, `_few`, `_many`, `_other` for Polish
- Always include `{{count}}` in pluralization keys
- Use `_zero` suffix for zero counts when needed
- Follow language-specific plural rules

## Examples

### Good example

```typescript
// Locale file
export const courseLocales = {
  enrollmentCount_one: '{{count}} student enrolled',
  enrollmentCount_other: '{{count}} students enrolled',

  assignmentCount_zero: 'No assignments',
  assignmentCount_one: '1 assignment',
  assignmentCount_other: '{{count}} assignments',
};

// Component
const { t } = useTranslation('courses');

<p>{t('enrollmentCount', { count: students.length })}</p>
<p>{t('assignmentCount', { count: assignments.length })}</p>

// Polish Pluralization
// pl/courses.locales.ts
export const courseLocales = {
  enrollmentCount_zero: 'Brak studentów',
  enrollmentCount_one: '{{count}} student',
  enrollmentCount_few: '{{count}} studentów',
  enrollmentCount_many: '{{count}} studentów',
  enrollmentCount_other: '{{count}} studentów',
};
```

### Bad example

```typescript
// ❌ Bad: Not using pluralization
<p>{count} student{count !== 1 ? 's' : ''} enrolled</p>

// ❌ Bad: Missing count in key
enrollmentCount_one: 'One student enrolled', // Should include {{count}}

// ❌ Bad: Not following language rules
// Using English rules for Polish
enrollmentCount_one: '{{count}} student', // Polish needs _few, _many
```

## Anti-patterns

- Not using pluralization suffixes
- Manually handling plural forms in components
- Missing `{{count}}` in pluralization keys
- Not following language-specific plural rules
- Using wrong plural suffixes for language

## Notes

### Plural Rules

**English:**

- `_one` - When count is 1
- `_other` - When count is 0, 2, or more

**Polish:**

- `_zero` - When count is 0
- `_one` - When count is 1
- `_few` - When count is 2-4, 22-24, etc.
- `_many` - When count is 5-21, 25-31, etc.
- `_other` - Other cases

### Suffix Rules

- Always include `{{count}}` in translation strings
- Use `_zero` suffix for zero counts when you want special message
- React-i18next automatically selects correct plural form based on count
- Pass `count` in interpolation object: `t('key', { count: number })`

### Output Examples

- `count: 0` → "No assignments" (if `_zero` exists) or uses `_other`
- `count: 1` → "1 assignment" (uses `_one`)
- `count: 5` → "5 assignments" (uses `_other`)
