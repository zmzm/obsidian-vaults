---
type: twir-item
issue: 207
item: 6
item_type: item
date: 2024-10-30
source: https://expressionstatement.com/html-form-validation-is-heavily-underused
tags:
  - "HTML"
status: auto
quality: keep
---

[[2024-10-30-TWIR-207|Index]]

# Item 6: HTML Form Validation is heavily underused

Source: [https://expressionstatement.com/html-form-validation-is-heavily-underused](https://expressionstatement.com/html-form-validation-is-heavily-underused)

Summary:
The article argues that native HTML form validation is underutilized, especially the setCustomValidity method, which allows for custom validation logic. While attributes like required and type are declarative and easy to use, setCustomValidity is imperative and requires boilerplate to integrate with React. The author proposes a more declarative approach, such as a custom-validity prop, and demonstrates how to implement this pattern in React for better ergonomics.

Key takeaways:
- Native HTML validation attributes are easy, but setCustomValidity is powerful yet cumbersome in React.
- Handling custom validity in React requires useRef, useLayoutEffect, and onChange, leading to duplicated logic.
- A declarative custom-validity prop would improve developer experience and code maintainability.
- Boilerplate and imperative APIs are barriers to wider adoption of native form validation.

Recommendation:
Read fully (read fully if you want to improve form validation patterns in React)

Why it matters:
read fully if you want to improve form validation patterns in React

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
