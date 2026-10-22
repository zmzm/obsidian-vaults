---
type: twir-item
issue: 299
item: 9
item_type: item
date: 2026-09-30
source: https://tannerlinsley.com/posts/ai-open-source-and-the-long-road-to-tanstack-charts
tags:
  - "TanStack"
status: auto
quality: keep
---

[[2026-09-30-TWIR-299|Index]]

# Item 9: AI, Open Source, and the Long Road to TanStack Charts

Source: [https://tannerlinsley.com/posts/ai-open-source-and-the-long-road-to-tanstack-charts](https://tannerlinsley.com/posts/ai-open-source-and-the-long-road-to-tanstack-charts)

Summary:
Tanner Linsley shares the journey of building charting libraries, culminating in TanStack Charts, and reflects on the evolving role of AI in open source. He describes how AI accelerated prototyping and implementation, but emphasizes that domain experience, API design, and open source knowledge remain crucial. The post also discusses the importance of leveraging existing libraries and the value of open source expertise in an AI-assisted world.

Key takeaways:
- AI can dramatically accelerate library development, but experience and design sense are still essential.
- Open source libraries encapsulate years of hard-won lessons; AI is a tool, not a replacement for expertise.
- The right abstractions and APIs matter more than raw implementation speed.
- Choosing and integrating the right libraries remains a key developer skill.

Recommendation:
Read fully (read fully for personal insights on AI and open source, or if interested in the history of charting libraries)

Why it matters:
read fully for personal insights on AI and open source, or if interested in the history of charting libraries

Content:
# AI, Open Source, and the Long Road to TanStack Charts

I went for a run and opened a Twitter Space. About 71 minutes later, I'd talked through my history with charting libraries, how I'm using AI, what that means for open source, and why I'm having so much fun building right now. I also spent most of the run wondering why nobody wanted to talk to me. Turns out I couldn't hear anybody. Thanks to Kevin for helping rescue that part of the evening.

[Listen to the full Space, TanStack Run](https://x.com/i/spaces/1rxmqpnNjNNxy), or [read the timestamped transcript](/transcripts/tanstack-run-2026-09-24.txt).

This is an edited recap of the conversation. The transcript is automatically generated and may contain mistakes, especially in names and overlapping speech. Library status and plans below reflect the day we recorded, September 24, 2026.

## I still love building things

I understand why AI is uncomfortable for people who have spent their careers getting good at programming. I was fast at writing code, and a lot of my identity was tied up in that. I worried that handing over more of the implementation would take away something I liked about myself.

But I've always been making things. Music, video, design, software. Looking back at all of that, getting an idea out of my head and into something other people could use was a huge part of what I loved. Programming was how I did it for a long time, and I associated the fulfillment with the act of writing the code because that was required.

Now I can iterate on an idea without wearing myself out on every little piece of implementation, and I'm having a lot of fun. That doesn't mean every use of AI is good. We see low quality issues and pull requests in open source, and AI makes it easier to produce more of them. The behavior behind those contributions existed before AI, too. Giving someone a much more powerful tool doesn't automatically give them better judgment about how to use it.

I joked about AI being a 50-foot lightsaber. You can do a lot with it, and you can also make a pretty big mess. I'm getting more confident about where I can use it well. Charts is probably the best example of that for me so far.

## The years before TanStack Charts

My interest in charts goes back to building Nozzle. We had all this marketing and SEO data, and we needed useful ways to explore it. I spent time with D3 and the ecosystem around it, then got involved with Chart.js. When its original creator, Nick, was ready to hand more of it over, Everett Timberg and I got access to help maintain it.

I worked on Chart.js 2.0, including animation and tweening work, and learned a lot. One thing I learned was that I really didn't want to keep writing directly against the Canvas API for everything I wanted to build.

Then React changed how I thought about UI. I wanted that declarative approach for charts, so I built react-charts. React handled rendering, D3 helped with calculations and layout, and I tried to make the common cases feel automatic. Give it your data, get a useful chart. I was also pretty surprised that the react-charts package name was still available.

There is a lot hiding inside âautomatic,â though. Margins, labels, rotated text, geometry, all the little decisions that make a chart look reasonable without asking the user to position everything by hand. I spent a lot of time on that work. We used react-charts at Nozzle for a long time, but eventually I wanted more freedom to combine chart types and work with different kinds of data and layouts.

I kept studying. D3's source, the Grammar of Graphics, other charting libraries. Observable Plot, from Mike Bostock and the people working on it, really clicked for me. The way it mapped data into visual representations changed how I thought about the API I wanted. I used it for roughly three years and accumulated wrappers around the things I needed for my own applications.

Those wrappers weren't an indictment of Plot. Libraries have priorities and contexts, and mine weren't always the same. But I was building up a pretty specific list of things I liked, things I wanted to work differently, and things I wished one library could bring together.

## A couple of hours to a first version

When I finally tried building TanStack Charts with AI, I wasn't starting with an empty idea. I had years of opinions about the API, the data model, the rendering, and the things that had been painful in earlier libraries. I had also been thinking about how agents would approach data and use the library, alongside the humans using it.

I got a first working version in a couple of hours. In less than a week, I had an experimental alpha. I built it without writing a line of code myself, and it was one of the most fun experiences I've had building a library.

That first version wasn't the end of the work. I had a direction for the architecture, including a scene graph and reactivity, and there was a lot of iteration around the API and how types flowed through it. Type safety is something you have to think about from the beginning. It doesn't just fall out of whatever implementation you happen to get first.

I worked on documentation, API references, migration guides, tests, and optimization. Friends tried migrating by asking their agents to use the new library. The early feedback I got was encouraging: more flexibility, smaller bundles, and faster charts in their applications. Those were early experiences with an alpha, and there was still plenty to polish.

I also had the agent walk me through the architecture. I'd given it react-charts as context, and I recognized ideas and patterns from my earlier work. Seeing those ideas come together with the things I'd learned since then was pretty satisfying.

There are mixed feelings in here, too. Access to more tokens and more money can affect what you can get done. But the old process had costs as well. I spent more than a year on react-charts. I'm happy to spend money to get some of that implementation time back, especially when it means I can focus on the API and the experience people actually have using the library.

I don't want to be sitting at my laptop all night thinking about chart geometry. I have a family, and there are other things I want to do with my life. I can care a lot about this library and still want to spend less of my life manually implementing every part of it.

## Open source still carries the experience

I wouldn't take this experience with Charts and decide to rewrite every TanStack library with AI. Router, Start, Table, and Form have complexities, especially around types, where the models still need help. Charts happened to be a project where what I wanted to build lined up well with what the tools could do.

And Charts owes a lot to the work that came before it. D3, the Grammar of Graphics, Observable Plot, Chart.js, Everett, Nick, and all the experience I got using and maintaining those tools. Bringing those ideas forward into something new doesn't erase where they came from.

That's part of why I still care so much about open source in a world where an agent can generate an implementation for you. A library carries the lessons from people who have spent years dealing with a problem. I don't want everybody's agent to start over with a fresh pile of SVG and math and rediscover every one of those lessons.

I gave another example from a project I was building with Codex. I could see that the caching and real-time behavior needed something different, so I pointed it toward TanStack DB. I could also see where we were going to need virtualization, so I pointed it toward TanStack Virtual. The agent could read the skills and do the implementation, but recognizing the problem and knowing what to reach for still mattered.

Sometimes knowing the name of the right library feels like knowing a magic word. You tell the agent what to use and a problem you've been fighting starts to go away. There's a lot of experience behind choosing that word.

## The questions at the end

Once I could finally hear everyone, we got into Three.js, Hotkeys, code review, and how far I want to take automation.

On Three.js, I think it's foundational at this point. It works well with a lot of other tools, and I've been impressed by what people are making with it and AI. I pointed people to the little game on [TanStack's explore page](https://tanstack.com/explore), which came out of me playing around with those tools. We also briefly entertained the idea of building and launching something during a half marathon, until I remembered I probably wouldn't have service.

Kevin talked about his work on TanStack Pacer and Hotkeys. I said I'd been dropping Hotkeys into my projects and asking the agent to use it whenever a keyboard shortcut made sense. Kevin had a useful counterpoint: he'd seen agents wrap Hotkeys in lots of unnecessary code to recreate behavior it already supported. At the time, it didn't have its TanStack Intent skills set up yet, and he was also working through an internal refactor and API changes. Getting an agent to install the right library is only part of using it well.

Someone asked about our code review process. It depends on the project. A lot of our open source libraries still have very hands-on human review, with AI helping along the way. Security-sensitive areas get extra scrutiny from maintainers, and release, CI, and publishing infrastructure are tightly controlled. These libraries are used by a lot of people, and that responsibility matters.

I'm much faster and looser with changes to tanstack.com, where we can fix things quickly and roll back. Even there, something like a database migration deserves more care. The consequences of a change affect how I want to review it.

I'm interested in having agents continually check the website, catch problems, and help fix them. I'm still very much in the loop, though. I want to understand the process before handing more of it over, and I'm not excited about letting an automated system decide what we should build next while I just approve more scope.

With Charts, I'm already leaning heavily on tests, integration and browser testing, and bundle budgets. I can approve a feature, describe the API I want, and ask the agent to implement it without breaking existing behavior or growing the bundle. If it comes back and says it needed more code, I want to understand why. Those conversations are part of the work now.

I also mentioned that we were focusing on getting more of the TanStack ecosystem stable, including a planned Start 1.0 release. We had a date in mind, but I didn't announce it in the Space. There are other libraries moving toward their next release stages, too, and I'm excited about what's coming.

By the end of the conversation, I was feeling pretty good about all of this. I still get to decide what I want to make, think hard about how it should work, and see those ideas become useful to other people. That's a part of building software I don't want to give up, and right now I get to do more of it.

## Find a part of the recording

- **02:48**: Running, building with voice, and getting the conversation started.
- **05:22**: AI, programming, and the things I enjoy about creating.
- **15:02**: Nozzle, Chart.js, react-charts, and the history behind Charts.
- **25:19**: Building TanStack Charts with AI, types, iteration, and tradeoffs.
- **37:30**: Knowing when to reach for an existing library.
- **45:48**: Where AI fits, and what's coming for TanStack.
- **49:09**: Discovering the audio problem and rescuing the Q&A.
- **53:39**: Three.js and the TanStack explore page.
- **59:29**: Kevin on Pacer, Hotkeys, and how agents use libraries.
- **1:02:07**: Human review, security, website changes, and automation.
- **1:08:11**: Tests, bundle budgets, and implementing Charts features.
