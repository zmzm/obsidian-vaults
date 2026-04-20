---
id: frontend/accessibility/keyboard-navigation
name: frontend/accessibility/keyboard-navigation
kind: reference
domain: frontend
topics: [accessibility, keyboard navigation]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Keyboard Navigation

## When to use

Use this document when:

- Implementing keyboard-accessible components
- Creating modals and dialogs with keyboard support
- Building custom interactive components (dropdowns, menus)
- Adding keyboard shortcuts to applications

## Rules

- All interactive elements must be keyboard accessible
- Modals must trap focus and support Escape key
- Custom components must support arrow key navigation
- Keyboard shortcuts should not conflict with browser defaults
- Tab order should follow visual order

## Examples

### Good example

```typescript
// ✅ Good: Keyboard accessible modal
export const Modal: React.FC<ModalProps> = ({ isOpen, onClose, children }) => {
  useEffect(() => {
    if (!isOpen) return;
    const handleEscape = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose();
      }
    };
    document.addEventListener('keydown', handleEscape);
    return () => document.removeEventListener('keydown', handleEscape);
  }, [isOpen, onClose]);

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent>
        {children}
        <Button onClick={onClose}>{t('close')}</Button>
      </DialogContent>
    </Dialog>
  );
};

// Arrow key navigation for custom dropdowns
const handleKeyDown = (e: React.KeyboardEvent) => {
  if (e.key === 'ArrowDown') {
    // Move to next item
  } else if (e.key === 'ArrowUp') {
    // Move to previous item
  } else if (e.key === 'Enter') {
    // Select item
  }
};

// Keyboard shortcuts
useEffect(() => {
  const handleKeyPress = (e: KeyboardEvent) => {
    if (e.ctrlKey && e.key === 's') {
      e.preventDefault();
      handleSave();
    }
  };
  document.addEventListener('keydown', handleKeyPress);
  return () => document.removeEventListener('keydown', handleKeyPress);
}, []);
```

### Bad example

```typescript
// ❌ Bad: Modal without Escape key support
export const Modal: React.FC<ModalProps> = ({ isOpen, onClose, children }) => {
  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent>{children}</DialogContent>
    </Dialog>
  );
};

// ❌ Bad: Custom component without keyboard support
<div onClick={handleClick}>Click me</div>;

// ❌ Bad: Keyboard shortcut without preventDefault
useEffect(() => {
  const handleKeyPress = (e: KeyboardEvent) => {
    if (e.ctrlKey && e.key === 's') {
      handleSave(); // May trigger browser save dialog
    }
  };
  document.addEventListener('keydown', handleKeyPress);
  return () => document.removeEventListener('keydown', handleKeyPress);
}, []);
```

## Anti-patterns

- Creating keyboard traps (focus cannot escape)
- Missing Escape key support in modals
- Not supporting arrow keys in custom components
- Using non-interactive elements for click handlers
- Keyboard shortcuts that conflict with browser defaults

## Notes

- Tab navigation should follow visual order (left-to-right, top-to-bottom)
- Modals should trap focus within the modal
- Escape key should close modals and dialogs
- Arrow keys should navigate within custom components (dropdowns, menus)
- Enter/Space should activate buttons and links
- Keyboard shortcuts should be documented and discoverable
