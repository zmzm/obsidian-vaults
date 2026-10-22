---
type: twir-item
issue: 298
item: 3
item_type: item
date: 2026-09-23
source: https://github.com/react/react/pull/37636
tags:
  - "PR"
status: auto
quality: keep
---

[[2026-09-23-TWIR-298|Index]]

# Item 3: React Flight PR – Server References for arbitrary object types

Source: [https://github.com/react/react/pull/37636](https://github.com/react/react/pull/37636)

Summary:
A new experimental feature in React Flight, behind the enableFlightObjectReferences flag, allows server references to point to arbitrary objects, not just functions. This is achieved via a new API, registerServerObjectReference, which tags objects for server reference in a similar way to server functions. The client receives an opaque handle, which can only be passed back to the server, enabling frameworks to pass request-scoped values by reference and improve cacheability. The initial implementation is in Turbopack bindings, with plans to expand if successful; some edge cases and security considerations are noted in the discussion.

Key takeaways:
- Server references can now represent objects, not just functions, improving flexibility for frameworks.
- Opaque object handles on the client can only be sent back to the server, not inspected or mutated.
- Enables passing request-scoped values (e.g., searchParams) by reference, reducing duplication and improving cacheability.
- Currently experimental and only available in Turbopack; security and serialization edge cases are under discussion.

Recommendation:
Read fully

Content:
# [Flight] Server References for arbitrary object types by acdlite · Pull Request #37636 · react/react · GitHub

```
Pulls the chunk-state machinery out of loadServerReference into two
helpers: resolveServerReferenceChunk (settle a blocked chunk to its
resolved value and wake any listeners) and readServerReference (return a
resolved chunk's value, or wait on a blocked one). loadServerReference
keeps its own local fulfill that computes the value and reports failures
via triggerErrorOnChunk. A follow-up reuses these for references that
point at objects.

Behavior-preserving for the function reference path; the only change is
that its resolution error handling now routes through triggerErrorOnChunk
like the rest of the decoder.
```

```
Added behind a new experimental flag, `enableFlightObjectReferences`.

Extends Server References so that a reference can point to an object,
not just a function. An object is registered with a new API,
`registerServerObjectReference`, which tags it with its module id the
same way `registerServerReference` tags a Server Function.

The client receives an opaque handle: reading a property or calling it
throws, similar to how Temporary References work inside Server
Functions. The only thing the client can do with the handle is pass it
back to the server via a Server Function, where it resolves through the
server manifest.

The motivating use case is letting a framework pass request-scoped
values by reference, so it can omit them from the request body. For
example, a framework could model `searchParams` as a module export
whose value resolves from the current request. This avoids encoding the
search params twice (they already appear in the request URL) but it
also makes the responses more cacheable: if the search params don't
appear elsewhere in the body, then a response cache can omit them from
its cache key.

This initial PR only exposes the new API in the Turbopack bindings. We
will port it to the other bundler configs if the experiment advances.
```

```
Added behind a new experimental flag, `enableFlightObjectReferences`.

Extends Server References so that a reference can point to an object,
not just a function. An object is registered with a new API,
`registerServerObjectReference`, which tags it with its module id the
same way `registerServerReference` tags a Server Function.

The client receives an opaque handle: reading a property or calling it
throws, similar to how Temporary References work inside Server
Functions. The only thing the client can do with the handle is pass it
back to the server via a Server Function, where it resolves through the
server manifest.

The motivating use case is letting a framework pass request-scoped
values by reference, so it can omit them from the request body. For
example, a framework could model `searchParams` as a module export whose
value resolves from the current request. This avoids encoding the search
params twice (they already appear in the request URL) but it also makes
the responses more cacheable: if the search params don't appear
elsewhere in the body, then a response cache can omit them from its
cache key.

This initial PR only exposes the new API in the Turbopack bindings. We
will port it to the other bundler configs if the experiment advances.

DiffTrain build for [71f7255](71f7255)
```

```
Added behind a new experimental flag, `enableFlightObjectReferences`.

Extends Server References so that a reference can point to an object,
not just a function. An object is registered with a new API,
`registerServerObjectReference`, which tags it with its module id the
same way `registerServerReference` tags a Server Function.

The client receives an opaque handle: reading a property or calling it
throws, similar to how Temporary References work inside Server
Functions. The only thing the client can do with the handle is pass it
back to the server via a Server Function, where it resolves through the
server manifest.

The motivating use case is letting a framework pass request-scoped
values by reference, so it can omit them from the request body. For
example, a framework could model `searchParams` as a module export whose
value resolves from the current request. This avoids encoding the search
params twice (they already appear in the request URL) but it also makes
the responses more cacheable: if the search params don't appear
elsewhere in the body, then a response cache can omit them from its
cache key.

This initial PR only exposes the new API in the Turbopack bindings. We
will port it to the other bundler configs if the experiment advances.

DiffTrain build for [71f7255](react@71f7255)
```
