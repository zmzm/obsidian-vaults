---
type: twir-item
issue: 232
item: 6
item_type: item
date: 2025-04-30
source: https://twofoldframework.com/blog/you-can-serialize-a-promise-in-react
tags:
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-04-30-TWIR-232|Index]]

# Item 6: You can serialize a promise in React

Source: [https://twofoldframework.com/blog/you-can-serialize-a-promise-in-react](https://twofoldframework.com/blog/you-can-serialize-a-promise-in-react)

Summary:
This article explores how React Server Components can serialize promises to enable data that starts on the server and resolves on the client. Traditional JSON serialization fails for promises, but by using streams, you can represent a promise’s lifecycle and transfer it across the network. The post demonstrates how to implement custom serialization and deserialization logic for promises, providing insight into RSC internals.

Key takeaways:
- Promises cannot be serialized with JSON, but can be represented as streams for network transfer.
- Custom serialization enables sharing pending and resolved promise states between server and client.
- Understanding this mechanism is key to grasping how React Server Components manage data flow.

Recommendation:
Read fully (for anyone working with RSCs or interested in advanced React data handling)

Why it matters:
for anyone working with RSCs or interested in advanced React data handling

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
