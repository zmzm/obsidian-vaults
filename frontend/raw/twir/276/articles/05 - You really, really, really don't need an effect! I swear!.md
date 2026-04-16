---
type: twir-item
issue: 276
item: 5
item_type: item
date: 2026-04-08
source: https://neciudan.dev/you-really-really-dont-need-an-effect
tags:
  - "Ink"
status: auto
quality: keep
---

[[2026-04-08-TWIR-276|Index]]

# Item 5: You really, really, really don't need an effect! I swear!

Source: [https://neciudan.dev/you-really-really-dont-need-an-effect](https://neciudan.dev/you-really-really-dont-need-an-effect)

Summary:
This article advocates for minimizing useEffect usage in React, emphasizing that effects should only be used to sync with external systems (e.g., DOM, browser APIs, subscriptions). It provides a decision tree and practical examples showing that many common patterns—like data transformation, handling user events, or resetting state—can be handled without effects, often leading to simpler, more predictable code. The author encourages developers to consult the React docs' "You Might Not Need an Effect" page and to rethink when effects are truly necessary.

Key takeaways:
- Effects are only needed for syncing with external systems, not for internal state, props, or derived data.
- Many common patterns (data filtering, event handling, expensive calculations) can be handled without useEffect.
- Overusing effects leads to unnecessary renders and complexity; alternatives include direct calculation, useMemo, or useSyncExternalStore.
- The article provides clear code examples and a decision tree for effect usage.

Recommendation:
Read fully (practical advice for React developers at all levels; helps reduce misuse of useEffect)

Why it matters:
practical advice for React developers at all levels; helps reduce misuse of useEffect

Content:
# You really, really, really don't need an effect! I swear!

Sometimes, I intentionally add it just to prove the point of removing it. Like in my naming [useEffect functions article](https://neciudan.dev/name-your-effects), where the whole point of the article was to remove most of the `useEffect` hooks.

But clearly, I was not being direct enough, as I kept getting comments about removing useEffects from people who probably didn’t finish the article.

So here it is: You really, really, really don’t need an effect! I swear!

## The one question

The React docs have a page called “You Might Not Need an Effect.” It’s one of the best pages in their entire documentation, and I think most React developers have either never read it or read it once and then forgotten it.

The core idea fits in a single question:

**Is this syncing with an external system?**

But how do we define an external system?

An external system is anything that React doesn’t manage. The browser DOM (for measurements or manual manipulation), a WebSocket server, a third-party library like a map SDK or chart widget, browser APIs like `IntersectionObserver` or `navigator.onLine`, and an `setInterval` timer.

React has no idea these things exist, so you need an effect to bridge the gap.

Things that are *not* external systems: your own props, your own state, values you can calculate from props or state, and user events like clicks and form submissions. React already knows about all of these. If you’re writing an effect that only touches React-managed values, you probably don’t need it.

A borderline example: `document.title`. Setting the page title based on state is technically syncing with the browser DOM, which is an external system.

`useEffect(() => { document.title = \`${count} items` }, [count])` is a valid use of an effect. It’s not one you should try to eliminate.

I made myself a decision tree that captures if I should use an effect or not:

```
function MyComponent() {
  // Ask yourself: "Is this syncing with an EXTERNAL system?"

  // YES → useEffect is fine
  useEffect(() => {
    // WebSocket connections
    // Browser API subscriptions
    // Third-party libraries
    // DOM measurements
  }, []);
  // ↑ The empty array [] means "run once on mount, clean up on unmount."
  // If you list dependencies like [userId], it re-runs when those values change.

  // NO → You probably don't need it!

  // Transforming data?
  // DON'T: useEffect(() => setFiltered(data.filter(...)), [data])
  // DO: const filtered = data.filter(...)
  // If it's slow and not using React Compiler: const filtered = useMemo(() => data.filter(...), [data])

  // Handling user event?
  // DON'T: useEffect(() => { if (clicked) doSomething() }, [clicked])
  // DO: <button onClick={doSomething}>Click</button>

  // Expensive calculation?
  // DON'T: useEffect(() => setResult(expensiveCalc(a, b)), [a, b])
  // DO: const result = expensiveCalc(a, b)
  // If it's slow and not using React Compiler: const result = useMemo(() => expensiveCalc(a, b), [a, b])

  // Resetting state on prop change?
  // DON'T: useEffect(() => setState(prop), [prop])
  // DO: <Component key={prop} />

  // Subscribing to external store?
}
```

That’s the whole mental model. Let me walk through each one, because the details matter.

## Transforming data

This is the most common one I see. You have some data, you want to derive something from it, and your instinct says, “Let’s put it in React state and sync it with an effect.”

```
function TodoList({ todos, filter }) {
  const [visibleTodos, setVisibleTodos] = useState([]);

  useEffect(() => {
    setVisibleTodos(todos.filter(todo => 
      filter === 'active' ? !todo.completed : true
    ));
  }, [todos, filter]);

  return <ul>{visibleTodos.map(todo => <li key={todo.id}>{todo.text}</li>)}</ul>;
}
```

This renders with stale data first, then the effect fires, then it re-renders with the correct data. Two render passes for something that could be zero.

When you can just calculate it:

```
function TodoList({ todos, filter }) {
  const visibleTodos = todos.filter(todo => 
    filter === 'active' ? !todo.completed : true
  );

  return <ul>{visibleTodos.map(todo => <li key={todo.id}>{todo.text}</li>)}</ul>;
}
```

The value exists during render because it can be calculated from things that already exist during render.

If the calculation is expensive, wrap it in `useMemo` or switch to the React Compiler, which memoizes by default:

```
const visibleTodos = useMemo(
  () => todos.filter(todo => filter === 'active' ? !todo.completed : true),
  [todos, filter]
);
```

Even without React Compiler, `useMemo` is still better than the `useEffect` + `setState` version because it doesn’t cause an extra render.

## Handling user events

This one is sneaky because it looks reasonable:

```
function SearchPage() {
  const [query, setQuery] = useState('');
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    if (submitted) {
      performSearch(query);
      setSubmitted(false);
    }
  }, [submitted, query]);

  return (
    <form onSubmit={() => setSubmitted(true)}>
      <input value={query} onChange={e => setQuery(e.target.value)} />
    </form>
  );
}
```

You probably wanted to run something when the user clicks submit. Instead of running it in the event handler, set a flag and have an effect watch it.

But the event handler already knows the user submitted because it has the event context. It runs synchronously. So you can just do the work there:

```
function SearchPage() {
  const [query, setQuery] = useState('');

  // FormEvent is a React type: import { FormEvent } from 'react'
  function handleSubmit(e: FormEvent) {
    e.preventDefault();
    performSearch(query);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={query} onChange={e => setQuery(e.target.value)} />
    </form>
  );
}
```

The React docs put it well: when you’re not sure whether code should be in an effect or in an event handler, ask yourself *why* this code needs to run.

If it’s because the user performed something, it belongs in an event handler.

## Resetting state on prop change

This one catches people off guard because the “obvious” solution works but is wasteful:

```
function UserProfile({ userId }) {
  const [comment, setComment] = useState('');

  useEffect(() => {
    setComment('');
  }, [userId]);

  return <textarea value={comment} onChange={e => setComment(e.target.value)} />;
}
```

When `userId` changes, you want to clear the comment. So you watch `userId` in an effect and reset the state. The component renders with the old comment, the effect fires, and it renders again with an empty comment.

React has a built-in mechanism for this. The `key` prop:

```
function UserProfilePage({ userId }) {
  return <UserProfile userId={userId} key={userId} />;
}

function UserProfile({ userId }) {
  const [comment, setComment] = useState('');
  return <textarea value={comment} onChange={e => setComment(e.target.value)} />;
}
```

When the key changes, React unmounts the old component and mounts a fresh one. All state resets automatically, including the state in child components you might have forgotten about.

One thing to keep in mind: this is a full remount.

If `UserProfile` contains expensive children, a map widget, or its own data fetching, changing the key destroys and recreates everything.

For lightweight components with local form state, that’s fine. For components with heavy initialization, you might want to selectively reset specific state values instead.

But in my experience, the cases where `key` is too expensive are rare, and when they do come up, you’ll know because the UI will visibly flash.

## The biggest one: data fetching

The React docs explicitly say that fetching data in effects is fine, because fetching *is* synchronizing with an external system (the network). But they also say it’s not great, and they list the reasons:

Race conditions. You type “hello” and five requests fire for “h”, “he”, “hel”, “hell”, “hello.” The responses come back in whatever order the network decides. You need cleanup logic to ignore stale responses.

No caching. Navigate away and come back, the whole thing fetches again. The user sees a spinner while the data(they already have) is being loaded.

No server rendering support. The effect runs after mount, so the initial HTML is always in a loading state.

Network waterfalls. A parent component fetches and displays a child component, which then fetches data. Sequential requests that could have been parallel.

You *can* solve all of these with a `useEffect`. You add an `ignore` flag for race conditions, a cache layer, server-side logic, and request deduplication.

At that point, you’ve built a data fetching library.

So why not just use one?

If you’re building a small project and don’t want to add a dependency, `useEffect` with `fetch` is fine.

It’s a valid use of an effect. Just add the cleanup function to ignore stale responses (the React docs show exactly how), and accept the limitations.

## This is where TanStack Query comes in

Data fetching is one of the cases where the decision tree says, “yes, this is an external system, `useEffect` is fine.” And that’s true. You’re allowed to write a `useEffect` that fetches data.

But someone already wrote that effect better than you will.

TanStack Query (React Query) handles every problem I just listed, and it does it by encapsulating the effects you’d write into a single hook call:

```
function UserProfile({ userId }) {
  const { data: user, isLoading, error } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
  });

  if (isLoading) return <Skeleton />;
  if (error) return <ErrorMessage error={error} />;

  return <div>{user.name}</div>;
}
```

No `useEffect`, no `useState` for loading and error states, no cleanup function, no race condition handling.

TanStack Query handles loading, errors, cleanup, and so much more internally. But more importantly, it handles the things you probably wouldn’t have built yourself:

**Caching.** Navigate away and come back, the data is still there. The user sees it instantly while a background revalidation runs silently.

**Automatic deduplication.** Ten components request the same user. One network request fires. All ten get the result.

**Background revalidation.** Show cached data immediately so the user sees something right away, then refetch in the background and swap in the fresh data when it arrives. The user never stares at a loading spinner for data they’ve already seen. (This pattern is called “stale-while-revalidate” if you want to look it up.)

**Window focus refetching.** Without TanStack Query, you’d write a `useEffect` that adds a `visibilitychange` listener, checks `document.visibilityState`, decides whether enough time has passed since the last fetch, and cleans up on unmount.

Every one of those features would be a `useEffect` if you built them yourself: one for the cache, one for deduplication, one for window focus, one for background revalidation. TanStack Query replaces that entire category of effects with a single hook call.

Plus, the `useEffect` version and the TanStack Query version have fundamentally different performance characteristics.

The effect version re-renders at a minimum twice per fetch (once to show loading, once with data). It can’t deduplicate. It can’t share cache across components. It’s doing more work and giving you less.

The same applies to mutations. I’ve seen components where a form submission triggers a `useEffect` chain: submit → set loading state → fetch → update local state → refetch related data → update UI.

`useMutation` replaces that entire chain. It works like `useQuery` but for write operations (creating, updating, deleting data):

```
function CreateUser() {
  // queryClient is TanStack Query's central cache manager.
  // You use it to tell other queries to refetch after a mutation.
  const queryClient = useQueryClient();

  const mutation = useMutation({
    mutationFn: (newUser: NewUser) => createUser(newUser),
    onSuccess: () => {
      // This tells TanStack Query: "the user's data is stale now,
      // refetch it." Any component using useQuery(['users']) 
      // will automatically get the fresh list.
      queryClient.invalidateQueries({ queryKey: ['users'] });
    },
  });

  function handleSubmit(e: FormEvent) {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    mutation.mutate({
      name: formData.get('name') as string,
      email: formData.get('email') as string,
    });
  }

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" />
      <input name="email" />
      <button disabled={mutation.isPending}>
        {mutation.isPending ? 'Creating...' : 'Create'}
      </button>
      {mutation.isError && <p>Something went wrong</p>}
    </form>
  );
}
```

Loading state, error state, cache invalidation, and refetching are all handled. The event handler calls `mutation.mutate()` and TanStack Query does the rest.

## Notifying parent components

Another case where you might use useEffect is when you want to notify parent components.

You have a `Toggle` component with internal state, and you want the parent to know when it changes:

```
function Toggle({ onChange }) {
  const [isOn, setIsOn] = useState(false);

  useEffect(() => {
    onChange(isOn);
  }, [isOn, onChange]);

  function handleClick() {
    setIsOn(!isOn);
  }

  function handleDragEnd(e) {
    if (isCloserToRightEdge(e)) {
      setIsOn(true);
    } else {
      setIsOn(false);
    }
  }

  return <Switch isOn={isOn} onClick={handleClick} onDragEnd={handleDragEnd} />;
}
```

The effect runs after the Toggle re-renders, calls `onChange`, which updates the parent’s state, which triggers the parent to re-render, which triggers the child to re-render. Two render passes for what should be one.

Call `onChange` directly in the event handlers:

```
function Toggle({ onChange }) {
  const [isOn, setIsOn] = useState(false);

  function updateToggle(nextIsOn: boolean) {
    setIsOn(nextIsOn);
    onChange(nextIsOn);
  }

  function handleClick() {
    updateToggle(!isOn);
  }

  function handleDragEnd(e) {
    updateToggle(isCloserToRightEdge(e));
  }

  return <Switch isOn={isOn} onClick={handleClick} onDragEnd={handleDragEnd} />;
}
```

React batches the `setIsOn` and the parent’s state update from `onChange` into a single render pass.

Both components update at once.

## Chaining effects

One effect sets a state, which triggers another effect, which sets another state. I see this most often in forms with dependent dropdowns:

```
function ShippingForm() {
  const [country, setCountry] = useState('');
  const [city, setCity] = useState('');
  const [district, setDistrict] = useState('');
  const [shippingCost, setShippingCost] = useState(0);

  useEffect(() => {
    setCity('');
  }, [country]);

  useEffect(() => {
    setDistrict('');
  }, [city]);

  useEffect(() => {
    if (country && city && district) {
      setShippingCost(calculateShipping(country, city, district));
    }
  }, [country, city, district]);

  // ...
}
```

Selecting a country triggers the first effect, which resets the city; the second effect resets the district; and the third effect triggers. Three re-renders in a cascade, each one painting an intermediate state the user never needed to see.

You can actually do the downstream resets in the event handler that started the chain.

```
function ShippingForm() {
  const [country, setCountry] = useState('');
  const [city, setCity] = useState('');
  const [district, setDistrict] = useState('');

  const shippingCost = country && city && district
    ? calculateShipping(country, city, district)
    : 0;

  function handleCountryChange(newCountry: string) {
    setCountry(newCountry);
    setCity('');
    setDistrict('');
  }

  function handleCityChange(newCity: string) {
    setCity(newCity);
    setDistrict('');
  }

  // ...
}
```

Or move everything into one useReducer call.

But React is smart and batches all three `setState` calls in the event handler into one render. The shipping cost is derived during rendering because it can be calculated from the existing state. You have zero effects.

## Subscribing to external stores

```
function useOnlineStatus() {
  const [isOnline, setIsOnline] = useState(true);

  useEffect(() => {
    function handleChange() {
      setIsOnline(navigator.onLine);
    }

    window.addEventListener('online', handleChange);
    window.addEventListener('offline', handleChange);
    return () => {
      window.removeEventListener('online', handleChange);
      window.removeEventListener('offline', handleChange);
    };
  }, []);

  return isOnline;
}
```

This looks right. You’re communicating with an external system (the browser’s network status), you have cleanup, and the dependency array is correct.

But React has `useSyncExternalStore` for exactly this pattern.

```
// gets the same function reference on every render
  window.addEventListener('online', callback);
  window.addEventListener('offline', callback);
  // Return a cleanup function, just like useEffect would
  return () => {
    window.removeEventListener('online', callback);
    window.removeEventListener('offline', callback);
  };
}

function useOnlineStatus() {
  return useSyncExternalStore(
    () => navigator.onLine,  // How to read the value in the browser
    () => true               // What to return during server rendering
  );
}
```

Once you see this pattern once, every `useSyncExternalStore` call looks the same.

The version with `useEffect` works, but `useSyncExternalStore` is safer in one specific way: it prevents a problem called “tearing” during concurrent renders.

That’s when React renders part of the tree with one value and another part with a different value because the external data changed mid-render.

With `useEffect`, you’d never detect this until your app gets complex enough for React to split work across frames. With `useSyncExternalStore`, React handles it for you.

## Analytics and event tracking

Sending an analytics event when a component mounts is a valid effect. The component appeared on screen, and you want to record that.

The “why” is correct: this runs because the user *saw* something.

```
useEffect(() => {
  trackPageView('/dashboard');
}, []);
```

That’s fine.

What’s not fine is tracking user actions with effects:

```
const [lastAction, setLastAction] = useState('');

useEffect(() => {
  if (lastAction) {
    trackEvent('user_action', { action: lastAction });
  }
}, [lastAction]);

function handleAddToCart() {
  addToCart(product);
  setLastAction('add_to_cart');
}
```

The developer didn’t want to duplicate the `trackEvent` call across multiple handlers, so they centralized it in an effect.

But this means the tracking fires after a render, loses the event context (which button, what timestamp, what was the event object), and breaks if the same action is dispatched twice in a row (same state value, effect doesn’t re-fire).

Track actions where they happen:

```
function handleAddToCart() {
  addToCart(product);
  trackEvent('add_to_cart', { productId: product.id });
}

function handleWishlist() {
  addToWishlist(product);
  trackEvent('add_to_wishlist', { productId: product.id });
}
```

If you need shared logic, extract it into a function.

## When useEffect IS appropriate

I don’t want to leave the impression that `useEffect` is bad. It’s a tool with a specific purpose: synchronizing React with things it doesn’t control.

WebSocket connections. You open the connection on mount, close it on unmount. The WebSocket server is an external system.

Third-party widget integration. You’re initializing a map library or a rich text editor that manages its own DOM. The library is an external system.

DOM measurements. You need the rendered size or position of an element to position something else. The DOM is an external system during layout.

One important detail here: use `useLayoutEffect`, not `useEffect`. The regular `useEffect` runs after the browser paints, so the user sees a flash of the unadjusted layout before the measurement kicks in. `useLayoutEffect` runs after the DOM update but before paint, so the adjustment happens invisibly.

Browser API subscriptions with cleanup. `IntersectionObserver`, `ResizeObserver`, media query listeners. These are browser APIs that React doesn’t manage.

Here’s what a well-organized effect looks like:

```
function ChatRoom({ roomId }) {
  useEffect(function connectToChatRoom() {
    const connection = createConnection(roomId);
    connection.connect();

    return function disconnectFromChatRoom() {
      connection.disconnect();
    };
  }, [roomId]);

  return <Chat />;
}
```

Named function so you can see what it does at a glance. A cleanup function that undoes the setup. A dependency array that lists the value it depends on.

When `roomId` changes, React disconnects from the old room and connects to the new one.

## Enforce it

If you want to catch these patterns mechanically, there’s an ESLint plugin for it: `eslint-plugin-react-you-might-not-need-an-effect`.

```
npm install --save-dev eslint-plugin-react-you-might-not-need-an-effect
```

```
// eslint.config.js
import reactYouMightNotNeedAnEffect from 'eslint-plugin-react-you-might-not-need-an-effect';

export default [
  reactYouMightNotNeedAnEffect.configs.recommended,
];
```

It analyzes state, props, refs, and their upstream sources to flag effects that are doing work that belongs elsewhere.

It’s not exhaustive. The ways to misuse an effect are practically infinite. But it catches the common ones, and more importantly, it keeps catching them after the team member who read this article leaves the project.

React’s own `eslint-plugin-react-hooks` also recently added a `set-state-in-effect` rule that flags synchronous `setState` calls inside effects.

Between the two, you cover a lot of ground.

## The mental model

The decision tree at the top of this article is really just one question asked five different ways. Is this an external system? No? Then you don’t need an effect for it.

The hard part isn’t understanding the rule. The hard part is that `useEffect` was the first escape hatch most of us learned, and it’s the one we reach for by default. Defaults are hard to override.

There’s a practical reason to care beyond performance.

React 18+ Strict Mode fires every effect twice in development to surface cleanup bugs. If your component has unnecessary effects that set state on mount without cleanup, Strict Mode makes them fire, unmount, and fire again.

I’ve watched teams disable Strict Mode entirely to “fix” this instead of fixing the effects.

Every unnecessary effect is an extra render pass, an extra place for bugs to hide, and an extra thing the next person reading your code has to understand.

Removing them makes your components faster and easier to read.

## For AI

If you’re using an AI coding assistant, whether it’s Claude Code, Copilot, Cursor, or anything else, you should know that AI models have a strong predisposition toward `useEffect`.

It’s one of the most common patterns in training data, and when in doubt, the model will reach for it the same way a junior developer would: “I need something to happen, so I’ll put it in an effect.”

### If you use Claude Code

I’ve packaged this decision tree as a Claude Code skill you can install in two commands.

It’s part of the [react-tips-skill](https://github.com/Cst2989/react-tips-skill) plugin, which also includes the skill from my [10 React tips](https://neciudan.dev/10-react-tips-that-actually-matter) article.

Add the marketplace and install the plugin:

```
/plugin marketplace add Cst2989/react-tips-skill
/plugin install react-tips@neciudan.dev
```

Once installed, you get two skills:

- `react-tips` — 10 React patterns and anti-patterns for state management, performance, hooks, and component design
- `no-unnecessary-effects` — the full decision tree from this article, applied automatically every time the AI is about to write a `useEffect`

The `no-unnecessary-effects` skill forces the AI to answer the same question you should be asking: **“Is this syncing with an external system?”** If the answer is no, it walks through each case (derived state, event handling, state resets, data fetching, parent notifications, effect chains, external stores) and uses the correct alternative instead.

You can invoke it directly with `/react-tips:no-unnecessary-effects`, but it also activates automatically when Claude is writing or reviewing React components.

If you’re not using Claude Code, you can still use the same approach. The core of the skill is a markdown file that encodes the decision tree as instructions. Here’s a condensed version you can adapt for `.cursorrules`, Copilot instructions, or any system prompt:

```
# Before Writing useEffect

Every time you are about to write a useEffect, stop and answer:
**Is this syncing with an external system?**

External systems: WebSocket, browser APIs (IntersectionObserver,
navigator.onLine), third-party libraries, DOM measurements, timers.

NOT external systems: props, state, derived values, user events.

## Check each case before writing the effect:

1. **Transforming data?** → Compute inline, or useMemo if expensive
2. **Responding to a user event?** → Put logic in the event handler
3. **Resetting state on prop change?** → Use the key prop
4. **Fetching data?** → Use TanStack Query; if useEffect, add cleanup
5. **Notifying a parent?** → Call callback in the event handler
6. **Chaining effects?** → Move cascade into one event handler
7. **Subscribing to external store?** → useSyncExternalStore

If none apply and the answer is genuinely "yes, external system,"
then useEffect is correct.

## Rules
- NEVER write useEffect(() => setSomething(derived), [dep])
- NEVER use useEffect for click/submit/change events
- NEVER use useEffect to reset state without considering key prop
- ALWAYS add cleanup when subscribing to external systems
- ALWAYS name effect functions for readability
```

The key insight is that the skill doesn’t just say “don’t use effects.” It gives the AI the same decision tree a human would use. The AI checks each case, finds the one that matches, and uses the correct alternative.

You can test whether it’s working by asking your AI to build a component with a search filter, a form submission, or dependent dropdowns. Without the skill, you’ll almost certainly get `useEffect`.

With it, you should get derived values, event handlers, and `key` props instead.

## References

⚡ LIVE · APRIL 27 – 30 · ONLY 3 SESSIONS LEFT

![](/images/lizard/lizard.png) 

🏆 SOLD OUT IN SINGAPORE · ATHENS · LONDON

### From Lizard to Wizard

4 hours. Algorithms, system design, security, observability, AI.  
The workshop that turns mid engineers into senior ones.

€250 4-HOUR INTENSIVE

 [Pick your date →](/lizard-to-wizard/signup) 

Spots are vanishing. Don't be the one who waited.

 ![](/images/lizard/wizard.png)

![Author](/images/logo.png)

### Discover more from The Neciu Dan Newsletter

A weekly column on Tech & Education, startup building and occasional hot takes.
