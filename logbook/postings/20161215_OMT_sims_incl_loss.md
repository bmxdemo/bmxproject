## Dec 15, 2106: Including coax in HFSS model (CDS)

In Figure 2 of [this posting](https://github.com/bmxdemo/bmxproject/issues/10#issue-185180814), I showed the measured S21 compared to the simulated S21. Including the coax dialectric improves the agreement considerably. 

### Figure 1 - S21 including coax dialectric

![omt_shorted_withdialectric_s21](https://cloud.githubusercontent.com/assets/6098508/21238810/6a3340ae-c2d2-11e6-8061-1a12d882aa47.png)

I also tested whether the coax produces the expected loss by drawing a 1 ft section of Micro Coax UT-085C-AL-TP-LL in HFSS and comparing the predicted loss to what is listed in the data sheet. I had to add a new material, LDPTFE (low density), because HFSS only has standard teflon. To do this, I tuned the conductivity until the impedance was 50 ohms. I did the same for ULDPTFE because this is used for the UT-250C-ULL coax.

### Figure 2 - simulated loss in UT-085C-AL-TP-LL coax

![ut-085c-al-tp-ll_loss](https://cloud.githubusercontent.com/assets/6098508/21238968/0be346a6-c2d3-11e6-9129-2c60d5f1c6b6.png)

These are the loss/ft in dB from the data sheet:
0.5 GHz 	 .134
1.0 GHz 	 .190
5.0 GHz 	 .431
10.0 GHz  .617

The agreement is pretty good at low frequencies. Given Figs 1 and 2, I think we can be satisfied that our HFSS modeling is accurate. Given the high loss of the 0.085" diameter coax, we have decided to use the 0.25" OD UT-250C-ULL coax going forward. 

