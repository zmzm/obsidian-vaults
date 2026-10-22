---
type: twir-item
issue: 296
item: 2
item_type: item
date: 2026-09-09
source: https://github.com/react/react/blob/main/packages/react-devtools/CHANGELOG.md#800
tags:
  - "DevTools"
  - "80"
status: auto
quality: keep
---

[[2026-09-09-TWIR-296|Index]]

# Item 2: React DevTools 8.0 - Suspense Tab enabled, React Element panel, remove Timeline profiler in favor of Performance tracks, display dimmed Activity subtree

Source: [https://github.com/react/react/blob/main/packages/react-devtools/CHANGELOG.md#800](https://github.com/react/react/blob/main/packages/react-devtools/CHANGELOG.md#800)

Summary:
React DevTools 8.0 introduces several major updates, including enabling the Suspense tab by default, removing the Timeline profiler in favor of browser-native Performance panel tracks, and adding a React Element pane to the browser’s Elements panel. The release also brings UI improvements, new navigation and filtering features, and a comprehensive set of bugfixes for stability and usability. The changelog covers enhancements from recent 7.x and 6.x releases as well.

Key takeaways:
- Suspense debugging is now more accessible with the Suspense tab enabled by default.
- The Timeline profiler is deprecated; use the browser’s Performance panel for profiling React with integrated tracks.
- Inspecting DOM nodes now reveals the corresponding React component, improving debugging workflows.
- Numerous UI, navigation, and bugfix improvements enhance the overall DevTools experience.

Recommendation:
Read fully (read fully if you rely on profiling, Suspense, or want to explore new inspection features)

Why it matters:
read fully if you rely on profiling, Suspense, or want to explore new inspection features

Content:
# react/packages/react-devtools/CHANGELOG.md at main · react/react · GitHub

---

September 8, 2026

The Suspense tab is now on by default, so you can inspect what caused a component to suspend without turning anything extra on.

The Timeline profiler tab has been removed. To profile React, use your browser's Performance panel — it includes React tracks.

When you inspect a DOM node in the browser Elements panel, you can now see the matching React component.

- Enable Suspense tab by default ([eps1lon](https://github.com/eps1lon) in [#35768](https://github.com/facebook/react/pull/35768))
- Remove Timeline profiler tab and dead Timeline profiler code ([hoxyq](https://github.com/hoxyq) in [#37186](https://github.com/facebook/react/pull/37186), [#37187](https://github.com/facebook/react/pull/37187))
- Redesign the Profiler empty states around a primary action ([hoxyq](https://github.com/hoxyq) in [#37185](https://github.com/facebook/react/pull/37185))
- Add React Element pane to browser Elements panel ([eps1lon](https://github.com/eps1lon) in [#35240](https://github.com/facebook/react/pull/35240))
- Display subtree for Activity and dim in hidden mode ([hoxyq](https://github.com/hoxyq) in [#36094](https://github.com/facebook/react/pull/36094))
- Show list of named Activities in Suspense tab ([eps1lon](https://github.com/eps1lon) in [#35092](https://github.com/facebook/react/pull/35092), [#35108](https://github.com/facebook/react/pull/35108), [#35164](https://github.com/facebook/react/pull/35164))
- Make component search results directly navigable ([Biki-das](https://github.com/Biki-das) in [#36786](https://github.com/facebook/react/pull/36786))
- Add component search to the Profiler's commit view ([Biki-das](https://github.com/Biki-das) in [#36944](https://github.com/facebook/react/pull/36944))
- Add parent stack tool ([hoxyq](https://github.com/hoxyq) in [#36825](https://github.com/facebook/react/pull/36825))
- Add ignore-listed stack frame disclosure ([devjiwonchoi](https://github.com/devjiwonchoi) in [#36828](https://github.com/facebook/react/pull/36828))
- Display `React.optimisticKey` in key positions ([eps1lon](https://github.com/eps1lon) in [#35760](https://github.com/facebook/react/pull/35760))
- Allow renaming Host Component props ([eps1lon](https://github.com/eps1lon) in [#35735](https://github.com/facebook/react/pull/35735))
- Hotkey to start/stop profiling ([emily8rown](https://github.com/emily8rown) in [#35160](https://github.com/facebook/react/pull/35160))
- Navigating commits performance panel hotkey ([emily8rown](https://github.com/emily8rown) in [#35238](https://github.com/facebook/react/pull/35238))
- Enable React DevTools Client connections to a custom host/port/path ([fullstackhacker](https://github.com/fullstackhacker) in [#35886](https://github.com/facebook/react/pull/35886))
- Enable minimal support in pages with `sandbox` Content-Security-Policy ([mochiya98](https://github.com/mochiya98) in [#35208](https://github.com/facebook/react/pull/35208))
- Create extension panels before React detection ([hoxyq](https://github.com/hoxyq) in [#37151](https://github.com/facebook/react/pull/37151))
- Apply component filters on initial load and update inspected element when filters change ([eps1lon](https://github.com/eps1lon) in [#35587](https://github.com/facebook/react/pull/35587), [#35599](https://github.com/facebook/react/pull/35599))
- Synchronize scroll position between Suspense tab and the main document ([sebmarkbage](https://github.com/sebmarkbage) in [#34641](https://github.com/facebook/react/pull/34641))
- Sort Suspense timeline by end time ([sebmarkbage](https://github.com/sebmarkbage) in [#35011](https://github.com/facebook/react/pull/35011))
- Disable log dimming Strict Mode setting ([emily8rown](https://github.com/emily8rown) in [#35207](https://github.com/facebook/react/pull/35207))
- Improve the detection of changed hooks ([blazejkustra](https://github.com/blazejkustra) in [#35123](https://github.com/facebook/react/pull/35123))

- Fix reconciliation of content with fallback Fiber ([eps1lon](https://github.com/eps1lon) in [#37475](https://github.com/facebook/react/pull/37475))
- Fix nested HOC name extraction in `extractHOCNames` ([Biki-das](https://github.com/Biki-das) in [#37215](https://github.com/facebook/react/pull/37215))
- Reset extension backend on `pagehide` and buffer Bridge messages during reconnects ([hoxyq](https://github.com/hoxyq) in [#37155](https://github.com/facebook/react/pull/37155), [#37075](https://github.com/facebook/react/pull/37075), [#37076](https://github.com/facebook/react/pull/37076))
- Don't connect or reconnect while a page is prerendering ([eps1lon](https://github.com/eps1lon) in [#35958](https://github.com/facebook/react/pull/35958), [Saransh-Jainbu](https://github.com/Saransh-Jainbu) in [#37009](https://github.com/facebook/react/pull/37009))
- Fix WhatChanged scrolling out of view in profiler sidebar ([Kertsu](https://github.com/Kertsu) in [#36244](https://github.com/facebook/react/pull/36244))
- Keep console specifiers literal when no argument is supplied, substitute `%i`/`%f`, and fix trailing percent signs ([anxkhn](https://github.com/anxkhn) in [#36930](https://github.com/facebook/react/pull/36930), [#36929](https://github.com/facebook/react/pull/36929), [UditDewan](https://github.com/UditDewan) in [#36852](https://github.com/facebook/react/pull/36852))
- Avoid HTML injection in standalone errors ([fallintoplace](https://github.com/fallintoplace) in [#36839](https://github.com/facebook/react/pull/36839))
- Preserve `-Infinity` in inspected values ([zxuhan](https://github.com/zxuhan) in [#36347](https://github.com/facebook/react/pull/36347))
- Clear highlight when the mouse leaves the DevTools panel ([petertdinh](https://github.com/petertdinh) in [#36177](https://github.com/facebook/react/pull/36177))
- Don't show an empty Suspended By section ([hoxyq](https://github.com/hoxyq) in [#36011](https://github.com/facebook/react/pull/36011))
- Ignore new production renderers if a page already uses an older React ([eps1lon](https://github.com/eps1lon) in [#35994](https://github.com/facebook/react/pull/35994))
- Fix crash when simulating an errored state on a new class component ([eps1lon](https://github.com/eps1lon) in [#35985](https://github.com/facebook/react/pull/35985))
- Fix null ref crash in ContextMenu when the items list is empty ([fresh3nough](https://github.com/fresh3nough) in [#35929](https://github.com/facebook/react/pull/35929))
- Fix `ReactDevToolsBackend` module for AMD ([fullstackhacker](https://github.com/fullstackhacker) in [#35891](https://github.com/facebook/react/pull/35891))
- Fix memory leak when unmounting hoistables ([eps1lon](https://github.com/eps1lon) in [#35741](https://github.com/facebook/react/pull/35741))
- Don't capture durations for disconnected subtrees when profiling ([hoxyq](https://github.com/hoxyq) in [#35718](https://github.com/facebook/react/pull/35718))
- Fix crash when revealing stable, filtered `<Activity>` children ([eps1lon](https://github.com/eps1lon) in [#35734](https://github.com/facebook/react/pull/35734))
- Fix false-positive re-render reports for filtered nodes ([hoxyq](https://github.com/hoxyq) in [#35723](https://github.com/facebook/react/pull/35723))
- Fix broken commit tree builder for initial operations ([eps1lon](https://github.com/eps1lon) in [#35710](https://github.com/facebook/react/pull/35710))
- Fix commit index reset when switching profiler roots ([hoxyq](https://github.com/hoxyq) in [#35672](https://github.com/facebook/react/pull/35672))
- Fix console links not being openable ([eps1lon](https://github.com/eps1lon) in [#35229](https://github.com/facebook/react/pull/35229))
- Feature-check `document`, stack trace methods, and `getClientRects` ([hoxyq](https://github.com/hoxyq) in [#35343](https://github.com/facebook/react/pull/35343), [#35293](https://github.com/facebook/react/pull/35293), [#35294](https://github.com/facebook/react/pull/35294))
- Reset forced states when changing component filters ([eps1lon](https://github.com/eps1lon) in [#34929](https://github.com/facebook/react/pull/34929))
- Fix hook indices when using `useSyncExternalStore` ([blazejkustra](https://github.com/blazejkustra) in [#34547](https://github.com/facebook/react/pull/34547))
- Fix `printOperationsArray` decode of applied Activity slice changes ([anxkhn](https://github.com/anxkhn) in [#36935](https://github.com/facebook/react/pull/36935))

---

October 20, 2025

- Various UI improvements to experimental Suspense tab ([sebmarkbage](https://github.com/sebmarkbage) & [eps1lon](https://github.com/eps1lon))
- devtools: fix ellipsis truncation for key values ([sophiebits](https://github.com/sophiebits) in [#34796](https://github.com/facebook/react/pull/34796))
- fix(devtools): remove duplicated "Display density" field in General settings ([Anatole-Godard](https://github.com/Anatole-Godard) in [#34792](https://github.com/facebook/react/pull/34792))

---

Oct 2, 2025

Add a "suspended by" section showing all causes of why the inspected element suspended. This includes:

- `await` in Server Components
- `React.lazy`
- `use()`
- suspensey images, CSS, and fonts

Add a Code Editor Sidebar Pane in the Chrome Sources Tab (@sebmarkbage [#33968](https://github.com/facebook/react/pull/33968), [#33987](https://github.com/facebook/react/pull/33987), [#33988](https://github.com/facebook/react/pull/33988))

Add Option to Open Local Files directly in External Editor (@sebmarkbage [#33983](https://github.com/facebook/react/pull/33983), [#33985](https://github.com/facebook/react/pull/33985), [#33965](https://github.com/facebook/react/pull/33965))

- Allow inspection of React tree before streaming has finished (@eps1lon [#34360](https://github.com/facebook/react/pull/34360))
- Always attempt to mount dehydrated roots (@eps1lon [#34209](https://github.com/facebook/react/pull/34209))
- Show `name` prop of Suspense / Activity in the Components Tree view (@sebmarkbage [#34135](https://github.com/facebook/react/pull/34135))
- 1st class support of used Thenables (@sebmarkbage, @eps1lon: [#32989](https://github.com/facebook/react/pull/32989), [#34097](https://github.com/facebook/react/pull/34097))
- Allow inspecting cause, name, message, stack of Errors in props (@eps1lon [#33023](https://github.com/facebook/react/pull/33023))
- Allow Introspection of React Elements and React.lazy (@sebmarkbage [#34129](https://github.com/facebook/react/pull/34129))
- Fix "View source" for sources with URLs that aren't normalized (@eps1lon [#32951](https://github.com/facebook/react/pull/32951))
- Fix symbolication with Index Source Maps (@eps1lon [#34300](https://github.com/facebook/react/pull/34300))
- Ignore List Stack Traces (@sebmarkbage [#34210](https://github.com/facebook/react/pull/34210))
- Linkify Source View (@sebmarkbage [#33954](https://github.com/facebook/react/pull/33954))
- Only show state for ClassComponents (@sebmarkbage [#34091](https://github.com/facebook/react/pull/34091))
- Show Owner Stacks in "rendered by" View (@sebmarkbage [#34130](https://github.com/facebook/react/pull/34130))
- Stop mounting empty roots (@eps1lon [#34467](https://github.com/facebook/react/pull/34467))
- Show changed hooks names in the Profiler tab (@piotrski [#31398](https://github.com/facebook/react/pull/31398))
- Display native tag for host components for Native (@ruslan [#32762](https://github.com/facebook/react/pull/32762))
- Static Components panel layout (@ruslan [#33696](https://github.com/facebook/react/pull/33696), [#33517](https://github.com/facebook/react/pull/33517), [#34088](https://github.com/facebook/react/pull/34088))
- Add Badge to Owners and sometimes stack traces (@sebmarkbage [#34106](https://github.com/facebook/react/pull/34106))
- Make a non-editable name of KeyValue clickable ([34095](https://github.com/facebook/react/pull/34095))
- Only inspect elements on left mouseclick (@eps1lon [#34361](https://github.com/facebook/react/pull/34361))
- Rerender when the browser theme changes (@sebmarkbage [#33992](https://github.com/facebook/react/pull/33992))
- Stop using native `title` for buttons/icons (@eps1lon [#34379](https://github.com/facebook/react/pull/34379))
- Style clickable Owner components with angle brackets and bold (@sebmarkbage [#34096](https://github.com/facebook/react/pull/34096))
- Swap Components tab layout based on container size (@eps1lon [#34035](https://github.com/facebook/react/pull/34035))
- Use Visually Lighter Skeletons (@sebmarkbage [#34185](https://github.com/facebook/react/pull/34185))

---

July 4, 2025

- fix: fallback to reading string stack trace when failed ([hoxyq](https://github.com/hoxyq) in [#33700](https://github.com/facebook/react/pull/33700))

---

July 4, 2025

- feat: static Components panel layout ([hoxyq](https://github.com/hoxyq) in [#33696](https://github.com/facebook/react/pull/33696))

---

June 27, 2025

- devtools: emit performance entries only when profiling ([hoxyq](https://github.com/hoxyq) in [#33652](https://github.com/facebook/react/pull/33652))
- Get Server Component Function Location for Parent Stacks using Child's Owner Stack ([sebmarkbage](https://github.com/sebmarkbage) in [#33629](https://github.com/facebook/react/pull/33629))
- Added minimum indent size to Component Tree ([jsdf](https://github.com/jsdf) in [#33517](https://github.com/facebook/react/pull/33517))
- refactor[devtools]: update css for settings and support css variables in shadow dom scnenario ([hoxyq](https://github.com/hoxyq) in [#33487](https://github.com/facebook/react/pull/33487))
- Get source location from structured callsites in prepareStackTrace ([sebmarkbage](https://github.com/sebmarkbage) in [#33143](https://github.com/facebook/react/pull/33143))

---

May 7, 2025

- Restore "double-click to view owners tree" functionality ([eps1lon](https://github.com/eps1lon) in [#33039](https://github.com/facebook/react/pull/33039))

---

February 7, 2025

- DevTools: refactor NativeStyleEditor, don't use custom cache implementation ([hoxyq](https://github.com/hoxyq) in [#32298](https://github.com/facebook/react/pull/32298))
- DevTools: fix host component filter option title ([hoxyq](https://github.com/hoxyq) in [#32296](https://github.com/facebook/react/pull/32296))
- chore[DevTools]: make clipboardWrite optional for chromium ([hoxyq](https://github.com/hoxyq) in [#32262](https://github.com/facebook/react/pull/32262))

---

January 16, 2025

- fix[DevTools]: fix HostComponent naming in filters for Native ([hoxyq](https://github.com/hoxyq) in [#32086](https://github.com/facebook/react/pull/32086))
- Fix copy functionality in Firefox ([V3RON](https://github.com/V3RON) in [#32077](https://github.com/facebook/react/pull/32077))
- Prevent crash when starting consecutive profiling sessions ([V3RON](https://github.com/V3RON) in [#32066](https://github.com/facebook/react/pull/32066))
- fix[DevTools/Tree]: only scroll to item when panel is visible ([hoxyq](https://github.com/hoxyq) in [#32018](https://github.com/facebook/react/pull/32018))
- feat[Tree]: set initial scroll offset when inspected element index is set ([hoxyq](https://github.com/hoxyq) in [#31968](https://github.com/facebook/react/pull/31968))
- DevTools: fix initial host instance selection ([hoxyq](https://github.com/hoxyq) in [#31892](https://github.com/facebook/react/pull/31892))
- chore[DevTools/Tree]: don't pre-select root element ([hoxyq](https://github.com/hoxyq) in [#32015](https://github.com/facebook/react/pull/32015))
- Show component names while highlighting renders ([piotrski](https://github.com/piotrski) in [#31577](https://github.com/facebook/react/pull/31577))
- allow non-coercible objects in formatConsoleArgumentsToSingleString ([henryqdineen](https://github.com/henryqdineen) in [#31444](https://github.com/facebook/react/pull/31444))

---

October 15, 2024

- Fix React Compiler badging ([poteto](https://github.com/poteto) in [#31196](https://github.com/facebook/react/pull/31196))
- fix[react-devtools]: record timeline data only when supported ([hoxyq](https://github.com/hoxyq) in [#31154](https://github.com/facebook/react/pull/31154))
- fix[react-devtools]: remove all listeners when Agent is shutdown ([hoxyq](https://github.com/hoxyq) in [#31151](https://github.com/facebook/react/pull/31151))
- fix[react-devtools]: wrap key string in preformatted text html element ([hoxyq](https://github.com/hoxyq) in [#31153](https://github.com/facebook/react/pull/31153))
- fix[react-devtools]: request hook initialization inside http server response ([hoxyq](https://github.com/hoxyq) in [#31102](https://github.com/facebook/react/pull/31102))
- refactor: allow custom impl of backend reload-to-profile support check ([EdmondChuiHW](https://github.com/EdmondChuiHW) in [#31048](https://github.com/facebook/react/pull/31048))

---

September 25, 2024

- Support Server Components in Tree ([sebmarkbage](https://github.com/sebmarkbage) in [#30684](https://github.com/facebook/react/pull/30684))
- feat: expose installHook with settings argument from react-devtools-core/backend ([hoxyq](https://github.com/hoxyq) in [#30987](https://github.com/facebook/react/pull/30987))
- Add Filtering of Environment Names ([sebmarkbage](https://github.com/sebmarkbage) in [#30850](https://github.com/facebook/react/pull/30850))
- Support secondary environment name when it changes ([sebmarkbage](https://github.com/sebmarkbage) in [#30842](https://github.com/facebook/react/pull/30842))
- Filter Server Components ([sebmarkbage](https://github.com/sebmarkbage) in [#30839](https://github.com/facebook/react/pull/30839))
- Make function inspection instant ([sebmarkbage](https://github.com/sebmarkbage) in [#30786](https://github.com/facebook/react/pull/30786))
- Make Functions Clickable to Jump to Definition ([sebmarkbage](https://github.com/sebmarkbage) in [#30769](https://github.com/facebook/react/pull/30769))
- [Flight/DevTools] Pass the Server Component's "key" as Part of the ReactComponentInfo ([sebmarkbage](https://github.com/sebmarkbage) in [#30703](https://github.com/facebook/react/pull/30703))
- Make Element Inspection Feel Snappy ([sebmarkbage](https://github.com/sebmarkbage) in [#30555](https://github.com/facebook/react/pull/30555))
- Print component stacks as error objects to get source mapping ([sebmarkbage](https://github.com/sebmarkbage) in [#30289](https://github.com/facebook/react/pull/30289))

- Fix: profiling crashes #30661 #28838 ([EdmondChuiHW](https://github.com/EdmondChuiHW) in [#31024](https://github.com/facebook/react/pull/31024))
- chore: remove settings manager from react-devtools-core ([hoxyq](https://github.com/hoxyq) in [#30986](https://github.com/facebook/react/pull/30986))
- fix[react-devtools/extensions]: fixed tabs API calls and displaying restricted access popup ([hoxyq](https://github.com/hoxyq) in [#30825](https://github.com/facebook/react/pull/30825))
- fix[react-devtools/InspectedElement]: fixed border stylings when some of the panels are not rendered ([hoxyq](https://github.com/hoxyq) in [#30676](https://github.com/facebook/react/pull/30676))
- fix: path handling in react devtools ([Jack-Works](https://github.com/Jack-Works) in [#29199](https://github.com/facebook/react/pull/29199))

- feat: display message if user ended up opening hook script ([hoxyq](https://github.com/hoxyq) in [#31000](https://github.com/facebook/react/pull/31000))
- refactor[react-devtools]: move console patching to global hook ([hoxyq](https://github.com/hoxyq) in [#30596](https://github.com/facebook/react/pull/30596))
- refactor[react-devtools]: initialize renderer interface early ([hoxyq](https://github.com/hoxyq) in [#30946](https://github.com/facebook/react/pull/30946))
- Use Unicode Atom Symbol instead of Atom Emoji ([sebmarkbage](https://github.com/sebmarkbage) in [#30832](https://github.com/facebook/react/pull/30832))
- feat[react-devtools]: support Manifest v3 for Firefox extension ([hoxyq](https://github.com/hoxyq) in [#30824](https://github.com/facebook/react/pull/30824))
- Enable pointEvents while scrolling ([sebmarkbage](https://github.com/sebmarkbage) in [#30560](https://github.com/facebook/react/pull/30560))

---

July 3, 2024

- chore[react-devtools/renderer]: dont show strict mode warning for prod renderer builds ([hoxyq](https://github.com/hoxyq) in [#30158](https://github.com/facebook/react/pull/30158))
- chore[react-devtools/ui]: fix strict mode badge styles ([hoxyq](https://github.com/hoxyq) in [#30159](https://github.com/facebook/react/pull/30159))
- fix[react-devtools]: restore original args when recording errors ([hoxyq](https://github.com/hoxyq) in [#30091](https://github.com/facebook/react/pull/30091))
- Read constructor name more carefully ([LoganDark](https://github.com/LoganDark) in [#29954](https://github.com/facebook/react/pull/29954))
- refactor[react-devtools/extensions]: dont debounce cleanup logic on navigation ([hoxyq](https://github.com/hoxyq) in [#30027](https://github.com/facebook/react/pull/30027))

---

June 17, 2024

- chore[react-devtools]: improve console arguments formatting before passing it to original console ([hoxyq](https://github.com/hoxyq) in [#29873](https://github.com/facebook/react/pull/29873))
- chore[react-devtools]: unify console patching and default to ansi escape symbols ([hoxyq](https://github.com/hoxyq) in [#29869](https://github.com/facebook/react/pull/29869))
- chore[react-devtools/extensions]: make source maps url relative ([hoxyq](https://github.com/hoxyq) in [#29886](https://github.com/facebook/react/pull/29886))
- fix[react-devtools] divided inspecting elements between inspecting do… ([vzaidman](https://github.com/vzaidman) in [#29885](https://github.com/facebook/react/pull/29885))
- fix[react-devtools] component badge in light mode is now not invisible ([vzaidman](https://github.com/vzaidman) in [#29852](https://github.com/facebook/react/pull/29852))
- fix[react-devtools] remove native inspection button when it can't be used ([vzaidman](https://github.com/vzaidman) in [#29779](https://github.com/facebook/react/pull/29779))
- chore[react-devtools]: ip => internal-ip ([hoxyq](https://github.com/hoxyq) in [#29772](https://github.com/facebook/react/pull/29772))
- Fix #29724: `ip` dependency update for CVE-2024-29415 ([Rekl0w](https://github.com/Rekl0w) in [#29725](https://github.com/facebook/react/pull/29725))
- Dim `console` calls on additional Effect invocations due to `StrictMode` ([eps1lon](https://github.com/eps1lon) in [#29007](https://github.com/facebook/react/pull/29007))
- refactor[react-devtools]: rewrite context menus ([hoxyq](https://github.com/hoxyq) in [#29049](https://github.com/facebook/react/pull/29049))

---

May 8, 2024

- feat[react-devtools]: display forget badge for components in profiling session ([hoxyq](https://github.com/hoxyq) in [#29014](https://github.com/facebook/react/pull/29014))
- fix[react-devtools]: add backwards compat with legacy element type symbol ([hoxyq](https://github.com/hoxyq) in [#28982](https://github.com/facebook/react/pull/28982))
- Expose "view source" options to Fusebox integration ([motiz88](https://github.com/motiz88) in [#28973](https://github.com/facebook/react/pull/28973))
- Enable inspected element context menu in Fusebox ([motiz88](https://github.com/motiz88) in [#28972](https://github.com/facebook/react/pull/28972))
- Check in `frontend.d.ts` for react-devtools-fusebox, include in build output ([motiz88](https://github.com/motiz88) in [#28970](https://github.com/facebook/react/pull/28970))
- Rename Forget badge ([jbonta](https://github.com/jbonta) in [#28858](https://github.com/facebook/react/pull/28858))
- Devtools: Add support for useFormStatus ([eps1lon](https://github.com/eps1lon) in [#28413](https://github.com/facebook/react/pull/28413))

---

April 15, 2024

- Look for a ReactMemoCacheSentinel on state ([gsathya](https://github.com/gsathya) in [#28831](https://github.com/facebook/react/pull/28831))
- feat[devtools]: add method for connecting backend with custom messaging protocol ([hoxyq](https://github.com/hoxyq) in [#28552](https://github.com/facebook/react/pull/28552))
- feat[devtools]: ship source maps for content scripts and ignore list installHook script ([hoxyq](https://github.com/hoxyq) in [#28730](https://github.com/facebook/react/pull/28730))
- Devtools: Display actual pending state when inspecting `useTransition` ([eps1lon](https://github.com/eps1lon) in [#28499](https://github.com/facebook/react/pull/28499))

---

March 5, 2024

- feat[devtools]: symbolicate source for inspected element ([hoxyq](https://github.com/hoxyq) in [#28471](https://github.com/facebook/react/pull/28471))
- refactor[devtools]: lazily define source for fiber based on component stacks ([hoxyq](https://github.com/hoxyq) in [#28351](https://github.com/facebook/react/pull/28351))
- fix[devtools/tree/element]: onClick -> onMouseDown to handle first click correctly ([hoxyq](https://github.com/hoxyq) in [#28486](https://github.com/facebook/react/pull/28486))
- Devtools: Unwrap Promise in useFormState ([eps1lon](https://github.com/eps1lon) in [#28319](https://github.com/facebook/react/pull/28319))
- Include server component names in the componentStack in DEV ([sebmarkbage](https://github.com/sebmarkbage) in [#28415](https://github.com/facebook/react/pull/28415))

---

February 22, 2024

- feature[REMOVED][devtools]: turn off / hide location based component filters ([hoxyq](https://github.com/hoxyq) in [#28417](https://github.com/facebook/react/pull/28417))
- Add useSyncExternalStore and useTransition to getPrimitiveStackCache ([jamesbvaughan](https://github.com/jamesbvaughan) in [#28399](https://github.com/facebook/react/pull/28399))
- chore[devtools]: use react-window from npm and bump react-virtualized-auto-sizer to ^1.0.23 ([hoxyq](https://github.com/hoxyq) in [#28408](https://github.com/facebook/react/pull/28408))
- [Debug Tools] Always use includeHooksSource option ([sebmarkbage](https://github.com/sebmarkbage) in [#28309](https://github.com/facebook/react/pull/28309))
- [Debug Tools] Introspect Promises in use() ([sebmarkbage](https://github.com/sebmarkbage) in [#28297](https://github.com/facebook/react/pull/28297))
- fix[devtools/useModalDismissSignal]: use getRootNode for shadow root case support ([hoxyq](https://github.com/hoxyq) in [#28145](https://github.com/facebook/react/pull/28145))
- DevTools: Add support for use(Context) ([eps1lon](https://github.com/eps1lon) in [#28233](https://github.com/facebook/react/pull/28233))
- Patch devtools before running useMemo function in strict mode ([gsathya](https://github.com/gsathya) in [#28249](https://github.com/facebook/react/pull/28249))
- DevTools: Add support for useFormState ([eps1lon](https://github.com/eps1lon) in [#28232](https://github.com/facebook/react/pull/28232))
- DevTools: Add support for useOptimistic Hook ([eps1lon](https://github.com/eps1lon) in [#27982](https://github.com/facebook/react/pull/27982))

---

November 29, 2023

- refactor[devtools]: highlight an array of elements for native ([hoxyq](https://github.com/hoxyq) in [#27734](https://github.com/facebook/react/pull/27734))

- feat[devtools]: display Forget badge for the relevant components ([hoxyq](https://github.com/hoxyq) in [#27709](https://github.com/facebook/react/pull/27709))

- Added windows powershell syntax to build scripts ([PrathamLalwani](https://github.com/PrathamLalwani) in [#27692](https://github.com/facebook/react/pull/27692))
- refactor[react-devtools-shared]: minor parsing improvements and modifications ([hoxyq](https://github.com/hoxyq) in [#27661](https://github.com/facebook/react/pull/27661))

---

October 18, 2023

- fix[devtools/useMemoCache]: add stub for useMemoCache in ReactDebugHook ([hoxyq](https://github.com/hoxyq) in [#27472](https://github.com/facebook/react/pull/27472))
- refactor[react-devtools-extensions]: use globals to eliminate dead code ([hoxyq](https://github.com/hoxyq) in [#27516](https://github.com/facebook/react/pull/27516))
- fix[devtools/inspectElement]: dont pause initial inspectElement call when user switches tabs ([hoxyq](https://github.com/hoxyq) in [#27488](https://github.com/facebook/react/pull/27488))

---

September 25, 2023

- feat:-Added a delete all filters action and added title to the add filter a… ([Biki-das](https://github.com/Biki-das) in [#27332](https://github.com/facebook/react/pull/27332))
- feat[devtools/extension]: add dark theme for popup ([rakleed](https://github.com/rakleed) in [#27330](https://github.com/facebook/react/pull/27330))

- refactor[devtools/extension]: refactored messaging logic across different parts of the extension ([hoxyq](https://github.com/hoxyq) in [#27417](https://github.com/facebook/react/pull/27417))
- fix[devtools/extension]: added a workaround for proxy content script injection in firefox ([hoxyq](https://github.com/hoxyq) in [#27375](https://github.com/facebook/react/pull/27375))
- fix[devtools/useTransition]: don't check for dispatch property when determining if hook is stateful ([hoxyq](https://github.com/hoxyq) in [#27365](https://github.com/facebook/react/pull/27365))
- feat[devtools/extension]: show disclaimer when page doesnt run react and refactor react polling logic ([hoxyq](https://github.com/hoxyq) in [#27373](https://github.com/facebook/react/pull/27373))
- fix[devtools/extension]: unregister dynamically injected content scripts instead of filtering ([hoxyq](https://github.com/hoxyq) in [#27369](https://github.com/facebook/react/pull/27369))
- refactor[devtools/extension]: more stable element updates polling to avoid timed out errors ([hoxyq](https://github.com/hoxyq) in [#27357](https://github.com/facebook/react/pull/27357))

---

September 5, 2023

- refactor[devtools/extension]: handle ports disconnection, instead of frequent reconnection ([hoxyq](https://github.com/hoxyq) in [#27336](https://github.com/facebook/react/pull/27336))
- refactor[devtools/extension]: migrate from using s

... (content truncated)
