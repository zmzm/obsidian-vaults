---
type: twir-item
issue: 275
item: 3
item_type: item
date: 2026-04-01
source: https://github.com/facebook/react/pull/35816
tags:
  - "TrustedTypes"
  - "PR"
status: auto
quality: keep
---

[[2026-04-01-TWIR-275|Index]]

# Item 3: React PR - Enable Trusted Types integration

Source: [https://github.com/facebook/react/pull/35816](https://github.com/facebook/react/pull/35816)

Summary:
React now supports the browser Trusted Types API, a security feature that helps prevent DOM-based XSS by requiring typed objects (TrustedHTML, TrustedScript, TrustedScriptURL) for DOM injection. Previously, React coerced all values to strings, breaking Trusted Types enforcement. With this change, React passes Trusted Types objects directly to the DOM, supporting use cases like dangerouslySetInnerHTML and attribute assignments without breaking security policies.

Key takeaways:
- Trusted Types objects are preserved and passed to the DOM, enabling secure integration for sites enforcing Trusted Types via CSP.
- No breaking changes for sites not using Trusted Types; normal string values continue to work as before.
- Applies to dangerouslySetInnerHTML, HTML/SVG attributes, and URL attributes.
- Fixes a longstanding incompatibility for security-conscious React applications.

Recommendation:
Summary sufficient

Content:
# [flags] land `enableTrustedTypesIntegration` by rickhanlonii · Pull Request #35816 · facebook/react · GitHub

```
## Summary

This flag enables React's integration with the browser [Trusted Types
API](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API).

The Trusted Types API is a browser security feature that helps prevent
DOM-based XSS attacks. When a site enables Trusted Types enforcement via
`Content-Security-Policy: require-trusted-types-for 'script'`, the
browser requires that values passed to DOM injection sinks (like
`innerHTML`) are typed objects (`TrustedHTML`, `TrustedScript`,
`TrustedScriptURL`) created through developer-defined sanitization
policies, rather than raw strings.

 ### What changed

Previously, React always coerced values to strings (via `'' + value`)
before passing them to DOM APIs like `setAttribute` and `innerHTML`.
This broke Trusted Types because it converted typed objects into plain
strings, which the browser would then reject under Trusted Types
enforcement.

React now passes values directly to DOM APIs without string coercion,
preserving Trusted Types objects so the browser can validate them. This
applies to `dangerouslySetInnerHTML`, all HTML and SVG attributes, and
URL attributes (`href`, `action`, etc).

 ### Before (broken)

Using Trusted Types with something like`dangerouslySetInnerHTML` would
throw:

 ```js
 const sanitizer = trustedTypes.createPolicy('sanitizer', {
   createHTML: (input) => DOMPurify.sanitize(input),
 });

 function Comment({text}) {
   const clean = sanitizer.createHTML(text);
   // clean is a TrustedHTML object, but React would call '' + clean,
   // converting it back to a plain string before setting innerHTML.
   // Under Trusted Types enforcement, the browser rejects the string:
   //
   //   TypeError: Failed to set 'innerHTML' on 'Element':
   //   This document requires 'TrustedHTML' assignment.
   return <div dangerouslySetInnerHTML={{__html: clean}} />;
 }
 ```

### After (works)

React now passes the TrustedHTML object directly to the DOM without
stringifying it:

```js
 const policy = trustedTypes.createPolicy('sanitizer', {
   createHTML: (input) => DOMPurify.sanitize(input),
 });

 function Comment({text}) {
   // TrustedHTML objects are passed directly to innerHTML
   return <div dangerouslySetInnerHTML={{__html: policy.createHTML(text)}} />;
 }

 function UserProfile({bio}) {
   // String attribute values also preserve Trusted Types objects
   return <div data-bio={policy.createHTML(bio)} />;
 }
 ```

 ## Non-breaking change

 - Sites using Trusted Types: React no longer breaks Trusted Types enforcement. TrustedHTML and TrustedScriptURL objects passed through React props are forwarded to the DOM without being stringified.
 - Sites not using Trusted Types: No behavior change. DOM APIs accept both strings and Trusted Types objects, so removing the explicit string coercion is functionally identical.

DiffTrain build for [074d96b](074d96b)
```
