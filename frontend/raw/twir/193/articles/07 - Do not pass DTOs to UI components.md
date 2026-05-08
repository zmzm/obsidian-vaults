---
type: twir-item
issue: 193
item: 7
item_type: item
date: 2024-07-24
source: https://darios.blog/posts/do-not-pass-dtos-to-ui-components
tags:
  - "DTOs"
  - "UI"
  - "ES"
status: auto
quality: keep
---

[[2024-07-24-TWIR-193|Index]]

# Item 7: Do not pass DTOs to UI components

Source: [https://darios.blog/posts/do-not-pass-dtos-to-ui-components](https://darios.blog/posts/do-not-pass-dtos-to-ui-components)

Summary:
The article warns against passing raw Data Transfer Objects (DTOs) from APIs directly into UI components, as this tightly couples UI to backend data structures and reduces maintainability. Instead, it recommends introducing a data access layer to map DTOs into UI-specific models, promoting separation of concerns and more robust, reusable component interfaces. Practical examples illustrate how to shape and pass only the necessary data to each component.

Key takeaways:
- Passing DTOs directly to UI components couples frontend to backend models, hindering maintainability.
- A data access layer should transform DTOs into UI-focused view models.
- Components should receive only the data they need, supporting the principle of least privilege.
- This approach improves modularity, reusability, and resilience to backend changes.

Recommendation:
Read fully (read fully for practical implementation details)

Why it matters:
read fully for practical implementation details

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
