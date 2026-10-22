---
type: twir-item
issue: 297
item: 6
item_type: item
date: 2026-09-16
source: https://www.brenelz.com/posts/solidjs-its-the-little-things/
tags:
  - "SolidJS"
status: auto
quality: keep
---

[[2026-09-16-TWIR-297|Index]]

# Item 6: SolidJS, It’s the Little Things

Source: [https://www.brenelz.com/posts/solidjs-its-the-little-things/](https://www.brenelz.com/posts/solidjs-its-the-little-things/)

Summary:
This article highlights small but impactful features in SolidJS 2.0, such as isPending for tracking async state, streamlined optimistic updates, and writable derived state. It compares these features to their React equivalents, noting where Solid offers more ergonomic or granular APIs. The focus is on developer experience improvements and subtle design choices that enhance productivity.

Key takeaways:
- SolidJS provides fine-grained APIs for tracking pending state, optimistic updates, and derived state overrides.
- Some patterns, like querying pending state or refreshing data, are more ergonomic in Solid compared to React.
- The article offers practical code comparisons between Solid and React for common scenarios.

Recommendation:
Summary sufficient

Content:
# SolidJS, It’s the Little Things

Today I want to walk you through a few of my favorite little things in Solid 2.0. Individually, they might seem small. Together, they make a real difference in how the framework feels to use.

Here are six small touches that make the difference:

1. Ask Your Data What’s Pending
2. Optimistic Updates with Less Wiring
3. Derived State You Can Override
4. Choose Where Each Value Is Computed
5. Server Reads as Function Calls
6. A Runtime That Explains Itself

## Ask Your Data What’s Pending

In Solid, checking whether your data is pending is a simple call to `isPending`. It takes a function that reads reactive state and reports whether that expression depends on an in-flight change. You can pass an accessor directly, like `isPending(user)`, or an expression, like `isPending(() => user().name)`.

```
import { createSignal, createMemo, isPending, Loading } from "solid-js";

function Example() {
  const [id, setId] = createSignal(1);
  const user = createMemo(() => fetchUser(id()));

  return (
    <Loading fallback={<p>Loading initial user...</p>}>
      <button onClick={() => setId(2)}>Load user 2</button>

      <p>User pending: {String(isPending(user))}</p>
      <p>ID pending: {String(isPending(id))}</p>
      <p>
        User {id()}: {user().name}
      </p>
    </Loading>
  );
}
```

The little detail I appreciate is that pending state can be queried from the data itself. I can ask whether user is pending - or whether the write to id is still waiting on downstream async work.

The equivalent in React would be something like:

```
"use client";

import { Suspense, use, useState, useTransition } from "react";
import { getUserPromise } from "./data";

function Example() {
  const [id, setId] = useState(1);
  const [isPending, startTransition] = useTransition();

  return (
    <>
      <button
        onClick={() => {
          startTransition(() => setId(2));
        }}
      >
        Load user 2
      </button>

      <p>Transition pending: {String(isPending)}</p>

      <Suspense fallback={<p>Loading initial user…</p>}>
        <UserDetails id={id} />
      </Suspense>
    </>
  );
}

function UserDetails({ id }: { id: number }) {
  const user = use(getUserPromise(id));

  return (
    <p>
      User {id}: {user.name}
    </p>
  );
}
```

Notice we can’t really ask if the `user` is pending. We might not even know the setting of the id triggered it.

## Optimistic Updates with Less Wiring

```
import { createOptimisticStore, action, refresh } from "solid-js";

function Example() {
  const [messages, setMessages] = createOptimisticStore(
    () => getMessages(),
    []
  );

  const addMessage = action(function* (message) {
    setMessages(m => {
      m.push(message);
    });

    yield saveMessage(message);
    refresh(messages);
  });
}
```

In Solid doing optimistic updates is a breeze. You see a few different things align nicely. First of all you can derive the optimistic straight from an API call. In this case `getMessages`. This will be a treated as the truth from the server. It’s initial value will be the messages it got, and then you can mutate on top of it the optimistic updates. In this case a `push` to the end.

When the action finishes, the optimistic layer is removed and the refreshed server data becomes authoritative. If that data reconciles to the same values already being displayed, Solid can avoid further DOM updates.

> Note: `function*` creates a generator, allowing Solid’s action runner to restore its context when execution resumes after a `yield`. React currently requires another `startTransition` to mark state updates after an `await` as transition updates.

React’s `useOptimistic` also takes an existing value as its source of truth. It doesn’t manage the API call that produces that value, so we need to connect the fetching and refreshing ourselves. In this example, the initial data comes from a parent through `initialMessages`.

```
import { startTransition, useOptimistic, useState } from "react";

function Example({ initialMessages = [] }) {
  const [messages, setMessages] = useState(initialMessages);

  const [optimisticMessages, setOptimisticMessages] = useOptimistic(messages);

  function addMessage(message) {
    startTransition(async () => {
      setOptimisticMessages(current => [...current, message]);

      await saveMessage(message);
      const refreshedMessages = await getMessages();

      startTransition(() => {
        setMessages(refreshedMessages);
      });
    });
  }
}
```

I’ve also come to appreciate expressing the change as a mutation: `m.push(message)` instead of `[...current, message]`. Solid’s store tracks those writes at a granular level, so it can update the parts of the UI that depend on what changed.

The other interesting thing shown above is that we don’t have a simple `refresh(messages)` ability and we need to call `getMessages()` again even though we presumably called it somewhere else before to get the `initialMessages`.

## Derived State You Can Override

Having writable derived state is easy in Solid. All you do is pass in a function to a primitive like `createSignal`. This gives you a local override of `props.name` in this example, but when `props.name` changes from above it will reset to that value.

```
import { createSignal } from "solid-js";

function Example(props) {
  const [name, setName] = createSignal(() => props.name);
}
```

In React, this takes a bit more wiring. `useState` uses `props.name` as its initial value, but later prop changes don’t automatically reset the state. Setting state during render might look unusual, but a guarded update like this is a [documented](https://react.dev/learn/you-might-not-need-an-effect#adjusting-some-state-when-a-prop-changes) pattern for adjusting state when props change. React retries the component before rendering its children, keeping the reset synchronized with the prop change.

```
import { useState } from "react";

function Example(props) {
  const [name, setName] = useState(props.name);
  const [previousName, setPreviousName] = useState(props.name);

  if (props.name !== previousName) {
    setPreviousName(props.name);
    setName(props.name);
  }
}
```

Solid lets me express exactly what I want: derive from a prop, allow a local override, and reset when the source changes. That’s what I call good DX.

## Choose Where Each Value Is Computed

Solid 2 lets you configure server rendering and hydration for individual reactive sources. For example, a saved draft might live in `localStorage`, which the server can’t access.

With `ssrSource: "client"`, we can tell Solid to run that computation only in the browser, after hydration.

```
import { createMemo, Loading } from "solid-js";

function DraftPreview(props) {
  const draft = createMemo(
    () => localStorage.getItem(`draft:${props.documentId}`),
    { ssrSource: "client" }
  );

  return (
    <section>
      <h2>Saved draft</h2>

      <Loading fallback={<p>Checking for a saved draft...</p>}>
        <p>{draft() ?? "No saved draft."}</p>
      </Loading>
    </section>
  );
}
```

On the server, Solid skips the computation and renders the `Loading` fallback. After hydration, it reads `localStorage` and displays the result.

What I like is that this decision lives right beside the data source. I can express that this particular value belongs to the browser.

React lets you do something similar with `use(browser())`. Here, the decision applies to the component calling it. To keep it server-rendered, we move the browser-only read into `DraftContent` and wrap that component in `Suspense`.

```
"use client";

import { Suspense, use } from "react";
import { browser } from "react-dom";

function DraftContent({ documentId }) {
  use(browser("The saved draft is stored in localStorage."));

  const draft = localStorage.getItem(`draft:${documentId}`);

  return <p>{draft ?? "No saved draft."}</p>;
}

function DraftPreview({ documentId }) {
  return (
    <section>
      <h2>Saved draft</h2>

      <Suspense fallback={<p>Checking for a saved draft...</p>}>
        <DraftContent documentId={documentId} />
      </Suspense>
    </section>
  );
}
```

What I appreciate about Solid is being able to attach that behavior directly to the data source. In this example, I don’t need another component just to express where one value should be computed.

## Server Reads as Function Calls

Solid 2 lets you use server functions for reads as well as mutations. With the `GET` helper, you can make a server function callable over HTTP GET while keeping the ergonomics of a normal function call.

```
import { GET } from "@solidjs/web/server-functions";
import { db } from "~/lib/db";

export const getMessages = GET(async () => {
  "use server";

  return db.message.findMany();
});
```

From the client, we call it like any other async function:

```
const messages = await getMessages();
```

Solid handles the endpoint, request serialization, and response decoding. The database access stays on the server, and the function’s argument and return types carry through to the caller.

I like that the same server function model covers both reads and writes, while letting the HTTP method reflect the operation.

React’s Server Functions are primarily designed for mutations. In Next.js, client calls use POST, while reads commonly go through Server Components or API routes. Server Components bring their own benefits, but they also introduce a different architectural model. I like that Solid lets me keep the same typed function call model for reads and writes, with GET available for reads.

> Note: TanStack Start also provides GET server functions for React, offering similar ergonomics without requiring React Server Components.

## A Runtime That Explains Itself

Solid 2 also puts more effort into explaining when something isn’t behaving the way you intended.

A common mistake is reading a reactive value at the top level of a component:

```
function Greeting(props) {
  const name = props.name;

  return <h1>Hello {name}</h1>;
}
```

Because Solid’s component function runs once, this captures the current value of `props.name`. Updating the prop later won’t update the greeting.

In development, Solid reports a `STRICT_READ_UNTRACKED` warning explaining that the read won’t update and should move into a tracking scope.

The fix is straightforward:

```
function Greeting(props) {
  return <h1>Hello {props.name}</h1>;
}
```

Now the read happens inside JSX, where Solid tracks it.

Solid also has an opt-in attribution engine for deeper runtime analysis.

In development, this can report why computations reran, tracing changes through the reactive graph back to their source. It can also flag patterns such as excessive subscriptions, sequential async waterfalls, and effects that feed their own inputs.

Good DX includes helping me understand where I went wrong, and giving me a useful path to fixing it.

## Conclusion

These are the little things that keep drawing me to Solid. I can ask the data whether it’s pending, layer optimistic changes over server truth, and express where a value should be computed. The runtime even helps explain when I get those relationships wrong. Each detail is small, but together they make Solid feel thoughtfully designed.
