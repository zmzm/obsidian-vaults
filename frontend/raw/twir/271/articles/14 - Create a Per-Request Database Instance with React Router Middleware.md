---
type: twir-item
issue: 271
item: 14
item_type: item
date: 2026-03-04
source: https://sergiodxa.com/tutorials/create-a-per-request-database-instance-with-middleware
tags:
  - "Router"
  - "Per-Request"
status: auto
---

[[2026-03-04-TWIR-271|Index]]

# Item 14: Create a Per-Request Database Instance with React Router Middleware

Source: [https://sergiodxa.com/tutorials/create-a-per-request-database-instance-with-middleware](https://sergiodxa.com/tutorials/create-a-per-request-database-instance-with-middleware)

Summary:
This tutorial shows how to use React Router middleware to create and clean up a per-request database instance, ensuring proper resource management and transactional integrity. It covers context setup, middleware implementation, and usage patterns for both loaders and actions.

Key takeaways:
- Middleware can manage resource lifecycles (e.g., DB connections) per request in React Router.
- Ensures cleanup (e.g., db.close()) even on errors or early exits.
- Supports transactional patterns for atomic multi-step operations.
- Pattern is extensible to other resources needing setup/teardown.

Recommendation: Summary sufficient
