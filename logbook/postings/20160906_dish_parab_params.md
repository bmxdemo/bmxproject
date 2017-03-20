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
