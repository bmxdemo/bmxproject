# Characterise the surface of the proto-petal, was issue 9

From Paul's email:

 Justine provided the mirrored ramp support pieces and the full set of "tee" sheet support pieces, for two intermediate locations in each interval; and Evan, Amina and I got the whole thing together this afternoon.  We then made a series of measurements, looking at the height of the (bottom of) the sheet above the diagonal spacer bar across several locations.  The results for the upper three intervals are shown in the attached graphs.  In each case, the colored curve represents where the sheet height should ideally be according to the mathematical model, while the  dots are the measured heights at intervals along the bar (figure about a +/-0.5mm measurement uncertainty, and these are only along the left edge of the petal).  The arrows show the locations of the new tee support pieces along each sheet.

As you can see from the graphs the sheet position is pretty good, within a millimeter or so of the ideal; except for a noticeable "sag" in the middle of the 4-5 interval and a slightly smaller one in the middle of the 2-3 interval.  These correspond to the width of the span between the tee supports: the 4-5 is about 56cm between supports and sags about 3mm low; the 2-3 spans over about 40cm and sags about 2mm; while in 3-4 the tee spacing is only 30cm and doesn't show any visible sag in the middle.  I think this is giving us a measure of how floppy the sheet is under its own weight between clamps, and you can even see the effect in the photo if you look closely enough.

  Now, a defect of 2-3mm over a part of the surface is within our original goal of 5mm accuracy, so we can simply declare victory at this point if we want to. Note that this assembly was with no fine-tuning or pulling of any kind; the sheets were just laid down naturally on the supports and screwed down with no internal tension, which is what we would want for the production assembly.  I am thinking, though, that it would be worth the small amount of additional effort and plastic to add one more support tee for the middle of at least spans 4-5 and 2-3, which should suffice to bring the whole surface to within +/- 1mm of ideal. That's a nice, conservative starting point to be at before bringing the assemblies out into the wild.

  I'll be away all next week, and during that time I invite Justine to have a look at the setup and see what she wants to recommend next.  Meanwhile, Mike I think you can go ahead and drill and pin the side plane diagonals whenever you want to, as it stands now, though there's no rush on this.  Note, that we are still wide open to any and all ideas about how to survey the sheet shape from an external vantage point, let us know if you have any (actionable) suggestions.

![full_sheet_with_tees_6may](https://cloud.githubusercontent.com/assets/1197186/15110234/91455144-15d7-11e6-8b95-a016a0084b2f.JPG)
[sheet_measured_23_withtees_6May.pdf](https://github.com/bmxdemo/bmxproject/files/254728/sheet_measured_23_withtees_6May.pdf)
[sheet_measured_34_withtees_6May.pdf](https://github.com/bmxdemo/bmxproject/files/254727/sheet_measured_34_withtees_6May.pdf)
[sheet_measured_45_withtees_6May.pdf](https://github.com/bmxdemo/bmxproject/files/254726/sheet_measured_45_withtees_6May.pdf)

## 2

Over the summer, myself, Paul Stankus, and Erin Sheldon pursued the method of photogrammetry for characterizing the dish surface after Paul O'Connor pointed us in the right direction.  The slides I gave for the June telecon describe the method in more detail.

[Photogrammetry.pdf](https://github.com/bmxdemo/bmxproject/files/452569/Photogrammetry.pdf)

I managed to use PhotoScan and Rhino 3D to create a 3D model of the dish, and then get a list of points on its surface.  The .txt file with the spatial (x, y, z) points of the surface is attached below.  The file is simply a three column list with no added features.  The method I used was to extract the surface of the petal in Rhino (after having created the 3D model in PhotoScan).  Basically, I explode the 3D model into various surfaces and then join together the pieces of interest -- i.e. the pieces that make up the dish surface.  This mesh is then converted into physical points (I believe the points correspond to intersections of the vectors that make up the mesh).  Each physical point is assigned a coordinate based on the axes I created around the dish surface and then exported as such.

A few things: these points are randomly chosen based on the mesh, so it is not all too clear to me what level of precision we are to expect here, or how accurately they represent the true dish surface.  There are roughly 80,000 points.  The next step is to analyze this data.

[BMX_petal_surface_Rhino.txt](https://github.com/bmxdemo/bmxproject/files/452492/BMX_petal_surface_Rhino.txt)

## Sept 6, 2016: Dish parabola parameters (PS)

I can specify what shape we were aiming for with the dish petal design, which may help with interpreting the photogrammetry data.  Some of these numbers are approximate, I can get them all to three digits later as needed.

Coordinates: x runs along the long axis of the petal, down the center line which is also the symmetry axis.  x=0 corresponds to the center of the parent paraboloid bowl

y runs horizontally across the petal, ie perpendicular to x in a horizontal plane.  y=0 corresponds to the x axis, ie the symmetry axis down the middle of the petal.

z runs vertically, ie parallel to the axis of the parent paraboloid.  The offset is effectively arbitrary, but can be approximated by saying that the front end of the sheet is about 15 cm above the
floor.

The petal surface should follow a parabola in the x-z plane

z(x) = x^2 / (4 f)

where the focal length f is a hair shy of the focal length of the parent paraboloid, which is chosen to be 290 cm.

The extent along the x axis for the sheet is intended to be from x=+70cm to +470cm, ie a full span of 4 meters; there is an added buffer of about 10cm on each end for mounting, so the full span of the actual piece is about x = 60cm to 480cm; these can be measured more exactly as needed.

The surface is flat along the y direction.  The extent of the surface along y at a given x satisfies the petal occupying a full width of 8 degrees as seen from above, ie

-sin(4 degree) x < y(x) < +sin(4 degree) x

## 2

Chris Sheehy and I have begun the process of using reflective tape and low exposure photographs to improve the photogrammetry procedure.  First of all, PhotoScan has a coordinate system that is not ideal -- it defines the direction that the camera is pointing (in one of any of the arbitrary photographs) to be -z.  The 3D model ends up sitting in a troubling position and when the XYZ points are exported from PhotoScan, it is difficult to analyze.  To account for this, we have written a simple python script that rotates the dish by applying rotation matrices to each exported point in the .txt file.

The code is here:
https://github.com/bmxdemo/bmxproject/blob/master/ipynb/parab3d.py

The code reads in the .txt file of XYZ points.  For now, all we have is the points from the original process in which we did not use reflective tape.  We realized that Rhino is not necessary after all, and thus here is the file of points exported directly from PhotoScan, located on my Google Drive since the file is too large for GitHub:

https://drive.google.com/drive/folders/0BxSWxTxFUD23ZXRFTHRST3lRM0U?usp=sharing

Here is the output of the code.  It plots the unrotated figure in blue and the rotated figure in red.  Since I had previously rotated this set of points by hand in PhotoScan (which is a pain, and hence the reason for the code) we set the rotation angles to zero, and the red and blue figures are overlaid.  The point is that every time we take a new set of photos it is anyone's guess as to how the coordinate system will orient itself.  So, while the figure does not need to be rotated for the old photos, it will need to be rotated for the new reflective tape photos.  

![petalv1](https://cloud.githubusercontent.com/assets/17692591/18458188/205ad724-792d-11e6-9ac2-67e5fd745d89.png)

Now for the reflective tape.  The first step was to figure out which tape would work best.  First, we tried 5997T81 floor tape.  Here is a photo of what this looks like on the petal at low exposure:

![img_2513](https://cloud.githubusercontent.com/assets/17692591/18458217/5db9feba-792d-11e6-8d42-878e84b9e821.JPG)

This was not really reflective enough, so today we tried 15835T58 vehicle tape.  You can see the improvement in this photo: 

![img_2528](https://cloud.githubusercontent.com/assets/17692591/18458227/67e76760-792d-11e6-8c94-6bce98650d5d.JPG)

Now, this tape will be cut up and placed all over the petal, but today I quickly took some photos with the strip sitting in the center of the dish to see what PhotoScan could do with it.  Here is the model it produced:

![vehicle_tape_model](https://cloud.githubusercontent.com/assets/17692591/18458371/99f929b8-792e-11e6-99b8-a01ae85cf7b1.png)

This is, indeed, extremely crude; however, I merely wanted to see if PhotoScan could handle low exposure images, and it seems like it can.  Therefore, the next steps are to cover the petal in the reflective vehicle tape and make a model in PhotoScan to export and analyze.

## 3

We have decided to try the Photogrammetry process with the lights turned on (without the reflective tape), while we sort out some issues with the reflective tape process, to make sure that everything is working properly.  This model uses a new set of photos that I took on 29 September 2016 since the dish has been slightly modified from the last set of photos I took with the lights on.

Here is a screenshot of the model for the tie points (the sparse point cloud):

![screen shot 2016-10-01 at 12 38 34 pm](https://cloud.githubusercontent.com/assets/17692591/19015518/15283058-87d4-11e6-9257-6697f076be96.png)

Here is the corresponding exported xyz points:

[Visual_v2_tie_points.txt.zip](https://github.com/bmxdemo/bmxproject/files/504484/Visual_v2_tie_points.txt.zip)

Here is a screenshot for the model of the dense point cloud:

![screen shot 2016-10-01 at 12 38 46 pm](https://cloud.githubusercontent.com/assets/17692591/19015519/19fc01a4-87d4-11e6-86fe-b102e219bdce.png)

and those corresponding xyz points which are located in my Google Drive:

https://drive.google.com/file/d/0BxSWxTxFUD23bWJmNllNaTd1alE/view?usp=sharing

## 4
The last model makes use of screws sticking out of the surface at various fixed locations to use as markers in order to analyze distances in a CAD program:

![img_2860](https://cloud.githubusercontent.com/assets/17692591/19174736/11be0620-8bff-11e6-98c1-00dc7cd81557.JPG)

Here is a .obj 3D mesh model of the dish

[Visual_v2.obj.zip](https://github.com/bmxdemo/bmxproject/files/515017/Visual_v2.obj.zip)

In order to analyze the surface properly, I removed these protruding objects in the software.  Here is the 3D points for the dish surface without the screws

https://drive.google.com/file/d/0BxSWxTxFUD23QkV1YlJtUGRKbUk/view?usp=sharing

and the .obj 3D model

[Visual_v2_surface.obj.zip](https://github.com/bmxdemo/bmxproject/files/515020/Visual_v2_surface.obj.zip)

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


## Oct 25, 2016: Directly measured screw locations w.r.t. photogrammetry

Figure 1 shows the 3D point cloud from [Evan's posting](https://github.com/bmxdemo/bmxproject/issues/9#issuecomment-252121391) imported into solidworks. We were able to measure the distance in the model between various pairs of screw heads and compare to measurements of the actual dish using our expensive, 2m long ruler. Results are in the next posting from Evan. 

It should be noted just how ragged the screws actually look, though. Figure 2 shows a zoom in. It is clear that it is not really localizing them very well.

### Figure 1 - photogrammetry points imported into Solidworks

![visual_v2_dense_cloud](https://cloud.githubusercontent.com/assets/6098508/19701382/2d685b7c-9ac9-11e6-9fa4-9a12ffc0b562.JPG)

### Figure 2 - screw heads

![screw_heads](https://cloud.githubusercontent.com/assets/6098508/19701666/5c5d1fb6-9aca-11e6-959c-3eb766e88c59.PNG)


## Oct 27, 2016: First results from Photomodeler

I purchased Photomodeler standard, the software SPT uses to do its dish photogrammetry. The program is vastly superior to Photoscan, which is what we have been using up until now. It is clear the Photoscan enterprise was doomed to failure from the start.

First we calibrated Evan's Canon DSLR using RAD targets that the software allows us to print. Using this calibration we then built a 3D model using points selected and matched by hand from pictures of the dish Evan had taken two weeks ago. The focal length might have been different between the dish photos and calibration, so we will update this on the next pass. The dish photos and Photomodeler interface is shown in Figure 1.

### Figure 1 - Photomodeler interface

![screenshot 1](https://cloud.githubusercontent.com/assets/6098508/19789474/e35ee602-9c7d-11e6-8773-9e9145be51fa.png)

Photomodeler allows for matching of points by hand. It also allows selection of points by hand, but we used the "sub pixel" functionality, which is pretty awesome in that it recognizes "high contrast circles" (like the shapes Evan cut out of reflective tape) and does a weighted centroid to find the center. This apparently gives much higher accuracy.The circles can be stuck on non-planar surfaces and the software figures it out. Many of the rows of reflective tape shapes are not circles, so a few hexagons are approximated as circles. We will fix this on the next pass.

We used only two photos and 11 points. 6 points is the minimum to solve the 3D model, so I assume with more photos and points we will continue to do way better. After solving for the 3D model, it gives a residual for each point in each photo of actual (x,y) pixel location minus predicted location given the best fit model. The max residual is 0.25 pixels at one of the back row points, which translates to 0.3 mm. Without more photos this might not be a fair test, but we are just trying to see if this works.

There is also a very nifty scaling and rotation function that orients the object along the axes of your choosing and puts it in physical units. We output these points to a text file, import to python, and fit to a 3D parabola as in the [previous posting](https://github.com/bmxdemo/bmxproject/issues/9#issuecomment-256148036).

Figure 2 shows the best fit parabola. Figure 3 shows the residuals. Compared to Figure 3 of the previous posting, we see that the residuals have come down from the totally unbelievable +/- 20 mm with Photoscan to +/- 2 mm with Photomodeler. Figure 1 of my previous posting, which shows residuals from fitting a 2D parabola to height of the dish surface measured directly with a ruler and plumb bob, has similar sized residuals. These data even show a sag between the uprights. Given the estimated 0.3 mm accuracy that Photomodeler reports, it's totally possible that the residuals we're now getting represent real surface error rather than measurement error. 

### Figure 2 - data points and best fit parabola

![fig1](https://cloud.githubusercontent.com/assets/6098508/19789623/2d29da2a-9c7f-11e6-9d41-0a2b7f478325.png)

### Figure 3 - residuals

![fig2](https://cloud.githubusercontent.com/assets/6098508/19789625/3335e1b6-9c7f-11e6-851d-a40bfa69b96b.png)

Next is for Evan to improve upon these measurements by adding more photos and points. If the residuals stay the same then we will probably have confidence they are real.

End of story is that Photomodeler is awesome, way less of a black box, accurate, and easy to use. It should be straightforward to do this in the field, including relative orientations of all dishes, feed horns, the tower etc. It is $1,100 well spent.

# 18 December 2016: PhotoModeler Precision (Residuals from fitting a scale factor)

In order to test how precisely PhotoModeler can generate a point cloud from a set of photos, we decided to cross-reference two sets of three photos point-by-point.  Each point is created by hand in the software using the sub-pixel function.  Each array of exported (x,y,z) points are of equal length and correspond to the same physical locations on the proto-petal.  These two data sets that are exported by the software differ by some position-dependent scaling factor, so Chris and I have written a python script that accounts for this via optimization.   Figure 1 shows a plot of the chi squared residuals sqrt[(x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2] versus the "x-axis", where x1, y1, z1 refer to the first data array and x2, y2, z2 refer to the second data array.  

### Figure 1: PhotoModeler residuals from fitting a scale factor
![resid_scale](https://cloud.githubusercontent.com/assets/17692591/21291978/d9c5f646-c4c1-11e6-9716-2d37cbe1c691.png)

Now, while the x, y, and z axes are arbitrary, it is important to note that each data set nominally share the same axes.  I am currently writing a script that accounts for any rotation between the two arrays, however I am finding that this rotation is very small.  The residuals we get from fitting a scale factor, then, are an upper bound on the repeatability of this procedure.
