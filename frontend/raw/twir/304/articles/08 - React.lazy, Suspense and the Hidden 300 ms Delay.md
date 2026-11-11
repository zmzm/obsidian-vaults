---
type: twir-item
issue: 304
item: 8
item_type: item
date: 2026-11-04
source: https://tabwidgets.com/blog/react-lazy-suspense-delay
tags:
  - "Suspense"
  - "Reactlazy"
  - "300"
status: auto
quality: keep
---

[[2026-11-04-TWIR-304|Index]]

# Item 8: React.lazy, Suspense and the Hidden 300 ms Delay

Source: [https://tabwidgets.com/blog/react-lazy-suspense-delay](https://tabwidgets.com/blog/react-lazy-suspense-delay)

Summary:
This post investigates a performance bottleneck in a React 19 app using React.lazy and Suspense, revealing that React intentionally delays revealing suspended content by 300 ms to batch updates and avoid flicker. Even when code loads quickly, this throttle causes visible delays. The author describes a workaround: preloading lazy components before rendering to bypass the initial suspension and reduce perceived latency.

Key takeaways:
- React.lazy always suspends on first render, even if code is already loaded.
- Suspense batches reveals with a 300 ms throttle (FALLBACK_THROTTLE_MS).
- This behavior can delay UI updates even when code is fast to load.
- Preloading lazy components before render can eliminate the delay.

Recommendation:
Read fully (for practical performance insights and workaround details)

Why it matters:
for practical performance insights and workaround details

Content:
# React.lazy, Suspense and the Hidden 300 ms Startup Delay • Tab Widgets

A new tab extension has an unusual performance problem: it starts from scratch every single time you open a tab. There's no warm page to come back to. So when the dashboard started taking a noticeable beat to fill in, we assumed the bundle was too big.

It wasn't. The biggest fix didn't remove a single byte, and we had to rethink our first version of it.

**TL;DR:** in headless Chromium, our widgets' code was loaded within about 100 ms, but the widgets didn't appear until about 380 ms, because a lazy component always suspends once and React then holds suspended content back for 300 ms. Rendering a placeholder ourselves instead of suspending got the first widget content on screen about 240 ms sooner, and most of the dashboard about 200 ms sooner, in Chrome on a Windows desktop. Shrinking the main bundle made no measurable difference.

---

## The setup

[Tab Widgets](/) is a React 19 app built with Rspack. Every widget (the clock, notes, weather, Gmail, Spotify and dozens more) lives in its own code chunk and is loaded with `React.lazy`, so a new tab only loads the code for the widgets you actually use. Each widget sits inside its own `Suspense` boundary, which shows a loading placeholder until the widget is ready.

When a new tab opens, the app:

1. loads the main bundle,
2. reads your saved pages and widgets,
3. loads the app shell and the list of available widgets,
4. renders the page, and
5. loads each widget's code as it's rendered.

---

## Bytes weren't the bottleneck

We started with the obvious suspect: what's in the startup bundle? We found real waste. A shared `~/ui` index file re-exported every modal, so the Add widget, Settings and Upgrade modals (with pricing tables and payment card logos) were bundled into startup code even though you only see them when you click a button. Removing that re-export moved about 100 KB off the startup path.

We also noticed the date and time library (luxon) was bundled into the main startup file because of a single helper that didn't use it. Moving it out made the 283 KB main file noticeably smaller, but it made no measurable difference to when anything appeared. The library just moved into a different file that was still needed at startup by the clock widgets, and it takes barely any time to run. We reverted it.

Then we profiled a production build in headless Chromium. Every script was loaded and evaluated within about 100 ms of opening the tab, yet the widgets didn't appear until about 380 ms. For most of that gap, the browser was doing nothing at all. Then several timers fired at once and the widgets rendered.

An extension's files are read from the local disk, not over the network, so a few hundred extra kilobytes cost very little, and shrinking the bundle further wasn't going to help. Our web version loads the same code over the network, where bundle size matters more, but the throttle fix below applies there too.

---

The waiting comes from two React behaviours that combine badly at startup.

**1. A lazy component always suspends the first time it renders**, even if its code has already loaded. `React.lazy` only calls `import()` when it first renders, and it hears back through a promise, which always resolves after that render. So the first render always shows the `Suspense` fallback.

Calling `import()` yourself beforehand doesn't help: the lazy component still starts its own import when it renders, gets a promise that hasn't resolved yet, and suspends once.

**2. React throttles how quickly suspended content is revealed.** When suspended content becomes ready, React only reveals it once 300 ms have passed since a fallback last appeared or was replaced anywhere on the page (`FALLBACK_THROTTLE_MS` in React's source). Anything that becomes ready inside that window is revealed together. The [`Suspense` caveats](https://react.dev/reference/react/Suspense#caveats) put it as "at most once every 300ms, measured from the last reveal". This is intentional: it stops a page from flickering as lots of small pieces finish loading at slightly different times. It does hurt cases like ours, where the content is ready almost straight away. There's a [long discussion on GitHub](https://github.com/react/react/issues/31819) about making it configurable, and so far React's maintainers have kept it as a fixed heuristic.

Put those together and every widget on a new tab was guaranteed to show its placeholder and then wait at least 300 ms, no matter how quickly its code arrived. Because that 300 ms timer is shared across the whole page, widgets also appeared in batches.

One widget on a new tab, suspending versus gatedSuspending: the app first renders at about 80 ms and shows the widget’s placeholder while its code loads, which takes until about 100 ms. React’s 300 ms throttle holds the placeholder until about 380 ms. Gated: the same placeholder shows at about 80 ms, and the widget replaces it as soon as its code is in.Suspending (before)300 ms throttleCodeapp codewidget codeOn screenplaceholderwidgetrevealed ~380 msGated (after)Codeapp codewidget codeOn screenwidgetrendered as soon as its code is in0 ms100 ms200 ms300 ms400 ms

One widget on a new tab, with approximate timings based on the headless numbers above. When it suspends, its code is in by about 100 ms, but React holds the placeholders for 300 ms from when they appeared. Behind the gate, the widget renders as soon as its code is in. Both rows use the same timings for comparison.

Wrapping the render in `startTransition` doesn't help here either. A transition stops content that's already on screen from going back to a fallback, but a `Suspense` boundary that's mounting for the first time still shows its fallback. (In React's development build, a transition can skip the fallback when the import has already resolved, so check this in a production build.)

---

React's own internals expose how a lazy component is started: it calls `component._init(component._payload)`. If we make that call ourselves before React renders, the import starts early, and once it finishes the lazy component no longer suspends. We still use this `preloadLazy` function in the final fix. It also keeps track of which components are settled (loaded or failed), which we'll need later:

```
type LazyInternals = {
  _init?: (payload: unknown) => unknown;
  _payload?: { _status?: number };
};

const settled = new WeakSet<object>();

export const preloadLazy = (component: object): Promise<void> => {
  const { _init, _payload } = component as LazyInternals;
  const settle = () => {
    settled.add(component);
  };

  if (typeof _init !== "function") {
    settle(); // not lazy (or React changed): render it as usual
    return Promise.resolve();
  }

  try {
    _init(_payload); // starts the import, and returns if it has already loaded
    settle();
    return Promise.resolve();
  } catch (thrown) {
    // still loading: React throws the promise our import() returned. Already failed: it
    // throws the error, which the widget's error boundary will show
    if (typeof (thrown as PromiseLike<unknown>)?.then === "function") {
      return Promise.resolve(thrown).then(settle, settle);
    }
    settle();
    return Promise.resolve();
  }
};

// React's lazy status: 1 loaded, 2 failed
export const isLazySettled = (component: object) =>
  settled.has(component) ||
  [1, 2].includes((component as LazyInternals)._payload?._status ?? -1);
```

`_init`, `_payload` and `_payload._status` are private fields, so we fall back gracefully: if React ever changes them, components count as settled straight away and render and suspend exactly as before.

We considered dropping `React.lazy` for our own map of loaded modules, which needs no private fields (we show a version of that below). But each widget's component, preview and settings are already lazy components, rendered from the dashboard, picture-in-picture, the Add widget catalog and the settings modals. So we kept them and isolated the private fields in one small, tested file. A unit test renders a real `React.lazy` component after preloading, so a React upgrade that breaks this fails our tests rather than silently losing the speedup.

At startup we worked out which page the tab opens to, preloaded its widgets, and waited up to 100 ms for them before rendering. In headless Chromium, widgets went from about **380 ms to about 95 ms**.

But a capped wait has a weak spot. Any widget whose code takes longer than the cap suspends anyway, and because its fallback now appears later, React's 300 ms window starts, and ends, later too. On a slow disk or a busy machine, that widget would appear up to 100 ms later than if we hadn't waited at all.

There was one regression along the way. With the modals no longer bundled into startup code, they load on demand behind a small loading spinner. That spinner took keyboard focus, so closing the Add widget modal no longer returned focus to the button that opened it. Our end-to-end tests caught it, and we now preload those modals once the page is idle so they open exactly as before.

---

## The fix that held up: don't suspend at all

Rather than racing a timer, we stopped widgets from suspending on their own code.

Each widget now checks whether its code has loaded. If it hasn't, it renders the usual placeholder as ordinary content and starts the load. When the code arrives, a normal state update swaps in the real widget. That's a small hook built on `preloadLazy`:

```
export const useLazyReady = (component: object) => {
  const [, rerender] = useReducer((count: number) => count + 1, 0);
  const ready = isLazySettled(component);

  useEffect(() => {
    if (ready) return;

    let active = true;
    preloadLazy(component).then(() => {
      if (active) rerender();
    });

    return () => {
      active = false;
    };
  }, [component, ready]);

  return ready;
};
```

`isLazySettled` is true once `preloadLazy` has finished with a component, whether its code loaded or failed. A failed load still renders the widget, so its error boundary can show the failure. It's also true once React has loaded the component on its own (for example in a picture-in-picture window). Each widget then picks what to render:

```
const isReady = useLazyReady(WidgetComponent);

return isReady ? <WidgetComponent {...config} /> : <WidgetLoading />;
```

Keep the widget's `Suspense` and error boundary around this. They still catch a failed import, and anything that suspends if React's private fields ever change.

React's 300 ms delay only applies when it reveals content that suspended, and nothing is suspending here, so each widget appears as soon as its code is in. Startup still begins loading the start page's widgets before the first render, but it no longer waits for them.

This does give up what the throttle was for: widgets now appear one by one as their code arrives rather than in a batch. That's fine for us. Each widget's frame has a fixed size on the grid and the placeholder fills it, so nothing moves when a widget swaps in.

We applied the same idea to the permission check that the timer, countdown, Pomodoro, history and bookmarks widgets run before they render. It used a suspending query, so those widgets were held back by the throttle too, even though the check takes a few milliseconds. It now runs as an ordinary query and shows the placeholder until it finishes.

### Results

We measured the build just before the fix and the build with it in Chrome on a Windows desktop: 4 cold new tabs each, with a busy 20-widget dashboard (including Gmail, Google Drive, Tasks, Spotify, an RSS reader and a pets game; 16 visible, signed out), a plain grey wallpaper and the wallpaper's entrance animation turned off so it didn't blur the screenshots. The "after" build is the whole change: the modals moved out of the startup bundle, the start page's widgets preloaded, the code gate and the permission check fix. Times are read from the trace screenshots and measured from when the tab started loading, so each row is the first screenshot where that much of the final page's widget detail is visible (5% for "first widget content", 85%, and 97% for "all"). Our test profile is signed out, so the seven Pro widgets (Gmail, Calendar, Drive and others) show a Sign in / Upgrade overlay instead of their content. We left those widgets out of the numbers, since a Pro user never sees that overlay. These times aren't comparable with the headless numbers above.

*Traces were recorded in Chrome 154.0.8037.98 on a Windows 11 desktop (i9-14900KF, 64GB 6000 MT/s, T-FORCE TM8FPL2000G NVME SSD).*

| Mean of 4 runs | Before | After | Change |
| --- | --- | --- | --- |
| Nav bar visible | 274 ms | 326 ms | +52 ms |
| First widget content visible | 540 ms (all at once) | 298 ms | −242 ms |
| 85% of widget content visible | 540 ms | 336 ms | −204 ms |
| All widget content visible | 540 ms | 544 ms | +4 ms |

One thing does show up earlier than any of these: the Pro widgets' sign-in overlay, at about 200 ms. It used to sit inside the widget's `Suspense` boundary, so the fallback hid it until the reveal. Now nothing suspends, so it paints straight away over the placeholder.

Two rows need explaining. The nav bar is first detected about 50 ms later, but it isn't rendered later: it's part of the same first render as the widget placeholders. It fades in over 150 ms, and our screenshot measure only catches it partway through that fade. With the fix, widgets render during the fade instead of in one batch afterwards, so the frames that show it land later. In our DOM-based headless runs, the nav bar arrived about 11 ms later with the fix (means of 157 and 169 ms), inside run-to-run noise.

The last widgets don't move: Weather and Word of the Day load their code and then suspend again while they fetch their data, so React's 300 ms throttle still holds them back. Before the fix, they were revealed in the same batch as everything else. The fix took code loading out of `Suspense`, not data loading, so those two are next.

Here's a typical run of each build (the one closest to the median), pixelated to hide the dashboard's contents:

![Two columns of pixelated new tab screenshots at 200, 300, 350, 450 and 550 ms. Before the fix: empty widget frames until 550 ms, when every widget appears at once. After the fix: the Pro widgets' sign-in overlays appear by 200 ms, the first widget content by 300 ms, most of the dashboard by 350 ms, and the weather widget at 550 ms.](https://assets.tabwidgets.com/cdn-cgi/image/width=1280,format=auto,quality=80/images/posts/2026/10/react-lazy-suspense-delay/startup-timeline-windows.png)

The same 20-widget dashboard in Chrome on a Windows desktop, the run closest to the median of 4 per build, signed out (so the Pro widgets show a sign-in overlay). Each frame is the last screenshot captured at or before that time.

### Without React's private fields

If you're starting fresh, or would rather not touch React's internals, you can skip `React.lazy` for this and keep the loaded components in a cache of your own. Same idea: start the import early, render a placeholder until it's in, then render the component through a normal state update:

```
type Loader<P> = () => Promise<{ default: ComponentType<P> }>;

const loaded = new Map<Loader<any>, ComponentType<any>>();

// call this before the first render to start loading early
export const preload = <P,>(load: Loader<P>) =>
  load().then((module) => {
    loaded.set(load, module.default);
    return module.default;
  });

export const useLoadedComponent = <P,>(load: Loader<P>) => {
  const [Component, setComponent] = useState(
    () => loaded.get(load) as ComponentType<P> | undefined,
  );

  useEffect(() => {
    if (Component) return;

    let active = true;
    preload(load).then((Loaded) => {
      if (active) setComponent(() => Loaded);
    });

    return () => {
      active = false;
    };
  }, [load, Component]);

  return Component;
};
```

Define each loader once at module level, so it's the same function on every render, and use it like the gate above:

```
const loadNotes = () => import("./NotesWidget");

const Notes = (props: NotesProps) => {
  const Widget = useLoadedComponent(loadNotes);
  return Widget ? <Widget {...props} /> : <WidgetLoading />;
};
```

A real version also needs to handle a failed import, for example by storing the error and throwing it while rendering so an error boundary shows it. Unlike `React.lazy`, which keeps a failed import for good, this can try again, for example when the widget mounts again.

---

## What we learned

- **Measure when things appear, not just how big the files are.** Making the main file smaller (moving luxon out) didn't change when anything appeared.
- **Look for idle time.** The biggest win came from a gap where the main thread was doing nothing, not from making any code faster.
- **Know what your framework does on purpose.** React's reveal throttle is a sensible default for avoiding flicker, but on a page that renders from scratch every time and loads its code from local files, the content is ready almost straight away, so a fixed 300 ms wait was our single largest delay.
- **Confirm lab results on real machines.** Headless Chromium made the idle gap easy to find and explain, and we then confirmed the result in Chrome on Windows.

These improvements shipped in [Tab Widgets v2](/blog/release-v2-0).

---

## Try it yourself

Every widget uses the gate from this post today. Open a few new tabs and watch the dashboard fill in.

It's free.
