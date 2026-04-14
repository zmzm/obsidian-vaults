---
type: twir-item
issue: 275
item: 9
item_type: item
date: 2026-04-01
source: https://handlewithcare.dev/blog/making_react_prosemirror_really_really_fast/
tags:
  - "ProseMirror"
status: auto
---

[[2026-04-01-TWIR-275|Index]]

# Item 9: Making React ProseMirror really, really fast

Source: [https://handlewithcare.dev/blog/making_react_prosemirror_really_really_fast/](https://handlewithcare.dev/blog/making_react_prosemirror_really_really_fast/)

Summary:
The article details performance challenges in integrating React with ProseMirror, particularly when rendering large documents. Memoization of components is essential, but passing position (pos) as a prop causes unnecessary rerenders. The solution involves removing pos from props and instead passing a getPos function, reducing the number of rerenders and significantly improving editor performance.

Key takeaways:
- Memoization is critical for performance in React ProseMirror integrations.
- Passing pos as a prop causes widespread rerenders; switching to getPos avoids this.
- The approach enables handling very large documents with minimal lag.
- Highlights the importance of API design for React integrations with non-React libraries.

Recommendation: Read fully (for anyone integrating React with complex, stateful editors)
