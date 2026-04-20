# Frontend Skills Index

Quick reference for selecting the right skill.

## Skill Selection Guide

| You're working on...                   | Use skill        |
| -------------------------------------- | ---------------- |
| Components in `apps/*/src/`            | `ui`             |
| Components in `libs/ui-components/`    | `chakra-ui`      |
| Test files (`*.spec.tsx`)              | `testing`        |
| Custom hooks (`*.hook.ts`)             | `hook`           |
| useQuery, useMutation, cache           | `react-query`    |
| Translations, t() function             | `i18n`           |
| ARIA, keyboard nav, screen readers     | `accessibility`  |
| Bundle size, re-renders, memoization   | `performance`    |
| General React patterns, file structure | `coding`         |
| Routes, navigation, useNavigate        | `routing`        |
| useAuth, Clerk, login/logout           | `auth`           |
| ErrorBoundary, toast errors, try/catch | `error-handling` |

## Decision Trees

### UI Work

```
Working with UI components?
├── In libs/ui-components/? → chakra-ui
└── In apps/*? → ui
```

### Hooks

```
Creating or modifying a hook?
├── Uses useQuery/useMutation? → react-query (for RQ-specific patterns)
└── Hook structure, naming, returns? → hook
```

### Testing

```
Writing tests?
├── Accessibility testing (jest-axe)? → accessibility
└── Component/integration tests? → testing
```

### Auth & Routing

```
Working with auth or navigation?
├── useAuth, login/logout, user data? → auth
├── Routes, guards, useNavigate? → routing
└── Both auth state AND route guards? → routing (references auth)
```

### Error Handling

```
Handling errors?
├── Unexpected render errors? → error-handling (ErrorBoundary)
├── API failures, user feedback? → error-handling (toast)
└── Form validation errors? → ui (forms)
```

## Skill Summaries

| Skill            | Purpose                                            |
| ---------------- | -------------------------------------------------- |
| `accessibility`  | WCAG compliance, ARIA, keyboard navigation         |
| `auth`           | Clerk integration, useAuth hook, login/logout      |
| `chakra-ui`      | Theme tokens, recipes, component wrappers in libs/ |
| `coding`         | React patterns, file structure, TypeScript         |
| `error-handling` | ErrorBoundary, toast notifications, API errors     |
| `hook`           | Custom hook design, naming, return interfaces      |
| `i18n`           | react-i18next, translations, pluralization         |
| `performance`    | Memoization, code splitting, bundle optimization   |
| `react-query`    | Server state, queries, mutations, caching          |
| `routing`        | React Router, route guards, navigation             |
| `testing`        | RTL, MSW, Jest, test patterns                      |
| `ui`             | @mentory/ui-components usage in apps/              |

## Common Mistakes

| Wrong                              | Right                | Why                                                 |
| ---------------------------------- | -------------------- | --------------------------------------------------- |
| Use `chakra-ui` in apps/           | Use `ui`             | chakra-ui is for library authors                    |
| Use `hook` for useQuery patterns   | Use `react-query`    | hook is for structure, react-query for RQ specifics |
| Use `coding` for component styling | Use `ui`             | coding is library-agnostic                          |
| Use `auth` for route guards        | Use `routing`        | auth is for auth logic, routing for guards          |
| Use `ui` for error toasts          | Use `error-handling` | error-handling has toast patterns                   |
| Use `coding` for useNavigate       | Use `routing`        | routing is specific to React Router                 |
