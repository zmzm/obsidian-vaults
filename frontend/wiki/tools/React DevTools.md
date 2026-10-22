---
type: tool
status: active
updated: 2026-10-22
tags: [react, devtools, profiling, suspense, ai]
---

# React DevTools

React DevTools connects component structure, state, and render timing to what appears in the browser. The captured 8.0 material also makes Suspense boundaries and hidden Activity trees easier to inspect.

## Key Ideas

- Use component and owner/parent inspection to locate responsibility; DOM ancestry and JSX ownership answer different questions.
- The captured 8.0 changelog enables the Suspense tab by default, adds a React Element pane, and retires the separate Timeline profiler in favor of browser Performance tracks.
- The Suspense panel exposes reveal order and waiting boundaries. Pair it with network traces and fallback geometry to distinguish slow data, sequential discovery, and layout shifts.
- The experimental react-devtools-cdt-mcp package runs in the page and registers React tools discovered by Chrome DevTools MCP. It is a browser library rather than a separate MCP server.
- Install the hook before React initializes. Keep this bridge in trusted development sessions: it exposes props/hooks and adds commit-reporting overhead; component UIDs survive rerenders but not reloads.

## Practical Significance

- Start from a slow interaction or visible loading boundary, identify responsible components, record a trace, and compare after a focused change.
- Agent access to runtime component evidence can reduce guesswork, but development instrumentation timings are not production latency measurements.

## Related Pages

- [[../topics/React Rendering|React Rendering]]
- [[../concepts/React Activity|React Activity]]
- [[../patterns/Component Confidence Boundaries|Component Confidence Boundaries]]
- [[../syntheses/Frameworks as Constraints in the AI Era|Frameworks as Constraints in the AI Era]]

## Sources

- [[../../raw/twir/296/articles/02 - React DevTools 8.0 - Suspense Tab enabled, React Element panel, remove Timeline profiler in favor of Performance tracks, display dimmed|02 - React DevTools 8.0 - Suspense Tab enabled, React Element panel, remove Timeline profiler in favor of Performance tracks, display dimmed]]
- [[../../raw/twir/296/articles/03 - React DevTools CDT MCP|03 - React DevTools CDT MCP]]
- [[../../raw/twir/301/articles/10 - Debugging Suspense with the React Suspense Panel|10 - Debugging Suspense with the React Suspense Panel]]
- [[../../raw/twir/302/articles/05 - React docs - React DevTools for agents|05 - React docs - React DevTools for agents]]

## Open Questions

- How much boundary and timing detail is available in each React/build configuration?
- Which runtime observations should be captured alongside end-user journey metrics?
