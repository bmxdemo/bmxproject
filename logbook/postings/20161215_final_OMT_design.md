## Dec 15, 2016 - Final new modified VLA + transition design

Following the [previous posting](20161215_VLA_OMT_sims.md), I detail the modifications made to the VLA OMT + transition design to make it work for BMX. The solidmodel can be found here:
Full OMT model, including assemblies: [directory](http://www.cosmo.bnl.gov/www/bmx/drawings/OMT_20161215), [zip](http://www.cosmo.bnl.gov/www/bmx/drawings/OMT_20161215.zip)
Only parts (to give to the shop): [directory](http://www.cosmo.bnl.gov/www/bmx/drawings/OMT_for_mfg_20161215/),  [zip](http://www.cosmo.bnl.gov/www/bmx/drawings/OMT_for_mfg_20161215.zip)

The overall weight is 32 lb. The modifications are:

- scale all dimensions up by factor 1.43 to make work at lower frequency
- change ridge thickness from 0.5"x1.43 = 0.715" to 0.75" for manufacturing ease
- increase ridge face length to 0.26" to accommodate 0.25" OD coax
- eliminate complicated blocks and absorber in favor of a single backshort, reduce coax spacing to 0.2" (center conductor is 0.08" OD).
- tune ridge spacing to maximize S21 - found 0.375" is optimal

The OMT and transitions ridges will be manufactured as once piece. Figure 1 shows the solidworks model of the assembly, cross sectioned to just show the OMT. I have also designed a simple clamp to hold the coax in place, as we found it could pull out easily as designed. (Only one clamp is shown, though there will be one for each polarization). Figure 2 shows the full design. Figure 3 is an alternate view of the full design without the upper outer walls, for visibility. Figure 4 is a cross section of the full design.

### Figure 1 - cross section showing OMT only
![fig3](https://cloud.githubusercontent.com/assets/6098508/21240669/4d2ceaac-c2da-11e6-80b4-3a43e5b97847.PNG)

### Figure 2 - OMT + transition
![fig6](https://cloud.githubusercontent.com/assets/6098508/21240709/7b903d54-c2da-11e6-8d3b-f463a09b3877.PNG)

### Figure 2 - OMT + transition (walls hidden)
![fig4](https://cloud.githubusercontent.com/assets/6098508/21240802/dfee0f92-c2da-11e6-879d-ccf1c2f2a5a5.PNG)

### Figure 4 - OMT + transition cross section
![fig7](https://cloud.githubusercontent.com/assets/6098508/21240735/9287abdc-c2da-11e6-8263-fbf11d05270e.PNG)

Next, I exported the solidworks model to HFSS to make sure there were no transcription errors. Figure 5 shows S21. Figure 6 shows the predicted loss, including UT-250C-ULL coax and the aluminum ridges (but not the aluminum side walls or backshort). It also includes a 1/4" radius fillet on the inside corners of the ridge face to approximate how it will actually be machined. This makes no difference and is not included in the drawings.

### Figure 5 - S21 (dB)
![omt_final_s21](https://cloud.githubusercontent.com/assets/6098508/21241304/0a47b5b6-c2dd-11e6-9c7b-eb40b319ddbe.png)

### Figure 6 - loss (dB)
![omt_final_loss](https://cloud.githubusercontent.com/assets/6098508/21241329/182ed3ee-c2dd-11e6-9c15-330e42e1e3a8.png)

The difference in S21 between x and y polarizations could be reduced by reducing the center conductor spacing. It is at 0.2" now. The center conductor spacing is 0.0808" so I could probably reduce this to 0.1", but that would risk a short. 0.15" would probably be safe. However, I am pretty satisfied as it is.

Lastly, following the VLA paper, I ran a sweep of the ridge spacing and far ridge coax penetration length to assess the sensitivity to manufacturing tolerances. Figure 7 shows the ridge spacing sweep. Figure 8 shows the coax penetration sweep. Each line is a different frequency.

### Figure 7 - S11, ridge spacing sweep
![omt_transition_final_noblocks_ridgespacing_sweep](https://cloud.githubusercontent.com/assets/6098508/21241482/d1111d5e-c2dd-11e6-9f6d-accaa53adf90.png)

### Figure 8 - S11, coax penetration sweep
![omt_transition_final_noblocks_coaxpenetration_sweep](https://cloud.githubusercontent.com/assets/6098508/21241501/e55de882-c2dd-11e6-8422-653fade2d073.png)

The nominal ridge spacing is 0.375". S11 stays below -15 dB within +/- 0.01" of this target, which is quite doable. (The two lines that exceed -15 dB below 0.375" are for 1.5 GHz and 0.7 GHz which are out of band and the extreme low end of the band, respectively.)

The nominal coax penetration is 1.62" as measured from the inner face of the ridge. Judging from Figure 8, there is a +/- 0.07 tolerance on this to keep S11 < -15 dB. This is small, but again, probably realizable. However, I do see this is a possible source of non-repeatability if we're not careful.

