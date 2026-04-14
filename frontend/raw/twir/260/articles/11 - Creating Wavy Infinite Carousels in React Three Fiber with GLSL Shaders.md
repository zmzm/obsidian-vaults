---
type: twir-item
issue: 260
item: 11
item_type: item
date: 2025-11-26
source: https://tympanus.net/codrops/2025/11/26/creating-wavy-infinite-carousels-in-react-three-fiber-with-glsl-shaders/
tags:
status: auto
---

[[2025-11-26-TWIR-260|Index]]

# Item 11: Creating Wavy Infinite Carousels in React Three Fiber with GLSL Shaders

Source: [https://tympanus.net/codrops/2025/11/26/creating-wavy-infinite-carousels-in-react-three-fiber-with-glsl-shaders/](https://tympanus.net/codrops/2025/11/26/creating-wavy-infinite-carousels-in-react-three-fiber-with-glsl-shaders/)

Content:
# Creating Wavy Infinite Carousels in React Three Fiber with GLSL Shaders

After coming across various infinite carousel effects on X created by some peers, I decided to give it a try and create my own. The idea here is to practice R3F and shader techniques while making something that can be easily reused in other projects.

[](https://codrops-1f606.kxcdn.com/codrops/wp-content/uploads/2025/11/carousels.mp4?x13084)

## Starter project

The base project is a simple Vite+React+TS application with an R3F Canvas, along with the following packages installed:

```
three
@react-three/fiber
@react-three/drei
```

Now that we’re all set, we can start writing our first shader.

## Creating the GLImage component

We want to display our images on planes, so that we can put them in our R3F scene and play with them, add displacement effects with shader etc.

First of all, let’s create our `vertex.glsl` and `fragment.glsl` files:

```
// vertex.glsl
varying vec2 vUv;

void main() {
  vec3 pos = position;
  gl_Position = projectionMatrix * modelViewMatrix * vec4( pos, 1.0 );

  // VARYINGS
  vUv = uv;
}
```

```
// fragment.glsl
precision highp float;

uniform sampler2D uTexture;
uniform vec2 uPlaneSizes;
uniform vec2 uImageSizes;

varying vec2 vUv;

void main() {
  vec2 ratio = vec2(
    min((uPlaneSizes.x / uPlaneSizes.y) / (uImageSizes.x / uImageSizes.y), 1.0),
    min((uPlaneSizes.y / uPlaneSizes.x) / (uImageSizes.y / uImageSizes.x), 1.0)
  );

  vec2 uv = vec2(
    vUv.x * ratio.x + (1.0 - ratio.x) * 0.5,
    vUv.y * ratio.y + (1.0 - ratio.y) * 0.5
  );

  vec4 finalColor = texture2D(uTexture, uv);  
  gl_FragColor = finalColor;
}
```

Here, we are passing the UVs of our mesh to the fragment shader and using them in the `texture2D` function to apply the image texture to our fragments.

We are also using two uniforms : `uPlaneSizes` and `uImageSizes`, which allow us to recalculate the UV coordinates and have an “object-fit cover like” effect on our plane. This will be very useful later if we want to change our plane sizes without distorting the images.

Now that our shaders are ready, let’s create our `<GLImage>` component:

```
import { useTexture } from "@react-three/drei";
import { forwardRef, useMemo, useRef } from "react";
import * as THREE from "three";
import imageFragmentShader from "../shaders/image/fragment.glsl?raw";
import imageImageVertexShader from "../shaders/image/vertex.glsl?raw";

interface GLImageProps {
  imageUrl: string;
  scale: [number, number, number];
  geometry: THREE.PlaneGeometry;
}

const GLImage = forwardRef<THREE.Mesh, GLImageProps>(
  (
    {
      imageUrl,
      scale,
      geometry,
    },
    forwardedRef
  ) => {
    const localRef = useRef<THREE.Mesh>(null);
    const imageRef = forwardedRef || localRef;
    const texture = useTexture(imageUrl);

    const imageSizes = useMemo(() => {
      if (!texture) return [1, 1];
      return [texture.image.width, texture.image.height];
    }, [texture]);

    const shaderArgs = useMemo(
      () => ({
        uniforms: {
          uTexture: { value: texture },
          uPlaneSizes: { value: new THREE.Vector2(scale[0], scale[1]) },
          uImageSizes: {
            value: new THREE.Vector2(imageSizes[0], imageSizes[1]),
          },
        },
        vertexShader: imageImageVertexShader,
        fragmentShader: imageFragmentShader,
      }),
      [texture, scale, imageSizes]
    );

    return (
      <mesh position={[0, 0, 0]} ref={imageRef} scale={scale}>
        <primitive object={geometry} attach="geometry" />
        <shaderMaterial {...shaderArgs} />
      </mesh>
    );
  }
);

export default GLImage;
```

Here, we’re loading the image texture with `useTexture` from `@react-three/drei`.

Then, we create our shader material arguments (the uniforms and shader files used in it) and add it to our plane mesh with `shaderMaterial`.

We should obtain something like this:

![](https://codrops-1f606.kxcdn.com/codrops/wp-content/uploads/2025/11/Screenshot-2025-11-17-at-22.00.20-800x432.png?x13084)

Displaying an image on a plane geometry with shaders

## Displaying multiple images

Now that our base `GLImage` component is ready, we will create a simple `<Carousel>` component that will map an image list and display them in a column shape, taking an image size and a gap as props:

```
import { useMemo, useRef } from "react";
import * as THREE from "three";
import { IMAGE_LIST } from "../constants";
import GLImage from "./GLImage";

interface CarouselProps {
  position?: [number, number, number];
  imageSize: [number, number];
  gap: number;
}

const Carousel = ({ position, imageSize, gap }: CarouselProps) => {
  const imageRefs = useRef<THREE.Mesh[]>([]);

  const planeGeometry = useMemo(() => {
    return new THREE.PlaneGeometry(1, 1, 16, 16);
  }, []);

  return (
    <group position={position || [0, 0, 0]}>
      {IMAGE_LIST.map((url, index) => (
        <GLImage
          key={index}
          imageUrl={url}
          scale={[imageSize[0], imageSize[1], 1]}
          geometry={planeGeometry}
          position={[0, index * (imageSize[1] + gap), 0]}
          ref={(el) => {
            if (el) imageRefs.current[index] = el;
          }}
        />
      ))}
    </group>
  );
};

export default Carousel;
```

Here, we’re mapping our image list and using the index of each image to set a new prop named `position` so that our images look like this:

![](https://codrops-1f606.kxcdn.com/codrops/wp-content/uploads/2025/11/Screenshot-2025-11-17-at-22.19.32-800x430.png?x13084)

Column layout for our images

## Infinite effect on scroll

For the infinite scroll effect, we’re going to move all our planes along the Y-axis based on the wheel velocity (using Lenis in my case for simplicity). On each frame, we apply a modulo function to the plane positions to wrap them back to the top or bottom depending on their current Y position:

```
// Carousel.tsx
const totalHeight = IMAGE_LIST.length * gap + IMAGE_LIST.length * imageSize[1];

useFrame(() => {
  imageRefs.current.forEach((ref) => {
    if (!ref) return;
    ref.position.y =
      mod(ref.position.y + totalHeight / 2, totalHeight) - totalHeight / 2;
  });
});

useLenis(({ velocity }) => {
  imageRefs.current.forEach((ref) => {
    if (ref) {
      ref.position.y -= velocity * 0.005;
    }
  });
});
```

The `mod()` function here is used to wrap each plane back into the valid range so that, whenever a plane moves too far up or down, its position is recalculated and it re-enters the loop seamlessly, keeping the carousel infinite:

```
function mod(n: number, m: number) {
  return ((n % m) + m) % m;
}
```

We should now have something like this:

[](https://codrops-1f606.kxcdn.com/codrops/wp-content/uploads/2025/11/record1.mov?x13084)

Infinite effect on scroll

## Displacement effect on the planes

First, we want our planes to stretch vertically depending on the wheel velocity. To do this, we are going to add a `uScrollSpeed` uniform to the material arguments and update this uniform on scroll in our `Carousel` component:

```
// GLImage.tsx
const shaderArgs = useMemo(
  () => ({
    uniforms: {
      // ...
      uScrollSpeed: { value: 0.0 },
    },
    vertexShader: imageImageVertexShader,
    fragmentShader: imageFragmentShader,
  }),
  [texture, scale, imageSizes]
);

// Carousel.tsx
useLenis(({ velocity }) => {
  imageRefs.current.forEach((ref) => {
    if (ref) {
      ref.position.y -= velocity * 0.005;
      ref.material.uniforms.uScrollSpeed.value = velocity * 0.005;
    }
  });
});
```

Then in our `vertex.glsl` shader, we’re going to use this uniform and displace our vertex on the Y axis with `PI` and a `sin()` function which will allow us to have that “rounded” displacement:

```
uniform float uScrollSpeed;

varying vec2 vUv;

#define PI 3.141592653

void main() {
  vec3 pos = position;

  // Y Displacement according to the scroll speed
  float yDisplacement = -sin(uv.x * PI) * uScrollSpeed;
  pos.y += yDisplacement;

  gl_Position = projectionMatrix * modelViewMatrix * vec4( pos, 1.0 );

  // VARYINGS
  vUv = uv;
}
```

We should now have something like this:

[](https://codrops-1f606.kxcdn.com/codrops/wp-content/uploads/2025/11/record2.mov?x13084)

Displacement on our planes depending on wheel velocity

## Wavy effect on the carousel

Now, let’s add a wavy effect to our carousel, I want the planes to be displaced in a curved shape according to their position in my 3D scene.

To do this, we’re going to add two more uniforms to our shader and use them with the world position of our planes just like this:

```
// vertex.glsl
uniform float uScrollSpeed;
uniform float uCurveStrength;
uniform float uCurveFrequency;

varying vec2 vUv;

#define PI 3.141592653

void main() {
  vec3 pos = position;
  vec3 worldPosition = (modelMatrix * vec4(position, 1.0)).xyz;

  // X Displacement depending on the world position Y
  float xDisplacement = uCurveStrength * cos(worldPosition.y * uCurveFrequency);
  pos.x += xDisplacement;
  pos.x -= uCurveStrength;

  // Y Displacement according to the scroll speed
  float yDisplacement = -sin(uv.x * PI) * uScrollSpeed;
  pos.y += yDisplacement;

  gl_Position = projectionMatrix * modelViewMatrix * vec4( pos, 1.0 );

  // VARYINGS
  vUv = uv;
}
```

Here, we’re using a cosinus on the `worldPosition.y` of our planes, so that the “top” of the curve will always be at the center of our canvas (because when `y=0`, `cos(y)=1`).

And don’t forget to add some props to the `GLimage` as well as adding the uniforms in our shader material arguments:

```
// GLImage.tsx
const shaderArgs = useMemo(
  () => ({
    uniforms: {
      // ...
      uCurveStrength: { value: curveStrength || 0 },
      uCurveFrequency: { value: curveFrequency || 0 },
    },
    vertexShader: imageImageVertexShader,
    fragmentShader: imageFragmentShader,
  }),
  [texture, curveStrength, curveFrequency, scale, imageSizes]
);
```

We should now have something like this:

[](https://codrops-1f606.kxcdn.com/codrops/wp-content/uploads/2025/11/record3.mov?x13084)

Curved effect on our carousel

Note : as a bonus, you can add `leva` or any other tweaking library in order to tweak and find the best values for the `curveStrength` and `curveFrequency` of the carousel.

## Playing around and going further

Now that we have an easily reusable and tweakable `<Carousel>` component, we can play with it, add more of them in the scene, change the wheel direction, the wheel speed etc.

Here are some examples of what you can do with it:

![](https://codrops-1f606.kxcdn.com/codrops/wp-content/uploads/2025/11/Screenshot-2025-11-18-at-00.13.02-800x446.png?x13084)
![](https://codrops-1f606.kxcdn.com/codrops/wp-content/uploads/2025/11/Screenshot-2025-11-18-at-00.20.10-800x440.png?x13084)
![](https://codrops-1f606.kxcdn.com/codrops/wp-content/uploads/2025/11/Screenshot-2025-11-18-at-01.14.03-800x448.png?x13084)

![](https://codrops-1f606.kxcdn.com/codrops/wp-content/uploads/2025/11/Screenshot-2025-11-18-at-00.27.29-800x431.png?x13084)
![](https://codrops-1f606.kxcdn.com/codrops/wp-content/uploads/2025/11/Screenshot-2025-11-24-at-22.49.43-800x434.png?x13084)
![](https://codrops-1f606.kxcdn.com/codrops/wp-content/uploads/2025/11/Capture-decran-2025-11-18-a-17.01.24-800x431.png?x13084)

Examples available in the demo

If you want to go further, you can try adding some noise displacement to the fragment shader based on the wheel velocity. This could give your carousel a more organic feel and is also a great exercise.  
You can also add a `direction` prop to the `Carousel` component to create a horizontal carousel instead of a vertical one, like I did in some of the examples.

Finally, if you’d like to see more of my work, make sure to follow me on [X](https://www.x.com/colindmg) or [Linkedin](https://www.linkedin.com/in/colindmg). I post all my projects and experiments there.

Thanks for reading! 🙂

Key takeaways:
- No key takeaways extracted.

Recommendation: Summary sufficient
