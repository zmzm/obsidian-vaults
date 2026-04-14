---
type: twir-item
issue: 271
item: 5
item_type: item
date: 2026-03-04
source: https://github.com/reactjs/react.dev/pull/8300
tags:
  - "RSC"
  - "Reactdev"
  - "PR"
  - "Bun"
  - "ServerComponents"
status: auto
---

[[2026-03-04-TWIR-271|Index]]

# Item 5: React.dev PR - Add RSC Sandboxes

Source: [https://github.com/reactjs/react.dev/pull/8300](https://github.com/reactjs/react.dev/pull/8300)

Summary:
This pull request adds a browser-only <SandpackRSC> component to the React documentation site, enabling interactive sandboxes for React Server Components (RSC) using web workers. The implementation leverages react-server-dom-webpack and sucrase for JSX transpilation, with streaming support and ongoing improvements for error handling and CI integration. The PR also discusses bundle size impacts and technical considerations for sandboxing RSCs in documentation.

Key takeaways:
- Enables hands-on RSC experimentation directly in the browser via sandboxes.
- Uses web workers and streaming to mimic server-side RSC execution in the client.
- Ongoing work to improve error handling, streaming, and developer experience.
- Bundle size impact is monitored, with attention to performance.

Recommendation: Summary sufficient (read PR for implementation details or if contributing)

Related notes: [[Server Components]]
