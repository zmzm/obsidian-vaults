---
type: twir-item
issue: 304
item: 9
item_type: item
date: 2026-11-04
source: https://ebey.dev/blog/3myyseusgd22h
tags:
  - "Actions"
status: auto
quality: keep
---

[[2026-11-04-TWIR-304|Index]]

# Item 9: Async React & Progressive Server Actions

Source: [https://ebey.dev/blog/3myyseusgd22h](https://ebey.dev/blog/3myyseusgd22h)

Summary:
This article explores how React's async APIs (useTransition, useActionState, useOptimistic) and server actions enable progressive enhancement and improved user experience. It demonstrates how to implement pending and optimistic UI states, both on the client and server, while maintaining compatibility with non-JavaScript environments. The post also highlights common pitfalls that can break progressive enhancement.

Key takeaways:
- React's async hooks enable seamless pending and optimistic states in forms.
- Server actions can be wired directly into <form> for progressive enhancement.
- useActionState and useOptimistic simplify async state management.
- Careful wiring is needed to ensure forms still work before JavaScript loads.

Recommendation:
Read fully (for practical, modern patterns in async React and progressive enhancement)

Why it matters:
for practical, modern patterns in async React and progressive enhancement

Content:
# Async React & Progressive Server Actions

Hopefully you've heard myself or others pushing for progressive enhancement these last few years. In React Router we have pushed patterns such as real `<form>` elements and exposed the platform behavior to you via hooks such as `useNavigation()` and `useFetcher()`, allowing you to respond and provide a seamless enhanced experience with native web and browser fallbacks. My unofficial motto for this has been "works before JavaScript, amazes after".

Since we started this push for fundamentals, React itself has expanded their API to allow you to build these enhanced experiences entirely within their component model.

## React `<form>`

Today, React allows us to implement server-run form actions within the component model. The following is an example that defines a form with an action that works before JavaScript.

```
function serverAction() {
  "use server";
  // ...
}

<form action={serverAction}>
  <button type="submit">Submit</button>
</form>
```

Our contract here is simply the `"use server"` directive. I know this isn't loved by everyone and I'm not trying to convince you it's good, but I want to give you another way to think about it.

Historically if we want to create a form that works before JavaScript in React, we would have to leave the component model and handle the callback in our server layer (Express, Hono, or React Router `action`). `"use server"` is this wiring built into the component model, handled by your bundler. `"use server"` simply tells `<form>` how to make a real POST request.

## Async React

Introducing server actions brought the need for React async APIs. These APIs brought React supported solutions to the questions of

### Pending States

React introduced the `useTransition` hook to much confusion. Many people have tried to describe what a React transition is and how they work with things like "lets you render a part of the UI in the background", "helps you keep your React app responsive during heavy updates".

The common use case, and IMO the way to think about it: "Is async work happening?".

```
const [state, setState] = useState();
const [loading, loadingWhenRunning] = useTransition();

function handleSubmit(event) {
  const formData = new FormData(event.currentTarget);
  loadingWhenRunning(async () => {
    const result = await longTask(formData.get("name"));
    setState(result);
  });
}

<form onSubmit={handleSubmit}>
  <button type="submit">
    {loading ? "Loading" : "Submit"}
  </button>
  {state?.name ? `Hello, ${state.name}` : null}
</form>
```

Straightforward enough, but a bit of boilerplate. This is where `useActionState` and `<form action>` come in.

```
const [state, action, loading] = useActionState(
  async (previousState, formData) => {
    return await longTask(formData.get("name"));
  },
  null,
);

<form action={action}>
  <button type="submit">
    {loading ? "Loading" : "Submit"}
  </button>
  {state?.name ? `Hello, ${state.name}` : null}
</form>
```

`useActionState` is another hook people seem to have a hard time describing, saying things like "lets you update state with side effects using Actions."... It's an async `useReducer`.

### Optimistic UI

Pending states can be a decent user experience, but what's the point of a fully client hydrated app with local state if all that state is doing is adding and removing a class from an element? The React team knows this is not the end UX and has the solution in the form of `useOptimistic`.

```
const [state_, action_, loading] = useActionState(
  async (_, formData) => {
    return await longTask(formData.get("name"));
  },
  null,
);

const [state, setOptimisticState] = useOptimistic(state_);

const action = (formData) => {
  setOptimisticState({ name: formData.get("name") });
  action_(formData);
};

<form action={action}>
  <button type="submit">
    {loading ? "Loading" : "Submit"}
  </button>
  {state?.name ? `Hello, ${state.name}` : null}
</form>
```

Out of all the new hooks, `useOptimistic` is described well with "that lets you optimistically update the UI". The one thing I'd add is "lets you optimistically update the UI when async work is active", as its state only lives for the lifetime of the transition (async work).

The above code does two main things:

## Server Action State

All of the above examples are of React's new async features running on the client. This alone will enable many apps to re-think their data loading, pending and optimistic states, and overall composability of how they can author components that interact with async business logic, but we are interested in how we can use these to enhance our server actions and keep our application interactive before JavaScript.

Good news right off the bat is we can utilize `useActionState` and server actions to achieve pending states just like we did for the client.

```
const [state, action, loading] = useActionState(
  serverAction,
  null,
);

<form action={action}>
  <button type="submit">
    {loading ? "Loading" : "Submit"}
  </button>
  {state?.name ? `Hello, ${state.name}` : null}
</form>
```

The above form still works before JavaScript, but now has a pending state for immediate user feedback. Now let's investigate a snippet that breaks the ability to run before JavaScript.

```
const [state, action, loading] = useActionState(
  async (previousState, formData) => {
    return await serverAction(previousState, formData)
  },
  null,
);

<form action={action}>
  <button type="submit">
    {loading ? "Loading" : "Submit"}
  </button>
  {state?.name ? `Hello, ${state.name}` : null}
</form>
```

Did you spot it? We have passed a client defined function into `useActionState` and called the `serverAction` ourselves. This form will still work after hydration, but because we are no longer passing the `serverAction` directly through, the `<form>` no longer knows how to submit before JavaScript.

## Optimistic Server Actions

Just like server action state, optimistic server actions look suspiciously like their client version. There is, however, one more thing we have to take into account for our actions to continue to run before JavaScript.

```
const [state_, action, loading] = useActionState(
  serverAction,
  null,
);

const [state, setOptimisticState] = useOptimistic(state_);

const enhancedAction = (formData) => {
  setOptimisticState({ name: formData.get("name") });
  action(formData);
};

<form action={enhancedAction}>
  <button type="submit">
    {loading ? "Loading" : "Submit"}
  </button>
  {state?.name ? `Hello, ${state.name}` : null}
</form>
```

Did you spot where we've broken the ability to submit before JavaScript again? We are passing a client defined `action` to the `<form>`. This is the one part where server action DX has to fall outside of React's built-in hooks and we have to introduce you to the `useHydrated` hook. Up to this point we've gotten by with a single, unified model with UI that responds immediately regardless of whether actions run on the client or server. For brevity, you can find the hook implementation in [remix-utils](https://github.com/sergiodxa/remix-utils/blob/777bbf39c2a131633925aa4963af20abfccf620a/src/react/use-hydrated.ts).

Enabling the form to submit before JavaScript is as simple as conditionally passing the `<form action>`.

```
const [state_, action, loading] = useActionState(
  serverAction,
  null,
);

const [state, setOptimisticState] = useOptimistic(state_);

const enhancedAction = (formData) => {
  setOptimisticState({ name: formData.get("name") });
  action(formData);
};

const hydrated = useHydrated();

<form action={hydrated ? enhancedAction : action}>
  <button type="submit">
    {loading ? "Loading" : "Submit"}
  </button>
  {state?.name ? `Hello, ${state.name}` : null}
</form>
```

If you audit the client and server action optimistic code you'll notice the only difference is the useHydrated`()`, and that's an amazingly far way for a historically client-focused library like React to come.

## Do your server actions run before JavaScript?

They do, as long as your server action always end up as the `<form action>`. That's the whole rule. With it, React now has supported patterns for async experiences that work before JavaScript and amaze after. For me, that's the real payoff: React's unified component model finally reaches the part of the web its community left behind.
