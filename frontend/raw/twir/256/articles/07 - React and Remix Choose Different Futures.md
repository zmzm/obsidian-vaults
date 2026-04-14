---
type: twir-item
issue: 256
item: 7
item_type: item
date: 2025-10-29
source: https://laconicwit.com/react-and-remix-choose-different-futures/
tags:
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-10-29-TWIR-256|Index]]

# Item 7: React and Remix Choose Different Futures

Source: [https://laconicwit.com/react-and-remix-choose-different-futures/](https://laconicwit.com/react-and-remix-choose-different-futures/)

Summary:
This essay analyzes the philosophical divergence between React and Remix, as highlighted by recent conferences and product announcements. React is doubling down on complexity-as-capability, introducing advanced features like the compiler and server components to optimize user experience, while Remix 3 is breaking away to prioritize simplicity, explicitness, and alignment with the Web Platform. The split results in incompatible mental models and a lack of upgrade path from Remix 2 to 3, reflecting fundamentally different values: React embraces complexity for stability and power, while Remix seeks simplicity even at the cost of backward compatibility.

Key takeaways:
- React's roadmap emphasizes stability, composability, and capability, accepting complexity to benefit end users.
- Remix 3 prioritizes simplicity, explicit control, and Web Platform alignment, even breaking compatibility with prior versions.
- The frameworks now embody incompatible philosophies, with Remix 3 moving away from React's event and reactivity models.
- The split is driven by values, not just technical differences, and signals a new era of framework differentiation.

Recommendation:
Read fully (for those interested in framework philosophy, migration planning, or the future of React/Remix)

Why it matters:
for those interested in framework philosophy, migration planning, or the future of React/Remix

Content:
# React and Remix Choose Different Futures

Bryan Cantrill's talk [Platform as a Reflection of Values](https://www.youtube.com/watch?v=Xhx970_JKX4&ref=laconicwit.com) gave me a lens I didn't know I needed. When platforms diverge, he argued, it's rarely about technical merit. It's about values misalignment. The things that matter most to one community simply rank differently for another.

I attended [Remix Jam](https://www.youtube.com/watch?v=xt_iEOn2a6Y&ref=laconicwit.com) two weeks ago, then spent this past week watching [React Conf 2025](https://www.youtube.com/watch?v=zyVRg2QR6LA&ref=laconicwit.com) videos. I have spent the last decade shipping production code on React and the last two years on Remix.

Now both ecosystems are shifting, and what seemed like different approaches has become incompatible visions.

React Conf's technical announcements were incremental: React 19.2 APIs, View Transitions experiments, the compiler getting more sophisticated. The message was clear: React is listening to the community while accepting complexity on your behalf. Stability, Composability, Capability: those are the values.

The Remix team announced something else entirely: they're breaking with React. The mental model shifts introduced by `use client` and the implementation complexity of Server Components forced a choice. And Remix 3 chose Simplicity. Remix 2 users pay the price; there's no upgrade path.

That choice, to sacrifice Stability for Simplicity, makes explicit what was already true: these values cannot coexist.

## React's Values: Complexity as Capability

React's stated goal is to "raise the bar for responsive user experience." At React Conf 2025, the team demonstrated what that means in practice. They will accept tremendous complexity on developers' behalf if it delivers better experiences for end users.

The React Compiler is the clearest example. It analyzes your code, breaks components into smaller pieces of logic, and automatically optimizes rendering. In Meta's Quest store app, they saw 12% faster load times and interactions that were twice as fast, even though the app was already hand-optimized. The compiler isn't replacing developer skill; it's handling complexity that would be unrealistic to maintain manually. Joe Savona explained the challenge: in context-based apps where "every component has to update" the compiler now skips most of that work automatically.

This is React's value proposition: **Stability** (the compiler works with existing code), **Composability** (it integrates with concurrent rendering, Suspense, transitions), and **Capability** (it unlocks performance that manual optimization can't reach). When the team talked about their multi-year exploration into incremental computation, they weren't apologizing for the complexity. They were explaining the price of raising that bar.

The React team knows this makes React complicated. But the bet is clear: React falls on the sword of complexity so developers don't have to. That’s admirable, but it asks developers to trust React's invisible machinery more than ever.

## Remix's Counter-Values: Simplicity as Liberation

The Remix team remembers when React was only a composable rendering library with few primitives. At Remix Jam, Ryan Florence demonstrated what Simplicity looks like when it becomes your organizing principle: explicit over implicit, traceable over automatic.

The clearest example is `this.update()`. When Ryan built a live drum machine on stage, every state change was manual: "In this code, the only time anything updates is because I told it to." No automatic reactivity graph, no hidden subscriptions, no debugging why something re-renders unexpectedly. If you're wondering why a component updated, "it's because you told it to somewhere."

This explicitness extends throughout Remix 3's design. Event handling uses the `on` property with native DOM events that bubble through normal DOM. AbortControllers (`this.signal`) wire cleanup explicitly. Context doesn't trigger re-renders. You set it, components read it, and you call `this.update()` when you want things to change.

After demonstrating the drum machine, Ryan explained the philosophy: "We've been chasing this idea that you construct things together, change values, and everything does what it's supposed to do. But my experience is getting it set up is difficult, and once it is set up, suddenly when something unexpected happens, you have to unravel it."

When Michael Jackson demonstrated server rendering with the `<Frame>` component, he showed how it uses plain HTML as its wire format. React Server Components solve real problems, but Remix believes it can solve them more simply by leaning on the Web Platform.

This is Remix's value proposition: **Simplicity** (explicitly control when things update), **Web Platform Alignment** (standard events, standard streams, cross-runtime compatibility), and **Debuggability** (trace every update back to a specific `this.update()` call). The team isn't rejecting React's goal of raising the UX bar, but they are rejecting the complexity tax React accepts to achieve it.

## The Web Platform: Inevitable or Chosen?

There's an irony in using Cantrill's framework to analyze Remix's break from React: the Remix team doesn't see their Web Platform commitment as a values choice at all. They believe they're simply skating to where the puck is going. Every framework will embrace Web Platform APIs eventually. It is only a matter of timing.

But Cantrill's talk shows this is an explicit value choice, not an inevitable destination. He lamented Node.js choosing Approachability over Rigor, adopting Web Platform APIs to make it easier for browser developers to work with server-side JavaScript. The practitioners who brought those APIs to Node were the ones he felt were pushing out his values: robustness, debuggability, operational correctness. For Cantrill, aligning with the Web Platform meant sacrificing engineering rigor for developer convenience.

Remix 3 is building itself entirely on those same Web Platform APIs. [Streams](https://developer.mozilla.org/en-US/docs/Web/API/Streams_API?ref=laconicwit.com), [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API?ref=laconicwit.com), the [File](https://developer.mozilla.org/en-US/docs/Web/API/File?ref=laconicwit.com) API, every platform dependency behaves identically in browsers, Bun, Deno, and Node. Ryan and Michael demonstrated this throughout Remix Jam: standard HTML responses, native DOM events, cross-runtime compatibility. React respects Web Platform APIs too, but treats them as a foundation to build upon. Remix 3 treats them as the destination. This has always been a Remix value, evident in Remix 1 and 2, but Remix 3 makes it absolute.

And I love Remix for it.

I'm a huge fan of the open web, but I’m not convinced every server framework will, or should, fully align with the Web Platform. The browser and server live under different constraints that force different tradeoffs. The goal isn’t to erase the seam between them, but to make it visible and intentional. Remix 2 handles this tension elegantly. However, it's a result of taste in where to expose the platform, not an inherent outcome of aligning with it.

## Remix 2 is dead. Long live react-router!

Despite Remix having one of the [best upgrade policies in the industry](https://v2.remix.run/docs/guides/api-development-strategy?ref=laconicwit.com) with future flags, there will be no migration path from Remix 2 to Remix 3. The changes are just too fundamental. At Remix Jam, Michael Jackson was explicit: "We've been working on React Router for a decade now... A lot of people built on React Router. Shopify's built on React Router... We're not just going to abandon that thing." Remix 2 users get a maintained evolutionary path as [react-router](https://reactrouter.com/start/framework/installation?ref=laconicwit.com) v7. But Remix 3 is taking the name in the divorce and moving in a new direction.

When Simplicity becomes the organizing principle, Stability becomes negotiable. The new `on` property can't coexist with React's legacy event system. The explicit `this.update` API replaces React's hooks entirely. Breaking backward compatibility isn't collateral damage, it's the point. It opens design space for tricks like overloading `this` (giving components an optional second parameter without relying on argument ordering), which feels Simple because it leans into JavaScript's existing capabilities.

An alpha is expected by year’s end, with a cohesive package to follow in 2026. But the warning is clear: Remix 3 isn't ready for production anytime soon. Everything is new and subject to change. In the meantime, we have react-router.

## The Open Questions

Leaning on [events](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener?ref=laconicwit.com) as a communication backbone is clever, but it reminds me of complex Backbone.js apps that relied on a shared event bus to communicate across components. It worked for a time, but at a certain level of complexity, it became difficult for new developers to get up to speed on existing projects. Remix's explicitness and TypeScript support should help. But will it be enough to solve the challenges we couldn't in 2010?

`this.update()` makes for an easier mental model to grasp than React's hook system. But explicit rendering means more verbose code. [AbortControllers](https://developer.mozilla.org/en-US/docs/Web/API/AbortController?ref=laconicwit.com) require you to wire cleanup manually. The tradeoff is clear: you write more, but you understand more. Whether that's liberation or just shifted complexity depends on your team and your codebase.

The story of Remix 2 and react-router shows that Ryan and Michael are no strangers to pivoting toward what works. This is absolutely one of their strengths, but it's hard for large organizations to build on top of a shifting platform. How much will change before Remix 3 settles?

## Living in the Divergence

Cantrill ended his talk with a warning: "Elections do not resolve differences in value. You can have as many votes as you want. If you are not actually changing people's minds, changing their values, you are not actually resolving anything."

The react-router fork exists because the Remix team knows values don’t change overnight. It's a maintained path for those who need Remix 2's stability while Remix 3 proves itself. That split acknowledges reality: production software doesn't adopt new frameworks on vision alone. Teams will make different choices based on different values. Some will stick with React and embrace the compiler's sophistication. Some will jump to Remix 3 early, betting that Simplicity is worth the migration cost and the uncertainty.

Both paths are valid. But they're valid *for different values*. When frameworks explicitly reprioritize what matters most, teams can't avoid choosing. Not based on features or performance benchmarks, but on what kind of complexity they're willing to accept and what kind of control they need to maintain. That's not a technical decision. It's a values decision.

The React ecosystem now has two incompatible visions of its future. Cantrill's framework helps us see why that's okay, even if it's uncomfortable. Choose your values, then choose your tools.

Related notes: [[Server Components]]
