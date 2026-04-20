---
id: frontend/accessibility/focus-management
name: frontend/accessibility/focus-management
kind: reference
domain: frontend
topics: [accessibility, focus management]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Focus Management

## When to use

Use this document when:

- Managing focus in modals and dialogs
- Implementing skip links for navigation
- Creating focus indicators for interactive elements
- Programmatically moving focus in response to user actions

## Rules

- Modals must trap focus within the modal
- Focus should return to trigger element when modal closes
- Skip links should be provided for main content
- Focus indicators must be visible and meet contrast requirements
- Programmatic focus should be used sparingly and predictably

## Examples

### Good example

```typescript
// ✅ Good: Manage focus for modals
export const useModal = () => {
  const [isOpen, setIsOpen] = useState(false);
  const previousFocusRef = useRef<HTMLElement | null>(null);

  const open = () => {
    previousFocusRef.current = document.activeElement as HTMLElement;
    setIsOpen(true);
  };

  const close = () => {
    setIsOpen(false);
    // Restore focus to element that opened modal
    previousFocusRef.current?.focus();
  };

  return { isOpen, open, close };
};

// ✅ Good: Skip to main content
export const Layout: React.FC = ({ children }) => {
  return (
    <>
      <a href="#main-content" className="sr-only focus:not-sr-only focus:absolute focus:top-4">
        {t('skipToContent')}
      </a>
      <Header />
      <main id="main-content" tabIndex={-1}>
        {children}
      </main>
    </>
  );
};

// Focus indicators
<Button
  _focus={{
    outline: '2px solid',
    outlineColor: 'blue.500',
  }}>
  {t('submit')}
</Button>;

// Programmatic focus
const inputRef = useRef<HTMLInputElement>(null);

useEffect(() => {
  if (shouldFocus) {
    inputRef.current?.focus();
  }
}, [shouldFocus]);
```

### Bad example

```typescript
// ❌ Bad: Modal without focus management
export const Modal: React.FC<ModalProps> = ({ isOpen, onClose, children }) => {
  return isOpen ? <div>{children}</div> : null;
};

// ❌ Bad: Missing skip links
export const Layout: React.FC = ({ children }) => {
  return (
    <>
      <Header />
      <main>{children}</main>
    </>
  );
};

// ❌ Bad: Removing focus indicators
<Button _focus={{ outline: 'none' }}>{t('submit')}</Button>;
```

## Anti-patterns

- Removing focus indicators without replacement
- Not trapping focus in modals
- Not restoring focus when modals close
- Missing skip links for main content
- Using tabIndex > 0 (should be 0 or -1)

## Notes

- tabIndex={-1} makes element focusable programmatically but not via Tab
- tabIndex={0} makes element focusable via Tab in natural order
- Skip links should be visually hidden but visible on focus
- Focus should be moved to modal when it opens
- Focus should return to trigger when modal closes
- Chakra UI components have built-in focus styles
