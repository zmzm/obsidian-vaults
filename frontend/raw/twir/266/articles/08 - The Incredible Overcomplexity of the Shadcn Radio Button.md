---
type: twir-item
issue: 266
item: 8
item_type: item
date: 2026-01-28
source: https://paulmakeswebsites.com/writing/shadcn-radio-button/
tags:
  - "shadcn"
  - "CSS"
status: auto
---

[[2026-01-28-TWIR-266|Index]]

# Item 8: The Incredible Overcomplexity of the Shadcn Radio Button

Source: [https://paulmakeswebsites.com/writing/shadcn-radio-button/](https://paulmakeswebsites.com/writing/shadcn-radio-button/)

Summary:
This article critiques the complexity of Shadcn's radio button implementation, which layers Shadcn and Radix UI components, custom icons, and extensive Tailwind classes over a simple native HTML radio input. The author highlights how the abstraction leads to unnecessary complexity, reliance on ARIA roles, and deviation from the "First Rule of ARIA" (prefer native elements). The piece argues that modern CSS allows for styling native radio buttons directly, making such abstractions often unnecessary.

Key takeaways:
- Shadcn radio buttons wrap Radix primitives, add custom icons, and use many Tailwind classes.
- The abstraction replaces native <input type="radio"> with buttons and ARIA roles, complicating accessibility.
- Native radio buttons can now be styled directly with CSS (appearance: none, pseudo-elements, etc.).
- Overengineering simple UI elements can introduce maintenance and accessibility issues.

Recommendation: Read fully (read fully for a deeper critique or if considering similar abstractions)
