---
id: chakra-ui/semantic-token-mapping
name: chakra-ui/semantic-token-mapping
kind: reference
domain: frontend-ui
topics: [chakra-ui, semantic tokens, colors]
priority: high
status: stable
canonical: true
updated: 2026-05-08
---

# Semantic Token Mapping

## Purpose

Canonical mapping from raw color values to semantic tokens.

## Required Mappings

- `gray.600` / `_dark gray.400` -> `text-secondary`
- `gray.500` / `_dark gray.400` -> `text-tertiary`
- `gray.900` / `_dark gray.50` -> `text-heading`
- `gray.800` / `_dark gray.200` -> `text-strong`
- `red.600` / `_dark red.400` -> `text-error`
- `blue.600` / `_dark blue.400` -> `text-info`
- `gray.50` / `_dark gray.900` -> `surface-subtle`
- `gray.100` / `_dark gray.700` -> `surface-muted`
- `red.50` / `_dark red.900` -> `surface-error`
- `blue.50` / `_dark blue.900` -> `surface-info`

## Icon Color Rule

Preferred:

- set color on wrapper: `color="text-tertiary"`
- icon uses `color="currentColor"`

Avoid:

- `color="var(--chakra-colors-...)"` in `.tsx`
