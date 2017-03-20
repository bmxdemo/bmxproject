## Oct 25, 2016: Michigan visit summary (CDS)

From Jeff's email with my notes interspersed:
- Chris and I figured out how to install coax lines into the OMT
- Chris tested the OMT revealing performance that is inline with what is predicted for S11 and S21
  - we realized that the reflection can be as high as 10% in power for one OMT
  - this means that with two OMTs connected together we can get standing waves that are 2\* sqrt(.1)  = 0.6 i the E-filed, or about 40% in power, we saw this
  - simulations revealed that this is to be expected
  - Chris measured S11 and s21 and summed these in power
  - if there were no loss these would add to 100%
  - we see evidence for a dielectric loss in each OMT at the 5% level, with a systematic error bar that is at least a few percent
    *Chris looked up the specs on the coax we used ([Micro Coax UT-085C-AL-TP-LL](http://www.micro-coax.com/products/product-details/?type=alumiline&part_id=75)), we predict ~3-5%  loss from this coax
  - All OMT’s behave the same, so we can repeatably assemble the OMTs
  - we noted that the vertical spacing between X- and Y- probes was larger than it needs to be and can be reduced in future versions

Jeff ran these sims in HFSS with the OMT open and the top and with two OMTs shorted together:
[QR_OTM_debug.pdf](https://github.com/bmxdemo/bmxproject/files/551245/QR_OTM_debug.pdf)

I then put the OMTs on the VNA (fully calibrated) and meaured the S parameters. This is what I get compared to Jeff's sims:
### Figure 1

![figure_1](https://cloud.githubusercontent.com/assets/6098508/19696255/5de577f4-9ab4-11e6-825f-5b419d630bea.png)
### Figure 2

![figure_2](https://cloud.githubusercontent.com/assets/6098508/19696417/03152f76-9ab5-11e6-964c-0fa3c0277292.png)
### Figure 3

![figure_3](https://cloud.githubusercontent.com/assets/6098508/19696420/07284422-9ab5-11e6-9a4b-ffe785ab31e6.png)

Figure 3 implies significant loss, but S11+S22>1 also implies a large measurement systematic. Given this measurement systematic, it's not clear to me how much improvement we'll see if using a lower loss coax. The measurement of S11+s11 with S11 and S22 calibrated separately looked much cleaner and more sensible, showing ~0.5 dB loss.. I'm not sure what to make of that.

These drawings are supposed to reflect the OMT in the state it was when we measured it.
[omt.pdf](https://github.com/bmxdemo/bmxproject/files/551301/omt.pdf)

