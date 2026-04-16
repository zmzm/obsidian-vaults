---
type: twir-item
issue: 260
item: 9
item_type: item
date: 2025-11-26
source: https://product.hubspot.com/blog/migrated-from-enzyme-to-react-testing-library
tags:
status: auto
quality: keep
---

[[2025-11-26-TWIR-260|Index]]

# Item 9: Moving Mountains: How We Migrated from Enzyme to React Testing Library

Source: [https://product.hubspot.com/blog/migrated-from-enzyme-to-react-testing-library](https://product.hubspot.com/blog/migrated-from-enzyme-to-react-testing-library)

Summary:
HubSpot shares their multi-year migration from Enzyme to React Testing Library (RTL), covering planning, education, execution, and scaling strategies. The migration involved over 76,000 tests, required runtime instrumentation to assess scope, and emphasized user-centric testing philosophy, with a focus on minimizing disruption and supporting teams throughout the process.

Key takeaways:
- Enzyme is deprecated and lacks support for React 18+; RTL is now the standard for user-focused testing.
- Migration required careful planning, education, and tooling to support hundreds of teams.
- Progress was tracked and communicated transparently, with a focus on not blocking feature delivery.
- Lessons learned include the importance of migration tooling and balancing infrastructure with product work.

Recommendation:
Read fully (for organizations planning or undergoing large-scale test migrations)

Why it matters:
for organizations planning or undergoing large-scale test migrations

Content:
# Moving Mountains: How We Migrated from Enzyme to React Testing Library

![Enzyme1](https://product.hubspot.com/hs-fs/hubfs/Enzyme1.png?width=1471&height=703&name=Enzyme1.png)

For years, Enzyme was the de facto standard for testing React applications. Originally built by Airbnb in 2015, Enzyme makes it easy to assert, manipulate, and traverse the output of React components. The last official release of Enzyme came after React 16 was launched in 2017, but even then did not fully support all React 16 features. Ongoing support for Enzyme shifted to the open source community with React 17. However, the creator of the community-maintained Enzyme adapter announced that he would not be offering an updated version for React 18. This effectively marked the end of the Enzyme project, as it would prevent users from leveraging new features like React 18’s concurrent mode.

Around the same time, a project called React Testing Library (RTL) had gained traction in the open source community. Released in 2018, RTL represented a paradigm shift in how to think about testing applications - rather than making assertions about the internals of your components (e.g., props updating, callbacks being invoked, etc.), it promoted writing tests that represent the way users interact with your software. RTL’s [guiding principle](https://testing-library.com/docs/guiding-principles) is “The more your tests resemble the way your software is used, the more confidence they can give you”.

We knew that Enzyme would eventually become a blocker to modernizing our React usage; in August of 2022, we announced Testing Library as our official UI testing framework and began our migration. Over the next two and a half years, we migrated more than 76,000 tests from Enzyme to React Testing Library with virtually no automation. At our peak, we were migrating more than 4,000 tests per month across hundreds of repositories while continuing to deliver new features to our customers.

I’ll discuss how we planned and executed this migration, and how we might approach this work differently in the age of AI.

## **Planning**

We knew we needed a plan, but we didn’t want to prevent teams from getting a head start. For the first few months, we allowed the migration to progress organically – letting teams move away from Enzyme voluntarily while we developed a strategy.

First, we needed to understand the scale of the work we were undertaking. Early in this process we decided that simple static analysis of Enzyme usage would not be sufficient. It is common for tests to be generated programmatically, or for Enzyme methods to be invoked via test utilities or lifecycle hooks like beforeEach/beforeAll in a way that would underrepresent the effort needed for migration. Knowing that we wouldn’t want tests migrated from Enzyme to Testing Library 1:1, we erred on the side of overestimating the migration effort. We instrumented Enzyme’s render methods to collect runtime usage metrics and started to build a picture of Enzyme usage across teams. We were then able to divide packages into buckets:

|  |  |  |  |
| --- | --- | --- | --- |
| **Category** | **Definition** | **# of Packages** | **% of total** |
| **No tests** | No specs and no Testing Library or Enzyme calls | 572 | 40.4 |
| **Pure tests only** | Has specs but no Testing Library or Enzyme calls | 207 | 14.6 |
| **Testing Library tests only** | Has specs but no Enzyme calls | 130 | 9.2 |
| **Low** | 1-50 Enzyme calls | 300 | 21.2 |
| **High** | 101 to 500 Enzyme calls | 98 | 6.9 |
| **Very High** | 501 to 1000 Enzyme calls | 19 | 1.3 |
| **Massive** | 1001+ Enzyme calls | 11 | 0.8 |

Setting aside the scary number of packages with no tests (that’s a blog post for another day), this gave us a way to prioritize the more than 500 packages that would need to be migrated. (If we started this migration today, that number would be more than 1,500.)

We decided to start with packages with fewer tests first, and work our way up to packages with more tests. There was some risk in deferring the largest and most complex migrations, but this allowed us to concentrate our tech debt across the smallest number of packages. Knowing that this work was required to unblock other modernization efforts, we set the ambitious goal of completing this migration by the end of 2024.

![Enzyme2](https://product.hubspot.com/hs-fs/hubfs/Enzyme2.png?width=1589&height=836&name=Enzyme2.png)

By the time we shared our plan with engineers in December 2022, nearly 15% of all UI tests were already using React Testing Library - teams were eager to embrace a more modern testing framework and philosophy.

## **Education**

Testing Library uses a fundamentally different philosophy about testing from Enzyme. It encourages you to write your tests from a user’s perspective rather than an engineer’s perspective. Viewing tests through this lens means that we had accumulated tens of thousands of tests over the years that were not applicable in this new paradigm. We knew that documentation and knowledge sharing would be vital to the success of this project, so we leaned heavily into creating informative content early on.

HubSpot hosts an annual internal conference called EPIC Week, where we are invited to give a talk on any subject (work-related or otherwise). The testing teams used this opportunity to give a talk called “How to Rethink your Testing strategy” to help teams better understand how to embrace the new paradigm and write more effective tests. This talk covered concepts like user-focused testing, the [testing trophy](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications), and how to select the right type of test for different scenarios. We created guides for how to write tests that used the most common libraries in our stack, and developed tooling to minimize the toil of creating test fixtures and mock network payloads. This helped teams to feel empowered to take on the migration without the pressure of an imminent deadline.

## **Execution**

The first phase of the migration was to slow the addition of new Enzyme tests. We did this by first restricting net-new dependencies on Enzyme, and automatically commenting on any pull requests that added new Enzyme tests. We call these “invasions”, and we use this workflow for things like reporting bundle size changes, providing branch previews, and calling attention to risky code changes.

![Enzyme3](https://product.hubspot.com/hs-fs/hubfs/Enzyme3.png?width=1600&height=519&name=Enzyme3.png)

We also commented on pull requests that removed Enzyme tests, including a note when all Enzyme invocations were removed.

![Enzyme4](https://product.hubspot.com/hs-fs/hubfs/Enzyme4.png?width=1600&height=481&name=Enzyme4.png)

And to keep teams in the loop with our overall progress, we shared quarterly updates with engineers.

![Enzyme5](https://product.hubspot.com/hs-fs/hubfs/Enzyme5.png?width=720&height=720&name=Enzyme5.png)

Our frontend test setup is unique compared to much of the open source ecosystem in that we exclusively run our frontend tests in the browser. We find that running tests in the same environment that our code runs gives us far more confidence than running them in an emulated environment like JSDOM. So we also surfaced migration progress within our test reporter to give engineers real-time progress reports.

![Enzyme7](https://product.hubspot.com/hs-fs/hubfs/Enzyme7.png?width=958&height=89&name=Enzyme7.png)

It was important for us to keep the migration effort top of mind, but we never wanted our engineers to feel like it was blocking their work or preventing them from shipping updates to our customers. We allow-listed packages for continued Enzyme usage as needed, and never resorted to blocking builds or deployments due to increased Enzyme usage. As an infrastructure team, even our high priority projects take a back seat to other engineers being able to deliver for our customers.

## **Migrations At Scale**

It’s not uncommon for infrastructure teams to ask product teams to undertake migrations as part of evolving our tech stack, but we need to be thoughtful about how we balance this work against other priorities. When we started the migration, this process was full of toil. For a given team, we took all Enzyme tests across all of their repositories, divided them into equal chunks across the remaining quarters we had allocated to this effort, and created separate tickets per quarter to track the work. This was incredibly inefficient, required lots of manual updates as we moved from quarter to quarter, and didn’t give us a good way to track our overall progress.

Fortunately, in early 2024 we launched an internal system called Monarch that serves as a centralized hub for planning and sequencing migration efforts across teams. Monarch campaigns are governed by a small team of engineering leaders and staff+ engineers who ensure that teams aren’t overburdened by infrastructure initiatives and are given sufficient time to incorporate migration work into their planning process. It also gives campaign creators an aggregated view of progress across all teams. This system has become a critical piece of how we coordinate engineering efforts across teams.

We often cite our small, highly-focused teams as critical to how we’re able to move quickly, and this was no exception. Having a team dedicated to frontend testing allowed us to provide tooling and direct support throughout the migration process.

We also used cross-team embeds to provide white-glove migration service for our largest consumers of Enzyme, or for teams that were concerned about meeting their deadline. In practice, this meant one or two members of the testing team partnering with one or two members of a host team to align on an app-specific testing strategy and dedicating 1-2 weeks to focus exclusively on migrating tests.

These embeds were incredibly successful and often resulted in migrating a quarter’s worth of tests in a matter of weeks. You can provide teams with an endless supply of tooling and guidelines, but sometimes it just takes a little extra horsepower to get across the finish line.

Through a combination of education, planning, and persistence, we removed our last Enzyme tests in February 2025.

![Enzyme8](https://product.hubspot.com/hs-fs/hubfs/Enzyme8.png?width=1600&height=1069&name=Enzyme8.png)

## **What About AI?**

It may seem unusual to publish a blog in 2025 that doesn’t involve generative AI, but agentic development and AI-assisted coding tools like Copilot and Cursor were still in their infancy when we began this project. By the time these tools became widely available, our migration had achieved significant momentum, and we decided not to disrupt our progress by pivoting our migration strategy.

We knew it was important to use this opportunity to rethink our testing strategy holistically across our frontend ecosystem, and we didn’t think that an AI-assisted migration would push us in the right direction. It almost certainly would have accelerated our progress, but we weren’t confident that we would be as happy with the output.

We have invested heavily in this area for subsequent migration efforts, and have generally found migrations to be a great use case for AI. [All HubSpot engineers leverage modern AI tools](/blog/context-is-key-how-hubspot-scaled-ai-adoption), and AI fluency is now a baseline expectation for all engineering roles. We’ve developed agents to help with things like our design system modernization efforts, iterating on pull request feedback, and analyzing packages for patterns that could lead to flaky tests.

## **Lessons Learned**

If we were to start this migration today, there are several lessons we would apply. First, administering work at this scale is time consuming. Any investment you can make in automating task management and progress reporting is time well spent.

Secondly, a combination of AST transformations and AI agents could have greatly accelerated the migration for simple use cases like component unit tests. We’re not convinced it would have been the right solution for more complex integration tests (which is our preferred style of testing), but the improvements we’ve seen in AI tooling in recent years are making it increasingly feasible to automate these kinds of tasks.

Finally, small teams win. This is something we absolutely wouldn’t do differently - there’s a reason it’s part of our [engineering values](/blog/hubspots-engineering-values). Having a small team dedicated to this effort allowed us to focus on tasks that reduced migration friction and to reinforce testing best practices. It also allowed us to be force multipliers when teams needed additional resources to complete their migrations.

## **Wrapping It Up**

We couldn’t be happier with the results of the migration. Our product teams are shipping more confidently, and we have been able to continue our modernization efforts. We’ve started experiments with modern features like [Suspense](https://react.dev/reference/react/Suspense) and the [React Compiler](https://react.dev/learn/react-compiler), and we’re excited to apply those learnings across our frontend stack. A huge thank you to all of the teams involved in this massive undertaking, and a special thank you to [Francesco Signoretti](https://www.linkedin.com/in/signorettif/), [Romulo Ferreira](https://www.linkedin.com/in/romulonf/), [Eleanor Reich](https://www.linkedin.com/in/eleanor-reich-9a8480122/), [Kevin Bon](https://www.linkedin.com/in/bon-kevin/), and [Matt McCherry](https://www.linkedin.com/in/mattmccherry/) for shepherding this work to completion.
