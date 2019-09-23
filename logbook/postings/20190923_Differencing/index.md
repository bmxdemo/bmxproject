## Measuring the radiometer equation with sample differencing

Anze Slosar, Sep 23, 2019

### Basic idea

We do the following:
 * take data without noise diode
 * Select chunks that are clean
 * take neighbouring samples in time and calculate the difference in power divided by the sum in power
 * this should be a random gaussian variate with variance given by the radiometer equation (proprtional to number of samples getting into the data)
 * compare this to theoretical predictions

We use the following data (chosen to avoid sats)
 * 21cm chunk 1AM
 * 21cm chunk 3AM
 * full spectra 1AM
 * full spectra 3AM

The digitizer card on DAQ1 was in a "funny state" (known issue with excess power on small scales) -- seems to affect both channels

Note that this test doesn't really test the noise temperature, but it tests is radiometer equation works on the time-scale of a single sample. If so, then we don't loose information by averaging.

Python Notebook in `bmxhacsk/ipynb/difftest.ipynb`.

#### Figure 1: waterfall plots

![Fig](Sep23B_1.png)
![Fig](Sep23D_1.png)
![Fig](Sep23A_1.png)
![Fig](Sep23C_1.png)


#### Figure 2: waterfall plots average in time direction

![Fig](Sep23B_2.png)
![Fig](Sep23D_2.png)
![Fig](Sep23A_2.png)
![Fig](Sep23C_2.png)

#### Figure 3: waterfall plots average in frequency direction

![Fig](Sep23B_3.png)
![Fig](Sep23D_3.png)
![Fig](Sep23A_3.png)
![Fig](Sep23C_3.png)


#### Figure 4: diff waterfall plots

![Fig](Sep23B_4.png)
![Fig](Sep23D_4.png)
![Fig](Sep23A_4.png)
![Fig](Sep23C_4.png)


#### Figure 5: diff plots averaged in time direction

![Fig](Sep23B_5.png)
![Fig](Sep23D_5.png)
![Fig](Sep23A_5.png)
![Fig](Sep23C_5.png)

#### Figure 6: diff plots averaged in frequency direction

![Fig](Sep23B_6.png)
![Fig](Sep23D_6.png)
![Fig](Sep23A_6.png)
![Fig](Sep23C_6.png)


#### Figure 7: Final plots - effective number of samples vs expectation

![Fig](Sep23B_7.png)
![Fig](Sep23D_7.png)
![Fig](Sep23A_7.png)
![Fig](Sep23C_7.png)


