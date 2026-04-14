---
type: twir-item
issue: 275
item: 7
item_type: item
date: 2026-04-01
source: https://tigerabrodi.blog/when-do-you-really-need-starttransition
tags:
status: auto
---

[[2026-04-01-TWIR-275|Index]]

# Item 7: When Do You Really Need startTransition?

Source: [https://tigerabrodi.blog/when-do-you-really-need-starttransition](https://tigerabrodi.blog/when-do-you-really-need-starttransition)

Content:
# When Do You Really Need startTransition?

## Introduction

Most React developers have heard of startTransition. Few actually understand what it does. Even fewer know when they need it. Let me explain it from the ground up.

* * *

## How React renders without startTransition

To understand startTransition, you first need to understand how React handles updates normally.

When you call setState, React schedules a render. A render means React runs your component function, builds a new tree of elements, compares it to the previous tree, and applies the differences to the DOM. This is called reconciliation. "Reconciliation" just means React figuring out what changed.

Here is the important part. By default, every state update is urgent. React treats them all the same. It processes them in order and each one must finish before the next one starts.

Say the user types in a search box. Every keystroke calls setState with the new text. React re-renders the component. If that component also filters a list of 10000 items, each keystroke triggers a full re-render of 10000 items. React must finish rendering all 10000 items before it can process the next keystroke.

The user types "hello". Five keystrokes. Five renders. Each render processes 10000 items. The input field freezes between keystrokes because React is busy rendering the list. The user sees their text appear in chunks instead of character by character.

This is jank. "Jank" means the interface stutters or feels unresponsive. It happens when the main thread is blocked by work that takes too long.

* * *

## What startTransition actually does

startTransition tells React that a specific state update is not urgent. React can work on it in the background and interrupt it if something more important comes in.

Here is the mental model. React now has two lanes.

The urgent lane. Things like typing, clicking, pressing keys. These must update the screen immediately or the app feels broken.

The transition lane. Things like updating a filtered list, rendering a large chart, processing search results. These are important but can wait a few frames without the user noticing.

When you wrap a setState call in startTransition, you are telling React to put that update in the transition lane.

```
import { useState, useTransition } from 'react';

function Search() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [isPending, startTransition] = useTransition();

  function handleChange(e) {
    // Urgent. Update the input immediately.
    setQuery(e.target.value);

    // Not urgent. Update the filtered list when React has time.
    startTransition(() => {
      setResults(filterItems(e.target.value));
    });
  }

  return (
    <div>
      <input value={query} onChange={handleChange} />
      {isPending && <span>Filtering...</span>}
      <ItemList items={results} />
    </div>
  );
}
```

Now when the user types "hello", here is what happens.

Keystroke "h". React immediately updates the input to show "h". Then it starts working on filtering the list in the transition lane.

Keystroke "e" arrives while React is still filtering. React abandons the filtering for "h". It immediately updates the input to show "he". Then it starts filtering for "he" instead.

The user sees their keystrokes appear instantly. The list updates when React has a moment to breathe. No jank.

The key word is "abandons." React can throw away an in-progress transition render when a new update comes in. It does not need to finish it. This is called interruptible rendering. Without startTransition, React cannot do this. It must finish what it started.

* * *

## How React knows what to interrupt

You might wonder how React can abandon a render midway. The answer is that React 18 changed how rendering works internally.

Before React 18, rendering was synchronous. React started rendering and did not stop until it was done. The main thread was blocked the entire time. No user events could be processed during a render.

React 18 introduced concurrent rendering. React breaks rendering work into small chunks. After each chunk, it checks if something more urgent needs attention. If yes, it pauses the current work and handles the urgent thing first.

startTransition is the way you tell React "this update is safe to pause." React will not pause urgent updates. It will only pause transitions.

The isPending boolean from useTransition tells you whether a transition is currently in progress. You can use it to show a loading indicator while the heavy work is happening in the background.

* * *

## Real use cases where you need it

## AI streaming

An AI sends tokens fast. Maybe 10 to 30 tokens per second. Each token makes the markdown string grow. You split it into blocks and re-render.

Without startTransition, each token triggers a synchronous render. If rendering takes 30ms and tokens arrive every 33ms, renders stack up. The browser never gets a chance to paint. The page freezes.

With startTransition, you wrap the block state update.

```
useEffect(() => {
  const newBlocks = splitIntoBlocks(content);
  startTransition(() => {
    setBlocks(newBlocks);
  });
}, [content]);
```

Token 1 arrives. React starts rendering the new blocks in the transition lane. Token 2 arrives 33ms later. React abandons the render for token 1 and starts fresh with token 2. Token 3 arrives. Abandon again. When tokens finally pause for a moment, React finishes the latest render.

The user sees the latest state. Not every intermediate state. The UI stays responsive the whole time.

## Filtering or searching large lists

The classic example. You have thousands of items. The user types a query. Without startTransition, each keystroke blocks the main thread while React re-renders thousands of items.

With startTransition, the input stays snappy. The list catches up when React has time.

## Tab switching with heavy content

The user clicks a tab. The new tab has a complex component tree. Charts. Tables. Lots of data.

Without startTransition, the clicked tab does not visually highlight until the entire new content is rendered. It feels like the click did nothing.

With startTransition, you update the active tab immediately as an urgent update. Then you load the tab content as a transition. The tab highlights instantly. The content appears a moment later.

```
function Tabs({ tabs }) {
  const [activeTab, setActiveTab] = useState(0);
  const [content, setContent] = useState(tabs[0].content);
  const [isPending, startTransition] = useTransition();

  function handleClick(index) {
    setActiveTab(index); // Urgent. Highlight the tab now.
    startTransition(() => {
      setContent(tabs[index].content); // Transition. Render content when ready.
    });
  }

  return (
    <div>
      <div className="tabs">
        {tabs.map((tab, i) => (
          <button
            key={i}
            onClick={() => handleClick(i)}
            className={i === activeTab ? 'active' : ''}
          >
            {tab.label}
          </button>
        ))}
      </div>
      {isPending ? <Spinner /> : <TabContent data={content} />}
    </div>
  );
}
```

## Navigation in single page apps

When the user clicks a link, you want the navigation to feel instant. But the new page might be heavy. Wrap the route update in startTransition. The old page stays visible while the new page renders in the background. No blank screen.

React Router and Next.js already do this internally.

* * *

## When you do NOT need startTransition

Not every state update needs startTransition. Most do not.

If the render triggered by setState is fast, under 16ms, you do not need it. The browser can handle it without dropping frames. Adding startTransition to a fast update adds complexity for no benefit.

If the state update directly controls user input, do not wrap it in startTransition. The input must update immediately. You can split the update. The input value is urgent. The downstream effect of that value is a transition.

If you only have one state update and it is small, startTransition adds overhead. The scheduling machinery is not free. For trivial updates it is slower than just rendering synchronously.

* * *

## startTransition vs debouncing

People sometimes solve the same problem with debouncing. "Wait until the user stops typing for 300ms, then update the list." This works but it adds artificial delay. The user waits 300ms after their last keystroke before seeing results. Even if React could render them faster.

startTransition is better because it does not add delay. React starts working immediately. It just does so in a way that can be interrupted. If React finishes rendering before the next keystroke, the user sees the result instantly. No 300ms wait.

Debouncing delays the start of work. startTransition does the work immediately but makes it interruptible.

You can combine them. Debounce for network requests where you do not want to fire an API call on every keystroke. Use startTransition for the render that follows.

* * *

## startTransition vs requestIdleCallback

Another thing people compare. requestIdleCallback is a browser API that says "run this function when the browser is idle." It sounds similar but it is very different.

requestIdleCallback is for scheduling work outside of React. It does not integrate with React's rendering at all. React does not know about it. It cannot interrupt a React render.

startTransition is React-native. It integrates with the reconciler. "Reconciler" is the part of React that decides what to re-render. React can interrupt and resume transitions because it controls the whole process.

Use requestIdleCallback for non-React work like analytics or logging. Use startTransition for React state updates that trigger expensive renders.

* * *

## The one sentence summary

startTransition tells React "this update matters but it can wait." React keeps the UI responsive by interrupting transition renders when urgent updates come in. Use it when a state update triggers expensive rendering and the user should not be blocked waiting for it to finish.

Key takeaways:
- No key takeaways extracted.

Recommendation: Summary sufficient
