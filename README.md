# CSC 365 Poster Project
This is the repository for our poster project. The cv2 image library for Python was used to take low sample path-traced images and turn them into clean images. The Cycles engine is required to make path-traced images as blender puts it, “Cycles is Blender’s physically-based path tracer for production rendering. It is designed to provide physically based results out-of-the-box, with artistic control and flexible shading nodes for production needs.” (Blender 2019) But to make really good images or animations requires a lot of computation power, our project is designed to reduce render costs and still make good quality images.

<br>

# Explanation of the Naming Conventions Used
Each of the pictures in the output folder is sorted into their specific 3D-model's file directory.
These follow the naming convention of:
typeOfAlgorithm + model + # of images + .png

<br>

# How to recreate the images given
### Step 1: Download the model of your choice:
Download one of the three models below in your choice of format (if you would like a different model choose)
### Step 2: Import model to blender:
First open blender, then at the top left of the scrreen hit the file menu then go down to import and select the file type you downloaded (Some may not be supported by blender, in that case select a supported file type), now you should see the model imported into blender, after that add lighting as needed and now it is time for rendering.
### Step 3: Render Settings
On the righthand side of your screen you should see the properties menu, to recreate the images used in the project, select the Cycles rendering engine, go to the render drop down table, here we will change two settings, the noise threshold, and the max samples. First set the noise threshold from 0.0100 to 0.1000, this will ensure noisier images which add a bit of texture to the image for added texture to the smoothing. Next comes the Max Samples, this will be set to 1, which gives 1 sample per pixel, which is the main cause for noisiness, a lower sample rate means it measures less of the object resulting in the kind of images we used in the project. After those two changes we made, we have to make a couple more changes, first is turning of the built-in denoise option, as it takes a while and denoises the image. After that you go into the advanced settings and add a custom seed. (One trick you could use is setting the seed to the frame and render it as an animation using ctrl+F12 this will generate all the images you want to put into the generator)

<br>

# References
### Blender Manual
Blender Team. (2019, August 13). Introduction — Blender Manual. Blender.org. [https://docs.blender.org/manual/en/2.80/render/cycles/introduction.html](https://docs.blender.org/manual/en/2.80/render/cycles/introduction.html)
### Mario Model
1. MatiasH290 (2020, November 10). Mario Obj. Sketchfab. [https://sketchfab.com/3d-models/mario-obj-c549d24b60f74d8f85c7a5cbd2f55d0f](https://sketchfab.com/3d-models/mario-obj-c549d24b60f74d8f85c7a5cbd2f55d0f)

### Space Explorer Model
2. Sharon Kunne (2021, May 12). Alien World Explorer. Sketchfab.
       [https://sketchfab.com/3d-models/alien-world-explorer-f73af15ccc2849098df32f48133cba9b](https://sketchfab.com/3d-models/alien-world-explorer-f73af15ccc2849098df32f48133cba9b)

### Voxel House Model
3. VoxelBear (2025, November 12). Minecraft House in the Forest. Sketchfab.
       [https://sketchfab.com/3d-models/minecraft-house-in-the-forest-5675f5d010a2408d98282ffd85a46198](https://sketchfab.com/3d-models/minecraft-house-in-the-forest-5675f5d010a2408d98282ffd85a46198)

### Lighting, Camera Work, and Editing by Michael Kauppila

<br>

# Credits (Code)
AI was used to help streamline the code and make it slightly faster.
It was specfically used in Lines 5 to 9 and Lines 15 to 25 to help read each of the images and make them fit into a faster reading of the images.
