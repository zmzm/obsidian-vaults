---
type: twir-item
issue: 262
item: 11
item_type: item
date: 2025-12-10
source: https://dev.to/artalar/reatom-state-management-that-grows-with-you-1i4
tags:
status: auto
quality: keep
---

[[2025-12-10-TWIR-262|Index]]

# Item 11: Reatom: State Management That Grows With You

Source: [https://dev.to/artalar/reatom-state-management-that-grows-with-you-1i4](https://dev.to/artalar/reatom-state-management-that-grows-with-you-1i4)

Summary:
Reatom is presented as a unified, composable state management solution for React, emphasizing minimalism, extensibility, and explicit reactivity. It covers simple to complex use cases, including async flows, forms, routing, and persistence, all built from small, composable primitives. The system avoids proxy-based reactivity and offers strong TypeScript support, performance, and debugging tools.

Key takeaways:
- Reatom uses atoms and computed values for explicit, scalable state management.
- Extensions handle async, persistence, routing, and more, reducing the need for multiple libraries.
- Strong TypeScript integration and debugging support.
- Outperforms alternatives in complex scenarios and avoids proxy pitfalls.

Recommendation:
Read fully (read fully if evaluating state management solutions or interested in advanced patterns)

Why it matters:
read fully if evaluating state management solutions or interested in advanced patterns

Content:
# Reatom: State Management That Grows With You

## The Fragmentation Problem

Modern frontend development has a familiar pattern:

- Start with simple `useState` hooks
- Need shared state? Add Context
- Context re-renders too much? Add a state manager
- State manager doesn't handle async well? Add a data fetching library
- Need forms? Another library
- Routes need data loading? Router with loaders
- Persistence? Yet another library
- Logging and analytics? Here we go again...

Each tool has its own mental model, API quirks, and bundle cost. The stack grows, complexity multiplies, and new team members need weeks to understand it all. Versioning and maintaining compatibility across multiple libraries becomes a nightmare.

**Reatom is a different approach.** One coherent system that can handle all of these concerns — from the simplest counter to the most complex enterprise data flows. Use what you need, integrate with what you have.

For fast overview, you can check out our site: <https://v1000.reatom.dev/>

## The Zen

Four principles guide Reatom's design:

- **Primitives outperform frameworks** — A few powerful building blocks beat a complex framework
- **Composition beats configuration** — Stack simple pieces instead of configuring monoliths
- **Explicit specifics, implicit generics** — Be clear about what matters, hide the boilerplate
- **Compatibility worth complexity** — Works with your stack, not against it

These aren't marketing slogans. They're the result of six years of production use and continuous refinement, starting with the first LTS release in December 2019.

## Start Simple

If signals are familiar, Reatom will feel natural:

```
import { atom, computed } from '@reatom/core'

const counter = atom(0)
const isEven = computed(() => counter() % 2 === 0)

// Read
console.log(counter()) // 0
console.log(isEven()) // true

// Write
counter.set(5)
counter.set((prev) => prev + 1)
```

Enter fullscreen mode

Exit fullscreen mode

No providers, no boilerplate, no ceremony. The core is less than **3KB gzipped** — smaller than some "lightweight" alternatives.

You can stop there, but here's where it gets interesting...

## Grow Infinitely

The same primitives that power a counter can handle enterprise-grade complexity:

```
import { atom, computed, withSearchParams, withAsyncData, wrap, sleep } from '@reatom/core'

// Sync with URL search params automatically
const search = atom('', 'search').extend(withSearchParams('search'))
const page = atom(1, 'page').extend(withSearchParams('page'))

// Async computed with automatic cancellation
const searchResults = computed(async () => {
  const url = `/api/search?q=${search()}&page=${page()}`
  await wrap(sleep(300)) // The wrap provides debouncing here

  const response = await wrap(fetch(url))
  return await wrap(response.json())
}, 'searchResults').extend(withAsyncData({ initState: [] }))

// Now you have:
searchResults.ready() // loading state
searchResults.data() // the results
searchResults.error() // any errors
```

Enter fullscreen mode

Exit fullscreen mode

What happens here:

1. `search` and `page` atoms automatically sync with URL params
3. If the user types faster than the API responds, **previous requests are automatically cancelled**
4. Race conditions? Handled. Memory leaks? Impossible.

This is the same `atom` from the counter example — just extended.

## The Extension System

Instead of a monolithic framework, Reatom provides composable extensions that stack cleanly:

```
const theme = atom('dark').extend(
  // Persist to localStorage
  withLocalStorage('theme'),
)

const list = atom([]).extend(
  // Memoize an equal changes
  withMemo(),
)

const unreadCount = atom(0).extend(
  // React to state changes
  withChangeHook((count) => {
    document.title = count > 0 ? `(${count}) My App` : 'My App'
  }),
  // Sync across tabs
  withBroadcastChannel('notificationsCounter'),
)
```

Enter fullscreen mode

Exit fullscreen mode

Each extension does one thing well. Compose exactly what's needed.

## Beyond State: Complete Solutions

Reatom provides full solutions for common frontend challenges:

### Forms

Type-safe form management with first-class support for:

- Field-level and form-level validation (sync and async)
- Integration with Standard Schema validators (Zod, Valibot, etc.)
- Dynamic field arrays with add, remove, reorder operations
- Focus tracking, dirty detection, error management
- No weird string paths — just objects and atoms
- Extremely optimized and performant

<https://v1000.reatom.dev/start/forms/>

### Routing

Type-safe routing with automatic lifecycle management:

- Parameter validation and transformation
- Data loading with automatic cancellation on navigation
- Nested routes with shared layouts
- Search parameter handling
- Isomorphic cross-framework support
- **Factory pattern** — state created in route loaders is automatically garbage collected on navigation, solving the "global state cleanup" problem

<https://v1000.reatom.dev/start/routing/>

### Persistence

A ton of built-in storage adapters with general advanced features:

- localStorage, sessionStorage, BroadcastChannel, IndexedDB, Cookie and Cookie Store
- Integration with Standard Schema validators (Zod, Valibot, etc.)
- Version migrations for data format changes
- TTL (time-to-live) support
- Graceful fallback to memory storage when unavailable

<https://v1000.reatom.dev/handbook/persist/>

## Deep Technical Advantages

### Cause Tracking

Reatom emulates [TC39 AsyncContext](https://github.com/tc39/proposal-async-context) and gets a TON of benefits from it:

The last feature is a game changer for complex async flows. You can easily inspect the cause of your concurrent operations and reduce debugging time from hours to minutes.

#### Performance

Reatom has the best possible performance given its feature set. The more complex the application, the faster Reatom performs compared to alternatives.

Benchmarks for complex computations show Reatom outperforming MobX in moderately sized dependency graphs — impressive given that Reatom uses immutable data structures and operates in a separate async context, features that bring significant benefits but typically add overhead.

### Explicit Reactivity, No Proxies

Proxy-based reactivity can be convenient for simple cases but becomes harder to trace in large codebases. With Reatom, hover over any property for a type hint — it's always clear what's reactive.

Reatom encourages **atomization** — transforming backend DTOs into application models where mutable properties become atoms:

```
// Backend DTO
type UserDto = { id: string; name: string }

// Application model with explicit reactivity
type User = { id: string; name: Atom<string> }

const userModel = { id: dto.id, name: atom(dto.name) }

// Now it's always clear:
userModel.id // static value — no reactivity
userModel.name() // reactive — tracks changes
```

Enter fullscreen mode

Exit fullscreen mode

This pattern gives you fine-grained control: define reactive elements precisely where needed, avoid the uncontrolled creation of observers, and never need `toJS`-like conversions to inspect or pass data.

#### Less complexity with atomization

In immutable state managers, updating one item in a list requires recreating the entire array — O(n) complexity. Reatom's atomization pattern provides O(1) updates:

```
// Traditional immutable approach: O(n)
const updateName = (state, idx, name) => ({
  ...state,
  users: state.users.map((u, i) => (i === idx ? { ...u, name } : u)),
})

// Reatom with atomization: O(1)
users()[idx].name.set(newName)
```

Enter fullscreen mode

Exit fullscreen mode

For lists with thousands of items, this difference matters.

## Framework Agnostic, Ecosystem Friendly

Right now Reatom works best with React (<https://v1000.reatom.dev/reference/react>), but we already have draft packages for Vue, Preact, Solid, and Lit, with plans for Svelte and Angular (signals). You can also bind any library using [reatomObservable](https://v1000.reatom.dev/reference/methods/#reatomobservable).

Write your state and effects once, get a reusable model for complex tests and any view framework. Perfect for modularity in general, and microfrontends especially.

Reatom isn't a walled garden. It plays well with the native web APIs and the entire npm ecosystem: use Zod for validation, any fetch wrapper for HTTP, use built-in AbortController's, bind any UI library for components. Adopt Reatom incrementally in existing projects — no need to rewrite everything at once.

## Try It

```
npm install @reatom/core @reatom/react
```

Enter fullscreen mode

Exit fullscreen mode

Start with atoms. Add extensions as needed. Scale to any complexity.

---

**Links:**
