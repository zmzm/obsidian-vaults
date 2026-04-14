---
type: twir-item
issue: 255
item: 12
item_type: item
date: 2025-10-22
source: https://sergiodxa.com/tutorials/transform-formdata-between-ui-and-database-in-react-router
tags:
  - "FormData"
  - "UI"
status: auto
quality: keep
---

[[2025-10-22-TWIR-255|Index]]

# Item 12: How to Transform FormData Between UI and Database in React Router

Source: [https://sergiodxa.com/tutorials/transform-formdata-between-ui-and-database-in-react-router](https://sergiodxa.com/tutorials/transform-formdata-between-ui-and-database-in-react-router)

Summary:
This tutorial explains best practices for transforming form data between UI and database layers in React Router apps. It advocates for a three-layer architecture (UI, HTTP, Data), with actions handling form-to-database transformations and loaders handling database-to-form transformations. The article provides code examples for parsing, validating, and transforming FormData, including handling file uploads and creating action-specific schemas.

Key takeaways:
- Keep form-data transformations in actions (UI→DB) and loaders (DB→UI), not in components or data functions.
- Use validation schemas tailored to each action, not generic database schemas.
- Handle complex cases (e.g., file uploads) in the HTTP layer, returning clean DTOs to the data layer.
- Promotes separation of concerns and maintainable code in React Router apps.

Recommendation:
Read fully (read fully if implementing complex forms or data flows in React Router)

Why it matters:
read fully if implementing complex forms or data flows in React Router

Content:
# How to Transform FormData Between UI and Database in React Router by sergiodxa

Imagine you're building a blog application where users can create and edit posts through forms. The form might submit data as `FormData` with fields like title, content, and tags, but your database expects a specific object structure with additional fields like `authorId` from the session. This transformation between UI and database formats is a common challenge that requires careful separation of concerns.

The key insight is understanding where these transformations belong in your application architecture: actions handle form-to-database transformations, while loaders handle database-to-form transformations when editing existing data.

## Understanding the Three-Layer Architecture

React Router applications naturally follow a three-layer architecture that keeps concerns properly separated:

- **UI Layer**: Your components that render forms and display data
- **HTTP Layer**: Your actions and loaders that handle requests and responses
- **Data Layer**: Your database functions that perform business operations

Each layer has specific responsibilities and shouldn't know about the others' implementation details.

## Transform Form Data in Actions

Actions receive `FormData` from forms and must transform it into objects your database functions expect. This transformation includes parsing form fields, adding session data, and handling file uploads.

```
import { z } from "zod";
import { createPost } from "~/data/posts.server";

const CreatePostSchema = z.object({
  title: z.string().min(1),
  content: z.string().min(1),
  tags: z.string().optional(),
});

export async function action({ request, context }: Route.ActionArgs) {
  let formData = await request.formData();
  let authorId = context.get(sessionContext).userId;

  
  let result = CreatePostSchema.safeParse({
    title: formData.get("title"),
    content: formData.get("content"),
    tags: formData.get("tags"),
  });

  if (!result.success) {
    return { errors: result.error.flatten() };
  }

  
  let createPostInput = {
    authorId,
    title: result.data.title,
    content: result.data.content,
    tags: result.data.tags ? result.data.tags.split(",") : [],
    publishedAt: new Date(),
  };

  let post = await createPost(createPostInput);
  return redirect(`/posts/${post.id}`);
}
```

The action transforms the `FormData` into a `CreatePostInput` object that includes session data (`authorId`) and business logic (`publishedAt`). The data layer function `createPost` receives a clean object without needing to know about forms or HTTP.

## Transform Database Data in Loaders

Loaders retrieve data from the database and transform it into the shape your UI components need. This is especially important when prefilling forms for editing.

```
import { getPostById } from "~/data/posts.server";

export async function loader({ params, context }: Route.LoaderArgs) {
  let post = await getPostById(params.postId);
  let userId = context.get(sessionContext).userId;

  if (post.authorId !== userId) {
    throw new Response("Unauthorized", { status: 403 });
  }

  
  return {
    post: {
      title: post.title,
      content: post.content,
      tags: post.tags.join(","), 
    },
  };
}
```

The loader transforms the database post object into a format that matches what the form expects. Arrays are converted to comma-separated strings, and only the fields needed by the UI are included.

## Handle Complex Transformations

Real-world forms often involve more complex transformations, like handling file uploads alongside text data:

```
export async function action({ request, context }: Route.ActionArgs) {
  let formData = await request.formData();
  let authorId = context.get(sessionContext).userId;

  
  let textFields = CreatePostSchema.safeParse({
    title: formData.get("title"),
    content: formData.get("content"),
  });

  if (!textFields.success) {
    return { errors: textFields.error.flatten() };
  }

  
  let imageFiles = z.file().array().parse(formData.getAll("images"));
  let imageUrls = await Promise.all(
    imageFiles.map((file) => {
      if (file.size === 0) return null;
      return uploadImage(file); 
    }),
  ).filter(Boolean);

  
  let createPostInput = {
    authorId,
    title: textFields.data.title,
    content: textFields.data.content,
    imageUrls,
    publishedAt: new Date(),
  };

  let post = await createPost(createPostInput);
  return redirect(`/posts/${post.id}`);
}
```

The action handles both form parsing and file processing before creating the final object. The data layer receives a complete DTO without knowing about `FormData` or file handling.

## Create Action-Specific Schemas

Don't reuse database schemas directly in actions. Each action should have its own schema that matches what the form actually submits:

```
const UpdatePostSchema = z.object({
  title: z.string().min(1),
  content: z.string().min(1),
  tags: z.string().optional(),
  
});

export async function action({ request, params, context }: Route.ActionArgs) {
  let formData = await request.formData();

  let result = UpdatePostSchema.safeParse({
    title: formData.get("title"),
    content: formData.get("content"),
    tags: formData.get("tags"),
  });

  if (!result.success) {
    return { errors: result.error.flatten() };
  }

  
  let updatePostInput = {
    title: result.data.title,
    content: result.data.content,
    tags: result.data.tags ? result.data.tags.split(",") : [],
    updatedAt: new Date(),
  };

  await updatePost(params.postId, updatePostInput);
  return redirect(`/posts/${params.postId}`);
}
```

This approach ensures your actions only validate what they actually receive, making them more maintainable and less coupled to database schemas.

## Keep Data Layer Independent

Your data layer functions should only handle business logic and database operations, not form parsing or HTTP concerns:

```
interface CreatePostInput {
  authorId: string;
  title: string;
  content: string;
  tags: string[];
  imageUrls?: string[];
  publishedAt: Date;
}

export async function createPost(input: CreatePostInput) {
  
  if (input.title.length > 100) {
    throw new Error("Title too long for SEO");
  }

  
  return await db.transaction(async (tx) => {
    let post = await tx.posts.create({
      authorId: input.authorId,
      title: input.title,
      content: input.content,
      publishedAt: input.publishedAt,
    });

    if (input.tags.length > 0) {
      await tx.postTags.createMany(
        input.tags.map((tag) => ({ postId: post.id, tag })),
      );
    }

    return post;
  });
}
```

The `createPost` function receives a clean typed object and focuses on business rules and database operations. It can be reused from different HTTP endpoints or even CLI commands.

## Final Thoughts

This separation of concerns makes your application more maintainable and testable. Actions and loaders act as translators between the HTTP world and your business logic, while keeping your data layer independent and reusable. The key is to remember that actions transform form data to database objects, loaders transform database data to UI-friendly formats, and the data layer remains focused on business operations.
