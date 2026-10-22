---
type: twir-item
issue: 301
item: 3
item_type: item
date: 2026-10-14
source: https://github.com/mobxjs/mobx/pull/4735
tags:
  - "MobX"
  - "PR"
  - "One"
  - "Observe"
  - "TS"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2026-10-14-TWIR-301|Index]]

# Item 3: MobX PR - MobX React plugin

Source: [https://github.com/mobxjs/mobx/pull/4735](https://github.com/mobxjs/mobx/pull/4735)

Summary:
MobX introduces a new plugin to simplify React integration and improve compatibility with the React Compiler. The plugin auto-wraps components in observer, adds "use no memo" to ensure MobX controls re-rendering, and transforms async methods to MobX flows, addressing longstanding async/await pain points. The approach is a compromise between full compiler compatibility and MobX’s automatic dependency discovery, with ongoing discussion about future direction.

Key takeaways:
- Plugin automates observer wrapping and disables memoization where MobX is used, aiding React Compiler integration.
- Transforms async methods for better MobX flow compatibility, reducing boilerplate and TypeScript friction.
- Offers a pragmatic path for existing MobX apps to adopt React Compiler without major rewrites.
- Tradeoffs remain between compiler compatibility and MobX’s automatic reactivity model.

Recommendation:
Read fully (if you use MobX, React Compiler, or are evaluating state management approaches)

Why it matters:
if you use MobX, React Compiler, or are evaluating state management approaches

Content:
# MobX React plugin by kubk · Pull Request #4735 · mobxjs/mobx · GitHub

|  |  |
| --- | --- |
| `website/​sidebars.json` | Adds React Compiler documentation. |
| `packages/​mobx/​jest.setup.ts` | Uses shared MobX test setup. |
| `packages/​mobx-react/​jest.setup.ts` | Uses shared React test setup. |
| `packages/​mobx-react-lite/​jest.setup.ts` | Uses shared React test setup. |
| `jest.setup.base.ts` | Centralizes MobX test-state cleanup. |
| `package.json` | Registers the new workspace. |
| `packages/​mobx-react-plugin/​package.json` | Defines package metadata and dependencies. |
| `packages/​mobx-react-plugin/​LICENSE` | Adds the MIT license. |
| `packages/​mobx-react-plugin/​tsconfig.json` | Configures production compilation. |
| `packages/​mobx-react-plugin/​tsconfig.test.json` | Configures test type-checking. |
| `packages/​mobx-react-plugin/​jest.config.js` | Configures plugin tests. |
| `packages/​mobx-react-plugin/​jest.setup.ts` | Initializes MobX test state. |
| `packages/​mobx-react-plugin/​src/​babel.ts` | Provides the Babel entry point. |
| `packages/​mobx-react-plugin/​src/​vite.ts` | Provides the Vite integration. |
| `packages/​mobx-react-plugin/​src/​options.ts` | Defines and normalizes options. |
| `packages/​mobx-react-plugin/​src/​transform.ts` | Implements component and directive transforms. |
| `packages/​mobx-react-plugin/​src/​flow.ts` | Implements async-to-flow conversion. |
| `packages/​mobx-react-plugin/​README.md` | Documents installation, behavior, and options. |
| `packages/​mobx-react-plugin/​__tests__/​vite.test.ts` | Tests Vite integration. |
| `packages/​mobx-react-plugin/​__tests__/​transform.test.ts` | Tests component transforms. |
| `packages/​mobx-react-plugin/​__tests__/​runtime.test.tsx` | Tests React runtime behavior. |
| `packages/​mobx-react-plugin/​__tests__/​react-native.test.ts` | Tests the Metro pipeline. |
| `packages/​mobx-react-plugin/​__tests__/​react-compiler.test.ts` | Tests React Compiler interoperability. |
| `packages/​mobx-react-plugin/​__tests__/​flow.test.ts` | Tests flow transformations. |
| `packages/​mobx-react-plugin/​__tests__/​flow-runtime.test.ts` | Tests transformed flows at runtime. |
| `packages/​mobx-react-plugin/​__tests__/​utils/​transform.ts` | Adds transformation test helpers. |
| `packages/​mobx-react-plugin/​__tests__/​utils/​compiled.ts` | Detects compiler-generated memoization. |
| `packages/​mobx-react-plugin/​__tests__/​fixtures/​rn-project/​babel.config.js` | Configures the React Native fixture. |
| `packages/​mobx-react-plugin/​examples/​react-compiler-vite/​.gitignore` | Ignores generated example files. |
| `packages/​mobx-react-plugin/​examples/​react-compiler-vite/​package.json` | Defines the example application. |
| `packages/​mobx-react-plugin/​examples/​react-compiler-vite/​tsconfig.json` | Configures example TypeScript. |
| `packages/​mobx-react-plugin/​examples/​react-compiler-vite/​vite.config.ts` | Configures the demonstration pipeline. |
| `packages/​mobx-react-plugin/​examples/​react-compiler-vite/​index.html` | Adds the example page shell. |
| `packages/​mobx-react-plugin/​examples/​react-compiler-vite/​README.md` | Documents the example. |
| `packages/​mobx-react-plugin/​examples/​react-compiler-vite/​src/​App.tsx` | Demonstrates protected and unprotected components. |
| `packages/​mobx-react-plugin/​examples/​react-compiler-vite/​src/​main.tsx` | Mounts the example application. |
| `packages/​mobx-react-plugin/​examples/​react-compiler-vite/​src/​store.ts` | Provides observable example state. |
| `packages/​mobx-react-plugin/​examples/​react-compiler-vite/​src/​controls/​UnsafeManualObserver.tsx` | Demonstrates stale compiled output. |
| `packages/​mobx-react-plugin/​examples/​react-compiler-vite/​src/​protected/​AutoObservedCounter.tsx` | Demonstrates automatic observation. |
| `packages/​mobx-react-plugin/​examples/​react-compiler-vite/​src/​protected/​AutoObservedTodos.tsx` | Demonstrates observable collection updates. |
| `packages/​mobx-react-plugin/​examples/​react-compiler-vite/​src/​pure/​PureReactComponent.tsx` | Demonstrates normal compiler optimization. |
| `packages/​mobx-react-plugin/​examples/​react-compiler-vite/​tests/​transform.spec.ts` | Verifies final Vite output. |
| `packages/​mobx-react-plugin/​examples/​react-compiler-vite/​tests/​runtime.spec.tsx` | Verifies example runtime behavior. |
| `docs/​react-compiler.md` | Adds React Compiler guidance. |
| `docs/​react-integration.md` | Links automatic integration guidance. |
| `docs/​installation.md` | Lists the new React plugin. |
| `docs/​actions.md` | Documents automatic flow conversion. |
| `.changeset/​mobx-react-plugin-package.md` | Records the new package release. |

Related notes: [[React Compiler]]
