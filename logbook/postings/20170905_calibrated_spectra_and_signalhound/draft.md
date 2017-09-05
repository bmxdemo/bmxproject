
## Aug 31, 2017: SignalHound Measurements and Calibration

On Aug 24, 2017, Chris and I configured the SignalHound in order to investigate/study the
broad RFI. Our objective was to obtain spectra from the sky, as well as with the
input terminated at two temperatures (290 K, and
77 K), calculate the gain and noise floor temperature and finally produce a
Calibrated Spectrum.

### Uncalibrated Spectra:

With the SignalHound in place of the spectrometer(PC), we collected 28 spectra
over the course of about 15 minutes. The .bbr file (CREATE LINK) and the log of changes with loose time-stamps
can be found in the SignalHound folder on the cluster. (CREATE LINK)

To decrease noise/eliminate some time variability, we took averages over a few
 spectra.
1.  Spectra from sky
2.  Spectra with input terminated at 290K
3.  Spectra with input terminated at 77K in liquid nitrogen
![spectra](SH_spectrum_mW.png)

### Gain and Noise Floor Calculations:

Power = Gain * (Temperature) + Noise

For a given frequency, a plot of power (mW) versus temperature (K) will be a
line segment, with points at T = 290 K, and T = 77 K. The slope of this line
segment is the gain, and the y-int of the "line" is the noise from the system,
as the temperature approaches T = 0 K.

In python, Chris helped me do some very simple array operations which calculated
the gain (mW/K), and the noise (mW). The ratio n/g then yields the noise
temperature in K.

![Temp](SH_Noise_Temp.png)

### Calibrated Spectra:

Utilizing these values, we calibrate the sky spectra, over the course of a few
minutes. This was taken with the SignalHound, so each color is a different sweep. The resulting plot of sky temperature vs. frequency can be
seen below.

![calspec](SH_fig1.png)