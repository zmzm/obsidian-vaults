---
type: twir-item
issue: 272
item: 9
item_type: item
date: 2026-03-11
source: https://sergiodxa.com/tutorials/access-react-router-context-with-asynclocalstorage
tags:
  - "AsyncLocalStorage"
  - "Nodejs"
status: auto
---

[[2026-03-11-TWIR-272|Index]]

# Item 9: How to Access React Router Context with AsyncLocalStorage

Source: [https://sergiodxa.com/tutorials/access-react-router-context-with-asynclocalstorage](https://sergiodxa.com/tutorials/access-react-router-context-with-asynclocalstorage)

Summary:
This tutorial explains how to use Node.js's AsyncLocalStorage to make React Router's context and request objects globally accessible during a request's lifecycle. By wrapping middleware with AsyncLocalStorage, any function can access context/request data without explicit parameter passing. The article also covers using Remix Utils for type-safe middleware and demonstrates practical patterns for accessing session, database, and request data throughout an app.

Key takeaways:
- AsyncLocalStorage enables per-request context sharing without prop drilling.
- Middleware setup ensures context/request are available anywhere in the call stack.
- Remix Utils provides a type-safe, ergonomic API for context storage.
- Useful for simplifying service and utility function signatures in React Router/Remix apps.

Recommendation: Read fully (read fully for setup code or if implementing request-scoped context)
