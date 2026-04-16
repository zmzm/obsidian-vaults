---
type: twir-item
issue: 274
item: 10
item_type: item
date: 2026-03-25
source: https://pavi2410.com/blog/post-react-compiler-coding-guide/
tags:
  - "Post-React"
  - "Post-ReactCompiler"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2026-03-25-TWIR-274|Index]]

# Item 10: Post-React Compiler React Coding Guide (For AI Agents)

Source: [https://pavi2410.com/blog/post-react-compiler-coding-guide/](https://pavi2410.com/blog/post-react-compiler-coding-guide/)

Summary:
With the React Compiler, many manual optimization patterns (useMemo, useCallback, React.memo) are now redundant or discouraged. The guide advocates for writing simple, declarative components, relying on the compiler for memoization and optimization. It provides practical rules for hooks usage, error boundaries, list keys, and when manual optimization is still appropriate.

Key takeaways:
- Avoid manual memoization; let the compiler optimize renders.
- Prefer plain JavaScript and derive data inline rather than storing it in state.
- Inline callbacks are fine; only lift state or memoize when semantically necessary.
- Manual optimization should be reserved for edge cases or integration with non-React systems.

Recommendation:
Read fully (read fully if you are transitioning to React 19 or want to write compiler-friendly code)

Why it matters:
read fully if you are transitioning to React 19 or want to write compiler-friendly code

Content:
# Post-React Compiler React Coding Guide (For AI Agents)

## Foreword: Why Iâm Writing React Guides for AI[#](#foreword-why-im-writing-react-guides-for-ai)

[React Compiler](https://react.dev/learn/react-compiler) v1.0 landed in 2025[1](#user-content-fn-1), and React 19 shipped with major changes to how we write components[2](#user-content-fn-2). But hereâs the problem: AI coding agents havenât caught up. Theyâre still generating code like itâs 2022.

I keep seeing AI-generated React code that wraps every callback in `useCallback`, memoizes simple calculations with `useMemo`, and still reaches for `forwardRef` even though React 19 doesnât need it anymore for function components[3](#user-content-fn-3). They havenât learned that ref callbacks now support cleanup functions[4](#user-content-fn-4). They donât know about the Compilerâs existence, let alone how to write code that works *with* it instead of against it.

Someone needs to teach them. So here we are.

This is the first in a series of guides Iâm writing specifically for AI agents generating React code. This one covers Post-React Compiler patternsâhow to write simple, compiler-friendly code that doesnât fight the optimization layer. Future guides will cover React 19âs new APIs like `useActionState`[5](#user-content-fn-5), `useOptimistic`[6](#user-content-fn-6), and more.

If youâre human and reading this, welcome! Think of this as a âwhat good AI should knowâ checklist. Itâs also a solid mental model for modern React development. The patterns Iâm recommending for AI are the same ones we should all be writing.

Letâs get AI caught up.

---

> **Audience**: AI agents generating React code targeting environments where the React Compiler (or equivalent automatic memoization / reactive analysis) is enabled.
>
> **Goal**: Produce React code that is **simple, readable, declarative, and compiler-friendly**, avoiding legacy performance patterns that are now either unnecessary or harmful.

## 1. Mental Model Shift[#](#1-mental-model-shift)

### Pre-Compiler React (Legacy Model)[#](#pre-compiler-react-legacy-model)

- Developers manually controlled re-renders.
- `useMemo`, `useCallback`, and `memo` were used defensively.
- Referential equality was a primary performance concern.
- Code was structured around *avoiding renders*.

### Post-Compiler React (Modern Model)[#](#post-compiler-react-modern-model)

- The compiler analyzes component behavior and inserts memoization automatically.
- Renders are cheap; *unnecessary complexity is expensive*.
- Code should be structured around **clarity and correctness**, not render avoidance.
- The compiler, not the author, owns optimization.

> **Rule of Thumb**: Write React as if every render is free and memoization is automatic.

---

## 2. Core Principles[#](#2-core-principles)

### 2.1 Prefer Plain JavaScript[#](#21-prefer-plain-javascript)

- Use normal variables, functions, and expressions.
- Avoid wrapping logic in hooks unless semantically required.

**Good**

```
const total = items.reduce((sum, i) => sum + i.price, 0)
```

**Avoid**

```
const total = useMemo(() => items.reduce((sum, i) => sum + i.price, 0), [items])
```

---

### 2.2 Avoid Manual Memoization by Default[#](#22-avoid-manual-memoization-by-default)

Do **not** introduce:

- `useMemo`
- `useCallback`
- `React.memo`

â¦unless one of the following is true:

- You are integrating with **non-React systems** (event listeners, subscriptions, imperative APIs).
- The value must be **referentially stable across renders for correctness**, not performance.

> Memoization for performance is the compilerâs job.

---

### 2.3 Treat Components as Pure Functions[#](#23-treat-components-as-pure-functions)

Components should:

- Derive UI purely from props, state, and context.
- Avoid hidden mutable state.
- Avoid observable side effects during render.

**Good**

```
function Price({ value }) {
  return <span>{value.toFixed(2)}</span>
}
```

**Avoid**

```
let cached
function Price({ value }) {
  cached ??= value.toFixed(2)
  return <span>{cached}</span>
}
```

---

## 3. Hooks Usage Guidelines[#](#3-hooks-usage-guidelines)

### 3.1 `useState`[#](#31-usestate)

- Use for true local UI state.
- Prefer multiple small states over one large object.

**Good**

```
const [open, setOpen] = useState(false)
const [count, setCount] = useState(0)
```

---

### 3.2 `useEffect`[#](#32-useeffect)

- Use only for **effects**, not derivations.
- Effects synchronize React with the outside world.

**Good**

```
useEffect(() => {
  document.title = title
}, [title])
```

**Avoid**

```
const [derived, setDerived] = useState()
useEffect(() => {
  setDerived(a + b)
}, [a, b])
```

Derive values inline instead.

---

### 3.3 `useRef`[#](#33-useref)

- Use for:

  - Imperative handles
  - Mutable values that do **not** affect rendering

**Avoid** using `useRef` as a memoization cache.

---

## 4. Props and Data Flow[#](#4-props-and-data-flow)

### 4.1 Inline Callbacks Are Fine[#](#41-inline-callbacks-are-fine)

Callbacks were historically wrapped in `useCallback` for performance. The compiler handles this now.

**Good**

```
<Dialog open={open} onClose={() => setOpen(false)} />
```

**Avoid Over-Engineering**

```
const onClose = useCallback(() => setOpen(false), [])
<Dialog open={open} onClose={onClose} />
```

The compiler can handle inline closures.

---

### 4.2 Lift State Only When Semantically Necessary[#](#42-lift-state-only-when-semantically-necessary)

- Do not lift state purely for performance.
- Lift state when multiple components need to *coordinate*.

---

## 5. Lists and Keys[#](#5-lists-and-keys)

- Keys should be **stable and semantic**. Avoid index-based keys when items can be reordered, added, or removed.
- Do not optimize list rendering with memoization.

**Good**

```
items.map(item => <Row key={item.id} item={item} />)
```

---

## 6. Derived Data[#](#6-derived-data)

### Rule: Derive, Donât Store[#](#rule-derive-dont-store)

- Never store derived data in state.
- Compute it directly during render.

**Good**

```
const visibleItems = items.filter(i => i.visible)
```

**Avoid**

```
const [visibleItems, setVisibleItems] = useState([])
```

---

## 7. Error Boundaries and Suspense[#](#7-error-boundaries-and-suspense)

- Treat `Suspense` as a **control-flow primitive**, not a performance trick.
- Do not prematurely split components for loading states.

---

## 8. When Manual Optimization *Is* Allowed[#](#8-when-manual-optimization-is-allowed)

Manual optimization is acceptable when:

- Profiling shows a real bottleneck **after** compilation.
- Interfacing with legacy or non-React systems.
- Referential stability is required for correctness (e.g., effect dependencies, subscriptions).
- You need **precise control over effect re-execution**, beyond what the compiler infers.

In these cases:

- Treat `useMemo`, `useCallback`, and `React.memo` as **escape hatches**, not defaults.
- Document *why* memoization exists.
- Scope it as narrowly as possible.

---

## 9. Compiler Configuration, Compilation Modes & Directives (Critical for AI Agents)[#](#9-compiler-configuration-compilation-modes--directives-critical-for-ai-agents)

### 9.1 Compilation Modes (`compilationMode`)[#](#91-compilation-modes-compilationmode)

React Compiler behavior depends on the configured **compilation mode**. AI-generated code must be correct under *all* modes.

Supported modes:

- **`infer` (default)**

  - Compiler heuristically detects React components and hooks.
  - PascalCase + JSX â component inference.
  - `use*` prefix + hook usage â hook inference.
  - This is the most common mode.
- **`annotation`**

  - Only functions explicitly annotated with `"use memo"` are compiled.
  - Used for incremental adoption and safety.
  - AI agents must not assume compilation unless annotations are present.
- **`syntax`**

  - Relies on Flow-specific component syntax.
  - Rare in TypeScript codebases.
- **`all`**

  - Attempts to compile all top-level functions.
  - Generally discouraged due to unpredictability.
  - Opt-out directives become especially important.

**AI Rules**:

- Assume `infer` unless explicitly told otherwise.
- Never rely on compilation for correctness.
- Follow naming conventions to aid inference.

---

### 9.2 Rules of Inference (How the Compiler Decides What to Optimize)[#](#92-rules-of-inference-how-the-compiler-decides-what-to-optimize)

The compiler infers intent based on structure and naming:

- PascalCase + JSX â Component
- `useX` + hook usage â Hook
- Everything else â Possibly ignored unless annotated

AI agents must:

- Use standard naming conventions.
- Avoid ambiguous helper functions that resemble components.
- Not depend on inference for semantics.

---

### 9.3 Compiler Directives[#](#93-compiler-directives)

React Compiler directives control *whether* code is compiled â not *how fast* it runs.

#### `"use memo"`[#](#use-memo)

- Explicitly opts a function or file **into** compilation.
- Required in `annotation` mode.
- Rarely needed in `infer` mode.

#### `"use no memo"`[#](#use-no-memo)

- Explicitly opts a function or file **out of** compilation.
- Takes precedence over all compilation modes.
- Equivalent to disabling the compiler for that scope.

**Guidelines for AI Agents**:

- Never introduce directives automatically.
- Respect existing directives.
- Use `"use no memo"` only as a last-resort escape hatch.
- Always document why an opt-out exists.

> Directives define **compiler trust boundaries**, not performance hints.

---

## 10. Code Style Expectations for AI Agents[#](#10-code-style-expectations-for-ai-agents)

AI-generated React code should:

- Prefer readability over cleverness.
- Avoid defensive patterns from pre-compiler React.
- Minimize hooks usage.
- Avoid comments explaining memoization or render behavior unless strictly required.

> If you feel the need to explain why a hook is used, reconsider whether it is needed.

---

## 11. Summary Rules (Checklist)[#](#11-summary-rules-checklist)

- â Do not use `useMemo` / `useCallback` by default
- â Do not store derived state
- â Do not optimize renders manually
- â Write components as pure functions
- â Derive values inline
- â Use hooks only for semantics, not performance
- â Trust the compiler

---

**Final Principle**:

> *In post-React Compiler React, performance is an implementation detail. Semantics are the API.*

Related notes: [[React Compiler]]
