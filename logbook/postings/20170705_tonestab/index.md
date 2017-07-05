### July 05 2017 - OMT tone stability (further) discussion

Chandler Conn

### Introduction

In [a previous posting](../postings/20170622_ToneStability_and_Acrylic/index.md), I examined the tone stability results from the rebuilt OMT tests. However, I neglected to consider a certain feature from the waterfall plot (figure 1 below): the transient values as the signal generator switches between the amplitude regimes. In the plot below, there are clear transient amplitudes that might be of importance.

| Figure 1| ![alt-text](../20170622_ToneStability_and_Acrylic/zoom.png)|
|:---:|:---:|


Now, however, I will be drawing my data not from the frequency slices around our input frequencies (the waterfall plot above is centered at 100 MHz and only extends +- 0.005 MHz) but from the entire spectrum (0-550 MHz). The plot of this, and its zoom, is given below:

| Full plot|Zoomed to see the 100, 300 MHz peaks (at about 450 and 2500 on x-axis)|
|:---:|:---:|
|![alt-text](../20170705_tonestab/fig2.png)|![alt-text](../20170705_tonestab/fig2_zoom.png)|

### New plots

To get the data from the transients, I split the entire dataset into 40-time chunks (one full power cycle). I then further separated these cycles into 4 groupings of 10 points, corresponding to the different aplitude regions. However, instead of keeping all 10 points, I only kept the middle 6 so as to ignore the transient values, and I placed the discarded transient values into a separate bin. Now, with five arrays spanning the entire frequency spectrum, but over ~1/4 of the time each, I averaged each frequency value over the entire time range to keep the frequency resolution but allowing me to plot a single trace. 

Below is this plot. l1-l4 correspond to the four different power regimes, but I didn't designate them "high, low, med, no" because these are not appropriate descriptors as the 100 MHz peak starts with a high amplitude while the 300 MHz peak starts with a medium one. Thus, I just kept the lists nameless as such. 

In log-scale, here is the plot of the different regions:

|Full plot|Zoom on upper tail|
|:---:|:---:|
|![alt-text](../20170705_tonestab/fig.png)|![alt-text](../20170705_tonestab/fig_tailzoom.png)|
|**Zoom between 100 MHz and 300 MHz peaks**|**Further zoom in this region**|
|![alt-text](../20170705_tonestab/fig_middle.png)|![alt-text](../20170705_tonestab/fig_highzoom.png)|


Next, I went back to absolute power (not log scale) and picked a random trace (l3 in my case) by which to divide all of the traces. The results are below, where I examine the region very close to 1:
![alt-text](../20170705_tonestab/abs1_br.png)
