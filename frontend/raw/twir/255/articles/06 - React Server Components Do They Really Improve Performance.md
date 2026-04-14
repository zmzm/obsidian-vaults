---
type: twir-item
issue: 255
item: 6
item_type: item
date: 2025-10-22
source: https://www.developerway.com/posts/react-server-components-performance
tags:
  - "RSC"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-10-22-TWIR-255|Index]]

# Item 6: React Server Components: Do They Really Improve Performance?

Source: [https://www.developerway.com/posts/react-server-components-performance](https://www.developerway.com/posts/react-server-components-performance)

Summary:
This article provides a practical, measurement-driven comparison of Client-Side Rendering (CSR), Server-Side Rendering (SSR), and React Server Components (RSC), focusing on real-world performance impacts. The author builds a semi-realistic app and benchmarks various rendering/data-fetching techniques, analyzing metrics like LCP, "sidebar visible," and "messages visible" under controlled network conditions. The goal is to clarify the actual benefits and trade-offs of RSC versus traditional approaches.

Key takeaways:
- RSC is often misunderstood; the article demystifies it with hands-on experiments and clear metrics.
- Performance is measured for initial load, dynamic data, and interactivity, comparing CSR, SSR, and RSC.
- The article provides reproducible steps and code for independent verification.
- Useful for teams evaluating RSC adoption or seeking concrete performance data.

Recommendation:
Read fully (especially for architects and teams considering RSC migration or performance optimization)

Why it matters:
especially for architects and teams considering RSC migration or performance optimization

Content:
# React Server Components: Do They Really Improve Performance?

Have you heard of [React Server Components](https://react.dev/reference/rsc/server-components)? You probably have. It's everything anyone talks about in the React community in the last few years. It's also the most misunderstood concept I feel.

To be totally honest with you, I didn't get their point for a while either. It's way too conceptual for my practical mind. Plus, we could fetch data on the server with Next.js and APIs like [getServerSideProps](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props) waaay before any Server Components were introduced. So what's the difference?

Only when I compared how all those patterns differ from an implementation point of view, how data is fetched across different rendering techniques, and when I traced the performance impact of each of them in different variations, it finally clicked.

So this is exactly what this article does. It looks into how Client-Side Rendering, Server-Side Rendering, and React Server Components are implemented, how JavaScript and data travel through the network for each of them, and the performance implications of migrating from CSR (Client-Side Rendering) to SSR (Server-Side Rendering) to RSC (React Server Components).

I implemented a semi-real multi-page app to measure all of this, so this will be fun! It's available on GitHub in case you want to replicate the experiments yourself.

I'm going to assume you've at least heard of Initial Load, Client-Side Rendering, Server-Side Rendering, the Chrome Performance tab, and how to read it. If you need a refresher, I have a few articles I recommend reading first, in this order:

1. [Initial load performance for React developers: investigative deep dive](https://www.developerway.com/posts/initial-load-performance)
2. [Client-Side Rendering in Flame Graphs](https://www.developerway.com/posts/client-side-rendering-flame-graph)
3. [SSR Deep Dive for React Developers](https://www.developerway.com/posts/ssr-deep-dive-for-react-developers)

## Introducing the Project To Measure

Let's say I want to implement an interactive and beautiful website. One of the pages on that website looks like this:

![](/assets/react-server-components-performance/inbox-full.png)

Some data on that page is dynamic and is fetched via REST endpoints. Namely, items in the Sidebar on the left are fetched via the `/api/sidebar` endpoint, and the list of messages on the right is fetched via the `/api/messages` endpoint.

The `/api/sidebar` endpoint is quite fast, taking **100ms** to execute. The `/api/messages` endpoint, however, takes **1s**: someone forgot to optimize the backend here. Those numbers are somewhat realistic for projects on the older and larger side, I'd say.

If you want to follow along with the article and verify the measurements on your own, the project is [available on GitHub](https://github.com/developerway/react-server-components). Clone the repo, install the dependencies, and follow the "how to reproduce" steps at the end of each section.

## Defining What We Are Measuring

When it comes to performance, there are a million and one things you can be measuring. It's impossible to say "this website has good or bad performance" without defining what exactly we mean by "performance", "good", and "bad".

For this particular experiment, I want to see the difference in *loading performance* between different rendering and data fetching techniques, including React Server Components. For the purpose of understanding them all, and also answering the question: "React Server Components: are they worth it from a performance perspective?"

I'm going to use the **Performance** tab of Chrome DevTools for measurements. With **CPU 6x slowdown** and **Network: Slow 4G**. In case you're not particularly familiar with some of them, I did an overview of the parts we're going to use today in the [Initial load performance for React developers: investigative deep dive](https://www.developerway.com/posts/initial-load-performance) article.

I'm interested in both first-time visitors, when JavaScript is downloaded for the first time, and in repeated visitors, when JavaScript is usually served from the browser cache.

I'm going to measure:

1. **[Largest Contentful Paint](https://developer.mozilla.org/en-US/docs/Glossary/Largest_contentful_paint) (LCP) value**, which happens to correspond to the time the user sees the page rendered with "skeletons" for the sidebar and messages.
2. **"Sidebar items visible"** time, which is pretty self-explanatory: when the sidebar items are fetched from the endpoint and rendered on the page.
3. **"Messages visible"** time, same as above, only for the messages.
4. **"Page interactive"** time, the time when the toggle in the header starts working (you'll see the importance of this one later).

![](/assets/react-server-components-performance/measurements.png)

I'll take each measurement a few times and use the median to eliminate outliers.

![](/assets/react-server-components-performance/http1-vs-http2.png)

In production, however, those files will likely be served via a CDN, and all of them are HTTP/2 or HTTP/3 these days. In this case, all the JavaScript files will be downloaded in parallel. So when testing locally, I want to imitate the CDN behavior for consistency. I did this via a reverse proxy with [Caddy](https://caddyserver.com/docs/), but any similar tool would do.

Okay, now that we're all set up, let's start playing with code.

## Measuring Client-Side Rendering

First, let's measure how Client-Side Rendering performs. Depending on the year you were born, Client-Side Rendering might be your default React or even default Web experience. If you're on old Webpack, or Vite + any router, and haven't implemented SSR (Server-Side Rendering) explicitly, you're on CSR (Client-Side Rendering).

From an implementation point of view, it means that when your browser requests the `/inbox` URL, the server responds with the HTML that looks like this:

```
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
```

You'll have `script` and `link` elements in the `head` tag and the empty `div` in the `body`. That's it. If you disable JavaScript in your browser, you'll see an empty page, as you'd expect from an empty div.

To transform this empty `div` into a beautiful page, the browser needs to download and execute the JavaScript file(s). The file(s) will contain everything you write as a React developer:

```
```
export default function App() {

return (

<SomeLayout>

<Sidebar />

<MainContent />

</SomeLayout>

);

}
```
```

Plus something like this:

```
```
const DOMElements = renderToDOM(<App />);

const root = document.getElementById('root');

root.appendChild(DOMElements);
```
```

React itself transforms the entry-point `App` component into DOM nodes. Then it finds that empty div by its `id`. And injects the generated elements into the empty div.

The entire interface is suddenly visible.

If you record Performance for the Initial Load, the picture will be something like this:

![](/assets/react-server-components-performance/client-side-rendering-schema.png)

While the JavaScript is downloading, the user still stares at the empty screen. Only after everything is downloaded AND JavaScript is compiled and executed by the browser does the UI become visible, the LCP metric is recorded, and side effects like fetch requests are triggered.

In real life, it will be much messier, of course. There will be multiple JavaScript files, sometimes chained, CSS files, a bunch of other stuff happening in the Main section, etc. If you record the actual profile of this project, it should look like this:

![](/assets/react-server-components-performance/client-side-rendering-real.png)

Data fetching for the sidebar and message items is triggered inside JavaScript:

```
```
useEffect(() => {

const fetchMessages = async () => {

const response = await fetch('/api/messages');

const data = await response.json();

};

fetchMessages();

}, []);
```
```

It could be any data-fetching framework, like [Tanstack Query](https://tanstack.com/query/latest), for example. In this case, the code will look like this:

```
```
const { isPending, error, data } = useQuery({

queryKey: ['messages'],

queryFn: () =>

fetch('/api/messages').then((res) => res.json()),

});
```
```

But it doesn't really matter. What's important here is that for the data fetching process to trigger, JavaScript needs to be downloaded, compiled, and executed.

The Initial Load numbers with no JavaScript cached look like this:

4.1 seconds wait to see *anything* on the screen! Whoever thought it was a good idea to render anything on the client??

Aside from everything related to dev experience and learning curve (which are huge deals by themselves), there are two main benefits compared to more "traditional" websites.

First, performance actually! Transitions between pages when everything is on the client and there is no back-and-forth with the server can be incredibly fast. In the case of this project, navigating from the Inbox page to Settings takes just **80ms**. It's as close to instantaneous as it can get.

And second, it's cheap. Ridiculously cheap. You can implement a really complicated, highly interactive, rich experience, upload it to something like Cloudflare CDN, have millions of monthly users, and still stay on the free plan. It's perfect for hobby projects, student projects, or anything with a large potential audience where money is a significant factor.

Plus, no servers, no maintenance, no CPU or memory monitoring, no scalability issues as a nice bonus. What's not to love?

Also, those > 4-second loading times are not as terrible as they look. It only happens the very first time the user visits your app. Granted, in something like a landing page, that's unacceptable. But for SaaS, where you'd expect users to visit the website often, the 4 seconds will happen only once (per deploy). Then the JavaScript is downloaded and cached by the browser, and the second and following load numbers will be significantly reduced.

800ms is much better, isn't it?

The final number I'm interested in today is when the Toggle becomes interactive. In this case, since everything shows up only when JavaScript is executed, it will match the LCP time. So the full table will look like this:

**Steps to reproduce the experiment**:

1. Clone the [repo](https://github.com/developerway/react-server-components), install all dependencies with `npm install`.
2. Start the backend API: `npm run start --workspace=backend-api`
3. Build the frontend: `npm run build --workspace=client-fetch-frontend`
4. Start the frontend: `npm run start --workspace=client-fetch-frontend`
5. Start reverse proxy for HTTP/2: `caddy reverse-proxy --to :3000`
6. Open the website at https://localhost/inbox
7. Measure!

## Measuring Server-Side Rendering (No Data Fetching)

The fact that we have to stare at the blank page for so long started to annoy people at some point. Even if it was for the first time only. Plus, for SEO purposes, it wasn't the best solution. Plus, the internet was slower, and the devices were not the latest MacBooks.

So people started scratching their heads to come up with a solution. While still staying within the React world, which was just way too convenient to give up.

We know that the entire React app at the very end looks like this:

```
```
const DOMElements = renderToDOM(<App />);
```
```

But what if instead of DOM nodes, React could produce the HTML of the app instead?

```
```
const HTMLString = renderToString(<App />);
```
```

Like the actual string that the server can then send to the browser instead of the empty div?

```
```
<div class="...">

<div class="...">...</div>

...

</div>
```
```

In theory, our extremely simple server for Client-Side Rendering:

```
```
export const serveStatic = async (c) => {

const html = fs.readFileSync('index.html').toString();

return c.body(html, 200);

};
```
```

Can continue to be just as simple. It just needs one additional step: find-and-replace a string in the `html` variable.

```
```
export const serveStatic = async (c) => {

const html = fs.readFileSync('index.html').toString();

const HTMLString = renderToString(<App />);

const htmlWithSSR = html.replace(

'<div id="root"></div>',

HTMLString,

);

return c.body(htmlWithSSR, 200);

};
```
```

Now the entire UI is visible right at the beginning without waiting for any JavaScript.

Welcome to the Server-Side Rendering (SSR) and Static-Site Generation (SSG) era of React. Because [renderToString](https://react.dev/reference/react-dom/server/renderToString) is actually a real API supported by React. This is literally the core implementation behind some React SSG/SSR frameworks.

If I do exactly this for my Client-Side Rendered project, it will be a Server-Side Rendered project. The performance profile will shift slightly. The LCP number will move to the left, right after the HTML and CSS are downloaded, since the entire HTML is sent in the initial server response, and everything is visible right away.

![](/assets/react-server-components-performance/server-side-rendering.png)

A few important things here.

First, as you can see, the LCP number (when the page "Skeleton" is visible) should drastically improve (we'll measure it in a bit).

However, we still need to download, compile, and execute the same JavaScript in exactly the same way. Because the page is supposed to be interactive, i.e., all those dropdowns, filters, and sorting algorithms we implemented should work. And while we wait, the entire page is already visible!

That gap between the page being already visible, but we're still waiting for JavaScript download to make it interactive, is the time when the page will appear ***broken*** for users. This is why I wanted to measure the "page becomes interactive" time. Because during that time, the nice Toggle in the header won't work.

Also, only the LCP mark has moved in that picture. The "Sidebar items" and "Messages" are in exactly the same places, structurally speaking. This is because we haven't changed the code a bit and are still fetching that data on the client! Somewhere deep in the React code, we still have something like this:

```
```
const Sidebar = () => {

useEffect(() => {

const fetchSidebarData = async () => {

const response = await fetch('/api/sidebar');

const data = await response.json();

setSidebarData(data);

};

fetchSidebarData();

}, []);

};
```
```

`useEffect` is an asynchronous side-effect. It will be triggered only when the app is properly mounted in the browser. Which will happen only when the browser downloads and processes JavaScript, and client-side React kicks in. `renderToString` will just skip it as irrelevant.

As a result, the fact that we have the page pre-rendered on the server has exactly zero effect on the time when the Sidebar items or table data show up!

If I finally measure what's happening instead of theoretical discussions, I'll see these numbers:

As you can see, the LCP value on initial load indeed radically dropped: from **4.1s to 1.61s**! Exactly as in the theoretical schematic.

However, the time when the Toggle became interactive remained the same, exactly as in the schematics. So the experience is almost **broken for more than 2 seconds** on initial load!

That "no interactivity" gap, along with the cost of running a server, is the price you'll pay for LCP improvements when transitioning from Client-Side Rendering to Server-Side Rendering. There is no way to get rid of it. We can only minimize it by reducing the amount of JavaScript users have to download during the first run.

**Steps to reproduce the experiment**:

1. Exactly the same steps as for Client-Side Rendering, plus:
2. Go to `src/frontend/client-fetch/server/index.ts` and uncomment `return c.html(simpleSSR(c, html));` line.

## Measuring Server-Side Rendering (With Data Fetching)

"No interactivity" gap aside, there is another somewhat problematic area in the previous experiment. The fact that there were no changes in the Sidebar and Messages appearances. But since we're in the server realm already, why can't we extract that data here? It surely will be faster. At the very least, latency and bandwidth will likely be much better.

The answer: we absolutely can! It would require much more work implementation-wise, though, compared to the simple pre-rendering we did. First, the server. We need to fetch that data there:

```
```
export const serveStatic = async (c) => {

  const html = fs.readFileSync("index.html").toString();

 

 

  const sidebarPromise = fetch(`/api/sidebar`).then((res) => res.json());

const messagesPromise = fetch(`/api/messages`).then((res) => res.json());

const [sidebar, messages] = await Promise.all([

sidebarPromise,

messagesPromise,

]);

...

};
```
```

Then we need to pass that data to React somehow so it can render the items when the rest of the UI is rendered. Luckily, since essentially the `App` component is nothing more than a function, it accepts arguments like any other JavaScript function. We know them as props. Yep, we need to pass good old props to the `App` when we're doing `renderToString`!

```
```
export const serveStatic = async (c) => {

const html = fs.readFileSync('index.html').toString();

const sidebarPromise = fetch(`/api/sidebar`).then((res) =>

res.json(),

);

const messagesPromise = fetch(`/api/messages`).then(

(res) => res.json(),

);

const [sidebar, messages] = await Promise.all([

sidebarPromise,

messagesPromise,

]);

const HTMLString = renderToString(

<App messages={messages} sidebar={sidebar} />,

);

};
```
```

Then our `App` component needs to be modified to accept props and pass them around with the regular prop drilling technique:

```
```
export default function App({ sidebar, messages }) {

return (

<SomeLayout>

<Sidebar data={sidebar} />

<MainContent data={messages} />

</SomeLayout>

);

}
```
```

In theory, this could already work. In practice, we need to handle a few more things here. First, "hydration". In SSR land, the "hydration" refers to React reusing the existing HTML sent from the server to attach event listeners.

For hydration to work properly, the HTML coming from the server should be *exactly the same* as on the client. Which is impossible, since the client doesn't have that fetched data yet. Only the server does. Which means we need to pass the data from the server to the client somehow at the same time we send the HTML so it's available during React initialization.

The easiest way to do that is to embed it into the HTML as a script tag and attach it as an object to `window`:

```
```
const htmlWithData = `

<script>window.__SSR_DATA__ = ${JSON.stringify({

sidebar,

messages,

})}</script>

${HTMLString}`;
```
```

Now on the frontend, it will be available as `window.__SSR_DATA__.sidebar` that we can read and pass around:

```
```
export default function App({ messages, sidebar }) {

const sidebarData =

typeof window === 'undefined'

? sidebar

: window.__SSR_DATA__?.sidebar;

const messagesData =

typeof window === 'undefined'

? messages

: window.__SSR_DATA__?.messages;

return (

<SomeLayout>

<Sidebar data={sidebarData} />

<MainContent data={messagesData} />

</SomeLayout>

);

}
```
```

And this actually works! The performance structure will change again:

![](/assets/react-server-components-performance/server-side-rendering-with-data.png)

Now the entire page, including previously dynamic items, will be visible as soon as CSS finishes downloading. Then we'll still have to wait for the exact same JavaScript as before, and only after that will the page become interactive.

The numbers now look like this:

The LCP value, unfortunately, degraded. This is no surprise. It's because we now have to wait for data-fetching promises to resolve themselves before we can proceed with pre-rendering of the React part.

```
```
export const serveStatic = async (c) => {

 

  const sidebarPromise = fetch(`/api/sidebar`).then((res) => res.json());

const statisticsPromise = fetch(`/api/statistics`).then((res) => res.json());

const [sidebar, statistics] = await Promise.all([

sidebarPromise,

statisticsPromise,

]);

...

};
```
```

And we really must wait for them since we need that data to start rendering anything.

Sidebar and Messages items, however, appear much faster now: **2.16 seconds instead of 5.1 seconds**. So it could be called an improvement if the LCP number is not that important to you compared to the full-page view. Or, we could prefetch only the Sidebar, by the way, with minimal regression (this endpoint is pretty fast), and keep the Messages part on the client. That will be a product decision based on your understanding of what's best for the users.

**Steps to reproduce the experiment**:

1. Exactly the same steps as for Client-Side Rendering, plus:
2. Go to `src/frontend/client-fetch/server/index.ts` and uncomment `simpleSSRWithHydration(c, html)` line.

## Measuring Next.js Pages ("Old" Next.js)

In reality, the code in the previous section is, of course, going to be much more complicated. First, it's a multi-page application. Most pages won't need the list of messages. Plus, we'd need to pre-render each page individually: showing HTML for the main page when the user loads the `/login` URL wouldn't make much sense.

So we need to introduce some form of routing on the server now. And at the very least create different entry points for each page.

Basically, we started inventing our own SSR framework. So there is no harm in switching to something existing now. For example, let's use Next.js Pages Router, the "old" Next.js experience. The one without React Server Components. We'll transition to the version with Server Components in the next section.

To migrate my custom SSR implementation to the Next.js Pages Router, I just need to move the fetching logic into [getServerSideProps](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props). Which is the old Next.js API to fetch page data on the server. Everything else, including props drilling, stays the same! Next.js just abstracts away the `renderToString` call and the find-and-replace logic that we did for the manual implementation.

This is how the code will look now if I want to fetch the data on the server:

```
```
export const getServerSideProps = async () => {

const sidebarPromise = fetch(`/api/sidebar`).then((res) =>

res.json(),

);

const messagesPromise = fetch(`/api/messages`).then(

(res) => res.json(),

);

const [sidebar, messages] = await Promise.all([

sidebarPromise,

messagesPromise,

]);

return { props: { messages, sidebar } };

};
```
```

Or I can just comment it out to keep client-side data fetching.

Everything else stays the same, including the performance profile. It should maintain the same structure as the SSR sections above, with and without data fetching.

Recording, writing down, and here's the result:

As you can see, the LCP value for initial load is even slightly *worse* than my custom implementation for the "Server Data Fetching" use case. Sidebar and Messages, on the other hand, show up a second earlier in this use case. In the "Server Data Fetching" use case, the LCP/Sidebar/Messages numbers are identical between my custom solution and Next.js. But the "no interactivity" gap is a full second shorter in Next.js.

This is a very visible use case of what will happen when code splitting is performed differently. Next.js splits JavaScript into many more chunks than my custom solution. As a result, when I measure initial load, many more parallel JavaScript files "steal" a bit of bandwidth from the CSS, resulting in the CSS download taking longer and the LCP value slightly degrading.

On the other hand, having many JavaScript files in parallel take a second faster to download overall, resulting in a much better time when the page becomes interactive, and, as a result, a much shorter "no interactivity" gap.

**Steps to reproduce the experiment**:

1. Clone the [repo](https://github.com/developerway/react-server-components), install all dependencies with `npm install`.
2. Start the backend API: `npm run start --workspace=backend-api`
3. Go to `frontend/utils/link.tsx`, uncomment Next.js link and comment out the custom implementation
4. Go to `src/frontend/next-pages/pages/inbox.tsx` and comment/uncomment `getServerSideProps` for toggling between data fetching use cases
5. Build the frontend: `npm run build --workspace=next-pages`
6. Start the frontend: `npm run start --workspace=next-pages`
7. Start reverse proxy for HTTP2/3: `caddy reverse-proxy --to :3000`
8. Open the website at https://localhost/inbox

## Introducing React Server Components

Okay, so to recap the previous section: fetching and pre-rendering on the server can be really good for the initial load performance numbers. There are, however, a few issues with it still.

The biggest issue with SSR is the "no interactivity" gap: when the page is already visible but the JavaScript is still downloading/initializing. The only way to shorten it is to reduce the amount of JavaScript necessary for interactivity. We already did some code splitting when we migrated to Next.js Pages and saw a whole second improvement in this area. Can we do more here, besides code splitting? Do we even need all that JavaScript?

The second issue with SSR is data fetching. Currently, if I want to pre-fetch messages on the server, thus reducing the wait time for messages to appear, it will negatively affect both the initial load and the time when the sidebar items show up.

This is due to the fact that server rendering is currently a synchronous process. We wait for all the data first, then pass that data to `renderToString`, then send the result to the client.

![](/assets/react-server-components-performance/current-ssr-structure.png)

But what if our server could be smarter? Those fetch requests are promises, async functions. Technically, we don't *need* to wait for them to start doing something else. What if we could:

1. Trigger those fetch promises without waiting for them.
2. Start rendering React stuff that doesn't need that data, and if it's ready, send it to the client immediately.
3. When the Sidebar promise is resolved and its data is available, render the Sidebar portion, inject it into the server page, and send it to the client.
4. Do the same for the Messages.

Basically, replicate the exact same structure of data fetching that we have in Client-Side Rendering, but *on the server*.

![](/assets/react-server-components-performance/server-components-structure.png)

In theory, if this is possible, it could be crazy fast. We'd be able to serve the initial rendered page with placeholders at the speed of the simplest SSR, and still be able to see Sidebar and Messages items way *before* any JavaScript is downloaded and executed.

React would need to abandon the simple synchronous `renderToString` for this, rewrite the rendering process to be in chunks, make those chunks injectable into the rendered structure somehow, and be able to serve those chunks independently to the client.

That's quite a task! And it's done already, since it describes the combination of React Server Components and Streaming working in harmony.

To understand how all of this fits and works together, we need to understand three main concepts.

### React Server Components

First of all, the React Server Components themselves.

A typical React component quite often just lays out HTML tags on a page. For example, the Sidebar component in this project looks like this:

```
```
export const TopbarForSidebarContentLayout = () => {

return (

<div className="lg:bg-blinkNeutral50 lg:dark:bg-blinkNeutral800">

<nav

aria-label="Main Navigation"

className="h-auto lg:h-16 px-6 flex items-center justify-between absolute top-3 lg:top-0 right-0 lg:right-0 left-12 lg:left-0 lg:relative"

>

<div className="text-3xl blink-text-primary italic font-blink-title">

<a href="#">My Dashboards</a>

</div>

<div className="gap-3 hidden lg:flex">

... // the rest of the code
```
```

As you can see, just a bunch of divs and links. However, all of this is still JavaScript, and exactly this code is included in all the JavaScript files that contribute to the "no interactivity" gap. But there is no interactivity here! The only thing from this component that we actually need is the divs, links, and other tags. The layout in its HTML form.

The only reason this code is included in the JavaScript bundle is because React needs it to construct the Virtual DOM: a hierarchical representation of everything that is rendered on the page.

Every time you "render" a component in React like this `<TopbarForSidebarContentLayout />`, you're creating an Element. Underneath this nice HTML-like syntax is just an object with a bunch of properties, one of which is "type". The "type" can be either a `string`, and then it represents a DOM element. Or a function - and in this case, React will call that function, extract the bunch of elements it returns, and merge them together into the unified tree.

```
```
{

"type": "div",

"props": {

"children": [

{

"type": "nav",

"props": {

"className": "...",

...

}

}

]

}

}
```
```

In the current SSR implementation, whether it's Next.js pages or my custom hacky solution, the process of extracting this tree from the React components happens twice. The first time is when we do the pre-rendering on the server. And the second time, completely from scratch, when we initialize the client-side React.

But what if we didn't have to? What if, when we first generated that tree on

... (content truncated)

Related notes: [[Server Components]]
