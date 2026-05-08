---
id: frontend/coding/style-extraction-thresholds
name: frontend/coding/style-extraction-thresholds
kind: reference
domain: frontend
topics: [coding, style extraction, component structure]
priority: high
status: stable
canonical: true
updated: 2026-05-08
---

# Style Extraction Thresholds

## Mandatory

If a pattern appears in 3+ places, extraction is REQUIRED.

## Decision Tree

1. Reused across features?
   - Yes -> shared component in `shared/components/...`
2. Reused only inside one feature?
   - Yes -> feature-local `Feature.styles.ts`
3. One-off but dense style object?
   - Move to `styles.ts` unless truly trivial.

## Prefer

- Shared component for structure and semantics
- `styles.ts` for variant maps and repeated prop sets

## Avoid

- Copy-pasting large `Box/Flex` prop groups in multiple files
