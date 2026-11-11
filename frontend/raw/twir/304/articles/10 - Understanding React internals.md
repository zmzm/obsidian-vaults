---
type: twir-item
issue: 304
item: 10
item_type: item
date: 2026-11-04
source: https://www.alexandretrotel.org/articles/understanding-react-internals
tags:
status: auto
quality: keep
---

[[2026-11-04-TWIR-304|Index]]

# Item 10: Understanding React internals

Source: [https://www.alexandretrotel.org/articles/understanding-react-internals](https://www.alexandretrotel.org/articles/understanding-react-internals)

Summary:
This article provides a deep dive into React's internal architecture, focusing on its scheduler, rendering process, lanes, server-client serialization, and hydration. It aims to demystify how React works beneath the surface, moving beyond hooks to the core mechanisms that drive updates and browser interaction.

Key takeaways:
- React is fundamentally a scheduler that manages rendering and prioritization.
- Covers async React, lanes, and the server-client data flow.
- Understanding internals helps develop better mental models and use React more effectively.
- Encourages reading React source code for deeper comprehension.

Recommendation:
Read fully (for developers seeking to master React's architecture and mental models)

Why it matters:
for developers seeking to master React's architecture and mental models

Content:
# Understanding React internals

Most people learn React through hooks. `useState`, `useEffect`, `useMemo`, and a list of rules to follow without really knowing why.

But hereâs the thing, React is not about hooks. Hooks are only the surface, the part you touch. So forget about them for now.

Underneath, React is a scheduler. It decides what to render, when to render it, and what can wait. It talks to the browser, splits work into small pieces, and pauses when something more important comes in.

This article is a deep dive into that part. Weâll go through async React, lanes, how React serializes components over the network between the server and the client, hydration, and all the things that usually stay hidden.

I wonât lie to you, some of it is hard to understand. So Iâll take the time to explain everything as simply as I can.

And itâs okay not to understand it all at once. I didnât either. Read it, come back later, and read it again.

Basically, this is the summary of what Iâve learned over these last years, using React every day and reading the source code of the [React repository](https://github.com/react/react).

If at any point you need to look at the source code, I really, REALLY encourage you to do it. Itâs the only and best way to understand how React works. Everything else, including this article, is someoneâs interpretation of it.

After reading this, you should understand React well enough to master it. Youâll know when to use each hook, and more importantly, why. Or, as [@infinterenders](https://x.com/infinterenders) would say, youâll become elite.

For me, it changed the way I use React. Especially the mental models between the server and the client, and how React interacts with the browser.

So, letâs get started.
