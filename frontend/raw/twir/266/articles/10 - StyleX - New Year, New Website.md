---
type: twir-item
issue: 266
item: 10
item_type: item
date: 2026-01-28
source: https://stylexjs.com/blog/a-new-year-2026
tags:
  - "StyleX"
  - "ServerComponents"
status: auto
quality: keep
---

[[2026-01-28-TWIR-266|Index]]

# Item 10: StyleX - New Year, New Website

Source: [https://stylexjs.com/blog/a-new-year-2026](https://stylexjs.com/blog/a-new-year-2026)

Summary:
StyleX announces a new website and playground, reflecting its growth and adoption by major companies. The new playground allows in-browser StyleX compilation via @babel/standalone, and the site is rebuilt with Waku (a minimal React framework) and Fumadocs for documentation. The update showcases StyleX's compatibility with React Server Components and improved developer experience.

Key takeaways:
- StyleX now features a browser-based playground for instant experimentation.
- The new website is built with modern tooling (Waku, Fumadocs, StyleX), highlighting RSC compatibility.
- Recent StyleX features include shareable media queries, view transitions, anchor positioning, and combinator-based styling.
- Ongoing focus on ergonomics, new features, and tooling for 2026.

Recommendation:
Read fully (read fully if interested in StyleX adoption or new developer tooling)

Why it matters:
read fully if interested in StyleX adoption or new developer tooling

Content:
# New Year, New Website

Happy New Year!

StyleX has been in development for just over six years. It started as a way to
solve
[styling problems](https://engineering.fb.com/2020/05/08/web/facebook-redesign/)
at the scale of [facebook.com](https://www.facebook.com/). It proved itself at
Meta and became the default way to author styles for web surfaces, and was
open-sourced a little over two years ago in December 2023.

2025 has been a big year for StyleX. We've seen adoption from companies like
Figma, Snowflake, and HubSpot. The feedback has been largely positive and has
validated our core design decisions within various use-cases. We've taken this
feedback and developed new features and refinements alongside the evolution of
CSS itself. Within the last year, we’ve added APIs for shareable media queries
([`stylex.defineConsts`](/docs/api/javascript/defineConsts)), View Transitions
([`stylex.viewTransitionClass`](/docs/api/javascript/viewTransitionClass)),
Anchor Positioning ([`stylex.positionTry`](/docs/api/javascript/positionTry)),
and combinator-based styling ([`stylex.when.*`](/docs/api/javascript/types)).

The new APIs are easy to spot, but a lot of progress is quieter. A recent
milestone was the release of the
[`@stylexjs/unplugin`](/docs/learn/installation/vite) package, which makes
integration in web projects a lot simpler than it used to be. Setup friction was
one of the most common reported painpoints, and this new package is a big step
toward reducing it.

The new playground was quietly made public a few weeks ago. It's now the
lowest-friction way to try StyleX without setting up a project. It is made
possible by a version of the StyleX compiler that uses `@babel/standalone` to
compile StyleX right in the browser. As a result, it's smaller, faster, and more
reliable than the previous playground. It's also now possible to share links to
your code examples within the playground.

A huge thanks to [Henry Q. Dineen](https://github.com/henryqdineen) for making
this a reality!

We redesigned and rebuilt the website from the ground up as a showcase of StyleX
itself. For the last two years, the StyleX website was built on Docusaurus 2. We
rewrote some of the core UI components with StyleX, but a large part of the site
still relied on Docusaurus components. As a result, the website used a mix of
traditional CSS, CSS Modules and StyleX for styling. We were also stuck on an
old version of React and updating to Docusaurus 3 would have been a major
effort.

The new website is built with Waku, a minimal React framework that lets us
benefit from, and showcase StyleX's compatibility with React Server Components.
Waku is built on Vite, which lets us dogfood the `@stylexjs/unplugin` package.

For documentation features, we chose Fumadocs, a small and flexible
documentation framework that is compatible with Waku. It is modular enough that
we could rewrite all the UI components with StyleX. We translated the components
from `fumadocs-ui` and then customized them further. This let us achieve a more
distinctive design without redundant code by using the features of StyleX and
modern CSS.

We're always thankful for the continued feedback and support from the community.
We have some [big plans](https://github.com/facebook/stylex/issues/1356) for
2026, with themes of better ergonomics, new feature work, and developer tooling.
For now, we are launching this new website as a celebration of the journey so
far.

Related notes: [[Server Components]]
