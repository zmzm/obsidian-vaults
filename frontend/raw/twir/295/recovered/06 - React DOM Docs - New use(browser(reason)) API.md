---
type: "twir-recovery"
issue: 295
item: 6
source: "https://react.dev/reference/react-dom/browser"
final_url: "https://react.dev/reference/react-dom/browser"
retrieved: "2026-10-22T11:30:09+00:00"
original_note: "frontend/raw/twir/295/articles/06 - React DOM Docs - New use(browser(reason)) API.md"
editorial_review: "pending"
truncated: false
---

Original intake note: [[../articles/06 - React DOM Docs - New use(browser(reason)) API|React DOM Docs - New use(browser(reason)) API]]

# browser - React

`browser` lets you mark a component as browser-only during server rendering.

---

## Reference

### `browser(reason?)`

Call `browser` inside [`use`](/reference/react/use) to mark a component as browser-only during server rendering:

```
import { use } from 'react';

import { browser } from 'react-dom';

function BrowserOnly() {

use(browser('This component requires browser APIs.'));

return <BrowserContent />;

}
```

During server rendering, `use(browser())` stops rendering the component and leaves the closest [`<Suspense>`](/reference/react/Suspense) boundary’s fallback in its place. In the browser, `use(browser())` returns `undefined`, so the component renders normally.

[See more examples below.](#usage)

#### Parameters

- **optional** `reason`: A string or function that explains why the content needs to render in the browser. The string or the function’s return value becomes the `cause` of the `Error` passed to [`onBrowserBailout`](#reporting-browser-only-rendering-on-the-server). React calls a reason function each time a server renderer encounters the value returned by `browser`, but does not call it in the browser. If creating the reason is expensive, pass a function such as `() => new Error(...)`.

#### Returns

`browser` returns an opaque value that you can pass to `use` in a component or use as the reason when [aborting a server render](#aborting-pending-server-rendering-for-the-browser). In the browser, passing this value to `use` returns `undefined`.

#### Caveats

- `use(browser())` must be inside a `<Suspense>` boundary during server rendering. Without one, the server render fails.
- `use(browser())` must be called from a [Client Component](/reference/rsc/use-client), not a [Server Component](/reference/rsc/server-components).
- Calling `browser()` by itself has no effect. To mark a component as browser-only, pass the value returned by `browser` to `use`. Do not throw it.

---

## Usage

### Rendering content only in the browser

Call `browser` inside `use` in a component that should only render in the browser:

You can use this instead of checking `typeof window`, waiting for an [`Effect`](/reference/react/useEffect) to set mounted state, or using a framework option to disable server rendering.

Click **Reload** to see the loading fallback in the initial HTML. After hydration, React displays the draft loaded from `localStorage`.

### Note

`use(browser())` must be called from a Client Component. If your framework uses Server Components by default, add the [`'use client'`](/reference/rsc/use-client) directive to that file or move the call to a child Client Component:

```
'use client';

import { use, useState } from 'react';

import { browser } from 'react-dom';

export default function SavedDraft() {

use(browser('The saved draft is stored in localStorage.'));

const [draft] = useState(() => localStorage.getItem('draft') ?? '');

return <DraftEditor initialDraft={draft} />;

}
```

---

### Conditionally rendering on the server

Like other calls to [`use`](/reference/react/use), `use(browser())` can be called inside a conditional statement or after an early return. This lets a Component or custom Hook opt out of server rendering based on a condition, such as the value of a prop.

For example, this `useTimeZone` Hook accepts an optional default value. When provided, React renders the default value in the initial HTML and in the browser. Without a default value, the Component suspends during server rendering and shows the device’s local time zone in the browser.

Click **Reload** to see the loading fallback before the user’s time zone appears.

You can apply a similar pattern to conditionally avoid server rendering when using a Suspense-enabled data-fetching library:

```
function useBrowserQuery(query, options) {

if (options.initialData === undefined) {

use(browser('useBrowserQuery: No initial data was provided.'));

}

return useQuery(query, options);

}

function ProductDetails({ productId, initialData }) {

const product = useBrowserQuery(`/api/products/${productId}`, {

initialData,

});

return <h1>{product.name}</h1>;

}
```

With `initialData`, React renders the Component to HTML on the server. Without it, React leaves the closest [`<Suspense>`](/reference/react/Suspense) boundary’s fallback in the HTML. In the browser, `useQuery` can fetch the data or read it from its client cache as usual.

---

### Reporting browser-only rendering on the server

Pass an `onBrowserBailout` callback to the server renderer to report browser-only rendering. When React leaves a Suspense fallback for the browser, it does not call the server renderer’s `onError` callback or [`hydrateRoot`’s `onRecoverableError`](/reference/react-dom/client/hydrateRoot#error-logging-in-production) callback. This example also passes a reason, which is available as the reported error’s `cause`:

```
import { Suspense, use, useState } from 'react';

import { browser } from 'react-dom';

import { renderToPipeableStream } from 'react-dom/server';

function SavedDraft() {

use(browser(() => new Error('The saved draft is stored in localStorage.')));

const [draft] = useState(() => localStorage.getItem('draft') ?? '');

return <DraftEditor initialDraft={draft} />;

}

function App() {

return (

<Suspense fallback={<p>Loading saved draft...</p>}>

<SavedDraft />

</Suspense>

);

}

const { pipe } = renderToPipeableStream(<App />, {

onShellReady() {

pipe(response);

},

onBrowserBailout(error, errorInfo) {

logBrowserBailout(error, errorInfo);

}

});
```

`onBrowserBailout` receives two arguments:

1. An `Error` describing the browser-only render. If you passed a reason to `browser`, it is available as the error’s `cause`.
2. An `errorInfo` object with a `componentStack` showing where browser-only rendering occurred.

The reason function can return any value. Return a new `Error` to give the cause its own stack without creating the `Error` in the browser. React does not serialize the reason into the HTML.

If there is no Suspense boundary to provide a fallback, the server render fails. React reports the failure through the renderer’s usual error callbacks instead of `onBrowserBailout`.

---

### Aborting pending server rendering for the browser

If you call a server rendering API directly, you can stop waiting for pending content and let the browser finish rendering it. Pass the value returned by `browser` as the reason when aborting the server render. React then leaves pending Suspense boundaries in their fallback state and renders their content in the browser:

```
import { browser } from 'react-dom';

import { renderToPipeableStream } from 'react-dom/server';

const { pipe, abort } = renderToPipeableStream(<App />, {

onShellReady() {

pipe(response);

setTimeout(() => {

abort(browser('The server render timed out.'));

}, 10000);

}

});
```

A `browser` abort reason does not trigger the server renderer’s `onError` callback or `hydrateRoot`’s `onRecoverableError` callback. Instead, the server renderer reports each recovered Suspense boundary to `onBrowserBailout`.

For server rendering APIs that accept an [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal), pass `browser()` as the reason to [`AbortController.abort`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController/abort).
