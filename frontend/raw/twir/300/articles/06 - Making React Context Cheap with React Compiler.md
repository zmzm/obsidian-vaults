---
type: twir-item
issue: 300
item: 6
item_type: item
date: 2026-10-07
source: https://jjenzz.com/making-react-context-cheap/
tags:
  - "Compiler"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2026-10-07-TWIR-300|Index]]

# Item 6: Making React Context Cheap with React Compiler

Source: [https://jjenzz.com/making-react-context-cheap/](https://jjenzz.com/making-react-context-cheap/)

Summary:
This article explores the performance limitations of React context, especially in large lists (e.g., 5,000 radios), and discusses why React still lacks a context selector API. It compares traditional context usage, external store patterns, and React’s recommended memoization techniques, showing that with proper memoization, context can be performant even at scale. The piece also notes that the React Compiler can optimize context usage, reducing unnecessary re-renders, and references ongoing discussions and RFCs about context selectors.

Key takeaways:
- React context causes all consumers to re-render on any value change, but memoization can limit actual DOM updates.
- React does not provide a useContextSelector API; workarounds and RFCs exist, but the team prefers memoization and compiler optimizations.
- useSyncExternalStore is not recommended for replacing internal state; sticking to React primitives ensures compatibility with concurrent features.
- Benchmarks show that with memoization, context performance can approach that of fine-grained external stores.

Recommendation:
Read fully (valuable for understanding context performance, best practices, and future directions)

Why it matters:
valuable for understanding context performance, best practices, and future directions

Content:
# Making React Context Cheap with React Compiler

When building React apps, many of us have probably craved a context selector at some point. Imagine a radio group where each radio needs to know if it is checked. When the selection moves from one radio to another, only those two radios need to render, but using React context means all context consumers render when any value on the context updates.

A context selector would let a component derive a value from context and render only when that value changes. For example:

```
const checked = useContextSelector(
  RadioContext,
  (context) => context.value === value,
);
```

But React still doesn't have an API like `useContextSelector`, even though re-rendering, say, 5,000 radios is generally understood to be expensive. Why?

## Why doesn't React have a context selector?

React used to have a way to control which context consumers updated. A previous context implementation accepted [a `calculateChangedBits` function](https://github.com/facebook/react/blob/v16.3.2/packages/react/src/ReactContext.js), so we could pass `unstable_observedBits`. The provider marked which bits had changed, and each consumer listened for the bits it cared about, but it was [removed in React PR #20953](https://github.com/react/react/pull/20953).

The need didn't seem to disappear with it though. Josh Story opened a [context selectors RFC](https://github.com/reactjs/rfcs/pull/119) in 2019 proposing a hook for it, and in 2022 I even [tried a ~40-line workaround](https://x.com/jjenzz/status/1565763198191632385?s=20) that turned each piece of state into its own provider 🙈.

I find this gap really interesting. So many React developers have felt this pain, yet React removed `calculateChangedBits` and still doesn't offer a context selector. How has the React team managed without one?

I went looking through the docs, and [React's guidance for `memo`](https://react.dev/reference/react/memo#updating-a-memoized-component-using-a-context) gave me a place to start:

> To make your component re-render only when a *part* of some context changes, split your component in two. Read what you need from the context in the outer component, and pass it down to a memoized child as a prop.

Let's see if that's fast enough with 5,000 radios.

## A small radio group

I built a small demo with a `RadioGroup` that keeps the selected value in React state and puts it in context alongside a stable handler. Each `Radio` receives its own value as a prop.

```
const RadioContext = React.createContext();

function RadioGroup({ children }) {
  const [value, setValue] = React.useState('');
  const context = React.useMemo(
    () => ({ value, onSelect: setValue }),
    [value],
  );

  return (
    <RadioContext.Provider value={context}>
      {children}
    </RadioContext.Provider>
  );
}

function Radio({ value }) {
  const context = React.useContext(RadioContext);

  return (
    <input
      type="radio"
      name="demo"
      checked={context.value === value}
      onChange={() => context.onSelect(value)}
    />
  );
}
```

The `Radio` elements are passed in as children, so the group rendering again doesn't render them, but selecting a radio changes `value`. The provider then passes down a new context object and every `Radio` that calls `useContext(RadioContext)` renders again. With 5,000 radios, that's 5,000 re-rendering radios caused by one click. Ouch.

Nowadays, devs often reach for `useSyncExternalStore` at this point, but the docs for the hook explicitly recommend [built-in state where possible](https://react.dev/reference/react/useSyncExternalStore#subscribing-to-an-external-store), and appear to position it as a bridge to existing external state (not a tool to create our own external state).

I find that interesting, because whenever we branch away from React's primitives, we risk missing out on the features React builds on top of them, like concurrent rendering. In fact, most of the libraries in [Daishi Kato's concurrent rendering tests](https://github.com/dai-shi/will-this-react-global-state-work-in-concurrent-rendering) can't interrupt a render or branch state during a transition, and [Base UI's store](https://github.com/mui/base-ui/blob/master/packages/utils/src/store/useStore.ts) currently fails the same two tests many of those do. That might not be a problem in practice for the places these stores are used, but it does highlight the risk of branching away from React's conventions.

To compare, I started with React's documented pattern. The outer `Radio` reads context and works out whether it's checked, and an inner view receives only the values it uses:

```
function Radio({ value }) {
  const context = React.useContext(RadioContext);

  return (
    <RadioView
      checked={context.value === value}
      onSelect={context.onSelect}
      value={value}
    />
  );
}

const RadioView = React.memo(function RadioView({ checked, onSelect, value }) {
  return (
    <input
      type="radio"
      name="demo"
      checked={checked}
      onChange={() => onSelect(value)}
    />
  );
});
```

Notice that the outer `Radio` still renders on every context update, but `RadioView` only renders when its props change. For one selection, the checked boolean changes for two radios. The handler and each radio's own value stay stable, so React can skip the other 4,998 views.

## Comparing `memo` with the store

These are p95 timings from a production build with 5,000 radios, measured in Chrome on a MacBook Pro (M3 Pro, 36GB RAM). The 4× columns use the 4× CPU slowdown in Chrome DevTools:

| Approach | Mount 1× | Mount 4× | Click 1× | Click 4× |
| --- | --- | --- | --- | --- |
| `useSyncExternalStore` store | 147.6 ms | 601.8 ms | 19.2 ms | 64.9 ms |
| Context with memoized view | 145.0 ms | 568.2 ms | 18.9 ms | 72.6 ms |

Benchmarks generated by Codex.

The store rendered two consumers while the context version still rendered all 5,000 radios, so I expected context to fall well behind. What I found really interesting was that it didn't. The outer readers ran, but the 4,998 unchanged views skipped their work, and the measured performance wasn't exactly worse.

## Letting the compiler memoize

I almost stopped here, but during my exploration I came across [Joseph Savona's reply on the context selectors RFC](https://github.com/reactjs/rfcs/pull/119#issuecomment-3240284309), where he argued that the compiler already does a lot of what we need:

> Our argument is the compiler already achieves a lot of what people want from context selectors.

In [his compiled example](https://github.com/reactjs/rfcs/pull/119#issuecomment-3224691246), the component still reads context, but expensive calculations and JSX are reused when the selected value stays the same. That sounds surprisingly close to fine-grained updates.

Oh wow, okay. Let's see what the radio looks like without the extra view component:

```
function Radio({ value }) {
  const context = React.useContext(RadioContext);
  const checked = context.value === value;
  const onSelect = context.onSelect;

  return (
    <input
      type="radio"
      name="demo"
      checked={checked}
      onChange={() => onSelect(value)}
    />
  );
}
```

So what happens when the selection changes? Every `Radio` still renders again, but [the compiler reuses the JSX](https://playground.react.dev/#N4Igzg9grgTgxgUxALhAMygOzgFwJYSYAEASgIYAmBAFMEQG5kA2UCRAvgJRHAA6xROITA5BhHAgAeogLykEZXADooYBAGFxUnNXJUImzBOmcA3PyJjMIwQAsEcANYIKROUKPaljFmxn+GZlZzAQ8bQgBlBCYHWStjHCVI6NiQiyIYBBxYYmp0ywAePEwABygcfMsiHABPEoQZXhAYSgImystMMgBbBqaKBG6IdoEquwdnChlgOHsnF3YOokJ1WzJMAHMG4GpuGQA+ZcwomNxqH1ZORdGiAHp99LN+dhAAGhAPNDwNlBA+AVutyE3RKeCYZHwhAAshABsgiE1mEwRi93mBbBAAO4ASU8MC6TDAKDQzDU7CAA) from any radio whose `checked`, `onSelect`, and `value` haven't changed. The React docs even show the compiler [reusing previously created JSX and memoizing intermediate values within components](https://react.dev/reference/react/memo#react-compiler-memo).

It's the same outer-consumer-and-memoized-child idea, but the memoizing happens during the consumer's render instead of in a separate component.

## Adding the compiler to the benchmark

I ran a compiler demo through the same p95 production benchmarks, and these were the results:

| Approach | Mount 1× | Mount 4× | Click 1× | Click 4× |
| --- | --- | --- | --- | --- |
| `useSyncExternalStore` store | 147.6 ms | 601.8 ms | 19.2 ms | 64.9 ms |
| Context with memoized view | 145.0 ms | 568.2 ms | 18.9 ms | 72.6 ms |
| Context with Compiler | 141.0 ms | 565.2 ms | 18.4 ms | 63.6 ms |

This is a narrow benchmark, so it isn't a general ranking of stores, context, and the compiler, but the result really did surprise me. The compiled radio has no extra component and no selector, and it kept up with both of the other approaches in every column.

Do we really need `useContextSelector` or `useSyncExternalStore` workarounds anymore?

## If you're not using React Compiler yet

If you haven't taken the leap to the compiler yet, the `React.memo` pattern still works without a build step. While experimenting with these benchmarks, I wrapped it in a small abstraction where each component selects the values its view needs:

```
const Radio = withContextSelector(
  RadioContext,
  (context, props) => ({
    checked: context.value === props.value,
    onSelect: context.onSelect,
  }),
  function Radio({ ctx, props }, ref) {
    return (
      <input
        ref={ref}
        type="radio"
        name="demo"
        checked={ctx.checked}
        onChange={() => ctx.onSelect(props.value)}
      />
    );
  },
);
```

```
function withContextSelector(Context, select, View) {
  const Comp = React.memo(
    React.forwardRef(View),
    (before, after) =>
      shallowEqual(before.ctx, after.ctx) &&
      shallowEqual(before.props, after.props),
  );
  Comp.displayName = View.name;

  return React.forwardRef(function ContextSelector(props, ref) {
    const context = React.useContext(Context);
    if (context === undefined) {
      throw new Error(`<${View.name} /> is missing required context.`);
    }

    const ctx = select(context, props);
    return <Comp ctx={ctx} props={props} ref={ref} />;
  });
}

function shallowEqual(before, after) {
  if (Object.is(before, after)) return true;

  const keys = Object.keys(before);
  return (
    keys.length === Object.keys(after).length &&
    keys.every(
      (key) => Object.hasOwn(after, key) && Object.is(before[key], after[key]),
    )
  );
}
```

This likely needs some TLC, but it at least demonstrates how the pattern could be packaged neatly into a reusable API. Bear in mind that `withContextSelector` is a component factory though, and React's lint rules [discourage those](https://react.dev/reference/eslint-plugin-react-hooks/lints/component-hook-factories). So if you do decide to move to the compiler later, you'd need to remember to remove it to reap the compiler's full benefits.

## What counting renders misses

I've always preferred making renders *cheap* over handholding every render, but this experiment really put that to the test. Every one of those 5,000 radios still rendered on each click, and it barely mattered because almost none of them had anything left to do.

So, is counting renders really useful? What users actually wait for is the work each render does, and that's where React Compiler helps. Rather than trying to avoid renders, maybe we should be focusing more on making them cheap.

Related notes: [[React Compiler]]
