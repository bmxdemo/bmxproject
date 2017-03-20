Over the summer, myself, Paul Stankus, and Erin Sheldon pursued the method of photogrammetry for characterizing the dish surface after Paul O'Connor pointed us in the right direction.  The slides I gave for the June telecon describe the method in more detail.

[Photogrammetry.pdf](https://github.com/bmxdemo/bmxproject/files/452569/Photogrammetry.pdf)

I managed to use PhotoScan and Rhino 3D to create a 3D model of the dish, and then get a list of points on its surface.  The .txt file with the spatial (x, y, z) points of the surface is attached below.  The file is simply a three column list with no added features.  The method I used was to extract the surface of the petal in Rhino (after having created the 3D model in PhotoScan).  Basically, I explode the 3D model into various surfaces and then join together the pieces of interest -- i.e. the pieces that make up the dish surface.  This mesh is then converted into physical points (I believe the points correspond to intersections of the vectors that make up the mesh).  Each physical point is assigned a coordinate based on the axes I created around the dish surface and then exported as such.

A few things: these points are randomly chosen based on the mesh, so it is not all too clear to me what level of precision we are to expect here, or how accurately they represent the true dish surface.  There are roughly 80,000 points.  The next step is to analyze this data.

[BMX_petal_surface_Rhino.txt](https://github.com/bmxdemo/bmxproject/files/452492/BMX_petal_surface_Rhino.txt)
