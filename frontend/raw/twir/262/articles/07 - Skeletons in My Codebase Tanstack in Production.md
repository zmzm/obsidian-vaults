---
type: twir-item
issue: 262
item: 7
item_type: item
date: 2025-12-10
source: https://oscargabriel.dev/blog/skeletons-in-my-codebase
tags:
status: auto
---

[[2025-12-10-TWIR-262|Index]]

# Item 7: Skeletons in My Codebase: Tanstack in Production

Source: [https://oscargabriel.dev/blog/skeletons-in-my-codebase](https://oscargabriel.dev/blog/skeletons-in-my-codebase)

Summary:
This article shares practical lessons from building a production app with TanStack Router and Better Auth, focusing on real-world architectural decisions and pitfalls. It covers route organization, layout patterns, authentication handling, and strategies to avoid common issues like race conditions and broken loading states. The author advocates for feature-based layouts and clear boundaries to manage complexity.

Key takeaways:
- TanStack Router offers flexibility but requires deliberate architectural choices, especially for layouts and auth guards.
- Feature-based directories with colocated route.tsx layouts and private components (-components/) provide clarity and maintainability.
- Pathless layouts and route groups have trade-offs; feature-based layouts are preferred for shared UI and logic.
- Real-world usage surfaces hidden issues not covered in documentation.

Recommendation: Read fully (for teams adopting TanStack Router or designing scalable React app architectures)
