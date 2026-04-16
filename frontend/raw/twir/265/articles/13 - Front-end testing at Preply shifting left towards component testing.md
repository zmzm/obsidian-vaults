---
type: twir-item
issue: 265
item: 13
item_type: item
date: 2026-01-21
source: https://www.columkelly.com/blog/use-optimistic
tags:
status: auto
quality: keep
---

[[2026-01-21-TWIR-265|Index]]

# Item 13: Front-end testing at Preply: shifting left towards component testing

Source: [https://www.columkelly.com/blog/use-optimistic](https://www.columkelly.com/blog/use-optimistic)

Summary:
Preply describes their transition from E2E-heavy testing to a component-focused strategy, aligning with new engineering principles for long-term quality and developer experience. The article details their testing culture, adoption of tools like Vitest, Storybook, and Chromatic, and the benefits of component tests for maintainability and documentation. The shift aims to balance speed with reliability and improve onboarding and collaboration across teams.

Key takeaways:
- Component testing is prioritized for maintainability, speed, and documentation benefits.
- Tools like Storybook and Chromatic are central to their workflow, with accessibility and visual regression testing.
- The approach supports both web and React Native, with custom solutions where official support is lacking.
- Reflects a broader industry trend towards shift-left testing and engineering excellence.

Recommendation:
Summary sufficient

Content:
# useOptimistic Won't Save You

## Optimistic UI

Updating the UI immediately in response to user interaction while the operation completes in the background. This decouples interface responsiveness from network latency. The canonical example is the "like" button.

You would think implementing this in React would be simple, but doing it without introducing visual glitches or race conditions is not. React 19's `useOptimistic` hook appears to make the pattern a first-class citizen. However, I would argue that with the advent of Concurrent React, optimistic UI has gotten even more complicated and harder to implement.

Let's explore why manual optimistic updates were historically fragile, how `useOptimistic` can help, and why it's not a silver bullet.

## Where We Came From

To understand the architectural significance of `useOptimistic`, we should first examine the limitations of previous user-land implementations.

### Example 1. Bad Optimistic Update

The most naive approach involves updating the UI on user interaction and again each time the server responds. There are a few issues here and a number of ways that the UI can get out of sync.

```
import { useState } from 'react';
import { toggleLike } from './api';
import { Heart } from 'lucide-react';
import { NetworkPanel } from './NetworkPanel';
import './styles.css';

export default function App() {
  const [liked, setLiked] = useState(false);

  async function handleToggle() {
    const nextLiked = !liked;
    
    
    
    setLiked(nextLiked);

    try {
      
      
      const updated = await toggleLike(nextLiked);
    
      
      
      setLiked(updated); 

    } catch (_) {
      
      setLiked(!nextLiked);
    }
  }

  return (
    <div className="app-container">
      <div className="card">
        <button 
          onClick={handleToggle}
          className={'like-button ' + (liked ? 'liked' : '')}
        >
          <Heart fill={liked ? "currentColor" : "none"} size={48} />
        </button>
      </div>
      <NetworkPanel />
    </div>
  );
}
```

If we spam the button, the state flicks back and forth as the requests complete. If we randomize the latency we'll see race conditions and the final state becomes a toss up.

Commenting out line #24 is a slight improvement. This stops the final sync with the server and solves the flickering, but it creates a new issue. If the UI goes out of sync it won't come back again until another bug occurs or the page is reloaded.

With that line still commented out, toggle "Always Error" and make a pair of requests. The UI reverts from the latter optimistic state to the former optimistic state with no way to reconcile the state from the server.

### Example 2. Better Optimistic Update

To prevent these issues we need to maintain two separate states: the server state and the optimistic state. We can then manually synchronize them, using a ref to track the latest request ID and discard stale responses.

This works, but it requires significant boilerplate to handle race conditions correctly.

```
import { useState, useRef } from 'react';
import { toggleLike } from './api';
import { Heart } from 'lucide-react';
import { NetworkPanel } from './NetworkPanel';
import './styles.css';

export default function App() {
const [serverLiked, setServerLiked] = useState(false);
const [optimisticLiked, setOptimisticLiked] = useState(false);
const callIdRef = useRef(null);

async function handleToggle() {
  const nextLiked = !optimisticLiked;

  
  setOptimisticLiked(nextLiked);

  const callId = Math.random().toString(36);
  callIdRef.current = callId;

  try {
    
    const updated = await toggleLike(nextLiked);

    
    if (callIdRef.current === callId) {
      setServerLiked(updated);
      setOptimisticLiked(updated);
    }
  } catch (_) {
    
    if (callIdRef.current === callId) {
      setOptimisticLiked(serverLiked);
    }
  }
}

return (
  <div className="app-container">
    <div className="card">
      <button 
        onClick={handleToggle}
        className={'like-button ' + (optimisticLiked ? 'liked' : '')}
      >
        <Heart fill={optimisticLiked ? "currentColor" : "none"} size={48} />
      </button>
    </div>
    <NetworkPanel />
  </div>
);
}
```

While this approach solves the issues from the previous example, it still has problems:

#### Boilerplate & Complexity

We now have to manage two separate states, a ref for tracking request IDs, and complex imperative logic in our event handlers. We have to manually ensure we check the `callId` in both success and failure cases.

Alternatively, we could use an abort controller to cancel any ongoing requests when a new one is made, but this would be a similar amount of code.

#### Transitions

What happens when the update happens in a transition? Concurrent React uses transitions for non-blocking updates. In the next example a todo is updated using a form action, which React handles as a transition.

### Example 3. Optimistic Update Within a Transition

Optimistic Update Within a Transition

```
import { useState } from 'react';
import { TodoList } from './TodoList';
import { updateTodo } from './api';
import './styles.css';

const initialTodos = {
  1: { id: 1, title: "Walk the dog", completed: false },
};

export default function App() {
  const [todos, setTodos] = useState(initialTodos);

  async function toggleTodo(todo) {
    
    
    setTodos((prev) => ({ ...prev, [todo.id]: todo }));

    try {
      
      const updated = await updateTodo(todo.id, todo);

      
      
      setTodos((prev) => ({ ...prev, [todo.id]: updated }));
      
    } catch (e) {
      
      setTodos((prev) => ({
        ...prev,
        [todo.id]: { ...todo, completed: !todo.completed },
      }));
    }
  }

  return <TodoList todos={todos} toggleTodoAction={toggleTodo} />;
}
```

It doesn't work. When the state updater function is called from within a transition, it doesn't cause an immediate re-render, which we need to show the optimistic state. This is where `useOptimistic` comes in. It allows us to update the UI immediately within a transition. It also batches reversions until the end of the last transition.

### Example 4. useOptimistic

```
import { useState, useOptimistic, startTransition } from "react";
import { updateTodo } from './api';
import { TodoList } from './TodoList';
import './styles.css';

const initialTodos = {
  1: { id: '1', title: 'Walk the dog', completed: false },
};

export default function App() {
  const [todos, setTodos] = useState(initialTodos);
  
  async function toggleTodo(todo) {
    try {
      
      const updated = await updateTodo(todo.id, todo);
    
      
      startTransition(() => {
        setTodos((prev) => ({ ...prev, [todo.id]: updated }));
      });

    } catch(_) {
      
    }
  }
  return (
    <TodoList todos={todos} toggleTodoAction={toggleTodo} />
  );
}
```

It appears to work. We've gotten rid of a few of those `setTodos` calls and wrapped the remaining one in a transition. We've also created a new state variable in the Todo component to track the optimistic state.

It's simpler than the earlier example with the `callIds` ref, but it's a little less explicit. The other issue is that using a transition doesn't prevent race conditions. It's possible to get the UI out of sync by spamming the checkbox with the latency randomized. The React docs have a note on this:

> This is because the updates are scheduled asynchronously, and React loses context of the order across the async boundary.

Okay, so we're failing to handle race conditions again. There's more:

> This is expected, because Actions within a Transition do not guarantee execution order. For common use cases, React provides higher-level abstractions like `useActionState` and `<form>` actions that handle ordering for you. For advanced use cases, you’ll need to implement your own queuing and abort logic to handle this.

In other words, "We have an API for that too."

### Example 5. Just for Kicks

Here's one last example using `useActionState` and `useOptimistic` together. I originally had some spaghetti code here, but Ricky [pointed out](https://bsky.app/profile/ricky.fm/post/3mciteprjzc2q) some issues with it and we cleaned it up. It does solve the issue of race conditions and ends up being quite lean.

Take a guess how React gets the execution order correct and then try it.

useOptimistic + useActionState

```
import { useState, useOptimistic, useActionState, startTransition } from "react";
import { TodoList } from "./TodoList";
import { updateTodo } from "./api";
import "./styles.css";

const initialTodos = {
  1: { id: "1", title: "Walk the dog", completed: false },
};

export default function App() {
  
  const [todos, toggleTodoAction] = useActionState(async (todos, newTodo) => {
    try {
      
      const updated = await updateTodo(newTodo.id, newTodo);

      
      return { ...todos, [updated.id]: updated };

    } catch (_) {
      
      return todos;
    }
  }, initialTodos);

  return <TodoList todos={todos} toggleTodoAction={toggleTodoAction} />;
}
```

The requests are queued and processed sequentially, with only one request made at a time. Now we're handling errors, race conditions, and we're updating the UI within a transition.

## So Where Do We Land?

The fact is that these new APIs don't make these situations any easier to handle than before. `useOptimistic` is useful but it doesn't simplify optimistic UI and doesn't solve the issue of race conditions on its own.

You really need to understand transitions, actions, and hooks like `useTransition` and `useActionsState` to use it correctly.

Frankly, we should leave these APIs to the library and framework authors. I recommend you watch Ricky Hanlon's talk [Async React](https://www.youtube.com/watch?v=tSO_tdnYprM) from React Conf. After an underwhelming demo with a string of mistakes, Ricky says:

> “So I think one of the key points here is, and you saw me struggling with it – is that writing all of these individual features is kind of a pain in the ass if I’m honest.”

And that's just it. The React team created a lot of controversy when they recommended that React be used with a framework, but this is why. These new APIs are a pain in the ass and they don't reduce the amount of boilerplate we have to write, or reduce the likelyhood of introducing bugs.

The intention is for the framework authors to build their routers and data layers using these APIs and for us to get the benefits without having to deal with the complexity ourselves.
