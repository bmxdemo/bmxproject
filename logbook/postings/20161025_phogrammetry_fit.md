## Oct 25, 2016: Fits of 3d parabola to photogrammetry points

First, Evan and I measured the z height of the dish surface as a function of distance along the floor. We measured from the top of the box section at the location of the uprights, using them as a guide for verticality, and in between the uprights, using a plumb bob to establish verticality. This is shown in Figure 1. Fitting to a 2d parabola, the residuals are less than +/- 5 mm.

### Figure 1 - directly measured dish height

![fig_meas](https://cloud.githubusercontent.com/assets/6098508/19700497/8c2b1e28-9ac5-11e6-8f8c-1f8bfd2133e9.png)

Next, I took the direct x,y,z point cloud from photoscan and fit to a 3D parabola. I scaled the points to the measured dish dimensions, which has some systematic uncertainty of maybe 10%. The parabola has free parameters corresponding to offsets in x, y and z, a quadratic term in x and y, and a rotation about the x, y , and z axes. (There is no linear term.) The results are shown in Figures 2, 3 and 4. The residuals are +/- 20 mm, so factor 5 greater than directly measured. 

### Figure 2 - direct photoscan points and best fit 3D parabola

![fig_xyz_1](https://cloud.githubusercontent.com/assets/6098508/19700628/0f59f044-9ac6-11e6-9e45-f137d455df2d.png)

### Figure 3 - direct photoscan z residuals in 3D

![fig_xyz_2](https://cloud.githubusercontent.com/assets/6098508/19700633/1570fb58-9ac6-11e6-8e08-1260b0159642.png)

### Figure 4 - direct photoscan z residuals in 2D (median z in bins along x)

![fig_xyz_3](https://cloud.githubusercontent.com/assets/6098508/19700638/1c356b22-9ac6-11e6-8ab5-9ccb7761d2d4.png)

There is some weirdness in that if, instead of fitting the point cloud directly from photoscan, one first makes a 3D model, passes through the RHINO 3D cad software, and back to a point cloud, things look a little different. The 2D residuals using this procedure are shown in Figure 5. It makes sense the residuals are smaller because of the smoothing inherent in generating a mesh from a point cloud. But the features at the locations of the uprights seem to indicate that it is capturing something real. Also, the direct points have a different scaling along the x, y, and z axes, while the RHINO points do not. Subsequent direct point clouds (not shown) seem to have the same scaling, so this is a mystery that is not yet solved. The RHINO point cloud residuals are ~2x those of those measured directly with a ruler.

### Figure 5 - RHINO z residuals in 2D

![fig_rhino_3](https://cloud.githubusercontent.com/assets/6098508/19700889/1ac96e72-9ac7-11e6-892e-9ffa932694ff.png)
