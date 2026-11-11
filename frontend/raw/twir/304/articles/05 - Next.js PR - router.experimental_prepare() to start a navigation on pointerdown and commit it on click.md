---
type: twir-item
issue: 304
item: 5
item_type: item
date: 2026-11-04
source: https://github.com/vercel/next.js/pull/101050
tags:
  - "Nextjs"
  - "PR"
  - "routerexperimental_prepare"
status: auto
quality: keep
---

[[2026-11-04-TWIR-304|Index]]

# Item 5: Next.js PR - router.experimental_prepare() to start a navigation on pointerdown and commit it on click

Source: [https://github.com/vercel/next.js/pull/101050](https://github.com/vercel/next.js/pull/101050)

Summary:
This PR introduces an experimental_prepare(href) API to Next.js's router, allowing navigation to be prepared on pointerdown and committed on click. The approach starts the dynamic request earlier, potentially improving perceived navigation speed. The prepared data is cached and only committed when the user completes the action, with clear semantics around cache invalidation and usage.

Key takeaways:
- Enables preloading navigation data before user confirmation, reducing latency.
- Prepared data is reused if committed, but not for regular navigations.
- API is experimental and gated behind a feature flag.
- Designed for advanced usage; may be integrated into Link in the future.

Recommendation:
Read fully (read fully if you are experimenting with navigation performance optimizations)

Why it matters:
read fully if you are experimenting with navigation performance optimizations

Content:
# Add router.experimental_prepare() by acdlite · Pull Request #101050 · vercel/next.js · GitHub

```
The review agent escalated #101043 (and the identical #101050) to a
human even though the feature is fully gated behind a new experimental
flag. Three rules added up:

- Adding a gate condition for the new flag to test/lib/gate/conditions.ts
  counted as a shared-test-infra change.
  trigger, as a placeholder until a separate proposal.
- Flag-gated code that ships in the client runtime counted as page
  weight, which app-router-client makes strong.

This changes each of them:

- A new gate condition that only reads a new experimental flag is part
  of the PR's own tests, not shared test infra. Changing how gate/
  evaluates conditions still escalates.
- A new feature fully gated behind a new experimental flag, wired per
  flags-wired-end-to-end, doesn't count as a change to public APIs or
  behaviors. Its code is still reviewed like any other change, and what
  changes with the flag off still counts.
- Code behind an experimental flag that, with the flag off, never runs,
  sends nothing extra, and adds no fields is a comment, not an
  escalation, in every area. The comment suggests gating it on the
  flag's compile-time env so it's dead-code eliminated, since otherwise
  every experiment ships to every app until it graduates.
```

```
The review agent escalated #101043 (and the identical #101050) to a
human largely because the PR adds a feature behind a new experimental
flag. Two rules contributed:

  trigger, as a placeholder until a separate proposal.
- Adding a gate condition for the new flag to test/lib/gate/conditions.ts
  counted as a shared-test-infra change.

This changes both:

- A new feature fully gated behind a new experimental flag, wired per
  flags-wired-end-to-end, doesn't count as adding to the public API
  surface. That's the only pass the flag gives. Everything else is
  reviewed as if the flag weren't there, and rule violations behind it
  escalate the same as anywhere else.
- A new gate condition that only reads a new experimental flag is part
  of the PR's own tests, not shared test infra. Changing how gate/
  evaluates conditions still escalates.
```

```
…01051)

The review agent escalated #101043 (and the identical #101050) to a
human largely because the PR adds a feature behind a new experimental
flag. Two rules contributed:

trigger, as a placeholder until a separate proposal.
- Adding a gate condition for the new flag to
`test/lib/gate/conditions.ts` counted as a shared-test-infra change.

This changes both:

- A new feature fully gated behind a new experimental flag, wired per
`flags-wired-end-to-end`, doesn't count as adding to the public API
surface. That's the only pass the flag gives. Everything else is
reviewed as if the flag weren't there, and rule violations behind it
escalate the same as anywhere else.
- A new gate condition that only reads a new experimental flag is part
of the PR's own tests, not shared test infra. Changing how `gate/`
evaluates conditions still escalates.
```

```
Adds `experimental_prepare(href)` to the router returned by `useRouter()`. It
starts a navigation that goes through all the same steps as a regular one,
including the dynamic request, but doesn't update the router. The response
writes into the same local cache used by back/forward navigations.

The returned handle has `push()` and `replace()`. Committing performs a
regular navigation, except it can read bfcache entries written since the
prepare began, regardless of stale time. If the prepared request is still in
flight, the commit reuses it instead of starting a new one.

The intended use is to prepare on pointerdown and commit on click, which
starts the dynamic request earlier. We may build this into Link eventually;
the low-level API lets people try it out first.

Semantics:

- If you don't commit, nothing else happens. The data stays in the bfcache,
  so a history traversal to an overlapping segment may observe it. This is
  intentional. The contract of the API is that you are OK with the navigation
  showing data that's as stale as when the preparation began.
- Prepared data doesn't expire. Committing much later still reuses it; the
  caller is responsible for not holding on to a handle too long.
- A refresh or server action between prepare and commit invalidates the
  prepared data, the same way it invalidates the bfcache.
- A handle can only be committed once. Later calls are a no-op, with a
  dev-only warning.
- A regular navigation to the same route doesn't reuse prepared data; only
  the commit ignores stale time.

Gated behind `experimental.prepareNavigation`.
```
