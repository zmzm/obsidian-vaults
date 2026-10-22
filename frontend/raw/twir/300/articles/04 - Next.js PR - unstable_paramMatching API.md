---
type: twir-item
issue: 300
item: 4
item_type: item
date: 2026-10-07
source: https://github.com/vercel/next.js/pull/97393
tags:
  - "Nextjs"
  - "PR"
  - "API"
status: auto
quality: keep
---

[[2026-10-07-TWIR-300|Index]]

# Item 4: Next.js PR - unstable_paramMatching API

Source: [https://github.com/vercel/next.js/pull/97393](https://github.com/vercel/next.js/pull/97393)

Summary:
A new Next.js pull request introduces the unstable_paramMatching and unstable_generateParamMatching APIs, allowing parameter matching to be configured separately from build-time prerenders in Cache Components apps. These APIs let developers specify how route parameters behave (e.g., 404, blocking, fallback, dynamic) at a granular level, improving control over static and dynamic route handling. The PR also details policy merging, validation, and integration with ensureStatic, along with comprehensive test coverage and performance metrics.

Key takeaways:
- New APIs enable fine-grained control over route parameter matching, independent of static param generation.
- Developers can specify per-parameter behaviors (not-found, blocking, fallback, dynamic) for more predictable routing.
- Policies merge from layouts to pages, with explicit override rules and validation.
- Extensive tests and performance metrics included; some regressions and improvements noted.

Recommendation:
Read fully (important for teams building advanced routing or static/dynamic hybrid apps in Next.js)

Why it matters:
important for teams building advanced routing or static/dynamic hybrid apps in Next.js

Content:
# Add unstable parameter matching APIs by gnoff · Pull Request #97393 · vercel/next.js · GitHub

```
## Summary

This is the behavior-preserving base of a four-PR stack that introduces
explicit prerender matching policy without coupling the foundational
refactor to the proposed API.

The build currently uses `PrerenderedRoute` values for two related but
distinct concepts:

- a logical request matcher that says which parameterized URL shapes the
route can handle
- a build-time render candidate that may or may not become a persisted
prerender artifact

A candidate is not guaranteed to be an output. It can be rendered only
to validate a shell, discarded, and still leave behind a matcher that
tells future requests to block.

The new relationship is:

```text
logical pathname matcher
  -> zero or more render candidates
    -> zero or more persisted artifacts
```

## Concrete example

Consider `/[top]/items/[bottom]`:

```ts
export function generateStaticParams() {
  return [{ top: 't1', bottom: 'b1' }]
}
```

Static-path generation may consider three shapes:

| Shape | Purpose |
| --- | --- |
| `/[top]/items/[bottom]` | A generic shell candidate and logical
matcher |
| `/t1/items/[bottom]` | A shell after resolving `top` |
| `/t1/items/b1` | A concrete build-time prerender |

Suppose the generic candidate renders an allowed empty shell. The build
should discard that candidate artifact and use blocking behavior for the
generic matcher. It should not remove `/[top]/items/[bottom]` from the
valid matcher set, and it should not discard the concrete `/t1/items/b1`
artifact.

This is why the build needs two sets:

- route matchers, which describe valid request shapes
- prerender candidates, whose render results determine whether an
artifact is retained and can refine inferred fallback behavior

## Variants compatibility

Variants will make pathname-only candidate maps insufficient. Several
variant combinations can share `/t1/items/b1` as their logical pathname
while writing distinct artifacts under variant-specific output paths.

This PR keeps the route matcher keyed by logical pathname but retains
every candidate associated with it. Candidate finalization can therefore
evaluate each variant artifact independently without changing the route
tree's matcher set.

## Behavior preservation

This PR does not add a user-facing API or change `generateStaticParams`
semantics:

- a usable static shell remains a fallback prerender
- an allowed empty shell is discarded and represented by a blocking
matcher
- a route that requires a non-empty shell still fails validation
- unresolved matchers remain gated by route-level PPR support
- the most-specific shell continues to supply first-writer-wins metadata
such as prefetch hints

Render results can decide whether a candidate artifact is published and
can refine inferred matcher behavior, but they do not remove the logical
route matcher itself.

## Stack plan

1. **#97431 — model prerenders as render candidates:** land the
behavior-preserving matcher/candidate separation and post-render
finalization first.
2. **#97393 — add the experimental matcher API:** add `unstable_matcher`
and `unstable_generateMatcher`, policy aggregation, validation, and
local diagnostics.
3. **#97426 — test complex route shapes:** add test-only coverage for
catch-alls, optional catch-alls, root parameters, and parallel slots.
4. **#97427 — test foreground policy behavior:** add test-only coverage
showing blocking misses generate before responding while fallback misses
return the shared shell immediately.

This layering lets the internal model be reviewed and landed
independently of the API design. The upper test PRs validate the final
behavior without increasing the implementation diff.

## Verification

- `pnpm --filter=next types`
- `pnpm test-start-turbo
test/e2e/app-dir/sub-shell-generation/sub-shell-generation.test.ts`
- `pnpm test-start-turbo
test/e2e/app-dir/segment-cache/prefetch-inlining/prefetch-inlining.test.ts`

<!-- NEXT_JS_LLM -->
```

```
## Summary

Use structural React keys during server rendering so an HTML prerender
can resume without rewriting React's postponed state when route params
become known. Browser keys and router-cache identity are unchanged.

For example, `/products/[slug]` previously prerendered layout boundaries
with a key containing an opaque slug placeholder. Resuming
`/products/shoe` produced a different key, so Next.js substituted `shoe`
into the serialized React state before handing it back to React. Both
server passes now use `slug|d`. The browser still uses `slug|shoe|d`,
preserving template remounts and back/forward state behavior.

The server only renders the active entry at each layout-router position,
so it does not need parameter values to distinguish cached browser
entries. React keys are not embedded in the HTML; hydration derives its
concrete keys from the request's route state.

- Use segment name/type for server layout keys and structural route
paths for the server head key. Server keys always omit search params.
The existing browser-module variant mechanism selects the concrete key
implementation for browser bundles in both Webpack and Turbopack.
- Remove placeholder substitution and the request-params argument from
postponed-state parsing. Persist only fallback param names for render
staging; React's postponed state no longer needs to be searched or
rewritten.
- Simplify the remaining opaque fallback map to param name →
placeholder. Its dynamic-param type slot is unused after removing
interpolation. Parameter wrappers still control suspension; this does
not make unknown params available to application code.
- Test server and browser keys directly, including catch-all/intercepted
segments and search params. Update the action-only resume fixture's
single assertion on the resume-metadata format so its three cases reach
their behavioral checks for action execution, revalidation, and
`notFound()` with names-only metadata.

This refactor is independently landable against `canary` and is now the
base of the parameter-matching stack: #98944 → #98891 → #98892 → #98893
→ #97393. It supersedes #98890. It retains internal opaque placeholders
but removes their role in matching React's postponed state. No new
integration fixtures are needed.

## Verification

Latest cleanup:

- 126 focused unit tests and 4 snapshots pass in both default and Cache
Components/Webpack configurations.
- 34 production Webpack tests pass across `fallback-shells`,
`partial-fallback-shell-upgrade`,
`action-only-fallback-resume-data-cache`, and
`resuming-head-runtime-search-param`; 4 existing tests remain skipped.
The three action-only resume cases now reach and pass their behavioral
assertions.

Earlier commits also passed existing production and dev Webpack coverage
for back/forward state, template remounts, base-path params,
nested/parallel/intercepted routes, form-state hydration, and
standalone/edge output.

A reviewer verified this head under Turbopack using a native binary
built from the same commit: a broader unit selection passed (144 tests,
the focused set above plus the remaining router-reducer suites), the
`packages/next` type check was clean, and 33 production e2e tests passed
across `fallback-shells`, `partial-fallback-shell-upgrade`, and
`action-only-fallback-resume-data-cache`.

<!-- NEXT_JS_LLM -->
```

```
Add the complete parameter-matching implementation across static generation, route composition, and runtime validation. Support per-parameter not-found, blocking, fallback, and dynamic policies; compose layout and page generators; and preserve generateStaticParams samples for matching. Wire inference, validation, development diagnostics, type generation, and comprehensive fixture coverage.

Consolidate the reviewed API implementation while excluding prerequisite changes already present in the base. This changes history only; the implementation tree is preserved.
```

```
Expose unstable_paramMatching and unstable_generateParamMatching without an experimental.paramMatching config opt-in. Cache Components remains required.

Update collection, diagnostics, type generation, and fixture coverage to use the unstable exports. Retain the parameter-matching debug switch.

Verification: full post-rebase JavaScript and native builds pass. Focused tests and types passed before rebase; additional post-rebase checks are being run by the parent.
```

```
…t behavior

Use PrefetchHint constants instead of stale bit positions and expect the dedicated build-time generator revalidation diagnostic. Keep admitted prefetches successful without requiring a particular partition of the RSC payload across transport requests.

Verify root-dependent content remains isolated across IT, NL, and IT requests after invalidation, while reserving generic-shell markup assertions for self-hosted production. Deployment adapters may key the shell on a concrete root value.

For the dynamic-tail deployment regression, wait for both suffixes to share a stable shell before and after a single invalidation. Vercel can initially treat a new shell as stale. Retry only generation stability; routing failures and incorrect parameter values still fail immediately. Self-hosted assertions remain unchanged.

Verified with focused generator, diagnostic, routing, and root-parameter tests; the final dynamic-tail test passes with production Turbopack and Webpack. Repository TypeScript and changed-file lint pass. The deployment-only stabilization path still needs deployment CI.
```

```
Use the decoded rewrite destination when selecting prerendered outputs and route matchers in dev, matching the production pathname convention. The original encoded URL rejected generated values such as "hello world" and valid rewrite aliases. Conversely, a rewrite from an allowed language to an excluded language could be admitted using the original prefix.

Reuse decodePathParams once for both matching loops without changing application-visible parameter values or production rendering. Add eleven regression cases covering spaces, literal percent sequences, rewrites, and rejection of unlisted destinations and double-encoded values.

Eight new cases fail in dev before the fix while all eleven pass in production. The complete routing fixture passes in dev and production with both Turbopack and Webpack after the fix. Repository TypeScript, lint, formatting, and the full bootstrap build also pass.
```

```
Evaluate matching configuration per declaring route module without sharing AppSegment objects across parallel branches. Re-exporting a common generator does not make its declaring modules the same module. Preserve the existing flat-list deduplication used by generateStaticParams.

Remove the synthetic segment-tree helper and redundant resolver unit tests. Keep existing end-to-end coverage for inheritance, matching order, and dynamic-param validation, and add real fixtures for the remaining cases:

- A page replaces an inherited lang fallback with not-found before the effective policy is validated.
- Parallel branches separately configure top as fallback and bottom as blocking, making their combined policy invalid.
- A child cannot silently close an explicitly blocking ancestor by configuring a later parameter as not-found.
- A sidebar catch-all configures parts, but the selected /[slug] matcher has no parts parameter. This exercises the route-key guard through real module collection rather than injecting an impossible unknown key.

Retain a focused concurrency test that waits for the child generator to start while its parent is pending, without requiring synchronous startup. The intentionally invalid catch-all fixture runs in dev and build, not deployment.

Verified with 87 unit tests, focused development and production fixtures under Turbopack and webpack, repository type checking and lint, and pnpm build-all.
```

```
Keep the newly landed ensureStatic navigation guarantee intact when routes configure parameter matching. Reject effective fallback and dynamic policies in both builds and development, including inherited, generated, and parallel-slot configurations; fallback support can be added separately.

Retain blocking and not-found matching, complete generateStaticParams requirements, and static validation even with instant=false. Preserve the generic prefetch render and specialized matchers beneath closed prefixes without producing intermediate navigation fallbacks.

Add real fixtures covering valid and invalid combinations, client navigation, cache reuse, and build artifacts with Partial Prefetching on and off. Update generator diagnostics for the renamed navigation and prefetch helpers.
```

```
The landed Draft Mode fix admits closed-route previews using the build-specific bypass cookie without requiring legacy preview data. Update the parameter matching regression to assert that contract while retaining the closed-prefix, open-suffix, and document/RSC/segment routing checks. No parameter matching runtime behavior changes.
```
