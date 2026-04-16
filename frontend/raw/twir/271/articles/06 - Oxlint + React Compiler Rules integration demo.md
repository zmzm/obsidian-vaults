---
type: twir-item
issue: 271
item: 6
item_type: item
date: 2026-03-04
source: https://github.com/TheAlexLichter/oxlint-react-compiler-rules
tags:
  - "ReactCompiler"
status: auto
quality: keep
---

[[2026-03-04-TWIR-271|Index]]

# Item 6: Oxlint + React Compiler Rules integration demo

Source: [https://github.com/TheAlexLichter/oxlint-react-compiler-rules](https://github.com/TheAlexLichter/oxlint-react-compiler-rules)

Summary:
This project demonstrates how to use React Compiler/Hook rules within Oxlint by leveraging its jsPlugins feature to load ESLint plugins. The setup allows React developers to enforce linting rules (like preventing setState in render) using Oxlint, even when rules are not natively ported to Rust. The included demo app shows the linter catching common React anti-patterns.

Key takeaways:
- Oxlint can run ESLint React rules via jsPlugins, enabling advanced linting in Rust-based workflows.
- Developers can enforce React best practices (e.g., no setState in render) with minimal configuration.
- Demo app illustrates practical usage and error detection.

Recommendation:
Summary sufficient

Content:
# TheAlexLichter/oxlint-react-compiler-rules: Demo of using React Compiler rules through Oxlint's JS plugin feature. · GitHub

# Oxlint + React Compiler Rules

This project demonstrates using React Compiler rules through Oxlint's JS plugin feature.

## Using React Compiler Rules with Oxlint

[A lot of common rules](https://oxc.rs/docs/guide/usage/linter/rules.html#rules) have been ported over to Rust and can run natively in Oxlint, however Oxlint supports loading ESLint plugins via the `jsPlugins` configuration. This allows you to use ESLint plugins directly in Oxlint, including React Compiler/Hooks rules.

Add the plugin to your `.oxlintrc.json`:

```
{
  "jsPlugins": [
    {
      "name": "react-hooks-js",
      "specifier": "eslint-plugin-react-hooks"
    }
  ],
  "rules": {
    "react-hooks-js/set-state-in-render": "error"
  }
}
```

The `jsPlugins` array loads the `eslint-plugin-react-hooks` package and makes its rules available under the `react-hooks-js` (or any other custom) namespace. You have to use a different name as `react-hooks` is a reserved name, [given that a big chunk is available through Oxlint itself](https://github.com/oxc-project/oxc/issues/1022). You can then configure individual rules using the plugin namespace as a prefix.

At the time of writing, rules have to be enabled explicitly, as they are not automatically enabled by the plugin.

This repository includes a simple React + Vite 8 beta + Oxlint demo app that demonstrates the `set-state-in-render` rule in action.

The demo app (`src/App.tsx`) contains an intentional bug:

```
export default function App({value}: {value: number}) {
  const [count, setCount] = useState(0);
  setCount(value); // Infinite loop! This will be caught by the linter
  return <div>{count}</div>;
}
```

Calling `setCount` directly in the component body causes an infinite render loop, which the `react-hooks-js/set-state-in-render` rule will detect.

Install dependencies:

Run the linter to see the rule in action:

You should see an error pointing to the problematic `setCount` call in `src/App.tsx:5`.

Start the development server:

Related notes: [[React Compiler]]
