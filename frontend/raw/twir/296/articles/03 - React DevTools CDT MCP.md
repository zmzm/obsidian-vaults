---
type: twir-item
issue: 296
item: 3
item_type: item
date: 2026-09-09
source: https://github.com/react/react/tree/main/packages/react-devtools-cdt-mcp
tags:
  - "DevTools"
  - "CDT"
  - "MCP"
  - "Ata"
status: auto
quality: keep
---

[[2026-09-09-TWIR-296|Index]]

# Item 3: React DevTools CDT MCP

Source: [https://github.com/react/react/tree/main/packages/react-devtools-cdt-mcp](https://github.com/react/react/tree/main/packages/react-devtools-cdt-mcp)

Summary:
The react-devtools-cdt-mcp package is an experimental library for integrating React inspection and profiling tools with Chrome DevTools MCP (Multi-Client Protocol). It exposes APIs for inspecting component trees, props, hooks, and profiling data, intended for use in trusted debugging sessions. The library requires chrome-devtools-mcp 1.3.0+ and is designed for advanced users needing programmatic or third-party tool integration.

Key takeaways:
- Provides programmatic access to React component and profiling data via Chrome DevTools MCP.
- Supports inspection of component trees, props, hooks, source locations, owner/parent stacks, and profiling sessions.
- Intended for advanced/experimental workflows; requires specific setup and is not for general end-user use.
- UIDs are stable across re-renders but not page reloads; output is structured for easy consumption.

Recommendation:
Read fully (read fully if you are building custom devtools or automation around React debugging/profiling)

Why it matters:
read fully if you are building custom devtools or automation around React debugging/profiling

Content:
# react/packages/react-devtools-cdt-mcp at main · react/react · GitHub

This is an **experimental** library. It is based on the [experimental
third-party developer tools API](https://developer.chrome.com/blog/devtools-for-agents-3p-tools) in chrome-devtools-mcp.

Browser library that registers React inspection and profiling tools with
[chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp).

This is **not** an MCP server and does not go in your MCP client config.
Import it in the page under test; chrome-devtools-mcp discovers the React
tools from the page.

Third-party tools are experimental. They require **chrome-devtools-mcp 1.3.0+**
and `--categoryExperimentalThirdParty=true`.

```
npm install react-devtools-cdt-mcp
```

Import the register entry **before** React so the DevTools hook is installed
before React initializes:

```
import 'react-devtools-cdt-mcp/register';
import React from 'react';
```

`react-devtools-cdt-mcp/register` throws outside a browser-like environment.
The package root is side-effect-free and exports the lower-level API for custom
targets:

```
import {register, buildToolGroup} from 'react-devtools-cdt-mcp';
```

## chrome-devtools-mcp setup

Add the experimental third-party category to your MCP client config:

```
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@latest",
        "--categoryExperimentalThirdParty=true"
      ]
    }
  }
}
```

When the page runs under chrome-devtools-mcp, the React tools are listed by
`list_3p_developer_tools` and callable either via
`execute_3p_developer_tool({toolName, params})` or directly via `evaluate_script`
(`window.__dtmcp.executeTool(toolName, params)`).

These tools can expose component props and hook values to the MCP client. Use
them in local or otherwise trusted debugging sessions.

- **UIDs** — components are identified by a stable uid like `r5`. UIDs
  are consistent across every tool and across re-renders. These UIDs don't survive page reloads.
- **Output** — every tool returns the shape described below as a plain
  JavaScript value. On failure a tool returns `{error: string}` instead.
- **Durations** — profiler durations are in milliseconds, or `null` when the
  build does not collect profiling timing.

Snapshot of the component tree.

- **Input:** `depth?` (number, max depth, default 20), `rootUid?` (string,
  start from this component).
- **Output:** `{nodes}` where `nodes` is an array of
  `{uid, type, name, key, firstChild, nextSibling}`. `firstChild` and
  `nextSibling` reference other nodes by uid (or are `null`).

### `react_get_component_by_uid`

Detailed info for a single component.

- **Input:** `uid` (string, required), `includeHooks?` (boolean, default
  `false`).
- **Output:** `{uid, type, name, key?, props?, hooks?}`. `props` excludes
  children and is normalized to a serialization-safe shape; when `includeHooks`
  is true, `hooks` (function, forwardRef, and memo components) is an array of
  `{id, name, value, subHooks}`. Inspecting hooks re-renders the component's
  render function; effects are not run.

### `react_get_component_by_dom_element`

Detailed info for the React host component corresponding to a DOM element
(the host node itself, not the function component that rendered it).

- **Input:** `element` (object, required). This is an opaque page-side DOM
  element reference. Chrome DevTools MCP clients pass this as
  `{uid: string}`, using an element uid from the page snapshot.
- **Output:** `{uid, type, name, key?, props?}`.

Find components by case-insensitive name substring.

- **Input:** `name` (string, required), `rootUid?` (string, limit to subtree),
  `page?` (number, default 1), `pageSize?` (number, default 10).
- **Output:** `{page, pageSize, totalCount, totalPages, results}` where
  `results` is an array of tree nodes (same shape as `react_get_component_tree`).

### `react_get_component_source`

Definition source location of a component.

- **Input:** `uid` (string, required).
- **Output:** `{source: {name, fileName, line, column}}`, or `{source: null}`
  when the location cannot be determined (e.g. host components, production
  builds).

### `react_get_owner_stack_trace`

Raw owner stack trace — the chain of JSX creation locations up to the root.

- **Input:** `uid` (string, required).
- **Output:** `{stack: string}` (DEV-only; empty in production).

Rendered parent list — where a component is mounted in the rendered component
tree.

- **Input:** `uid` (string, required).
- **Output:** an array of `{uid, name, type}`, ordered from immediate parent to
  root (empty for the root). This can include host DOM components and the root.

Structured owner list — which components created/rendered this element through
JSX.

- **Input:** `uid` (string, required).
- **Output:** an array of `{uid, name, type}`, ordered from immediate owner to
  root owner (empty for a root component). DEV-only. Owners are not structural
  parents; use `react_get_parent_stack` for mounted tree ancestry.

Start a profiling session that records per-commit render timing.

- **Input:** `traceName?` (string, trace name; auto-generated if omitted).
- **Output:** `{status: "started", traceName}`.

Stop the active profiling session.

- **Input:** none.
- **Output:** `{status: "stopped", traceName, commits}` (`commits` is the number of
  commits recorded).

Per-commit overview of a recorded trace.

- **Input:** `traceName` (string, required).
- **Output:** array of
  `{commit, committedAt, renderDuration, layoutDuration, passiveDuration, componentsChanged}`,
  one row per commit.

Detailed report for a single commit.

- **Input:** `traceName` (string, required), `commitIndex` (number, required;
  zero-based).
- **Output:**
  `{committedAt, priority, renderDuration, layoutDuration, passiveDuration, components}`
  where `components` is an array of
  `{uid, name, type, actualDuration, selfDuration}` sorted by `actualDuration`
  descending.
