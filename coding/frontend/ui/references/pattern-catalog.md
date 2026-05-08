---
id: fe-ui/pattern-catalog
name: fe-ui/pattern-catalog
kind: reference
domain: frontend-ui
topics: [patterns, components, style extraction]
priority: high
status: stable
canonical: true
updated: 2026-05-08
---

# Pattern Catalog (Frontend UI)

## Purpose

Catalog of reusable UI patterns that MUST be used instead of duplicating style-heavy JSX.

## Mandatory Patterns

### 1. PageContainer

Use for standard page content width/padding.

Use when:

- Page-level content wrapper
- Repeated `maxW + mx + py + px` combinations

Do:

```tsx
<PageContainer py={8}>
  ...
</PageContainer>
```

Do not:

```tsx
<Box maxW="7xl" mx="auto" py={8} px={{ base: 4, sm: 6, lg: 8 }}>
  ...
</Box>
```

### 2. CenteredPageLayout

Use for full-page centered states: loading, access denied, and not signed in.

Do:

```tsx
<CenteredPageLayout>
  <Card>...</Card>
</CenteredPageLayout>
```

### 3. SectionHeader

Use for title and description blocks.

Do:

```tsx
<SectionHeader
  title={t('courses:title')}
  description={t('courses:subtitle')}
  as="h1"
  size="xl"
/>
```

### 4. SurfaceBox

Use for subtle surface containers and repeated padded boxes.

Do:

```tsx
<SurfaceBox p={3} border="1px solid" borderColor="line">
  ...
</SurfaceBox>
```

### 5. StatValue

Use for label and large value display.

Do:

```tsx
<StatValue label={t('stats.completed')} value={42} />
```

### 6. IconText

Use for icon and text rows where repeated.

Do:

```tsx
<IconText icon={Clock} size={14}>
  <Text>2.3s</Text>
</IconText>
```

## Rule

If a style-heavy JSX pattern repeats in 3+ places, extract into:

1. shared component (preferred), or
2. feature-local `*.styles.ts` if not globally reusable.
