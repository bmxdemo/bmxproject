## ADC Synchronization
Hindy Drillick\
March 2, 2018


Palantir2 can currently handle data acquisition for four channels, using two digitizer cards. 
We want to measure the delay in the signal between the two cards, as the cards might not start at the exact same time. 
To test this, I sent the same pulse modulated signal to both cards. I then checked the raw digitizer output and
compared the positions of the pulse edges for both cards.

### Test 1 - Buffer size: 2^27 samples (122 ms)
The buffer size here refers to the number of samples per FFT. The data is received from the digitizer in chunks of that size.
To perform the the synchronization test, DAQ is run for 10 of these chunks - 1.22 s, and the raw digitizer data is dumped to a file (before
taking its FFT or doing any kind of data reduction). The signal was sent to the second channel on each card. 

Signal information:\
Frequency: 1 MHz \
Amplitude: -6 dBm\
Pulse modulated with period of 500 ms and duty factor of 1

I then locate the positions of the rising edges for both cards and subtract to get the delay. I ran DAQ in this way 1000 times, and plotted the results.

Histogram of delays between the cards: 
(Although the pulse appears 2-3 times per 1.22 s trial, I only plotted one of the delays)

![Image](https://github.com/bmxdemo/bmxproject/blob/master/logbook/postings/20180303_ADC_Synchronization/Hist_delays_122_ms_0305.png)

mean: -6.20161839239 ms \
std: 6.91247066538 \
min: -24.046652728 ms\
max: 18.9160409091 

To check that I am actually detecting the beginning edge of each pulse, I also plotted the time delay between subsequent pulses for each card. 

![Image](https://github.com/bmxdemo/bmxproject/blob/master/logbook/postings/20180303_ADC_Synchronization/Hist_peak_dist_card1_127_ms_0305.png)

mean: 496.428267745 ms\
std: 49.3797379964 \
min: 11.93553 ms \
max: 511.935527273 ms

![Image](https://github.com/bmxdemo/bmxproject/blob/master/logbook/postings/20180303_ADC_Synchronization/Hist_peak_dist_card2_127_ms_0305.png)

mean: 499.994508796 ms\
std: 0.485631669499 \
min: 495.048052727 ms\
max: 511.935526364 ms

The outliers are all either 511 or 11 ms, leading me to belive there may be some bug in the way I was detecting the edges, which I will try to fix. Aside from those outliers, the other values are all within 10^-3 ms of 500 ms.

### Test 2 - Buffer size: 2^23 samples (7.62 ms)
