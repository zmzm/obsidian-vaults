---
type: "twir-recovery"
issue: 294
item: 12
source: "https://tkdodo.eu/blog/reliable-query-prefetching-with-tanstack-router"
final_url: "https://tkdodo.eu/blog/reliable-query-prefetching-with-tanstack-router"
retrieved: "2026-10-22T11:30:07+00:00"
original_note: "frontend/raw/twir/294/articles/12 - Reliable Query Prefetching with TanStack Router.md"
editorial_review: "pending"
truncated: false
---

Original intake note: [[../articles/12 - Reliable Query Prefetching with TanStack Router|Reliable Query Prefetching with TanStack Router]]

# Reliable Query Prefetching with TanStack Router

```
const

```
const Route: RouteApi<"/dashboard/$dashboardId", RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, {}, AnyContext, AnyContext, {}, undefined, readonly [Route<Register, RootRoute<Register, undefined, {}, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", undefined, ResolveParams<"/dashboard/$dashboardId">, ... 9 more ..., undefined>], unknown, unknown, unknown, undefined>, "never", false, RouterHistory, Record<...>>>
```

Route

=

```
getRouteApi<"/dashboard/$dashboardId", RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, {}, AnyContext, AnyContext, {}, undefined, readonly [Route<Register, RootRoute<Register, undefined, {}, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", undefined, ResolveParams<"/dashboard/$dashboardId">, ... 9 more ..., undefined>], unknown, unknown, unknown, undefined>, "never", false, RouterHistory, Record<...>>>(id: ConstrainLiteral<...>): RouteApi<...>
```

getRouteApi

('/dashboard/$dashboardId')

function

```
function DashboardContent(): void
```

DashboardContent

() {

const

params

=

```
const Route: RouteApi<"/dashboard/$dashboardId", RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, {}, AnyContext, AnyContext, {}, undefined, readonly [Route<Register, RootRoute<Register, undefined, {}, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", undefined, ResolveParams<"/dashboard/$dashboardId">, ... 9 more ..., undefined>], unknown, unknown, unknown, undefined>, "never", false, RouterHistory, Record<...>>>
```

Route

.

```
RouteApi<"/dashboard/$dashboardId", RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, {}, AnyContext, AnyContext, ... 6 more ..., undefined>, "never", false, RouterHistory, Record<...>>>.useParams: <RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, {}, AnyContext, AnyContext, {}, undefined, readonly [Route<Register, RootRoute<Register, undefined, {}, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", undefined, ResolveParams<"/dashboard/$dashboardId">, AnyContext, ... 8 more ..., undefined>], unknown, unknown, unknown, undefined>, "never", false, RouterHistory, Record<...>>, unknown, boolean>(opts?: (UseParamsBaseOptions<...> & OptionalStructuralSharing<...>) | undefined) => {
```

useParams

()

const {

data

} =

```
useSuspenseQuery<Dashboard, Error, Dashboard, string[]>(options: UseSuspenseQueryOptions<Dashboard, Error, Dashboard, string[]>, queryClient?: QueryClient): UseSuspenseQueryResult<Dashboard, Error>
```

useSuspenseQuery

(

```
const dashboardQueryOptions: (dashboardId: string) => OmitKeyof<UseQueryOptions<Dashboard, Error, Dashboard, string[]>, "queryFn"> & {

queryFn?: QueryFunction<Dashboard, string[], never>;

[dataTagSymbol]: Dashboard;

[dataTagErrorSymbol]: Error;
```

dashboardQueryOptions

(

params

.

dashboardId

),
```

```
const

```
const Route: RouteApi<"/dashboard/$dashboardId", RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, {}, AnyContext, AnyContext, {}, undefined, readonly [Route<Register, RootRoute<Register, undefined, {}, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", (data: unknown) => {

}, ResolveParams<"/dashboard/$dashboardId">, ... 9 more ..., undefined>], unknown, unknown, unknown, undefined>, "never", false, RouterHistory, Record<...>>>
```

Route

=

```
getRouteApi<"/dashboard/$dashboardId", RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, {}, AnyContext, AnyContext, {}, undefined, readonly [Route<Register, RootRoute<Register, undefined, {}, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", (data: unknown) => {

}, ResolveParams<"/dashboard/$dashboardId">, ... 9 more ..., undefined>], unknown, unknown, unknown, undefined>, "never", false, RouterHistory, Record<...>>>(id: ConstrainLiteral<...>): RouteApi<...>
```

getRouteApi

('/dashboard/$dashboardId')

function

```
function DashboardContent(): void
```

DashboardContent

() {

const

params

=

```
const Route: RouteApi<"/dashboard/$dashboardId", RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, {}, AnyContext, AnyContext, {}, undefined, readonly [Route<Register, RootRoute<Register, undefined, {}, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", (data: unknown) => {

}, ResolveParams<"/dashboard/$dashboardId">, ... 9 more ..., undefined>], unknown, unknown, unknown, undefined>, "never", false, RouterHistory, Record<...>>>
```

Route

.

```
RouteApi<"/dashboard/$dashboardId", RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, {}, AnyContext, AnyContext, ... 6 more ..., undefined>, "never", false, RouterHistory, Record<...>>>.useParams: <RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, {}, AnyContext, AnyContext, {}, undefined, readonly [Route<Register, RootRoute<Register, undefined, {}, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", (data: unknown) => {

}, ResolveParams<"/dashboard/$dashboardId">, ... 9 more ..., undefined>], unknown, unknown, unknown, undefined>, "never", false, RouterHistory, Record<...>>, unknown, boolean>(opts?: (UseParamsBaseOptions<...> & OptionalStructuralSharing<...>) | undefined) => {
```

useParams

()

const {

```
const asOf: string | undefined
```

asOf

} =

```
const Route: RouteApi<"/dashboard/$dashboardId", RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, {}, AnyContext, AnyContext, {}, undefined, readonly [Route<Register, RootRoute<Register, undefined, {}, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", (data: unknown) => {

}, ResolveParams<"/dashboard/$dashboardId">, ... 9 more ..., undefined>], unknown, unknown, unknown, undefined>, "never", false, RouterHistory, Record<...>>>
```

Route

.

```
RouteApi<"/dashboard/$dashboardId", RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, {}, AnyContext, AnyContext, ... 6 more ..., undefined>, "never", false, RouterHistory, Record<...>>>.useSearch: <RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, {}, AnyContext, AnyContext, {}, undefined, readonly [Route<Register, RootRoute<Register, undefined, {}, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", (data: unknown) => {

}, ResolveParams<"/dashboard/$dashboardId">, ... 9 more ..., undefined>], unknown, unknown, unknown, undefined>, "never", false, RouterHistory, Record<...>>, unknown, boolean>(opts?: (UseSearchBaseOptions<...> & OptionalStructuralSharing<...>) | undefined) => {
```

useSearch

()

const {

data

} =

```
useSuspenseQuery<Dashboard, Error, Dashboard, (string | Options | undefined)[]>(options: UseSuspenseQueryOptions<Dashboard, Error, Dashboard, (string | Options | undefined)[]>, queryClient?: QueryClient): UseSuspenseQueryResult<Dashboard, Error>
```

useSuspenseQuery

(

```
const dashboardQueryOptions: (dashboardId: string, options?: Options) => OmitKeyof<UseQueryOptions<Dashboard, Error, Dashboard, (string | Options | undefined)[]>, "queryFn"> & {

queryFn?: QueryFunction<Dashboard, (string | Options | undefined)[], never>;

queryKey: (string | Options | undefined)[] & {

[dataTagSymbol]: Dashboard;

[dataTagErrorSymbol]: Error;
```

dashboardQueryOptions

(

params

.

dashboardId

, {

asOf

}),
```

```
export const

```
const Route: Route<Register, RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", (data: unknown) => {

}, ResolveParams<"/dashboard/$dashboardId">, AnyContext, AnyContext, AnyContext, {

asOf: string | undefined;

}, ({ context, params, deps }: LoaderFnContext<Register, ... 8 more ..., undefined>) => Promise<...>, ... 4 more ..., undefined>
```

Route

=

```
createFileRoute<"/dashboard/$dashboardId", RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId">(path?: "/dashboard/$dashboardId" | undefined): <TRegister, TSearchValidator, TParams, TRouteContextFn, TBeforeLoadFn, TLoaderDeps, TLoaderFn, TChildren, TSSR, TMiddlewares, THandlers>(options?: (ParamsOptions<...> & ... 1 more ... & UpdatableRouteOptions<...>) | undefined) => Route<...>
```

createFileRoute

('/dashboard/$dashboardId')({

```
FilebaseRouteOptionsInterface<Register, RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, ... 12 more ..., undefined>.validateSearch?: Constrain<(data: unknown) => {

}, AnyValidator, DefaultValidator>
```

validateSearch

:

```
readonly 'asOf?': "string.date.iso";

}, {}>>(def: validateObjectLiteral<{

readonly 'asOf?': "string.date.iso";

readonly 'asOf?': "string.date.iso";
```

type

({ 'asOf?': 'string.date.iso' }).

```
Inferred<{ asOf?: string; }, {}>.assert: (data: unknown) => {
```

assert

,

```
FilebaseRouteOptionsInterface<Register, RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, ... 12 more ..., undefined>.loaderDeps?: (opts: FullSearchSchemaOption<RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, (data: unknown) => {

asOf: string | undefined;
```

loaderDeps

: ({

```
FullSearchSchemaOption<RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, (data: unknown) => { ...; }>.search: {
```

search

: {

asOf

} }) => ({

asOf

}),

```
FilebaseRouteOptionsInterface<Register, RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, ... 12 more ..., undefined>.loader?: Constrain<({ context, params, deps }: LoaderFnContext<Register, ... 8 more ..., undefined>) => Promise<...>, RouteLoaderFn<...> | RouteLoaderObject<...>>
```

loader

: async ({

```
queryClient: QueryClient;
```

context

,

params

,

```
asOf: string | undefined;
```

deps

}) => {

await

```
queryClient: QueryClient;
```

context

.

queryClient

.

```
QueryClient.ensureQueryData<Dashboard, Error, Dashboard, (string | Options | undefined)[]>(options: EnsureQueryDataOptions<Dashboard, Error, Dashboard, (string | Options | undefined)[], never>): Promise<Dashboard>
```

ensureQueryData

(

```
const dashboardQueryOptions: (dashboardId: string, options?: Options) => OmitKeyof<UseQueryOptions<Dashboard, Error, Dashboard, (string | Options | undefined)[]>, "queryFn"> & {

queryFn?: QueryFunction<Dashboard, (string | Options | undefined)[], never>;

queryKey: (string | Options | undefined)[] & {

[dataTagSymbol]: Dashboard;

[dataTagErrorSymbol]: Error;
```

dashboardQueryOptions

(

params

.

dashboardId

,

```
asOf: string | undefined;
```

deps

),

```
UpdatableRouteOptionsExtensions.component?: RouteComponent
```

component

:

```
const Dashboard: () => ReactElement
```

Dashboard

,
```

```
export const

```
const Route: Route<Register, RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", (data: unknown) => {

}, ResolveParams<"/dashboard/$dashboardId">, AnyContext, ({ params, deps }: RouteContextOptions<RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, ... 6 more ..., undefined>, ResolveParams<...>, AnyContext, {

}, "/dashboard/$dashboardId">) => {

}, ... 7 more ..., undefined>
```

Route

=

```
createFileRoute<"/dashboard/$dashboardId", RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId">(path?: "/dashboard/$dashboardId" | undefined): <TRegister, TSearchValidator, TParams, TRouteContextFn, TBeforeLoadFn, TLoaderDeps, TLoaderFn, TChildren, TSSR, TMiddlewares, THandlers>(options?: (ParamsOptions<...> & ... 1 more ... & UpdatableRouteOptions<...>) | undefined) => Route<...>
```

createFileRoute

('/dashboard/$dashboardId')({

```
FilebaseRouteOptionsInterface<Register, RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, ... 12 more ..., undefined>.validateSearch?: Constrain<(data: unknown) => {

}, AnyValidator, DefaultValidator>
```

validateSearch

:

```
readonly 'asOf?': "string.date.iso";

}, {}>>(def: validateObjectLiteral<{

readonly 'asOf?': "string.date.iso";

readonly 'asOf?': "string.date.iso";
```

type

({ 'asOf?': 'string.date.iso' }).

```
Inferred<{ asOf?: string; }, {}>.assert: (data: unknown) => {
```

assert

,

```
FilebaseRouteOptionsInterface<Register, RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, ... 12 more ..., undefined>.loaderDeps?: (opts: FullSearchSchemaOption<RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, (data: unknown) => {

asOf: string | undefined;
```

loaderDeps

: ({

```
FullSearchSchemaOption<RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, (data: unknown) => { ...; }>.search: {
```

search

: {

asOf

} }) => ({

asOf

}),

```
FilebaseRouteOptionsInterface<Register, RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, ... 12 more ..., undefined>.context?: Constrain<({ params, deps }: RouteContextOptions<RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, ... 6 more ..., undefined>, ResolveParams<...>, AnyContext, {

}, "/dashboard/$dashboardId">) => {

}, (ctx: RouteContextOptions<...>) => any>
```

context

: ({

params

,

```
asOf: string | undefined;
```

deps

}) => ({

```
dashboardQueryOptions: OmitKeyof<UseQueryOptions<Dashboard, Error, Dashboard, (string | Options | undefined)[]>, "queryFn"> & {

queryFn?: QueryFunction<Dashboard, (string | Options | undefined)[], never>;

queryKey: (string | Options | undefined)[] & {

[dataTagSymbol]: Dashboard;

[dataTagErrorSymbol]: Error;
```

dashboardQueryOptions

:

```
const dashboardQueryOptions: (dashboardId: string, options?: Options) => OmitKeyof<UseQueryOptions<Dashboard, Error, Dashboard, (string | Options | undefined)[]>, "queryFn"> & {

queryFn?: QueryFunction<Dashboard, (string | Options | undefined)[], never>;

queryKey: (string | Options | undefined)[] & {

[dataTagSymbol]: Dashboard;

[dataTagErrorSymbol]: Error;
```

dashboardQueryOptions

(

```
asOf: string | undefined;
```

deps

,

```
FilebaseRouteOptionsInterface<Register, RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, ... 12 more ..., undefined>.loader?: Constrain<({ context }: LoaderFnContext<Register, RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", ResolveParams<"/dashboard/$dashboardId">, {

asOf: string | undefined;

}, AnyContext, ({ params, deps }: RouteContextOptions<RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, ResolveParams<"/dashboard/$dashboardId">, AnyContext, {

asOf: string | undefined;

}, "/dashboard/$dashboardId">) => {

}, AnyContext, unknown, undefined>) => Promise<...>, RouteLoaderFn<...> | RouteLoaderObject<...>>
```

loader

: async ({

```
queryClient: QueryClient;

dashboardQueryOptions: OmitKeyof<UseQueryOptions<Dashboard, Error, Dashboard, (string | Options | undefined)[]>, "queryFn"> & {

queryFn?: QueryFunction<Dashboard, (string | Options | undefined)[], never>;

queryKey: (string | Options | undefined)[] & {

[dataTagSymbol]: Dashboard;

[dataTagErrorSymbol]: Error;
```

context

}) => {

await

```
queryClient: QueryClient;

dashboardQueryOptions: OmitKeyof<UseQueryOptions<Dashboard, Error, Dashboard, (string | Options | undefined)[]>, "queryFn"> & {

queryFn?: QueryFunction<Dashboard, (string | Options | undefined)[], never>;

queryKey: (string | Options | undefined)[] & {

[dataTagSymbol]: Dashboard;

[dataTagErrorSymbol]: Error;
```

context

.

queryClient

.

```
QueryClient.ensureQueryData<Dashboard, Error, Dashboard, (string | Options | undefined)[]>(options: EnsureQueryDataOptions<Dashboard, Error, Dashboard, (string | Options | undefined)[], never>): Promise<Dashboard>
```

ensureQueryData

(

```
queryClient: QueryClient;

dashboardQueryOptions: OmitKeyof<UseQueryOptions<Dashboard, Error, Dashboard, (string | Options | undefined)[]>, "queryFn"> & {

queryFn?: QueryFunction<Dashboard, (string | Options | undefined)[], never>;

queryKey: (string | Options | undefined)[] & {

[dataTagSymbol]: Dashboard;

[dataTagErrorSymbol]: Error;
```

context

.

```
dashboardQueryOptions: OmitKeyof<UseQueryOptions<Dashboard, Error, Dashboard, (string | Options | undefined)[]>, "queryFn"> & {

queryFn?: QueryFunction<Dashboard, (string | Options | undefined)[], never>;

queryKey: (string | Options | undefined)[] & {

[dataTagSymbol]: Dashboard;

[dataTagErrorSymbol]: Error;
```

dashboardQueryOptions

,

```
UpdatableRouteOptionsExtensions.component?: RouteComponent
```

component

:

```
const Dashboard: () => null
```

Dashboard

,

// in a different file, far far away

const

```
const routeApi: RouteApi<"/dashboard/$dashboardId", RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, RouteContext, AnyContext, AnyContext, {}, undefined, readonly [Route<Register, RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", (data: unknown) => {

}, ... 10 more ..., undefined>], unknown, unknown, unknown, undefined>, "never", false, RouterHistory, Record<...>>>
```

routeApi

=

```
getRouteApi<"/dashboard/$dashboardId", RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, RouteContext, AnyContext, AnyContext, {}, undefined, readonly [Route<Register, RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", (data: unknown) => {

}, ... 10 more ..., undefined>], unknown, unknown, unknown, undefined>, "never", false, RouterHistory, Record<...>>>(id: ConstrainLiteral<...>): RouteApi<...>
```

getRouteApi

('/dashboard/$dashboardId')

function

```
function DashboardContent(): void
```

DashboardContent

() {

const

```
queryClient: QueryClient;

dashboardQueryOptions: OmitKeyof<UseQueryOptions<Dashboard, Error, Dashboard, (string | Options | undefined)[]>, "queryFn"> & {

queryFn?: QueryFunction<Dashboard, (string | Options | undefined)[], never>;

queryKey: (string | Options | undefined)[] & {

[dataTagSymbol]: Dashboard;

[dataTagErrorSymbol]: Error;
```

context

=

```
const routeApi: RouteApi<"/dashboard/$dashboardId", RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, RouteContext, AnyContext, AnyContext, {}, undefined, readonly [Route<Register, RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", (data: unknown) => {

}, ... 10 more ..., undefined>], unknown, unknown, unknown, undefined>, "never", false, RouterHistory, Record<...>>>
```

routeApi

.

```
RouteApi<"/dashboard/$dashboardId", RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, RouteContext, AnyContext, ... 7 more ..., undefined>, "never", false, RouterHistory, Record<...>>>.useRouteContext: <RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, RouteContext, AnyContext, AnyContext, {}, undefined, readonly [Route<Register, RootRoute<Register, undefined, RouteContext, AnyContext, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", "/dashboard/$dashboardId", (data: unknown) => {

}, ResolveParams<"/dashboard/$dashboardId">, ... 9 more ..., undefined>], unknown, unknown, unknown, undefined>, "never", false, RouterHistory, Record<...>>, unknown>(opts?: UseRouteContextBaseOptions<...> | undefined) => {
```

useRouteContext

()

const {

data

} =

```
useSuspenseQuery<Dashboard, Error, Dashboard, (string | Options | undefined)[]>(options: UseSuspenseQueryOptions<Dashboard, Error, Dashboard, (string | Options | undefined)[]>, queryClient?: QueryClient): UseSuspenseQueryResult<Dashboard, Error>
```

useSuspenseQuery

(

```
queryClient: QueryClient;

dashboardQueryOptions: OmitKeyof<UseQueryOptions<Dashboard, Error, Dashboard, (string | Options | undefined)[]>, "queryFn"> & {

queryFn?: QueryFunction<Dashboard, (string | Options | undefined)[], never>;

queryKey: (string | Options | undefined)[] & {

[dataTagSymbol]: Dashboard;

[dataTagErrorSymbol]: Error;
```

context

.

```
dashboardQueryOptions: OmitKeyof<UseQueryOptions<Dashboard, Error, Dashboard, (string | Options | undefined)[]>, "queryFn"> & {

queryFn?: QueryFunction<Dashboard, (string | Options | undefined)[], never>;

queryKey: (string | Options | undefined)[] & {

[dataTagSymbol]: Dashboard;

[dataTagErrorSymbol]: Error;
```

dashboardQueryOptions

)
```

```
export const

```
const Route: RootRoute<Register, (data: unknown) => {

userQueryOptions: OmitKeyof<UseQueryOptions<User, Error, User, string[]>, "queryFn"> & {

queryFn?: QueryFunction<User, string[], never>;

[dataTagErrorSymbol]: Error;

}, AnyContext, {}, ({ context }: LoaderFnContext<Register, any, "__root__", {}, {}, RouteContext, () => {

}, AnyContext, unknown, undefined>) => Promise<...>, ... 4 more ..., undefined>
```

Route

=

```
createRootRouteWithContext<RouteContext>(): <TRegister, TRouteContextFn, TBeforeLoadFn, TSearchValidator, TLoaderDeps, TLoaderFn, TSSR, TServerMiddlewares>(options?: RootRouteOptions<TRegister, TSearchValidator, RouteContext, TRouteContextFn, TBeforeLoadFn, TLoaderDeps, TLoaderFn, TSSR, TServerMiddlewares, undefined> | undefined) => RootRoute<...>
```

createRootRouteWithContext

<

```
queryClient: QueryClient;
```

RouteContext

>()({

```
validateSearch?: Constrain<(data: unknown) => {

}, AnyValidator, DefaultValidator>
```

validateSearch

:

```
readonly debug: "boolean=false";

debug: Default<boolean, false>;

}, {}>>(def: validateObjectLiteral<{

readonly debug: "boolean=false";

readonly debug: "boolean=false";

debug: Default<boolean, false>;
```

type

({

debug

: `boolean=false` }).

```
Inferred<{ debug: Default<boolean, false>; }, {}>.assert: (data: unknown) => {
```

assert

,

```
context?: Constrain<() => {

userQueryOptions: OmitKeyof<UseQueryOptions<User, Error, User, string[]>, "queryFn"> & {

queryFn?: QueryFunction<User, string[], never>;

[dataTagErrorSymbol]: Error;

}, (ctx: RouteContextOptions<any, {}, RouteContext, {}, "__root__">) => any>
```

context

: () => ({

```
userQueryOptions: OmitKeyof<UseQueryOptions<User, Error, User, string[]>, "queryFn"> & {

queryFn?: QueryFunction<User, string[], never>;

[dataTagErrorSymbol]: Error;
```

userQueryOptions

:

```
queryOptions<User, Error, User, string[]>(options: UnusedSkipTokenOptions<User, Error, User, string[]>): OmitKeyof<UseQueryOptions<User, Error, User, string[]>, "queryFn"> & {

queryFn?: QueryFunction<User, string[], never>;

[dataTagErrorSymbol]: Error;
```

queryOptions

({

```
queryFn?: QueryFunction<User, string[], never>
```

queryFn

:

```
const getUser: () => Promise<User>
```

getUser

,

```
loader?: Constrain<({ context }: LoaderFnContext<Register, any, "__root__", {}, {}, RouteContext, () => {

}, AnyContext, unknown, undefined>) => Promise<...>, RouteLoaderFn<...> | RouteLoaderObject<...>>
```

loader

: async ({

```
queryClient: QueryClient;

userQueryOptions: OmitKeyof<UseQueryOptions<User, Error, User, string[]>, "queryFn"> & {

queryFn?: QueryFunction<User, string[], never>;

[dataTagErrorSymbol]: Error;
```

context

}) => {

await

```
queryClient: QueryClient;

userQueryOptions: OmitKeyof<UseQueryOptions<User, Error, User, string[]>, "queryFn"> & {

queryFn?: QueryFunction<User, string[], never>;

[dataTagErrorSymbol]: Error;
```

context

.

queryClient

.

```
QueryClient.ensureQueryData<User, Error, User, string[]>(options: EnsureQueryDataOptions<User, Error, User, string[], never>): Promise<User>
```

ensureQueryData

(

```
queryClient: QueryClient;

userQueryOptions: OmitKeyof<UseQueryOptions<User, Error, User, string[]>, "queryFn"> & {

queryFn?: QueryFunction<User, string[], never>;

[dataTagErrorSymbol]: Error;
```

context

.

```
userQueryOptions: OmitKeyof<UseQueryOptions<User, Error, User, string[]>, "queryFn"> & {

queryFn?: QueryFunction<User, string[], never>;

[dataTagErrorSymbol]: Error;
```

userQueryOptions

,

```
component?: RouteComponent
```

component

:

Root

,
```

```
const {

```
const userQueryOptions: OmitKeyof<UseQueryOptions<User, Error, User, string[]>, "queryFn"> & {

queryFn?: QueryFunction<User, string[], never>;

[dataTagErrorSymbol]: Error;
```

userQueryOptions

,

```
const dashboardQueryOptions: OmitKeyof<UseQueryOptions<Dashboard, Error, Dashboard, string[]>, "queryFn"> & {

queryFn?: QueryFunction<Dashboard, string[], never>;

[dataTagSymbol]: Dashboard;

[dataTagErrorSymbol]: Error;
```

dashboardQueryOptions

} =

```
const Route: Route<Register, Route<Register, RootRoute<Register, undefined, RouteContext, () => {

userQueryOptions: OmitKeyof<UseQueryOptions<User, Error, User, string[]>, "queryFn"> & {

queryFn?: QueryFunction<User, string[], never>;

[dataTagErrorSymbol]: Error;

}, AnyContext, {}, undefined, unknown, unknown, unknown, unknown, undefined>, ... 15 more ..., undefined>, ... 15 more ..., undefined>
```

Route

.

```
RouteExtensions<"/dashboard/$dashboardId/widget/$widgetId/", "/dashboard/$dashboardId/widget/$widgetId/">.useRouteContext: <RouterCore<Route<Register, any, "/", "/", string, "__root__", undefined, {}, RouteContext, () => {

userQueryOptions: OmitKeyof<UseQueryOptions<User, Error, User, string[]>, "queryFn"> & {

queryFn?: QueryFunction<User, string[], never>;

[dataTagErrorSymbol]: Error;

}, AnyContext, {}, undefined, readonly [Route<Register, ... 16 more ..., undefined>], unknown, unknown, unknown, undefined>, "never", false, RouterHistory, Record<...>>, unknown>(opts?: UseRouteContextBaseOptions<...> | undefined) => {
```

useRouteContext

()
```
