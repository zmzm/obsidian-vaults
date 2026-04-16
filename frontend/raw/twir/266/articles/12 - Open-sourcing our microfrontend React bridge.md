---
type: twir-item
issue: 266
item: 12
item_type: item
date: 2026-01-28
source: https://alexocallaghan.com/open-sourcing-mfe-react-bridge
tags:
status: auto
quality: keep
---

[[2026-01-28-TWIR-266|Index]]

# Item 12: Open-sourcing our microfrontend React bridge

Source: [https://alexocallaghan.com/open-sourcing-mfe-react-bridge](https://alexocallaghan.com/open-sourcing-mfe-react-bridge)

Summary:
Mintel has open-sourced @mintel/mfe-react-bridge, a small library to help micro-frontend architectures upgrade React independently across multiple apps. Unlike existing solutions, it focuses on minimalism and avoids unnecessary re-rendering, supporting React 17 and 18+ with TypeScript types and robust testing.

Key takeaways:
- Enables independent React version upgrades in micro-frontend setups.
- Lightweight, focused alternative to @module-federation/bridge-react.
- Supports React 17/18+, TypeScript, and is production-tested.
- Open to community feedback and contributions.

Recommendation:
Read fully (read fully if working with React micro-frontends or versioning challenges)

Why it matters:
read fully if working with React micro-frontends or versioning challenges

Content:
# Open sourcing our microfrontend React bridge

I wrote previously about how we upgraded React incrementally across multiple micro-frontends using a bridge component. We initially looked to use the `@module-federation/bridge-react` package, but ran into some issues with re-rendering and it doing more than we needed.

To solve this we created our own package, which we're using successfully in production to allow our 28 micro-frontends to upgrade React independently. We've now open sourced this package as [@mintel/mfe-react-bridge](https://www.npmjs.com/package/@mintel/mfe-react-bridge) on npm.

It's a small library with a couple helper functions to provide a React component interface to render micro-frontends that use different React versions (or totally different UI frameworks). It provides TypeScript types, supports React 17 and 18+, and is well-tested.

Hopefully this proves useful to others facing similar challenges with micro-frontends and React versioning. Feel free to raise any issues on [GitHub](https://github.com/awocallaghan/mfe-react-bridge).
