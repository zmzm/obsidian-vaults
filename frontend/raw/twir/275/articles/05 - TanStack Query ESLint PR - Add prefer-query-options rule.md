---
type: twir-item
issue: 275
item: 5
item_type: item
date: 2026-04-01
source: https://github.com/TanStack/query/pull/10359
tags:
status: auto
---

[[2026-04-01-TWIR-275|Index]]

# Item 5: TanStack Query ESLint PR - Add prefer-query-options rule

Source: [https://github.com/TanStack/query/pull/10359](https://github.com/TanStack/query/pull/10359)

Content:
# feat(eslint-plugin-query): add prefer-query-options rule by Newbie012 · Pull Request #10359 · TanStack/query

[![@Newbie012](https://avatars.githubusercontent.com/u/10504365?s=80&v=4)](https://github.com/Newbie012)

[![@Newbie012](https://avatars.githubusercontent.com/u/10504365?s=40&v=4)](https://github.com/Newbie012)

[![@Newbie012](https://avatars.githubusercontent.com/u/10504365?s=40&v=4)](https://github.com/Newbie012)

[![@coderabbitai](https://avatars.githubusercontent.com/in/347564?s=80&v=4)](https://github.com/apps/coderabbitai)

📝 Walkthrough

## Walkthrough

Adds a new ESLint rule `prefer-query-options` with implementation, tests, docs, demo examples, a changeset, and new plugin exports/configs (`recommendedStrict` and `flat/recommended-strict`) to enable the rule.

## Changes

| Cohort / File(s) | Summary |
| --- | --- |
| **Release Metadata**
`\.changeset/prefer-query-options-rule.md` | New changeset declaring a minor bump for `@tanstack/eslint-plugin-query` and announcing `prefer-query-options` and `recommendedStrict`. |
| **Documentation**
`docs/config.json`, `docs/eslint/eslint-plugin-query.md`, `docs/eslint/prefer-query-options.md` | Added nav entry and docs: new "Prefer Query Options" rule page, and "recommended strict" config docs for flat and legacy ESLint usage. |
| **Rule Implementation**
`packages/eslint-plugin-query/src/rules/prefer-query-options/prefer-query-options.rule.ts` | New ESLint rule detecting inline `queryKey`/`queryFn` in hooks, useQueries variants (including mapped returns), useIsFetching, and QueryClient calls; reports usage that should use `queryOptions()`/`infiniteQueryOptions()`. |
| **Rule Registration & Plugin Exports**
`packages/eslint-plugin-query/src/rules.ts`, `packages/eslint-plugin-query/src/index.ts` | Registered the new rule; added `recommendedStrict` and `flat/recommended-strict` configs and corresponding Plugin interface entries; factored recommended rules into shared constants. |
| **Tests**
`packages/eslint-plugin-query/src/__tests__/prefer-query-options.test.ts` | Comprehensive RuleTester suite with allowed/forbidden cases across hooks, useQueries mappings, query client methods, edge cases, and expected messages/fixability. |
| **Examples / Demo**
`examples/react/eslint-plugin-demo/eslint.config.js`, `examples/react/eslint-plugin-demo/src/queries.tsx`, `examples/react/eslint-plugin-demo/src/prefer-query-options-demo.tsx` | Switched demo config to `flat/recommended-strict`; added `queries.tsx` exporting `queryOptions` builders and a demo `prefer-query-options-demo.tsx` showing compliant and lint-suppressed violating examples. |

## Estimated code review effort

🎯 4 (Complex) | ⏱️ ~45 minutes

## Poem

> 🐇 I hop through code and sniff each line,
>
> > Bundling keys and funcs so queries align.
> > No inline tangles, no mix-and-match fights,
> > Options bundled snugly — oh what delights!

🚥 Pre-merge checks | ✅ 2 | ❌ 1

### ❌ Failed checks (1 warning)

| Check name | Status | Explanation | Resolution |
| --- | --- | --- | --- |
| Docstring Coverage | ⚠️ Warning | Docstring coverage is 35.29% which is insufficient. The required threshold is 80.00%. | Write docstrings for the functions missing them to satisfy the coverage threshold. |

✅ Passed checks (2 passed)

| Check name | Status | Explanation |
| --- | --- | --- |
| Title check | ✅ Passed | The title accurately summarizes the main change: adding a new ESLint rule `prefer-query-options` to the eslint-plugin-query package. |
| Description check | ✅ Passed | The description comprehensively covers the changes, includes prior discussion context, provides clear examples of allowed and disallowed patterns, and confirms all checklist items are completed including testing and changeset creation. |

✏️ Tip: You can configure your own custom pre-merge checks in the settings.

✨ Finishing Touches 📝 Generate docstrings

-   Create stacked PR
-   Commit on current branch

🧪 Generate unit tests (beta)

-   Create PR with unit tests
-   Commit unit tests in branch `feat-eslint-prefer-query-options`

* * *

❤️ Share

-   [X](https://twitter.com/intent/tweet?text=I%20just%20used%20%40coderabbitai%20for%20my%20code%20review%2C%20and%20it%27s%20fantastic%21%20It%27s%20free%20for%20OSS%20and%20offers%20a%20free%20trial%20for%20the%20proprietary%20code.%20Check%20it%20out%3A&url=https%3A//coderabbit.ai)
-   [Mastodon](https://mastodon.social/share?text=I%20just%20used%20%40coderabbitai%20for%20my%20code%20review%2C%20and%20it%27s%20fantastic%21%20It%27s%20free%20for%20OSS%20and%20offers%20a%20free%20trial%20for%20the%20proprietary%20code.%20Check%20it%20out%3A%20https%3A%2F%2Fcoderabbit.ai)
-   [LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fcoderabbit.ai&mini=true&title=Great%20tool%20for%20code%20review%20-%20CodeRabbit&summary=I%20just%20used%20CodeRabbit%20for%20my%20code%20review%2C%20and%20it%27s%20fantastic%21%20It%27s%20free%20for%20OSS%20and%20offers%20a%20free%20trial%20for%20proprietary%20code)

Comment `@coderabbitai help` to get the list of available commands and usage tips.

[![@nx-cloud](https://avatars.githubusercontent.com/in/80458?s=80&v=4)](https://github.com/apps/nx-cloud)

| Command | Status | Duration | Result |
| --- | --- | --- | --- |

* * *

[![@github-actions](https://avatars.githubusercontent.com/in/15368?s=80&v=4)](https://github.com/apps/github-actions)

## 🚀 Changeset Version Preview

**1** package(s) bumped directly, **23** bumped as dependents.

### 🟨 Minor bumps

| Package | Version | Reason |
| --- | --- | --- |
| `@tanstack/eslint-plugin-query` | 5.95.2 → 5.96.0 | Changeset |
| `@tanstack/angular-query-experimental` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/angular-query-persist-client` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/preact-query` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/preact-query-devtools` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/preact-query-persist-client` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/query-async-storage-persister` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/query-broadcast-client-experimental` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/query-core` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/query-devtools` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/query-persist-client-core` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/query-sync-storage-persister` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/react-query` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/react-query-devtools` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/react-query-next-experimental` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/react-query-persist-client` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/solid-query` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/solid-query-devtools` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/solid-query-persist-client` | 5.95.2 → 5.96.0 | Dependent |
| `@tanstack/vue-query` | 5.95.2 → 5.96.0 | Dependent |

### 🟩 Patch bumps

| Package | Version | Reason |
| --- | --- | --- |
| `@tanstack/svelte-query` | 6.1.10 → 6.1.11 | Dependent |
| `@tanstack/svelte-query-devtools` | 6.1.10 → 6.1.11 | Dependent |
| `@tanstack/svelte-query-persist-client` | 6.1.10 → 6.1.11 | Dependent |
| `@tanstack/vue-query-devtools` | 6.1.10 → 6.1.11 | Dependent |

[![@autofix-ci](https://avatars.githubusercontent.com/in/243519?s=40&v=4)](https://github.com/marketplace/autofix-ci)

## Verified

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.

[![@github-actions](https://avatars.githubusercontent.com/in/15368?s=80&v=4)](https://github.com/apps/github-actions)

## size-limit report 📦

| Path | Size |
| --- | --- |
| react full | 11.98 KB (0%) |
| react minimal | 9.01 KB (0%) |

[![coderabbitai[bot]](https://avatars.githubusercontent.com/in/347564?s=60&v=4)](https://github.com/apps/coderabbitai)

[![@Newbie012](https://avatars.githubusercontent.com/u/10504365?s=40&v=4)](https://github.com/Newbie012)

[![@Newbie012](https://avatars.githubusercontent.com/u/10504365?s=40&v=4)](https://github.com/Newbie012)

…k/query into feat-eslint-prefer-query-options

[![coderabbitai[bot]](https://avatars.githubusercontent.com/in/347564?s=60&v=4)](https://github.com/apps/coderabbitai)

Comment on lines +78 to +94

<table data-tab-size="4" data-paste-markdown-skip=""><tbody><tr><td></td><td data-line-number="78"></td><td><span>function reportInlineQueryOptions(node: TSESTree.Node): void {</span></td></tr><tr><td></td><td data-line-number="79"></td><td><span>if (ASTUtils.isObjectExpression(node) &amp;&amp; hasInlineQueryOptions(node)) {</span></td></tr><tr><td></td><td data-line-number="80"></td><td><span>context.report({</span></td></tr><tr><td></td><td data-line-number="81"></td><td><span>node,</span></td></tr><tr><td></td><td data-line-number="82"></td><td><span>messageId: 'preferQueryOptions',</span></td></tr><tr><td></td><td data-line-number="83"></td><td><span>})</span></td></tr><tr><td></td><td data-line-number="84"></td><td><span>}</span></td></tr><tr><td></td><td data-line-number="85"></td><td><span>}</span></td></tr><tr><td></td><td data-line-number="86"></td><td><span><br></span></td></tr><tr><td></td><td data-line-number="87"></td><td><span>function reportInlineFilterQueryKey(node: TSESTree.Node): void {</span></td></tr><tr><td></td><td data-line-number="88"></td><td><span>if (ASTUtils.isObjectExpression(node) &amp;&amp; hasInlineFilterQueryKey(node)) {</span></td></tr><tr><td></td><td data-line-number="89"></td><td><span>context.report({</span></td></tr><tr><td></td><td data-line-number="90"></td><td><span>node,</span></td></tr><tr><td></td><td data-line-number="91"></td><td><span>messageId: 'preferQueryOptionsQueryKey',</span></td></tr><tr><td></td><td data-line-number="92"></td><td><span>})</span></td></tr><tr><td></td><td data-line-number="93"></td><td><span>}</span></td></tr><tr><td></td><td data-line-number="94"></td><td><span>}</span></td></tr></tbody></table>

[![TkDodo](https://avatars.githubusercontent.com/u/1021430?s=60&v=4)](https://github.com/TkDodo)

[![@Newbie012](https://avatars.githubusercontent.com/u/10504365?s=40&v=4)](https://github.com/Newbie012)

[![@Newbie012](https://avatars.githubusercontent.com/u/10504365?s=40&v=4)](https://github.com/Newbie012)

[![coderabbitai[bot]](https://avatars.githubusercontent.com/in/347564?s=60&v=4)](https://github.com/apps/coderabbitai)

[![@Newbie012](https://avatars.githubusercontent.com/u/10504365?s=40&v=4)](https://github.com/Newbie012)

## Verified

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.

[![@Newbie012](https://avatars.githubusercontent.com/u/10504365?s=40&v=4)](https://github.com/Newbie012) [Newbie012](https://github.com/Newbie012) deleted the feat-eslint-prefer-query-options branch

[March 31, 2026 10:13](https://github.com/TanStack/query/pull/10359#event-24069223475)

Merged

Closed

4 tasks

Key takeaways:
- No key takeaways extracted.

Recommendation: Summary sufficient
