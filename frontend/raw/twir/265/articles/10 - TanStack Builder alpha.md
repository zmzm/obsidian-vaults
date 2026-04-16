---
type: twir-item
issue: 265
item: 10
item_type: item
date: 2026-01-21
source: https://github.com/facebook/react/pull/35449
tags:
  - "TanStack"
status: auto
quality: keep
---

[[2026-01-21-TWIR-265|Index]]

# Item 10: TanStack Builder alpha

Source: [https://github.com/facebook/react/pull/35449](https://github.com/facebook/react/pull/35449)

Summary:
TanStack Builder Alpha is announced, but no substantive content or details are provided in the excerpt.

Key takeaways:
- Announcement of an alpha release; details not available.

Recommendation:
Summary sufficient

Content:
# [RFC] useStore/createStore APIs by captbaritone · Pull Request #35449 · facebook/react · GitHub

**Note: This is a proof of concept for discussion purposes. API is subject to change and may not ship in this form.**

- *Update 2026-01-07: Added description of the `ReactExternalDataSource` interface, clarified behavior of `getState` and explained how we avoid needing to tell the data source about React commits.*

Many libraries in the React ecosystem exist to allow React components to observe non-React state. As of today there is no way for such a library to do this in a way that is acceptably performant while also taking advantage of React transition semantics. This RFC proposes a new API for modeling state that is not conceptually owned by any one React component but which can be observed by multiple React components in a way that avoids unnecessary rerenders while correctly implementing React’s transition semantics.

## Proposed API

At a high level, this proposal consist of an interface which joins two APIs:

### Interface `ReactExternalDataSource`

The `ReactExternalDataSource` interface describes a unit of dynamic non-React state that can be observed in React using `useStore`. In advanced use-cases store/cache libraries could implement this API to allow their state to be safely consumed in React components.

```
export interface ReactExternalDataSource<S, A> {
  // Get the current state of the store. State must be immutable.
  getState(): S,
  // The stable reducer function used by the store to produce new states.
  // Reducer must be pure.
  reducer: (S, A) => S,
  // updated and includes the action that was dispatched.
};
```

Note that `getState()` here must always returns the “current” version of the data source (the result of applying all the actions in the order in which they were triggered) irrespective of any React transition. Different React roots may be rendering different states at any given time, but the data source itself does not need to be aware of that.

### `useStore`

```
function useStore<S, T>(
  store: ReactExternalDataSource<S, mixed>,
  selector?: (state: S) => T
): T;
```

`useStore` is designed to echo `useContext`. It allows users to observe a store’s value, or a slice/selection of that store value, in a React component. Notably it avoids triggering a render if the observed portion of the store has not changed while still correctly implementing React’s transition semantics including avoiding tearing and correctly implementing [React’s update reordering semantics](https://jordaneldredge.com/react-rebasing/).

### `createStore`

```
function createStore<S, A>(
  initialValue: S,
  reducer?: (S, A) => S
): ReactStore<S, A>;
```

For simple use cases, React provides it’s own simple (~20loc) store implementation which implements `ReactExternalDataSource`. `createStore` is designed to echo `useState` and `useReducer`. If a reducer is not provided, the `dispatch` method of the store mirrors `setState` in that it accepts either a new value, or an updater function. If a reducer *is* provided, the `dispatch` method accepts a concrete action value which is passed to the reducer.

The returned `ReactStore` object implements `ReactExternalDataSource` and also exposes a `.dispatch(action)` method.

## Example Usage

```
const store = createStore(1);

function App() {
  const value = useStore(store);
  return <button onClick={() => store.dispatch(prev => prev + 1)}>
    {value}
   </button>;
}
```

## Implementation Details

The core problems that any implementation of a concurrent compatible store API must solve are:

1. When a store reader mounts sync during a transition, it must observe the pre-transition state, and then update to the new state with all other components.
2. If a store update is dispatched sync while one or more other updates to the store are still pending as part of a transition, it must correctly model React’s [update reordering semantics](https://jordaneldredge.com/react-rebasing/).

To address these problems, the current implementation maintains a reference counted registry of currently observed stores at each React root. As stores update, each root is able to track which state updates are pending and which have flushed to the UI. When a new component mounts sync, it’s able to find the “current” state value for that store in its React root even if other updates are pending. When a sync update is triggered while a previous update is still pending within that root, the update (action + reducer) can be applied on top of the “current” state for that React root.

Note that the underlying data source does not need to be told when an update commits, and is never aware of any non-canonical states that React produces when sync updates interrupt transition updates. Those temporary states are created by React itself using: `source.reducer(comittedState, syncAction)`.

(See “Unsolved Problems” below for some limitations associated with the ref counting portion of this approach).

For maintaining per-component state, this implementation currently leverages the internal `updateReducerImpl` function, but eagerly pre-computes each update’s value, and explicitly triggers transition fixups, instead of allowing the update queue to be computed during render. This is likely not the cleanest approach, but was minimally invasive while still allowing us to take advantage of the many battle tested detailed of the `updateReducerImpl` implementation, which felt like a good balance for a proof of concept. I expect we will eventually want to either create a custom fork of `updateReducerImpl` for this API, or at least refactor `updateReducerImpl` so that it can be sensibly reused by this API.

## Existing Alternative Solutions

Today existing libraries are choosing between one of a few imperfect existing solutions:

1. `useReducer` + `useContext` this works and is correct, but quickly becomes impractical in the real world due to the performance implications of `useContext` triggering rerenders on every state update.
2. `useSyncExternalStore` this API allows the efficient observation of non-React state, but it prevents updates to stores from participating in React transitions.
3. Rolling their own per-component subscription using `useEffect`. This is fraught with challenges and I believe it’s impossible to fully match React’s transition semantics. I believe [this](https://github.com/thejustinwalsh/react-concurrent-store/tree/main/packages/use-store/src/experimental) is the closest anyone has been able to get, but it makes unsafe assumptions about React and still has known edge cases which are incorrect or have sub-optional performance.

## Unsolved Problems

The current implementation is not perfect. It has some known limitations, but I wanted to share it in its current state to get feedback before continuing with the work/discussion needed to address these issues. But, for the sake of completeness I’ve captured them here:

### Lifetimes

In the edge case where a React root starts observing a store while that store is already updating as part of a transition, the current implementation will incorrectly observe the post-transition value of that store even though the transition is still pending. I believe resolving this issue would require all React roots to know about all stores that are updating as part of transitions, even if they are not observing that store. This is somewhat tricky to implement without interfering with the GC of either stores or React roots. I suspect there is a solution here using WeakRefs, but its possible there is a simpler approach that I am overlooking.

### Custom equality

A key feature of this API is avoiding rerenders when the value observed by a component has not changed. To determine if the result of evaluating a selector has changed, we currently use [`Object.is`](http://object.is/) which is the standard in React. However, in many cases this is not sufficient, and libraries like Redux provide mechanisms for providing custom equality functions for determining if a selector’s value has changed. I believe our API should enable this behavior by either allowing the user provide a third `isEqual` argument to `useStore` when providing a selector, *or* by calling the selector with both the current state value *and* the previous state value.

Neither of these are currently implemented since our current approach of leveraging `updateReducerImpl` does not allow us to easily “see” the currently rendered/rendering value for a given lane.

### Categorically avoiding unnecessary rerenders

The current implementation reuses the logic from `useReducer` to model per-component state updates. This allows us to reuse a bunch of known-correct logic to get something working correctly quickly. However, `useReducer` has known/accepted issues where it will trigger a rerender despite the value not actually changing. This may be less acceptable for `useStore` than it is for `useReducer` since `useStore` with a selector is specifically designed to avoid unnecessary renders.

Updating the `useReduce` logic to avoid useless renders would be nice, though it seems the task is tricky enough that previous attempts have been reverted and not reattempted.
