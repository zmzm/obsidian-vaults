---
type: twir-item
issue: 261
item: 13
item_type: item
date: 2025-12-03
source: https://adactio.com/journal/22265
tags:
status: auto
quality: keep
---

[[2025-12-03-TWIR-261|Index]]

# Item 13: Why use React?

Source: [https://adactio.com/journal/22265](https://adactio.com/journal/22265)

Summary:
This opinion piece questions the default use of React for web development, arguing that inertia and enterprise mandates often drive adoption more than user experience. The author suggests React’s strengths are best leveraged on the server, and encourages minimizing client-side React in favor of native browser capabilities or lighter alternatives like Preact.

Key takeaways:
- React is often chosen due to team familiarity and hiring, not always user needs.
- Client-side React imposes a performance cost on users.
- Server-side rendering (SSR) can mitigate some drawbacks, but tools like Next.js often default to client-side hydration.
- Developers should consider vanilla JS or lighter frameworks for the client.

Recommendation:
Read fully (read fully for broader context or if considering SSR strategies)

Why it matters:
read fully for broader context or if considering SSR strategies

Content:
# Journal-Why use React?

This isn’t a rhetorical question. I genuinely want to know why developers choose to build websites using React.

There are many possible reasons. Alas, none of them relate directly to user experience, other than a trickle-down justification: happy productive developers will make better websites. Citation needed.

It’s also worth mentioning that some people don’t *choose* to use React, but its use is mandated by their workplace (like some other more recent technologies I could mention). By my definition, this makes React enterprise software in this situation. My definition of enterprise software is any software that you use but that you yourself didn’t choose.

### Inertia

By far the most common reason for choosing React today is inertia. If it’s what you’re comfortable with, you’d need a really compelling reason *not* to use it. That’s generally the reason behind usage mandates too. If we “standardise” on React, then it’ll make hiring more straightforward (though the reality isn’t quite so simple, as the React ecosystem has mutated and bifurcated over time).

And you know what? Inertia is a perfectly valid reason to choose a technology. If time is of the essence, and you know it’s going to take you time to learn a new technology, it makes sense to stick with what you know, even if it’s out of date. This isn’t just true of React, it’s true of any tech stack.

This would all be absolutely fine if React weren’t a framework that gets executed in browsers. Any client-side framework is a tax on the end user. They have to download, parse, and execute the framework in order for you to benefit.

But maybe React doesn’t need to run in the browser at all. That’s the promise of server-side rendering.

### The front end

There used to be a fairly clear distinction between front-end development and back-end development. The front end consisted of HTML, CSS, and client-side JavaScript. The back end was anything you wanted as long as it could spit out those bits of the front end: PHP, Ruby, Python, or even just a plain web server with static files.

Then it became possible to write JavaScript on the back end. Great! Now you didn’t need to context-switch when you were scripting for the client or the server. But this blessing also turned out to be a bit of a curse.

When you’re writing code for the back end, some things matter more than others. File size, for example, isn’t really a concern. Your code can get really long and it probably won’t slow down the execution. And if it does, you can always buy your way out of the problem by getting a more powerful server.

On the front end, your code should have different priorities. File size matters, especially with JavaScript. The code won’t be executed on your server. It’s executed on all sorts of devices on all sorts of networks running all sorts of browsers. If things get slow, you can’t buy your way out of the problem because you can’t buy every single one of your users a new device and a new network plan.

Now that JavaScript can run on the server as well as the client, it’s tempting to just treat the code the same. It’s the same language after all. But the context really matters. Some JavaScript that’s perfectly fine to run on the server can be a resource hog on the client.

And this is where it gets interesting with React. Because most of the things people like about React still apply on the back end.

### React developers

When React first appeared, it was touted as front-end tool. State management and a near-magical virtual DOM were the main selling points.

Over time, that’s changed. The claimed speed benefits of the virtual DOM turned out to be just plain false. That just left state management.

But by that time, the selling points had changed. The component-based architecture turned out to be really popular. Developers liked JSX. A lot. Once you got used to it, it was a neat way to encapsulate little bits of functionality into building blocks that can be combined in all sorts of ways.

For the longest time, I didn’t realise this had happened. I was still thinking of React as being a framework like jQuery. But React is a framework like Rails or Django. As a developer, it’s where you do all your work. Heck, it’s pretty much your identity.

But whereas Rails or Django run on the back end, React runs on the front end …except when it doesn’t.

JavaScript can run on the server, which means React can run on the server. It’s entirely possible to have your React cake and eat it. You can write all of your code in React without serving up a single line of React to your users.

That’s true in theory. The devil is in the tooling.

### Priorities

Next.js allows you to write in React and do server-side rendering. But it really, really wants to output React to the client as well.

By default, you get the dreaded hydration pattern—do all the computing on the server in JavaScript (yay!), serve up HTML straight away (yay! yay!) …and then serve up all the same JavaScript that’s on the server anyway (ya—wait, what?).

It’s possible to get Next.js to skip that last step, but it’s not easy. You’ll be battling it every step of the way.

[Astro](https://astro.build/) takes a very different approach. It will do everything it can to keep the client-side JavaScript to a minimum. Developers get to keep their beloved JSX authoring environment without penalising users.

Alas, the collective inertia of the “modern” development community is bound up in the React/Next/Vercel ecosystem. That’s a shame, because Astro shows us that it doesn’t have to be this way.

Switching away from using React on the front end doesn’t mean you have to switch away from using React on the back end.

### Why use React?

The titular question I asked is too broad and naïve. There are plenty of reasons to use React, just as there are plenty of reasons to use Wordpress, Eleventy, or any other technology that works on the back end. If it’s what you like or what you’re comfortable with, that’s reason enough.

All I really care about is the front end. I’m not going to pass judgment on anyone’s choice of server-side framework, as long as it doesn’t impact what you can do in the client. [Like Harry says](https://csswizardry.com/2025/01/build-for-the-web-build-on-the-web-build-with-the-web/):

> …if you’re going to use one, I shouldn’t be able to smell it.

Here’s the question I should be asking:

Why use React *in the browser*?

Because if the reason you’re using React is cultural—the whole team works in JSX, it makes hiring easier—then there’s probably no need to make your users download React.

If you’re making a single-page app, then …well, the first thing you should do is ask yourself if it really needs to be a single-page app. They should be the exception, not the default. But if you’re determined to make a single-page app, then I can see why state management becomes very important.

In that situation, try shipping [Preact](https://preactjs.com/) instead of React. As a developer, you’ll almost certainly notice no difference, but your users will appreciate the refreshing lack of bloat.

Mostly though, I’d encourage you to investigate [what you can do with vanilla JavaScript in the browser](https://gomakethings.com/a-lot-of-what-people-use-react-for-would-be-better-handled-with-vanilla-javascript/). I totally get why you’d want to hold on to React as an authoring environment, but [don’t let your framework limit what you can do on the front end](https://adactio.com/journal/22235). If you use React on the client, you’re not doing your users any favours.

You can continue to write in React. You can continue to use JSX. You can continue to hire React developers. But keep it on your machine. For your users, make the most of what web browsers can do.

Once you keep React on the server, then a whole world of possibilities opens up on the client. Web browsers have become incredibly powerful in what they offer you. Don’t let React-on-the-client hold you back.

And if you want to know more about what web browsers are capable of today, come to [Web Day Out](https://webdayout.com/) in Brighton on Thursday, 12th March 2026.
