---
type: twir-item
issue: 262
item: 2
item_type: item
date: 2025-12-10
source: https://github.com/facebook/react/pull/35277
tags:
  - "PR"
  - "FlightReplyServer"
  - "ReactFlightClient"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-12-10-TWIR-262|Index]]

# Item 2: React PR - Patch FlightReplyServer with fixes from ReactFlightClient

Source: [https://github.com/facebook/react/pull/35277](https://github.com/facebook/react/pull/35277)

Summary:
A major PR synchronizes the server and client implementations of React Flight, addressing deep cycle resolution and deferred error handling. This patch also fixes the critical CVE-2025-55182 vulnerability in React Server Components. The update is included in React 19.2.1, and users of React Server Components are strongly urged to upgrade. Some community members noted the patch is large and mixes refactors with security fixes, making review challenging.

Key takeaways:
- The patch brings critical security fixes to React Server Components (RSC).
- React 19.2.1 is the minimum safe version for RSC users.
- The patch is large and includes unrelated refactoring, complicating security review.
- Further technical details will be released after the fix rollout.

Recommendation:
Summary sufficient (read the PR or changelog if you need implementation details or are maintaining custom RSC infrastructure)

Why it matters:
read the PR or changelog if you need implementation details or are maintaining custom RSC infrastructure

Content:
# Patch FlightReplyServer with fixes from ReactFlightClient by sebmarkbage · Pull Request #35277 · facebook/react · GitHub

```
![snyk-top-banner](https://res.cloudinary.com/snyk/image/upload/r-d/scm-platform/snyk-pull-requests/pr-banner-default.svg)

<h3>Snyk has created this PR to upgrade react from 16.14.0 to
19.2.3.</h3>

:information_source: Keep your dependencies up-to-date. This makes it
easier to fix existing vulnerabilities and to more quickly identify and
fix newly disclosed vulnerabilities when they affect your project.

<hr/>

- The recommended version is **1059 versions** ahead of your current
version.

- The recommended version was released **a month ago**.

<details>
<summary><b>Release notes</b></summary>
<br/>
  <details>
    <summary>Package name: <b>react</b></summary>
    <ul>
      <li>
<b>19.2.3</b> - <a
href="https://redirect.github.com/facebook/react/releases/tag/v19.2.3">2025-12-11</a></br><h2>React
Server Components</h2>
<ul>
<li>Add extra loop protection to React Server Functions (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a> <a
href="https://redirect.github.com/facebook/react/pull/35351"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/35351/hovercard">#35351</a>)</li>
</ul>
      </li>
      <li>
<b>19.2.2</b> - <a
href="https://redirect.github.com/facebook/react/releases/tag/v19.2.2">2025-12-11</a></br><h2>React
Server Components</h2>
<ul>
<li>Move <code>react-server-dom-webpack/*.unbundled</code> to private
<code>react-server-dom-unbundled</code> (<a class="user-mention
notranslate" data-hovercard-type="user"
data-hovercard-url="/users/eps1lon/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/eps1lon">@ eps1lon</a> <a
class="issue-link js-issue-link" data-error-text="Failed to load title"
data-id="3697023033" data-permission-text="Title is private"
data-url="https://github.com/facebook/react/issues/35290"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/35290/hovercard"
href="https://redirect.github.com/facebook/react/pull/35290">#35290</a>)</li>
<li>Patch Promise cycles and toString on Server Functions (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a>, <a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/unstubbable/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/unstubbable">@ unstubbable</a> <a
href="https://redirect.github.com/facebook/react/pull/35289"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/35289/hovercard">#35289</a>, <a
href="https://redirect.github.com/facebook/react/pull/35345"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/35345/hovercard">#35345</a>)</li>
</ul>
      </li>
      <li>
<b>19.2.1</b> - <a
href="https://redirect.github.com/facebook/react/releases/tag/v19.2.1">2025-12-03</a></br><h2>React
Server Components</h2>
<ul>
<li>Bring React Server Component fixes to Server Actions (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a> <a
href="https://redirect.github.com/facebook/react/pull/35277"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/35277/hovercard">#35277</a>)</li>
</ul>
      </li>
      <li>
<b>19.2.0</b> - <a
href="https://redirect.github.com/facebook/react/releases/tag/v19.2.0">2025-10-01</a></br><p>Below
is a list of all new features, APIs, and bug fixes.</p>
<p>Read the <a href="https://react.dev/blog/2025/10/01/react-19-2"
rel="nofollow">React 19.2 release post</a> for more information.</p>
<h2>New React Features</h2>
<ul>
<li><a href="https://react.dev/reference/react/Activity"
rel="nofollow"><code>&lt;Activity&gt;</code></a>: A new API to hide and
restore the UI and internal state of its children.</li>
<li><a href="https://react.dev/reference/react/useEffectEvent"
rel="nofollow"><code>useEffectEvent</code></a> is a React Hook that lets
you extract non-reactive logic into an <a
href="https://react.dev/learn/separating-events-from-effects#declaring-an-effect-event"
rel="nofollow">Effect Event</a>.</li>
<li><a href="https://react.dev/reference/react/cacheSignal"
rel="nofollow"><code>cacheSignal</code></a> (for RSCs) lets your know
when the <code>cache()</code> lifetime is over.</li>
<li><a
href="https://react.dev/reference/developer-tooling/react-performance-tracks"
rel="nofollow">React Performance tracks</a> appear on the Performance
panel’s timeline in your browser developer tools</li>
</ul>
<h2>New React DOM Features</h2>
<ul>
<li>Added resume APIs for partial pre-rendering with Web Streams:
<ul>
<li><a href="https://react.dev/reference/react-dom/server/resume"
rel="nofollow"><code>resume</code></a>: to resume a prerender to a
stream.</li>
<li><a
href="https://react.dev/reference/react-dom/static/resumeAndPrerender"
rel="nofollow"><code>resumeAndPrerender</code></a>: to resume a
prerender to HTML.</li>
</ul>
</li>
<li>Added resume APIs for partial pre-rendering with Node Streams:
<ul>
<li><a
href="https://react.dev/reference/react-dom/server/resumeToPipeableStream"
rel="nofollow"><code>resumeToPipeableStream</code></a>: to resume a
prerender to a stream.</li>
<li><a
href="https://react.dev/reference/react-dom/static/resumeAndPrerenderToNodeStream"
rel="nofollow"><code>resumeAndPrerenderToNodeStream</code></a>: to
resume a prerender to HTML.</li>
</ul>
</li>
<li>Updated <a
href="https://react.dev/reference/react-dom/static/prerender"
rel="nofollow"><code>prerender</code></a> APIs to return a
<code>postponed</code> state that can be passed to the
<code>resume</code> APIs.</li>
</ul>
<h2>Notable changes</h2>
<ul>
<li>React DOM now batches suspense boundary reveals, matching the
behavior of client side rendering. This change is especially noticeable
when animating the reveal of Suspense boundaries e.g. with the upcoming
<code>&lt;ViewTransition&gt;</code> Component. React will batch as much
reveals as possible before the first paint while trying to hit popular
first-contentful paint metrics.</li>
<li>Add Node Web Streams (<code>prerender</code>,
<code>renderToReadableStream</code>) to server-side-rendering APIs for
Node.js</li>
<li>Use underscore instead of <code>:</code> IDs generated by useId</li>
</ul>
<h2>All Changes</h2>
<h3>React</h3>
<ul>
<li><code>&lt;Activity /&gt;</code> was developed over many years,
starting before <code>ClassComponent.setState</code> (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/acdlite/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/acdlite">@ acdlite</a> <a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a> and
many others)</li>
<li>Stringify context as "SomeContext" instead of "SomeContext.Provider"
(<a class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/kassens/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/kassens">@ kassens</a> <a
href="https://redirect.github.com/facebook/react/pull/33507"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33507/hovercard">#33507</a>)</li>
<li>Include stack of cause of React instrumentation errors with
<code>%o</code> placeholder (<a class="user-mention notranslate"
data-hovercard-type="user" data-hovercard-url="/users/eps1lon/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/eps1lon">@ eps1lon</a> <a
href="https://redirect.github.com/facebook/react/pull/34198"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/34198/hovercard">#34198</a>)</li>
<li>Fix infinite <code>useDeferredValue</code> loop in popstate event
(<a class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/acdlite/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/acdlite">@ acdlite</a> <a
href="https://redirect.github.com/facebook/react/pull/32821"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/32821/hovercard">#32821</a>)</li>
<li>Fix a bug when an initial value was passed to
<code>useDeferredValue</code> (<a class="user-mention notranslate"
data-hovercard-type="user" data-hovercard-url="/users/acdlite/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/acdlite">@ acdlite</a> <a
href="https://redirect.github.com/facebook/react/pull/34376"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/34376/hovercard">#34376</a>)</li>
<li>Fix a crash when submitting forms with Client Actions (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a> <a
href="https://redirect.github.com/facebook/react/pull/33055"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33055/hovercard">#33055</a>)</li>
<li>Hide/unhide the content of dehydrated suspense boundaries if they
resuspend (<a class="user-mention notranslate"
data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a> <a
href="https://redirect.github.com/facebook/react/pull/32900"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/32900/hovercard">#32900</a>)</li>
<li>Avoid stack overflow on wide trees during Hot Reload (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/sophiebits/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sophiebits">@ sophiebits</a> <a
href="https://redirect.github.com/facebook/react/pull/34145"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/34145/hovercard">#34145</a>)</li>
<li>Improve Owner and Component stacks in various places (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a>, <a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/eps1lon/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/eps1lon">@ eps1lon</a>: <a
href="https://redirect.github.com/facebook/react/pull/33629"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33629/hovercard">#33629</a>, <a
href="https://redirect.github.com/facebook/react/pull/33724"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33724/hovercard">#33724</a>, <a
href="https://redirect.github.com/facebook/react/pull/32735"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/32735/hovercard">#32735</a>, <a
href="https://redirect.github.com/facebook/react/pull/33723"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33723/hovercard">#33723</a>)</li>
<li>Add <code>cacheSignal</code> (<a class="user-mention notranslate"
data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a> <a
href="https://redirect.github.com/facebook/react/pull/33557"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33557/hovercard">#33557</a>)</li>
</ul>
<h3>React DOM</h3>
<ul>
<li>Block on Suspensey Fonts during reveal of server-side-rendered
content (<a class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a> <a
href="https://redirect.github.com/facebook/react/pull/33342"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33342/hovercard">#33342</a>)</li>
<li>Use underscore instead of <code>:</code> for IDs generated by
<code>useId</code> (<a class="user-mention notranslate"
data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a>, <a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/eps1lon/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/eps1lon">@ eps1lon</a>: <a
href="https://redirect.github.com/facebook/react/pull/32001"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/32001/hovercard">#32001</a>, <a
class="issue-link js-issue-link" data-error-text="Failed to load title"
data-id="3084407166" data-permission-text="Title is private"
data-url="https://github.com/facebook/react/issues/33342"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33342/hovercard"
href="https://redirect.github.com/facebook/react/pull/33342">#33342</a><a
href="https://redirect.github.com/facebook/react/pull/33099"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33099/hovercard">#33099</a>, <a
href="https://redirect.github.com/facebook/react/pull/33422"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33422/hovercard">#33422</a>)</li>
<li>Stop warning when ARIA 1.3 attributes are used (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/Abdul-Omira/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/Abdul-Omira">@ Abdul-Omira</a> <a
href="https://redirect.github.com/facebook/react/pull/34264"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/34264/hovercard">#34264</a>)</li>
<li>Allow <code>nonce</code> to be used on hoistable styles (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/Andarist/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/Andarist">@ Andarist</a> <a
href="https://redirect.github.com/facebook/react/pull/32461"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/32461/hovercard">#32461</a>)</li>
<li>Warn for using a React owned node as a Container if it also has text
content (<a class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a> <a
href="https://redirect.github.com/facebook/react/pull/32774"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/32774/hovercard">#32774</a>)</li>
<li>s/HTML/text for for error messages if text hydration mismatches (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/rickhanlonii/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/rickhanlonii">@ rickhanlonii</a> <a
href="https://redirect.github.com/facebook/react/pull/32763"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/32763/hovercard">#32763</a>)</li>
<li>Fix a bug with <code>React.use</code> inside
<code>React.lazy</code>-ed Component (<a class="user-mention
notranslate" data-hovercard-type="user"
data-hovercard-url="/users/hi-ogawa/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/hi-ogawa">@ hi-ogawa</a> <a
href="https://redirect.github.com/facebook/react/pull/33941"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33941/hovercard">#33941</a>)</li>
<li>Enable the <code>progressiveChunkSize</code> option for
server-side-rendering APIs (<a class="user-mention notranslate"
data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a> <a
href="https://redirect.github.com/facebook/react/pull/33027"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33027/hovercard">#33027</a>)</li>
<li>Fix a bug with deeply nested Suspense inside Suspense fallback when
server-side-rendering (<a class="user-mention notranslate"
data-hovercard-type="user" data-hovercard-url="/users/gnoff/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/gnoff">@ gnoff</a> <a
href="https://redirect.github.com/facebook/react/pull/33467"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33467/hovercard">#33467</a>)</li>
<li>Avoid hanging when suspending after aborting while rendering (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/gnoff/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/gnoff">@ gnoff</a> <a
href="https://redirect.github.com/facebook/react/pull/34192"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/34192/hovercard">#34192</a>)</li>
<li>Add Node Web Streams to server-side-rendering APIs for Node.js (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a> <a
href="https://redirect.github.com/facebook/react/pull/33475"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33475/hovercard">#33475</a>)</li>
</ul>
<h3>React Server Components</h3>
<ul>
<li>Preload <code>&lt;img&gt;</code> and <code>&lt;link&gt;</code> using
hints before they're rendered (<a class="user-mention notranslate"
data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a> <a
href="https://redirect.github.com/facebook/react/pull/34604"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/34604/hovercard">#34604</a>)</li>
<li>Log error if production elements are rendered during development (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/eps1lon/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/eps1lon">@ eps1lon</a> <a
href="https://redirect.github.com/facebook/react/pull/34189"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/34189/hovercard">#34189</a>)</li>
<li>Fix a bug when returning a Temporary reference (e.g. a Client
Reference) from Server Functions (<a class="user-mention notranslate"
data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a> <a
href="https://redirect.github.com/facebook/react/pull/34084"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/34084/hovercard">#34084</a>, <a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/denk0403/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/denk0403">@ denk0403</a> <a
href="https://redirect.github.com/facebook/react/pull/33761"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33761/hovercard">#33761</a>)</li>
<li>Pass line/column to <code>filterStackFrame</code> (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/eps1lon/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/eps1lon">@ eps1lon</a> <a
href="https://redirect.github.com/facebook/react/pull/33707"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33707/hovercard">#33707</a>)</li>
<li>Support Async Modules in Turbopack Server References (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/lubieowoce/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/lubieowoce">@ lubieowoce</a> <a
href="https://redirect.github.com/facebook/react/pull/34531"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/34531/hovercard">#34531</a>)</li>
<li>Add support for .mjs file extension in Webpack (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/jennyscript/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/jennyscript">@ jennyscript</a> <a
href="https://redirect.github.com/facebook/react/pull/33028"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33028/hovercard">#33028</a>)</li>
<li>Fix a wrong missing key warning (<a class="user-mention notranslate"
data-hovercard-type="user"
data-hovercard-url="/users/unstubbable/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/unstubbable">@ unstubbable</a> <a
href="https://redirect.github.com/facebook/react/pull/34350"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/34350/hovercard">#34350</a>)</li>
<li>Make console log resolve in predictable order (<a
class="user-mention notranslate" data-hovercard-type="user"
data-hovercard-url="/users/sebmarkbage/hovercard"
data-octo-click="hovercard-link-click"
data-octo-dimensions="link_type:self"
href="https://redirect.github.com/sebmarkbage">@ sebmarkbage</a> <a
href="https://redirect.github.com/facebook/react/pull/33665"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33665/hovercard">#33665</a>)</li>
</ul>
<h3>React Reconciler</h3>
<ul>
<li><a
href="https://redirect.github.com/facebook/react/blob/v19.2.0/packages/react-reconciler/src/ReactFiberReconciler.js#L255-L261">createContainer</a>
and <a
href="https://redirect.github.com/facebook/react/blob/v19.2.0/packages/react-reconciler/src/ReactFiberReconciler.js#L305-L312">createHydrationContainer</a>
had their parameter order adjusted after <code>on*</code> handlers to
account for upcoming experimental APIs</li>
</ul>
<h2>eslint-plugin-react-hooks@6.1.0</h2>
<p><strong>Note:</strong> Version 6.0.0 was mistakenly released and
immediately deprecated and untagged on npm. This is the first official
6.x major release and includes breaking changes.</p>
<ul>
<li><strong>Breaking:</strong> Require Node.js 18 or newer. (<a
href="https://redirect.github.com/michaelfaith">@ michaelfaith</a> in <a
href="https://redirect.github.com/facebook/react/pull/32458"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/32458/hovercard">#32458</a>)</li>
<li><strong>Breaking:</strong> Flat config is now the default
<code>recommended</code> preset. Legacy config moved to
<code>recommended-legacy</code>. (<a
href="https://redirect.github.com/michaelfaith">@ michaelfaith</a> in <a
href="https://redirect.github.com/facebook/react/pull/32457"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/32457/hovercard">#32457</a>)</li>
<li><strong>New Violations:</strong> Disallow calling <code>use</code>
within try/catch blocks. (<a href="https://redirect.github.com/poteto">@
poteto</a> in <a
href="https://redirect.github.com/facebook/react/pull/34040"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/34040/hovercard">#34040</a>)</li>
<li><strong>New Violations:</strong> Disallow calling
<code>useEffectEvent</code> functions in arbitrary closures. (<a
href="https://redirect.github.com/jbrown215">@ jbrown215</a> in <a
href="https://redirect.github.com/facebook/react/pull/33544"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/33544/hovercard">#33544</a>)</li>
<li>Handle <code>React.useEffect</code> in addition to
<code>useEffect</code> in rules-of-hooks. (<a
href="https://redirect.github.com/Ayc0">@ Ayc0</a> in <a
href="https://redirect.github.com/facebook/react/pull/34076"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/34076/hovercard">#34076</a>)</li>
<li>Added <code>react-hooks</code> settings config option that to accept
<code>additionalEffectHooks</code> that are used across exhaustive-deps
and rules-of-hooks rules. (<a
href="https://redirect.github.com/jbrown215">@ jbrown215</a>) in <a
href="https://redirect.github.com/facebook/react/pull/34497"
data-hovercard-type="pull_request"
data-hovercard-url="/facebook/react/pull/34497/hovercard">#34497</a></li>
</ul>
      </li>
      <li>
        <b>19.2.0-canary-fa3feba6-20250623</b> - 2025-06-23
      </li>
      <li>
        <b>19.2.0-canary-f9ae0a4c-20250527</b> - 2025-05-27
      </li>
      <li>
        <b>19.2.0-canary-f7396427-20250501</b> - 2025-05-02
      </li>
      <li>
        <b>19.2.0-canary-f508edc8-20250818</b> - 2025-08-18
      </li>
      <li>
        <b>19.2.0-canary-f3a80361-20250911</b> - 2025-09-11
      </li>
      <li>
        <b>19.2.0-canary-f1e70b5e-20250811</b> - 2025-08-11
      </li>
      <li>
        <b>19.2.0-canary-f1222f76-20250812</b> - 2025-08-13
      </li>
      <li>
        <b>19.2.0-canary-ef8b6fa2-20250702</b> - 2025-07-03
      </li>
      <li>
        <b>19.2.0-canary-ef889445-20250930</b> - 2025-09-30
      </li>
      <li>
        <b>19.2.0-canary-edac0dde-20250723</b> - 2025-07-23
      </li>
      <li>
        <b>19.2.0-canary-eaee5308-20250728</b> - 2025-07-28
      </li>
      <li>
        <b>19.2.0-canary-ea05b750-20250408</b> - 2025-04-09
      </li>
      <li>
        <b>19.2.0-canary-e9db3cc2-20250501</b> - 2025-05-01
      </li>
      <li>
        <b>19.2.0-canary-e9638c33-20250721</b> - 2025-07-21
      </li>
      <li>
        <b>19.2.0-canary-e6dc25da-20250709</b> - 2025-07-09
      </li>
      <li>
        <b>19.2.0-canary-e5dd82a7-20250401</b> - 2025-04-01
      </li>
      <li>
        <b>19.2.0-canary-e2332183-20250924</b> - 2025-09-24
      </li>
      <li>
        <b>19.2.0-canary-dffacc7b-20250717</b> - 2025-07-17
      </li>
      <li>
        <b>19.2.0-canary-df38ac9a-20250926</b> - 2025-09-26
      </li>
      <li>
        <b>19.2.0-canary-de5a1b20-20250905</b> - 2025-09-05
      </li>
      <li>
        <b>19.2.0-canary-d92056ef-20250627</b> - 2025-06-27
      </li>
      <li>
        <b>19.2.0-canary-d85f86cf-20250514</b> - 2025-05-14
      </li>
      <li>
        <b>19.2.0-canary-d85ec5f5-20250716</b> - 2025-07-16
      </li>
      <li>
        <b>19.2.0-canary-d415fd3e-20250919</b> - 2025-09-19
      </li>
      <li>
        <b>19.2.0-canary-d15d7fd7-20250929</b> - 2025-09-29
      </li>
      <li>
        <b>19.2.0-canary-cee7939b-20250625</b> - 2025-06-25
      </li>
      <li>
        <b>19.2.0-canary-c498bfce-20250426</b> - 2025-04-28
      </li>
      <li>
        <b>19.2.0-canary-c4676e72-20250520</b> - 2025-05-20
      </li>
      <li>
        <b>19.2.0-canary-c44e4a25-20250409</b> - 2025-04-10
      </li>
      <li>
        <b>19.2.0-canary-c260b38d-20250731</b> - 2025-07-31
      </li>
      <li>
        <b>19.2.0-canary-c129c242-20250505</b> - 2025-05-05
      </li>
      <li>
        <b>19.2.0-canary-c0464aed-20250523</b> - 2025-05-26
      </li>
      <li>
        <b>19.2.0-canary-befc1246-20250708</b> - 2025-07-08
      </li>
      <li>
        <b>19.2.0-canary-be11cb5c-20250804</b> - 2025-08-04
      </li>
      <li>
        <b>19.2.0-canary-bdb4a96f-20250801</b> - 2025-08-01
      </li>
      <li>
        <b>19.2.0-canary-bc6184dd-20250417</b> - 2025-04-18
      </li>
      <li>
        <b>19.2.0-canary-bbc13fa1-20250624</b> - 2025-06-24
      </li>
      <li>
        <b>19.2.0-canary-bb6f0c8d-20250901</b> - 2025-09-01
      </li>
      <li>
        <b>19.2.0-canary-b9cfa0d3-20250505</b> - 2025-05-05
      </li>
      <li>
        <b>19.2.0-canary-b9a04536-20250904</b> - 2025-09-04
      </li>
      <li>
        <b>19.2.0-canary-b94603b9-20250513</b> - 2025-05-13
      </li>
      <li>
        <b>19.2.0-canary-b7e2de63-20250611</b> - 2025-06-11
      </li>
      

... (content truncated)

Related notes: [[Server Components]]
