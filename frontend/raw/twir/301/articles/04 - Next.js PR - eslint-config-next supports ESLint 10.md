---
type: twir-item
issue: 301
item: 4
item_type: item
date: 2026-10-14
source: https://github.com/vercel/next.js/pull/99628
tags:
  - "Nextjs"
  - "TS"
  - "PR"
  - "ESLint"
  - "10"
status: auto
quality: keep
---

[[2026-10-14-TWIR-301|Index]]

# Item 4: Next.js PR - eslint-config-next supports ESLint 10

Source: [https://github.com/vercel/next.js/pull/99628](https://github.com/vercel/next.js/pull/99628)

Summary:
The Next.js ESLint config now supports both ESLint 9 and 10, addressing crashes and compatibility issues with newer Node.js and plugin versions. The update includes patches for plugins that haven’t yet officially adopted ESLint 10, ensuring smooth upgrades for Next.js users, along with new tests and documentation. Some peer dependency warnings remain until upstream plugins are updated, but linting works as expected.

Key takeaways:
- Next.js users can safely upgrade to ESLint 10 without breaking linting or raising Node.js minimums.
- Patches restore compatibility for key plugins (react, import, babel parser) pending official updates.
- New tests verify consistent linting across JS/TS projects and ESLint versions.
- Some peer warnings persist, but are non-blocking unless strict peer deps are enforced.

Recommendation:
Summary sufficient (read PR if you maintain tooling or have custom ESLint setups)

Why it matters:
read PR if you maintain tooling or have custom ESLint setups

Content:
# support ESLint 10 by jamiboym · Pull Request #99628 · vercel/next.js · GitHub

```
- Add `addGlobals()` to the bundled Babel parser's scope manager, which
  ESLint 10 calls to register configured and inline globals.
- Restore the rule context members ESLint 10 removed for
  eslint-plugin-react and eslint-plugin-import, patching rules in place so
  the plugin objects keep their identity.
- Raise eslint-plugin-react-hooks to ^7.1.0 and typescript-eslint to
  ^8.56.0, the first versions that support ESLint 10.
- Lint JavaScript and TypeScript fixture apps with ESLint 9 and 10 in an
  isolated install.
```

```
test/.gitignore ignores production/**/tsconfig.json, so the TypeScript
fixture's path alias config was missing in CI. Also removes the temporary
CI debug output.
```

```
eslint-plugin-import looks up resolvers by name from the linted file. With
ESLint 10, npm nests eslint-plugin-import and eslint-import-resolver-typescript
under eslint-config-next because of the plugins' ESLint peer ranges, so the
lookup falls back to the `typescript` package and fails. Resolving the paths
from eslint-config-next, as it did before the flat config rewrite, works
regardless of the install layout.
```

```
ESLint 9 reached end-of-life on 2026-08-06 (eslint.org/version-support)
and gets no more fixes, security fixes included; npm already flags
eslint@9.39.5 as unsupported on every install. This moves eslint ^9 ->
^10.12.0 (9.39.5 -> 10.12.0) and eslint-config-next ^16.3.8 -> ^16.4.0.
next and @next/third-parties stay at 16.3.8.

It supersedes Dependabot's #285 and its replacement #301, which bump
only eslint and can't pass. ESLint 10 requires every scope manager to
implement addGlobals(), and eslint-config-next before 16.4.0 parses JS
with the @babel/eslint-parser 7 bundled in next, which lacks it, so
lint dies with "TypeError: scopeManager.addGlobals is not a function"
(exit 2) before reporting anything. That still holds today: eslint
10.12.0 with eslint-config-next 16.3.8 crashes the same way. 16.4.0
(vercel/next.js#99628) wraps that parser with an addGlobals() shim and
restores the rule-context methods ESLint 10 removed (getFilename,
getSourceCode, parserOptions, ...) for eslint-plugin-react and
eslint-plugin-import. It still takes the parser from next, and works
with next 16.3.8's copy.

Every install, npm ci included, prints three "npm warn ERESOLVE
overriding peer dependency" warnings: eslint-plugin-import 2.32.0,
eslint-plugin-jsx-a11y 6.10.2 and eslint-plugin-react 7.37.5 don't list
ESLint 10 in their peer ranges yet. They are only warnings. Don't
silence them with overrides, --legacy-peer-deps or an .npmrc (legacy
mode drops the auto-installed typescript peer and the config then fails
to load), and don't add the plugins as direct dependencies (npm then
fails with ERESOLVE). npm nests the three under eslint-config-next, and
`npm ls eslint` now exits 1 with "invalid: eslint@10.12.0"; neither CI
nor the deploy runs npm ls. The warnings clear once eslint-plugin-import
releases its merged ESLint 10 support
(import-js/eslint-plugin-import#3278), eslint-plugin-react ships
jsx-eslint/eslint-plugin-react#4022 and eslint-plugin-jsx-a11y merges
jsx-eslint/eslint-plugin-jsx-a11y#1081.

Until then, don't enable import/order or react/jsx-curly-spacing,
jsx-equals-spacing, jsx-tag-spacing, jsx-space-before-closing or
jsx-one-expression-per-line. They call SourceCode methods ESLint 10
removed (getTokenOrCommentBefore, isSpaceBetweenTokens), which
eslint-config-next doesn't restore, so they crash. None is enabled now.
eslint-plugin-react also calls the removed getJSDocComment and swallows
the error, so a JSDoc @extends or @Augments React.Component tag no
longer makes a class a component; only a real extends Component or
PureComponent (React.* included) does. react/display-name,
no-deprecated, no-direct-mutation-state and require-render-return
therefore skip classes that are components only through JSDoc. src/
has none, and jsx-eslint/eslint-plugin-react#4022 fixes it. ESLint 10
also turns /* eslint-env */ comments into errors (src/ has none; use
/* global */) and needs Node ^20.19, ^22.13 or >=24.

Drop the devDependency @eslint/eslintrc. Nothing imports it
(eslint.config.mjs spreads eslint-config-next's flat config and doesn't
use FlatCompat), and ESLint 10 neither supports eslintrc nor depends on
it. The js-yaml override stays: it now reaches only @lhci/utils, and
without it argparse 1 and sprintf-js 1.0.3 (GHSA-hp3w-g68c-fv3c,
moderate, no fix) come back.

Lint results on src/ don't change. With the repo's eslint.config.mjs,
ESLint 9.39.5 + eslint-config-next 16.3.8 and ESLint 10.12.0 + 16.4.0
both report 0 problems on src/, and the same 79 problems (40 errors, 39
warnings; identical file, line, column, rule, severity and message) on
an out-of-repo fixture project written to trip 57 of the 62 enabled
rules, through both the Babel and the TypeScript parser. Run one at a
time, the 373 rules of the six plugins in the config, plus 20
scope-sensitive core rules that exercise the addGlobals shim, give
identical results apart from the six crashing rules and the JSDoc-only
class components, both described above.

Lockfile: eslint 9 -> 10 is the only major for a direct dependency. The
other majors are eslint's own dependencies and reachable only from it:
eslint-scope 9, espree 11, @eslint/core 1, @eslint/plugin-kit 0.7,
@eslint/config-helpers 0.7 and file-entry-cache 11 (with flat-cache 6,
keyv 5 and a new cacheable/hookified/qified chain). eslint-visitor-keys
5 sits at the root, where typescript-eslint's visitor-keys shares it,
and acorn moves 8.18.0 -> 8.19.0 with espree. @eslint/js, chalk 4,
lodash.merge and @eslint/eslintrc's subtree drop out, and eslint now
uses the root @eslint/config-array 0.23.5 instead of a nested 0.21.2.
@next/eslint-plugin-next follows to 16.4.0, and
string.prototype.matchall 4.1.0 and two wasm-only packages npm doesn't
install on x64 ride along within range. npm 11.17.0 also records libc
on the @unrs/resolver-binding-* entries, so npm ci on glibc no longer
installs the unused musl binding. Every non-dev entry is unchanged, the
static export is byte-identical apart from the build ID, and npm audit
is unchanged (the allowlisted braces advisory only).

Rebased onto React 19 and Mantine 9 (#294) and regenerated on top of
its lockfile under Node 24 / npm 11.17.0; a second npm install leaves
it byte-identical, and so does npm 11.19.0, which CI now runs. From
scratch, npm ci reproduces the tree, and npm run audit:ci, npm run lint
and npm run build pass.
```

```
ESLint 9 reached end-of-life on 2026-08-06 (eslint.org/version-support)
and gets no more fixes, security fixes included; npm already flags
eslint@9.39.5 as unsupported on every install. This moves eslint ^9 ->
^10.12.0 (9.39.5 -> 10.12.0) and eslint-config-next ^16.3.8 -> ^16.4.0.
next and @next/third-parties stay at 16.3.8.

It supersedes Dependabot's #285 and its replacement #301, which bump
only eslint and can't pass. ESLint 10 requires every scope manager to
implement addGlobals(), and eslint-config-next before 16.4.0 parses JS
with the @babel/eslint-parser 7 bundled in next, which lacks it, so
lint dies with "TypeError: scopeManager.addGlobals is not a function"
(exit 2) before reporting anything. That still holds today: eslint
10.12.0 with eslint-config-next 16.3.8 crashes the same way. 16.4.0
(vercel/next.js#99628) wraps that parser with an addGlobals() shim and
restores the rule-context methods ESLint 10 removed (getFilename,
getSourceCode, parserOptions, ...) for eslint-plugin-react and
eslint-plugin-import. It still takes the parser from next, and works
with next 16.3.8's copy.

Every install, npm ci included, prints three "npm warn ERESOLVE
overriding peer dependency" warnings: eslint-plugin-import 2.32.0,
eslint-plugin-jsx-a11y 6.10.2 and eslint-plugin-react 7.37.5 don't list
ESLint 10 in their peer ranges yet. They are only warnings. Don't
silence them with overrides, --legacy-peer-deps or an .npmrc (legacy
mode drops the auto-installed typescript peer and the config then fails
to load), and don't add the plugins as direct dependencies (npm then
fails with ERESOLVE). npm nests the three under eslint-config-next, and
`npm ls eslint` now exits 1 with "invalid: eslint@10.12.0"; neither CI
nor the deploy runs npm ls. The warnings clear once eslint-plugin-import
releases its merged ESLint 10 support
(import-js/eslint-plugin-import#3278), eslint-plugin-react ships
jsx-eslint/eslint-plugin-react#4022 and eslint-plugin-jsx-a11y merges
jsx-eslint/eslint-plugin-jsx-a11y#1081.

Until then, don't enable import/order or react/jsx-curly-spacing,
jsx-equals-spacing, jsx-tag-spacing, jsx-space-before-closing or
jsx-one-expression-per-line. They call SourceCode methods ESLint 10
removed (getTokenOrCommentBefore, isSpaceBetweenTokens), which
eslint-config-next doesn't restore, so they crash. None is enabled now.
eslint-plugin-react also calls the removed getJSDocComment and swallows
the error, so a JSDoc @extends or @Augments React.Component tag no
longer makes a class a component; only a real extends Component or
PureComponent (React.* included) does. react/display-name,
no-deprecated, no-direct-mutation-state and require-render-return
therefore skip classes that are components only through JSDoc. src/
has none, and jsx-eslint/eslint-plugin-react#4022 fixes it. ESLint 10
also turns /* eslint-env */ comments into errors (src/ has none; use
/* global */) and needs Node ^20.19, ^22.13 or >=24.

Drop the devDependency @eslint/eslintrc. Nothing imports it
(eslint.config.mjs spreads eslint-config-next's flat config and doesn't
use FlatCompat), and ESLint 10 neither supports eslintrc nor depends on
it. The js-yaml override stays: it now reaches only @lhci/utils, and
without it argparse 1 and sprintf-js 1.0.3 (GHSA-hp3w-g68c-fv3c,
moderate, no fix) come back.

Lint results on src/ don't change. With the repo's eslint.config.mjs,
ESLint 9.39.5 + eslint-config-next 16.3.8 and ESLint 10.12.0 + 16.4.0
both report 0 problems on src/, and the same 79 problems (40 errors, 39
warnings; identical file, line, column, rule, severity and message) on
an out-of-repo fixture project written to trip 57 of the 62 enabled
rules, through both the Babel and the TypeScript parser. Run one at a
time, the 373 rules of the six plugins in the config, plus 20
scope-sensitive core rules that exercise the addGlobals shim, give
identical results apart from the six crashing rules and the JSDoc-only
class components, both described above.

Lockfile: eslint 9 -> 10 is the only major for a direct dependency. The
other majors are eslint's own dependencies and reachable only from it:
eslint-scope 9, espree 11, @eslint/core 1, @eslint/plugin-kit 0.7,
@eslint/config-helpers 0.7 and file-entry-cache 11 (with flat-cache 6,
keyv 5 and a new cacheable/hookified/qified chain). eslint-visitor-keys
5 sits at the root, where typescript-eslint's visitor-keys shares it,
and acorn moves 8.18.0 -> 8.19.0 with espree. @eslint/js, chalk 4,
lodash.merge and @eslint/eslintrc's subtree drop out, and eslint now
uses the root @eslint/config-array 0.23.5 instead of a nested 0.21.2.
@next/eslint-plugin-next follows to 16.4.0, and
string.prototype.matchall 4.1.0 and two wasm-only packages npm doesn't
install on x64 ride along within range. npm 11.17.0 also records libc
on the @unrs/resolver-binding-* entries, so npm ci on glibc no longer
installs the unused musl binding. Every non-dev entry is unchanged, the
static export is byte-identical apart from the build ID, and npm audit
is unchanged (the allowlisted braces advisory only).

Rebased onto React 19 and Mantine 9 (#294) and regenerated on top of
its lockfile under Node 24 / npm 11.17.0; a second npm install leaves
it byte-identical, and so does npm 11.19.0, which CI now runs. From
scratch, npm ci reproduces the tree, and npm run audit:ci, npm run lint
and npm run build pass.
```

```
* chore(deps): upgrade eslint to 10

- eslint-config-next 16.4 supports ESLint 10 (vercel/next.js#99628). It patches
  eslint-plugin-react, eslint-plugin-import and the Babel parser for the removed APIs.
- eslint-plugin-react, eslint-plugin-import and eslint-plugin-jsx-a11y do not list
  ESLint 10 as a peer yet. npm warns and installs them; lint output is the same.
- eslint.config.mjs needs no change.

Closes #178

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

* docs(lint): note ESLint 10 support and the expected peer warnings

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

---------

Co-authored-by: Claude Opus 5.5 <noreply@anthropic.com>
```

```
…ore を外す (#569)

eslint-config-next 16.4.0（vercel/next.js#99628）が、ESLint 10 で削除された
rule context のメンバーを eslint-plugin-react / eslint-plugin-import に戻す互換処理
（fixupPluginRules）を持つため、eslint 10.12.0 で lint 結果が eslint 9 と一致する。
2026-10-13 の Dependency Unblock Check で UNBLOCKED（exit 10）になっていた。

- frontend の eslint を ^9 から ^10.12.0 に上げ、package-lock.json を更新する
- .github/dependabot.yml の /frontend の eslint ignore とコメントを削除する
- scripts/ci/dependabot-unblock.json の /frontend の eslint エントリを削除する

eslint-plugin-react / eslint-plugin-import / eslint-plugin-jsx-a11y の peer は
まだ eslint 10 を含まないため、install 時の ERESOLVE 警告と npm ls --all の
exit 1 は残る。peer 不一致の解消は #427 で追跡を続ける。

Refs #568
Refs #427

Claude-Session: https://claude.ai/code/session_01PPszW4Rvm6ppEAvUWbRP6j

Co-authored-by: Claude Opus 5.5 <noreply@anthropic.com>
```
