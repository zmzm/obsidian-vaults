---
type: twir-item
issue: 296
item: 4
item_type: item
date: 2026-09-09
source: https://github.com/reactjs/react.dev/pull/8632
tags:
  - "Reactdev"
  - "PR"
  - "SSR"
status: auto
quality: keep
---

[[2026-09-09-TWIR-296|Index]]

# Item 4: React.dev PR - Document missing SSR and hydration options

Source: [https://github.com/reactjs/react.dev/pull/8632](https://github.com/reactjs/react.dev/pull/8632)

Summary:
This documentation update adds missing options for server-side rendering (SSR) and hydration APIs in React, including formState, importMap, onHeaders, maxHeadersLength, and improved nonce handling. It clarifies the behavior of hydrateRoot and various render/prerender methods, ensuring that all stable options are now documented. The update also corrects references and removes outdated experimental badges.

Key takeaways:
- hydrateRoot and server render APIs now have documented support for formState, improving SSR form handling.
- Additional SSR options (importMap, onHeaders, maxHeadersLength, nonce) are now officially documented.
- Documentation now accurately reflects stable API surface and corrects naming/reference errors.
- No functional changes—this is a documentation catch-up for features already in stable releases.

Recommendation:
Read fully (read fully if you need to leverage advanced SSR/hydration options or maintain documentation)

Why it matters:
read fully if you need to leverage advanced SSR/hydration options or maintain documentation

Content:
# Document missing react-dom server rendering and hydration options by eps1lon · Pull Request #8632 · reactjs/react.dev · GitHub

```
This adds the `formState`, `importMap`, `onHeaders`, and `maxHeadersLength` options to the `renderToPipeableStream` and `renderToReadableStream` reference pages, documents the object form of `nonce` for separate script and style nonces, and adds `importMap`, `onHeaders`, and `maxHeadersLength` to the `prerender` and `prerenderToNodeStream` pages. All of these options are supported in stable releases but were never documented. The `resumeAndPrerender` entries on the `react-dom/static` index were marked as experimental-only even though they ship in stable releases, so the badge is removed, and the `resumeAndPrerender` intro destructured a `postpone` property that is actually called `postponed`.

The `resumeToPipeableStream` page no longer documents a `signal` option because the Node.js implementation neither types nor reads it, and it now documents the `onAllReady` callback that the implementation does support. The same page referred to `resume` in its intro and Returns section where it meant `resumeToPipeableStream`, and the `react-dom/server` index linked both resume entries to the `renderToPipeableStream` page; they now point at their own pages.

Co-Authored-By: Claude Code (kimi-k3[1m]) <noreply@anthropic.com>
```

```
This adds the `formState` option to the `hydrateRoot` reference. The option carries the form state produced by a Server Function form submission so that `useActionState` with a `permalink` returns the submitted state during hydration instead of the initial state, and it must match the `formState` passed to the server renderer. The option shipped in React 19.0 but was never documented.

Co-Authored-By: Claude Code (kimi-k3[1m]) <noreply@anthropic.com>
```
