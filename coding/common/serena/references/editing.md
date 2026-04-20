---
id: common/serena/editing
name: common/serena/editing
kind: reference
domain: common
topics: [serena, editing]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Serena Editing Patterns

## When to use

Use this document when you need to make code changes using Serena's editing tools.

## Choosing the Right Editing Tool

| Scenario                     | Tool                             | Reason                 |
| ---------------------------- | -------------------------------- | ---------------------- |
| Replace entire function      | `replace_symbol_body`            | Clean replacement      |
| Change 1-3 lines in function | `replace_content`                | More efficient         |
| Add new method               | `insert_after_symbol`            | Preserves structure    |
| Add import                   | `insert_before_symbol`           | At file top            |
| Rename everywhere            | `rename_symbol`                  | Updates all references |
| Delete symbol                | `replace_symbol_body` with empty | Or file operations     |

## Symbol Body Replacement

**Good example**:

```
replace_symbol_body(
  name_path="UserService/create",
  relative_path="users.service.ts",
  body="async create(dto: CreateUserDto): Promise<User> {\n    return this.prisma.user.create({ data: dto });\n  }"
)
```

**Rules**:

- Include the complete symbol definition (signature + body)
- Do NOT include preceding comments/docstrings
- Do NOT include imports
- Match existing indentation style

## Regex Replacement (replace_content)

**When to use**: Small changes within a larger symbol

**Good example** (change one line):

```
replace_content(
  relative_path="users.service.ts",
  needle="return this.prisma.user.create\\(\\{ data: dto \\}\\)",
  repl="return this.prisma.user.create({ data: { ...dto, createdAt: new Date() } })",
  mode="regex"
)
```

**Using wildcards** (change multiple lines):

```
replace_content(
  relative_path="users.service.ts",
  needle="if \\(condition\\).*?\\}",  # .*? is non-greedy
  repl="if (newCondition) {\n    newLogic();\n  }",
  mode="regex"
)
```

**Rules**:

- Escape special regex characters: `\(\)`, `\[\]`, `\{\}`, `\.`
- Use `.*?` (non-greedy) instead of `.*` to avoid over-matching
- Test pattern uniqueness: if multiple matches, add more context

## Insertion Patterns

**Add method at end of class**:

```
# Find last method
find_symbol("ClassName", depth=1)  # Returns method list
# Insert after last method
insert_after_symbol(
  name_path="ClassName/lastMethodName",
  relative_path="file.ts",
  body="\n\n  newMethod(): void {\n    // implementation\n  }"
)
```

**Add import at top of file**:

```
# Find first symbol in file
get_symbols_overview("file.ts")
# Insert before first symbol
insert_before_symbol(
  name_path="FirstClassOrFunction",
  relative_path="file.ts",
  body="import { NewDep } from './new-dep';\n"
)
```

## Safe Refactoring Pattern

Always check references before modifying:

```
# 1. Find all usages
find_referencing_symbols("functionToChange", "source-file.ts")

# 2. Assess impact
#    - How many files affected?
#    - Breaking changes?
#    - Public API?

# 3. Make change
replace_symbol_body(...)

# 4. Update affected references if needed
```

## Anti-patterns

❌ **Don't**: Replace entire file to change one function ✅ **Do**: Use `replace_symbol_body` or `replace_content`

❌ **Don't**: Use regex for complex multi-symbol changes ✅ **Do**: Use multiple `replace_symbol_body` calls

❌ **Don't**: Change symbol without checking references ✅ **Do**: Always `find_referencing_symbols` first

❌ **Don't**: Include comments/imports in symbol body replacement ✅ **Do**: Only include the symbol definition itself
