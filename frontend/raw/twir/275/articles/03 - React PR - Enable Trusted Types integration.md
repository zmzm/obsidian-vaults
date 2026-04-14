---
type: twir-item
issue: 275
item: 3
item_type: item
date: 2026-04-01
source: https://github.com/facebook/react/pull/35816
tags:
status: auto
---

[[2026-04-01-TWIR-275|Index]]

# Item 3: React PR - Enable Trusted Types integration

Source: [https://github.com/facebook/react/pull/35816](https://github.com/facebook/react/pull/35816)

Content:
# [flags] land `enableTrustedTypesIntegration` by rickhanlonii · Pull Request #35816 · facebook/react

[![@rickhanlonii](https://avatars.githubusercontent.com/u/2440089?s=40&u=fce440640002476dda4407828fe8ed0e8885823e&v=4)](https://github.com/rickhanlonii) [rickhanlonii](https://github.com/rickhanlonii) changed the title ~\[flags\] land enableTrustedTypesIntegration~ \[flags\] land `enableTrustedTypesIntegration`

[Feb 18, 2026](https://github.com/facebook/react/pull/35816#event-22891797701)

[![@rickhanlonii](https://avatars.githubusercontent.com/u/2440089?s=40&v=4)](https://github.com/rickhanlonii)

[github-actions](https://github.com/apps/github-actions) bot pushed a commit that referenced this pull request

[Feb 25, 2026](https://github.com/facebook/react/pull/35816#ref-commit-ba27039)

[![@rickhanlonii](https://avatars.githubusercontent.com/u/2440089?s=40&u=fce440640002476dda4407828fe8ed0e8885823e&v=4)](https://github.com/rickhanlonii)

\## Summary

This flag enables React's integration with the browser \[Trusted Types
API\]([https://developer.mozilla.org/en-US/docs/Web/API/Trusted\_Types\_API](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API)).

The Trusted Types API is a browser security feature that helps prevent
DOM-based XSS attacks. When a site enables Trusted Types enforcement via
\`Content-Security-Policy: require-trusted-types-for 'script'\`, the
browser requires that values passed to DOM injection sinks (like
\`innerHTML\`) are typed objects (\`TrustedHTML\`, \`TrustedScript\`,
\`TrustedScriptURL\`) created through developer-defined sanitization
policies, rather than raw strings.

 ### What changed

Previously, React always coerced values to strings (via \`'' + value\`)
before passing them to DOM APIs like \`setAttribute\` and \`innerHTML\`.
This broke Trusted Types because it converted typed objects into plain
strings, which the browser would then reject under Trusted Types
enforcement.

React now passes values directly to DOM APIs without string coercion,
preserving Trusted Types objects so the browser can validate them. This
applies to \`dangerouslySetInnerHTML\`, all HTML and SVG attributes, and
URL attributes (\`href\`, \`action\`, etc).

 ### Before (broken)

Using Trusted Types with something like\`dangerouslySetInnerHTML\` would
throw:

 \`\`\`js
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
   return <div dangerouslySetInnerHTML={{\_\_html: clean}} />;
 }
 \`\`\`

### After (works)

React now passes the TrustedHTML object directly to the DOM without
stringifying it:

\`\`\`js
 const policy = trustedTypes.createPolicy('sanitizer', {
   createHTML: (input) => DOMPurify.sanitize(input),
 });

 function Comment({text}) {
   // TrustedHTML objects are passed directly to innerHTML
   return <div dangerouslySetInnerHTML={{\_\_html: policy.createHTML(text)}} />;
 }

 function UserProfile({bio}) {
   // String attribute values also preserve Trusted Types objects
   return <div data-bio={policy.createHTML(bio)} />;
 }
 \`\`\`

 ## Non-breaking change

 - Sites using Trusted Types: React no longer breaks Trusted Types enforcement. TrustedHTML and TrustedScriptURL objects passed through React props are forwarded to the DOM without being stringified.
 - Sites not using Trusted Types: No behavior change. DOM APIs accept both strings and Trusted Types objects, so removing the explicit string coercion is functionally identical.

DiffTrain build for \[[074d96b](https://github.com/facebook/react/commit/074d96b9dd57ea748f2e869959a436695bbc88bf)\]([074d96b](https://github.com/facebook/react/commit/074d96b9dd57ea748f2e869959a436695bbc88bf))

[github-actions](https://github.com/apps/github-actions) bot pushed a commit that referenced this pull request

[Feb 25, 2026](https://github.com/facebook/react/pull/35816#ref-commit-d360586)

[![@rickhanlonii](https://avatars.githubusercontent.com/u/2440089?s=40&u=fce440640002476dda4407828fe8ed0e8885823e&v=4)](https://github.com/rickhanlonii)

\## Summary

This flag enables React's integration with the browser \[Trusted Types
API\]([https://developer.mozilla.org/en-US/docs/Web/API/Trusted\_Types\_API](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API)).

The Trusted Types API is a browser security feature that helps prevent
DOM-based XSS attacks. When a site enables Trusted Types enforcement via
\`Content-Security-Policy: require-trusted-types-for 'script'\`, the
browser requires that values passed to DOM injection sinks (like
\`innerHTML\`) are typed objects (\`TrustedHTML\`, \`TrustedScript\`,
\`TrustedScriptURL\`) created through developer-defined sanitization
policies, rather than raw strings.

 ### What changed

Previously, React always coerced values to strings (via \`'' + value\`)
before passing them to DOM APIs like \`setAttribute\` and \`innerHTML\`.
This broke Trusted Types because it converted typed objects into plain
strings, which the browser would then reject under Trusted Types
enforcement.

React now passes values directly to DOM APIs without string coercion,
preserving Trusted Types objects so the browser can validate them. This
applies to \`dangerouslySetInnerHTML\`, all HTML and SVG attributes, and
URL attributes (\`href\`, \`action\`, etc).

 ### Before (broken)

Using Trusted Types with something like\`dangerouslySetInnerHTML\` would
throw:

 \`\`\`js
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
   return <div dangerouslySetInnerHTML={{\_\_html: clean}} />;
 }
 \`\`\`

### After (works)

React now passes the TrustedHTML object directly to the DOM without
stringifying it:

\`\`\`js
 const policy = trustedTypes.createPolicy('sanitizer', {
   createHTML: (input) => DOMPurify.sanitize(input),
 });

 function Comment({text}) {
   // TrustedHTML objects are passed directly to innerHTML
   return <div dangerouslySetInnerHTML={{\_\_html: policy.createHTML(text)}} />;
 }

 function UserProfile({bio}) {
   // String attribute values also preserve Trusted Types objects
   return <div data-bio={policy.createHTML(bio)} />;
 }
 \`\`\`

 ## Non-breaking change

 - Sites using Trusted Types: React no longer breaks Trusted Types enforcement. TrustedHTML and TrustedScriptURL objects passed through React props are forwarded to the DOM without being stringified.
 - Sites not using Trusted Types: No behavior change. DOM APIs accept both strings and Trusted Types objects, so removing the explicit string coercion is functionally identical.

DiffTrain build for \[[074d96b](https://github.com/facebook/react/commit/074d96b9dd57ea748f2e869959a436695bbc88bf)\]([074d96b](https://github.com/facebook/react/commit/074d96b9dd57ea748f2e869959a436695bbc88bf))

Merged

[github-actions](https://github.com/apps/github-actions) bot pushed a commit to code/lib-react that referenced this pull request

[Mar 1, 2026](https://github.com/facebook/react/pull/35816#ref-commit-e8d87d4)

[![@pull](https://avatars.githubusercontent.com/in/12910?s=40&v=4)](https://github.com/apps/pull)

\## Summary

This flag enables React's integration with the browser \[Trusted Types
API\]([https://developer.mozilla.org/en-US/docs/Web/API/Trusted\_Types\_API](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API)).

The Trusted Types API is a browser security feature that helps prevent
DOM-based XSS attacks. When a site enables Trusted Types enforcement via
\`Content-Security-Policy: require-trusted-types-for 'script'\`, the
browser requires that values passed to DOM injection sinks (like
\`innerHTML\`) are typed objects (\`TrustedHTML\`, \`TrustedScript\`,
\`TrustedScriptURL\`) created through developer-defined sanitization
policies, rather than raw strings.

 ### What changed

Previously, React always coerced values to strings (via \`'' + value\`)
before passing them to DOM APIs like \`setAttribute\` and \`innerHTML\`.
This broke Trusted Types because it converted typed objects into plain
strings, which the browser would then reject under Trusted Types
enforcement.

React now passes values directly to DOM APIs without string coercion,
preserving Trusted Types objects so the browser can validate them. This
applies to \`dangerouslySetInnerHTML\`, all HTML and SVG attributes, and
URL attributes (\`href\`, \`action\`, etc).

 ### Before (broken)

Using Trusted Types with something like\`dangerouslySetInnerHTML\` would
throw:

 \`\`\`js
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
   return <div dangerouslySetInnerHTML={{\_\_html: clean}} />;
 }
 \`\`\`

### After (works)

React now passes the TrustedHTML object directly to the DOM without
stringifying it:

\`\`\`js
 const policy = trustedTypes.createPolicy('sanitizer', {
   createHTML: (input) => DOMPurify.sanitize(input),
 });

 function Comment({text}) {
   // TrustedHTML objects are passed directly to innerHTML
   return <div dangerouslySetInnerHTML={{\_\_html: policy.createHTML(text)}} />;
 }

 function UserProfile({bio}) {
   // String attribute values also preserve Trusted Types objects
   return <div data-bio={policy.createHTML(bio)} />;
 }
 \`\`\`

 ## Non-breaking change

 - Sites using Trusted Types: React no longer breaks Trusted Types enforcement. TrustedHTML and TrustedScriptURL objects passed through React props are forwarded to the DOM without being stringified.
 - Sites not using Trusted Types: No behavior change. DOM APIs accept both strings and Trusted Types objects, so removing the explicit string coercion is functionally identical.

DiffTrain build for \[[074d96b](https://github.com/code/lib-react/commit/074d96b9dd57ea748f2e869959a436695bbc88bf)\]([facebook@074d96b](https://github.com/facebook/react/commit/074d96b9dd57ea748f2e869959a436695bbc88bf))

[github-actions](https://github.com/apps/github-actions) bot pushed a commit to code/lib-react that referenced this pull request

[Mar 1, 2026](https://github.com/facebook/react/pull/35816#ref-commit-254e741)

[![@pull](https://avatars.githubusercontent.com/in/12910?s=40&v=4)](https://github.com/apps/pull)

\## Summary

This flag enables React's integration with the browser \[Trusted Types
API\]([https://developer.mozilla.org/en-US/docs/Web/API/Trusted\_Types\_API](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API)).

The Trusted Types API is a browser security feature that helps prevent
DOM-based XSS attacks. When a site enables Trusted Types enforcement via
\`Content-Security-Policy: require-trusted-types-for 'script'\`, the
browser requires that values passed to DOM injection sinks (like
\`innerHTML\`) are typed objects (\`TrustedHTML\`, \`TrustedScript\`,
\`TrustedScriptURL\`) created through developer-defined sanitization
policies, rather than raw strings.

 ### What changed

Previously, React always coerced values to strings (via \`'' + value\`)
before passing them to DOM APIs like \`setAttribute\` and \`innerHTML\`.
This broke Trusted Types because it converted typed objects into plain
strings, which the browser would then reject under Trusted Types
enforcement.

React now passes values directly to DOM APIs without string coercion,
preserving Trusted Types objects so the browser can validate them. This
applies to \`dangerouslySetInnerHTML\`, all HTML and SVG attributes, and
URL attributes (\`href\`, \`action\`, etc).

 ### Before (broken)

Using Trusted Types with something like\`dangerouslySetInnerHTML\` would
throw:

 \`\`\`js
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
   return <div dangerouslySetInnerHTML={{\_\_html: clean}} />;
 }
 \`\`\`

### After (works)

React now passes the TrustedHTML object directly to the DOM without
stringifying it:

\`\`\`js
 const policy = trustedTypes.createPolicy('sanitizer', {
   createHTML: (input) => DOMPurify.sanitize(input),
 });

 function Comment({text}) {
   // TrustedHTML objects are passed directly to innerHTML
   return <div dangerouslySetInnerHTML={{\_\_html: policy.createHTML(text)}} />;
 }

 function UserProfile({bio}) {
   // String attribute values also preserve Trusted Types objects
   return <div data-bio={policy.createHTML(bio)} />;
 }
 \`\`\`

 ## Non-breaking change

 - Sites using Trusted Types: React no longer breaks Trusted Types enforcement. TrustedHTML and TrustedScriptURL objects passed through React props are forwarded to the DOM without being stringified.
 - Sites not using Trusted Types: No behavior change. DOM APIs accept both strings and Trusted Types objects, so removing the explicit string coercion is functionally identical.

DiffTrain build for \[[074d96b](https://github.com/code/lib-react/commit/074d96b9dd57ea748f2e869959a436695bbc88bf)\]([facebook@074d96b](https://github.com/facebook/react/commit/074d96b9dd57ea748f2e869959a436695bbc88bf))

Key takeaways:
- No key takeaways extracted.

Recommendation: Summary sufficient
