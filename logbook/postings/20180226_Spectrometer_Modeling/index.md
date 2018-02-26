## February 26, 2018 - Modeling the Spectrometer Output


### An attempt at modeling our spectrometer output in Octave/Matlab

Outline of code:
1. Read in the S21 data for Lorch filters (labeled AU1 and AU2)
2. Model mission sources:
  -The sky
  -RFI background
  -6 TV stations + harmonics
  -Cygnus A
  -Thermal noise (amp chain)
3. Model OMT output signal
4. Model input filter output signal
5. Model amp chain output signal
6. Model output filter output signal
7. Model aliasing
8. Results (simulated spectrometer output) for various test cases, compare with data browser data


    -The sky: constant @ 9K.[16Jy]
  -RFI background: consant at 100Jy
  -6 TV stations + harmonics: gaussians at 524.328MHz


### 1. Read in the S21 data for Lorch filters (labeled AU1 and AU2)

**Lorch filter "AU1" passband (dB):**
<img src="AU1Passband_dB.png" width="800" height="200">

**Lorch filter "AU1" passband (linear):**
<img src="AU1Passband_Linear.png" width="800" height="200">

**Lorch filter "AU2" passband (dB):**
<img src="AU2Passband_dB.png" width="800" height="200">

**Lorch filter "AU2" passband (linear):**
<img src="AU2Passband_Linear.png" width="800" height="200">


### 2. Model emission sources
