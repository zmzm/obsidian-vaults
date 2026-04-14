---
type: twir-item
issue: 275
item: 8
item_type: item
date: 2026-04-01
source: https://julesblom.com/writing/colocated-svg-defs
tags:
  - "SVG"
status: auto
---

[[2026-04-01-TWIR-275|Index]]

# Item 8: Hoistable SVG Defs in React

Source: [https://julesblom.com/writing/colocated-svg-defs](https://julesblom.com/writing/colocated-svg-defs)

Summary:
This article explores the challenge of managing SVG definitions (<defs>) in React, especially regarding ID collisions and component encapsulation. It demonstrates how to colocate SVG definitions with components using React portals and context, ultimately rendering all definitions into a single <defs> element at the top of the SVG. The approach avoids duplication, enables component ownership of definitions, and prevents ID clashes.

Key takeaways:
- Inline SVGs can suffer from ID collisions; colocating <defs> with components helps but can cause duplication.
- Using React portals and context, definitions authored in components are hoisted into a single <defs> element.
- This pattern enables encapsulation and avoids duplicated or scattered definitions.
- The solution is analogous to React 19’s handling of <head> elements.

Recommendation: Read fully (especially for those working with complex SVGs in React)
