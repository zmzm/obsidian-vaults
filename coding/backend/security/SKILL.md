---
name: be-security
description:

  Guide for security best practices in NestJS applications including authentication, authorization, input validation, and OWASP Top 10
  protection. Use when implementing security features, adding guards, validating input, configuring CORS, or protecting against common
  vulnerabilities.
---

# Backend Security Skill

## When to use this knowledge

Use this skill when you are:

- Adding authentication/authorization guards
- Validating and sanitizing user input
- Implementing password hashing
- Configuring CORS and security headers
- Protecting against OWASP Top 10 vulnerabilities
- Setting up rate limiting

## When not to use this knowledge

- **API design** → See `be-api` skill
- **Error handling** → See `be-coding` skill
- **Database security** → See `be-database` skill (SQL injection prevention)

## What this skill covers

This skill provides guidance for:

- OWASP Top 10 protection patterns
- Input validation with class-validator
- Rate limiting configuration
- Environment variable security
- HTTP security headers (Helmet)
- Session management

## Knowledge map

Always start here, then follow references as needed:

- OWASP protection → `references/owasp-protection.md`
- Input validation → `references/input-validation.md`
- Rate limiting → `references/rate-limiting.md`
- Environment config → `references/environment-config.md`
- HTTP headers → `references/http-headers.md`
- Session management → `references/session-management.md`

## Fast decision hints

- If the task is mainly about Adding authentication/authorization guards, start with this skill.
- If the task also involves Validating and sanitizing user input, follow the most relevant reference page.
- If the work drifts into Implementing password hashing, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Validate and sanitize all user input
- `<default>` Default: Use environment variables for all secrets
- `<heuristic>` Heuristic: Hash passwords with bcrypt (min salt rounds: 10)
- `<exception>` Exception: Implement authentication and authorization on protected endpoints

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **security implementation**. For:

- **API design** → See `be-api` skill
- **Error handling** → See `be-coding` skill
- **Database security** → See `be-database` skill (SQL injection prevention)

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
