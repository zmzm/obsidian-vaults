---
type: twir-item
issue: 267
item: 11
item_type: item
date: 2026-02-04
source: https://skills.sh/vercel-labs/agent-skills/vercel-composition-patterns
tags:
  - "Skills"
status: auto
quality: keep
---

[[2026-02-04-TWIR-267|Index]]

# Item 11: React Composition Patterns Agent Skills

Source: [https://skills.sh/vercel-labs/agent-skills/vercel-composition-patterns](https://skills.sh/vercel-labs/agent-skills/vercel-composition-patterns)

Summary:
Vercel Labs releases a set of "Agent Skills" focused on React composition patterns, targeting both human and AI developers. The guide covers component architecture, state management, implementation patterns, and React 19-specific APIs, with rules and code examples for building scalable, maintainable components. Emphasis is placed on avoiding boolean prop proliferation, using compound components, and leveraging new React APIs.

Key takeaways:
- The skills document best practices for flexible, maintainable React component design, especially for large codebases.
- Guidance includes explicit rules for architecture, state, and implementation, with React 19-specific recommendations.
- Designed for both manual refactoring and AI agent reference, improving code quality and consistency.
- Each rule is documented with explanations and before/after code samples.

Recommendation:
Summary sufficient

Content:
# vercel-composition-patterns by vercel-labs/agent-skills

# React Composition Patterns

Composition patterns for building flexible, maintainable React components. Avoid
boolean prop proliferation by using compound components, lifting state, and
composing internals. These patterns make codebases easier for both humans and AI
agents to work with as they scale.

## When to Apply

Reference these guidelines when:

- Refactoring components with many boolean props
- Building reusable component libraries
- Designing flexible component APIs
- Reviewing component architecture
- Working with compound components or context providers

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
| --- | --- | --- | --- |
| 1 | Component Architecture | HIGH | `architecture-` |

## Quick Reference

### 1. Component Architecture (HIGH)

- `architecture-avoid-boolean-props` - Don't add boolean props to customize
  behavior; use composition
- `architecture-compound-components` - Structure complex components with shared
  context

- `state-decouple-implementation` - Provider is the only place that knows how
  state is managed
- `state-context-interface` - Define generic interface with state, actions, meta
  for dependency injection
- `state-lift-state` - Move state into provider components for sibling access

- `patterns-explicit-variants` - Create explicit variant components instead of
  boolean modes
- `patterns-children-over-render-props` - Use children for composition instead
  of renderX props

> **⚠️ React 19+ only.** Skip this section if using React 18 or earlier.

- `react19-no-forwardref` - Don't use `forwardRef`; use `use()` instead of `useContext()`

## How to Use

Read individual rule files for detailed explanations and code examples:

```
rules/architecture-avoid-boolean-props.md
rules/state-context-interface.md
```

Each rule file contains:

- Brief explanation of why it matters
- Incorrect code example with explanation
- Correct code example with explanation
- Additional context and references

## Full Compiled Document

For the complete guide with all rules expanded: `AGENTS.md`
