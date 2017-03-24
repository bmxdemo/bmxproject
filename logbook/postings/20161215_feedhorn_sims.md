## Dec 15, 2016: Pyramidal feedhorn design and simulations

Starting from the OMT + transition design from [this posting](https://github.com/bmxdemo/bmxproject/issues/10#issuecomment-267434363), I simply tacked on a square pyramidal horn to the HFSS model. The dimension at the back is the dimension of the transition aperture, and the dimension at the entrance aperture is 46.5". The flare angle is 30 degrees (15 degree half angle), making the overall height of the horn 69.4". 

(We chose this aperture size so that lambda/D (i.e. approx. the far field beam FWHM) at the 700 MHz would be 1/3 of the angle subtended by the dish as viewed from the center of the horn. You can see that here:

[tower_assem_hornmockup.PDF](https://github.com/bmxdemo/bmxproject/files/656097/tower_assem_hornmockup.PDF)

The horn does not intersect the dish footprint as viewed from above, and the half angle from the edge of the horn to the edge of the dish is ~25 deg.)

Figure 1 is a great animated gif of the propagating E-field in a cross section of the y-coax plane. Figure 2 is a zoom of Figure 1. In all plots in this posting, the E-fields and beams are shown at 1 GHz.

### Figure 1 - E-field of OMT + pyramidal horn 
![horngif](https://cloud.githubusercontent.com/assets/6098508/21246305/dda6ade6-c2f5-11e6-9516-c8e3586f23f1.gif)

### Figure 2 - E-field of OMT + pyramidal horn  (zoom)
![horngif2](https://cloud.githubusercontent.com/assets/6098508/21246327/f4a64498-c2f5-11e6-975a-a57d4df5bf78.gif)

Figures 3 and 4 are the same as Figures 1 and 2 except in a cross sectional plane plane rotated 45 degrees. This is just meant to illustrate that the E-field strength is concentrated in the center of the OMT. (This is by definition true in Figures 1 and 2 because the E-field must be zero in the aluminum ridges.)

### Figure 3 - E-field in 45 deg rotated plane
![horngif_45deg](https://cloud.githubusercontent.com/assets/6098508/21246362/3c02c712-c2f6-11e6-9a08-89e6f4ea0e9f.gif)

### Figure 4 - E-field in 45 deg rotated plane (zoom) 
![horngif2_45deg](https://cloud.githubusercontent.com/assets/6098508/21246365/4763fb80-c2f6-11e6-9403-481d83372231.gif)

Figures 5 and 6 show the far field co-polar beam (i.e. gain, i.e. E field squared) as a function of latitudinal polar angle for an excitation at the x and y coax ports, respectively. In each plot, the two lines marked phi=0 and phi=90 are the x and y cuts through the 2D beam. Also shown on the plot are the cross polar beams, which are very small.

### Figure 5 - x coax beam
![omt_final_beam_xcoax](https://cloud.githubusercontent.com/assets/6098508/21246510/40e2963a-c2f7-11e6-97cf-cd5c4108b1c5.png)

### Figure 6 - y coax beam
![omt_final_beam_ycoax](https://cloud.githubusercontent.com/assets/6098508/21246513/4ad202e8-c2f7-11e6-9664-1970fb9574a5.png)

The FWHM is ~14 deg at 1 GHz. At 700 MHz, this would be 20 deg, which meets our spec of 1/3 the angle subtended by the dish (~65 deg.)

We can also see a ~4 deg difference between beam FWHM in the x and y directions, a ~30% beam ellipticity. Beam ellipticity is expected for a single polarization of a square horn, though I do not know how much. (I do know it is a function of flare angle. I simulated a larger flare angle to reduce the overall height and saw the ellipticity get worse.)

Lastly, the far field beam is ~20 dB at 32 deg half angle, i.e. "the edge taper is -20 dB." This will hopefully give us good sidelobe suppression. 

This is all for the far field however. In fact, the Fraunhofer distance is 2D^2/lambda = 9.3 m at 1 GHz. The near edge of the dish is 2.8 m from the horn center, and so is in the near-to-mid field. I therefore ran a near field setup in HFSS. In HFSS, you can evaluate the electric field on line segments at any distance from a radiating boundary, so I inserted a line whose endpoints corresponded to the dish endpoints. Obviously, the center of the line is closer to the dish than the parabola constrained by the same endpoints, but the difference is not large, and I just want to quickly get the edge taper anyways, which will be the same. Figure 7 shows the setup.

### Figure 7 - HFSS near field setup
![omt_final_nf_model](https://cloud.githubusercontent.com/assets/6098508/21247007/55f0bfc2-c2fa-11e6-8dac-0753c67b0680.png)

Figure 8 shows the total E-field squared in dB as a function of normalized distance along the line.
Whereas in the far field the edge taper is -20 dB, in the near field the edge taper is ~ -10 dB. I checked that I am plotting E^2 and not E. I also checked that the near-field solution converges to approximately the far field solution by drawing a line at 20x the far field distance that subtended 60 degrees and 80 degrees, and comparing to the far field solution at the end points. For instance, at 80 degrees, both the far field and near fields setups give  ~-35 dB. It's still possible I'm messing something up here and I'd like to check with Jeff that this is all kosher, but I think it probably is.

### Figure 8 - Near field E-field^2 along straight line dish approximation
![omt_final_nf_e2](https://cloud.githubusercontent.com/assets/6098508/21247222/d1cb6d12-c2fb-11e6-9316-01a0a0d7bed8.png)

If this edge taper is fine, then someone can design the horn (just 4 pieces of metal) and how to mate it to the OMT. The OMT drawings are [here](http://www.cosmo.bnl.gov/www/bmx/drawings/OMT_20161215/). The assembly drawing OMT_assem.pdf details the mounting surfaces that are available.
