---
type: twir-item
issue: 274
item: 6
item_type: item
date: 2026-03-25
source: https://neciudan.dev/name-your-effects
tags:
  - "useEffect"
status: auto
quality: keep
---

[[2026-03-25-TWIR-274|Index]]

# Item 6: Start naming your useEffect functions, you will thank me later

Source: [https://neciudan.dev/name-your-effects](https://neciudan.dev/name-your-effects)

Summary:
The article advocates naming functions passed to useEffect for improved readability and maintainability. Anonymous arrow functions in useEffect obscure intent, making code harder to review and understand, especially in large components. Naming effect functions clarifies their purpose at a glance and streamlines code reviews.

Key takeaways:
- Named functions in useEffect make component logic easier to follow.
- Improves code review speed and reduces cognitive load.
- Simple syntax change with significant readability benefits.
- Encouraged as a best practice for teams and large codebases.

Recommendation:
Read fully (read fully for practical examples or to advocate for this practice in your team)

Why it matters:
read fully for practical examples or to advocate for this practice in your team

Content:
# Start naming your useEffect functions, you will thank me later

Last month, I opened a pull request from a colleague.

A component I’d never seen before, about 200 lines, handling inventory synchronization with a warehouse API. It had four `useEffect` calls. I spent a solid minute reading through each one, tracing the dependency arrays, reconstructing which state belonged to which effect, and what triggered what.

I’ve done this a hundred times. You probably have too.

The thing that frustrated me wasn’t that the code was bad. It was well written, and the effects were correctly separated by concern.

But I still had to read every line of every effect to understand what the component was doing, because `useEffect(() => {` tells you absolutely nothing about intent. It tells you *when* code runs. It doesn’t tell you *why*.

We inherited this, in a way, from the class component era. Back when we only had `componentDidMount` and `componentDidUpdate`, there was literally only one place to put side-effect code per lifecycle event.

That constraint bred a mental model where the *where* of your code told you the *when*, and you relied on comments or careful reading for the *why*.

Hooks freed us from the lifecycle constraint, but the anonymous arrow function replaced it with a different kind of opacity.

Instead of one giant lifecycle method, we now have six anonymous closures in a row, each one requiring you to read the implementation to know what it does.

I started naming my effect functions about a year ago. It’s the smallest change I’ve made to how I write React, and it’s had the most disproportionate impact on how I read it.

## The Problem

Here’s a simplified version of that inventory component:

```
function InventorySync({ warehouseId, locationId, onStockChange }) {
  const [stock, setStock] = useState<StockLevel[]>([]);
  const [connected, setConnected] = useState(false);
  const prevLocationId = useRef(locationId);

  useEffect(() => {
    const ws = new WebSocket(`wss://inventory.api/ws/${warehouseId}`);
    ws.onopen = () => setConnected(true);
    ws.onclose = () => setConnected(false);
    ws.onmessage = (event) => {
      const update = JSON.parse(event.data);
      setStock(prev => prev.map(s =>
        s.sku === update.sku ? { ...s, quantity: update.quantity } : s
      ));
    };
    return () => ws.close();
  }, [warehouseId]);

  useEffect(() => {
    if (!connected) return;
    fetch(`/api/warehouses/${warehouseId}/stock?location=${locationId}`)
      .then(res => res.json())
      .then(setStock);
  }, [warehouseId, locationId, connected]);

  useEffect(() => {
    if (prevLocationId.current !== locationId) {
      setStock([]);
      prevLocationId.current = locationId;
    }
  }, [locationId]);

  useEffect(() => {
    if (stock.length > 0) {
      onStockChange(stock);
    }
  }, [stock, onStockChange]);

  // ... render
}
```

Four effects. What does each one do? The first one sets up… a WebSocket? Okay. The second one fetches something… when `connected` changes? The third one resets the stock when the location changes. The fourth one… calls a callback from props whenever stock updates.

Your brain just did four compilation passes.

In a code review on GitHub, where you can’t hover for type info, and you’re scanning a diff with limited context, this is where things slow down.

Multiply it by every component in a pull request.

Now, try to read the same component but with some small changes:

```
function InventorySync({ warehouseId, locationId, onStockChange }) {
  const [stock, setStock] = useState<StockLevel[]>([]);
  const [connected, setConnected] = useState(false);
  const prevLocationId = useRef(locationId);

  useEffect(function connectToInventoryWebSocket() {
    const ws = new WebSocket(`wss://inventory.api/ws/${warehouseId}`);
    ws.onopen = () => setConnected(true);
    ws.onclose = () => setConnected(false);
    ws.onmessage = (event) => {
      const update = JSON.parse(event.data);
      setStock(prev => prev.map(s =>
        s.sku === update.sku ? { ...s, quantity: update.quantity } : s
      ));
    };
    return () => ws.close();
  }, [warehouseId]);

  useEffect(function fetchInitialStock() {
    if (!connected) return;
    fetch(`/api/warehouses/${warehouseId}/stock?location=${locationId}`)
      .then(res => res.json())
      .then(setStock);
  }, [warehouseId, locationId, connected]);

  useEffect(function resetStockOnLocationChange() {
    if (prevLocationId.current !== locationId) {
      setStock([]);
      prevLocationId.current = locationId;
    }
  }, [locationId]);

  useEffect(function notifyParentOfStockUpdate() {
    if (stock.length > 0) {
      onStockChange(stock);
    }
  }, [stock, onStockChange]);

  // ... render
}
```

Now I can skim four function names and understand the entire data flow: connect to the WebSocket, fetch the initial stock, reset on location change, notify the parent.

I don’t need to read a single line of code unless I’m debugging something specific.

The change is just syntax. Instead of passing an anonymous arrow function to `useEffect`, you pass a named function expression:

```
// anonymous arrow (what everyone writes)
useEffect(() => {
  document.title = `${count} items`;
}, [count]);

// named function expression (what I'm arguing for)
useEffect(function updateDocumentTitle() {
  document.title = `${count} items`;
}, [count]);
```

You could also declare the function separately and pass it by name (`useEffect(updateDocumentTitle, [count])`), but I prefer the inline version because the name sits right at the call site. You don’t have to look up to find the function declaration.

There’s a debugging payoff, too.

When an anonymous arrow throws, your error message shows `at (anonymous) @ InventorySync.tsx:14`.

With four effects in the file, that’s useless.

A named function gives you `at connectToInventoryWebSocket @ InventorySync.tsx:14`, which tells you which effect broke without opening the file.

This matters when you’re triaging error reports in a monitoring tool like Sentry on your phone, far from your editor. It also matters in React DevTools profiling, where named functions appear with their names, and anonymous ones appear as… anonymous.

## Naming Reveals Too Much Responsibility

The readability argument is enough on its own, but something else happened when I started naming effects. It changed how I wrote them.

Try naming this:

```
useEffect(() => {
  const handleResize = () => setWidth(window.innerWidth);
  window.addEventListener('resize', handleResize);

  if (user?.preferences?.theme) {
    document.body.className = user.preferences.theme;
  }

  return () => window.removeEventListener('resize', handleResize);
}, [user?.preferences?.theme]);
```

What do you call it? `syncWidthAndApplyTheme`? That “and” is a warning sign. It means the effect is doing two unrelated things.

The moment you struggle to name an effect without using “and” or “also,” that’s the effect telling you it should be split.

```
useEffect(function trackWindowWidth() {
  const handleResize = () => setWidth(window.innerWidth);
  window.addEventListener('resize', handleResize);
  return () => window.removeEventListener('resize', handleResize);
}, []);

useEffect(function applyUserTheme() {
  if (user?.preferences?.theme) {
    document.body.className = user.preferences.theme;
  }
}, [user?.preferences?.theme]);
```

If you can’t name it clearly, it’s doing too much. React recommends splitting effects by concern rather than lifecycle timing anyway.

The name makes that principle visible in a way that comments never do, because comments rot and names get read.

This extends beyond `useEffect`. The same readability gain applies to `useCallback`, `useMemo`, and reducer functions.

Anywhere you pass an anonymous function to a hook, a name helps the next person reading the code. But `useEffect` is where it pays off the most because effects are the hardest hooks to understand at a glance. They run at non-obvious times, have hidden cleanup semantics, and require you to reconstruct their trigger dependencies.

You can name cleanup functions, too. Instead of returning an anonymous arrow, return a named function:

```
useEffect(function pollServerForUpdates() {
  const intervalId = setInterval(() => {
    fetch(`/api/status/${serverId}`)
      .then(res => res.json())
      .then(setServerStatus);
  }, 5000);

  return function stopPollingServer() {
    clearInterval(intervalId);
  };
}, [serverId]);
```

I don’t always bother with naming the cleanup because it’s usually obvious from context. But when the teardown does non-trivial work, the symmetry between `pollServerForUpdates` and `stopPollingServer` makes both halves immediately clear.

## Naming Reveals Effects That Shouldn’t Exist

Some effects resist naming, and that resistance itself is a signal.

If you find yourself reaching for something like `updateStateBasedOnOtherState` or `syncDerivedValue`, stop.

That vagueness usually means the code doesn’t belong in an effect. The naming is hard because the effect is doing something that shouldn’t be an effect.

```
// You probably don't need this
useEffect(function syncFullName() {
  setFullName(`${firstName} ${lastName}`);
}, [firstName, lastName]);

// Just derive it
const fullName = `${firstName} ${lastName}`;
```

Why is the effect version worse? Because it triggers an extra render cycle.

React renders the component, then runs the effect, which calls `setFullName`, which triggers *another* render with the updated value.

The screen updates twice instead of once, and you’ve introduced a frame where `fullName` is stale.

The derived version computes the value during render, so it’s always correct and always in sync, with zero extra work for React.

```
// You probably don't need this either
useEffect(function resetFormOnSubmit() {
  if (submitted) {
    setName('');
    setEmail('');
    setSubmitted(false);
  }
}, [submitted]);

// Put it in the event handler
function handleSubmit() {
  submitForm({ name, email });
  setName('');
  setEmail('');
}
```

The form reset is the event handler case: user clicks submit, that’s a user interaction, handle it where the interaction happens. The effect version reacts to a `submitted` flag change, and the extra hop makes the flow harder to follow.

I’ve seen components with eight or nine effects, where half were state-to-state synchronization that shouldn’t have been effects at all.

AI code-generation tools make this worse because they’ve been trained on millions of examples of effects being misused, so they confidently reproduce the same anti-patterns. The misuse feeds back into the training data, and the cycle continues.

Go back to the `InventorySync` example. That fourth effect, `notifyParentOfStockUpdate`, is a good candidate for this scrutiny.

Calling a parent callback inside an effect that reacts to state changes is one of the patterns the React docs specifically flag in *“You Might Not Need an Effect.”*

The parent could fetch the data itself, or the stock update could trigger the callback at the source (in the WebSocket handler and the fetch `.then` callback).

I kept it in the example because it’s incredibly common in real codebases, but naming it made the problem visible. `notifyParentOfStockUpdate` is honest about what it does, and that honesty is what makes you question whether it should exist.

If the best name you can come up with sounds like internal state shuffling, the code probably belongs somewhere else.

React 19 pushes this even further — Actions handle mutations, `use()` handles data fetching, and Server Components eliminate client-side effects for data loading entirely.

The effects that remain in a modern React app are the true synchronization points, and those are the ones worth naming well.

## Naming vs Custom Hooks

Kyle Shevlin wrote a great piece called “useEncapsulation,” where he argues that every use of `useEffect` should live inside a custom hook.

His reasoning starts from a real problem: as you add hooks to a component, related implementation details get separated by unrelated hook declarations.

Custom hooks fix this by putting the state, the effect, and the handlers for one concern in one place:

```
function useWindowWidth() {
  const [width, setWidth] = useState(
    typeof window !== 'undefined' ? window.innerWidth : 0
  );

  useEffect(function trackWindowWidth() {
    const handleResize = () => setWidth(window.innerWidth);
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return width;
}
```

(The `typeof window !== 'undefined'` check is there for server-side rendering frameworks like Next.js, where `window` doesn’t exist when the component first renders on the server. If you’re building a purely client-side app, you can use `window.innerWidth` directly.)

But notice something in `useWindowWidth`. I still named the `useEffect` inside the custom hook.

Custom hooks can have multiple effects, too, and when you’re debugging inside one, named functions in the stack trace still help.

Not everything needs to be a custom hook, though. Sometimes a component has a one-off effect that’s specific to its behavior and will never be reused.

Extracting it into `useCloseOnEscapeKeyForThisSpecificModal` adds indirection for no benefit. The React docs caution against premature abstraction here — function components getting longer as they do more is normal, and not every piece of logic needs to be pulled into its own file the moment it exists.

I usually apply this formula: If the effect manages its own state and might be reused, make it a custom hook. If it’s a single-use effect with no associated state, name the function and leave it inline.

In both cases, name the function. You can also extract the core logic into a separate module if you want to unit test it without rendering a component — this works well for effects that interact with third-party SDKs or complex external systems.

## Five Effects Became Three

Story time: About a year ago, I was working on a Next.js project that had a component syncing a Mapbox instance with application state. It had five effects: one to initialize the map instance, one to sync the zoom level, one to sync the map center coordinates, one to handle marker click events, and one to clean up event listeners when the selected markers changed.

Every time I opened that file, I’d spend 30 seconds re-orienting, scrolling up and down, reminding myself which anonymous effect did what.

I named them: `initializeMapSDK`, `synchronizeZoomLevel`, `synchronizeCenterPosition`, `handleMarkerInteractions`, `cleanupStaleMarkerListeners`. Immediately, I could see where to look for whatever I was debugging.

But the naming did something else.

Once I could see the five names listed out, I realized `cleanupStaleMarkerListeners` wasn’t really a separate concern from `handleMarkerInteractions`.

It was the cleanup half of the same synchronization — the setup added listeners, and this effect removed the old ones.

I merged them into a single effect with a proper cleanup return, which simplified the component. Then I realized `synchronizeZoomLevel` and `synchronizeCenterPosition` had the same dependency on the map instance being ready, and they always ran together anyway. I combined them into `synchronizeMapViewport`.

Five effects became three, and the three had clearer boundaries than the original five.

Sergio Xalambrí wrote about naming useEffect functions back in 2020. Cory House said the same thing. This isn’t new. But almost nobody does it, because the community collectively internalized `useEffect(() => {` as the only way to write effects.

We copy-paste from docs, from tutorials, from AI-generated code. The anonymous arrow is the default, and defaults are hard to escape.

The cost of switching is near zero. You don’t need a new library or a build plugin. You add a name to a function, and you’ll notice the difference the first time you open an old file and don’t have to re-read every effect to remember what it does.

Name your effects.

---

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
