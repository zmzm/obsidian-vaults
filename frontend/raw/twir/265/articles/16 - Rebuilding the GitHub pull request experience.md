---
type: twir-item
issue: 265
item: 16
item_type: item
date: 2026-01-21
source: https://playfulprogramming.com/posts/react-compiler-library-support/
tags:
  - "GitHub"
  - "Navigation"
status: auto
quality: keep
---

[[2026-01-21-TWIR-265|Index]]

# Item 16: Rebuilding the GitHub pull request experience

Source: [https://playfulprogramming.com/posts/react-compiler-library-support/](https://playfulprogramming.com/posts/react-compiler-library-support/)

Summary:
The article announces a project to rebuild the GitHub pull request UI for improved responsiveness and navigation, especially for large PRs. Details are minimal, but the goal is to enhance code review focus and performance.

Key takeaways:
- Focus on improving PR review UX and performance.
- May interest those building custom code review or diff tools in React.

Recommendation:
Summary sufficient

Content:
# Adapting Library Logic for React Compiler

## Post contents

Being the lead maintainer of TanStack Form, I wanted to make sure that we supported the then-upcoming release of React Compiler properly.

While it required us to [rethink some strategies we were relying on for internal code authoring](https://github.com/TanStack/form/pull/1035), it seemed to me that we were successful in that endeavor after some testing and user feedback.

After all, we could test against our examples and didn't see any issues present. It wasn't until much later when [we got a report of an issue with ternaries and compiler issues](https://github.com/TanStack/form/issues/1832) that we took a second look at things to revalidate our Compiler support.

### Finding edgecases when React Compiler is enabled

Without going too far into our codebase, this is the gist of what we were doing wrong, recontextualized as a scroll listener hook:

```
```

When this hook is used in a parent component:

```
export default function ScrollPosition() {  const position = usePosition();  return <div style={{ position: 'fixed', top: '1rem', left: '1rem' }}>    <p>      {position.current.scrollY}    </p>  </div>;}
```

Things seem to work fine, even with the React Compiler enabled.

However, move the `position` to a child component:

```
function ShowScroll({ position }) {  return (    <p>      {position.current.scrollY}    </p>  );}export default function ScrollPosition() {  const position = usePosition();  return <div style={{ position: 'fixed', top: '1rem', left: '1rem' }}>    <ShowScroll position={position} />  </div>;}
```

And suddenly the `position.current.scrollY` doesn't update anymore.

Broken Scroll Demo - StackBlitz

[Edit](https://stackblitz.com/github/playfulprogramming/playfulprogramming/tree/main/content/crutchcorn/posts/react-compiler-library-support/broken-scroll?file=src%2FApp.jsx)

```
import { usePosition } from './useScroll';function ShowScroll({ position }) {  return (    <p>      {position.current.scrollY}    </p>  );}export default function ScrollPosition() {  const position = usePosition();  return <div style={{ position: 'fixed', top: '1rem', left: '1rem' }}>    <ShowScroll position={position} />    <p>      {position.current.scrollY}    </p>  </div>;}
```

If we look at a minimal version of this code [compiled through the React Compiler](https://playground.react.dev/), we get:

```
import { c as _c } from "react/compiler-runtime";import { usePosition } from "./useScroll";function ShowScroll(t0) {  const $ = _c(2);  const { position } = t0;  let t1;  if ($[0] !== position.current.scrollY) {    t1 = <p>{position.current.scrollY}</p>;    $[0] = position.current.scrollY;    $[1] = t1;  } else {    t1 = $[1];  }  return t1;}export default function ScrollPosition() {  const $ = _c(2);  const position = usePosition();  let t0;  if ($[0] !== position) {    t0 = <ShowScroll position={position} />;    $[0] = position;    $[1] = t0;  } else {    t0 = $[1];  }  return t0;}
```

If we then focus on `ScrollPosition`:

```
export default function ScrollPosition() {  const $ = _c(2);  const position = usePosition();  let t0;  if ($[0] !== position) {    t0 = <ShowScroll position={position} />;    $[0] = position;    $[1] = t0;  } else {    t0 = $[1];  }  return t0;}
```

We can see that `t0` is defined as a memoized `<ShowScroll>` element that is not updated until `position`'s [referential stability](/posts/object-mutation#mutation) has changed.

Compare and contrast to the code generated when we have:

```
import { usePosition } from './useScroll';export default function ScrollPosition() {  const position = usePosition();   return (    <p>      {position.current.scrollY}    </p>  );}
```

```
import { c as _c } from "react/compiler-runtime";import { usePosition } from "./useScroll";export default function ScrollPosition() {  const $ = _c(2);  const position = usePosition();  let t0;  if ($[0] !== position.current.scrollY) {    t0 = <p>{position.current.scrollY}</p>;    $[0] = position.current.scrollY;    $[1] = t0;  } else {    t0 = $[1];  }  return t0;}
```

Here, we see that `position.current.scrollY` itself is being compared by reference rather than the `position` object.

This explains why our code broke in some edgecases but not others.

### Why didn't ESLint catch this?

While this particular instance is flagged by ESLint:

```
Modifying a value returned from 'useState()', which should not be modified directly. Use the setter function to update instead.  34 |   const position = useState(() => ({ current: null }))[0];  35 |> 36 |   position.current = useScroll();     |   ^^^^^^^^ value cannot be modified  37 |  38 |   return position;  39 | }  react-hooks/immutability
```

The way our code was written did not seem to be covered by React's ESLint rules at the time. See, TanStack Form utilizes classes that contain all of the library logic. These classes lives outside of the framework and are then glued back into a given framework via manual re-renders (ala [`useSyncExternalStore`](https://react.dev/reference/react/useSyncExternalStore)).

> Why we use classes for library logic
>
> This enables us to write all core logic once while supporting many frameworks outside of React at once. As such, TanStack Form is able to currently support:

Here's a simplified view of how the scroll handler example above might be rewritten using this pattern:

```
import { useLayoutEffect, useMemo, useReducer } from 'react';class ScrollHandler {  scrollX = 0;  scrollY = 0;  cb = () => {};  constructor(cb) {    this.cb = cb;  }  listener = () => {    this.scrollY = window.scrollY;    this.scrollX = window.scrollX;    this.cb();  }  mount = () => {    window.addEventListener('scroll', this.listener);    return () => {      window.removeEventListener('scroll', this.listener);    }  }}export function usePosition() {  const [_, rerender] = useReducer(() => ({}), {});  const scrollHandler = useMemo(() => ({current: new ScrollHandler(rerender)}), [rerender]);  // Using `useLayoutEffect` for simplicity  useLayoutEffect(() => {    const cleanup = scrollHandler.current.mount();    return () => cleanup();  }, [scrollHandler]);  return scrollHandler;}
```

If you run the same ESLint rules over this code, you won't find any issues reported.

Broken Scroll Indirection Demo - StackBlitz

[Edit](https://stackblitz.com/github/playfulprogramming/playfulprogramming/tree/main/content/crutchcorn/posts/react-compiler-library-support/broken-scroll-indirection?file=src%2FApp.jsx)

```
import { usePosition } from './useScroll';function ShowScroll({ position }) {  return (    <p>      {position.current.scrollY}    </p>  );}export default function ScrollPosition() {  const position = usePosition();  return <div style={{ position: 'fixed', top: '1rem', left: '1rem' }}>    <ShowScroll position={position} />    <p>      {position.current.scrollY}    </p>  </div>;}
```

### How to detect *all* Compiler errors

What's worse than ESLint not catching things, React Compiler will not report these issues to you by default. Instead, in many instances it will choose to bypass optimizations of your components silently.

Luckily, the React team has [a `panicThreshold` flag you can enable in your Compiler settings to have React report these issues more consistently](https://react.dev/reference/react-compiler/panicThreshold):

```
import { defineConfig } from 'vite';import react from '@vitejs/plugin-react';export default defineConfig({  plugins: [    react({      babel: {        plugins: [          ['babel-plugin-react-compiler', { panicThreshold: 'all_errors' }],        ],      },    }),  ],});
```

![Vite showing an error to the browser about position.current being mutated]()

This helps immensely in debugging library code that might have ESLint reporting problems in some capacity or another.

Likewise, if you want to simulate Babel ignoring the transform of your installed library (as it would when it's in `node_modules`), you can simply add your library code to `{babel: {exclude: []}}` like so:

```
import { defineConfig } from 'vite';import react from '@vitejs/plugin-react';export default defineConfig({  plugins: [    react({      babel: {        plugins: [          ['babel-plugin-react-compiler', { panicThreshold: 'all_errors' }],        ],        // Simulate `useScroll` being in a dependency, therefore not covered by Babel        exclude: ['src/useScroll.js'],      },    }),  ],});
```

### Fixing the bug

The long-term fix for these kinds of problems is to do what the compiler suggests and avoid mutating `position` here:

```
export function usePosition() {  const basePosition = useState(() => ({ current: null }))[0];  const scroll = useScroll();    const position = useMemo(() => {    return {      ...basePosition,      current: scroll    }  }, [scroll, basePosition]);    return position;}
```

This might seem bad for some performance edgecases until you realize that the React Compiler should handle almost all performance hiccups you might anticipate from creating a new `position` object on each scroll. In particular, it should handle:

- Preventing re-renders of un-needed nodes
- Memoizing usage of `position.current.scrollY` for you
- And more
