---
type: twir-item
issue: 299
item: 5
item_type: item
date: 2026-09-30
source: https://github.blog/engineering/architecture-optimization/improving-site-performance-by-shipping-more-css/
tags:
  - "GitHub"
  - "CSS"
status: auto
quality: keep
---

[[2026-09-30-TWIR-299|Index]]

# Item 5: GitHub - Improving site performance by shipping more CSS

Source: [https://github.blog/engineering/architecture-optimization/improving-site-performance-by-shipping-more-css/](https://github.blog/engineering/architecture-optimization/improving-site-performance-by-shipping-more-css/)

Summary:
GitHub’s Primer Design System migrated from a CSS-in-JS solution to CSS Modules to improve performance and maintainability. The migration was incremental, using feature flags and automated tools to safely transition thousands of components and inline style props (sx) to CSS Modules. The process resulted in significant server-side rendering and initialization time reductions, and the approach may be extended to the broader GitHub codebase.

Key takeaways:
- CSS Modules replaced CSS-in-JS for Primer, yielding 55% SSR and 25% component init time improvements.
- Migration was gradual, using feature flags, visual regression tests, and automated codemods.
- Removal of the sx prop and styled-components required extensive, partially automated refactoring.
- Demonstrates a scalable, low-risk migration strategy for large React codebases.

Recommendation:
Read fully (especially if you maintain large React apps or design systems and are considering CSS-in-JS alternatives)

Why it matters:
especially if you maintain large React apps or design systems and are considering CSS-in-JS alternatives

Content:
# Improving site performance by shipping more CSS

The [Primer Design System](https://primer.style/) powers many of the experiences you see on GitHub today. From buttons to banners to breadcrumbs, these foundational components are required to be accessible, flexible, and performant across a wide variety of scenarios.

Back in 2023, the number of components on certain pages began to explode. This led to several performance-related challenges with our existing CSS-in-JS solution:

- Initial page loads took longer due to styles being initialized on the client
- Server-side rendering performance declined as style collection shifted from the client
- Updates to styles grew out of control as component count grew on a page

It became clear that the Primer team needed to address the issue at the source. We needed to find an alternative that would completely avoid the client and server costs that we were seeing with our current solution. Most importantly, any alternative we pick would need to work in a way that would avoid any breakage to GitHub during the migration.

## Introducing CSS (Modules)

The Primer team found a solution that met all of our criteria: [CSS Modules](https://github.com/css-modules/css-modules). This format would allow us to do one of our favorite things: write and use native CSS features, while still allowing some amount of the colocation and encapsulation that we had come to expect from CSS-in-JS.

With CSS Modules, styles would be authored in a CSS file alongside the JavaScript source for the component. It would also allow us to treat all class names as local by default, preventing some of the collisions and challenges that can come from global selectors. This format also removes the need for any client or server runtime behavior. Instead, styles would roll up into CSS stylesheets that were sent as part of the HTML for a page.

However, this solution was radically different from the CSS-in-JS solution we had at the time. This change would require an update to every Primer component and every component at GitHub authored using this technique. Thankfully, design systems are a perfect vehicle to deliver this kind of change at scale.

## A gradual march towards CSS Modules

The situation for moving towards CSS Modules was clear. The Primer team would need to deliver updates to each of its components, moving them from CSS-in-JS to CSS Modules. At the same time, updates we made to these components could not break any usage in GitHub. Finally, the underlying technique we used for CSS-in-JS also had to continue working for any components in GitHub that were currently using it.

With all these constraints in place, we decided on an incremental migration strategy that would allow us to safely ship component updates without breaking the world. For each component, our plan was to:

- Add a new file that translated existing styles to CSS Modules
- Add the component to a feature flag that would toggle between the new and old styles
- Use existing visual regression tests to verify snapshots were identical between our CSS-in-JS solution and CSS Modules
- Gradually roll out the feature flag to our team, then to GitHub staff, and finally to all GitHub users to catch any issues along the way

This process created a strong feedback loop where issues were flagged early in the process as Primer continuously delivered these changes to GitHub. The use of feature flags allowed us to do this migration safely while giving us clear signals on the performance benefits of CSS Modules.

By December 2024, all components in Primer were migrated over to CSS Modules using this process. We saw performance wins across the board, in particular:

- 55% less time to server-side render a page
- 25% less time for components on a page to initialize

With clear performance wins from doing this work in Primer, we began to wonder if we could see similar performance wins by doing these conversions in other parts of GitHub. Similarly, how long until we could ultimately drop support for CSS-in-JS across the company?

## Moving away from CSS-in-JS at GitHub

One of the trickiest parts about removing our CSS-in-JS solution from Primer was due to the usage of the `sx` prop. This prop was *the* way to style and customize components from Primer. Teams could provide an inline object to customize everything about the component. It represented the best and worst parts of CSS-in-JS:

- Excellent TypeScript support with integration with our Design Tokens
- Co-located with the component so that everything was in one place
- High runtime cost due to the dynamic nature of inline objects used for `sx`
- Difficulties scaling as the number of components using `sx` on a page grew

As a result, the first part of our journey to move away from CSS-in-JS was to reduce `sx` usage across GitHub. This would allow us to immediately improve performance similar to the wins we saw when migrating Primer components. It also set us up perfectly for removing CSS-in-JS entirely from the product.

## The Duality of Primer

It’s important to note that, while the design system itself was officially off `styled-components`, a large part of the GitHub codebase itself wasn’t. With `sx` props having been the de facto styling standard at GitHub for years, we were looking at thousands of `sx` props that needed migration before we could even think of getting GitHub onto the sleek new `@primer/react` version which didn’t rely on `styled-components`.

So… how did we do this immense amount of work while increasing confidence and reducing risk? The answer: not all at once.

The original CSS migration was a little bit more nuanced than we led on: in addition to migrating the components to CSS modules, feature flagging to test in production and slowly rolling them out, we also created “wrapper” components in a transitive library we called [`@primer/styled-react`](https://github.com/primer/react/blob/main/packages/styled-react/README.md). The whole purpose of this package was to allow `sx` usage into the newly migrated components. This way, the instances of the GitHub UI codebase that were using this prop could continue to consume them by importing the same component through `@primer/styled-react`, while we realized the performance gains of importing straight from `@primer/react` for the cases that didn’t.

## Styled Box Zero

The next phase of the migration process was as follows:

- On a package-by-package basis:
  - Translate all `sx`usage into equivalent CSS modules files. This included cross referencing (See [migrating to CSS variables](https://primer.style/product/primitives/migrating/))
  - Replace `@primer/styled-react` imports with `@primer/react` imports
  - Test in pre-production
  - Deploy

Curiously enough, while we were getting ready to undertake this massive effort, `styled-components` [maintenance mode](https://opencollective.com/styled-components/updates/thank-you) was announced, offering further confirmation that we were taking steps in the right direction.

The work kicked off April 2025 with a peak of ~7,760 `sx`props to be migrated; we wouldn’t see it realized until May 2026. Initially, one of our great in-house developers, [Ian Sanders,](https://github.com/iansan5653) created a [VS Code plugin](https://marketplace.visualstudio.com/items?itemName=ian-sanders.sx-to-css) that would assist with per-prop migration. A similar codemod was developed internally and utilized to migrate entire files in the GitHub codebase. The work, while requiring a bit of manual oversight and careful validation, was mostly automated. A rotation of 8 engineers migrated 6,419 props over the course of 6 months, observing Server-Side Rendering time performance gains ranging from 1% up to 22% in some pages.

![Table titled “Server Side Rendering” with a search field and columns for CATALOG_SERVICE, CONTROLLER, and IMPROVEMENT. It lists GitHub services and controllers with improvement percentages ranging from 3.05% to 21.97%, including a highest value of 21.97% for github/code_view / commit.](https://github.blog/wp-content/uploads/2026/09/625328348-91f668f6-2565-492d-aa76-632d429fb4ba.png?resize=1024%2C966)

In a different side of GitHub, Copilot’s capabilities were increasing exponentially. AI was getting smarter, more capable; we released Copilot coding agent and Copilot code review while this work was still underway.

By the time we picked this work back up, now April of 2026, the panorama was different; we were able to get down from 895 to 0 `sx`props in the span of three weeks with a team of two engineers, relentless determination, and a whole lot of Copilot coding agents.

![Area chart titled “Total SX props” showing values declining from about 7,300 in May to near zero by June–July of the following year, with several short-lived spikes. Two highlighted points are labeled 6.87k around August and 5.37k around October.](https://github.blog/wp-content/uploads/2026/09/623314819-82999b6e-c79e-4163-8ec5-a4a36e439c6c.png?resize=1024%2C232)

## Battle of the themes

It was a big day: we had finally completed the `sx` migrations that were standing between us and full `styled-components` removal, years in the making… we can finally clean up these dependencies and move on to different, more exciting work, right? Wrong!

GitHub supports [seven different themes](https://docs.github.com/en/get-started/accessibility/managing-your-theme-settings), all of which offer a high contrast mode variation. All of it enabled through, you guessed it, `styled-components`. Before we can even think of removing these dependencies, we need to decouple our theming.

Now, this isn’t as huge a deal as it sounds. Our theming variables have always been defined in CSS through our `@primer/css` package, and we already planned forward for non-styled Theming when we migrated `@primer/react` in late 2025. It’s the JavaScript usage and utilities that are enabled by `styled-components` that we needed to remove. Once again, we got to work.

You know the drill by now: perform the migrations, roll it out slowly, feature flag everything. Two months and a few hiccups along the way later, we were all-systems go for dependency removal; we even feature flagged that. Better safe than sorry.

## All’s well that ends well

GitHub has been running on 100% CSS modules as of June 2026. The safeguards we put in place enabled us to roll out significant architectural changes safely, stress test in production, catch errors, pivot and repair efficiently, ultimately allowing us to succeed in our goals and realize great performance gains along the way.

What looked at first like a CSS migration turned out to be a gradual re-platforming of how GitHub styles, themes, and ships UI at scale. By the end, we had not only removed `sx`, `styled-components`, and `styled-system` from dotcom, but completed it without breaking GitHub along the way. Enhancing the performance, user experience and delight of our products continues to be top of mind for all of us here at GitHub.

## Written by

Josh Black is a Software Engineer based in Austin, Texas. He loves working on Design Systems, creating accessible experiences, and eating chilaquiles.

Marie is an Atlanta-based Software Engineer on GitHub Primer. If she's not pushing pixels, she's probably pushing a carry-on into an overhead bin somewhere over the Atlantic.
