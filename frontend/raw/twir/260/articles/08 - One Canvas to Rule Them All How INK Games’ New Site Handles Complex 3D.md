---
type: twir-item
issue: 260
item: 8
item_type: item
date: 2025-11-26
source: https://tympanus.net/codrops/2025/11/21/one-canvas-to-rule-them-all-how-ink-games-new-site-handles-complex-3d/
tags:
status: auto
---

[[2025-11-26-TWIR-260|Index]]

# Item 8: One Canvas to Rule Them All: How INK Games’ New Site Handles Complex 3D

Source: [https://tympanus.net/codrops/2025/11/21/one-canvas-to-rule-them-all-how-ink-games-new-site-handles-complex-3d/](https://tympanus.net/codrops/2025/11/21/one-canvas-to-rule-them-all-how-ink-games-new-site-handles-complex-3d/)

Content:
# One Canvas to Rule Them All: How INK Games’ New Site Handles Complex 3D

We set out to create a digital presence that reflects INK Games’ ambition and showcases the scale of their work in a way that feels bold, modern, and unmistakably theirs.

## Tech Stack and Tools

Like most of our projects, INK Games is built on top of ToyBox, our Next.js starter project.

CSS is handled with Styled Components and, as always, it features a bunch of scroll triggered animations, split texts, and cursor interactions, which are all handled with [GSAP](https://gsap.com/). Add in [Lenis](https://lenis.darkroom.engineering/) for smooth scrolling and [React Three Fiber](https://r3f.docs.pmnd.rs/) (R3F) for all your 3D needs and you have a solid base.

One additional requirement for this project was to use a self-hosted, headless CMS. For this we chose [Strapi](https://strapi.io/).

## Not Quite 3D

The website features many 3D elements, but not all of them use WebGL. Some sections have videos and images which rotate depending on the cursor position. We wanted to have a 3D perspective effect, where the image almost felt like a portal. We created a component, made to work with both images and videos and achieved the effect by mixing CSS 3D rotation and translating the image inside to fake perspective.

[](https://res.cloudinary.com/durdzswls/video/upload/v1763032686/codrops/not-quite-3d_bpzu00.mp4)

We use `<a href="https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/">gsap.matchMedia</a>` to handle the rotation on desktop only, and animate both the wrapper’s rotation and the inner image’s position with `gsap.to` on mouse movement.

## Actual 3D

One of the challenges for this project was handling multiple 3D sections on the same page. We could just have a canvas for each section, but having multiple canvases can really kill performance and some browsers limit how many 3D contexts you can have at the same time. We decided that every 3D section in a page needed to use the same canvas.

[](https://res.cloudinary.com/durdzswls/video/upload/v1763032688/codrops/3d_ozg88t.mp4)

R3F (more precisely [Drei](https://drei.docs.pmnd.rs/)) has a View component that is really useful. It uses WebGL’s scissor method to draw in a specific portion of a fixed canvas. We added a canvas to our Layout component so that it appeared on every page of the site, and inside of it a `View.Port` component, which tells R3F where the View components need to be rendered. Then, each of our sections using 3D is wrapped in a View component, which allows R3F to track the size and position of the container in which we want to render our 3D scene, and render the scene in the corresponding portion of the canvas.

The final part of our canvas preparation was to add some custom logic to dictate when the frame loop should be running, based on whether any 3D elements were visible or whether the page was resizing or scrolling.

To determine if any 3D section is visible, we used [ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/) on each section, and updated whether it was visible or not with the `onToggle` callback.

## Models

The trickiest part is done! Now we need to figure out how to best import the 3D models to our project. Thankfully there’s a great command-line tool that can do most of the work for us. Running a GLTF model through gltfjsx compresses and optimizes our model, and creates a JSX file which can then be imported into our scenes.

These JSX files are also useful if we want to change some things dynamically in our model, like the material. We can add props to the component that was generated, and change things accordingly.

## Portal cards

A really interesting section to work on was the portal cards section. The cards needed to do several things:

- To rotate with the cursor
- To have HTML text
- To have a background image with perspective/parallax
- To have 3D elements masked within the card bounds
- To have 3D elements visible outside of the card bounds

We managed to make them work by mixing a few techniques.

### Setting up the cards

First of all, we have both 3D elements and DOM elements that are positioned and sized in the same way. The DOM elements contain the text only, and the rest is in 3D.

We listen to the mouse events and compute the rotation according to the DOM elements, and apply the rotation both to the 3D elements and DOM elements on each frame.  
We cheat a bit to make things easier and apply a CSS perspective value to the DOM container in which we have our cards, computed based on the 3D viewport factor value.

For the background image, we use the R3F Billboard component, which makes sure the image always faces the camera, and we make the image a bit further away from the camera and a bit bigger than the container, for the parallax effect.

To have the elements masked within the card bounds, we use the R3F Mask component. This uses WebGL’s stencil buffer to cut out parts of the scene. We can wrap our card geometry with the Mask component, and then use the useMask hook to get a stencil value that needs to be used by every element that will be masked’s material (the background image as well as the 3D models). This is where having our models as JSX components where we can dynamically change the material can be useful.

[](https://res.cloudinary.com/durdzswls/video/upload/v1763030916/codrops/graph_cbz5e3.mp4)

Finally, for the elements visible outside the card bounds, we need clipping planes. We use a plane, which matches the card’s rotation to clip certain parts of the 3D elements. Whenever we update the card’s 3D rotation, we reset the plane to follow the Z axis again, and then apply the card’s 3D element’s world matrix to it.

We can now add the same models, which are masked within the card, a second time, but this time without stencil and with clipping planes. These elements will only be shown outside the card’s bounds.

### Animate the cards

Once everything is set up, we can add some animations.

First, we want the cards to rotate with our cursor. Since this should only happen on desktop, we use `gsap.matchMedia` to handle mouse events.

[](https://res.cloudinary.com/durdzswls/video/upload/v1763032263/codrops/portal_l21dsa.mp4)

Depending on the cursor position, we can now compute a target rotation for the card, and lerp the current rotation towards it on each frame.

Finally, we want to add a nice reveal animation for the cards, so we can use Scroll Trigger to trigger an animation when the section is in view, and animate the card’s target rotation from PI to 0.

## Conclusion

This project was quite challenging, especially in the 3D setup, but it was great to work on.

GSAP can be of great help for projects with lots of animations, especially when those are triggered with scroll. It’s such a flexible tool that it had us covered whether we were adding parallax to a simple DOM element or updating values to be fed into R3F frame loops.

We’re really happy with how it turned out 🙂

## Our Stack

- Next.js Framework
- GSAP for animation
- Lenis for scroll
- React Three Fiber + drei for WebGL
- Strapi for CMS

Key takeaways:
- No key takeaways extracted.

Recommendation: Summary sufficient
