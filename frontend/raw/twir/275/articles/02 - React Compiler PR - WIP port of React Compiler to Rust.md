---
type: twir-item
issue: 275
item: 2
item_type: item
date: 2026-04-01
source: https://github.com/facebook/react/pull/36173
tags:
status: auto
---

[[2026-04-01-TWIR-275|Index]]

# Item 2: React Compiler PR - WIP port of React Compiler to Rust

Source: [https://github.com/facebook/react/pull/36173](https://github.com/facebook/react/pull/36173)

Content:
# [compiler] Port React Compiler to Rust by josephsavona · Pull Request #36173 · facebook/react

added 30 commits

[March 17, 2026 12:30](https://github.com/facebook/react/pull/36173#commits-pushed-3cb806e)

Fixes:
- TSNonNullExpression: Allow module-scope bindings in isReorderableExpression,
  matching TS behavior where ModuleLocal/Import bindings are safe to reorder
- Gating: Fix is\_valid\_identifier to reject JS reserved words (true, false,
  null, etc.), add proper description/loc to gating error messages
- Object getter/setter: Skip getter/setter methods in ObjectExpression
  (matching TS behavior) instead of lowering them as ObjectMethod
- For-of destructuring: Return Destructure temp from lower\_assignment for
  array/object patterns so for-of test value is correct
- MemberExpression assignment: Return PropertyStore/ComputedStore temp from
  lower\_assignment so compound assignments use correct result
- Blocklisted imports: Add loc from import declaration to error detail

Test results: 1682 passed, 35 failed (was 1672 passed, 45 failed)

Key fixes:
- gather\_captured\_context: skip binding declaration sites and type-only
  bindings to avoid spurious context captures
- find\_functions\_to\_compile: find nested function expressions/arrows in
  top-level expressions for compilationMode 'all'
- Compound member assignment: return PropertyStore/ComputedStore value
  directly to match TS temporary allocation behavior
- UpdateExpression with MemberExpression: use member expression loc
- Tagged template: add raw/cooked value mismatch check
- BabelPlugin: handle scope extraction errors gracefully

Test results: 1704 passed, 13 failed (was 1682 passed, 35 failed)

\- Compound member assignment: return PropertyStore/ComputedStore value
  directly to match TS temporary allocation pattern
- UpdateExpression with MemberExpression: use member expression loc
  instead of update expression loc for inner operations
- Tagged template: add raw/cooked value mismatch check, fix error prefix
- resolve\_binding\_with\_loc: prefer binding declaration loc over reference
  loc, fixing identifier location for destructured variables

Test results: 1706 passed, 11 failed (was 1704 passed, 13 failed)

Fix destructuring assignment return values, reserved word detection,
catch clause destructuring invariants, fbt local binding detection,
function redeclaration handling, and invariant error propagation.

…feedback

Fix remaining HIR lowering test failures to reach 1717/1717 passing:
- Exclude JSX identifier references from hoisting analysis (matching TS traversal)
- Resolve function declaration names from inner scope for shadowed bindings
- Share binding maps between parent/child builders (matching TS shared-by-reference)
- Lower catch bodies via block statement for hoisting support
- Fix fbt error recording to simulate TS scope.rename deduplication
Also extracted convert\_binding\_kind helper and improved catch scope fallback per review.

Port the SSA pass (Braun et al. algorithm) from TypeScript to Rust as a new
react\_compiler\_ssa crate. Includes helper functions for map\_instruction\_operands,
map\_instruction\_lvalues, and map\_terminal\_operands. Test results: 1267/1717 passing.

Add eliminate\_redundant\_phi to the react\_compiler\_ssa crate. Implements the
Braun et al. redundant phi elimination with fixpoint loop for back-edges,
cascading rewrites, and recursive inner function handling. Test results: 1267/1717 passing.

Port Sparse Conditional Constant Propagation from TypeScript to Rust in the
react\_compiler\_optimization crate. Implements constant folding for arithmetic,
bitwise (with correct JS ToInt32 wrapping), comparison, and string operations,
plus branch elimination for constant If terminals with fixpoint iteration.
Test results: 1266/1717 passing.

Add react\_compiler\_typeinference crate with a full port of the InferTypes
pass. Generates type equations from HIR instructions, unifies them via a
substitution-based Unifier, and applies resolved types back to identifiers.
Property type resolution (getPropertyType/getFallthroughPropertyType) and
global declaration lookup (getGlobalDeclaration) are stubbed pending the
shapes/globals system port. 732/1717 fixtures passing at InferTypes step
with no regression on prior passes.

Ports the Environment configuration infrastructure from TypeScript to Rust,
including ShapeRegistry, GlobalRegistry, EnvironmentConfig (feature flags),
custom hooks, module type provider, and the key type resolution methods:
getGlobalDeclaration, getPropertyType, getFallthroughPropertyType, and
getFunctionSignature. Wires these into InferTypes to enable type inference
for built-in globals, hooks, and property accesses. Config fields requiring
JS function callbacks (moduleTypeProvider, flowTypeProvider) are skipped
with TODOs; the hardcoded defaultModuleTypeProvider is ported directly.

…t arena

Delegate HirBuilder::make\_type() to env.make\_type() instead of using an
independent counter. This ensures TypeIds for TypeCastExpression types
are allocated from the same sequence as identifier type slots, matching
the TS compiler's single global typeCounter.

…m scope serialization

Replace serialized referenceLocs and jsxReferencePositions fields with an
IdentifierLocIndex built by walking the function's AST on the Rust side.
The index maps byte offsets to (SourceLocation, is\_jsx) for all Identifier
and JSXIdentifier nodes, replacing data that was previously sent from JS.
Extends the AST visitor with enter\_jsx\_identifier and JSX element name
walking. Updates all 4 consumption points in build\_hir.rs and hir\_builder.rs.

Fix PruneMaybeThrows to null out the handler instead of replacing with
Goto, matching TS behavior that preserves MaybeThrow structure. Fix
ValidateUseMemo to return VoidUseMemo errors for pipeline logging and
gate checks behind the validateNoVoidUseMemo config flag. Suppress
false-positive ValidateContextVariableLValues errors from incomplete
lowering by using a temporary error collector in the pipeline.

Add comments to scope.ts and a "JS→Rust Boundary" section to the
architecture guide describing the principle of keeping the serialization
layer thin: only serialize core data structures from Babel, and let the
Rust side derive any additional information from the AST.

…d ValidateNoCapitalizedCalls passes

Ports three passes from TypeScript to Rust and wires them into the pipeline
after InferTypes. Adds post-dominator tree computation and unconditional blocks
analysis to react\_compiler\_hir as shared infrastructure for ValidateHooksUsage.

…sses

Ports the TS enableValidations getter to Rust and wraps the
validateHooksUsage and validateNoCapitalizedCalls calls with it,
matching the TS Pipeline.ts structure.

Fix test-rust-port.ts to properly access CompilerDiagnostic details
(stored in this.options.details without a getter) and serialize
CompilerDiagnostic.details in the Rust log\_error/compiler\_error\_to\_info
paths. Update build\_hir.rs and hir\_builder.rs error sites to use
CompilerDiagnostic with .with\_detail() matching the TS compiler.

Add serde Serialize/Deserialize derives to EnvironmentConfig, HookConfig,
ExhaustiveEffectDepsMode, Effect, and ValueKind. Change PluginOptions.environment
from serde\_json::Value to typed EnvironmentConfig, replacing ad-hoc .get() calls
with typed field access. Wire config through pipeline via Environment::with\_config().
On the JS side, convert customHooks Map to plain object and strip non-serializable
fields (moduleTypeProvider, flowTypeProvider) before sending to Rust.

…ommit with orchestrator log

Add /compiler-orchestrator skill that drives the Rust port forward in a loop: discover frontier, fix/port, review, commit. Update /compiler-commit to maintain the orchestrator log file at compiler/docs/rust-port/rust-port-orchestrator-log.md with pass status and timestamped entries.

Initial orchestrator status log tracking the Rust port progress across all
10 ported HIR passes (HIR through OptimizePropsMethodCalls).

Move frontier discovery (Step 1) in compiler-orchestrator and test collection
(Step 7) in compiler-commit into subagents so intermediate binary-search steps
and test output don't fill the main context window. Also reorder compiler-commit
steps so the orchestrator log is updated before staging/committing instead of
via a post-commit amend.

…rk to subagents

Rewrote Steps 3-5 of the orchestrator to explicitly launch subagents for
fixing, porting, reviewing, and committing. Added a directive that the main
context must only orchestrate (parse results, update log, launch subagents)
and never investigate or edit code directly.

…rust-port

Make the pass argument optional by auto-detecting the last ported pass from
pipeline.rs DebugLogEntry calls. Add per-pass divergence tracking to identify
the frontier (earliest pass with failures). Print the summary line with
frontier info as both the first and last output line for easy head/tail access.

Simplify compiler-orchestrator, compiler-commit, and compiler-port skills
to leverage the new no-arg test-rust-port mode and frontier detection.
The orchestrator no longer needs a subagent for discovery — a single
\`test-rust-port.sh | tail -1\` replaces binary search and per-pass testing.

Fixed error.reserved-words.ts test failure by adding the missing details array to the CompileError event in BabelPlugin.ts's scope extraction catch block. HIR pass now 1717/1717.

…ass arg

When a specific pass is given and has no failures, show
"frontier: <pass> passes, rerun without a pass name to find frontier"
instead of "frontier: none", since the global frontier is unknown.

Replace \`loweredFunc: <HIRFunction>\` placeholder with full inline function
body printing in both TS and Rust debug HIR printers. Remove \`Function #N:\`
header from formatFunction. This exposes real lowering differences in inner
functions (e.g. LoadLocal/LoadContext patterns).

…test-rust-port

Add machine-readable output modes to test-rust-port.ts so agents can parse
results without ANSI stripping or grep pipelines. Also adds per-pass breakdown
to human-readable output and updates orchestrator/commit skills to use --json.

Fixed multiple bugs in Rust HIR lowering exposed by the new inner function
debug printing. Removed incorrect is\_context\_identifier fallback that emitted
LoadContext instead of LoadLocal. Fixed context variable source locations using
IdentifierLocIndex. Changed ScopeInfo.reference\_to\_binding to IndexMap for
deterministic iteration order. Added JSXOpeningElement loc tracking and
UnsupportedNode type fields. HIR pass now 1717/1717.

…eachable block preds

Fixed validateContextVariableLValues to properly propagate errors instead of
discarding them. Fixed validateUseMemo event logging to include diagnostic
details. Fixed unreachable block predecessor tracking in hir\_builder.

Joe Savona added 7 commits

[March 31, 2026 17:24](https://github.com/facebook/react/pull/36173#commits-pushed-1a1b6ae)

… normalization

Major OXC scope info fixes:
- Fix function parameter binding kind (FormalParameter before FunctionScopedVariable)
- Fix catch parameter and rest parameter binding kinds
- Add object method scope mapping for property positions
- Handle TS type alias/enum/module bindings

AST conversion fixes:
- Include rest parameters in function param conversion
- Fix optional chain base expression conversion
- Implement ClassDeclaration reverse conversion
- Add TS declaration source text extraction
- Script source type detection via [@script](https://github.com/script) pragma

Test normalization improvements:
- HTML entity and unicode quote normalization
- Multi-line ternary collapsing and block comment stripping
- JSX paren wrapping normalization

OXC e2e results: 1467 → 1695 passing. SWC remains at 1717/1717.

… normalization

Final fixes for OXC e2e test failures:

1. Default parameters: handle OXC's FormalParameter.initializer field in
   both forward and reverse AST conversion
2. TS enum handling: treat TSEnumDeclaration bindings as globals in HIR
   builder to avoid invariant errors
3. Test normalization: JSX collapsing, ternary collapsing, newline escape
   normalization, error fixture tolerance

Both SWC and OXC now pass all 1717/1717 e2e tests (0 failures).

Remove unused Place import and fix multiline comment style in
DebugPrintReactiveFunction.ts. Add test script to babel-plugin-react-compiler-rust
package.json so yarn test succeeds. Prettier formatting in test-e2e.ts.

Port the test-only ValidateSourceLocations pass that ensures compiled output
preserves source locations for Istanbul coverage instrumentation. The pass
compares important node locations from the original Babel AST against the
generated CodegenFunction output. Fixes the error.todo-missing-source-locations
code comparison failure (1724/1724 now passing).

Fix 4 issues causing 27 errors vs TS's 22: (1) Don't record root function
node as important — TS func.traverse() visits descendants only. (2) Use
make\_var\_declarator for hoisted scope declarations to reconstruct
VariableDeclarator source locations. (3) Pass HIR pattern source locations
through to generated ArrayPattern/ObjectPattern AST nodes. (4) Sort errors
by source position for deterministic output. yarn snap --rust now 1725/1725.

SSR test fixtures used \`@enableOptimizeForSSR\` which is not a valid config key
and was silently ignored. Changed to \`@outputMode:"ssr"\` so the fixtures
actually compile in SSR mode and exercise the optimizeForSSR pass.

Port the conditional OptimizeForSSR pass ([facebook#13](https://github.com/facebook/react/pull/13)) from TypeScript to Rust. The pass
optimizes components for server-side rendering by inlining useState/useReducer,
removing effects and event handlers, and stripping event handler/ref props from
builtin JSX elements. Gated on outputMode === 'ssr'. All 1724 test-rust-port
fixtures and 1725 snap --rust fixtures pass.

…il objects

Replace method calls (primaryLocation(), printErrorMessage(), detail.options)
on the old class instances with static helper functions that work with the
plain CompileErrorDetail object shape. Fixes both eslint-plugin-react-compiler
and eslint-plugin-react-hooks.

Joe Savona added 4 commits

[April 1, 2026 10:55](https://github.com/facebook/react/pull/36173#commits-pushed-dceabf6)

…c in codegen

Move error formatting from the babel-plugin-react-compiler-rust JS layer into
the Rust core. Added code\_frame.rs to react\_compiler\_diagnostics with a plain-text
code frame renderer matching @babel/code-frame's non-highlighted mode, and
format\_compiler\_error() which produces the same "Found N error(s):" message format.
Rust now returns pre-formatted messages via a new formatted\_message field on
CompilerErrorInfo, eliminating ~160 lines of JS formatting code and the
@babel/code-frame dependency. Also fixed JSXExpressionContainer codegen to
propagate source locations, removing the ensureNodeLocs JS post-processing walk.

… dependency

Now that error formatting is done in Rust (returning formattedMessage on
CompilerErrorInfo), remove the JS fallback: formatCompilerError(),
categoryToHeading(), printCodeFrame(), their constants, and the
@babel/code-frame import from babel-plugin-react-compiler-rust.

Extended test-e2e.sh to compare logEvent() calls across all frontends against
the TS baseline. Added --json flag to e2e CLI binary to expose logger events
from SWC/OXC. Removed all code output normalization — comparison now uses
prettier only. Fixed TS directive logging (\[object Object\] → string value) and
Rust CompileSuccess fnName (used inferred name instead of codegen function id).

Fix 121 of 123 babel e2e test failures by aligning diagnostic event
output with the TypeScript compiler. Key changes: serialize description/
message fields as null (not omitted), implement diagnostic suggestions
with LoggerSuggestionOp enum, make record\_error() return Result for
invariant short-circuiting, emit CompileUnexpectedThrow events, use
CompilerDiagnostic format for invariant errors, and emit CompileSuccess
events for JSX-outlined functions.

Closed

20 tasks

Joe Savona added 5 commits

[April 2, 2026 14:45](https://github.com/facebook/react/pull/36173#commits-pushed-8a36ba6)

…ant errors

Replace all \`let \_ = record\_error(...)\` with \`record\_error(...)?\` so that
Invariant-category errors short-circuit execution via Result propagation,
matching TypeScript's throw behavior. Update function signatures throughout
build\_hir, hir\_builder, validation passes, and environment to return
Result<..., CompilerError>. Non-Invariant errors (Todo, Syntax, Hooks, etc.)
are unaffected since record\_error returns Ok(()) for those categories.

…egen loc index

Emit PipelineError event (instead of CompileError) for simulated unknown
exceptions (throwUnknownException\_\_testonly), matching TS behavior. Strip
JS stack traces from PipelineError data in e2e comparison since Rust
can't reproduce them. Preserve source location index field in codegen's
base\_node\_with\_loc so error detail locations include byte offsets.

…rettier

Use printWidth=1 then printWidth=80 in test-e2e.ts formatCode() to erase
single-vs-multi-line style differences between frontend codegen outputs.
This eliminates ~400 false-positive OXC failures caused by compact object
formatting that Prettier was preserving.

\- Populate index field in OXC Position (was None, now Some(offset))
- Use native 0-based columns/indices for OXC (matches Babel convention)
- Fix test-e2e.ts to only apply 1-based column adjustment for SWC
  (OXC is natively 0-based, no adjustment needed)
- Replace two-pass Prettier normalization with babel parse → generate
  (compact:true) → prettier pipeline, which normalizes all whitespace
  and formatting differences between frontend codegen outputs

OXC e2e: 689 → 1647 passing (1035 → 77 failures)
SWC e2e: 1585 → 1624 passing (139 → 100 failures)

Track code and event match results independently in test-e2e.ts,
showing per-variant pass rates for code output, logger events, and
the combined total in both summary table and single-variant modes.

[![f440](https://avatars.githubusercontent.com/u/9423?s=60&v=4)](https://github.com/f440)

Joe Savona added 5 commits

[April 4, 2026 16:30](https://github.com/facebook/react/pull/36173#commits-pushed-54bd672)

Export CompilerSuggestion type from the compiler and use it instead of
\`as Array<any>\` in the eslint plugin's makeSuggestions(), restoring
proper type narrowing for the assertExhaustive default branch.

Add "snap": "yarn workspace snap run snap" to match
babel-plugin-react-compiler, so "yarn snap --rust" in the test
script resolves correctly.

Add GitHub Actions workflow that runs cargo check, cargo build,
test-babel-ast.sh, test-rust-port.sh, and yarn snap --rust on PRs
touching the compiler/ directory.

… testing

The test script ran \`yarn snap --rust\` directly, but snap's dist/main.js
doesn't exist in CI. Add snap:build and snap:ci scripts matching the
babel-plugin-react-compiler pattern.

The snap workspace needs to be built (tsc) before its dist/main.js
can be executed.

[![@josephsavona](https://avatars.githubusercontent.com/u/6425824?s=40&v=4)](https://github.com/josephsavona) [josephsavona](https://github.com/josephsavona) changed the title ~\[compiler\] WIP port of React Compiler to Rust~ \[compiler\] Port React Compiler to Rust

[Apr 5, 2026](https://github.com/facebook/react/pull/36173#event-24201628993)

Joe Savona added 2 commits

[April 4, 2026 17:58](https://github.com/facebook/react/pull/36173#commits-pushed-8ef671f)

Bump retries from 3 to 5 to reduce flakiness in playground e2e tests.

This commits adds some tools to help with internal testing:
\* \`yarn snap minimize-rust-delta <path>\` which uses our existing snap minimizer infra to reduce a test case down while it still produces a difference in codegen btw TS and Rust
\* \`scripts/test-internal-files.sh\` is designed to test the compiler against internal files, pulling from our internal compiler configuration in order to figure out the exact plugin options that we would use when compiling through our normal code path
\* rust-compiler-workflow-guide.md documents the workflow i've been using to help [@mofeiZ](https://github.com/mofeiZ) and [@mvitousek](https://github.com/mvitousek) contribute

Key takeaways:
- No key takeaways extracted.

Recommendation: Summary sufficient
