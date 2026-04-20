---
id: frontend/performance/bundle-optimization
name: frontend/performance/bundle-optimization
kind: reference
domain: frontend
topics: [performance, bundle optimization]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Bundle Size Optimization

## When to use

Use this document when:

- Reducing initial bundle size
- Implementing code splitting
- Optimizing build output
- Analyzing bundle composition

## Rules

- Import only what you need (tree shaking)
- Use dynamic imports for large dependencies
- Lazy load routes and heavy components
- Split vendor bundles
- Monitor bundle size in CI/CD

## Examples

### Good example

```typescript
// ✅ Good: Import only what you need
import { format } from 'date-fns';
import { Button } from '@mentory/ui-components';

// ✅ Good: Lazy load routes
const DashboardPage = lazy(() => import('./features/dashboard/DashboardPage'));

// ✅ Good: Lazy load heavy components
const Chart = lazy(() => import('./components/Chart'));

// ✅ Good: Dynamic imports for libraries
const loadChartLibrary = async () => {
  const { Chart } = await import('chart.js');
  return Chart;
};
```

### Bad example

```typescript
// ❌ Bad: Import entire library
import * as dateFns from 'date-fns';

// ❌ Bad: Not code splitting routes
import DashboardPage from './features/dashboard/DashboardPage';

// ❌ Bad: Importing heavy library upfront
import { Chart } from 'chart.js'; // Should be dynamic import
```

## Anti-patterns

- Importing entire libraries instead of specific exports
- Not code splitting routes
- Not using dynamic imports for large dependencies
- Not monitoring bundle size
- Including unused dependencies

## Notes

### Tree Shaking

- Import only what you need: `import { format } from 'date-fns'`
- Avoid namespace imports: `import * as lib from 'lib'`
- Use ES modules for better tree shaking
- Configure bundler for tree shaking

### Code Splitting

- Lazy load routes with `React.lazy()`
- Lazy load heavy components
- Use Suspense for loading states
- Split vendor bundles from app code

### Dynamic Imports

- Load libraries only when needed
- Use for heavy dependencies (charts, editors)
- Reduces initial bundle size
- Improves initial load time

### Analyze Bundle

```bash
# Use build analyzer
npm run build -- --analyze

# Check bundle size
npm run build
```

### Best Practices

- Use dynamic imports for large dependencies
- Split vendor bundles
- Remove unused dependencies
- Monitor bundle size in CI/CD
- Set bundle size budgets
