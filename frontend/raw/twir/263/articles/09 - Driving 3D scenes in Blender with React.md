---
type: twir-item
issue: 263
item: 9
item_type: item
date: 2025-12-17
source: https://romanliutikov.com/blog/driving-3d-scenes-in-blender-with-react
tags:
  - "Blender"
  - "3D"
status: auto
quality: keep
---

[[2025-12-17-TWIR-263|Index]]

# Item 9: Driving 3D scenes in Blender with React

Source: [https://romanliutikov.com/blog/driving-3d-scenes-in-blender-with-react](https://romanliutikov.com/blog/driving-3d-scenes-in-blender-with-react)

Summary:
This article explores using a custom React reconciler to declaratively build and manage Blender 3D scenes from JavaScript/React code. By embedding a JS engine in Blender and mapping React components to Blender objects, developers can use familiar React patterns—including hooks and component composition—to control 3D content and animation.

Key takeaways:
- Custom React reconciler enables React-driven 3D scene management in Blender.
- Blender’s Python API is exposed to React via an embedded JS engine (QuickJS).
- Materials, transforms, and animation can be managed using React components and hooks.
- Demonstrates the flexibility of React’s architecture beyond web UIs.

Recommendation:
Read fully

Content:
# Driving 3D scenes in Blender with React

*In this article I'm exploring an idea of using React to create and manage 3D scenes in [Blender](https://www.blender.org/). The project embeds a JavaScript engine into Blender and provides a custom [React reconciler](https://legacy.reactjs.org/docs/reconciliation.html) that maps React components to Blender objects.*

[](https://cdn.romanliutikov.com/videos/react-blender.mp4)

After playing a bit more with [custom React reconciler to render ImGui UIs natively with Static Hermes](https://romanliutikov.com/blog/native-apps-with-clojurescript-react-and-static-hermes), I thought of another fun idea, what if you could manage 3D scene in Blender using React's declarative approach to describing structure?

## The Architecture

Blender is a Python-based application. You can write addons in Python and call into Blender's API. This means we can embed JS interpreter in an addon, where we can run React code which in turn will call into Python API exposed to the interpreter.

I went with [QuickJS](https://bellard.org/quickjs/), since it's available on pip. It's a lightweight and fast JavaScript engine. A Python addon loads QuickJS into Blender and exposes Blender's API to JavaScript through a command interface. On top of that runs React with a custom reconciler that translates React operations into Blender commands.

## The Reconciler

If you've ever wondered how React can render to different targets: DOM, native mobile views, terminal UIs, the answer is the reconciler. React's core doesn't know anything about DOM elements or Blender objects. It just manages a tree of components and tells the reconciler when to create, update, or delete things. You can think of React as an interface of a virtual machine that translates declarative code into a series of imperative operations. And it's up to you to provide a concrete implementation of that interface for whatever target you want it to run on.

For Blender React, the reconciler translates React operations into commands that get sent to Python:

```
// When React creates a new element
createInstance(type, props) {
  const node = new BlenderNode(type, props);
  // Send command to Python/Blender
  sendCommand({
    type: "create_primitive",
    shape: type, // "cube", "sphere", etc.
    name: node.id,
    location: props.position,
    rotation: props.rotation,
    scale: props.scale,
  });
  return node;
}

// When React updates props
commitUpdate(instance, type, oldProps, newProps) {
  if (newProps.position !== oldProps.position) {
    sendCommand({
      type: "set_transform",
      name: instance.blenderName,
      location: newProps.position,
    });
  }
}
```

The Python side receives these commands and calls the appropriate Blender API functions:

```
elif kind == "create_primitive":
    shape = cmd["shape"]
    if shape == "cube":
        bpy.ops.mesh.primitive_cube_add(
            location=loc,
            rotation=rot,
            scale=scl
        )
    elif shape == "sphere":
        bpy.ops.mesh.primitive_uv_sphere_add(
            location=loc,
            rotation=rot,
            scale=scl
        )
    # ...
```

## Defining Scenes with Components

Once the reconciler is in place, you can define Blender scenes using familiar React patterns. Here's a simple example:

```
(ns app.core
  (:require [uix.core :as uix :refer [$ defui]]
            [blender.client :as bc]))

(defui app []
  ($ :<>
    ($ :cube {:position #js [0 0 0]})
    ($ :sphere {:position #js [3 0 0]})
    ($ :camera {:position #js [10 -10 8]
                :rotation #js [1.0 0 0.8]})))

(defn init []
  (bc/render #'app))
```

That's it, a cube, a sphere, and a camera. The `$` macro is UIx's way of creating React elements, and keywords like `:cube` and `:sphere` become Blender primitive types. I'm using ClojureScript on top of React here since hot-reloading works really well in cljs and it's crucial for interactive exploratory programming. In the video above you could see how objects are updated in real time as I'm updating code.

## Materials as Children

One thing that feels natural in this model is treating materials as children of mesh objects:

```
;; Red metallic cube
($ :cube {:position #js [0 0 0]}
  ($ :material {:color #js [1 0.2 0.2]
                :metallic 0.8
                :roughness 0.2}))

;; Glowing green sphere
($ :sphere {:position #js [3 0 0]}
  ($ :material {:color #js [0.1 0.1 0.1]
                :emission #js [0 1 0]
                :emissionStrength 5.0}))
```

When a material component is appended as a child of a mesh, the reconciler automatically assigns it. This is handled in the `appendInitialChild` hook:

```
appendInitialChild(parent, child) {
  parent.children.push(child);
  child.parent = parent;

  if (isMaterialType(child.type)) {
    assignMaterialToParent(child);
  }
}
```

## Animation with Hooks

Since we have full React running, hooks just work. Here's a spinning cube using `requestAnimationFrame`:

```
(defhook use-frame [f]
  (let [f* (uix/use-effect-event f)]
    (uix/use-effect
      (fn []
        (let [raf-id (atom nil)
              time (atom (js/getTime))
              animate (fn animate [t]
                        (f* (- t @time))
                        (reset! time t)
                        (reset! raf-id (js/requestAnimationFrame animate)))]
          (reset! raf-id (js/requestAnimationFrame animate))
          #(js/cancelAnimationFrame @raf-id)))
      [])))

(defui spinning-cube []
  (let [[rotation set-rotation] (uix/use-state 0)]
    (use-frame
      (fn [dt]
        (set-rotation + (* dt 0.005))))
    ($ :cube {:position #js [0 0 0]
              :rotation #js [0 0 rotation]}
      ($ :material {:color #js [0 0.5 0.2]
                    :metallic 0
                    :roughness 0.2}))))
```

The `use-frame` hook is similar to what you'd find in [react-three-fiber](https://github.com/pmndrs/react-three-fiber). It gives you a callback that runs every frame with delta time, and you use that to update state. The cube smoothly rotates because every state update triggers a re-render, which updates the Blender object's rotation at constant frame rate.

On the Python side, `requestAnimationFrame` is implemented using Blender's timer system:

```
def request_animation_frame(callback):
    raf_id = _next_raf_id[0]
    _next_raf_id[0] += 1

    _raf_callbacks[raf_id] = callback
    _pending_rafs.append((raf_id, callback))

    if not _raf_running[0]:
        _raf_running[0] = True
        bpy.app.timers.register(raf_loop, first_interval=1/60)

    return raf_id
```

## Geometry Nodes

Here's where it gets interesting. [Blender's geometry nodes](https://www.youtube.com/watch?v=aO0eUnu0hO0) are a powerful procedural system, and exposing them as React components opens up some nice composition patterns.

```
;; Scatter cubes on a grid
($ :plane {:position #js [0 0 0]}
  ($ :geometryNodes
    ($ :meshGrid {"Size X" 5 "Size Y" 5
                  "Vertices X" 20 "Vertices Y" 20})
    ($ :instanceOnPoints
      {:Instance ($ :meshCube {:Size #js [0.1 0.1 0.1]})})))
```

Notice how `:meshCube` is passed as a prop to `:instanceOnPoints`. The reconciler detects React elements in props and automatically creates the corresponding geometry nodes, connecting them to the right input sockets.

For sequential operations, nodes auto-chain:

```
;; Create a spiral tube
($ :cube {:position #js [0 0 0]}
  ($ :geometryNodes
    ($ :curveSpiral {:Rotations 3 :Height 2.0})
    ($ :curveToMesh {"Profile Curve" ($ :curveCircle {:Radius 0.1})})))
```

The reconciler walks through the geometry node children, creates them in Blender's node editor, and wires them together. Generators connect to processors, and the last node connects to the output.

![](https://cdn.romanliutikov.com/imgs/react-blender-1.jpg)

## Parent-Child Hierarchies

React's component tree naturally maps to Blender's object hierarchy:

```
($ :empty {:position #js [0 0 3]}
  ;; Children are positioned relative to parent
  ($ :cube {:position #js [1 0 0]}
    ($ :material {:color #js [1 0 0]}))
  ($ :sphere {:position #js [-1 0 0]}
    ($ :material {:color #js [0 0 1]})))
```

When you move the empty, both the cube and sphere move with it. The reconciler calls `set_parent` in Blender whenever a component is mounted as a child:

```
elif kind == "set_parent":
    child_name = cmd["child"]
    parent_name = cmd.get("parent")

    child_obj = bpy.data.objects.get(child_name)
    if parent_name:
        parent_obj = bpy.data.objects.get(parent_name)
        child_obj.parent = parent_obj
```

## Conclusion

That's yet another fun exploration of how âReact as VMâ can be applied in unexpected environments. The project is available at [github.com/roman01la/blender-react](https://github.com/roman01la/blender-react), have fun!
