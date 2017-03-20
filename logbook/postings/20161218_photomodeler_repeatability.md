## 18 December 2016: PhotoModeler Precision (Residuals from fitting a scale factor)

In order to test how precisely PhotoModeler can generate a point cloud from a set of photos, we decided to cross-reference two sets of three photos point-by-point.  Each point is created by hand in the software using the sub-pixel function.  Each array of exported (x,y,z) points are of equal length and correspond to the same physical locations on the proto-petal.  These two data sets that are exported by the software differ by some position-dependent scaling factor, so Chris and I have written a python script that accounts for this via optimization.   Figure 1 shows a plot of the chi squared residuals sqrt[(x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2] versus the "x-axis", where x1, y1, z1 refer to the first data array and x2, y2, z2 refer to the second data array.  

### Figure 1: PhotoModeler residuals from fitting a scale factor
![resid_scale](https://cloud.githubusercontent.com/assets/17692591/21291978/d9c5f646-c4c1-11e6-9716-2d37cbe1c691.png)

Now, while the x, y, and z axes are arbitrary, it is important to note that each data set nominally share the same axes.  I am currently writing a script that accounts for any rotation between the two arrays, however I am finding that this rotation is very small.  The residuals we get from fitting a scale factor, then, are an upper bound on the repeatability of this procedure.
