---
type: twir-item
issue: 194
item: 5
item_type: item
date: 2024-07-31
source: https://reacttraining.com/blog/react-owner-components
tags:
  - "Ownercomponents"
  - "ServerComponents"
status: auto
quality: keep
---

[[2024-07-31-TWIR-194|Index]]

# Item 5: React Owner Components

Source: [https://reacttraining.com/blog/react-owner-components](https://reacttraining.com/blog/react-owner-components)

Summary:
This article revisits the concept of "owner" components in React, distinguishing them from "parent" components, and explains why this distinction matters, especially with server and client components. It clarifies how ownership affects prop passing and re-rendering, and why understanding this is important for React Server Components (RSC) architecture.

Key takeaways:
- "Owner" refers to the component that creates JSX and can pass props; "parent" is about tree hierarchy.
- Owners trigger re-renders of their owned components; parents do not necessarily do so.
- In RSC, only server components can own other server components; client components cannot own server components due to re-rendering constraints.
- The term "owner" is underused but helpful for understanding advanced React patterns.

Recommendation:
Read fully (especially if working with RSC or advanced component architecture)

Why it matters:
especially if working with RSC or advanced component architecture

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
