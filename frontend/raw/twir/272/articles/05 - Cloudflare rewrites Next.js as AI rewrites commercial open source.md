---
type: twir-item
issue: 272
item: 5
item_type: item
date: 2026-03-11
source: https://newsletter.pragmaticengineer.com/p/the-pulse-cloudflare-rewrites-nextjs
tags:
  - "Nextjs"
status: auto
quality: keep
---

[[2026-03-11-TWIR-272|Index]]

# Item 5: Cloudflare rewrites Next.js as AI rewrites commercial open source

Source: [https://newsletter.pragmaticengineer.com/p/the-pulse-cloudflare-rewrites-nextjs](https://newsletter.pragmaticengineer.com/p/the-pulse-cloudflare-rewrites-nextjs)

Summary:
Cloudflare announced that a single engineer, aided by AI agents, rewrote most of Next.js in one week, producing ‘vinext’—a Vite-based, drop-in replacement for Next.js optimized for Cloudflare Workers. This move highlights how AI can disrupt commercial open source by enabling rapid replication and modification of complex frameworks. While vinext is not yet production-ready, the event raises questions about the defensibility of open source business models and the evolving role of proprietary build outputs.

Key takeaways:
- Cloudflare’s ‘vinext’ replaces Turbopack with Vite, standardizing build outputs for broader deployment.
- AI dramatically reduced development time and cost, challenging traditional engineering timelines.
- The approach exposes new risks for commercial open source projects, as AI can quickly replicate functionality.
- Defensive strategies may shift toward private test suites, closed source, or emphasizing support and infrastructure.

Recommendation:
Summary sufficient (read the full article for broader industry analysis and implications)

Why it matters:
read the full article for broader industry analysis and implications

Content:
# The Pulse: Cloudflare rewrites Next.js as AI rewrites commercial open source

---

Today’s issue of The Pulse focuses on a single event because it’s a significant one with major potential ripple effects. On Tuesday, Cloudflare shocked the dev world by announcing that they have rewritten [Next.js](http://next.js) in just one week, with a single developer who used only $1,100 in tokens:

*Cloudflare CTO Dane Knecht [on X](https://x.com/dok2001/status/2026386974580330830?s=20)*

There are several layers to dig into here:

1. **The Next.js ecosystem: a recap**. Close to half of React devs use Next.js, and the best place to deploy Next.js is on Vercel – partly thanks to its proprietary build output.
2. **What Cloudflare did with Next.js**. Replacing the build engine in Next.js with the more standard Vite one, allowing Next.js apps to be easily deployed on Cloudflare.
3. **AI brings the impossible within reach**. What would take years in engineering terms was executed in one week with some tokens.
4. **“AI slop” still an issue.** Contrary to Cloudflare’s claims, vinext is not production-ready, and will need plenty of cleanup and auditing to make it on par with Next.js.
5. **New attack vector on commercial open source?** AI makes it trivial to “piggyback” off any commercial open source project. That’s a massive problem for commercial open source startups.
6. **Defense or offense?** Making test suites private is one defense, and going closed source is another. Code is no longer a moat, but other things like support, community, and infrastructure could become more important.
7. **AI-world reality.** Tests are an efficient way to use AI agents, vendors will start deploying “migration agents” like Cloudflare, and more.

First, some background. [Next.js](https://nextjs.org/) is the most popular fullstack React framework and around half of all React devs use it, as per recent research such as the 2025 Stack Overflow developer survey. Next.js is an open source project, built and mostly maintained by Vercel, which is the preferred deployment target for Next.js applications for many reasons. One of them is that Next.js is ideal to deploy to Vercel because Next.js applications are built with Vercel’s Turbopack build tool. The output of a build is a proprietary format. As Netlify engineer Eduardo Bouças [writes](https://eduardoboucas.com/posts/2025-03-25-you-should-know-this-before-choosing-nextjs/):

> “The output of a Next.js build has a proprietary and undocumented format that is used in Vercel deployments to provision the infrastructure needed to power the application.
>
> This means that any hosting providers other than Vercel must build on top of undocumented APIs that can introduce unannounced breaking changes in minor or patch releases. (And they have)”.

Next.js is an interestingly built project, where everything is open source, and the best place to deploy a Next.js application is on Vercel, as it’s optimized to run undocumented build artifacts the most efficiently. This is a smart strategy from Vercel which competitors will dislike, as any hosting provider would prefer Next.js to produce a standard build format. To do this, the build engine, Turbopack, would need to be replaced with something more standard.

**Let’s talk about build tools for web development.** According to the [State of JS 2025 survey](https://2025.stateofjs.com/en-US/libraries/), the most popular in the web ecosystem are:

1. **[Vite](https://vite.dev/)**: the most popular choice for new projects due to its speed and developer experience. Uses projects like [esbuild](https://esbuild.github.io/) and [Rollup](https://rollupjs.org/) under the hood
2. **[Webpack](https://webpack.js.org/)**: a legacy tool that’s not very performant, but still widely deployed in older projects
3. **[Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)**: Created by Vercel and optimized for larger [Next.js](http://next.js) applications. Built in Rust and intended to be more performant
4. **[Bun](https://bun.com/)**: a relatively new, all-in-one runtime and bundler. Anthropic acquired the team [in December](https://newsletter.pragmaticengineer.com/i/180722007/anthropic-acquires-javascript-runtime-bun), and some Bun folks are now focused on improving Claude Code’s performance.

So, most of the web ecosystem uses Vite as a build tool; Next.js uses Turbopack, and the majority of React applications with a full-stack React framework use Next.js. Basically, most devs using Next.js are likely to use Vite as their build tool.

Here’s a naive idea: what if Next.js used Vite to generate build outputs? In that case, build outputs would be standardized and would run equally well on any cloud provider, as there would be nothing proprietary or undocumented to Vercel.

And this is what Cloudflare did: replace Turbopack with Vite and call the new package ‘vinext’:

*Cloudflare replaced the Turbopack build dependency with Vite to create vinext*

Buried midway in the announcement is how this project [is experimental](https://blog.cloudflare.com/vinext/#status-experimental) and not at all guaranteed to work okay: it’s a ‘use-at-own-risk’ project. Still, the mere fact of this development feels like an earthquake in the tech world because of *how* it was pulled off.

In a blog post announcing the project, Cloudflare claims only one engineer “rebuilt” the whole thing in a way that’s trivial to deploy to Cloudflare’s own infrastructure, and only cost $1,100 in tokens. From Cloudflare’s [statement](https://blog.cloudflare.com/vinext/):

> “Last week, one engineer and an AI model rebuilt the most popular front-end framework from scratch. The result, vinext (pronounced “vee-next”), is a drop-in replacement for Next.js, built on Vite, that deploys to Cloudflare Workers with a single command. In early benchmarks, it builds production apps up to 4x faster and produces client bundles up to 57% smaller. And we already have customers running it in production.
>
> The whole thing cost about $1,100 in tokens”.

What Cloudflare did:

- Took the Next.js public API
- Reimplemented behaviour using Vite
- Created build output whose behaviour matches the “original” Next.js implementation

After 10 years, the core of Next has around 194,000 lines of code (LOC)\*\*. Meanwhile, [vinext](https://github.com/cloudflare/vinext) is about 67,000 lines of code which suggests a much leaner implementation: for example, vinext does not need to support legacy Next APIs, and vinext currently supports 94% of the Next.js API (and it’s safe to assume they left complex edge cases in the remaining 6%).  
  
\*\* the Next.js repository is closer to 2M lines of code: 1M is bundled dependencies (eg React bundles, CSS build etc), tests are 308,000 LOC, Turbopack 311,000 LOC.

**Pre-AI, this reimplementation would have taken years of engineering time to complete.** Doing what Cloudflare did was always possible *in theory*, but never seemed practical. I mean, why have a team of engineers spend potentially years on generating a standardized build output for Next.js apps? Even if they did, the dev community would have doubts about whether Cloudflare would maintain the project.

This is the thing with forking or rewriting open source projects: a major value proposition for commercial open source is to know that they will be *maintained*. Vercel has proved it’s a reliable custodian of Next.js for the past 10 years. Without AI, it could be assumed that any new reimplementation would eventually run out of steam.

**Separately but relatedly, Cloudflare has now proved that the cost of rewriting** ***existing*** **software has become ~100x cheaper, thanks to AI, and this economy is likely to be the case for maintenance, too.** Considering how trivial it was to rebuild one of the more complex open source projects, this augers well for it being trivial and much cheaper to maintain in the future. Potentially, Cloudflare no longer needs to budget an engineering team only for maintenance, if a single engineer could maintain the project, part-time!

Cloudflare had a project measured in engineering years, and completed it in *one engineering week*! It just took a single engineer using [OpenCode](https://opencode.ai/) (open source coding agent), Opus 4.5, and a bunch of tokens, then: ‘*boom’*, *vinext* was born.

There are questions about the quality of vinext, though.Vercel, naturally, is unhappy and hit out at the obvious weakness that vinext is unfit for production usage because it’s insecure. Vercel CEO, Guillermo Rauch, did not miss a beat by tying Cloudflare’s effort to the “vibe coding” stereotype of sloppy work executed with a lack of understanding:

Guillermo has a point: anyone who stopped reading [Cloudflare’s launch announcement](https://blog.cloudflare.com/vinext/) after the first few sentences would assume it’s production-ready, with the first paragraph of this announcement closing with:

“And we already have customers running it in production.”

However, Cloudflare doesn’t [share](https://blog.cloudflare.com/vinext/#status-experimental) the rather crucial detail that “running in production” means that vinext has been deployed onto a beta site, until more than 1,000 words (around 2–3 pages) into the announcement:

> “We want to be clear: vinext is experimental. It’s not even one week old, and it has not yet been battle-tested with any meaningful traffic at scale. (...)
>
> We’ve been working with National Design Studio, a team that’s aiming to modernize every government interface, **on one of their beta sites**, CIO.gov.

Oh. So, “customers running it in production” at Cloudflare apparently means “customer running a beta site in production without meaningful traffic.” This is a first from the infrastructure giant, which usually prides itself on accurate statements!

This detail was also absent when Cloudflare’s CEO and CTO [were boosting](https://x.com/eastdakota/status/2026389179345916255?s=20) vinext like it was a mature, battle-tested product. In that context, Vercel’s raising of the issue of security vulnerabilities is more than fair game, in my view.

Still, all that doesn’t alter the core learning from this project: that AI has the power to drastically reduce engineering time by up to ~100x and deliver *usable-enough* output, for relatively negligible financial cost. *Just keep in mind that security and reliability issues will probably take plenty of extra time and effort to address.*

If arch-rivalries exist in tech, then Cloudflare and Vercel are a prime example. Both are gunning to become the most popular platform for developers to deploy their code, and the CEOs are regularly seen in public taking shots at the other side. One such spat happened [in March](https://newsletter.pragmaticengineer.com/i/160004343/ceos-scrap), as covered at the time:

> “Things kicked off on social media, with developers confused about the severity of the incident, and about why Next.js seemed silent, and also why Cloudflare sites were breaking due to its fix for the CVE causing its own issues. It was at that point that Cloudflare’s CEO, Matthew Prince, entered the chat to accuse Vercel of [not caring about security](https://x.com/rauchg/status/1903590962498326771):
>
> Given the security incident was ongoing, this felt a bit “below the belt” by the Cloudflare chief. Criticizing rivals is fair game, but why not wait until the incident is over? The punch landed, and Vercel’s CEO Guillermo Rauch is not someone to take it lying down, so he [hit back](https://x.com/rauchg/status/1903590962498326771).
>
> Cloudflare’s CEO then responded with a cartoon [implying](https://x.com/eastdakota/status/1903690805576909227) that although Vercel is much larger than its competitor Netlify, Cloudflare is 100x bigger than both, and could stomp them into the ground at will.”

Serving the public interest wasn’t why Cloudflare rewrote [Next.js](http://next.js): they did it because they want Next.js sites to be deployed onto Cloudflare, but doing so made little sense until now because Next.js produced bespoke build output optimized for Vercel’s infrastructure. With this change, Cloudflare [claims](https://blog.cloudflare.com/vinext/) it provides *superior* performance when hosting Next.js apps, according to their own measurements.

*I’d just add that performance is important for developers, but other things matter, too. Cost, reliability, developer experience, and how much devs like a company, are all factors in choosing between vendors. Also, performance measurements from a vendor about its own service must be taken with a large pinch of salt.*

**Zooming out from this episode, it seems that AI is bringing the value of existing commercial open source moats into question.** Vercel carved out a clever open source strategy that helped turn its open source investment into business revenue:

1. Build and maintain Next.js, delivering the best developer experience (DX).
2. Optimize Vercel to serve the specific (and undocumented) build output of Next.js.
3. Most developers onboarding to Next.js will decide to deploy on Vercel to get the most benefit, in terms of DX and performance.
4. … repeat for years while the business becomes worth billions! (Vercel was [valued](https://startupwired.com/2025/10/01/vercel-raises-300-million-reaches-9-3-billion-valuation/) at $9B last October).

Underpinning this success are some assumptions:

1. Next.js will remain the #1 choice for developers to build React applications, thanks to ongoing investment.
2. It is expensive to rewrite Next.js to be deployable and performant on another cloud vendor.
3. Even if someone did #2, developers would be skeptical and not switch over.

Vercel can invest in #1 to keep Next as best-in-class, while knowing that the risk of #2 occurring is minor. However, Cloudflare has now “cloned” Next, and can easily keep up with all changes in the future, and port them back to vinext.

**But AI makes it trivial to “piggyback” off any commercial open source project, which is a massive problem for commercial open source startups.** It puts all the effort and investment into building and maintaining [Next.js](http://next.js), while Cloudflare enjoys the benefit of this hard work (the Next.js public API) which is easily deployable to Cloudflare, and it can now undercut Vercel on price. For all future Next.js changes, Cloudflare will just sync it to vinext, using AI!

WordPress had [a similar problem](https://newsletter.pragmaticengineer.com/i/149770356/2-open-source-business-model-struggles-wordpress), with WP Engine “piggybacking” off its work and undercutting their pricing in 2024. As I analyzed at the time:

> “Free-riding on permissive open source is too tempting to pass on for other vendors. WP Engine uses a common loophole of contributing almost nothing in R&D to WordPress, while selling it as a managed service. This means that they could either easily undercut the pricing of larger players like Automattic which do spend on WordPress’s R&D. Alternatively, a company like WP Engine could charge as much, or more, as Automattic, but be able to spend a lot more on marketing, while being similarly profitable. “Saving” on R&D gives the “free-riders” plenty of options to grow their businesses: options not necessarily open to Automattic while they invest as much into R&D as they do.
>
> Commercial open source vendors pressure to end “freeriding”. Automattic is likely facing lower revenue growth, with customers choosing vendors like WP Engine which offer a similar service — getting these customers either via a cheaper price or thanks to more marketing spend. This legal fight could be an effort to force WP Engine to stop eating Automattic’s lunch, or perhaps get WP Engine to sell to Automattic, which would cement its leading status in managed Wordpress, while also boosting revenue by $400M a year – according to its own figures”.

Vercel managed to avoid the “free-riding” problem with [Next.js](http://next.js), but that’s no longer possible now that AI makes it trivial to rewrite.

How should commercial open source companies respond to the threat that a competitor can easily rewrite the software behind the managed solutions which they sell as services?

**One obvious response is to make tests private, so that replication is harder for AI.** One thing that made it so easy for Cloudflare to rewrite Next was the project’s comprehensive test suite. From [their announcement](https://blog.cloudflare.com/vinext/) (emphasis mine):

> “We also want to acknowledge the Next.js team. They’ve spent years building a framework that raised the bar for what React development could look like. **The fact that their** API surface is so well-documented and their **test suite so comprehensive** is a big part of what made this project possible.”

Database solution SQLite is famous for its incredible test suite. What some people don’t know is that while core [SQLite](https://sqlite.org/) tests are open source, its most comprehensive test suite – [TH3](https://sqlite.org/testing.html) – is closed source. SQLite monetizes its advanced infrastructure as a [service](https://sqlite.org/prosupport.html) for purchase. This is a fair tradeoff: for most contributors, the basic open source tests work well enough. For enterprise users or customers who really care about correctness, it makes sense to purchase advanced testing services from the service’s creator.

Open source canvas project, tldraw, [announced](https://github.com/tldraw/tldraw/issues/8082) it will relocate its test suite to a closed source repository; a move which makes plenty of sense. Here’s commentary from Simon Willison:

> “It’s become very apparent over the past few months that a comprehensive test suite is enough to build a completely fresh implementation of any open source library from scratch, potentially in a different language.”

In the event, tldraw’s announcement turned out [to be a joke](https://github.com/tldraw/tldraw/issues/8082#issuecomment-3964650501), but who’s laughing now? An open source project with excellent tests is an easy target for an AI agent to execute a full rewrite of it.

**Could new licenses be created for the AI era?** Existing open source licenses were created on the assumption that humans read open source code, and humans modify it. Agents break that assumption.

Could we see new license types emerge to ban AI agents from modifying projects’ source code? It seems pretty far-fetched and hard to implement, but not beyond the realms of possibility.

AI agents are still very new, and going mainstream in tech. Once they break into other industries, I wouldn’t be surprised if legal frameworks are reworded to also apply to AI agents. If and when this happens, it would open the path for open source licenses to distinguish between agents and humans.

**What is a moat, if code can be trivially ported?** A team operating a popular open source project can no longer assume it’s expensive to fork or to be completely rewritten, meaning it makes sense to focus on other moats, such as:

- **Outstanding (paid) support.** AI could make this much easier at a higher quality, if done right.
- **Smaller open core, larger closed source part.** “Open core” as a business model has been dominant for commercial open source: keep the core of the software open source, while advanced enterprise features are source available or closed source. I would expect more companies to move their additional services to closed source, not source available.
- **In-person connection and community.** Projects with a real-world community will form a sense of connection that goes beyond code. For example, it’s hard to imagine vinext meetups popping up – whereas there are many Next.js communities.
- **Infrastructure and hardware remains a massive moat.** In a world where software is trivial to copy, infrastructure remains a moat. Commercial open source might make most sense for players that own and operate superior infrastructure layers than their rivals: and being able to offer lower cost, higher reliability, lower latency, higher performance, or a combination of these.

**One of the single best AI use cases is full-on rewrites of well-tested products.** I estimate that AI sped up the creation of vinext by at least 100x, which is massive. But we don’t really see efficiency boosts of anything like that with AI tools, in general. As Laura Tacho [shared](https://newsletter.pragmaticengineer.com/i/189035949/1-data-vs-hype-how-orgs-actually-win-with-ai) at The Pragmatic Summit in San Francisco, the average self-reported efficiency ‘AI gain’ seems to be circa 10%.

I suspect this vast chasm in efficiency boosts is because AI is many times more efficient at “no-brainer tasks” where correctness can be verified with tests, versus those which are more open ended or involve more creativity.

**In general, tests are incredibly important for efficient AI usage.** On The Pragmatic Engineer Podcast, Peter Steinberger stressed how important “closing the loop” in his developer flow is by instructing the AI to test itself, and ensuring the AI has tests to run that verify correctness.

Automated tests were always considered a best practice for creating maintainable code. Now, having a codebase with extensive tests is the baseline to make AI agents work productively for refactors, rewrites – or even adding new features and verifying that things did not break!

**Vendors will start to deploy “migration AI agents” to move customers over to their own stacks.** This got lost in Cloudflare’s announcement, but it’s [important](https://github.com/cloudflare/vinext):

> vinext includes an Agent Skill that handles migration for you. It works with Claude Code, OpenCode, Cursor, Codex, and dozens of other AI coding tools. Install it, open your Next.js project, and tell the AI to migrate:
>
> *> npx skills add cloudflare/vinext*
>
> Then open your Next.js project in any supported tool and say:
>
> *> migrate this project to vinext*
>
> The skill handles compatibility checking, dependency installation, config generation, and dev server startup. It knows what vinext supports and will flag anything that needs manual attention.

This is very clever from Cloudflare, and a true “AI-native” move. They have not only used AI to migrate Next.js, but also built an “AI plugin” (a skill) to help customers migrate their existing codebases over to vinext – and deploy on Cloudflare!

This move will surely be copied by other vendors, since migrations which are tedious for humans are much less effort with agents.

**AI is making the tech industry more ruthless when it comes to business practices.** Laura Tacho said something interesting at The Pragmatic Summit:

> “AI is an accelerator, it’s a multiplier, and it is moving organizations in different directions.”

AI seems to be accelerating the ruthlessness of competition for customers and the speed at which this happens. In one week, Cloudflare rebuilt Next.js, and it’s attacking Vercel full-on: claiming their “vibe coded” alternative is more performant and production-ready, and burying at the foot of the launch announcement the crucial information that vinext is very much experimental.

I sense vendors are realizing that there’s a limited amount of time in which to use AI to their advantage, and some will decide to use it like Cloudflare has.

**On the other hand, AI could be great news for non-commercial open source.** AI presents as a threat to commercial open source because it removes existing moats which make code hard to fully rewrite. However, beyond that, AI could help non-commercial open source to thrive:

- With AI, it’s easy to fork an open source project and keep the fork in-sync with the original.
- It’s trivial to instruct AI to rewrite an open source project to another language or framework.
- …and it’s equally trivial for AI to add features to a fork.

For these reasons, I believe there could be a lot more forks and rewrites to come, and more open source projects and code, in general.

Personally, I could not have imagined things changing this quickly in software. Rewriting Next.js in a single week, even to a version that is not quite there – but mostly works? This was out of the question as recently as a few months ago.

Things changed around last December, when Opus 4.5 and GPT-5.2 came out and proved capable [of writing most of the code](https://newsletter.pragmaticengineer.com/p/when-ai-writes-almost-all-code-what). What used to be expensive is now cheap – like rewriting complete projects – and we still need to learn what the “new” expensive parts of software engineering are.

All this is new territory for everyone. To succeed in the tech industry, you need to be able to capitalize upon change, as Cloudflare has clearly done in this case by making the most of an opportunity created by new technology. It’s unclear how popular vinext will become, and how much of a moat Vercel has around the broader Next.js ecosystem, but I suspect that it’d take more than a Next rewrite to make Cloudflare into a viable Next.js platform-as-a-service provider.
