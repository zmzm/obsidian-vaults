---
type: twir-item
issue: 275
item: 2
item_type: item
date: 2026-04-01
source: https://github.com/facebook/react/pull/36173
tags:
  - "ReactCompiler"
  - "PR"
  - "WIP"
status: auto
quality: keep
---

[[2026-04-01-TWIR-275|Index]]

# Item 2: React Compiler PR - WIP port of React Compiler to Rust

Source: [https://github.com/facebook/react/pull/36173](https://github.com/facebook/react/pull/36173)

Summary:
An experimental, work-in-progress port of the React Compiler to Rust has been shared for early feedback. The Rust version closely mirrors the TypeScript architecture, using a Babel-like AST and a high-level intermediate representation (HIR), and is already showing significant performance improvements. Integrations for Babel, OXC, and SWC are available, with all fixtures passing and a focus on correctness and incremental migration. The port was largely AI-generated under human guidance, and the team is seeking partner feedback on API shape, integration, and scope representation.

Key takeaways:
- Rust port is 3x faster as a Babel plugin, with transformation logic up to 10x faster; native integrations expected to be even faster.
- All test fixtures pass, and the port maintains parity with the TypeScript implementation at every compiler pass.
- Integration examples for Babel, OXC, and SWC are provided; partners are encouraged to experiment and provide feedback.
- Future plans include returning patches instead of full programs and improving scope analysis and data representation.

Recommendation:
Read fully

Content:
# [compiler] Port React Compiler to Rust by josephsavona · Pull Request #36173 · facebook/react · GitHub

```
Ports the Environment configuration infrastructure from TypeScript to Rust,
including ShapeRegistry, GlobalRegistry, EnvironmentConfig (feature flags),
custom hooks, module type provider, and the key type resolution methods:
getGlobalDeclaration, getPropertyType, getFallthroughPropertyType, and
getFunctionSignature. Wires these into InferTypes to enable type inference
for built-in globals, hooks, and property accesses. Config fields requiring
JS function callbacks (moduleTypeProvider, flowTypeProvider) are skipped
with TODOs; the hardcoded defaultModuleTypeProvider is ported directly.
```

Related notes: [[React Compiler]]
