---
type: rules
status: active
updated: 2026-04-16
---

# Coding Vault Rules

This file defines the shared rule hierarchy for the coding vault.

Use it to keep skill content consistent, especially when rules from multiple skills overlap.

## Rule Priority

When multiple rules apply, use this order:

1. correctness and data integrity
2. security and access control
3. accessibility and user safety
4. product and domain constraints
5. framework or platform conventions
6. design system conventions
7. performance and optimization
8. local convenience or stylistic preference

Lower-priority guidance should not override higher-priority constraints unless the skill explicitly documents an exception.

## Rule Categories

Every important rule should fit one of these categories:

### Mandatory

Use this for hard constraints that should almost never be violated.

Examples:

- auth checks that protect sensitive operations
- route constants required by project convention
- i18n requirements mandated by product scope

### Default

Use this for the normal preferred choice when no special context pushes in another direction.

Examples:

- preferred component composition patterns
- normal React Query organization
- usual DTO or controller shape

### Heuristic

Use this for judgment calls, tradeoffs, or advice that depends strongly on context.

Examples:

- memoization guidance
- file splitting thresholds
- when to extract a custom hook

### Exception

Use this to document when a mandatory or default rule may be intentionally bypassed.

Every exception should explain:

- what rule is being bypassed;
- when that is acceptable;
- what cost or risk it introduces.

## Wording Rules

Avoid unsupported absolutes.

Prefer:

- `mandatory`
- `default`
- `prefer`
- `usually`
- `only when`
- `unless`

Avoid using `always` and `never` unless the project genuinely treats the rule as non-negotiable.

## Canonical Guidance

When the same topic appears in multiple skills:

- choose one canonical reference;
- link to it from neighboring skills;
- avoid restating the same detailed rules in several places.

Good canonical candidates include:

- forms
- accessibility testing
- API error handling
- route guards
- query and mutation conventions

## Skill Boundary Rules

- `SKILL.md` should route and scope.
- `references/*.md` should carry the detailed rules and examples.
- `INDEX.md` should help selection, not store domain policy.

## Migration Guidance

When normalizing older content:

1. keep the original intent;
2. reduce boilerplate;
3. recategorize rules into `mandatory/default/heuristic/exception`;
4. point repeated topics to canonical references;
5. split oversized files when routing becomes unclear.
