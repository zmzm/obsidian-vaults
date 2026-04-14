---
type: twir-item
issue: 257
item: 9
item_type: item
date: 2025-11-05
source: https://lingual.dev/blog/quality-assurance-for-i18n-in-react/
tags:
  - "i18n"
  - "RCE"
status: auto
quality: keep
---

[[2025-11-05-TWIR-257|Index]]

# Item 9: Quality Assurance for i18n in React

Source: [https://lingual.dev/blog/quality-assurance-for-i18n-in-react/](https://lingual.dev/blog/quality-assurance-for-i18n-in-react/)

Summary:
Ensuring quality in React internationalization (i18n) is challenging, as translation errors often go undetected until runtime. The article introduces i18n-check, a CLI tool that scans translation files for missing, unused, or invalid keys, and integrates with CI to automate i18n QA. It provides setup instructions, usage examples, and tips for keeping translation files clean and in sync with code.

Key takeaways:
- i18n bugs are subtle and often missed by standard tests.
- i18n-check automates detection of missing, unused, or invalid translation keys.
- Integrates with CI/CD to enforce i18n quality as part of the development workflow.
- Supports common React i18n libraries and customizable for various setups.

Recommendation:
Summary sufficient (read full article for implementation details or if adopting i18n-check)

Why it matters:
read full article for implementation details or if adopting i18n-check

Content:
# Quality Assurance for i18n in React

November 1, 2025

## Introduction

Quality assurance (QA) for internationalization (i18n) means preventing translation errors, missing keys, and inconsistent user experiences across languages. i18n bugs are often hard to detect before production, as they rarely break builds or show up in standard tests, but can quietly impact users at runtime.

Common scenarios include:

- Seeing placeholders like `{user.greeting}` instead of translated text
- Pages crashing due to missing plural forms
- Translation files becoming out of sync, with unused or missing keys

Testing strategies for i18n should be part of your QA process to ensure a consistent experience for all users, regardless of language.

## The problem

Take the following example: the English version of a new product page works perfectly, but a missing translation key in the German locale causes the checkout button to disappear. The tests probably checked for the English version, but never tested if the button is visible when switching to German.
The issue might not be noticeable up until a customer reports that they can’t checkout the product.

Internationalization issues usually have multiple possible sources like:

- A translator can forget to translate a key.
- A refactor removes a component but not its translation keys.
- A typo in the key name

There are more scenarios and most can happen more commonly. The issues are similar no matter if working with `i18next`, `react-intl`, `next-intl`, or any JSON-based i18n setup in React.

In this write-up, we’ll see how using [`i18n-check`](https://github.com/lingualdev/i18n-check)
can make **quality assurance a seamless part of the regular development workflow**, helping to catch any i18n related issues before they hit production.

---

## What is i18n-check?

**i18n-check** is a CLI tool that acts like a **linter for your translation files**.

It scans your app to catch:

- **Missing translations**
- **Invalid ICU syntax**
- **Placeholders that don’t match**
- **Unused or obsolete keys**
- **Keys used in code but missing in your source locale**

It’s currently mainly focused on common React setups.

---

## Getting started with i18n-check in React

### Installation

```
npm install --save-dev i18n-check
# or
yarn add -D i18n-check
# or
pnpm add --save-dev @lingual/i18n-check
```

### Translation files setup

Here’s a typical setup:

```
locales/
  en.json   ← source locale (used as reference)
  fr.json
  de.json
src/
  components/
  pages/
```

> Tip: Keeping your en.json clean and complete. Think of it as your single source of i18n truth.

### Run checks

```
i18n-check --locales locales --source en
```

This will:

Output:

```
Found missing keys!
┌────────────────────┬────────────────────┐
│ file               │ key                │
├────────────────────┼────────────────────┤
│ locales/fr.json    │ navbar.about       │
│ locales/de.json    │ footer.contact     │
└────────────────────┴────────────────────┘
```

## Catching unused or undefined keys

If you’re using `react-intl`, `i18next`, or `next-intl` , i18n-check can parse your source code:

```
i18n-check --locales locales --source en -u src -f react-intl
```

This adds two useful checks, that can help with cleaning locale files and catch potential runtime issues:

- **Undefined keys**: used in code, but missing in your source translations
- **Unused keys**: sitting in your .json files, but never referenced in code

Translation files can accumulate unnecessary entries over time like keys from features that have been removed, temporary messages or outdated labels.

This enables to remove these **unused keys**, keeping the translation in sync with the actual code. This not only reduces confusion for translators but also helps prevent accidental re-use of outdated content.

**Before/After Example:**

```
// Before cleanup
{
  "navbar.home": "Home",
  "navbar.about": "About",
  "oldFeature.unused": "Old feature text",
  "temp.message": "Temporary message"
}

// After running i18n-check and removing unused keys
{
  "navbar.home": "Home",
  "navbar.about": "About"
}
```

## Integrating i18n-check with CI

Integrating i18n-check into your **CI pipeline** will ensure a seamless qa process.

- Run `i18n-check` on every pull request and push to main branches.
- Fail the build if critical translation errors are found.
- Keep your source locale (e.g., en.json) up to date and reviewed.
- Make fixing i18n errors of the review process.

Example of a Github action you can setup:
˘

```
# .github/workflows/i18n-check.yml
name: i18n Check
on:
  pull_request:
    branches:
      - main
  push:
    branches:
      - main

jobs:
  i18n-check:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@master

      - name: yarn install & build
        run: |
          yarn install
          yarn build          

      - name: yarn i18n-check
        run: |
          yarn i18n-check --locales translations/messageExamples --source en-US
```

For more information on how to setup a Github action [check the README](https://github.com/lingualdev/i18n-check?tab=readme-ov-file#as-github-action)
.

Additionally you can also run it locally with a pre-push or pre-commit hook using Husky.

---

## Customizing i18n-check

`i18n-check` can be customized for the commonly used i18n libraries:

- Supports ICU and i18next formats
- Works with flat or nested JSON structures
- Can ignore certain paths or patterns (`--ignore some.path.*`)

The [README](https://github.com/lingualdev/i18n-check)
lists a number of options and possible customizations to help with working with your internationalization.

---

## Summary

Maintaining accuracy and consistency in translation files is essential for reliable multilingual React apps. Using tools like i18n-check as part of your QA process helps teams catch issues early and deliver a better experience for all users.

---
