---
type: twir-item
issue: 254
item: 5
item_type: item
date: 2025-10-15
source: https://www.orilivni.com/2025/10/serialization-and-deserialization/
tags:
status: auto
quality: keep
---

[[2025-10-15-TWIR-254|Index]]

# Item 5: Serialization and deserialization without blowing React

Source: [https://www.orilivni.com/2025/10/serialization-and-deserialization/](https://www.orilivni.com/2025/10/serialization-and-deserialization/)

Summary:
The article discusses efficient patterns for synchronizing string-based sources (like localStorage or history) with React state, focusing on minimizing unnecessary re-renders and performance issues. It walks through naive and improved implementations for deserializing data, handling partial updates, and avoiding redundant parsing or object instantiation, especially when dealing with non-primitive values. The final approach advocates for a single deserialized source of truth and careful update logic to prevent excessive renders.

Key takeaways:
- Naive deserialization can cause unnecessary re-renders and performance hits.
- Parsing data once and sharing a single instance across components improves efficiency.
- Special care is needed when updating nested or referenced values to avoid full re-renders.
- Write-only patterns can further optimize updates but require careful state management.

Recommendation:
Read fully (for developers handling complex state synchronization or optimizing React performance)

Why it matters:
for developers handling complex state synchronization or optimizing React performance

Content:
# Serialization and deserialization without blowing React

Letâs say you have a `string` source of data. You need to read and write from it. You donât really have much to do with `string` so youâd deserialize it and use `JSON.parse(â¦)` and when you need to serialize it again, youâd use `JSON.stringify(â¦)`.

It might not sound much, but when youâre dealing with complex objects combined with an immutable data based system, it might lead to unintended re-rendering cycles, and can cause full page re-renders for data that wasnât actually changed. This specifically was a major performance issue we had to fix where I work.

This isnât an esoteric issue, since popular browser APIs such as `history`, `localStorage` force you to use `string`s while we often work with `object`s.

Until we reached a solution we are happy with, we went through a few phases. I think most developers would go a similar path.

## The naive solution

When approaching this problem, the naive solution is something as:

```
function useData() {
	

	
	
	
	const data = useMemo(() => JSON.parse(rawData), [rawData]);

	const setData = useCallback((data) => {
		
		source.setValue(JSON.stringify(data));
	}, []);

	return [data, setData];
}
```

And the usage of this hook might look like:

```
const [data, setData] = useData();

return (
	<button
		onClick={() => {
			setData({ ...data, count: data.count + 1 });
		}}
	>
		{data.count}
	</button>
);
```

This solution might be good enough for many cases, but it has some limitations.

For example, if you have 100 components that are based on different parts of the data, you might suffer from ergonomics. So you might change the implementation to something as:

```
function useData(key) {

	const value = useMemo(() => JSON.parse(rawData)[key], [rawData, key]);

	const setValue = useCallback(
		(value) => {
			source.setValue(
				JSON.stringify({
					...JSON.parse(source.value),
					[key]: value,
				}),
			);
		},
		[key],
	);

	return [value, setValue];
}
```

And the usage will be turned to something simpler as:

```
const [count, setCount] = useData("count");

return (
	<button
		onClick={() => {
			setCount(count + 1);
		}}
	>
		{data.count}
	</button>
);
```

This solution might be more ergonomic, but it still has some issues. If you have 100 components that are connected to the source:

1. it means you will call `JSON.parse(â¦)` implicitly 100 times, which is expensive!
2. it also means you hold in memory 100 instances of identical data

## Single source for all

The solution for this issue is moving to a single source for all the deserialized state. So we only deserialize once, and save only a single instance for all usages. To make it, we need to wrap the source. For the sake of simplicity of the example, I didnât make an actual wrapper, but added a variable and emitter that will replace the âsourceâ inside the hook. So now, our implementation looks as followed:

```
const emitter = new Emitter();

let currentValue = JSON.parse(source.value);

	
	currentValue = JSON.parse(source.value);
	
	emitter.emit();
});

function useData(key) {
	const value = useSyncExternalStore(
		
		() => currentValue[key],
	);

	const setValue = useCallback(
		(value) => {
			source.setValue(
				JSON.stringify({
					...currentValue,
					[key]: value,
				}),
			);
		},
		[key],
	);

	return [value, setValue];
}
```

We have some improvement, but now our issue is what happens when the values of the object arenât primitives. (Values that have a reference. For example: `array` and `object`).

If we have structure such as this:

## Using serialization as write-mode only

To solve this, the naive solution is just ignoring updates, and moving to write-only mode. So, we might read from the source on loading, but from there, we only write and never read again.

So now, after page load `currentValue` will only change during `setValue`, and it will be modified directly. It means that if `b` changes, `a` will remain with the same reference.

```
const emitter = new Emitter();

let currentValue = JSON.parse(source.value);

function useData(key) {
	const value = useSyncExternalStore(
		() => currentValue[key],
	);

	const setValue = useCallback(
		(value) => {
			
			
			
			currentValue = {
				...currentValue,
				[key]: value,
			};

			
			source.setValue(JSON.stringify(currentValue));

			
			emitter.emit();
		},
		[key],
	);

	return [value, setValue];
}
```

We solved one issue, but we got another bigger issue. The source might be updated externally, and we need to choose between, ignoring updates, or updating and losing the optimization. But there is a good solutionâ¦

## Structural sharing

What if we could create a new object that all of its unchanged parts preserve the old references? In Solid we have a nice utility called [`reconcile`](https://docs.solidjs.com/reference/store-utilities/reconcile) that works with mutable data. Sadly, React doesnât have something similar for immutable data, but [TanStack Query](https://tanstack.com/query/latest) did exactly this inside their code. Itâs called [`replaceEqualDeep`](https://github.com/TanStack/query/blob/v5.90.3/packages/query-core/src/utils.ts#L257) and I recommend you take a look at its code.

The way `replaceEqualDeep` works is by recursively traversing both the old and the new objects. It goes from the leaves to the root, and checks if data is changed. If it is structurally equal it will return the old data. If itâs not structurally equal it will merge old data with new data to a new object. This way it achieves structure sharing, and old data will be preserved and left unchanged.

It means that places that werenât changed, wonât be re-rendered. From React perspective nothing has changed. No re-render is needed.

The complete solution is:

```
const emitter = new Emitter();

let currentValue = JSON.parse(source.value);

	
	currentValue = replaceEqualDeep(currentValue, JSON.parse(source.value));
	emitter.emit();
});

function useData(key) {
	const value = useSyncExternalStore(
		() => currentValue[key],
	);

	const setValue = useCallback(
		(value) => {
			source.setValue(
				JSON.stringify({
					...currentValue,
					[key]: value,
				}),
			);
		},
		[key],
	);

	return [value, setValue];
}
```

## Conclusion

With structural sharing weâve fixed our performance issue, and the freedom to update the source out of our own wrapper. Weâre also getting extra benefits. Now, we can also have selectors, and we arenât limited to a top-level property.

Iâve ignored issues related to `useSyncExternalStore` and lack of support for concurrent rendering as itâs not what the post is about.
