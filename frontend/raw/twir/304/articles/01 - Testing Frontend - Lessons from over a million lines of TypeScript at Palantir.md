---
type: twir-item
issue: 304
item: 1
item_type: featured
date: 2026-11-04
source: https://www.meticulous.ai/blog/lessons-from-a-decade?utm_source=this_week_in_react&utm_medium=newsletter&utm_campaign=26q3_2&utm_term=react_link
tags:
  - "TypeScript"
status: auto
quality: keep
---

[[2026-11-04-TWIR-304|Index]]

# Item 1: Testing Frontend - Lessons from over a million lines of TypeScript at Palantir

Source: [https://www.meticulous.ai/blog/lessons-from-a-decade?utm_source=this_week_in_react&utm_medium=newsletter&utm_campaign=26q3_2&utm_term=react_link](https://www.meticulous.ai/blog/lessons-from-a-decade?utm_source=this_week_in_react&utm_medium=newsletter&utm_campaign=26q3_2&utm_term=react_link)

Summary:
This article distills a decade of frontend testing experience at Palantir, focusing on strategies that maximize engineering velocity. It emphasizes that the main determinant of a team's impact is confidence in making changes, which is directly tied to the cost and effectiveness of automated tests. The key insight is that most frontend tests, if not thoughtfully designed, can slow teams down due to high maintenance costs. The post advocates for testing at the "minimal cut"—choosing stable boundaries for tests to minimize fragility and maintenance overhead.

Key takeaways:
- Testing is the only engineering investment that can potentially double velocity; most others yield incremental gains.
- Maintenance cost per test is crucial—lowering it increases total test coverage and value.
- Tests should be scoped to stable, domain-reflecting APIs to avoid frequent breakage from internal changes.
- Poorly chosen test boundaries lead to fragile tests and slow development.

Recommendation:
Read fully (for practical strategies and nuanced examples on test design and maintenance)

Why it matters:
for practical strategies and nuanced examples on test design and maintenance

Content:
# Testing Frontend - Lessons from over a million lines of TypeScript at Palantir

## Lessons from a decade: the most critical three

Prior to Meticulous.ai I spent ten years at Palantir helping lead engineering for Palantir’s main frontend. Through this we learnt how to test frontends effectively, the hard way.

With dozens of apps, 100s of developers, and millions of lines of TypeScript we were able to try different approaches, study the root causes behind each bug that made it to production, iterate and learn. We combined our own experiences with talking with other tech leaders - and reading the best materials we could find out there. Our learnings over those years are something I’ve never been able to find somewhere else. This post distills the most critical three.

There’s a lot to FE stability beyond just testing (monitoring & alerting, incremental metric-dependent rollout, fast or auto rollback etc.). Here we concentrate just on testing. Here’s why:

## Getting testing right is the only investment that has the potential to double your engineering velocity

The main determinant of the impact of an engineering org is building the right product†: prioritising the investments & experiments that give you maximal *information* on product/market fit, and iterating on a daily or weekly cycle with your users.

But if you look at pure engineering changes — developer education, developer tooling, developer practices etc. — most only make incremental improvements to your total velocity. Few have the potential to double your impact. Testing is the single exception.

If you look carefully at how your team spends their hours, only a fraction of it is likely hammering out code — in most teams more time is sunk into:

- Searching through the codebase to understand all code that could be affected, before making your change, and so minimise risk of any unexpected impacts
- Manually testing your changes as you write them and before pushing up your PR. And then testing again after addressing PR comments, and sometimes testing again at release stage (each time often testing not just the direct targets of your change but also all related paths that *could* be affected, each sometimes across multiple permutations -- configurations; user types, data responses, feature flags, screen sizes etc.)
- Triaging, repro’ing, root causing and fixing issues that occur in the field
- … and all the context switching in-between

In contrast if you can make any change with confidence then you can not only iterate dramatically faster (shipping code at the speed you can write it), you can also refactor continuously with complete ease, and ensure you can *maintain* that initial velocity over time. When developers don’t have the confidence to make sweeping changes they tend to just avoid large refactors to protect their individual velocity. The result can be a self-reinforcing downward spiral: as the codebase quality degrades, refactors become even more risky, and we become even more cautious to do them.

Despite this most automated frontend tests we’ve seen teams add (whether at the unit level or the end-to-end level) actually make the team slower rather than faster. The time taken to author them and, much more significantly, to *maintain* them, outweighs the value they provide.

However… if you think carefully about a testing strategy for your projects you can make new tests trivial to write, and often almost entirely eliminate any maintenance. If you can crack this then you can move extremely fast. But before we move onto our three most important learnings in how to make that happen, it’s worth understanding the most critical determinant of success in a testing strategy: maintenance cost.

**†** *The second largest determinant of impact for mature engineering organisations may well be careful strategy (and extreme caution!) around migrations and rebuilds where you have to match existing functionality or compatibility. Tip: break it down into incrementally deliverable steps that allow you to iterate as you learn the full costs and tradeoffs involved. Deliver incremental value and ensure you can successfully abandon at any point.*

## Maintenance cost *really* matters

Roughly speaking, given a fixed budget, the number of tests you can afford in the long run is inversely proportional to the maintenance cost of each test:

![](/images/blog/lessons-from-a-decade/67910626bcafbac4661ac0e7_65904cad11f274f3b2155cde_maintenance-cost.png)

The more tests you can afford the more coverage you have, and the more value your tests provide. This means the maintenance cost ***really matters.*** A fixed decrease in maintenance cost per test can give an exponential increase in the collective value of your tests.

There are two strategies to achieve this: the first is to assume the tests break all the time, but make it lightning fast to understand whether the change is expected or not, and to update the tests or snapshots. In this case every second matters: shaving off the time to review and update from 5 seconds to 4 seconds can be transformative.

The second strategy is to avoid having to update tests at all — and the most important principle here is to test at the minimal cut:

## #1: Unit tests: test the right sized unit, at the [minimal cut](https://en.wikipedia.org/wiki/Minimum_cut)

When you write a test, whether a unit test or an integration test, you have to decide the scope of your test — what application code do you run as part of your test, and what do you mock out.

Often it’s tempting to fall into the trap of having a unit test test a single class, function or component — but more often than not this doesn’t make sense.

Imagine you have an app that calculates an optimal route between two map points and renders it to a canvas:

![](/images/blog/lessons-from-a-decade/67910626bcafbac4661ac10f_659042a47ab093299d225aa8_Untitled-201.png)

Your test can test the route calculation and the route rendering separately, or test it together. It may be easier to cover all the route-calculation edge cases (different types of route tradeoffs) and all the rendering edge cases (different types of curves) by testing each component separately. If the way you want to render routes changes frequently then you won’t need to touch the tests for the route-calculation edge cases; and when something breaks it’ll be easier to narrow it down to the part of code broken. Each of these modules has enough complexity to be worth testing separately.

However now imagine that your optimal route calculation module uses a sub-function to calculate the time taken for each potential sub-part of the route, and then utilises that to calculate the optimal overall route. In this case it’s possible that it makes more sense to test the whole route calculation module as a single unit: you only care that it continues to return the optimal route over time, not how the internals are wired together. You may want to change the internal implementation (say, improving performance) over time without breaking the tests.

In general you can imagine your app as a network of collaborating modules (functions/classes/components etc.):

![](/images/blog/lessons-from-a-decade/67910626bcafbac4661ac0ff_659042d088fbae0751ed9c2f_graph.png)

When you write a unit test, you decide what application code is inside the scope of the unit test:

![](/images/blog/lessons-from-a-decade/67910626bcafbac4661ac0fc_6590494cdbb6f549d68735fe_graph-good-no-caption.png)

Any API that has to be mocked out adds fragility to the test. Try to minimise the API surface that your test boundary bisects, and bisect APIs that are as stable as possible: APIs that naturally reflect your domain, rather than APIs that are internal implementation details that may change over time.

Any communication lines crossing this boundary have to be mocked out. And if any of those communication lines change - say due to refactoring how the modules communicate, or by changing the APIs of those communication lines — then your test breaks and you have to update it. You therefore want to choose a minimum cut, that gives maximal coverage: choose the boundary to intersect a minimum API surface, that is as stable as possible, while containing inside of the boundary code of a sufficient complexity to be worth testing as a single unit.

If you choose those boundaries poorly then your tests will frequently break as the codebase evolves, and you may find their cost exceeds their value:

![](/images/blog/lessons-from-a-decade/67910626bcafbac4661ac102_659042ec582e5f01dc760e56_graph-bad.png)

‍

**The art of writing productive tests requires working out how to carve up your application such that each test exposes itself to a minimal set of APIs that are as stable as possible.**

Getting the scope of the tests matters more than pretty much anything else. When deciding the scope of your tests, consider:

- What behaviour do you care about preserving over time? If your test implicitly tests implementation details you don’t care about then you may be testing at the wrong level.
- Choose natural boundaries for your units to test, that run across stable API lines in your codebase that are easy to mock.
- Have the scope of the test sufficiently large such that the unit is complex enough to be worth testing, and the test does not assert too many implementation details. But not so large that it becomes hard to test the many combinations of edge cases, and hard to keep track of what you have vs haven’t tested.

## #2: (Probably) don’t write Enzyme or component tests

[Component tests](https://enzymejs.github.io/enzyme/) are unit tests that render a React component in a virtual environment and test interacting with it. We’ve found these tests are rarely worthwhile writing, except for maybe a minority of the more complex collections of components in your application. If you do write them, it often makes sense to test a collection of collaborating utilities and components that together form a single much more complex component.

Even in the most extreme case where you’d expect such tests to be a clear win — Palantir’s open source component framework [BlueprintJS](https://blueprintjs.com/), which has complex components, used by 10s of 1000s of projects, where the slightest bug can have huge consequences — it wasn’t always clear that the Enzyme tests actually paid off.

The reason is:

(1) these tests are slow to write and fragile to maintain - you’re often tweaking your UX and components, and as you do so the tests need updating

(2) most of the complexity can be more reliably tested by pulling the complex logic out of your component, into utility functions, separate from the UI itself, and testing those. These tests are less fragile since they break only when you change your abstractions or logic: not when you change the structure of your DOM. They interact with a much smaller API surface.

**If you have over 50% test coverage from manual unit tests in a frontend codebase then you’ve over-invested in testing**: you’re almost certainly slowing yourself down rather than speeding yourself up.

## #3: Scalable integration tests: look for stable APIs in your app where the variation in the values passed through that API is the root of a lot of the complexity in your app

*- and build a structure that makes each next integration test trivial to add, and costs zero to maintain*

Think carefully about your application — where does the majority of the complexity you want to test come from? What APIs (internal and external) change frequently vs rarely? And can you setup structures that make each individual test trivial to add, and align the testing boundary with the APIs that change rarely, such that these tests rarely need updating?

This won’t work with all applications, but it does for many. MapboxGL, an open source library for rendering maps, is a great example. All the information to render a map is defined by a [JSON document](https://docs.mapbox.com/style-spec/guides/) called a style spec. Their main test suite maps style specs to screenshots of the resultant rendered map: adding a test is just a case of dropping a [style spec JSON file](https://github.com/mapbox/mapbox-gl-js/blob/main/test/integration/render-tests/real-world/bangkok/style.json) into a folder. If the code changes it’ll show you the difference between the before and after screenshot, and you can merge the updated snapshot. The style spec is public API for MapboxGL, so it rarely if ever breaks — and since the style spec never breaks the tests never break.

Similar techniques can be used with any application that has a stable API format, where variation in the values provided to that API account for the majority of the complexity that needs to be tested. This includes any app where users author things — like Figma (designs), Google Docs (docs), and Slack (messages). But it can also cover anywhere there’s a stable API between services, or inside an app.

For example, one of Palantir’s backing services is responsible for returning sets of objects from the database systems given a certain query. The tests consist of a library of triples of files: the first file defines the objects to populate into the test database, the second a query, and the third a generated snapshot of the expected results. Adding a test is just a case of dropping in a couple of extra files. Since the query format should never break the tests are write-once-change-never: your test coverage grows over time but you never need to update an existing test.

## What tests are worth writing?

Ok, so:

- Don’t fall into the trap of every unit test testing a single function/class.
- Choose the size and the scope of the code covered by each test judiciously: not too big to be complex to cover all edge cases; but large enough to cover sufficiently complex functionality to make the test pay off, with a minimal surface to mock out — and pick a boundary that runs along stable API lines in your codebase that are easy to mock.
- If you’re writing tests manually, don’t aim for 100% coverage for FE apps (or anywhere near) — instead think whether the test will provide more value than it costs
- Skip the component tests
- Look for opportunities specific to your application, and build a structure that makes each next integration test trivial to add, and costs zero to maintain.

But what tests *are* worth writing? If you’re still writing tests manually, rather than automatically generating tests, then we’d suggest:

![](/images/blog/lessons-from-a-decade/67910626bcafbac4661ac0ea_659050e7720c2702e4af0800_pyramid.png)

- Write unit tests for sufficiently complex logic (a single test may test may a small network of functions/classes collaborating together).
- Write a smaller number of integration tests for key parts of the system, that test multiple of those modules collaborating together.
- And a couple of end to end tests to smoke test key flows that everything works together as a whole.

You don’t want too many end-to-end tests, or to use these to cover all edge cases, since they’ll be extremely expensive to maintain as your UX evolves. This is true whether they’re written in code or recorded through a point-and-click tool.

These techniques will accelerate your team. But they won’t let you double your engineering velocity, not even close. To get there you’ll need to move beyond manually writing and maintaining tests, and:

## Take the denominator to zero

A large web-app has 10s of 1000s of edge cases (logical branches, feature flags, configurations, screen sizes, locales, variations in user data & content and flows initiated from different starting states and in different orders). As long as you’re manually writing and maintaining tests it’ll be infeasible (and unadvisable) to get anywhere close to 100% test coverage: the maintenance cost will kill you.

A different approach is needed. For that we first need to step back:

At most engineering organisations every feature is used at least once before it’s deployed to production: developers click around on localhost while they iterate on their branch, previewing their changes. The issue is that every existing user flow can not feasibly be retested on every future change to the codebase (or even on follow up commits on the original pull request). You have an N2 problem.

However those daily interactions on localhost, staging stacks, and preview URLs by your development team are the key. This data stream describes the complex flows that unlock the path to test every feature of your app -- and can be used to automatically test for regressions.

[Meticulous AI](https://meticulous.ai/) is the category leader here - and can even be used to sample production flows too. Every interaction is recorded, and by understanding every line of code executed by each flow it maintains a visual snapshot test suite that covers close to 100% of your code. This suite tests your apps UI, user flows and logic at all layers, across all edge cases, all branches, all feature flags. As your app evolves, your test suite evolves. The tests are executed in an environment that preserves determinism from the browsers scheduling layer up — so no flakes.

You’ve taken the denominator to zero, and the maximum maintainable test count becomes unbounded.

If you’ve ever had the rare chance of working on a project with testing at this level you’ll know that programming feels completely different. Every dev can refactor with complete confidence and speed. And so they do, keeping the code fresh & nimble. You’ll be able to move faster than you’ve likely ever experienced before in your career.

Never write, debug or fix a test again. Book a call [here](https://www.meticulous.ai/book-a-demo) to learn more.
