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

