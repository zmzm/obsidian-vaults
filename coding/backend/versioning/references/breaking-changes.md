---
id: backend/versioning/breaking-changes
name: backend/versioning/breaking-changes
kind: reference
domain: backend
topics: [versioning, breaking changes]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Breaking vs Non-Breaking Changes

## When to use

Use this document when:

- Determining if a change needs new version
- Planning API changes
- Documenting changes in CHANGELOG

## ❌ Breaking Changes (Require New Version)

These changes **require** incrementing the API version:

- Removing an endpoint
- Removing a field from response
- Changing field type (string → number)
- Renaming fields
- Changing HTTP status codes
- Changing error response format
- Making optional fields required
- Changing authentication requirements

### Examples

```typescript
// ❌ Breaking: Field removed
// V1: { id, name, email }
// V2: { id, email }  // 'name' removed

// ❌ Breaking: Field renamed
// V1: { userName: 'john' }
// V2: { displayName: 'john' }

// ❌ Breaking: Type changed
// V1: { age: '25' }
// V2: { age: 25 }  // string → number

// ❌ Breaking: Status code changed
// V1: 200 OK for update
// V2: 204 No Content for update

// ❌ Breaking: Optional → required
// V1: phone?: string
// V2: phone: string  // Now required
```

## ✅ Non-Breaking Changes (No Version Change)

These changes do **not** require a new version:

- Adding new endpoints
- Adding optional query parameters
- Adding new fields to response
- Adding new error codes (existing ones unchanged)
- Improving performance
- Bug fixes
- Adding new optional headers

### Examples

```typescript
// ✅ Non-breaking: New field added
// V1: { id, name }
// V1: { id, name, createdAt }  // New field added

// ✅ Non-breaking: New optional parameter
@Get()
findAll(@Query('includeDeleted') includeDeleted?: boolean) { }

// ✅ Non-breaking: New endpoint
@Get('users/:id/preferences')  // New endpoint

// ✅ Non-breaking: Performance improvement
// Same response, faster query
```

## Version Migration Example

### V1: Original API

```typescript
interface UserV1Response {
  id: string;
  name: string;  // Actually contains email
  role: string;
}

@Get(':id')
async findOne(@Param('id') id: string): Promise<UserV1Response> {
  const user = await this.usersService.findOne(id);
  return {
    id: user.id,
    name: user.email,
    role: user.role,
  };
}
```

### V2: Breaking Change (Separate Name and Email)

```typescript
interface UserV2Response {
  id: string;
  email: string;        // New field
  displayName: string;  // Renamed from 'name'
  role: string;
}

@Get(':id')
async findOne(@Param('id') id: string): Promise<UserV2Response> {
  const user = await this.usersService.findOne(id);
  return {
    id: user.id,
    email: user.email,
    displayName: user.name,
    role: user.role,
  };
}
```

## CHANGELOG Documentation

````markdown
# API Changelog

## v2.0.0 (2025-11-07)

### Breaking Changes

- **Users API**: Separated `name` and `email` fields
  - V1: `name` contained email
  - V2: `email` and `displayName` are separate fields

### Migration Guide

```javascript
// V1
fetch('/v1/users/123');
// Response: { id, name: "user@example.com", role }

// V2
fetch('/v2/users/123');
// Response: { id, email: "user@example.com", displayName: "User Name", role }
```
````

### Deprecation Notice

- V1 will be sunset on 2026-01-01

```

## Notes

- Only increment version for breaking changes
- Batch related breaking changes together
- Always provide migration guide
- Document in CHANGELOG.md

```
