---
type: twir-item
issue: 271
item: 10
item_type: item
date: 2026-03-04
source: https://twofoldframework.com/blog/error-rendering-with-rsc
tags:
  - "RSC"
  - "ServerComponents"
status: auto
quality: keep
---

[[2026-03-04-TWIR-271|Index]]

# Item 10: Error rendering with RSC

Source: [https://twofoldframework.com/blog/error-rendering-with-rsc](https://twofoldframework.com/blog/error-rendering-with-rsc)

Summary:
This article explains how React Server Components (RSC) handle errors across different rendering environments: RSC render, SSR render, and browser render. Errors in RSCs are serialized into the stream rather than crashing the render, but when SSR attempts to convert the stream to HTML, errors are surfaced and must be handled, typically resulting in a crash unless caught at the application level. Error boundaries only work in the browser render phase, not during SSR or RSC streaming.

Key takeaways:
- RSC errors are serialized in the stream and do not crash the server render process.
- SSR will throw if it encounters an error in the RSC stream, requiring explicit error handling.
- Error boundaries are only effective in the browser, not during SSR or RSC streaming.

Recommendation:
Read fully (read fully if working with RSC error handling or SSR internals)

Why it matters:
read fully if working with RSC error handling or SSR internals

Content:
# Error rendering with RSC

Today weâre going to take a look at what happens when a React Server Component throws an error during render. Although this post is mostly a look under the hood at how an RSC framework handles errors, it will shed some light on what happens when Reactâs rendering functions encounter errors.

In this post weâll cover:

- How Reactâs different rendering environments respond to errors.
- How exceptions thrown in RSCs make their way to error messages displayed on the userâs screen.
- How error rendering changes with Suspense and streaming.

To get started, letâs dive into Reactâs different rendering environments and see how they each respond to errors.

## The three environments

Typically RSC applications are going to consist of three environments in which they render. Each of these environments has its own rules and handles errors differently from the others.

#### RSC Render

The RSC render is responsible for executing React Server Components. When an error is thrown inside a Server Component the error object gets serialized into the RSC stream in place of the component tree. The error does not causing rendering to crash, but instead it gets turned into data that exists within the RSC stream.

#### SSR Render

The SSR render is responsible for turning an RSC stream and its client components into HTML. When an error is thrown during SSR one of two things happens:

If the error happens inside a `<Suspense>` boundary, then everything inside that boundary stops rendering.

Otherwise SSR throws and exits.

#### Browser Render

This is the client-side React render that is most familiar to frontend developers. If an error is thrown here then React will allow the closest Error Boundary to catch the error and display a fallback. This is the only environment where React supports Error Boundaries, and is the best place for errors to be caught and displayed to the user.

Now letâs take a deeper look at each of these environments and follow an error thrown in the RSC render on its journey to becoming a warning message displayed by the browser.

### Errors in the RSC Render

Rendering RSCs is done through a bundler specific implementation of the `renderToReadableStream` API. Weâll use the `react-server-dom-webpack` package to show what happens when rendering an RSC that errors.

```
import { renderToReadableStream } from "react-server-dom-webpack/server";

function MyComponent() {
  throw new Error("Whoops!");
}

const rscStream = await renderToReadableStream(<MyComponent />, {});
```

Although `<MyComponent>` can never successfully render, the above code works perfectly fine. Instead of rendering a component, the stream is created with a serialized error inside it.

In fact, if we peek inside the stream weâll see the thrown error:

```
0:E{"digest":"","name":"Error","message":"Whoops!","stack":[["MyComponent","/index.js",9130,9,0,0,false]],"env":"Server","owner":null}
```

This is why throwing an error in an RSC environment doesnât cause `renderToRedableStream` to fail. React is able to catch the error and serialize it right into the RSC stream.

Although we have successfully created a stream, we donât know what will happen when the stream is handed off to a client for rendering.

### Errors during the SSR Render

The next rendering environment weâll look at is the SSR render. This environment is responsible for taking an RSC stream and producing HTML that can be served to a browser when it initially visits the application.

This environment relies on the `renderToReadableStream` API from the `react-dom/server` package.

Letâs see what happens when we try to render the RSC stream containing the error from above.

```
// The RSC environment creates a stream with an error

import { renderToReadableStream } from "react-server-dom-webpack/server";

function MyComponent() {
  throw new Error("Whoops!");
}

const rscStream = await renderToReadableStream(<MyComponent />, {});

// And now the SSR client environment tries to render that stream

import { createFromReadableStream } from "react-server-dom-webpack/client";
import { renderToReadableStream } from "react-dom/server";
import { use } from "react";

function App({ usableTree }) {
  const tree = use(usableTree);

  return (
    <html>
      <body>
        <p>Here is the React Server Component render turned into HTML:</p>
        <div>{tree}</div>
      </body>
    </html>
  );
}

const usableTree = createFromReadableStream(rscStream);

try {
  const htmlStream = await renderToReadableStream(
    <App usableTree={usableTree} />,
  );
  return new Response(htmlStream);
} catch (e) {
  console.log("Unable to render HTML...");
  console.log(error);
}
```

As soon as we try to turn this RSC stream into HTML we are met with a catastrophic error:

```
Unable to render HTML...

Error: Whoops!
    at MyComponent (about://React/Server/file:///index.js)
    ...
  environmentName: 'Server',
  digest: ''
}
```

React is unable to turn the `rscStream` into HTML due to the error inside the stream. The `renderToReadableStream` function from `react-dom/server` throws and weâre left with a rejected promise that contains the original *âWhoops!â* error from the RSC stream.

This is the point where React materializes the RSC error into an actual exception that our code has to handle. Conceptually, when React DOMâs `renderToReadableStream` encounters an RSC stream with an error itâs the same as rendering a component that throws an error. Whatâs so interesting about this is itâs not the RSC render that causes the exception, itâs the SSR render attempting to turn the RSC stream into HTML that forces the error to be dealt with.

So how do we deal with this error now that it has come to life?

Normally we would use a React Error Boundary to handle components that throw errors during render. However, since Error Boundaries do not work in the SSR environment the only option for our code here is to crash.

In this case, weâll need to update the try-catch statement to respond with something when it encounters an error.

```
import { createFromReadableStream } from "react-server-dom-webpack/client";
import { renderToReadableStream } from "react-dom/server";
import { use } from "react";

function App({ usableTree }) {
  const tree = use(usableTree);

  return (
    <html>
      <body>
        <p>Here is the React Server Component render turned into HTML:</p>
        <div>{tree}</div>
      </body>
    </html>
  );
}

const usableTree = createFromReadableStream(rscStream);

try {
  const htmlStream = await renderToReadableStream(
    <App usableTree={usableTree} />,
  );
  return new Response(htmlSream);
} catch (err) {
  return new Response(`Unable to generate SSR response`, {
    status: 500,
  });
}
```

Now responding with an *âUnable to generate SSR responseâ* isnât the most helpful message in the world, but since we cannot render the RSC stream there is not much left for the SSR environment to do in this situation.

Iâve found that the best thing to do here is to let the RSC stream attempt to render one more time, but this time in the browser instead of in the SSR environment. The reason being that the browserâs rendering environment has better options for handling errors.

### Errors during the Browser Render

The browser render is similar to the SSR render in that it takes an RSC stream that was created on the server and attempts to render it. However, since React supports Error Boundaries in the browser environment we have a blessed way to deal with RSC streams that contain errors.

app.jsxrsc-stream-error-boundary.jsx

```
// The RSC environment creates a stream with an error

import { renderToReadableStream } from "react-server-dom-webpack/server";

function MyComponent() {
  throw new Error("Whoops!");
}

app.get("/rsc-stream", async () => {
  const rscStream = await renderToReadableStream(<MyComponent />, {});
  return new Response(rscStream);
});

// And now the browser environment tries to fetch and render that stream

import { createFromFetch } from "react-server-dom-webpack/client";
import { createRoot } from "react-dom/client";
import { use } from "react";
import { RSCStreamErrorBoundary } from "./rsc-stream-error-boundary";

function App({ usableTree }) {
  const tree = use(usableTree);

  return (
    <html>
      <body>
        <p>Here is the React Server Component render turned into HTML:</p>

        <div>{tree}</div>
      </body>
    </html>
  );
}

const root = createRoot(document);

const usableTree = createFromFetch(fetch("/rsc-stream"));

root.render(
  <RSCStreamErrorBoundary>
    <App usableTree={usableTree} />
  </RSCStreamErrorBoundary>,
);
```

In the above example we fetch the RSC stream from an HTTP endpoint on our server and then attempt to render it using Reactâs browser APIs. Since the stream contains an error React will throw during render and the `<RSCStreamErrorBoundary>` component will catch the error and display a friendly message.

The browser environment is the only rendering environment that supports Error Boundaries. This means that whenever an Error happens during an RSC render our job is to get it over the browser as quickly as possible so that a message can be displayed to the user. 1

## How Suspense changes errors

So far in this post weâve only looked at a single Server Component that does nothing but throw an error. Real-world RSC applications are much more complicated and are often filled with streaming Suspense Boundaries.

Letâs take a look at what happens when we render an RSC stream that doesnât error until after a second.

```
import { renderToReadableStream } from "react-server-dom-webpack/server";

function MyTree() {
  return (
    <div>
      <p>Hello from RSC!</p>

      <Suspense fallback={<p>Waiting for the error...</p>}>
        <Throws />
      </Suspense>
    </div>
  );
}

async function Throws() {
  await new Promise((r) => setTimeout(r, 1000));

  throw new Error("Whoops (after 1 second)!");
}

const rscStream = await renderToReadableStream(<MyTree />, {});
```

For the first second the stream output looks normal, we see the serialized component tree and Suspense Boundary:

```
1:"$Sreact.suspense"
0:["$","div",null,{"children":[["$","p",null,{"children":"Hello from RSC!"}],["$","$1",null,{"fallback":["$","p",null,{"children":"Waiting for the error..."}],"children":"$L2"}]]}]
```

But then after a second the `<Throws>` component renders and our stream captures its error.

```
1:"$Sreact.suspense"
0:["$","div",null,{"children":[["$","p",null,{"children":"Hello from RSC!"}],["$","$1",null,{"fallback":["$","p",null,{"children":"Waiting for the error..."}],"children":"$L2"}]]}]

// one second later...

2:E{"digest":"","name":"Error","message":"Whoops (after 1 second)!","stack":[["Throws","/index.js",9138,9,0,0,false]]}
```

From our streams point of view thereâs no crash, itâs just a stream of JSX followed by a serialized error.

So weâre left with a stream that works for the first second and then fills with an error. What happens when we try to render this stream in an SSR environment?

### Suspended errors in SSR

In the SSR environment React will start producing HTML as soon as it has anything it can render. Since the tree now contains a Suspense Boundary with text that says *âWaiting for the error...â*, React can turn that into HTML before the `<Throws />` component finishes running.

```
// The RSC environment creates a stream with an error

import { renderToReadableStream } from "react-server-dom-webpack/server";

function MyTree() {
  return (
    <div>
      <p>Hello from RSC!</p>

      <Suspense fallback={<p>Waiting for the error...</p>}>
        <Throws />
      </Suspense>
    </div>
  );
}

async function Throws() {
  await new Promise((r) => setTimeout(r, 1000));

  throw new Error("Whoops (after 1 second)!");
}

const rscStream = await renderToReadableStream(<MyTree />, {});

// And now the SSR client environment tries to render that stream

import { createFromReadableStream } from "react-server-dom-webpack/client";
import { renderToReadableStream } from "react-dom/server";
import { use } from "react";

function App({ usableTree }) {
  const tree = use(usableTree);

  return (
    <html>
      <body>
        <p>Here is the React Server Component render turned into HTML:</p>
        <div>{tree}</div>
      </body>
    </html>
  );
}

const usableTree = createFromReadableStream(rscStream);

try {
  const htmlStream = await renderToReadableStream(
    <App usableTree={usableTree} />,
  );
  return new Response(htmlStream);
} catch (e) {
  console.log("Unable to render HTML...");
  console.log(error);
}
```

When the code above is rendered something interesting happens:

```
<!DOCTYPE html>
<html>
  <head></head>
  <body>
    <p>Here is the React Server Component render turned into HTML:</p>
    <div>
      <div>
        <p>Hello from RSC!</p>
        <!--$?-->
        <template id="B:0"></template>
        <p>Waiting for the error...</p>
        <!--/$-->
      </div>
    </div>

    <!-- A one second pause here... -->

    <script>
      $RX = function (b, c, d, e, f) {
        var a = document.getElementById(b);
        a &&
          ((b = a.previousSibling),
          (b.data = "$!"),
          (a = a.dataset),
          c && (a.dgst = c),
          d && (a.msg = d),
          e && (a.stck = e),
          f && (a.cstck = f),
          b._reactRetry && b._reactRetry());
      };

      $RX(
        "B:0",
        "",
        `
        Switched to client rendering because the server rendering errored:
        Whoops (after 1 second)!`,
        `
        Switched to client rendering because the server rendering errored:

        Error: Whoops (after 1 second)!
          at Throws (about://React/Server/file:////index.js?9:9138:9)
          ...
        `,
      );
    </script>
  </body>
</html>
```

We can see that React is able to successfully produce HTML for this RSC stream! In fact we see a Suspense Boundary, with ID `B:0`, that renders the *âWaiting for the error...â* fallback message.

Then after one second the interesting part happens. The `<Throws />` component throws its error and now there is nothing for React to fill in the `B:0` Suspense Boundary with. So instead React leaves the fallback rendered and displays a message that says: *âSwitched to client rendering because the server rendering erroredâ*.

And this is how Suspense Boundaries affect errors in the SSR environment. Once the SSR process has started generating HTML then any errors that happen inside of Suspense will cause those boundaries to remain in their fallback state. In a way, React has given up on rendering this part of the tree on the server.

Why give up? Well, React cannot throw an exception because itâs already produced HTML output from the non-suspended parts of the tree, but it also cannot render a component that errors. So the next best thing for React to do here is to leave this tree untouched and let the browser attempt to render it.

Letâs see what happens when the browser renders the error inside a `<Suspense>` Boundary.

### Suspended errors in the browser

Weâll use another browser based React app to fetch a suspended RSC error and attempt to render it.

app.jsxrsc-stream-error-boundary.jsx

```
// The RSC environment creates a stream with an error

import { renderToReadableStream } from "react-server-dom-webpack/server";

function MyTree() {
  return (
    <div>
      <p>Hello from RSC!</p>

      <Suspense fallback={<p>Waiting for the error...</p>}>
        <Throws />
      </Suspense>
    </div>
  );
}

async function Throws() {
  await new Promise((r) => setTimeout(r, 1000));

  throw new Error("Whoops (after 1 second)!");
}

app.get("/rsc-stream", async () => {
  const rscStream = await renderToReadableStream(<MyTree />, {});
  return new Response(rscStream);
});

// And now the browser environment tries to fetch and render that stream

import { createFromFetch } from "react-server-dom-webpack/client";
import { createRoot } from "react-dom/client";
import { use } from "react";
import { RSCStreamErrorBoundary } from "./rsc-stream-error-boundary";

function App({ usableTree }) {
  const tree = use(usableTree);

  return (
    <html>
      <body>
        <p>Here is the React Server Component render turned into HTML:</p>

        <div>{tree}</div>
      </body>
    </html>
  );
}

const root = createRoot(document);

const usableTree = createFromFetch(fetch("/rsc-stream"));

root.render(
  <RSCStreamErrorBoundary>
    <App usableTree={usableTree} />
  </RSCStreamErrorBoundary>,
);
```

Go ahead and try to render the suspended error in your browser:

When the browser attempts to render the RSC stream it will produce a Suspense Boundary with a *âWaiting for the error...â* fallback. Everything looks fine until the `<Throws />` component unsuspends and throws its error.

At this point the error materializes in the browser and we have to deal with. Since weâre in the browser React is able to let the closest Error Boundary catch and handle the error.

## Errors across the environments

Handling RSC errors during render is tricky because each environment treats errors differently from the others.

- In the RSC environment errors are treated as data and serialized into the RSC stream. They do not cause the RSC render to crash.
- In the SSR environment errors will crash the render if they happen outside of a Suspense Boundary. Inside a Suspense Boundary, errors cause the fallback to remain rendered and React stops rendering the suspended part of the tree.
- In the Browser environment errors will trigger the nearest Error Boundary. This allows applications to show helpful error messages to users.

My biggest take away from implementing errors inside an RSC framework is that an error needs to make itâs way to the browser as quickly as possible, since thatâs the only environment that can realistically use React to show an error message to the user. When errors happen in RSC or SSR there needs to be a clear path for rendering them in the browser.

Hopefully this article shed some light on how errors flow through Reactâs different rendering environments.

I plan on writing a few more posts on error handling that cover errors inside of server actions and using RSC errors for control flow in React. If thereâs anything about RSC error handling that youâd like to know more about please do not hesitate to reach out.

And as always thanks for reading.

Related notes: [[Server Components]]
