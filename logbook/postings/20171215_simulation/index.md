## Dec 15, 2017 - Simulation Data

The simulation data is generated with bmxsim from CRIME data. The CRIME data fields include cosmo, gfree, gsync, ptso, egfree.

Cosmo image plot:

![cosmo_img](cosmo_img.png)

All fields image plot:

![full_img](full_img.png)

To see it clearly, I plot cosmo and all field data at time 0.

Cosmo time 0 plot:

![cosmo_0](cosmo_0.png)

All fields time 0 plot:

![full_0](full_0.png)

We can see two features from the above plots:
- The value of all field data is much bigger than cosmo data.
- All field data is much smoother than cosmo data.

To get the cosmo data from all field data, I make a polynomial fit on the all field data, and subtract the polynomial curve from the all field data.

Cosmo data vs subtracted data

![cosmo_subpoly](cosmo_subpoly.png)

The two curves are almost the same except for the glitch. The glitch is also visible at the same x location in the all field plot.