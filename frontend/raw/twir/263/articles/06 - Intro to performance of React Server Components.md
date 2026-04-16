---
type: twir-item
issue: 263
item: 6
item_type: item
date: 2025-12-17
source: https://calendar.perfplanet.com/2025/intro-to-performance-of-react-server-components/
tags:
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-12-17-TWIR-263|Index]]

# Item 6: Intro to performance of React Server Components

Source: [https://calendar.perfplanet.com/2025/intro-to-performance-of-react-server-components/](https://calendar.perfplanet.com/2025/intro-to-performance-of-react-server-components/)

Summary:
This article provides a practical overview of React Server Components (RSC) from a performance perspective, comparing them to traditional client-side and server-side rendering. It explains how RSC can reduce JavaScript sent to the client, enable earlier data fetching, and improve initial load times, but also notes the complexity of measuring real-world impact due to integration with frameworks and bundlers.

Key takeaways:
- RSC aims to improve performance by offloading work to the server and reducing client JS.
- Measuring RSC performance requires understanding both client and server rendering models.
- Real-world performance gains depend on app architecture and backend/API speed.
- The article is a condensed version; a much longer, detailed investigation is available.

Recommendation:
Read fully

Content:
# Intro to Performance of React Server Components

Have you heard of [React Server Components](https://react.dev/reference/rsc/server-components)? Even if you don’t work with React daily, you probably have. It’s been the hottest topic in the last few years in the React Community.

And in addition to being the fanciest new toy, Server Components are quite often mentioned in the context of performance. As in, they are supposed to be really good for it.

Their main promise is relatively simple: we push more work to the server, ship less JavaScript, fetch data earlier, and the initial load of a page gets faster. But how exactly does this happen? And how much of a performance improvement can I expect? This is what I want to investigate today.

By the way, this article is a much shorter overview for the non-React audience of a full investigation, which is a 40-minute read. If you *really* want to know all the implementation details, [check out the original](https://www.developerway.com/posts/bundle-size-investigation).

## Setting Up the Investigation

Here’s the kicker, though: I can’t just *use* Server Components in isolation to measure what I want. It’s not a React feature that I can turn on and off.

It’s highly complicated technology, deeply integrated into some of the modern bundlers and frameworks, and almost impossible to replicate at home. At least with a reasonable amount of effort.

Also, it’s not the simplest feature to understand either. To actually make sense out of it, especially in the performance context, it’s almost mandatory to have a very clean mental model of how React normally renders and fetches data.

Both on the client and on the server, by the way! Because he’s the fun part: we already have the concept of server rendering! And had it for *years*. So what exactly is the difference then?

To investigate all of this, I built a single-page app (SPA) with multiple client-side routes and client-side data fetching. It’s also [available on GitHub](https://github.com/developerway/react-server-components) in case you want to replicate all the experiments by yourself.

One of the pages on that website looks like this:

![Demo app inbox page showing sidebar navigation on the left and messages list on the right](https://calendar.perfplanet.com/images/2025/nadia/inbox-full.png)

Some data on that page is dynamic and is fetched via REST endpoints. Namely, items in the Sidebar on the left are fetched via the `/api/sidebar` endpoint, and the list of messages on the right is fetched via the `/api/messages` endpoint.

The `/api/sidebar` endpoint is quite fast, taking **100ms** to execute. The `/api/messages` endpoint, however, takes **1s**: someone forgot to optimise the backend here. Those numbers are somewhat realistic for projects on the older and larger side, I’d say.

For this article, I’m going to focus on initial load and measure:

- Good old [LCP](https://web.dev/articles/lcp), which happens to correspond to the loading of the static part of the page.
- The time when the messages in the Inbox list become visible.
- The time when the items in the sidebar become visible.

## Client-Side Rendering

First, Client-Side Rendering. Depending on the year you were born, Client-Side Rendering might be your default React or even default Web experience.

From an implementation point of view, it means that when your browser requests the `/inbox` URL, the server responds with the HTML that looks like this:

```
<!doctype html>  
<html lang="en">  
  <head>  
    <script type="module" src="/assets/index-C3kWgjO3.js"></script>  
    <link rel="stylesheet" href="/assets/index-C26Og_lN.css">
  </head>  
  <body>  
    <div id="root"></div>  
  </body>  
</html>
```

You’ll have `script` and `link` elements in the `head` tag and the empty `div` in the `body`. That’s it. If you disable JavaScript in your browser, you’ll see an empty page, as you’d expect from an empty div.

To transform this empty `div` into a beautiful page, the browser needs to download and execute the JavaScript file(s). The file(s) will contain everything you write as a React developer:

```
// That's the entry point to the beautiful app
export default function App() {  
  return (  
    <SomeLayout>  
      <Sidebar />  
      <MainContent />  
    </SomeLayout>  
  );  
}
```

Plus something like this:

```
// this is made up API for simplicity
const DOMElements = renderToDOM(<App />);
const root = document.getElementById("root");
root.appendChild(DOMElements);
```

React itself transforms the entry point `App` component into DOM nodes. Then it finds that empty div by its `id`. And injects those generated elements into the empty div.

The entire interface is suddenly visible.

If you record Performance for the initial load, the picture will be something like this:

![Timeline diagram showing client-side rendering](https://calendar.perfplanet.com/images/2025/nadia/client-side-rendering-schema.png)

While the JavaScript is downloading, the user still stares at the empty screen. Only after everything is downloaded AND JavaScript is compiled and executed by the browser, the UI becomes visible, the LCP metric is recorded, and the side effects, like fetch requests, are triggered.

The initial loading numbers with no JavaScript cached look like this, with the CPU and Network throttling (6x slowdown and Slow 4G):

|  | LCP | Sidebar | Messages |
| --- | --- | --- | --- |
| Client-Side Rendering | 4.1 s | 4.7 s | 5.1 s |

## Server-Side Rendering (No Data Fetching)

The fact that we have to stare at the blank page for so long started to annoy people at some point. Even if it was for the first time only. Plus, for SEO purposes, it wasn’t the best solution.

So people started scratching their heads to come up with a solution. While still staying within the React world, which was just way too convenient to give up.

We know that the entire React app at the very end looks like this:

```
// this is a made-up API for simplicity
const DOMElements = renderToDOM(<App />);
```

But what if instead of DOM nodes, React could produce the HTML of the app instead?

```
const HTMLString = renderToString(<App />);
```

Like the actual string that the server can then send to the browser instead of the empty div?

```
// HTMLString then would contain this string:
<div className="...">
  <div className="...">...</div>
  ...
</div>
```

In theory, our extremely simple server for the Client-Side Rendering:

```
// Yep, this is basically all we need for the Client-Side Rendering
export const serveStatic = async (c) => {
  const html = fs.readFileSync("index.html").toString();

  return c.body(html, 200);
};
```

Can continue to be just as simple. It just needs one additional step: find-and-replace a string in the `html` variable.

```
// Same server with SSR
export const serveStatic = async (c) => {
  const html = fs.readFileSync("index.html").toString();
  
  // Extract HTML string
  const HTMLString = renderToString(<App />);
  // And inject it into the server response
  const htmlWithSSR = html.replace('<div id="root"></div>', HTMLString);
  
  return c.body(htmlWithSSR, 200);
};
```

Now the entire UI will be visible right at the beginning without waiting for any JavaScript.

Welcome to the server-side rendering (SSR) and static-site generation (SSG) era of React. Because [renderToString](https://react.dev/reference/react-dom/server/renderToString) is actually a real API supported by React. This is literally the core implementation behind some of the React SSG/SSR frameworks.

If I do exactly this for my client-side rendered project, it will be a server-side rendered project. The performance profile will shift slightly. The LCP number will move to the left, right after the HTML and CSS are downloaded, since the entire HTML is sent in the initial server response, and everything is visible right away.

![Timeline diagram showing server-side rendering](https://calendar.perfplanet.com/images/2025/nadia/server-side-rendering.png)

A few important things here.

First, as you can see, the LCP number (when the page “Skeleton” is visible) should drastically improve (we’ll measure it in a bit).

However, we still need to download, compile, and execute the same JavaScript in the exact same way. Because the page is supposed to be interactive, i.e., all those dropdowns, filters, and sorting algorithms we implemented should work. And while we wait, the entire page is already visible!

That gap between the page being already visible, but we’re still waiting for JavaScript download to make it interactive, is the time when the page will appear ***broken*** to the users. Unless special measures are taken, of course.

Also, only the LCP mark has moved on that picture. The “Sidebar items” and “Messages” are in exactly the same places, structurally speaking. This is because we haven’t changed the code a bit and are still fetching that data on the client!

As a result, the fact that we have the page pre-rendered on the server has exactly zero effect on the time when the Sidebar items or the list data show up.

And here are the numbers:

|  | LCP (no cache) | Sidebar (no cache) | Messages (no cache) | No interactivity gap |
| --- | --- | --- | --- | --- |
| Client-Side Rendering | 4.1 s | 4.7 s | 5.1 s |  |
| Server-Side Rendering (Client Data Fetching) | **1.61 s** | 4.7 s | 5.1 s | 2.39 s |

As you can see, the LCP value on initial load indeed radically dropped: from **4.1 s to 1.61 s**! Exactly as in the theoretical schematic. However, the page is not interactive for more than 2 seconds on the initial load.

That “no interactivity gap”, along with the cost of having a server, is the price you’ll pay for LCP improvements when transitioning from Client-Side Rendering to Server-Side Rendering. There is no way to get rid of it. We can only minimize it by reducing the amount of JavaScript the users have to download during the first run.

However, no one is going to implement SSR manually. Most likely, people are going to use some SSR-friendly framework right away. If I move my app to Next.js, for example, the numbers will look like this:

|  | LCP (no cache) | Sidebar (no cache) | Messages (no cache) | No interactivity gap |
| --- | --- | --- | --- | --- |
| Client-Side Rendering | 4.1 s | 4.7 s | 5.1 s |  |
| Server-Side Rendering (Client Data Fetching) | **1.61 s** | 4.7 s | 5.1 s | 2.39 s |
| Next.js SSR (latest version) | ***1.28 s*** | 4.4 s | 4.9 s | 2.52 s |

Next.js handles code splitting and resource prioritization very differently, so it managed to squeeze even more out of the LCP. The rest of the numbers are similar.

## Server-Side Rendering (With Data Fetching)

“No interactivity gap” aside, there is another somewhat problematic area in the previous experiment. The fact that there were no changes in the Sidebar and Messages appearances. But since we’re in the server realm already, why can’t we extract that data here? It surely will be faster. At the very least, latency and bandwidth will likely be much better.

The answer: we absolutely can! It would need to do much more work implementation-wise, though, compared to the simple pre-rendering we did. First, the server. We need to fetch that data there:

```
// Add data fetching to the SSR server
export const serveStatic = async (c) => {
  const html = fs.readFileSync("index.html").toString();
  
  // Data fetching logic
  const sidebarPromise = fetch(`/api/sidebar`).then((res) => res.json());  
  const messagesPromise = fetch(`/api/messages`).then((res) => res.json());  
    
  const [sidebar, messages] = await Promise.all([  
    sidebarPromise,  
    messagesPromise,  
  ]);
  
  // Extract HTML string
  const HTMLString = renderToString(<App />);
  // And inject it into the server response
  const htmlWithSSR = html.replace('<div id="root"></div>', HTMLString);

  ... // the rest is the same
};
```

Then, we’d need to pass that data to the React app:

```
// Pass fetched data as props
const HTMLString = renderToString(<App messages={messages} sidebar={sidebar} />);
```

Then a bunch of magic with injecting that data into the HTML code, then on the app’s side, extracting that data and initializing the app. The exact details not important right now. The important thing is:

- Nothing stops us from fetching that data on the server. We just need to `await` for a few promises.
- It works like a charm!

The performance structure will change again:

![Timeline diagram showing SSR with server data fetching](https://calendar.perfplanet.com/images/2025/nadia/server-side-rendering-with-data.png)

Now the entire page, including previously dynamic items, will be visible as soon as CSS finishes downloading. Then, we’ll still have to wait for the exact same JavaScript as before, and only after that, the page will become interactive.

Again, most of the time, people would use a framework for this, so I’ll show the Next.js numbers right away:

|  | LCP (no cache) | Sidebar (no cache) | Messages (no cache) | No interactivity gap |
| --- | --- | --- | --- | --- |
| Client-Side Rendering | 4.1 s | 4.7 s | 5.1 s |  |
| Server-Side Rendering (Client Data Fetching) | **1.61 s** | 4.7 s | 5.1 s | 2.39 s |
| Next.js SSR (Client Data Fetching) | ***1.28 s*** | 4.4 s | 4.9 s | 2.52 s |
| Next.js SSR (Server Data Fetching) | 1.78 s | 1.78 s | 1.78 s | 2.52 s |

The LCP value, unfortunately, degraded. This is no surprise. It’s because we now have to wait for data-fetching promises to resolve themselves before we can proceed with pre-rendering of the React part.

And we really must wait for them since we need that data to start rendering anything.

Sidebar and Messages items, however, appear much faster now: **1.78 seconds instead of 4.9 seconds**. So it could be called an improvement if the LCP number is not that important to you compared to the full-page view. Or, we could pre-fetch only the Sidebar, by the way, with minimal regression (this endpoint is pretty fast), and keep the Messages part on the client.

## Introducing React Server Components

Okay, so to recap the previous section: fetching and pre-rendering on the server can be really good for the initial load performance numbers. There is, however, an issue with it still.

Data fetching! Currently, if I want to pre-fetch messages on the server, thus reducing the wait time for messages to appear, it will negatively affect both the initial load and the time when the sidebar items show up.

This is due to the fact that server rendering is currently a synchronous process. We wait for all the data first, then pass that data to `renderToString`, then send the result to the client.

![Diagram showing synchronous SSR structure](https://calendar.perfplanet.com/images/2025/nadia/current-ssr-structure.png)

But what if our server could be smarter? Those fetch requests are promises, async functions. Technically, we don’t *need* to wait for them to start doing something else. What if we could:

1. Trigger those fetch promises without waiting for them.
2. Start rendering React stuff that doesn’t need that data, and if it’s ready, send it to the client immediately.
3. When the Sidebar promise is resolved and its data is available, render the Sidebar portion, inject it into the server page, and send it to the client.
4. Do the same for the Messages.

Basically, replicate the exact same structure of data fetching that we have in the Client-Side Rendering, but *on the server*.

![Diagram showing React Server Components streaming structure](https://calendar.perfplanet.com/images/2025/nadia/server-components-structure.png)

In theory, if this is possible, it could be crazy fast. We’d be able to serve the initial rendered page with placeholders at the speed of the simplest SSR, and still be able to see Sidebar and Messages items way *before* any JavaScript is downloaded and executed.

React would need to abandon the simple synchronous `renderToString` for this, rewrite the rendering process to be in chunks, make those chunks injectable into the rendered structure somehow, and be able to serve those chunks independently to the client.

That’s quite a task! And it’s literally what React Server Components in combination with Streaming do.

How exactly it’s implemented is [mind-blowingly complicated](https://www.developerway.com/posts/react-server-components-performance#introducing-react-server-components) and not really relevant for the non-React audience. Let’s assume it works exactly as described. In this case, for the purpose of this exercise, we only need to see the numbers.

And here they are:

|  | LCP (no cache) | Sidebar (no cache) | Messages (no cache) | No interactivity gap |
| --- | --- | --- | --- | --- |
| Client-Side Rendering | 4.1 s | 4.7 s | 5.1 s |  |
| Server-Side Rendering (Client Data Fetching) | **1.61 s** | 4.7 s | 5.1 s | 2.39 s |
| Next.js SSR (Client Data Fetching) | ***1.28 s*** | 4.4 s | 4.9 s | 2.52 s |
| Next.js SSR (Server Data Fetching) | 1.78 s | 1.78 s | 1.78 s | 2.52 s |
| Next.js App router (Server Fetching with Suspense) | ***1.28 s*** | ***1.28 s*** | ***1.28 s*** | **2.52 s** |

The numbers are impressive, I must admit. They merged together for some reason, something somewhere does some form of batching I’d assume, and those three ended up in the same chunk.

However, if I increase the times for the `/api/sidebar` to 3 seconds and for `/api/messages` to 5 seconds, the picture of progressive rendering becomes visible. Although it will look exactly as Client-Side rendering for the users, just faster.

The performance profile, however, becomes hilarious:

![Chrome DevTools performance profile showing React Server Components](https://calendar.perfplanet.com/images/2025/nadia/server-components-performance-profile.png)

See that loooooong HTML bar in the Network section? That’s the server keeping the connection open while waiting for the data. Compare it with more “traditional” SSR:

![Chrome DevTools performance profile showing traditional SSR](https://calendar.perfplanet.com/images/2025/nadia/traditional-ssr-performance-profile.png)

HTML is done as soon as it’s done, no waiting.

## The Investigation Results

Okay, those numbers are pretty impressive, aren’t they? Server Components are clear winners in all categories except the no-interactivity gap.

|  | LCP (no cache) | Sidebar (no cache) | Messages (no cache) | No interactivity gap |
| --- | --- | --- | --- | --- |
| Client-Side Rendering | 4.1 s | 4.7 s | 5.1 s |  |
| Server-Side Rendering (Client Data Fetching) | **1.61 s** | 4.7 s | 5.1 s | 2.39 s |
| Next.js SSR (Client Data Fetching) | ***1.28 s*** | 4.4 s | 4.9 s | 2.52 s |
| Next.js SSR (Server Data Fetching) | 1.78 s | 1.78 s | 1.78 s | 2.52 s |
| Next.js App router (Server Fetching with Suspense) | ***1.28 s*** | ***1.28 s*** | ***1.28 s*** | **2.52 s** |

So, should you press everyone around you to move to Server Components?

Hard to say, to be honest. Yes, the initial load can be improved if Server Components are implemented correctly.

However!

You’ll only see performance benefits from Server Components if ***data fetching*** is involved. If you only need to render an interactive app, or you don’t really care about dynamic data, and LCP is your main concern, then you’ll have the same performance result as with the “traditional” SSR.

And moving to Server Components will come at a huge cost. Because you’d need to completely re-architect your entire app to fetch data in a new server-first way. Everything you knew will turn upside-down (once again). And more so, you’d need to implement it *the right way*. One mistake, and your performance might actually not improve at all, at best, or worsen at worst.

And it’s really, really, really easy to make a mistake there. Don’t forget, it’s still a very experimental bleeding-edge technology. There are no established best patterns there yet, minimal IDE support, and total vendor lock-in if you go all-in. Not to mention the [recent security vulnerability](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components) that blew the internet, at least in React-related circles.

Whether the potential performance improvements are worth it – up to you to decide, of course.

Related notes: [[Server Components]]
