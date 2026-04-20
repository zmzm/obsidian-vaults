---
id: frontend/chakra-ui/chakra-v3-component-patterns
name: frontend/chakra-ui/chakra-v3-component-patterns
kind: reference
domain: frontend
topics: [chakra-ui, chakra v3 component patterns]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Chakra UI v3 Component Patterns

## When to use

Use this document when:

- Creating or wrapping Chakra UI components in @mentory/ui-components
- Understanding v3 compositional component patterns
- Defining component types with MentoryXProps naming convention
- Setting up component file structure following atomic design

## Rules

- Use `MentoryXProps` naming convention for component types
- Follow atomic design file structure
- Use `colorPalette` instead of `colorScheme` (v3 API)
- Use compositional patterns for complex components (e.g., `Avatar.Root`, `Avatar.Image`)
- Include `traceEventName` prop for analytics
- Extend Chakra props types, don't replace them

## Examples

### Good example

```typescript
// Badge.type.ts
import { BadgeProps as ChakraBadgeProps } from '@chakra-ui/react';

export interface MentoryBadgeProps extends ChakraBadgeProps {
  textColor?: string;
  backgroundColor?: string;
  traceEventName?: string; // Analytics
}

// Badge.tsx
import { Badge as ChakraBadge } from '@chakra-ui/react';

export const Badge: FC<MentoryBadgeProps> = ({ variant = 'solid', colorPalette = 'primary', children, ...rest }) => (
  <ChakraBadge variant={variant} colorPalette={colorPalette} {...rest}>
    {children}
  </ChakraBadge>
);

// Compositional Component (Avatar)
import { Avatar as ChakraAvatar, Float, Circle } from '@chakra-ui/react';

export const Avatar: FC<MentoryAvatarProps> = ({ src, name, isOnline }) => (
  <Float>
    <ChakraAvatar.Root>
      <ChakraAvatar.Image src={src} />
      <ChakraAvatar.Fallback>{name}</ChakraAvatar.Fallback>
    </ChakraAvatar.Root>
    {isOnline && <Circle bg="green.500" size="3" />}
  </Float>
);
```

### Bad example

```typescript
// ❌ Bad: Using v2 API (colorScheme)
export const Badge: FC<MentoryBadgeProps> = ({
  colorScheme = 'blue', // Should be colorPalette
  ...
}) => ...

// ❌ Bad: Not using compositional pattern
<ChakraAvatar src={src} name={name} /> // v3 uses Avatar.Root, Avatar.Image

// ❌ Bad: Not extending Chakra props
export interface MentoryBadgeProps { // Should extend ChakraBadgeProps
  ...
}
```

## Anti-patterns

- Using v2 API (`colorScheme` instead of `colorPalette`)
- Not using compositional patterns for complex components
- Not extending Chakra props types
- Missing `traceEventName` prop for analytics
- Not following atomic design file structure

## Notes

### Key v3 Changes

- `colorScheme` → `colorPalette`
- `extendTheme` → `createSystem + defineConfig`
- Monolithic components → Compositional patterns (e.g., `Avatar.Root`, `Avatar.Image`)
- Style props → Recipe-based styling

### Component Wrapper Structure

**File organization** (atomic design):

```
src/components/atoms/[Component]/
├── [Component].tsx         # Main implementation
├── [Component].type.ts     # TypeScript interfaces
├── [Component].style.ts    # Styling hook (useStyleConfig)
└── [Component].story.tsx   # Storybook stories
```

### Compositional Patterns

v3 uses composition instead of monolithic components. For example:

- No `AvatarBadge` in v3 - use `Float + Circle` pattern
- Use `Avatar.Root`, `Avatar.Image`, `Avatar.Fallback` instead of single `<Avatar>` component
