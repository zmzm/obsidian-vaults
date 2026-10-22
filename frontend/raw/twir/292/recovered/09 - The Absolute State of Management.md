---
type: "twir-recovery"
issue: 292
item: 9
source: "https://infrequently.org/2026/07/state-management/"
final_url: "https://infrequently.org/2026/07/state-management/"
retrieved: "2026-10-22T11:29:59+00:00"
original_note: "frontend/raw/twir/292/articles/09 - The Absolute State of Management.md"
editorial_review: "pending"
truncated: false
---

Original intake note: [[../articles/09 - The Absolute State of Management|The Absolute State of Management]]

# The Absolute State of Management

It is by no means the gravest linguistic crime of the React epoch, but *"state management"* grates like nails on chalkboard. A Socratic dialogue I keep having about it goes something like this:

> *me:* This UI is far too heavyweight for what it does, have you considered not using React?
>
> *them:* But how will we do state management without React?
>
> *me:* What do you mean? `<alternatives>` are reactive.
>
> *them:* React manages state in our app.
>
> *me:* It does? Then what are `<various_libraries>` for?
>
> *them:* Oh, those manage state.
>
> *me:* [](/2026/07/state-management/mal-speechless.mp4)

The libraries that trigger this *"Who's on First?"* routine include:

- [MobX,](https://mobx.js.org/) which promises *"simple, scalable state management."*
- [Satchel,](https://github.com/microsoft/satcheljs) apparently, *"is characterized by exposing an observable state that makes view updates painless and efficient"*
- [Recoil,](https://recoiljs.org/) billed as *"a state management library for React"*
- [Jotai,](https://jotai.org/) which pledges *"primitive and flexible state management for React"*
- [XState,](https://xstate.js.org/) [a](https://stately.ai/docs/xstate) *"state management and orchestration solution for JavaScript and TypeScript apps"*
- [Apollo,](https://www.apollographql.com/) [promising](https://www.apollographql.com/docs/react) *"a comprehensive GraphQL state management library for JavaScript"*
- [Redux,](https://redux.js.org) [tagline:](https://web.archive.org/web/20160528035759/http://redux.js.org/) *"a predictable state container for JavaScript apps."*
- [TanStack Store,](https://tanstack.com/store/latest) *"a framework-agnostic state primitive for immutable updates"*
- [Zustand,](https://github.com/pmndrs/zustand) described as the *"🐻 bear necessities for state management in React"*

Contrasts sharp enough to cut softened butter.

Suffice it to say, the ecosystem has not picked a winner. Indeed, I regularly see several of these libraries on a single page. But even one would seem too many, given that we're adding a second *"state management"* system to a framework that [spills considerable documentation ink chest-beating about its state management facilities.](https://react.dev/learn/managing-state)

One of the following must be true:

- **React *is* a state management system** and someone has smuggled in a duplicative dependency we can jettison.
- **React is an *inadequate* state management system** and we should stop trusting it with an ill-defined subset of the *"state management"* problem.
- **React *is not* a state management system** and we should stop pretending otherwise.

But in the to-and-fro of consulting engineering one can't just say as much, for fear of offence against [frameworkist articles of faith.](/2024/11/if-not-react-then-what/)

Thankfully, this is a blog post, so we can cut to the chase and admit that *none of these tools manage state.*

True state management wrestles with the time dimension, but React-centric *"state management"* libraries handle time the way C++ does for multithreaded code — which is to say, it's left as an exercise to the reader.

Systems without a built-in conception of time and ordering are *subject* to temporal effects. They can even synthesise compound state out of unordered, un-timestamped updates. But they occupy a world of hopes and dreams when it comes to asserting affirmative management of state because **managing state means correctly applying changes over time and resolving conflicts.**

A large fraction of the problems from overgrown React and Redux attempts at *"state management"* spring from the same wellstone: updates to the state propagation systems come from a variety of sources, with varying frequency and specificity. Pure propagation systems crumble under the incidental complexity that results from trying to sort out the consequences with only an event bus abstraction. It becomes unclear whose job it is to sort out which updates are "correct", and optimistic UI updates become a liability — or at least a bun fight.

At bottom, this is the same problem as managing data across multiple machines, and managing data over the network is the same as managing it across time that spans from the past, to the current moment, as well as the future.

This insight is important because it allows us to consider what's currently in memory vs. the same app rebooted at some future point without losing our minds. A future local instance of an app is conceptually the same as the app booting on an entirely different computer. Getting crisp on this is the key to throwing out jejune notions of *"state management"* and replacing them with tools that are fit for purpose.

Systems that *manage* state — rather than merely propagating or filtering it — have built-in concepts of time and order, and this allows them to handle both offline state and online real-time collaboration naturally. Instead of hoping that everything is happening in some window that we can squint at and call "now," true managers of state mutations have a way to reorder and resolve conflicts, and through that coherence, build a reliable and high-performance view of data changes over time.

You can distinguish them from state propagation tools by looking for variations of [vector clocks](https://en.wikipedia.org/wiki/Vector_clock) in their internals. Time and order metadata attached to mutation enables global ordering, and we can't truly manage state without it.

This conceptual break also provides an answer to our fish-or-fowl question: none of those libraries actually manage state; React included.

Now that we can more accurately describe what these systems do (and don't do), the phrase *"state management"* mostly reads as confusion. But hold on to some grace; the folks deploying jumbled terminology come by it honestly.

Systems that *really* manage application state are not yet popular, and most teams are not familiar with the algorithms and systems that do it credibly. Discussions of [CRDTs,](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type) [Operational Transforms,](https://en.wikipedia.org/wiki/Operational_transformation) [Prolly Trees,](https://www.dolthub.com/docs/architecture/storage-engine/prolly-tree/) and related approaches to consistency are still rare in the frontend discourse.

Thankfully the gap from upgrading our understanding of theory to deploying better patterns is small. Practical implementations are readily available; each have strengths and weaknesses depending on use-case, but all manage data in a time-aware way:

- [Y.js](https://yjs.dev/): CRDTs meet text editing. Thanks to breakthroughs in data structure performance, a full CRDT approach is dramatically more practical than it was just a few years ago.
- [Zero](https://zero.rocicorp.dev/): the successor to [Replicache,](https://replicache.dev/) Zero targets live collaboration in addition to data sync. [OSS'd or hosted,](https://zero.rocicorp.dev/docs/open-source) it's what I'd start with on a new project today.
- [Fluid](https://fluidframework.com/): Microsoft's in-house, OSS'd sync and collaboration system that [takes cues from OT.](https://fluidframework.com/docs/concepts/tob)

A beautiful, generative outcome of these systems is that because they think about time and conflicts, they're perfect for building systems that gracefully handle both edges of "now", enabling real-time collaboration seamlessly while simultaneously lighting up [offline-first styles of development.](https://offlinefirst.org/) Some (e.g., Y.js and Replicache) go far enough in this direction to enable true local-first development.

Regardless of which mechanism you adopt, these systems are a sea change. Data models stop being amalgamated hopium, and both offline use and realtime collaboration become possible as a side effect of getting the ordering of data mutation application correct.

This is the future we can have today. All we need to do is admit that *"state management"* isn't, then decide to do something about it.
