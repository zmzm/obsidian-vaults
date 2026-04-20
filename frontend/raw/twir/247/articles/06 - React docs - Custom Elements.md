---
type: twir-item
issue: 247
item: 6
item_type: item
date: 2025-08-27
source: https://react.dev/reference/react-dom/components#custom-html-elements
tags:
status: auto
quality: keep
---

[[2025-08-27-TWIR-247|Index]]

# Item 6: React docs - Custom Elements

Source: [https://react.dev/reference/react-dom/components#custom-html-elements](https://react.dev/reference/react-dom/components#custom-html-elements)

Summary:
The React documentation now provides comprehensive guidance on using custom HTML and SVG elements, including how React treats tags with dashes as custom elements and how to pass data via attributes and properties. It covers event handling for custom elements, including case-sensitive event names, and details on prop naming conventions for HTML and SVG elements.

Key takeaways:
- Custom elements are recognized by tag naming or the is attribute; React passes string attributes by default, but can set properties if detected.
- Event listeners on custom elements use the on prefix and are case-sensitive.
- Prop names for HTML/SVG elements use camelCase, and namespaced attributes drop the colon.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
