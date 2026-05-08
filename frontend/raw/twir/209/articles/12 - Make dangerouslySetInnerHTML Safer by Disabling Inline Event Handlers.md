---
type: twir-item
issue: 209
item: 12
item_type: item
date: 2024-11-13
source: https://macarthur.me/posts/safer-dangerouslysetinnerhtml/
tags:
  - "dangerouslySetInnerHTML"
  - "TS"
status: auto
quality: keep
---

[[2024-11-13-TWIR-209|Index]]

# Item 12: Make dangerouslySetInnerHTML Safer by Disabling Inline Event Handlers

Source: [https://macarthur.me/posts/safer-dangerouslysetinnerhtml/](https://macarthur.me/posts/safer-dangerouslysetinnerhtml/)

Summary:
The post highlights a security risk with React's dangerouslySetInnerHTML: inline event handlers (e.g., onclick) are not blocked and can execute arbitrary JavaScript. The author demonstrates how to sanitize HTML to remove these handlers, either using DOMParser or a regular expression, and provides a SafeElement component that strips unsafe attributes before rendering.

Key takeaways:
- dangerouslySetInnerHTML does not block inline event handlers, posing XSS risks.
- Use a sanitization step (DOMParser or regex) to remove on* attributes before rendering.
- Regular expressions offer a more performant, though less robust, solution than DOMParser.
- For full safety, consider established HTML sanitization libraries or strict Content Security Policies.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
