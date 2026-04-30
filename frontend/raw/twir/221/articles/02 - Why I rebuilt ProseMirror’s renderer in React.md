---
type: twir-item
issue: 221
item: 4
item_type: item
date: 2025-02-12
source: https://smoores.dev/post/why_i_rebuilt_prosemirror_view/
tags:
  - "ProseMirror"
status: auto
quality: keep
---

[[2025-02-12-TWIR-221|Index]]

# Item 4: Why I rebuilt ProseMirror’s renderer in React

Source: [https://smoores.dev/post/why_i_rebuilt_prosemirror_view/](https://smoores.dev/post/why_i_rebuilt_prosemirror_view/)

Summary:
A developer recounts the challenges and motivations behind rebuilding the ProseMirror rich text editor's renderer in React for the New York Times. The integration was complex due to fundamental differences between React's and ProseMirror's approaches to DOM updates and state management. The team invested years in understanding both systems, ultimately devising a more robust adapter layer. The article details the technical and organizational journey, including early integration attempts and the rationale for choosing React despite the challenges.

Key takeaways:
- Integrating React and ProseMirror is non-trivial due to differences in DOM and state handling.
- React's unidirectional data flow can conflict with ProseMirror's synchronous updates.
- Deep technical understanding and team collaboration were required for a robust solution.
- React was chosen for its state management strengths and component reuse across the NYT stack.

Recommendation:
Read fully (for those interested in advanced editor integrations or React interop)

Why it matters:
for those interested in advanced editor integrations or React interop

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
