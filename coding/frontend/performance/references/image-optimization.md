---
id: frontend/performance/image-optimization
name: frontend/performance/image-optimization
kind: reference
domain: frontend
topics: [performance, image optimization]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Image Optimization

## When to use

Use this document when:

- Optimizing image loading and performance
- Implementing lazy loading for images
- Using modern image formats (WebP, AVIF)
- Creating responsive images

## Rules

- Always specify `width` and `height` to prevent layout shift
- Use `loading="lazy"` for below-the-fold images
- Provide alt text for accessibility
- Use appropriate image formats (WebP, AVIF when supported)
- Use responsive images with srcSet

## Examples

### Good example

```typescript
// ✅ Good: Lazy load images
<img
  src={course.thumbnail}
  alt={course.title}
  loading="lazy"
  width={300}
  height={200}
/>

// ✅ Good: WebP with Fallback
<picture>
  <source srcSet={course.thumbnailWebp} type="image/webp" />
  <img src={course.thumbnailJpg} alt={course.title} loading="lazy" />
</picture>

// ✅ Good: Responsive Images
<img
  srcSet={`
    ${course.thumbnailSmall} 300w,
    ${course.thumbnailMedium} 600w,
    ${course.thumbnailLarge} 1200w
  `}
  sizes="(max-width: 600px) 300px, (max-width: 1200px) 600px, 1200px"
  src={course.thumbnailMedium}
  alt={course.title}
  loading="lazy"
/>
```

### Bad example

```typescript
// ❌ Bad: Missing width/height (causes layout shift)
<img src={course.thumbnail} alt={course.title} />

// ❌ Bad: Not lazy loading below-the-fold images
<img src={course.thumbnail} alt={course.title} loading="eager" />

// ❌ Bad: Missing alt text
<img src={course.thumbnail} />
```

## Anti-patterns

- Missing width/height attributes (causes layout shift)
- Not lazy loading below-the-fold images
- Missing alt text for accessibility
- Not using modern image formats
- Loading large images on mobile devices

## Notes

### Best Practices

- Always specify `width` and `height` to prevent layout shift (CLS)
- Use `loading="lazy"` for below-the-fold images
- Provide alt text for accessibility
- Use appropriate image formats (WebP, AVIF when supported)
- Use responsive images with srcSet for different screen sizes

### Image Formats

- WebP: Better compression than JPEG/PNG
- AVIF: Even better compression (newer browsers)
- Always provide fallback for older browsers
- Use `<picture>` element for format selection

### Responsive Images

- Use `srcSet` for different image sizes
- Use `sizes` attribute to tell browser which size to use
- Reduces bandwidth on mobile devices
- Improves loading performance
