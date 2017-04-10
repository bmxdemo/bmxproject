## April 7, 2017: Beam from aperture plane FFT
Christopher D. Sheehy
<hr>

### 1 - Introduction

In [a previous posting](../20170323_beam_sims/index.md), I showed beams at 1 GHz
simulated using HFSS. In Fig 8, I showed the beam for the "compact" pyramidal
feed horn coupled to the dish. I also showed the surface current, J, induced on
the dish. The far field beam and the electric field in the aperture plane are
Fourier transforms of each other. Thinking in terms of the aperture illumination
is sometimes useful in interferometry. In this posting, I try to compute the far
field beam using the surface current output by HFSS and show that it equals the
far field beam output by HFSS.

Furthermore, this was a very useful exercise for figuring out how full sky
beam polarization conventions work.

<hr>

### 2 - Method

The procedure follows [Rahmat-Samii,
1984](http://ieeexplore.ieee.org/document/7768593/), [pdf](rds2368.pdf). 

1. In HFSS, excite one OMT coax polarization.
2. Save the resulting complex surface current vector, **J**, defined on the dish
  surface 
3. Bin J in x,y pixels, which effectively projects it onto the xy plane
4. Manipulate J to get the far field beam

For step 4, we can do various things:
1. Compute |FFT(J)|^2 to get the far field beam
2. Apply Equation 11, which multiplies J by the "surface projection Jacobian" of
  the parabola and FFTs to account for surface curvature. This is written down as an expansion
  about small theta, so including higher order terms approximates the beam
  better. All terms are FFTs of J with different complex prefactors and so are fast to compute.
3. Directly compute the surface integral in Eq. 4, which should not be an
  approximation. 	   

A few things to keep in mind:

- FFTing the surface current does not account for obscuration caused by the
  horn. The dish is off axis, so the effect should not be large, but surely some
  rays are scattered at large angles. (I ran a test with a perfect parabola and
  a downward facing horn, and putting in the effect of the central obscuration
  by zeroing J at r<r_horn made a huge difference.)
- I approximated the surface as a parabola for computing the surface projection Jacobian
  and complex prefactors. This I can improve, and it might make small
  differences. 

<hr>

### 3 - Results

**Figure 1** shows the HFSS setup.

<center><i>Figure 1 - HFSS setup</i></center>


![](Screenshot.png)


**Figure 2** shows the projected surface current in the left panels and the
  resulting beams in the right panel. The top row shows a uniformly illuminated
  circular aperture with no curvature. In rows 2-5, J does not change but I am
  sometimes plotting |J| and sometimes plotting Re[J] to reflect how the beam
  calculation is done. Row 2 shows the straight FFT of |J|. Rows 3-5 use the
  equations in the linked paper which include complex phase factors multipliying J, and therefore
  need complex J in the FFT. Row 3 shows the first FFT term of the beam approximation. Row 4 is
  the sum over the first 100 FFT terms, which breaks down as theta->90 deg. Row 5 shows the full numerical
  integration of the surface current.

The max polar angle theta of the FFTed beams is set by the sampling of the x/y plane. In binning J to produce
the left hand column I can choose the bin size, but if I choose too small a bin size I get holes. 
Since HFSS chooses the native sampling of the surface, I don't think there's much I can do to increase the resolution. 
The surface integral beam has no such limitation.

An important note: in the right hand column Figure 2 I added the contribution from direct horn/sky coupling by running
HFSS with the horn but no dish and adding the horn and dish beams as (sqrt(B_horn) +
sqrt(B_dish))^2. The beams plotted are the "Ludwig third definition" co-polar beam,
which I compute from the x, y, and z components of the radiated E-field. Basically, I have complex Jx, Jy
and Jz, and from these can compute the far field Ex, Ey, and Ez. (In the left column, I'm only
showing Jx.) Ex and Ey are the co and cross
polar E-field near theta=0, but at large theta this is no longer true. For instance, Ez is zero
at theta=0, but at (theta, phi) = (90,0), Ez is a maximum and Ex is zero. To get
around this, one then projects Ex, Ey, and Ez onto the theta/phi spherical coordinate unit vectors. 
This basis has the advantage of being 2D, which far-field polarization inherently is, but 
has the drawback that E_theta and E_phi are not aligned
with the dominant polarization axes at theta=0. Therefore, we use this Ludwig definition thing 
(Eq. 14-15), wherein E_ludwig_x and E_ludwig_y
are 2D, orthogonal at all points on the sky, and equal to Ex and Ey at small theta. 
This seems to be used as the commonly accepted definition of co and cross polar
beams. HFSS outputs these beams directly (L3X/L3Y).


<center><i>Figure 2 - projected surface current and resulting far field beam</i></center>

![](beam_fig1.png)

**Figure 3** shows the azimuthal average of the top right panel of Fig 3
  compared to the Airy function, the theoretical expectation. The fact they
  agree means I'm getting the FFT frequency axis and power units correct. Side
  note: I assume that Jy=Jz=0 for the circular aperture, and I need to plot Bx
  instead of B_co-pol to match the Airy function. 

<center><i>Figure 3 - circular aperture check</i></center>

![](beam_fig3.png)


**Figure 4** shows the 2D gridded co-pol (L3X) beam from HFSS, which I'm regarding at
  "truth." HFSS outputs on the sphere, so despite the projection distortions, the beam as a function of (theta,phi) is correct. The full beam goes all
  the way out to theta=180, but I'm stopping it before that for plotting purposes.

<center><i>Figure 4 - HFSS beam</i></center>

![](beam_fig2.png)



Lastly, **Figure 5** shows x and y cross sectional slices (phi=0 and 90 deg) through all
the beams. The thick blue line is the HFSS "true" beam. The simple FFT is the
dotted blue line, and isn't terrible, but doesn't get the main beam shape quite
right. Doing the FFT but accounting for curvature using the first term of the
Rahmat approximation is shown as the dashed cyan line. This captures the main
beam asymmetry. Including 100 terms in the approximation gets us to dashed black
line, which is exactly the same as the full surface integral beam, shown as the solid red line,
up to theta = 75 deg. Neither of these is a big improvement over just the first term. Nonetheless,
I'm pretty happy that this seems to be working.

The dashed red line is the same as the solid red line but does not include the effect of
direct horn/sky or horn/ground coupling, the common name for which is spillover. You can see this makes a pretty big
difference outside the main beam, especially at phi=0, theta=-50, where it's clear that sipllover dominates 
over the reflected power. This is also evident in Fig 4 as the large -25 dB lobe
at the left end of the plot. Since the way I included the effect of the horn was
pretty kludgy (for instance, not taking into account reflections or coherent interference
from path length differences) I expect that much of the beam structure that the
surface integral fails to account for comes from higher order effects of horn
coupling. (The HFSS beam of course includes all this.)

<center><i>Figure 5 - beam cross sections</i></center>

![](beam_fig4.png)


<hr>

### 4 - Conclusions

FFTing the surface current on the dish while accounting for curvature
reproduces the directly calculated HFSS far-field beam quite well. The exercise is partly
academic because we will likely use the directly calculated HFSS beam in any simulation pipeline
we use. However, it shows that spillover dominates reflected power from the horizon to 45 deg  
in the horn->dish direction, so interferometer fringing from sources at these angles will not be via the 
baselines established by the dish positions. We currently plan to make the flat sky approximation
and use only the main beam (down to -30 dB or so), so this will be not be a problem for now, and possibly 
forever.

Future work: compute the beam as a function of frequency in HFSS and input into
BMX pipeline; tile aperture illumination for 4 dishes and compute autocorrelation to get
automatically beam convolved uv plane coverage with realistic high ell cutoff. 



<!--

One panel

<p>
<center>
<table border="1" cellpadding="0" cellspacing="0">
<tr><td>
  <table border="0" cellpadding="5" cellspacing="0">
  <tr><th>Fig.&nbsp;1&nbsp;-</th>
      <th>Figure title</th>
  </tr>
  <tr><td>&nbsp;</td>
      <td><a href="fig_1.png"><img src="fig_1.png"></a></td>
  </tr>
  </table>
</td></tr>
</table>
</center>

Two panel

<p>
<center>
<table border="1" cellpadding="0" cellspacing="0">
<tr><td>
  <table border="0" cellpadding="5" cellspacing="0">
  <tr><th rowspan="2">Fig.&nbsp;1&nbsp;-</th>
      <th colspan="2">Figure title</th>
  </tr>
  <tr><td align="center"><b>a. </b> label a</td>
      <td align="center"><b>b. </b> label b</td>
  </tr>
  <tr><td>&nbsp;</td>
      <td><img src="fig_1.png"></td>
      <td><img src="fig_2.png"></td>
  </tr>
  </table>
</td></tr>
</table>
</center>

Three panel

<p>
<b>Fig 1 - Figure title</b>
<table border="1">
<tr><th>a - label 1
<th>b - label 2
<th>c - label 3
<tr>
<td><a href="fig_1.png"><img src="fig_1.png"></a>
<td><a href="fig_2.png"><img src="fig_2.png"></a>
<td><a href="fig_3.png"><img src="fig_3.png"></a>
</table>

-->
