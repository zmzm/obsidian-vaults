---
type: twir-item
issue: 268
item: 7
item_type: item
date: 2026-02-11
source: https://spin.atomicobject.com/authenticated-routes-tanstack-router/
tags:
  - "TanStack"
  - "TanStackRouter"
status: auto
quality: keep
---

[[2026-02-11-TWIR-268|Index]]

# Item 7: Authenticated Routes with TanStack Router

Source: [https://spin.atomicobject.com/authenticated-routes-tanstack-router/](https://spin.atomicobject.com/authenticated-routes-tanstack-router/)

Summary:
The author details a practical approach to implementing authenticated and protected routes in a React app using TanStack Router. The solution involves structuring routes with context for authentication, leveraging file-based route groups for protected/unprotected paths, and handling redirects both on initial load and authentication state changes. The article provides code samples for organizing routes, applying layouts, and ensuring users are redirected appropriately based on authentication status.

Key takeaways:
- Use RouterProvider context to make authentication state available throughout the route tree.
- Organize routes into protected and unprotected groups using file-based routing and special route.tsx files.
- Implement beforeLoad hooks for pre-render authentication checks and redirects.
- Invalidate the router on auth state changes to trigger correct navigation and layout updates.

Recommendation:
Read fully (for developers implementing authentication flows with TanStack Router or similar routing solutions)

Why it matters:
for developers implementing authentication flows with TanStack Router or similar routing solutions

Content:
# Authenticated Routes with TanStack Router

When my software development team spun up a new React web app, we decided not to use Next.js. We needed a routing solution that would allow us to organize our routes intuitively, redirect efficiently, and display layout components. We decided to use [TanStack Router](https://tanstack.com/router/latest), and I recently spent some time setting up our basic routing infrastructure. Here was my process.

## The Requirements

I wanted to:

1. Get authenticated user data (including roles and permissions) at the highest possible level and have it accessible throughout the entire route tree.
2. Redirect away from protected routes if the user is not yet authenticated.
3. Accessing the route index (i.e. www.example.com/) redirects appropriately based on authentication and role.
4. Apply a dashboard layout to all pages that are accessible to an admin.
5. Use changes in authentication status (i.e. login, logout, forced logout) to trigger redirects.

## The Solutions

The best solution for these challenges was to:

1. Make the authentication API call and pass that to the route tree via the `RouterProvider context`.
2. Use TanStack’s file-based routing scheme pathless route groups to differentiate between protected and unprotected routes and perform redirects in `beforeLoad`, before rendering the route component.
3. Handle initial landing page navigation based on authentication status and roles using redirects in `routes/index.tsx`.
4. Use `route.tsx` files to apply layouts to child routes.
5. Invalidate the router on auth change, in order to reload the current route and trigger the appropriate redirect.

## Step 1: Set Up the Router with Context.

First, we need to provide authentication state to all routes. We create the router:

```
// App.tsx
  const queryClient = new QueryClient(); // From TanStack Query

  const router = createRouter({
    routeTree,
    context: {
      auth: undefined!, // TanStack Router docs recommend undefined! for required context
      queryClient,
    },
  defaultPreload: 'intent',
  defaultPreloadStaleTime: 0,
});
```

When we create the router, we indicate that we want auth to be part of the context, but there is no meaningful value to put here. That needs to be handled in the React component, because we will get this data from the API.

```
// App.tsx continued
function App() {
  return (
    <ThemeProvider defaultTheme="light">
      <QueryClientProvider client={queryClient}>
        <AuthedRouterProvider />
      </QueryClientProvider>
    </ThemeProvider>
  );
}

function AuthedRouterProvider() {
  const auth = useAuth();
  
  useEffect(() => {
    // Forces routes to reload when the auth state changes
    router.invalidate();
  }, [auth]);

  return <RouterProvider router={router} context={{ auth }} />;
}
```

To keep things tidy, I created a `AuthedRouterProvider` that uses the useAuth as a hook to access the API data from the query cache. This auth data is delivered to the `RouterProvider context`. Note the `useEffect` invalidates the router when auth changes; we’ll get back to that in Step 5.

## Step 2: Create Protected Route Groups.

Using TanStack Router’s file-based routing, we have two route group directories: `_authenticated` and `_unauthenticated`. The underscore means that these directory names will not appear in the route. Here is a pared-down version of our routes directory:

```
routes/
├── _authenticated/
│ ├── admin/
│ │ ├── profile.tsx
│ │ └── route.tsx
│ └── route.tsx
├── _unauthenticated/
│ ├── sign-up.tsx
│ ├── login.tsx
│ └── route.tsx
├── __root.tsx
└── index.tsx
```

The gist here is that any route that requires the user to be authenticated should sit somewhere in the directory tree underneath `_authenticated`. Then we can use a special type of route file named `route.tsx` . This acts as a layout file and works wonderfully for our redirects, because any child of its parent directory will render this route component first.

```
// routes/_authenticated/route.tsx

export const Route = createFileRoute('/_authenticated')({
  component: RouteComponent,
  beforeLoad: async ({ context: { auth } }) => {
    // If user is not authenticated, redirect to login
    if (!auth?.user) {
      return redirect({ to: '/login' });
    }
  },
});

function RouteComponent() {
  return <Outlet />;
}
```

Note that `Outlet` here is the placeholder for the route components of any child routes. It’s kind of like `{children}` if `RouteComponent` received `children` as props. Now, in the beforeLoad, we check whether we have the auth.user data. If not, we redirect to the login page before we even render the `RouteComponent`.

We also set up a similar `/_unauthenticated/route.tsx` , which redirects the user to the `_authenticated` base route when they are logged in, so that they don’t accidentally land on the login or sign-up pages.

## Step 3: Create a User-friendly Index Route.

We also want the plain domain to be accessible, like www.example.com, so we needed to create a `routes/index.tsx` that can redirect us to the right location. As-is, we default to the admin route when the user is authenticated, but we could also handle redirecting to a future customer view by checking auth.user.groups and redirecting accordingly.

```
import { PageLoader } from '@/components/base/page-loader';
import { createFileRoute, redirect } from '@tanstack/react-router';
import { Route as AdminRoute } from './_authenticated/admin/route';
import { Route as LoginRoute } from './_unauthenticated/login';

export const Route = createFileRoute('/')({
  component: PageLoader,
  beforeLoad: async ({ context: { auth } }) => {
    // If user is not authenticated, redirect to login
    if (auth) {
      if (!auth?.user) {
        return redirect({ to: LoginRoute.to });
      }
      
      return redirect({ to: AdminRoute.to });
    }
  },
});
```

## Step 4: Use Nested Layouts with Dashboards.

We can also use `_route.tsx` for component layout. In our app, we will have two different dashboard layouts. Here, I show the admin view, which is accessible under `/_authenticated/admin` routes.

```
// _authenticated/admin/route.tsx
import { AdminDashboard } from '@/pages/admin/dashboard';
import { createFileRoute, redirect } from '@tanstack/react-router';

export const Route = createFileRoute('/_authenticated/admin')({
  component: AdminDashboard,
  beforeLoad: async ({ location }) => {
    // Redirect bare /admin to a default child route
    if (location.pathname === '/admin') {
      return redirect({ to: '/admin/profile' });
    }
  },
});
```

The AdminDashboard component includes the sidebar and an `Outlet` for child content:

```
// pages/admin/dashboard.tsx
export function AdminDashboard() {
  return (
    <SidebarProvider defaultOpen={true}>
      <div className="flex min-h-screen w-full">
        <AdminSidebar onLogout={handleLogout} />
        <SidebarInset>
          <Outlet />
        </SidebarInset>
      </div>
    </SidebarProvider>
  );
}
```

## Step 5: Redirect on Auth Change.

Remember that `useEffect` back in `App.tsx`? Whenever the auth data changes, we can invalidate the router, which results in the entire route tree being rerendered. This causes the `beforeLoad`s to run again with the new `auth` data and will trigger any appropriate redirects. Because we’re using TanStack Query to make and cache our auth request, all we need to do is `queryClient.invalidateQueries({ queryKey: [‘auth’] })` whenever we perform an auth action, like logging in or out of the app.

Note: We are also using TanStack Query for this project, and instead of removing related code, I left it here to illustrate how these complementary libraries are wired up together. However, I won’t be diving into the details of how we use that here; that’s another post entirely!
