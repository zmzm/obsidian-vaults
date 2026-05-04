---
type: source
status: active
updated: 2026-04-30
tags:
  - react
  - forms
  - react-19
---

# Progressive React Forms

This source captures the React 19 form direction: action-based form submission, `useActionState`, server-side validation, and less reliance on controlled-input boilerplate for ordinary forms.

## Summary

- React 19 allows form actions and `useActionState` to carry loading, validation, error, and success state closer to the form submission flow.
- Simple forms can avoid controlled-input state when the browser form model is sufficient.
- Progressive forms still need explicit UX decisions around preserving values, validation errors, and backend-driven failure states.
- Type-safe FormData/input-name patterns can reduce silent bugs when action handlers read submitted fields.

## Why This Source Matters

- It connects React 19 forms to `React use()` and Server Actions-era data flow without turning every form into a client-state problem.
- It strengthens `Type-Driven Frontend Safety` with a concrete form-contract example.
- It gives the component-design branch a practical place for form accessibility, field naming, and validation boundaries.

## Caveats

- The supporting sources are tutorial-oriented, so this page should stay a source summary rather than becoming a full form architecture pattern yet.
- Framework-specific Server Action behavior may differ, especially outside Next.js.

## Related Pages

- [[../concepts/React use()|React use()]]
- [[../concepts/Server Components|Server Components]]
- [[../patterns/Type-Driven Frontend Safety|Type-Driven Frontend Safety]]
- [[TWIR 215]]
- [[TWIR 217]]
- [[TWIR 218]]

## Raw Sources

- [[../../raw/twir/215/articles/07 - Building a simple form in React - before and after React 19|Building a simple form in React - before and after React 19]]
- [[../../raw/twir/217/articles/12 - Make FormData and input names type-safe in React|Make FormData and input names type-safe in React]]
- [[../../raw/twir/218/articles/07 - Progressive Forms with React 19|Progressive Forms with React 19]]
