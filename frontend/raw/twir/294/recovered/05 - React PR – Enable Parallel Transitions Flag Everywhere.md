---
type: "twir-recovery"
issue: 294
item: 5
source: "https://github.com/react/react/pull/37290"
final_url: "https://github.com/react/react/pull/37290"
retrieved: "2026-10-22T11:30:05+00:00"
original_note: "frontend/raw/twir/294/articles/05 - React PR \u2013 Enable Parallel Transitions Flag Everywhere.md"
editorial_review: "pending"
truncated: true
---

Original intake note: [[../articles/05 - React PR – Enable Parallel Transitions Flag Everywhere|React PR – Enable Parallel Transitions Flag Everywhere]]

# [flags] Enable enableParallelTransitions by acdlite · Pull Request #37290 · react/react · GitHub

## Conversation

```
Reverse #35709. Turn the flag on in the OSS/canary default and in every
hardcoded fork, including the native (RN) forks, and keep the test
renderers in sync. www stays GK-driven, so www.js and www-dynamic.js are
unchanged.

Leaving the flag in the repo for now; this just flips the default on.

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
```

Hide details
View details

[github-actions](/apps/github-actions) Bot
pushed a commit
that referenced
this pull request
[Aug 14, 2026](#ref-commit-7032932)

```
Reverse #35709. Turn the flag on in the OSS/canary default and in every
hardcoded fork, including the native (RN) forks, and keep the test
renderers in sync. www stays GK-driven, so `www.js` and `www-dynamic.js`
are unchanged.

Leaving the flag in the repo for now; this just flips the default on.

Co-authored-by: Claude Opus 4.8 (1M context) <noreply@anthropic.com>

DiffTrain build for [eb8feb7](eb8feb7)
```

[github-actions](/apps/github-actions) Bot
pushed a commit
that referenced
this pull request
[Aug 14, 2026](#ref-commit-d7c9f71)

```
Reverse #35709. Turn the flag on in the OSS/canary default and in every
hardcoded fork, including the native (RN) forks, and keep the test
renderers in sync. www stays GK-driven, so `www.js` and `www-dynamic.js`
are unchanged.

Leaving the flag in the repo for now; this just flips the default on.

Co-authored-by: Claude Opus 4.8 (1M context) <noreply@anthropic.com>

DiffTrain build for [eb8feb7](eb8feb7)
```

[github-actions](/apps/github-actions) Bot
pushed a commit
to code/lib-react
that referenced
this pull request
[Aug 15, 2026](#ref-commit-77ac661)

```
Reverse react#35709. Turn the flag on in the OSS/canary default and in every
hardcoded fork, including the native (RN) forks, and keep the test
renderers in sync. www stays GK-driven, so `www.js` and `www-dynamic.js`
are unchanged.

Leaving the flag in the repo for now; this just flips the default on.

Co-authored-by: Claude Opus 4.8 (1M context) <noreply@anthropic.com>

DiffTrain build for [eb8feb7](react@eb8feb7)
```

[github-actions](/apps/github-actions) Bot
pushed a commit
to code/lib-react
that referenced
this pull request
[Aug 15, 2026](#ref-commit-ce85b10)

```
Reverse react#35709. Turn the flag on in the OSS/canary default and in every
hardcoded fork, including the native (RN) forks, and keep the test
renderers in sync. www stays GK-driven, so `www.js` and `www-dynamic.js`
are unchanged.

Leaving the flag in the repo for now; this just flips the default on.

Co-authored-by: Claude Opus 4.8 (1M context) <noreply@anthropic.com>

DiffTrain build for [eb8feb7](react@eb8feb7)
```

[github-actions](/apps/github-actions) Bot
pushed a commit
to xb18/react
that referenced
this pull request
[Aug 19, 2026](#ref-commit-7172290)

```
Reverse react#35709. Turn the flag on in the OSS/canary default and in every
hardcoded fork, including the native (RN) forks, and keep the test
renderers in sync. www stays GK-driven, so `www.js` and `www-dynamic.js`
are unchanged.

Leaving the flag in the repo for now; this just flips the default on.

Co-authored-by: Claude Opus 4.8 (1M context) <noreply@anthropic.com>

DiffTrain build for [eb8feb7](react@eb8feb7)
```

[github-actions](/apps/github-actions) Bot
pushed a commit
to xb18/react
that referenced
this pull request
[Aug 19, 2026](#ref-commit-57411c2)

```
Reverse react#35709. Turn the flag on in the OSS/canary default and in every
hardcoded fork, including the native (RN) forks, and keep the test
renderers in sync. www stays GK-driven, so `www.js` and `www-dynamic.js`
are unchanged.

Leaving the flag in the repo for now; this just flips the default on.

Co-authored-by: Claude Opus 4.8 (1M context) <noreply@anthropic.com>

DiffTrain build for [eb8feb7](react@eb8feb7)
```

[shnakatani](/shnakatani)
added a commit
to shnakatani/tanstack-start-template
that referenced
this pull request
[Sep 13, 2026](#ref-commit-5be87ac)

```
react / react-dom / @types/react / @types/react-dom を 19.2.x から 19.3.0 へ上げる。
19.3.0 は 2026-09-09 公開で、pnpm-workspace.yaml の minimumReleaseAge (3 日) を経過している。

動機: Transition の独立描画 (react/react#37290) と useDeferredValue の修正 (react/react#36134) を
前提に、ユーザー操作の Transition 化を進める (後続の ADR-0014)。

検証: mise run verify → Tests 271 passed (271)、build と security-headers 検査を通過。
テスト中の console.warn (useRouter must be used inside a <RouterProvider>) は
19.2.8 の baseline でも同じ 1 件が出ており、この更新とは無関係。

Co-authored-by: Claude Fable 5.1 <noreply@anthropic.com>
```

[sickn33](/sickn33)
added a commit
to sickn33/agentic-awesome-skills
that referenced
this pull request
[Oct 1, 2026](#ref-commit-569942e)

```
![snyk-top-banner](https://res.cloudinary.com/snyk/image/upload/r-d/scm-platform/snyk-pull-requests/pr-banner-default.svg)

<h3>Snyk has created this PR to upgrade react-dom from 19.2.8 to 19.3.0.</h3>

:information_source: Keep your dependencies up-to-date. This makes it easier to fix existing vulnerabilities and to more quickly identify and fix newly disclosed vulnerabilities when they affect your project.

<hr/>

- The recommended version is **204 versions** ahead of your current version.

- The recommended version was released **21 days ago**.

#### Breaking Change Risk

![Merge Risk: Low](https://img.shields.io/badge/Merge%20Risk%3A%20Low-006400?style=for-the-badge)

> **Notice:** This assessment is enhanced by AI.

<details>
<summary><b>Release notes</b></summary>
<br/>
  <details>
    <summary>Package name: <b>react-dom</b></summary>
    <ul>
      <li>
        <b>19.3.0</b> - <a href="https://redirect.github.com/react/react/releases/tag/v19.3.0">2026-09-09</a></br><p>Below is a list of all new features, APIs, and bug fixes.</p>
<p>Read the <a href="https://react.dev/blog/2026/09/09/react-19-3" rel="nofollow">React 19.3 release post</a> for more information.</p>
<h2>New React Features</h2>
<ul>
<li><code>&lt;ViewTransition /&gt;</code>: Adds <code>&lt;ViewTransition /&gt;</code> and <code>addTransitionType</code> APIs to power View Transition animations in React (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/sebmarkbage/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a>, <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/jackpope/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://redirect.github.com/jackpope">@ jackpope</a>, <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/gaearon/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://redirect.github.com/gaearon">@ gaearon</a>: <a href="https://redirect.github.com/facebook/react/pull/31975" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/31975/hovercard">#31975</a>, <a href="https://redirect.github.com/facebook/react/pull/31987" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/31987/hovercard">#31987</a>, <a href="https://redirect.github.com/facebook/react/pull/31996" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/31996/hovercard">#31996</a>, <a href="https://redirect.github.com/facebook/react/pull/31999" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/31999/hovercard">#31999</a>, <a href="https://redirect.github.com/facebook/react/pull/32001" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32001/hovercard">#32001</a>, <a href="https://redirect.github.com/facebook/react/pull/32002" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32002/hovercard">#32002</a>, <a href="https://redirect.github.com/facebook/react/pull/32028" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32028/hovercard">#32028</a>, <a href="https://redirect.github.com/facebook/react/pull/32029" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32029/hovercard">#32029</a>, <a href="https://redirect.github.com/facebook/react/pull/32031" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32031/hovercard">#32031</a>, <a href="https://redirect.github.com/facebook/react/pull/32034" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32034/hovercard">#32034</a>, <a href="https://redirect.github.com/facebook/react/pull/32038" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32038/hovercard">#32038</a>, <a href="https://redirect.github.com/facebook/react/pull/32041" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32041/hovercard">#32041</a>, <a href="https://redirect.github.com/facebook/react/pull/32050" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32050/hovercard">#32050</a>, <a href="https://redirect.github.com/facebook/react/pull/32090" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32090/hovercard">#32090</a>, <a href="https://redirect.github.com/facebook/react/pull/32105" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32105/hovercard">#32105</a>, <a href="https://redirect.github.com/facebook/react/pull/32254" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32254/hovercard">#32254</a>, <a href="https://redirect.github.com/facebook/react/pull/32379" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32379/hovercard">#32379</a>, <a href="https://redirect.github.com/facebook/react/pull/32422" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32422/hovercard">#32422</a>, <a href="https://redirect.github.com/facebook/react/pull/32462" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32462/hovercard">#32462</a>, <a href="https://redirect.github.com/facebook/react/pull/32540" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32540/hovercard">#32540</a>, <a href="https://redirect.github.com/facebook/react/pull/32545" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32545/hovercard">#32545</a>, <a href="https://redirect.github.com/facebook/react/pull/32585" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32585/hovercard">#32585</a>, <a href="https://redirect.github.com/facebook/react/pull/32599" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32599/hovercard">#32599</a>, <a href="https://redirect.github.com/facebook/react/pull/32611" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32611/hovercard">#32611</a>, <a href="https://redirect.github.com/facebook/react/pull/32612" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32612/hovercard">#32612</a>, <a href="https://redirect.github.com/facebook/react/pull/32617" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32617/hovercard">#32617</a>, <a href="https://redirect.github.com/facebook/react/pull/32651" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32651/hovercard">#32651</a>, <a href="https://redirect.github.com/facebook/react/pull/32653" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32653/hovercard">#32653</a>, <a href="https://redirect.github.com/facebook/react/pull/32656" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32656/hovercard">#32656</a>, <a href="https://redirect.github.com/facebook/react/pull/32664" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32664/hovercard">#32664</a>, <a href="https://redirect.github.com/facebook/react/pull/32699" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32699/hovercard">#32699</a>, <a href="https://redirect.github.com/facebook/react/pull/32723" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32723/hovercard">#32723</a>, <a href="https://redirect.github.com/facebook/react/pull/32734" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32734/hovercard">#32734</a>, <a href="https://redirect.github.com/facebook/react/pull/32751" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32751/hovercard">#32751</a>, <a href="https://redirect.github.com/facebook/react/pull/32752" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32752/hovercard">#32752</a>, <a href="https://redirect.github.com/facebook/react/pull/32760" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32760/hovercard">#32760</a>, <a href="https://redirect.github.com/facebook/react/pull/32761" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32761/hovercard">#32761</a>, <a href="https://redirect.github.com/facebook/react/pull/32764" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32764/hovercard">#32764</a>, <a href="https://redirect.github.com/facebook/react/pull/32772" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32772/hovercard">#32772</a>, <a href="https://redirect.github.com/facebook/react/pull/32790" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32790/hovercard">#32790</a>, <a href="https://redirect.github.com/facebook/react/pull/32819" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32819/hovercard">#32819</a>, <a href="https://redirect.github.com/facebook/react/pull/32820" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32820/hovercard">#32820</a>, <a href="https://redirect.github.com/facebook/react/pull/32822" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32822/hovercard">#32822</a>, <a href="https://redirect.github.com/facebook/react/pull/32833" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32833/hovercard">#32833</a>, <a href="https://redirect.github.com/facebook/react/pull/32849" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32849/hovercard">#32849</a>, <a href="https://redirect.github.com/facebook/react/pull/33094" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/33094/hovercard">#33094</a>, <a href="https://redirect.github.com/facebook/react/pull/33191" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/33191/hovercard">#33191</a>, <a href="https://redirect.github.com/facebook/react/pull/33200" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/33200/hovercard">#33200</a>, <a href="https://redirect.github.com/facebook/react/pull/33206" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/33206/hovercard">#33206</a>, <a href="https://redirect.github.com/facebook/react/pull/33293" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/33293/hovercard">#33293</a>, <a href="https://redirect.github.com/facebook/react/pull/33330" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/33330/hovercard">#33330</a>, <a href="https://redirect.github.com/facebook/react/pull/33331" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/33331/hovercard">#33331</a>, <a href="https://redirect.github.com/facebook/react/pull/33332" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/33332/hovercard">#33332</a>, <a href="https://redirect.github.com/facebook/react/pull/33357" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/33357/hovercard">#33357</a>, <a href="https://redirect.github.com/facebook/react/pull/33362" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/33362/hovercard">#33362</a>, <a href="https://redirect.github.com/facebook/react/pull/33433" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/33433/hovercard">#33433</a>, <a href="https://redirect.github.com/facebook/react/pull/33576" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/33576/hovercard">#33576</a>, <a href="https://redirect.github.com/facebook/react/pull/34374" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/34374/hovercard">#34374</a>, <a href="https://redirect.github.com/facebook/react/pull/34450" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/34450/hovercard">#34450</a>, <a href="https://redirect.github.com/facebook/react/pull/34481" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/34481/hovercard">#34481</a>, <a href="https://redirect.github.com/facebook/react/pull/34500" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/34500/hovercard">#34500</a>, <a href="https://redirect.github.com/facebook/react/pull/34502" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/34502/hovercard">#34502</a>, <a href="https://redirect.github.com/facebook/react/pull/34510" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/34510/hovercard">#34510</a>, <a href="https://redirect.github.com/facebook/react/pull/34511" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/34511/hovercard">#34511</a>, <a href="https://redirect.github.com/facebook/react/pull/34539" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/34539/hovercard">#34539</a>, <a href="https://redirect.github.com/facebook/react/pull/35567" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/35567/hovercard">#35567</a>, <a href="https://redirect.github.com/facebook/react/pull/35564" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/35564/hovercard">#35564</a>, <a href="https://redirect.github.com/facebook/react/pull/35485" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/35485/hovercard">#35485</a>, <a href="https://redirect.github.com/facebook/react/pull/35380" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/35380/hovercard">#35380</a>, <a href="https://redirect.github.com/facebook/react/pull/35063" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/35063/hovercard">#35063</a>, <a href="https://redirect.github.com/facebook/react/pull/35060" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/35060/hovercard">#35060</a>, <a href="https://redirect.github.com/facebook/react/pull/34676" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/34676/hovercard">#34676</a>, <a href="https://redirect.github.com/facebook/react/pull/36917" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/36917/hovercard">#36917</a>, <a href="https://redirect.github.com/facebook/react/pull/35337" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/35337/hovercard">#35337</a>, <a href="https://redirect.github.com/facebook/react/pull/35520" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/35520/hovercard">#35520</a>)</li>
<li>Fragment Refs: Add Refs to <code>&lt;Fragment /&gt;</code> to support composable platform behavior (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/jackpope/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://redirect.github.com/jackpope">@ jackpope</a>, <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/sebmarkbage/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a>, <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/eps1lon/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://redirect.github.com/eps1lon">@ eps1lon</a>, <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Dhakshin2007/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://redirect.github.com/Dhakshin2007">@ Dhakshin2007</a>, <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/chirokas/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://redirect.github.com/chirokas">@ chirokas</a>, <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/teamleaderleo/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://redirect.github.com/teamleaderleo">@ teamleaderleo</a>, <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/fallintoplace/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://redirect.github.com/fallintoplace">@ fallintoplace</a>: <a href="https://redirect.github.com/facebook/react/pull/32465" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32465/hovercard">#32465</a>, <a href="https://redirect.github.com/facebook/react/pull/32613" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32613/hovercard">#32613</a>, <a href="https://redirect.github.com/facebook/react/pull/32619" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32619/hovercard">#32619</a>, <a href="https://redirect.github.com/facebook/react/pull/32654" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32654/hovercard">#32654</a>, <a href="https://redirect.github.com/facebook/react/pull/32660" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32660/hovercard">#32660</a>, <a href="https://redirect.github.com/facebook/react/pull/32682" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32682/hovercard">#32682</a>, <a href="https://redirect.github.com/facebook/react/pull/32722" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32722/hovercard">#32722</a>, <a href="https://redirect.github.com/facebook/react/pull/32813" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32813/hovercard">#32813</a>, <a href="https://redirect.github.com/facebook/react/pull/32814" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/32814/hovercard">#32814</a>, <a href="https://redirect.github.com/facebook/react/pull/33056" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/33056/hovercard">#33056</a>, <a href="https://redirect.github.com/facebook/react/pull/33058" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/33058/hovercard">#33058</a>, <a href="https://redirect.github.com/facebook/react/pull/33093" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/33093/hovercard">#33093</a>, <a href="https://redirect.github.com/facebook/react/pull/34069" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/34069/hovercard">#34069</a>, <a href="https://redirect.github.com/facebook/react/pull/34103" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/34103/hovercard">#34103</a>, <a href="https://redirect.github.com/facebook/react/pull/34544" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/34544/hovercard">#34544</a>, <a href="https://redirect.github.com/facebook/react/pull/34545" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/34545/hovercard">#34545</a>, <a href="https://redirect.github.com/facebook/react/pull/37062" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37062/hovercard">#37062</a>, <a href="https://redirect.github.com/facebook/react/pull/37061" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37061/hovercard">#37061</a>, <a href="https://redirect.github.com/facebook/react/pull/37060" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37060/hovercard">#37060</a>, <a href="https://redirect.github.com/facebook/react/pull/36047" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/36047/hovercard">#36047</a>, <a href="https://redirect.github.com/facebook/react/pull/36010" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/36010/hovercard">#36010</a>, <a href="https://redirect.github.com/facebook/react/pull/35642" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/35642/hovercard">#35642</a>, <a href="https://redirect.github.com/facebook/react/pull/35641" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/35641/hovercard">#35641</a>, <a href="https://redirect.github.com/facebook/react/pull/35637" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/35637/hovercard">#35637</a>, <a href="https://redirect.github.com/facebook/react/pull/35630" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/35630/hovercard">#35630</a>, <a href="https://redirect.github.com/facebook/react/pull/34935" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/34935/hovercard">#34935</a>, <a href="https://redirect.github.com/facebook/react/pull/37457" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37457/hovercard">#37457</a>, <a href="https://redirect.github.com/facebook/react/pull/37408" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37408/hovercard">#37408</a>, <a href="https://redirect.github.com/facebook/react/pull/37326" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37326/hovercard">#37326</a>, <a href="https://redirect.github.com/facebook/react/pull/37251" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37251/hovercard">#37251</a>, <a href="https://redirect.github.com/facebook/react/pull/37171" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37171/hovercard">#37171</a>, <a href="https://redirect.github.com/facebook/react/pull/37169" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37169/hovercard">#37169</a>, <a href="https://redirect.github.com/facebook/react/pull/37168" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37168/hovercard">#37168</a>, <a href="https://redirect.github.com/facebook/react/pull/37167" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37167/hovercard">#37167</a>, <a href="https://redirect.github.com/facebook/react/pull/37166" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37166/hovercard">#37166</a>, <a href="https://redirect.github.com/facebook/react/pull/37165" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37165/hovercard">#37165</a>, <a href="https://redirect.github.com/facebook/react/pull/37164" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37164/hovercard">#37164</a>, <a href="https://redirect.github.com/facebook/react/pull/37163" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37163/hovercard">#37163</a>, <a href="https://redirect.github.com/facebook/react/pull/37162" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37162/hovercard">#37162</a>, <a href="https://redirect.github.com/facebook/react/pull/37161" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37161/hovercard">#37161</a>, <a href="https://redirect.github.com/facebook/react/pull/37160" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37160/hovercard">#37160</a>, <a href="https://redirect.github.com/facebook/react/pull/37125" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37125/hovercard">#37125</a>, <a href="https://redirect.github.com/facebook/react/pull/37063" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37063/hovercard">#37063</a>)</li>
</ul>
<h2>New React DOM Features</h2>
<ul>
<li><code>browser()</code>: a new <code>react-dom</code> API that returns a usable which errors during server rendering and resolves in the browser. <code>use(browser())</code> inside a <code>&lt;Suspense&gt;</code> boundary marks a subtree as browser-only without reporting a recoverable error (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/gnoff/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://redirect.github.com/gnoff">@ gnoff</a>: <a href="https://redirect.github.com/facebook/react/pull/37143" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37143/hovercard">#37143</a>, <a href="https://redirect.github.com/facebook/react/pull/37241" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37241/hovercard">#37241</a>)
<ul>
<li>Added an <code>onBrowserBailout</code> option to the <code>react-dom/server</code> APIs to observe when a subtree defers to the browser (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/gnoff/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://redirect.github.com/gnoff">@ gnoff</a> <a href="https://redirect.github.com/facebook/react/pull/37193" data-hovercard-type="pull_request" data-hovercard-url="/react/react/pull/37193/hovercard">#37193</a>)</li>
</ul>
</li>
</ul>
<h2>Notable changes</h2>
<ul>
<li>Enable Trusted Types API integration (<a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-ur

... (content truncated)
