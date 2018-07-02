## July 2nd, 2018: Photogrammetry Fitting with Fixed Axes

### Rotation Matrices Using Fixed Axes

In the [previous iterations](../20180622_Dish_With_Rotation/index.md) of rotating the photogrammetry data, we discovered that the matrices we were using were rotating with respect to a local frame of reference. This would cause a problem in which rotations about the z axis were completely arbitrary no matter the order of rotation due to the symmetry of the parent paraboloid. In order to solve this problem, we had to find a way to modify the rotation matrices so that each successive rotation would use a global frame of reference containing fixed axes. This would require the use of quaternions.

### Using Quaternions for Rotation

A normal vector contains three elements that each represent a coordinate within three dimensions. A quaternion used for rotation is a way to represent a vector by using four elements instead of three. The standard form of a quaternions follows the format of (cos(θ/2), x(sin(θ/2)), y(sin(θ/2)), z(sin(θ/2))). The three coordinates are any arbitrary vector that you wish to rotate around and θ is the angle of rotation. The best way to use this for our purposes was to convert the quaternions into a rotation matrix. The given vectors would be the x,y, and z unit vectors and the angles of rotation would be what the function would optimize. The rotation matrix using quaternions can be found in [this link](http://www.euclideanspace.com/maths/geometry/rotations/conversions/quaternionToMatrix/index.htm).

### Parameters of Different Rotation Combinations

The first thing that we had to figure out is what each angle that would be given would do to change the graph. It was found that a positive angle would result in a counterclockwise rotation about the chosen axis and a negative angle would represent a clockwise rotation, as shown in the drawing below.

![drawing](Dish_Rotation.png)

The rotations we were most interested in were around the x and z axes, which represented altitude and azimuth respectively. We also tried out different combinations of rotations to see if there was a significant difference in the final position of the parabola and to see if there would be a large amount of degeneracy in the parameters. The parameters are given below.

#### XZ Rotation

|   Data   | Focal Length | Xtrans  | Ytrans   | Ztrans  | XRot     | YRot  | ZRot      |
|:--------:|--------------|---------|----------|---------|----------|-------|-----------|
| Subset 1 | 3011 mm      | 2336 mm | -857 mm  | 75.7 mm | 0.35 deg | 0 deg | -8.42 deg |
| Subset 2 | 3016 mm      | 2348 mm | -865 mm  | 72.1 mm | 0.43 deg | 0 deg | 14.8 deg  |
| Subset 3 | 3011 mm      | 2336 mm | -857 mm  | 73.6 mm | 0.36 deg | 0 deg | -5.97 deg |

#### XY Rotation

|   Data   | Focal Length | Xtrans  | Ytrans  | Ztrans  | XRot     | YRot      | ZRot  |
|:--------:|--------------|---------|---------|---------|----------|-----------|-------|
| Subset 1 | 3013 mm      | 2016 mm | -740 mm | 86.1 mm | 1.47 deg | 3.04 deg  | 0 deg |
| Subset 2 | 3006 mm      | 2461 mm | -865 mm | 76.1 mm | 1.76 deg | -1.18 deg | 0 deg |
| Subset 3 | 3008 mm      | 2570 mm | -857 mm | 79.4 mm | 1.30 deg | -2.18 deg | 0 deg |

#### XYZ Rotation

|   Data   | Focal Length | Xtrans  | Ytrans  | Ztrans  | XRot     | YRot      | ZRot      |
|:--------:|--------------|---------|---------|---------|----------|-----------|-----------|
| Subset 1 | 3011 mm      | 2432 mm | -852 mm | 76.5 mm | 0.33 deg | -0.94 deg | -4.25 deg |
| Subset 2 | 3016 mm      | 2305 mm | -866 mm | 72.2 mm | 0.44 deg | 0.24 deg  | -6.64 deg |
| Subset 3 | 3011 mm      | 2280 mm | -870 mm | 73.9 mm | 0.59 deg | -0.17 deg | -83.8 deg |

The parameters for the xz rotation remained relatively close between each of the subsets with the exception of the second subset's z-rotation. The xy rotation produced similar results, but the xyz rotation showed a large amount of parameter degeneracy. The residuals between all sets of data for the rotations continued to remain close to the pattern that was shown in my [previous posting](../20180622_Dish_With_Rotation/index.md). 
