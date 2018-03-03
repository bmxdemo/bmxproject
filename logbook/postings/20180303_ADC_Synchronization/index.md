## ADC Synchronization
Hindy Drillick
March 2, 2018


Palantir2 can currently handle data acquisition for four channels, using two digitizer cards. 
We want to measure the delay in the signal between the two cards, as the cards might not start at the exact same time. 
To test this, I sent the same pulse modulated signal to both cards. I then checked the raw digitizer output and
compared the positions of the pulse edges for both cards.

### Test 1 - Buffer size: 2^27 samples (122 ms)
The buffer size here refers to the number of samples per FFT. The data is received from the digitizer in chunks of that size.
To perform the the synchronization test, DAQ is run for 10 of these chunks - 1.22 s, and the raw digitizer data is dunped to a file (before
taking its FFT or doing any kind of data reduction). The signal was sent to the second channel on each card. 

Signal information:\
Frequency: 1 MHz \
Amplitude: 0 dBm\
Pulse modulated with period of 500 ms and duty factor of 1

I then locate the positions of the rising edges for both cards and subtract to get the delay. I ran DAQ in this way 1000 times, and plotted the results.

Histogram of delays between the cards: 
![Image](https://github.com/bmxdemo/bmxproject/blob/master/logbook/postings/20180303_ADC_Synchronization/Hist_Delays_122_ms.png)

mean: -7.64221984374 ms\
std: 7.37008751626\
min: -27.001950909 ms\
max: 19.894790909 ms

To check that I am actually detecting the beginning edge of each pulse, I also plotted the time delay between subsequent pulses for each card. 

