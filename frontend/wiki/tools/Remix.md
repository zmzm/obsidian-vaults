---
type: tool
status: active
updated: 2026-10-22
tags: [remix, react-router, routing, web-platform]
---

# Remix

Remix is a lineage and architecture hub. The archive uses the name for both the React-based Remix v2 line that evolves into React Router framework mode and a separate Remix 3 design centered on web APIs and a different UI model.

## Key Ideas

- Keep lineage explicit: the captured kentcdodds.com account upgrades Remix v2 to React Router v7. This is distinct from adopting the Remix 3 design presented at Remix Jam.
- The first-party Remix Jam recap presents composable Fetch-based server modules, named routes, explicit UI updates, selective hydration, and HTML-oriented async frames. Those examples describe the captured design stage, not a current API guarantee.
- The durable React-based branch is route-associated loading, mutations, and validation; follow React Router for maintained architectural discussion in this wiki.
- The later Remix UI tutorial is summary-only. Do not use its date or the older Preact-fork plan to infer current implementation, compatibility, or release readiness.

## Practical Significance

- When a source says Remix, identify its generation, rendering model, and intended migration path before carrying its advice into an application.
- Treat explicit update ownership and web-platform boundaries as design choices with coordination and cleanup costs, rather than proof that one framework is inherently simpler.

## Related Pages

- [[React Router|React Router]]
- [[Vite|Vite]]
- [[Preact|Preact]]
- [[../case-studies/Remix v2 to React Router Route Parity|Remix v2 to React Router Route Parity]]
- [[../patterns/Typed Routing and URL State|Typed Routing and URL State]]
- [[../syntheses/Frameworks as Constraints in the AI Era|Frameworks as Constraints in the AI Era]]

## Sources

- [[../../raw/twir/255/articles/09 - Remix Jam 2025 Recap|09 - Remix Jam 2025 Recap]] — extracted first-party design recap.
- [[../../raw/twir/270/articles/06 - Kent C. Dodds - Migrating Remix v2 to React Router v7 with Cursor|06 - Kent C. Dodds - Migrating Remix v2 to React Router v7 with Cursor]] — extracted application migration account.
- [[../../raw/twir/292/articles/08 - How to Think in Remix UI Instead of React|08 - How to Think in Remix UI Instead of React]] — summary-only later UI tutorial.
- [[../../raw/twir/236/articles/01 - Wake up Remix - The plan for Remix v3|01 - Wake up Remix - The plan for Remix v3]] — summary-only historical plan; not a current dependency claim.

## Open Questions

- Which parts of the captured Remix 3 design remain in subsequent releases?
- Where does explicit update ownership simplify debugging, and where does it shift synchronization work to application code?
