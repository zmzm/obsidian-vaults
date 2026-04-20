---
id: frontend/hook/form-state
name: frontend/hook/form-state
kind: reference
domain: frontend
topics: [hook, form state]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Hooks for Form State

## When to use

Use this document when:

- Creating hooks for form state management
- Implementing form validation logic
- Handling form submission with API calls
- Managing form errors and validation

## Rules

- Extract form state logic to hooks
- Handle validation in hooks
- Clear errors when fields change
- Return form data, errors, and handlers
- Use React Hook Form for complex forms when appropriate
- Keep validation logic in hooks, not components

## Examples

### Good example

```typescript
// useLoginForm.hook.ts
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

interface LoginFormData {
  email: string;
  password: string;
}

export const useLoginForm = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState<LoginFormData>({
    email: '',
    password: '',
  });
  const [errors, setErrors] = useState<Partial<LoginFormData>>({});

  const handleChange = (field: keyof LoginFormData, value: string) => {
    setFormData(prev => ({ ...prev, [field]: value }));
    if (errors[field]) {
      setErrors(prev => ({ ...prev, [field]: undefined }));
    }
  };

  const validate = (): boolean => {
    const newErrors: Partial<LoginFormData> = {};
    if (!formData.email) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = 'Email is invalid';
    }
    if (!formData.password) {
      newErrors.password = 'Password is required';
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (onSuccess?: () => void) => {
    if (!validate()) return;
    try {
      await apiClient.post('/auth/login', formData);
      onSuccess?.();
      navigate('/dashboard');
    } catch (error) {
      setErrors({ email: 'Invalid credentials' });
    }
  };

  return { formData, errors, handleChange, handleSubmit };
};

// Form Hook with React Hook Form
import { useForm } from 'react-hook-form';

export const useCourseForm = () => {
  const form = useForm<CreateCourseDto>({
    defaultValues: {
      title: '',
      description: '',
      difficulty: CourseDifficulty.BEGINNER,
    },
  });

  return {
    ...form,
    handleSubmit: form.handleSubmit(data => {
      // Handle submission
    }),
  };
};
```

### Bad example

```typescript
// ❌ Bad: Form logic in component
export const LoginForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  // ... validation and submission logic in component
};

// ❌ Bad: Not clearing errors on change
const handleChange = (field: string, value: string) => {
  setFormData(prev => ({ ...prev, [field]: value }));
  // Missing error clearing
};
```

## Anti-patterns

- Keeping form logic in components instead of hooks
- Not clearing errors when fields change
- Not validating before submission
- Mixing form state with other concerns
- Not handling submission errors

## Notes

- Extract all form logic to hooks for reusability
- Clear field errors when user starts typing
- Validate before submission
- Handle both client-side and server-side errors
- Use React Hook Form for complex forms with many fields
- Keep form hooks focused on form state and validation
