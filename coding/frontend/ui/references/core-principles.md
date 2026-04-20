---
id: fe-ui/core
name: fe-ui/core
kind: reference
domain: frontend-ui
topics: [core]
priority: high
status: stable
canonical: false
updated: 2026-04-16
---

# UI Core Principles

## When to use

Use this document when:

- Working with UI components from @mentory/ui-components
- Understanding import rules and component usage
- Setting up providers for the application

## Rules

- **ALWAYS** use `@mentory/ui-components` for all UI elements
- **NEVER** import directly from `@chakra-ui/*` packages
- The ui-components library is the single source of truth for UI components
- Follow consistent spacing, typography, and color patterns
- Ensure responsive design for all screen sizes
- Maintain visual consistency across the platform

## Current exceptions

- `temporary`: `apps/frontend/src/features/auth/DevLoginPage/DevLoginPage.tsx` historically used direct Chakra imports for a dev-only screen.
  Exit condition: keep this file on `@mentory/ui-components` imports (no direct Chakra in `apps/frontend/src/**`).

## Examples

### Good example

```typescript
// ✅ Good: Import from @mentory/ui-components
import { Button, Input, useToast } from '@mentory/ui-components';
import { ChakraProvider } from '@mentory/ui-components';

export function App() {
  return <ChakraProvider>{/* Your app content */}</ChakraProvider>;
}
```

### Bad example

```typescript
// ❌ Bad: Direct Chakra UI imports
import { Button } from '@chakra-ui/react';
import { useToast } from '@chakra-ui/react';

// ❌ Bad: Missing provider
export function App() {
  return <div>{/* Your app content */}</div>;
}
```

## Anti-patterns

- Importing directly from `@chakra-ui/*` packages
- Not using ChakraProvider wrapper
- Mixing ui-components with direct Chakra imports
- Not following design system patterns
- Inconsistent spacing and typography

## Notes

### Available Components

**Layout Components:**

- `Card` - Container component for content grouping
- `Separator` - Visual divider between content sections

**Form Components:**

- `Button` - Interactive button with multiple variants
- `Input` - Text input field
- `Textarea` - Multi-line text input
- `Label` - Form field label
- `Select` - Dropdown selection component
- `Switch` - Toggle switch for boolean values
- `Form` - Form wrapper with validation support

**Feedback Components:**

- `Alert` - Informational message display
- `Dialog` - Modal dialog component
- `useToast` - Hook for toast notifications

**Display Components:**

- `Avatar` - User avatar display
- `Badge` - Status or category indicator
- `Skeleton` - Loading placeholder
- `ThemeToggle` - Dark/light mode toggle

**Navigation Components:**

- `DropdownMenu` - Contextual menu with actions

**Provider:**

- `ChakraProvider` - Required wrapper for the entire app

### Provider Setup

The app must be wrapped with `ChakraProvider` from `@mentory/ui-components`. The ChakraProvider is already set up in
`apps/frontend/src/app/app.tsx`. You don't need to add it again in feature components.

**Why use @mentory/ui-components?** The ui-components library provides a consistent API wrapper around Chakra UI. Direct imports bypass this
abstraction and break consistency.
