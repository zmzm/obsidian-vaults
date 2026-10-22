---
type: "twir-recovery"
issue: 295
item: 5
source: "https://github.com/DefinitelyTyped/DefinitelyTyped/pull/75429"
final_url: "https://github.com/DefinitelyTyped/DefinitelyTyped/pull/75429"
retrieved: "2026-10-22T11:30:10+00:00"
original_note: "frontend/raw/twir/295/articles/05 - React Types PR - Types for React 19.3.md"
editorial_review: "pending"
truncated: false
---

Original intake note: [[../articles/05 - React Types PR - Types for React 19.3|React Types PR - Types for React 19.3]]

# [react] 19.3 by eps1lon · Pull Request #75429 · DefinitelyTyped/DefinitelyTyped · GitHub

```
React 19.3 promotes `browser()` from the canary channel to stable, so its types move out of `react-dom/canary` into the main entrypoint. The `browser()` function, the opaque `BrowserUsable` return type, and the `"react-dom/browser"` entry in the `RendererUsable` registry are now declared in `index.d.ts`, and the corresponding tests move from `canary-tests.tsx` to `react-dom-tests.tsx`. The declarations are unchanged apart from an added `@version 19.3.0` JSDoc tag. A bare `export {}` is added to `index.d.ts` so the private `browserUsable` brand symbol stays unexported, matching the pattern already used in `static.d.ts`.

Co-Authored-By: Claude Code (kimi-k3[1m]) <noreply@anthropic.com>
```

```
The current React canary features are shipping as stable in React 19.3, so the remaining canary declarations move into the stable entrypoints. In `react`, the `<ViewTransition>` component with its `ViewTransitionProps`, `ViewTransitionInstance`, and `ViewTransitionClass` types, `addTransitionType`, the `ref` prop on `FragmentProps` together with the renderer-augmented `FragmentInstance` interface, and `submitter` on `SubmitEvent` are now stable, and the `ts5.0` fork is kept in sync. In `react-dom`, the `ViewTransitionPseudoElement` interface and the DOM-specific fields on `ViewTransitionInstance` and `FragmentInstance` move into the existing `declare module "react"` block in `index.d.ts`. `unstable_useCacheRefresh` stays in `react/canary`; both canary entrypoints remain so existing `react/canary` and `react-dom/canary` references keep resolving, with `react-dom/canary` reduced to an empty shell. Tests move from the canary test files into the stable test files, and the stale "Only passes because program includes React Canary types" comment in `formrelatedEventTests` is replaced with a real `$ExpectType` assertion. Finally, the package versions are bumped to match the React 19.3 prerelease version bump (react/react#34674): `@types/react`, `@types/react-dom`, `@types/react-is`, and `@types/react-test-renderer` to 19.3.9999, `@types/scheduler` to 0.28.9999, `@types/use-sync-external-store` to 1.7.9999, `@types/react-refresh` to 0.19.9999, and `@types/use-subscription` to 1.13.9999, and the `@types/react-dom` peer dependency floor on `@types/react` is raised to `^19.3.0`. The `react-refresh` types are also brought up to date with the runtime: `findAffectedHostInstances`, removed from the runtime in react-refresh 0.15, is dropped along with its `Instance` type, and the exported `_getMountedRootCount` is added.

Co-Authored-By: Claude Code (kimi-k3[1m]) <noreply@anthropic.com>
```
