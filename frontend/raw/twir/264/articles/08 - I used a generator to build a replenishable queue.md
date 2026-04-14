---
type: twir-item
issue: 264
item: 8
item_type: item
date: 2026-01-14
source: https://macarthur.me/posts/queue/
tags:
status: auto
---

[[2026-01-14-TWIR-264|Index]]

# Item 8: I used a generator to build a replenishable queue

Source: [https://macarthur.me/posts/queue/](https://macarthur.me/posts/queue/)

Summary:
The author describes building a replenishable FIFO queue using JavaScript generators, overcoming the typical one-way nature of generators by integrating promises to pause and resume processing. The approach is illustrated with practical code and is later adapted for use in React, supporting dynamic workloads like file uploads.

Key takeaways:
- Generators can be combined with promises to create queues that pause and resume as items are added.
- This pattern is useful for managing asynchronous, replenishable work streams.
- The technique is adaptable to React UIs needing controlled, sequential processing.
- Offers a clean, reusable API for queue management.

Recommendation: Summary sufficient
