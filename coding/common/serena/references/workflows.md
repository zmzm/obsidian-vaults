---
id: common/serena/workflows
name: common/serena/workflows
kind: reference
domain: common
topics: [serena, workflows]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Common Serena Workflows

## When to use

Use this document when you need step-by-step guidance for common code navigation and modification tasks.

## Workflow: Understanding Unknown Code

```
1. list_dir(".", recursive=True)           # See project structure
2. get_symbols_overview("target/file.ts")  # See file contents
3. find_symbol("InterestingClass", depth=1) # See class methods
4. find_symbol("InterestingClass/method", include_body=True)  # Read method
5. find_referencing_symbols("method", "file.ts")  # Find usages
```

## Workflow: Adding New Feature

```
1. Find similar existing code as reference
2. get_symbols_overview to understand target file
3. find_symbol to locate insertion point
4. insert_after_symbol to add new function/method
5. insert_before_symbol for imports if needed
6. find_referencing_symbols if modifying existing code
```

## Workflow: Refactoring

```
1. find_symbol to locate target symbol
2. find_referencing_symbols to find ALL usages
3. Assess impact: How many files? Breaking changes?
4. If just renaming: rename_symbol (updates all references)
5. If changing signature:
   - replace_symbol_body for implementation
   - Update each reference manually or with replace_content
6. Verify: find_referencing_symbols again
```

## Workflow: Bug Investigation

```
1. find_symbol to locate problematic code
2. find_symbol with include_body=True to read implementation
3. find_referencing_symbols to trace call chain
4. Read related symbol bodies to understand flow
5. Make targeted fix with replace_content or replace_symbol_body
```

## Workflow: Adding Method to Existing Class

```
1. get_symbols_overview("class-file.ts") - See existing methods
2. find_symbol("ClassName", depth=1) - Get method list
3. find_symbol("ClassName/lastMethod", include_body=True) - See last method
4. insert_after_symbol("ClassName/lastMethod", "class-file.ts", "new method body")
```

## Workflow: Safe API Changes

```
1. find_symbol to locate function/method
2. find_referencing_symbols to identify all callers
3. For each caller:
   - If internal: Update to new signature
   - If external/public: Create backward-compatible wrapper
4. replace_symbol_body with new implementation
5. Update or create tests
```

## Workflow: Moving Code Between Files

```
1. find_symbol(target, include_body=True) - Get code to move
2. Create/open destination file
3. insert_after_symbol or insert_before_symbol in destination
4. find_referencing_symbols(target, source_file) - Find all imports
5. Update imports in each file using replace_content
6. Delete original with replace_symbol_body (empty) or file operations
```
