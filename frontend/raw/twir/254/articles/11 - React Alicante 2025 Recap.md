---
type: twir-item
issue: 254
item: 11
item_type: item
date: 2025-10-15
source: https://kalabro.tech/react-alicante-2025/
tags:
  - "2025"
  - "Compiler"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-10-15-TWIR-254|Index]]

# Item 11: React Alicante 2025 Recap

Source: [https://kalabro.tech/react-alicante-2025/](https://kalabro.tech/react-alicante-2025/)

Summary:
The recap provides a detailed summary of talks from React Alicante 2025, covering topics like React Server Components, compilers, testing, accessibility, design systems, and AI in development. Highlights include practical demos, state management explorations, advanced UI patterns, and community discussions on the state of React. The summary also notes the growing importance of accessibility, local-first architectures, and collaboration between developers and designers.

Key takeaways:
- Diverse talks on React internals, RSC, compilers, testing, and accessibility.
- Emphasis on personal projects, local-first data, and AI-driven workflows.
- Notable sessions on advanced UI, type-safe design systems, and avoiding frontend anti-patterns.
- Community is adapting to new features and organizational changes (e.g., React Foundation).

Recommendation:
Read fully (read fully for conference insights or specific talk details)

Why it matters:
read fully for conference insights or specific talk details

Content:
# React Alicante 2025

October 13, 2025

On this page, you can find a full list of all [React Alicante 2025](https://reactalicante.es/) talks with my short comments. A longer opinionated summary at the end.

Enjoy and feel free to reuse it if you need a summary for your team or employer.

## Table Of Contents

## Sessions - Day 1

*16 high quality talks on React Server Components, Compilers, CSS and personal projects.*

### Building for You by Kadi Kraman

[**@kadikraman**](https://x.com/kadikraman)

Kadi, a software developer at Expo, set a theme for this year’s conference: personal side projects built out of curiosity and passion.
She touched on common obstacles like procrastination, scope creep, and goal setting when building something outside of work.

### Developing Waku and Exploring Client State with React Server Components by Daishi Kato

[**@dai\_shi**](https://x.com/dai_shi)

The author of Zustand and Jotai talks about [Waku](https://waku.gg/), the project he initially built to explore React Server Components but ended up
with a fully functional React framework that offers a minimalistic alternative to Next.js.
Daishi demystified the RSC API by breaking it down to serializing and deserializing components. As a state management guru, he went deeper and explored
how jotai may look like in RSC world. The result is [waku-jotai](https://github.com/wakujs/waku-jotai).

### Building Interactive Async UI with React 19 and Ariakit by Aurora Scharff

[**@aurorascharff**](https://x.com/aurorascharff)

Aurora took a real life example of a dropdown component with some data fetching logic and walked us through a series of refactorings
to make it more accessible, maintainable, and user friendly. The synergy between React, Ariakit and Tailwind made code much more compact and declarative.

### The 2025 State of React Testing by Daniel Afonso

[**@danieljcafonso**](https://x.com/danieljcafonso)

The past, present and future of frontend testing featuring Vitest Browser Mode, MSW, Playwright, and emerging AI tools.

### Compilers, User Interfaces & the Rest of Us by Matheus Albuquerque

[**@ythecombinator**](https://x.com/ythecombinator) ([slides](https://speakerdeck.com/ythecombinator/react-alicante-2025))

Typical frontend work can feel distant from computer science theory, but many of the tools we use every day actually involve compilers.
The deck is packed with links to libraries, concepts and articles that I’m yet to explore. In the past, I would be overwhelmed by this talk,
but with AI I feel I can easily dig couple layers deeper if I need to.

### React Beyond the DOM by Erik Rasmussen

[**@erikras**](https://x.com/erikras)

The talk started as a typical overview of React internals but suddenly turned into a fascinating live demo that blew everyone’s mind 💡

### Legacy Starts Tomorrow: Surviving the Refactoring Loop by Paulina Chojnowska

[**@AntariaPaulina**](https://x.com/AntariaPaulina)

A much needed reminder that we should never stop refactoring despite it’s rarely immediately profitable. Advice from Paulina is as obvious as
“sleep well and brush your teeth” and yet it has to be said: refactor all the time, plan for it, own the code.

### Feature Flags 101: Transforming Your Development with a Simple Switch by Luis Oliveira

[**@\_luisFilipePT**](https://x.com/_luisFilipePT)

Feature flags allow us to control behavior without deploy. Luis clarifies use cases for environment variables vs feature flags and shares
some common patterns like “Kill Switch”.

### Building component libraries with designers, not for them by Przemek Krupiński

[**@pppemo**](https://github.com/pppemo)

Przemek is a regular React Alicante attendee who came back this year with a lighting talk on collaborating with designers. He focused
on the importance of building shared language, trust and cross-functional transparency.

### Local first is the new black by Miquel Company

[**@solilokiam**](https://github.com/solilokiam)

Miquel builds a cool personal project, The Pyrenees Challenge event for motorcycle enthusiasts. He shared his local-first journey starting with
DIY Zustand+Yjs, continuing with Tinybase and its performance issues, and eventually settling on [jazz tools](https://jazz.tools/).

### Level up your React knowledge with vibe coding by Heather Thacker

[**@hhthacker**](https://x.com/hhthacker)

A lightning talk on how AI can be used to learn React.

### How I used AI Workflows with Figma & Playwright MCPs to accelerate my development time by Aris Markogiannakis

[**@arismarko**](https://x.com/arismarko) ([slides](https://www.canva.com/design/DAFqwlKyZ5o/fMvjcBAcd1dZp0F73Lzhbg/edit))

MCPs made a lot of noise when they were first introduced, but it’s not always clear how they can be used in our day to day work.
Aris shared some examples from his own workflows.

### Scaling a React Application from 0 to a Brazilian users by Dan Neciu

[**@neciudan**](https://x.com/neciudan)

Dan shared a brief story of co-founding CareerOS and surviving its early days. Some technical tips include starting component
library early and bringing wrappers for all 3rd party libraries.

### My CSS is Faster Than Your React! Writing CSS only React Search! by Evyatar Alush

[**@evyataral**](https://x.com/evyataral)

Evyatar blew everyone’s mind by building a fully functioning search with just CSS. In fact it was used in his library [emoji-picker-react](https://github.com/ealush/emoji-picker-react) ([code](https://github.com/ealush/emoji-picker-react/blob/6c27ae29cb95b628cc86246b54f4cb6d410d7661/src/components/header/Search/CssSearch.tsx)) before he replaced it with vistualization.

### Reacting to Surprises: Creating Engaging Hidden Features by Courtney Yatteau

[**@c\_yatteau**](https://x.com/c_yatteau)

Courtney shared a few examples of easter eggs in apps that can make user experience more engaging.

### Nearly Familiar: Can Web Developers Relate to Genealogy? by Kevin Maes

[**@kvmaes**](https://x.com/kvmaes)

Kevin wrapped up the first day with an insanely well-built personal project for exploring genealogical data, his longtime hobby.
While we learned a lot about genealogy and visualization pipelines, the main takeaway for us was to reconnect with our inner creativity.
It can be very satisfying and educational to build something for fun.

## Sessions - Day 2

*Another 16 talks on React 19.2, animations, and of course AI!*

### The State of React and the Community in 2025 by Mark Erikson

[**@acemarke**](https://x.com/acemarke) ([slides](https://blog.isquaredsoftware.com/presentations/2025-06-state-react-community/))

Mark acknowledged the complicated state of React community caused by the weird and intense Vercel’s push for React Server Components.
Several years later, the community is still recovering. Just a few days after this talk, React introduced the [React Foundation](https://react.dev/blog/2025/10/07/introducing-the-react-foundation).

### The Suspense Continues: ViewTransition and Activity by Chance Strickland

[**@chancethedev**](https://x.com/chancethedev)

Just a few days before React Alicante, React 19.2 was released and Chance gave us a live demo of the new features.

### The Beachcomber’s Guide to Type-Safe Design Systems by Kathleen McMahon

[**@resource11**](https://x.com/resource11)

Kathleen covered several important topics, such as the polymorphic component smell (`<Button as="a" /> 💩`), the semantics of `interface` vs `type` in component libraries, and the power of typed design systems. She also led an accessibility workshop at the conference and shared with me that overall awareness of a11y is growing!

### Unleashing the Magic of JavaScript Generators by Mattia Manzati

[**@mattiamanzati**](https://x.com/mattiamanzati) ([slides](https://github.com/mattiamanzati/magic-of-js-generators))

Generators have been around longer than async/await and yet most of us without Python background don’t quite understand them.
“Generators are iterators *and* iterables that provide pull-based data flow” - Mattia unpacked this for us starting small and ending up
with its own UI rendering engine powered by generators.

Surprisingly, there is not much educational content on the topic. The most relevant I found is [Algebraic Effects in JavaScript](https://fnayre.github.io/2018-11-19-algebraic-effects-series-1/) series by Redux Saga author.

### The Dark Side of UI – Avoiding Common Frontend Anti-Patterns by Bree Hall

[**@bytesofbree**](https://x.com/bytesofbree)

Bree walked us through a few poorly written React components and offered better approaches, featuring libraries like TanStack Query
and TanStack Vistualization.

### Navigating the hype driven world of AI development without going crazy by Kitze

[**@thekitze**](https://x.com/thekitze)

Super fun talk ridiculing the hype around AI as well as our FOMO around it.
For Kitze, coding is a form of procrastination. He doesn’t allow himself to write code manually and instead forces himself to always use AI. The [“Managers have been vibe coding forever”](https://x.com/PR0GRAMMERHUM0R/status/1974625610124148844) slide immediately went viral

### Zen and the art of code maintenance by Beth Swingler

[**@bethylogism**](https://x.com/bethylogism)

Using Zen as analogy, Beth highlighted some common code maintenance problems. Bonus points for mentioning the [Tidy First?](https://kalabro.tech/tidy-first/) book! 😻

### Fun with emails by Daniel Mocan

[**@danielsmocan**](https://x.com/danielsmocan)

Daniel gave us a quick intro to [React Email](https://react.email/), a great library to dramatically simplify email templating.

### End-to-end testing: the hard parts by Kate Marshalkina

[**@kalabro**](https://x.com/kalabro)

I gave a shorter version of my [“Playwright testing at scale”](https://www.youtube.com/watch?v=OYZNTPp04hw) talk focusing on the hard parts.
More on my speaker experience at the end of the post.

### Deploying an app with Docker by Forbes Lindesay

[**@ForbesLindesay**](https://x.com/ForbesLindesay)

A friendly intro to Docker for frontend developers who want to deploy their apps outside Vercel.

### Boosting React Native Performance with React Compiler: A Sneak Peek into the Future by Ilda Neta

[**@ildaneta**](https://github.com/ildaneta)

Ilda demonstrated how React Compiler can be used in a React Native project. I didn’t know about `"use no memo"` directive to opt out of automatic memoization.

### Make development easier with your own browser extensions by Łukasz Nowak

[**@LukaszNowakPL**](https://github.com/LukaszNowakPL)

Łukasz wanted to build a helper extension for himself and his teammates but it turned out to be tricker than expected. He faced several challenges
such as embedding React, communicating with the main page, and debugging.

### Audio recording and playback complexity across browsers by Vinu Vijy Nair

[**@vinu-phoenix**](https://github.com/vinu-phoenix)

Vinu shared how he attempted to build a new audio feature for ManyChat fully in the browser, what challenges he faced and
of course what he learned.

### The Missing Middle Ground: Fast & Real Testing for React Native by Łukasz Chludziński

[**@lukasz\_app**](https://x.com/lukasz_app)

Another testing talk, this time in React Native space. Łukasz demoed a new library [`react-native-harness`](https://www.npmjs.com/package/react-native-harness) that allows testing native capabilities while keeping tests fast and developer friendly.

### Running WebAssembly in React Native Applications by Shivay Lamba

[**@HowDevelop**](https://x.com/HowDevelop)

WebAssembly is not super common in React Native due to the differences between web and mobile platforms. Apparently, there are some interesting
use cases and solutions in this space.

### Practical guide to animation in React by Kateryna Porshnieva

[**@krambertech**](https://x.com/krambertech)

This year Kateryna demystified animations for the rest of us. Very visual and practical talk covering everything from basics
to spring physics.

## My summary

It was my third (!) React Alicante conference in a row and the fourth (!) React conference this year. I’ll be honest, I was not sure I would enjoy it that much, given that I had already heard from many of the speakers earlier this year.

Turns out, I had no reason to worry. After visiting so many conferences, React Alicante is still one of my favorites:

1. I prefer single-track conferences with a larger audience - it feels more engaging.
2. I love the packed agenda, with 32 talks plus optional workshops.
3. The average talk quality is high, with some lightning talks outperforming full talks.
4. Tickets are cheaper than most other conferences.
5. The organization is always very smooth. For a regular attendee, everything just works, while behind the scenes the organizers work hard to fix all the random issues.
6. A very special location creates vacation vibes.
7. The lovely community spirit and super friendly atmosphere ❤️

### Speaker experience

Delivering the same talk at multiple conferences is efficient but boring.

For React Alicante, I decided to rework my material into something new.
I love the time constraint that a lightning talk imposes - it requires me to be laser-focused on what’s important. Last year, I gave a deck-free inspirational [speech on mentorship](https://www.youtube.com/watch?v=bZoji7jCSU8). This year, I decided to go technical and even included a short live coding demo. I had a lot of fun, and I hope the attendees enjoyed it as well!

### Popular topics

This year’s agenda was very well balanced. AI topics were carefully kept under control, and I really appreciated it.

React remained at the center of attention, complemented by a mix of evergreen frontend topics like testing, design, and refactoring.
I was a bit surprised by the lack of TanStack deep dives, especially given the recent TanStack Start v1 RC release. To compensate, I read [“An Interactive Guide to TanStack DB”](https://frontendatscale.com/blog/tanstack-db/) on my flight back.

### Videos

All sessions were recorded and will be available on YouTube. While waiting, checkout React Conf 2025 recordings ([day 1](https://www.youtube.com/watch?v=zyVRg2QR6LA), [day 2](https://www.youtube.com/watch?v=p9OcztRyDl0)).

Related notes: [[Server Components]]
