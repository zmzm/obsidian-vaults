---
type: twir-item
issue: 273
item: 3
item_type: item
date: 2026-03-18
source: https://www.aha.io/engineering/articles/why-we-rolled-our-own-rsc-framework
tags:
  - "RSC"
  - "SSR"
  - "ServerComponents"
status: auto
quality: keep
---

[[2026-03-18-TWIR-273|Index]]

# Item 3: Why we rolled our own React Server Components framework

Source: [https://www.aha.io/engineering/articles/why-we-rolled-our-own-rsc-framework](https://www.aha.io/engineering/articles/why-we-rolled-our-own-rsc-framework)

Summary:
The Aha! engineering team replaced their mature React framework with a custom, minimal RSC framework, reducing JS/JSON payloads by 90% and improving time-to-interactive by over 80%. The article explains their motivations, the trade-offs of frameworks, and how they achieved simplicity and performance with less than 1,000 lines of code. It also discusses the complexity of SSR and the rationale for building a bespoke solution versus using off-the-shelf frameworks.

Key takeaways:
- Custom RSC framework led to dramatic performance and payload improvements.
- Frameworks solve common problems (routing, SSR, data loading) but impose constraints and complexity.
- Server-side rendering is essential for fast, accessible content but adds significant setup overhead.
- Building a tailored framework is feasible for specific needs, but most teams benefit from established solutions.

Recommendation:
Read fully (especially for teams evaluating SSR, RSC, or considering custom frameworks)

Why it matters:
especially for teams evaluating SSR, RSC, or considering custom frameworks

Content:
# Less code, more power: Why we rolled our own React Server Components framework

We ripped out the mature React framework powering [this website](https://www.aha.io/) and built our own mini framework with a few handcrafted files. By most accounts, that's the last thing you should do. But it reduced the amount of JavaScript and JSON data loaded by 90% and cut our time-to-interactive by over 80%. Tedious tasks became trivial. It might be the right option for you, too!

I know what you might be thinking: "Yet *another* React framework? Doesn't a new one pop up every week? Use an existing one and save yourselves the trouble."

Or maybe: "Sure, you don't really need one of those complicated frameworks. Just drop in React as a client-side library like it was originally intended."

Or even: "React is too heavy for a content-focused website anyway. You should have used something else."

But none of those arguments felt right to us. We wanted it all — total customizability, great performance, and a smooth developer experience. And we built it in under 1,000 lines of code. Here's what it looks like to use:

```
export const handleRequest = defineApp(
 // Get a web Request, return a web Response
  route('/ping', (request) => new Response('pong')),
  // Or return JSX to send HTML!
  route('/greet/:name', (request, params) => (
    <Greeting name={params.name} />
  )),
);

async function Greeting(props: { name: string }) {
   // Do async work inline, no hooks or wrappers. Full access to secrets.
   // Only runs once on the server!
  await loadSomeData(process.env.ACCESS_TOKEN);
  return (
    <html>
      <body>
        <h1>Hello, {props.name}!</h1>
      </body>
    </html>
  );
}
```

You can also get it even smaller than we did. I'll show you how to build a full framework in under 50 lines of code.

## The case for frameworks

But let's back up. What really is a framework? Why do we reach for frameworks anyway?

UI libraries like React generally only handle updating the DOM. Frameworks (e.g., Next.js, React Router, TanStack Start, and Gatsby) handle other major concerns that pretty much every site needs: routing, data loading, and all the plumbing that needs to happen to turn your nice, clean components into raw HTML. They fill the gap between writing the components that define what should go on a page and having a real, functional website. And they go to great lengths to make sure your site is fast to use. It's a big job!

Of course, you *can* build a React application without any special setup, and even without JSX syntax:

```
<html>
<body>
  <div id="root"></div>
  <script type="module">
  import React from "https://esm.sh/react";
  import ReactDOM from "https://esm.sh/react-dom";

  function Greeting(props) {
    return React.createElement("h1", {}, "Hello, ", props.name, "!");
  }

  const root = ReactDOM.createRoot(document.getElementById("root"));
  root.render(React.createElement(Greeting, { name: "Josh" });
  // <h1>Hello, Josh!</h1>
  </script>
</body>
</html>
```

A little ugly, but simple!

As a web developer, you'd probably add a build step to use JSX and TypeScript syntax. You would also split up your code into multiple files, making it easier to write more components. Whether you do or don't, though, the architecture is still the same. *That's where the trouble starts*.

When you first load the page above, it's completely blank. Your users won't see any content until your JavaScript dependencies load and your React components mount. For smaller greenfield projects and on fast developer machines, that might not be a noticeable delay. But it can be surprisingly frustrating for users with slow mobile phones on lagging network connections. And bots that don't run JavaScript will see your site as just a blank screen.

How do you fix this? Generally, what you want to do is to ensure all of your content is already in the HTML you serve to the user, so it's visible instantly. (This is known as server-side rendering, or SSR.)

```
<html>
<body>
  <div id="root">
    <h1>Hello, Josh!</h1>
  </div>
  <script type="module">
    // continued...
```

Doing this is not as easy as it might seem. You need to:

```
import ReactDOMServer from "react-dom/server";
import { Greeting } from "./greeting.tsx";

// this is usually fingerprinted, e.g., "client-ab6df7e.js"
const builtScriptLocation = "/assets/client.js";

export const handleRequest = (request: Request) => {
  return new Response(`
<html>
<body>
  <div id="root">
    ${ReactDOMServer.renderToString(<Greeting name="Josh" />)}
  </div>
  <script type="module" src="${builtScriptLocation}"></script>
</body>
</html>`, {
    headers: {
      "Content-Type": "text/html"
    }
  });
}
```

Your simple setup is suddenly riddled with complexity. It's fragile, and you'll find yourself reading manifest files from bundler outputs. And not everybody uses a JavaScript runtime like Node.js on the server. So many people stop here, stick with just a client-side script, and deal with the blank initial load.

Fortunately, framework authors have already done the dirty work for you! You can start with a simple client-side script, and then add in SSR as needed without pulling your hair out. Frameworks usually also give you additional APIs to handle data fetching, routing, forms, headers, cookies, and more. You also might get options for how you want your site to be delivered, like as a collection of `*.html` files or with automatic deploys to some cloud provider. For most people, using a modern off-the-shelf framework is the best option.

## The case against frameworks

That begs the question: If frameworks save you so much work, why did we get rid of one and build our own?

Frameworks come with opinions. Some more than others, but that's the deal. (By opinions, I mean answers to questions like: How do you define what pages there are? How do you load the data a page needs?) There are many possible ways to build a full-stack web application, and frameworks *must* constrain how you build so they can provide useful abstractions to make your life easier.

That's generally for the best. Ideally, a framework's opinions will make your site faster to load, easier to develop, and more [lovable](https://www.aha.io/roadmapping/guide/plans/what-is-a-minimum-lovable-product) to use. You'll be guided down a happy path — free to focus on what differentiates your site and not slogging through bundler configuration. It's similar to how React frees you to focus on what content should be on the screen instead of wiring together thousands of low-level `document.createElement()` calls.

*However.* Sometimes, a framework's opinions don't age gracefully. This is especially true in the JavaScript ecosystem, where new techniques are constantly emerging.

We previously used Gatsby for this website. Like other React frameworks built at the time, its opinion is to load and run React components for *everything* on the page, even the non-interactive static parts. As our website grew, the amount of JavaScript we shipped grew with it. We determine which components to render based on content, so we couldn't even take advantage of code-splitting — all of the JavaScript for our components needed to be loaded upfront.

Gatsby in particular optimizes for static site generation (SSG). It runs SSR in a build step — rendering all your pages to plain HTML — to get benefits like great initial load times and cheap hosting. But that comes at the cost of having to rebuild and redeploy the entire site when any of its content changes. A blog post author fixed a typo? We'd need to redeploy. It was a long, inefficient feedback loop for our marketing team.

The crux of the issue? You'll have a good time if you can work within a framework's opinions. But if a framework doesn't provide what you need on an architectural level, you'll have to migrate to something else. And here's the kicker: You can't always predict what architecture you'll eventually need.

## How to build a React Server Components framework

Remember how complex and fragile it is to build your own SSR? Building a whole framework has been a nightmare. But that's changed recently for two reasons:

1. React 19 released [React Server Components](https://react.dev/reference/rsc/server-components) (RSCs). Server Components are distinct from the components you know (Client Components) and *only run once on the server* (or during a build step). The browser never sees the code for these components, only their rendered output. Server Components can be async, load data, and access secrets. By loading data and passing it to a Client Component, the complexity of client-side data fetching completely disappears. The `<Greeting>` example at the top of this post is just a Server Component — everything it can do is provided by React alone.
2. Vite (the bundler on which most modern frameworks are built) now has an official [RSC plugin](https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-rsc). Server Components have been public in some form since [2020](https://legacy.reactjs.org/blog/2020/12/21/data-fetching-with-react-server-components.html), but until recently they've been undocumented, requiring incredibly deep expertise with Webpack plugins and the React codebase just to get a toy example running. Now, you can browse the Vite RSC plugin's [examples directory](https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-rsc/examples) and get started with RSCs in minutes.

By evolving from a front-end library to a suite of features covering the full stack, React absorbs much of the complexity frameworks used to handle. RSCs *are the API* for many needs that previously required dedicated framework support. So with less to do and better tooling to do it, it's now feasible to build your own framework! You can start from a template with `npm create vite@latest -- --template rsc` or from scratch.

### Entries

The first thing you notice when you configure the RSC Vite plugin is an `entries` option:

```
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import rsc from '@vitejs/plugin-rsc';

export default defineConfig({
  plugins: [
    react(),
    rsc({
      entries: {
        rsc: './src/framework/entry.rsc.tsx',
        ssr: './src/framework/entry.ssr.tsx',
        client: './src/framework/entry.client.tsx',
      }
    }),
  ],
});
```

"Entry" in a bundler config refers to the main module — the first file to be run. But why are there three: `rsc`, `ssr`, and `client`?

Again, modern front ends don't only run JavaScript in the browser anymore. They also run JavaScript on a server or during the bundler build step. Vite's [Environment feature](https://vite.dev/guide/api-environment) lets you bundle JavaScript for both the browser and a server runtime like Node.js in one build step and from one codebase. Here, the `client` entry is the first module run in the browser and handles rendering interactive Client Components there. The `ssr` entry runs the exact same Client Components on the server side to produce the initial plain HTML. (Yes, SSR is a "client." It does effectively the same job as the browser, just without a real DOM or interactivity.)

That explains two of them, but what about the `rsc` entry? Don't Server Components also run on the server side?

Yes, but RSCs are *different*. They can be `async`, they only run once, and they can't use React's interactive features, like hooks or event handlers. Their output — JSX and props — is serialized to a special format known as an "RSC payload" in a separate step from SSR. The `ssr` entry then combines that payload with your Client Components to produce HTML. This doesn't have to matter much in practice, as you can run both `rsc` and `ssr` in the same process to render your Server Components directly into HTML.

### Framework files

Let's finally have a peek at what should go in those `./src/framework/entry.*.tsx` files. We'll keep it as simple as possible — we want our framework to always serve HTML, and we'll use standard browser navigation (no client-side routing). The beauty of owning your framework is that you can add whatever else you need.

The RSC entrypoint's job is to render Server Components into an RSC payload as a stream. By default, we need to export a handler function that receives a `Request` and returns a `Response`. It's a surprisingly small amount of code:

```
// src/framework/entry.rsc.tsx
import * as ReactServer from '@vitejs/plugin-rsc/rsc';
import Root from '../../Root.tsx';

export default async function handleRequest(
  request: Request
): Promise<Response> {
  // turn the <Root> Server Component into an RSC payload.
  // Server Components can be async, so the payload streams in.
  const rscStream = ReactServer.renderToReadableStream(
    <Root request={request} />
  );

  // delegate to the SSR environment to turn the RSC payload into HTML.
  const ssrEntryModule = await import.meta.viteRsc.loadModule<
    typeof import('./entry.ssr.tsx')
  >('ssr', 'index');
  // HTML streams in as content is ready, based on <Suspense> boundaries.
  const htmlStream = await ssrEntryModule.renderHTML(rscStream);

  // stream the HTML to the user
  return new Response(htmlStream, {
    headers: { 'Content-Type': 'text/html;charset=utf-8' }
  });
}
```

The SSR entrypoint's job is to turn the RSC payload into HTML. Again, it's very small:

```
// src/framework/entry.ssr.tsx
import { use, type ReactNode } from 'react';
import { renderToReadableStream } from 'react-dom/server';
import * as ReactClient from '@vitejs/plugin-rsc/ssr';

export async function renderHTML(rscStream: ReadableStream<Uint8Array>) {
  // turn the RSC payload containing <Root>'s output into JSX and render it.
  // (needs to be inside a component for certain APIs to work.)
  let jsx: Promise<ReactNode> | undefined;
  function SsrRoot() {
    jsx ??= ReactClient.createFromReadableStream<ReactNode>(rscStream);
    return use(jsx);
  }

  // render the SsrRoot component to HTML, just like the original SSR example
  const htmlStream = await renderToReadableStream(<SsrRoot />);
  return htmlStream;
}
```

At this point, you have a fully functional HTML server powered by RSCs! It supports importing CSS, rendering all DOM elements (including `<html>`, `<link>`, and `<meta>`), and streaming in parts of a page as they're ready while other parts are waiting on async work. All with zero bytes of bundle size. It's as if React had been rebuilt from the ground up as a server-side templating engine based on async components. With this, you could use React to build a basic site with the same page weight as handwritten HTML.

But there's still something missing: the client entrypoint, `entry.client.tsx`. Without that, no JavaScript is loaded and none of your Client Components will run in the browser. Look how small it is:

```
// src/framework/entry.client.tsx
import { createElement, use, type ReactNode } from 'react';
import { hydrateRoot } from 'react-dom/client';
import * as ReactClient from '@vitejs/plugin-rsc/browser';

const rscStream = getRscStream(); // TODO: load the RSC payload somehow

// turn the RSC payload containing <Root>'s output into JSX and hydrate it.
const jsx = ReactClient.createFromReadableStream<ReactNode>(rscStream);
function ClientRoot() {
  return use(jsx);
}

hydrateRoot(
  // hydrate the entire document, not just a div, to control <html> and <head>
  document,
  // same as <ClientRoot />, but helps avoid issues from HMR/Fast Refresh
  createElement(ClientRoot, {})
)
```

Notice that just like the SSR `renderHTML()` function, we need the RSC payload on the client. React (in the browser) needs to know what Client Components to load and how to match them up to the HTML. There are different ways to do this, but the [rsc-html-stream](https://github.com/devongovett/rsc-html-stream) package makes it easiest — it embeds the RSC payload into the HTML.

```
// src/framework/entry.ssr.tsx
import { use, type ReactNode } from 'react';
import { renderToReadableStream } from 'react-dom/server';
import * as ReactClient from '@vitejs/plugin-rsc/ssr';
import { injectRSCPayload } from 'rsc-html-stream/server'; 

export async function renderHTML(rscStream: ReadableStream<Uint8Array>) {
  // duplicate the RSC stream: one to generate the HTML,
  // one to embed inside the HTML
  const [rscStream1, rscStream2] = rscStream.tee();
  rscStream = rscStream1;

  // turn the RSC payload containing <Root>'s output into JSX and render it.
  // (needs to be inside a component for certain APIs to work.)
  let jsx: Promise<ReactNode> | undefined;
  function SsrRoot() {
    jsx ??= ReactClient.createFromReadableStream<ReactNode>(rscStream);
    return use(jsx);
  }

  // render the SsrRoot component to HTML, just like the original SSR example
  const htmlStream = await renderToReadableStream(<SsrRoot />, {
    bootstrapScriptContent:
      await import.meta.viteRsc.loadBootstrapScriptContent('index'),
  });

  // transform the HTML stream to embed the RSC payload
  const htmlStreamWithPayload = htmlStream.pipeThrough(
    injectRSCPayload(rscStream2)
  );
  return htmlStreamWithPayload;
}
```

```
// src/framework/entry.client.tsx
import { createElement, use, type ReactNode } from 'react';
import { hydrateRoot } from 'react-dom/client';
import * as ReactClient from '@vitejs/plugin-rsc/browser';

// import the RSC payload extracted from the HTML
import { rscStream } from 'rsc-html-stream/client';

// etc.
```

That's it! You now have a fully functional RSC framework. Data fetching and static work like rendering Markdown can run on the server, while React's state-of-the-art interactivity can still run in the browser. Only Client Components add to your bundle size, and code splitting Just Works™ better than ever before.

While this isn't trivial, it's easier than building support for SSR alone, and much more powerful. How? The RSC Vite plugin and React 19 have absorbed a ton of complexity. For example, loading JavaScript and CSS assets correctly is one of the most difficult parts of supporting SSR. Now, the RSC Vite plugin provides the script needed to bootstrap React rendering, and adds `<link ref="stylesheet" href="some-fingerprinted-stylesheet.css">` to your components. React 19 handles moving `<link>`, `<meta>`, and `<title>` tags into the document `<head>`, no matter where they are, and prevents flash-of-unstyled-content. As a framework author, all you need to do is add a few lines of boilerplate code.

You can find the full code for this micro-framework [on GitHub](https://github.com/aha-app/micro-rsc-framework). Or, [try it out](https://stackblitz.com/github/aha-app/micro-rsc-framework?file=src%2FRoot.tsx) in an online code editor.

### What to build next

This micro-framework probably won't meet all of your needs. Fortunately, you own this code and can change it as you see fit.

- Want a server router like ~~Express~~ [Hono](https://hono.dev/)? Point the RSC entrypoint to a file like `src/server.tsx`, turn your `src/framework/entry.rsc.tsx` into an importable utility to convert JSX to HTML, and add a bunch of routes that render your Server Components. Build your own server router if you want.
- Want client-side navigations instead of standard browser navigations? Intercept link clicks with event delegation and listen to `'popstate'` events to hijack browser navigations, and fetch RSC payloads for the next page. Use a convention like an `Accept: x-rsc-payload` header to fetch RSC payloads directly. Or fetch the HTML and extract the RSC from it, using Base64 instead of `rsc-html-stream`.
- Want to put your server behind a CDN? Add a `Cache-Control: public, max-age=123` header to your responses, and use `import { prerender } from 'react-dom/static'` instead of `import { renderToReadableStream } from 'react-dom/server'`.
- Want file-based routing where your routes are determined by the layout of your source code? You can build your own in a few lines with Vite's `import.meta.glob()` feature. Use a pattern that matches all the files you want, then map the keys of the object it gives you to a route with each module.

  ```
  for (const [path, loadModule] of Object.entries(
    import.meta.glob("./pages/**/*.{js,jsx,ts,tsx}"),
  )) {
    const pattern = path
      .replace(/^\.\/pages|\.(js|jsx|ts|tsx)$/g, "")
      .toLowerCase();
    addRoute(pattern, async () => {
      const Component = (await loadModule()).default;
      return <Component />;
    });
  }
  ```
- Want to forego a server and build a static site? You can write a Vite plugin that handles it based on [this example](https://github.com/vitejs/vite-plugin-react/blob/0a158860f75bb4152bc7fdf4bf487a138a1f7f71/packages/plugin-rsc/examples/ssg/vite.config.ts#L27-L74). Any server-rendered site can be turned into a static site by hitting the server with requests and storing the responses to disk. You'll need a way to determine which routes to build upfront. This doesn't have to be all or nothing — you could make some routes static and some routes dynamic. If you want to get fancy, build a list of routes statically and fall back to the server once those routes aren't fresh enough (known as Incremental Static Regeneration).
- Want to use React's support for Server Functions, Actions, and forms? Pull in a few more lines of boilerplate from [this example](https://github.com/vitejs/vite-plugin-react/blob/0a158860f75bb4152bc7fdf4bf487a138a1f7f71/packages/plugin-rsc/examples/starter/src/framework/entry.rsc.tsx).

We added variations of all the above features and kept it under 1,000 lines of code. Compared to about a million lines of code powering the biggest frameworks, it feels miraculous.

Want something else? With such powerful low-level APIs, you can do things that aren't possible in other frameworks or come up with a totally different way to work with RSCs. Leverage your hosting provider's APIs or your infrastructure for caching, edge rendering, and more. Remember: RSC payloads are just streams of bytes representing JSX, and they can be shuffled around as you please.

## Should you build a framework?

Even if you *can* build a React framework, does it mean you *should*? There's been a lot of controversy about that question. The React team [puts it fairly](https://react.dev/learn/build-a-react-app-from-scratch#consider-using-a-framework):

> As your requirements evolve, you may need to solve more framework-like problems that our recommended frameworks already have well-developed and supported solutions for. ... Our recommended frameworks also help you build better-performing apps. ... Going this route also makes it more difficult to get support, since the way you develop routing, data-fetching, and other features will be unique to your situation. You should only choose this option if you are comfortable tackling these problems on your own.

You'll have an easier time using one of the [recommended frameworks](https://react.dev/learn/creating-a-react-app#full-stack-frameworks), especially as you're getting started. They're built by developers who treat it as a full-time job, not just a setup that needs to be good enough to ship your actual features. If you need a new feature, it may already be usable with a line of configuration. If a bug is found, someone else will probably report it and a maintainer will get it fixed. And there's actual documentation for those who still read it.

When evaluating React frameworks, you'll probably look at the development velocity, the size and maturity of the ecosystem, and performance metrics. You'll consider how well they meet your current and expected needs and how badly you'd be locked in if you ever wanted to migrate. All important things, but I'd encourage you to also look into the framework's *philosophy:*

- [Next.js](https://nextjs.org/docs) tries to optimize your site automatically by choosing the architecture for each route based on which magical APIs you use.
- [React Router](https://reactrouter.com/home) (AKA Remix) ties data loading to routes (not components) and emphasizes web standards.
- [TanStack Start](https://tanstack.com/start/latest) focuses on type safety to a remarkable degree and prioritizes client-first development, layering on server-side features instead of RSC's server-first approach.
- [Waku](https://waku.gg/) and [RedwoodSDK](https://docs.rwsdk.com/) are minimal RSC frameworks. RedwoodSDK has an especially clear philosophy that I strongly agree with and implemented in our framework's design: zero magic, composability over configuration, and web-first architecture.

If one of these frameworks meets your needs and matches your philosophy, it's probably the best option for your next site.

The calculus changes a bit if you already have an established site and need to migrate off your current setup. There might not be a smooth migration path to your framework of choice. Building your own framework gives you the opportunity to shape the available APIs in a backward-compatible way so you don't have to rewrite as much of your codebase. While you can build a compatibility layer on top of any framework, full control gives you more power and saves you from mediating your old and new frameworks' competing opinions. Don't get me wrong — it won't be easy to keep your site running while you swap out the framework powering it on top of building your new framework. But you might find that easier than migrating to a framework you don't own.

Beyond the pragmatic case for building a framework, there's a more personal one: You might just want to bring your own philosophy to life. Maybe you'll share it with the world someday, or maybe you'll keep it tailored just right for yourself. Do whatever you want, because now you can.

---

**We're happy and hiring engineers — take a look at** [**our open roles**](https://www.aha.io/company/careers/current-openings)**.**

Related notes: [[Server Components]]
