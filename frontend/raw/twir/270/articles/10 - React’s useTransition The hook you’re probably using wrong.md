---
type: twir-item
issue: 270
item: 10
item_type: item
date: 2026-02-25
source: https://www.nutrient.io/blog/react-usetransition-guide/
tags:
  - "Async"
status: auto
quality: keep
---

[[2026-02-25-TWIR-270|Index]]

# Item 10: React’s useTransition: The hook you’re probably using wrong

Source: [https://www.nutrient.io/blog/react-usetransition-guide/](https://www.nutrient.io/blog/react-usetransition-guide/)

Summary:
This guide clarifies the intended use of React’s useTransition hook, emphasizing its role in deferring expensive, CPU-bound state updates rather than network requests. It explains the double-render behavior, lane scheduling, and contrasts useTransition with useDeferredValue and debouncing. Practical examples illustrate how to keep input state outside transitions and when to use each hook.

Key takeaways:
- useTransition is best for deferring expensive synchronous updates, not async/network requests.
- It causes two renders: one immediate (isPending=true), one deferred.
- Keep input state updates outside transitions; use useDeferredValue for props-driven deferral.
- Debouncing is still preferable for network requests; useTransition is for UI responsiveness.

Recommendation:
Summary sufficient

Content:
# React’s useTransition: The hook you’re probably using wrong

TL;DR

- `useTransition` causes two renders: one immediate (`isPending` = `true`), and one deferred
- Use it for expensive CPU-bound state updates, not network requests
- Keep input state outside the transition; only wrap derived/filtered state
- Choose `useDeferredValue` when you don’t control the state setter

Your search input feels laggy. Users type, the user interface (UI) freezes for a moment, and then results appear. You’ve probably tried debouncing, but the user experience still isn’t quite right. Sound familiar? Did you know that React has a built-in solution?

The [`useTransition`(opens in a new tab)](https://react.dev/reference/react/useTransition) hook has been available since React 18 but is still widely misunderstood. This article will look at how it actually works under the hood, outline when you should (and shouldn’t) use it, and walk through real examples from a production PDF viewer codebase.

## What useTransition actually does

Before checking some usage patterns, it’s important to first understand what’s happening behind the scenes. When you call `useTransition`, you get back two things:

```
const [isPending, startTransition] = useTransition();
```

The `isPending` Boolean tells you if there’s a transition in progress, and `startTransition` is a function to wrap your state updates. But here’s what’s usually ignored: `useTransition` causes a double rerender.

This becomes clear when you consider the required behavior for `isPending`: It needs to be `true` during the transition, allowing the UI to render a transition state, and `false` afterward to indicate the transition has completed.

The first is an immediate, high-priority render where `isPending` becomes `true`. The callback is then scheduled at a lower priority, and when it completes, a second render occurs with `isPending` set to `false`. This means React can interrupt this work if something more urgent comes along (like the user typing another character).

### Lane scheduling: How React prioritizes

React 18 introduced a concept called “lanes” for scheduling updates. When you wrap state updates in `startTransition`, React assigns your updates to a lower-priority lane. This is what makes transitions interruptible — higher-priority updates (like direct user input) can jump the queue.

## The classic use case: Search input

The most common scenario for `useTransition` is search-as-you-type functionality. Here’s a typical problematic implementation:

```
function SearchDocuments({ documents }) {

const [query, setQuery] = useState('');

const [results, setResults] = useState(documents);

const handleSearch = (value) => {

// Expensive filtering blocking the input.

setResults(documents.filter(doc =>

doc.content.toLowerCase().includes(value.toLowerCase())

onChange={e => handleSearch(e.target.value)}

<ResultsList results={results} />
```

When filtering thousands of documents, every keystroke triggers an expensive operation that blocks the main thread. The input feels sluggish because React can’t update the input value until the filtering completes.

Here’s the same component with `useTransition`:

```
function SearchDocuments({ documents }) {

const [query, setQuery] = useState('');

const [results, setResults] = useState(documents);

const [isPending, startTransition] = useTransition();

const handleSearch = (value) => {

setQuery(value);  // Immediate — keeps input responsive.

// Expensive filtering — can be interrupted.

setResults(documents.filter(doc =>

doc.content.toLowerCase().includes(value.toLowerCase())

onChange={e => handleSearch(e.target.value)}

{isPending && <LoadingSpinner />}

style={{ opacity: isPending ? 0.7 : 1 }}
```

The key insight: `setQuery(value)` happens immediately (high priority), while `setResults()` is wrapped in a transition (low priority). If the user types another character before filtering completes, React abandons the in-progress transition and starts a new one with the updated query.

## useTransition vs. useDeferredValue: When to use which

React 18 also introduced [`useDeferredValue`(opens in a new tab)](https://react.dev/reference/react/useDeferredValue), which can seem similar. Here’s how to choose.

**Use `useTransition` when:**

- You control the state update (you have access to the setter)
- You need the `isPending` flag to show the loading UI
- You want to wrap multiple related state updates together

**Use `useDeferredValue` when:**

- The value comes from props or external state you don’t control
- You just need a “stale” version of a value that updates later
- You’re optimizing a child component without modifying the parent

Here’s `useDeferredValue` in action:

```
function ResultsList({ results }) {

// Create a deferred copy that lags behind during transitions.

const deferredResults = useDeferredValue(results);

const isStale = results !== deferredResults;

<div style={{ opacity: isStale ? 0.7 : 1 }}>

{deferredResults.map(result => (

<ResultItem key={result.id} result={result} />
```

The child component doesn’t need to know about transitions — it just gets props and creates a deferred version. This is great for optimizing existing components without refactoring parents.

## useTransition vs. debouncing

You might wonder: Why not just debounce the search? The following table shows how `useTransition` and debouncing compare.

| Aspect | Debouncing | useTransition |
| --- | --- | --- |
| **Delay** | Fixed (e.g. 300ms) | Dynamic (React decides) |
| **Input feel** | Potentially laggy | Always instant |
| **Loading state** | Must manage yourself | Built-in `isPending` |
| **Cancellation** | Manual cleanup needed | Automatic |

Debouncing adds an artificial delay before any work starts. `useTransition` starts work immediately but allows it to be interrupted. The practical difference is that with debouncing, users wait for a predetermined amount of time before anything happens. With `useTransition`, work begins immediately but the input stays responsive.

That said, debouncing is still the right choice when you’re making network requests — `useTransition` is for CPU-bound work, not I/O.

## Real-world example: PDF document search

At Nutrient, our [Web Viewer SDK](/sdk/web/) needs to search through potentially thousands of pages of text. Here’s a simplified version of how we handle search:

```
// Before: Every keystroke dispatches immediately.

const handleSearchQueryChange = (value) => {

dispatch(searchForTerm(value));  // Expensive operation

// After: Wrap expensive dispatch in transition.

const [isPending, startTransition] = useTransition();

const handleSearchQueryChange = (value) => {

dispatch(searchForTerm(value));
```

The search input stays responsive even when searching through a 500-page document.

## When NOT to use useTransition

`useTransition` isn’t a silver bullet. Avoid it in the following scenarios.

### 1. Network requests

`useTransition` doesn’t wait for promises. If you wrap a fetch call, the transition completes immediately while the request is still in flight:

```
// This doesn't work as expected.

fetchResults(query).then(setResults);  // Transition ends before data arrives.
```

For async operations, use React Suspense with data fetching libraries, or manage loading state separately.

### 2. Already fast operations

If your state update takes less than 16ms (one frame), the overhead of transitions isn’t worth it. Measure first with React DevTools Profiler.

### 3. Critical UI feedback

Don’t wrap state updates that users need to see immediately:

```
// Don't do this — form validation should be instant.

setValidationError('Email is required');
```

## Advanced pattern: Transition with context

In larger applications, a coordination problem may arise when global state changes trigger expensive rerenders across multiple components and you need a way to manage transitions at the source rather than in every consumer.

In these advanced use cases, `Context` may be required to update and propagate to all consumers simultaneously, which may prove challenging. If your filter state affects — for example — a sidebar, a results list, and a summary panel, a single `setFilters()` call triggers rerenders in all three. Without coordination, each component would need its own `useTransition` — leading to duplicated logic and inconsistent loading states.

By placing `useTransition` in the `Context` provider, you centralize the transition logic and expose `isPending` alongside the state:

```
function FilterProvider({ children }) {

const [filters, setFilters] = useState(defaultFilters);

const [isPending, startTransition] = useTransition();

const updateFilters = (newFilters) => {

<FilterContext.Provider value={{ filters, updateFilters, isPending }}>

</FilterContext.Provider>
```

All consumers of the context can now show loading states based on `isPending` without implementing transitions themselves. The sidebar can dim its content, the results list can show a spinner, and the summary panel can display a skeleton — all reacting to the same `isPending` flag from a single source of truth.

## Debugging tips

When transitions don’t behave as expected, two approaches help: inspecting render priority in DevTools, and logging to detect interrupted work.

In React DevTools, transitions show up with a special “Transition” label. You can see which renders were high priority vs. transition priority.

### Console logging

Add logs inside your transition callback to see when work starts and if it gets interrupted:

```
console.log('Transition starting for:', value);

setResults(expensiveFilter(value));

console.log('Transition completed for:', value);
```

If a transition gets interrupted, you’ll see “starting” without a corresponding “completed.”

## Key takeaways

1. `useTransition` causes two renders — one immediate (`isPending` = `true`), and one deferred (`isPending` = `false` + your updates)
2. Use it for expensive CPU-bound state updates, not network requests
3. The input state should NOT be wrapped — only the expensive derived state
4. Choose `useDeferredValue` when you don’t control the state setter or want to optimize a child component
5. Measure before optimizing — transitions add overhead, so only use them when you have a measurable jank problem

React’s concurrent features give you control over update priority. Instead of all-or-nothing renders, you can now keep input responsive while expensive work happens in the background. When your UI feels sluggish during state updates, `useTransition` is worth considering — and now you know exactly what’s happening under the hood.
