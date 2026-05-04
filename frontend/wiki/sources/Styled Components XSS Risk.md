---
type: source
status: active
updated: 2026-04-30
tags:
  - security
  - xss
  - css-in-js
---

# Styled Components XSS Risk

This source captures a concrete frontend security risk: interpolating unsanitized user-controlled values into CSS-in-JS can create XSS or data-leak paths.

## Summary

- Dynamic styled-components interpolations are dangerous when they accept arbitrary user input.
- Attackers can abuse CSS injection paths, including external requests and browser-specific behaviors.
- Safer patterns constrain interpolations to booleans, enums, or validated/sanitized values.
- The source broadens the safety branch beyond DOM HTML sinks into CSS and styling APIs.

## Why This Source Matters

- It strengthens `Trusted Types` and `Type-Driven Frontend Safety` with a concrete non-HTML injection scenario.
- It supports the broader point that frontend safety depends on API boundaries and allowed value sets, not only escaping output.
- It gives security guidance a practical component-styling example.

## Caveats

- Trusted Types do not directly solve all CSS-in-JS interpolation risks; this page is adjacent safety evidence, not a direct Trusted Types mechanism.
- The exact exploitability depends on browser behavior, CSS property, and data flow.

## Related Pages

- [[../concepts/Trusted Types|Trusted Types]]
- [[../patterns/Type-Driven Frontend Safety|Type-Driven Frontend Safety]]
- [[React Trusted Types Integration]]
- [[TWIR 218]]

## Raw Sources

- [[../../raw/twir/218/articles/09 - The XSS dangers in interpolating styled-components|The XSS dangers in interpolating styled-components]]
- [[../../raw/twir/218/2025-01-22-TWIR-218|TWIR #218]]
