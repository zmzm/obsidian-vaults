---
type: twir-item
issue: 272
item: 8
item_type: item
date: 2026-03-11
source: https://dev.to/link2twenty/react-singletons-arent-as-evil-as-you-think-44m8
tags:
  - "TypeScript"
status: auto
quality: keep
---

[[2026-03-11-TWIR-272|Index]]

# Item 8: React: Singletons aren't as evil as you think

Source: [https://dev.to/link2twenty/react-singletons-arent-as-evil-as-you-think-44m8](https://dev.to/link2twenty/react-singletons-arent-as-evil-as-you-think-44m8)

Summary:
The article challenges the negative perception of singletons in React, arguing that they can be a powerful and lightweight solution for global state when implemented thoughtfully. It demonstrates how to synchronize singleton state with React components using event listeners, and advocates for leveraging native JavaScript classes (e.g., extending EventTarget) for clean, type-safe implementations. A practical example is provided by building a toast notification manager as a singleton.

Key takeaways:
- Singletons, when paired with event-driven updates, can provide efficient global state management in React.
- Extending native classes like EventTarget enables type-safe, event-based communication between singletons and components.
- The approach avoids unnecessary re-renders and package bloat, relying on browser-native APIs.
- Practical patterns and TypeScript types are illustrated for robust singleton design.

Recommendation:
Read fully (read fully for implementation details or if considering singletons for global state)

Why it matters:
read fully for implementation details or if considering singletons for global state

Content:
# React: Singletons aren't as evil as you think

In the world of React, the humble singleton gets a bit of a bad rap. It is often dismissed as a messy shortcut to global state, one that is difficult to track and even harder to test. But what if I told you the singleton is not the architectural terror you have been led to believe? What if I showed you it is actually powerful, lightweight and remarkably simple to implement? You might think me mad, but I am about to convince you that singletons are not the villains of the story.

## The Singleton Scepticism

Historically, if you wanted to pull data from a singleton in React, you often had to wait for the app to re-render for some other reason. You might have seen a manual sync button or a poll used to bridge the gap, but it was rarely pretty.

```
import { useState, useEffect, useCallback } from 'react';
import SomeSingleton from '@/singletons/some';

export function ReactElement() {
  const [singletonData, setSingletonData] = useState(SomeSingleton.data || null);

  /**
   * Sync singleton and state
   */
  const handleRefresh = useCallback(() => {
    setSingletonData(SomeSingleton.data || null)
  }, []);

  // Trigger refresh every 5 seconds
  useEffect(() => {
    const interval = window.setInterval(handleRefresh, 5000);

    return () => window.clearInterval(interval);
  }, [handleRefresh]);

  return (
    <div>
      <span>{singletonData || 'N/A'}</span>
      <button onClick={handleRefresh}>Manual Refresh</button>
    </div>
  )
}
```

Enter fullscreen mode

Exit fullscreen mode

If this is what you are imagining when I say singletons are easy to implement, I understand the confusion. This is not a good way to implement them and it was not a good way back then either. Let me show you a much nicer approach.

```
import { useState, useEffect, useCallback } from 'react';
import SomeSingleton from '@/singletons/some';

export function ReactElement() {
  const [singletonData, setSingletonData] = useState(SomeSingleton.data || null);

  // Update the state as soon as things change in the singleton
  useEffect(() => {
    const ac = new AbortController();

    SomeSingleton.addEventListener('change', ({detail})=>{
      setSingletonData(detail);
    }, {signal: ac.signal})

    return () => ac.abort();
  }, []);

  return (
    <div>
      <span>{singletonData || 'N/A'}</span>
    </div>
  )
}
```

Enter fullscreen mode

Exit fullscreen mode

This is already much cleaner, more readable and less prone to falling behind. It does, however, require some work in the singleton to make the events happen and we will get to that shortly.

Even though this is now perfectly usable, there are a few more tips and tricks we can deploy to make it feel like native React state.

## The Simplicity of Classes

Classes are native to JavaScript and as such have no extra package bloat to worry about. You simply define your class, initialise it and off you go.

Believe it or not, many parts of the language you probably use every day are classes that can be extended, such as `Error`, `Array`, `Map` or even `HTMLElement`. Having access to so many pre-made classes means that if we see a behaviour we want to use, we do not have to rewrite it or ship a library for it. We can simply extend the native class and it is there, in the browser, waiting for us.

That is the pitch: classes are powerful because we can extend native behaviour, lightweight because they are built into the engine and easy to implement because the documentation is simply the web spec.

### Typed Target Event

Earlier I mentioned wanting our singletons to be able to fire events. We can extend `EventTarget` to do exactly this. However, if you are using TypeScript (and I hope you are) the native implementation can feel a little loose. I have previously written about how to make `EventTarget` a bit more type-safe to ensure your messaging remains robust.

## A Problem to Solve

Let us come up with a problem that we do not necessarily need to solve, simply to show off what we can do. The problem I have chosen is a toast manager. We definitely do not need to build one from scratch given that [sonner](https://sonner.emilkowal.ski/) and [toastify](https://fkhadra.github.io/react-toastify/introduction/) both exist and are excellent, but this will go a lot smoother with a tangible demo.

Building a notification system is the perfect test for our singleton architecture. It needs to be accessible from any part of the application, it must handle its own timers and it should be able to trigger UI updates without being coupled to a specific component tree.

### The Singleton

As discussed, we are going to extend my `TypedEventTarget` class, which itself is built on the native `EventTarget` class. We are going to need a list of toasts, a method to add toasts, a method to remove toasts early and a timer that will remove toasts after enough time has elapsed. We will also have to fire an event every time the list of toasts has changed. Simple enough.

First, let us define some types. I am doing this in TypeScript but you do not have to; feel free to skip this bit if you prefer.

```
export interface Toast {
  id: string;
  message: string;
  type: "info" | "success" | "loading" | "error";
  action?: {
    label: string;
    callback: () => void;
  };
}

type ToastEvents = {
  changed: void;
};
```

Enter fullscreen mode

Exit fullscreen mode

Now that we have our types, we know what a toast object looks like and what events will be fired. Let us set up the class next. We know it will extend `TypedEventTarget` and will have some private internals to hide away.

```
class ToastManager extends TypedEventTarget<ToastEvents> {
  private _toasts: Toast[] = [];
  private _timers = new Map<string, number>();
}
```

Enter fullscreen mode

Exit fullscreen mode

This is a good start, but our `_toasts` property is private, meaning we cannot access it from outside the class, and currently we would have to manually dispatch an event every time we update it. Getters and setters to the rescue.

```
get toasts() {
  return this._toasts;
}

private set toasts(value: Toast[]) {
  this._toasts = [...value];
  this.dispatchEvent("changed");
}
```

Enter fullscreen mode

Exit fullscreen mode

Now we can read our `toasts` property and even update it internally, but we still cannot control this class externally. We need to add some methods.

```
// add or update a toast item
add = (toast: Omit<Toast, "id"> & { id?: string }, duration = 3000) => {
  const id = toast.id ?? Math.random().toString(36).substring(2, 9);
  this.clearTimer(id);

  const newToast = { ...toast, id };
  const exists = this.toasts.some((t) => t.id === id);

  if (exists) {
    this.toasts = this.toasts.map((t) => (t.id === id ? newToast : t));
  } else {
    this.toasts = [...this.toasts, newToast];
  }

  if (duration > 0) {
    const timer = window.setTimeout(() => this.remove(id), duration);
    this._timers.set(id, timer);
  }

  return id;
};

// remove a toast and its timer
remove = (id: string) => {
  this.clearTimer(id);
  const index = this.toasts.findIndex(({ id: _id }) => _id === id);

  if (index >= 0) {
    this.toasts = this.toasts.filter(({ id: _id }) => _id !== id);
  }
};

// remove a timer
private clearTimer(id: string) {
  if (this._timers.has(id)) {
    clearTimeout(this._timers.get(id));
    this._timers.delete(id);
  }
}
```

Enter fullscreen mode

Exit fullscreen mode

Finally, we instantiate our class and export it.

```
export const toastManager = new ToastManager();
```

Enter fullscreen mode

Exit fullscreen mode

I do not know about you, but this does not feel like a lot of code. The addition of TypeScript means we get the safety net of auto-completion and type checking without the bloat of a heavy library.

### The Connection

When I showed you how to connect to a singleton with a `useEffect` earlier, I mentioned that it did not quite feel like it was a natural part of React. This is where `useSyncExternalStore` comes in. It allows us to define a subscription to an external source and a function to retrieve a snapshot of that state, handling the synchronisation for us.

First, we need to create the functions to pass to the hook.

```
import { toastManager } from '@/singletons/toastManager';

// Add an event listener
  const ac = new AbortController();

  toastManager.addEventListener("changed", callback, {
    signal: ac.signal,
  });

  return () => ac.abort();
};

// Get the state
const getSnapshot = () => toastManager.toasts;
```

Enter fullscreen mode

Exit fullscreen mode

Now we can put it all together inside a component.

```
import { useSyncExternalStore } from 'react';

export default function ToastContainer() {

  return (
    <ul>
      {toastList.map(({id, message}) => (<li key={id}>{message}</li>))}
    </ul>
  );
}
```

Enter fullscreen mode

Exit fullscreen mode

This is a somewhat simplistic implementation, but it demonstrates the core principle. We have full access to the data inside the singleton and it triggers a React render cycle whenever the internal state updates. By using `useSyncExternalStore`, we ensure that our UI is always in sync with our source of truth, without having to manually manage state variables or worry about stale closures.

### The Demo

There we have it: a toast manager singleton that feeds into React whenever it needs to, allowing for the controlling and monitoring of toasts from anywhere in the application. I have not gone as far as making a feature-complete product and it certainly will not win any awards for its looks, but please do enjoy the demo.

## Closing words

Have I convinced you, or are you still against singletons? Perhaps you were already a fan. I am happy to continue the discussion in the comments. You might be surprised to know that the new, at the time of writing, [TanStack Hotkeys](https://tanstack.com/hotkeys/latest) actually works in a similar way, with a singleton controller connected to React, or indeed any other library.

Thanks for reading! If you'd like to connect, here are my [BlueSky](https://bsky.app/profile/link2twenty.bsky.social) and [LinkedIn](https://www.linkedin.com/in/andrew-bone-ba241b179/) profiles. Come say hi 😊
