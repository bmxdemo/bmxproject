## February 26, 2018 - Modeling the Spectrometer Output


### An attempt at modeling our spectrometer output in Octave (Matlab)

Outline of code:
1. Read in the S21 data for Lorch filters (labeled AU1 and AU2)
2. Model emission sources:
   * Sky 
   * RFI background
   * TV stations + harmonics
   * Cygnus A
   * Thermal noise (amp chain)

3. Model OMT output signal
4. Model input filter output signal
5. Model amp chain output signal
6. Model output filter output signal
7. Model aliasing
8. Results (simulated spectrometer output) for a few test cases
9. Conclusion

### 1. Read in the S21 data for Lorch filters from VNA

The [VNA scan](postings/20170327_LorchFilterMeasurements/index.md) was taken from 20kHz to 4.8GHz (20 - 4800000kHz)). These scans are taken as the bandpass function further down the model. The dataset contains 10008 points. A 10008 element vector ranging from 20 to 4800000 provides a frequency axis.

**Lorch filter "AU1" passband (dB):**
<img src="AU1Passband_dB.png" width="800" height="200">

**Lorch filter "AU1" passband (linear):**
<img src="AU1Passband_Linear.png" width="800" height="200">

**Lorch filter "AU2" passband (dB):**
<img src="AU2Passband_dB.png" width="800" height="200">

**Lorch filter "AU2" passband (linear):**
<img src="AU2Passband_Linear.png" width="800" height="200">


### 2. Model emission sources

#### Cygnus A

Referring to this spectrum: http://www.cv.nrao.edu/course/astr534/images/CygAspectrum.gif 

Considering the Lorch passband starts at 1GHz I approximate the emission with a line. It goes from 2200Jy [= 2.2e-13mW] at 1GHz to 470Jy [= 4.7e-14mW] at 4GHz. With the frequency axis in KHz I have 1730Jy/3000000KHz = -.000577Jy/KHz. Y intercept is 2777Jy [= 2.77e-13mW], so the crude "synchrotron" line looks like:

**Cygnus A emission model (Jy):**
<img src="CygAEmissionModel.png" width="800" height="200">

#### Sky

Set constant over frequency @ 9K.[16Jy] (assumed lambda=21cm and .5deg beamwidth using https://science.nrao.edu/facilities/vla/proposing/TBconv.)

#### RFI Background hum

Set consant at 100Jy (guess, starting point)

#### TV Stations

6 TV stations + harmonics were modeled as 7MHz FWHM gaussians. From POC the stations are:

   * 524.328MHz: -61dbm [= 7.94e16 Jy]
   * 615.99MHz: -83dbm [= 5.012e14 Jy]
   * 671.67MHz: -75dbm [= 3.2e15 Jy]
   * 770.01MHz: -81dbm [= 7.943e14 Jy]
   * 867.73MHz: -85dbm [= 3.162e14 Jy]
   * 1.00GHz: -83dbm [= 5.012e14 Jy]

Wasn't sure how to model the intensity of the harmonics. I started with a 1/n^x relation and by experimentation came to I/n^50, where I is the intensity of the fundamental and n is the harmonic number. It seems a reasonable starting point but one TV station in the final output is definitely too bright. 4 harmonics are modeled for each station.

**TV stations (only the fundamentals are visible at this scaling):**
<img src="TVStations_Jy.png" width="800" height="200">

#### Thermal noise within amplifier chain

This is modeled as a vector of white noise averaged over 100 iterations where length = frequency vector length (10008 elements) from 20KHz to 4.8GHz. The 0-1 random numbers are scaled to 20 Jy (wild guess, starting point).

### 3. Model output from OMT by summing the modeled emission for Cygnus A, the sky, the RFI background, and the TV stations

### 4. Model output from input filter by multiplying the above by the input filter passband 

### 5. Model the output from the amplifier chain by add thermal noise to the above (no intermod yet)

### 6. Model the output from the output filter by multiplying the above by the output filter passband

### 7. Model the spectrometer output by divde the complete dataset into component Nyquist zones and summing:

**Nyq. 1 = 0-550MHz:**
<img src="NoSource_Nyq1.png" width="800" height="200">

**Nyq. 2 = 551-1100MHz:**
<img src="NoSource_Nyq2.png" width="800" height="200">

**Nyq. 3 = 1101-1650MHz:**
<img src="NoSource_Nyq3.png" width="800" height="200">

**Nyq. 4 = 1651-2200MHz:**
<img src="NoSource_Nyq4.png" width="800" height="200">

**Nyq. 5 = 2201-2750MHz:**
<img src="NoSource_Nyq5.png" width="800" height="200">

**Nyq. 6 = 2751-3300MHz:**
<img src="NoSource_Nyq6.png" width="800" height="200">

**Nyq. 7 = 3301-3850MHz:**
<img src="NoSource_Nyq7.png" width="800" height="200">

**Nyq. 8 = 3851-4400MHz:**
<img src="NoSource_Nyq8.png" width="800" height="200">


### 8. Sum of Nyquist zones (simulated spectrometer output) for different test cases

**Simulated spectrometer output: WITH Cygnus A, input filter=Lorch AU1, output filter = Lorch AU2**
<img src="SpectOut_CygA.png" width="800" height="200">

**Simulated spectrometer output: NO Cygnus A, input filter = Lorch AU1, output filter = Lorch AU2**
<img src="SpectOut_NoSource.png" width="800" height="200">

**Simulated spectrometer output: NO Cygnus A, input AND output filter = Lorch AU1**
<img src="SpectOut_NoSource_2xAU1.png" width="800" height="200">

**Simulated spectrometer output: NO Cygnus A, input AND output filter = Lorch AU2**
<img src="SpectOut_NoSource_2xAU2.png" width="800" height="200">

**Simulated spectrometer output: NO Cygnus A, input filter = Lorch AU1, output filter = Lorch AU2, Nyquist zones 6 and 7 suppressed**
<img src="SpectOut_NoSource.png" width="800" height="200">

### 9. Conclusion

What does this suggest about the spectrometer output we're seeing?
   * The wavy character of the spectrum is a direct result of the filter passband shape (as measured in this [previous posting](postings/20170327_LorchFilterMeasurements/index.md))
   * There should be noticeable variation in this structure from one Lorch filter to the other
   * Some minor features of the spectrum are being aliased from the the Lorch filters' ~4GHz passband
   * Clearly the strange frequency binning of a source passing is not reproduced.
   * If intermodulation is at play the wavy passband is likely complicating it.

**Comparison to raw spectrum from 2/25/18 at 0800 with notes**
<img src="TestCaseComparison.png" width="800" height="600">

Possible additional work:
  * Improve the interaction in the amp chain (section 5) by simulating intermodulation 
  * Replace guesswork w.r.t. source intensities (RFI background, thermal noise), and replace linear approximation of synchrotron emission with actual synchrotron function (Bessel functions were too much work for this pass)
