---
type: twir-item
issue: 304
item: 3
item_type: item
date: 2026-11-04
source: https://github.com/react/react/pull/36921
tags:
  - "Compiler"
  - "PR"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2026-11-04-TWIR-304|Index]]

# Item 3: React Compiler PR - Preserve source locations for accurate source maps

Source: [https://github.com/react/react/pull/36921](https://github.com/react/react/pull/36921)

Summary:
This React Compiler PR ensures that source offsets and declarator ranges are preserved when rebuilding AST nodes in both Rust and TypeScript, improving the accuracy of generated source maps. The change carries raw AST offsets as internal metadata, restores TypeScript node offsets, and adds comprehensive test coverage for various scenarios. This addresses issues where source maps were previously inaccurate, especially after code transformations.

Key takeaways:
- Preserves original source offsets through the compilation pipeline for better debugging.
- Adds new fields to internal structures and updates test coverage for edge cases.
- Fixes source map issues reported in downstream tools and frameworks.
- Minimal performance impact observed; backward compatibility considerations discussed.

Recommendation:
Summary sufficient (unless you work on source maps, compilers, or debugging tooling)

Why it matters:
unless you work on source maps, compilers, or debugging tooling

Content:
# [compiler] Preserve AST source offsets and declarator ranges by magic-akari · Pull Request #36921 · react/react · GitHub

```
FBT uses AST start/end offsets to distinguish plural count expressions.
Missing offsets conflate distinct counts and produce incorrect plural
forms.

Carry raw offsets independently of location indices through Rust
lowering and codegen, and restore offsets from original source nodes in
TypeScript codegen. Add unit coverage for missing and shifted offsets
and enable evaluator checks for both FBT plural regression fixtures.
```

```
Declarator ranges derived from transformed child locations can become
reversed or exclude the closing parenthesis of a cast initializer.

Carry statement and declarator locations separately through lowering
and use the original declarator location in codegen for both backends.
Automatically assert surviving declaration ranges for source-locations/
fixtures in snap, and add Rust unit tests for missing declarator metadata.
```

```
Catch compiler crate unit test failures and deep AST deserialization
regressions in CI.

Add cargo test --workspace to the Rust compiler workflow before the AST
round-trip and Rust/TypeScript port checks.
```

```
Copy the original raw start/end offsets when rebuilding function declarations,
function expressions, and arrow functions. Cover all three forms with original,
shifted, and absent offsets so the entrypoint preserves the caller's AST metadata.
```

```
…ties

Build outlined scope and reference maps from node IDs without overwriting source
offsets, sharing a borrowed JSX traversal and moving the codegen function fields
directly into the declaration. Add regressions for shifted and absent offsets,
colliding ranges, local bindings, and nested JSX member references.
```

```
Store each source node's original offsets alongside its Babel location in HIR and
apply them as AST nodes are generated, removing the offset restoration traversals.
Preserve location identity in analyses and diagnostics, with regressions for
shifted, absent, nullable, and shared-location offsets, outlined JSX, and hook guards.
```

```
Validate numeric ranges throughout both TypeScript and Rust snapshot output,
allowing original shifted offsets and leaving absent or partial offsets intact.
Add focused regressions for inconsistent and reversed ranges and run them through
the snapshot package test command.
```

```
## Summary

Preserve original source offsets and declarator ranges when React
Compiler rebuilds AST nodes in both Rust and TypeScript, so downstream
AST consumers can identify the correct source ranges.

Generated nodes can retain `loc` while losing node-level `start` / `end`
offsets. Declarator ranges derived from transformed children can become
reversed after constant propagation or exclude the closing parenthesis
of a cast initializer.

This change:

- Carries raw AST offsets through Rust lowering and codegen
independently of `loc.start.index` / `loc.end.index`, storing them as
internal, non-serialized HIR metadata.
- Restores TypeScript node offsets from the original AST during codegen.
- Carries statement and declarator locations separately in the existing
instruction and instruction-value fields, then emits the original
declarator range. Absent source metadata stays absent.
- Adds shared declaration-range assertions to snap, unit coverage for
missing and shifted metadata, and `cargo test --workspace` to the Rust
compiler CI workflow.

### Related
- vercel/next.js#97392
- web-infra-dev/rspack#15350

## How did you test this change?

- `cargo test --offline --locked --workspace`: 59 tests passed.
- Targeted Jest run for `CodegenReactiveFunction-test.ts`: 3 tests
passed, including shifted and absent raw offsets.
- `yarn snap` and `yarn snap --rust`: 1,832 fixtures passed in each
backend. The five `source-locations/` fixtures automatically assert
original declaration ranges after constant propagation, for grouped
declarations, loop initializers, and parenthesized casts.
- `bash scripts/test-babel-ast.sh`: 1,811 AST round-trip, 1,812
scope-info round-trip, and 1,797 scope-resolution rename fixtures
passed.
- TS/Rust comparison for the five `source-locations/` fixtures: HIR and
generated code matched in all five cases.
- TypeScript type checking, Rust formatting, Prettier, and scoped ESLint
checks passed.

The two FBT plural fixtures provide end-to-end regression coverage for a
downstream Babel transform that consumes the preserved raw offsets. Rust
unit tests also cover missing offsets, missing declaration locations,
and offsets that differ from location indices.

On ARM64, `SourceLocation` grows from 32 to 48 bytes and `Place` from 40
to 56 bytes. In two paired release runs over six inputs, median times
per 30 compilations were 14.13–14.57 ms on `main` and 14.54–14.70 ms on
this branch. These limited measurements do not establish a stable
performance difference.

Workspace Clippy completes with warnings, including
`large_enum_variant`. Strict `-D warnings` stops at pre-existing
warnings in unchanged `disjoint_set.rs` and `code_frame.rs`.

DiffTrain build for [a703ca6](a703ca6)
```

```
## Summary

Preserve original source offsets and declarator ranges when React
Compiler rebuilds AST nodes in both Rust and TypeScript, so downstream
AST consumers can identify the correct source ranges.

Generated nodes can retain `loc` while losing node-level `start` / `end`
offsets. Declarator ranges derived from transformed children can become
reversed after constant propagation or exclude the closing parenthesis
of a cast initializer.

This change:

- Carries raw AST offsets through Rust lowering and codegen
independently of `loc.start.index` / `loc.end.index`, storing them as
internal, non-serialized HIR metadata.
- Restores TypeScript node offsets from the original AST during codegen.
- Carries statement and declarator locations separately in the existing
instruction and instruction-value fields, then emits the original
declarator range. Absent source metadata stays absent.
- Adds shared declaration-range assertions to snap, unit coverage for
missing and shifted metadata, and `cargo test --workspace` to the Rust
compiler CI workflow.

### Related
- vercel/next.js#97392
- web-infra-dev/rspack#15350

## How did you test this change?

- `cargo test --offline --locked --workspace`: 59 tests passed.
- Targeted Jest run for `CodegenReactiveFunction-test.ts`: 3 tests
passed, including shifted and absent raw offsets.
- `yarn snap` and `yarn snap --rust`: 1,832 fixtures passed in each
backend. The five `source-locations/` fixtures automatically assert
original declaration ranges after constant propagation, for grouped
declarations, loop initializers, and parenthesized casts.
- `bash scripts/test-babel-ast.sh`: 1,811 AST round-trip, 1,812
scope-info round-trip, and 1,797 scope-resolution rename fixtures
passed.
- TS/Rust comparison for the five `source-locations/` fixtures: HIR and
generated code matched in all five cases.
- TypeScript type checking, Rust formatting, Prettier, and scoped ESLint
checks passed.

The two FBT plural fixtures provide end-to-end regression coverage for a
downstream Babel transform that consumes the preserved raw offsets. Rust
unit tests also cover missing offsets, missing declaration locations,
and offsets that differ from location indices.

On ARM64, `SourceLocation` grows from 32 to 48 bytes and `Place` from 40
to 56 bytes. In two paired release runs over six inputs, median times
per 30 compilations were 14.13–14.57 ms on `main` and 14.54–14.70 ms on
this branch. These limited measurements do not establish a stable
performance difference.

Workspace Clippy completes with warnings, including
`large_enum_variant`. Strict `-D warnings` stops at pre-existing
warnings in unchanged `disjoint_set.rs` and `code_frame.rs`.

DiffTrain build for [a703ca6](a703ca6)
```

Related notes: [[React Compiler]]
